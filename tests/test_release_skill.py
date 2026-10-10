from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import package_skill
import release_skill


class FakeGitHub(release_skill.GitHub):
    def __init__(self, root: Path, sha: str) -> None:
        super().__init__(root)
        self.sha = sha
        self.current: release_skill.Release | None = None
        self.tag_commit: str | None = None
        self.contents: dict[str, bytes] = {}
        self.writes: list[str] = []
        self.deny_create = False
        self.interrupt_upload = False
        self.corrupt_upload = False
        self.leave_draft = False
        self.notes = ""

    def release(self, tag: str) -> release_skill.Release | None:
        return self.current

    def tag_sha(self, tag: str) -> str | None:
        return self.tag_commit

    def create(self, tag: str, sha: str, notes: Path) -> None:
        if self.deny_create:
            raise PermissionError("Publication permission denied")
        self.writes.append("create")
        self.notes = notes.read_text()
        self.current = release_skill.Release(7, tag, sha, True, ())

    def upload(self, tag: str, paths: list[Path]) -> None:
        if self.current is None:
            raise AssertionError("No draft")
        for path in paths:
            self.writes.append(f"upload:{path.name}")
            content = path.read_bytes()
            self.contents[path.name] = content
            digest = "sha256:" + hashlib.sha256(content).hexdigest()
            if self.corrupt_upload:
                digest = "sha256:" + "0" * 64
            asset = release_skill.Asset(
                len(self.contents), path.name, len(content), digest
            )
            self.current = replace(self.current, assets=(*self.current.assets, asset))
            if self.interrupt_upload:
                raise OSError("Interrupted after first file")

    def asset_bytes(self, asset: release_skill.Asset) -> bytes:
        return self.contents[asset.name]

    def publish(self, release: release_skill.Release) -> None:
        self.writes.append("publish")
        if not self.leave_draft:
            self.current = replace(release, draft=False)
            self.tag_commit = release.target


class ReleaseSkillTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        files = {
            "LICENSE": "MIT License\n",
            "README.md": "# Skill\n",
            "README.fr.md": "# Skill\n",
            "docs/verification.md": "# Checks\n",
            "skills/seedance-2-5/SKILL.md": "---\nname: seedance-2-5\ndescription: >-\n  Write a video prompt.\n---\n",
            "skills/seedance-2-5/LICENSE": "MIT License\n",
            "skills/seedance-2-5/VERSION": "1.0.0\n",
            "skills/seedance-2-5/agents/openai.yaml": "interface:\n",
            "skills/seedance-2-5/assets/icon.svg": "<svg/>\n",
        }
        for name, content in files.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        package_skill.run(self.root, check=False)
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.commit()
        self.sha = self.git("rev-parse", "HEAD")
        self.environment = {
            "GITHUB_ACTIONS": "true",
            "GITHUB_EVENT_NAME": "push",
            "GITHUB_REF": "refs/heads/main",
            "GITHUB_REPOSITORY": release_skill.REPOSITORY,
            "GITHUB_SHA": self.sha,
            "BASE_SHA": "0" * 40,
        }
        self.github = FakeGitHub(self.root, self.sha)

    def git(self, *arguments: str) -> str:
        return (
            subprocess.check_output(
                ["git", *arguments], cwd=self.root, stderr=subprocess.PIPE
            )
            .decode()
            .strip()
        )

    def commit(self) -> None:
        if hasattr(self, "environment"):
            self.environment["BASE_SHA"] = self.git("rev-parse", "HEAD")
        self.git(
            "add", "LICENSE", "README.md", "README.fr.md", "docs", "skills", "downloads"
        )
        self.git("commit", "-m", "Test fixture")

    def publish(self) -> str:
        return release_skill.publish(self.root, self.environment, self.github)

    def seed_release(self, *, draft: bool = False) -> None:
        expected = release_skill.expected_assets(self.root)
        self.github.contents = expected.copy()
        assets = tuple(
            release_skill.Asset(
                index,
                name,
                len(content),
                "sha256:" + hashlib.sha256(content).hexdigest(),
            )
            for index, (name, content) in enumerate(expected.items(), start=1)
        )
        self.github.current = release_skill.Release(
            7, "v1.0.0", self.sha, draft, assets
        )
        self.github.tag_commit = self.sha

    def test_first_publication_verifies_commit_files_and_notes(self) -> None:
        result = self.publish()
        self.assertIn(f"Published v1.0.0 at {self.sha}", result)
        self.assertEqual(
            self.github.writes,
            [
                "create",
                "upload:seedance-2-5.skill",
                "upload:seedance-2-5.zip",
                "upload:SHA256SUMS",
                "publish",
            ],
        )
        self.assertIn(self.sha, self.github.notes)
        self.assertIn("1.0.0", self.github.notes)
        self.assertEqual(self.github.tag_commit, self.sha)
        self.assertEqual(
            self.github.contents["seedance-2-5.skill"],
            self.github.contents["seedance-2-5.zip"],
        )
        for line in self.github.contents["SHA256SUMS"].decode().splitlines():
            digest, name = line.split("  ")
            self.assertEqual(
                hashlib.sha256(self.github.contents[name]).hexdigest(), digest
            )
        self.assertEqual(release_skill.expected_assets(self.root), self.github.contents)

    def test_already_published_is_verified_without_writes(self) -> None:
        self.seed_release()
        self.assertIn("Already published v1.0.0", self.publish())
        self.assertEqual(self.github.writes, [])

    def test_docs_only_commit_does_not_republish_same_version(self) -> None:
        self.seed_release()
        (self.root / "README.md").write_text("# Improved documentation\n")
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        self.assertIn(f"at {self.sha}", self.publish())
        self.assertEqual(self.github.writes, [])

    def test_same_version_with_changed_skill_fails_before_writes(self) -> None:
        (self.root / "skills/seedance-2-5/assets/icon.svg").write_text(
            "<svg>changed</svg>\n"
        )
        package_skill.run(self.root, check=False)
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        with self.assertRaisesRegex(ValueError, "higher VERSION"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_lower_version_fails_before_writes(self) -> None:
        (self.root / release_skill.VERSION_PATH).write_text("0.9.0\n")
        package_skill.run(self.root, check=False)
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        with self.assertRaisesRegex(ValueError, "backwards"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_lower_version_before_docs_commit_fails_before_writes(self) -> None:
        (self.root / release_skill.VERSION_PATH).write_text("0.9.0\n")
        package_skill.run(self.root, check=False)
        self.commit()
        (self.root / "README.md").write_text("# Improved documentation\n")
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        self.environment["BASE_SHA"] = self.sha
        with self.assertRaisesRegex(ValueError, "backwards"):
            release_skill.check_transition(self.root, self.sha)
        with self.assertRaisesRegex(ValueError, "backwards"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_changed_skill_before_docs_commit_requires_higher_version(self) -> None:
        (self.root / "skills/seedance-2-5/assets/icon.svg").write_text(
            "<svg>changed</svg>\n"
        )
        package_skill.run(self.root, check=False)
        self.commit()
        (self.root / "README.md").write_text("# Improved documentation\n")
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        self.environment["BASE_SHA"] = self.sha
        with self.assertRaisesRegex(ValueError, "higher VERSION"):
            release_skill.check_transition(self.root, self.sha)
        with self.assertRaisesRegex(ValueError, "higher VERSION"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_higher_version_before_docs_commit_can_publish(self) -> None:
        (self.root / release_skill.VERSION_PATH).write_text("1.1.0\n")
        package_skill.run(self.root, check=False)
        self.commit()
        (self.root / "README.md").write_text("# Improved documentation\n")
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        self.environment["BASE_SHA"] = self.sha
        self.github.sha = self.environment["GITHUB_SHA"]
        self.assertEqual(release_skill.check_transition(self.root, self.sha), "1.1.0")
        self.assertIn("Published v1.1.0", self.publish())
        self.assertEqual(self.github.tag_commit, self.environment["GITHUB_SHA"])

    def test_publication_rejects_missing_empty_invalid_or_unknown_base(self) -> None:
        for base in (None, "", "--invalid", "f" * 40):
            with self.subTest(base=base):
                environment = self.environment.copy()
                if base is None:
                    environment.pop("BASE_SHA")
                else:
                    environment["BASE_SHA"] = base
                github = FakeGitHub(self.root, self.sha)
                error = RuntimeError if base == "f" * 40 else ValueError
                with self.assertRaises(error):
                    release_skill.publish(self.root, environment, github)
                self.assertEqual(github.writes, [])

    def test_initial_push_without_previous_ref_can_publish(self) -> None:
        self.assertEqual(release_skill.check_transition(self.root, "0" * 40), "1.0.0")
        self.assertIn("Published v1.0.0", self.publish())
        self.assertEqual(self.github.tag_commit, self.sha)

    def test_higher_version_and_explicit_pr_base_are_accepted(self) -> None:
        (self.root / release_skill.VERSION_PATH).write_text("1.1.0\n")
        package_skill.run(self.root, check=False)
        self.assertEqual(release_skill.check_transition(self.root, self.sha), "1.1.0")
        with self.assertRaisesRegex(ValueError, "full commit SHA"):
            release_skill.check_transition(self.root, "--invalid")

    def test_version_check_never_changes_files_or_git_index(self) -> None:
        (self.root / release_skill.VERSION_PATH).write_text("1.1.0\n")
        package_skill.run(self.root, check=False)
        before = {
            path: (path.read_bytes(), path.stat().st_mtime_ns)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(release_skill.check_transition(self.root, self.sha), "1.1.0")
        after = {
            path: (path.read_bytes(), path.stat().st_mtime_ns)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(before, after)

    def test_wrong_context_or_commit_fails_before_writes(self) -> None:
        for key, value in [
            ("GITHUB_ACTIONS", "false"),
            ("GITHUB_EVENT_NAME", "pull_request"),
            ("GITHUB_REF", "refs/heads/feature"),
            ("GITHUB_REPOSITORY", "someone/seedance-2-5"),
            ("GITHUB_SHA", "0" * 40),
            ("GITHUB_SHA", "main"),
        ]:
            with self.subTest(key=key, value=value):
                environment = {**self.environment, key: value}
                with self.assertRaises(ValueError):
                    release_skill.publish(self.root, environment, self.github)
        self.assertEqual(self.github.writes, [])

    def test_uncommitted_and_untracked_payload_is_rejected(self) -> None:
        for name in ["assets/icon.svg", "extra.txt"]:
            with self.subTest(name=name):
                path = self.root / "skills/seedance-2-5" / name
                original = path.read_bytes() if path.exists() else None
                path.write_text("uncommitted")
                with self.assertRaisesRegex(ValueError, "committed"):
                    self.publish()
                if original is None:
                    path.unlink()
                else:
                    path.write_bytes(original)
        self.assertEqual(self.github.writes, [])

    def test_collision_with_different_tag_payload_fails_without_writes(self) -> None:
        old_sha = self.sha
        (self.root / release_skill.VERSION_PATH).write_text("1.1.0\n")
        package_skill.run(self.root, check=False)
        self.commit()
        self.environment["GITHUB_SHA"] = self.git("rev-parse", "HEAD")
        self.github.tag_commit = old_sha
        with self.assertRaisesRegex(ValueError, "different skill"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_interrupted_upload_resumes_without_replacing_files(self) -> None:
        self.github.interrupt_upload = True
        with self.assertRaisesRegex(OSError, "Interrupted"):
            self.publish()
        first_file = self.github.contents["seedance-2-5.skill"]
        self.github.interrupt_upload = False
        self.github.writes.clear()
        self.assertIn("Published", self.publish())
        self.assertEqual(
            self.github.writes,
            [
                "upload:seedance-2-5.zip",
                "upload:SHA256SUMS",
                "publish",
            ],
        )
        self.assertEqual(self.github.contents["seedance-2-5.skill"], first_file)

    def test_complete_draft_resumes_without_upload(self) -> None:
        self.seed_release(draft=True)
        self.assertIn("Published", self.publish())
        self.assertEqual(self.github.writes, ["publish"])

    def test_draft_from_another_commit_is_not_mutated(self) -> None:
        self.seed_release(draft=True)
        if self.github.current is None:
            self.fail("Missing fixture")
        self.github.current = replace(self.github.current, target="0" * 40)
        with self.assertRaisesRegex(ValueError, "another commit"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_existing_asset_digest_and_bytes_are_both_checked(self) -> None:
        for change in ["digest", "bytes"]:
            with self.subTest(change=change):
                self.seed_release(draft=True)
                if self.github.current is None:
                    self.fail("Missing fixture")
                asset = self.github.current.assets[0]
                if change == "digest":
                    bad = replace(asset, digest="sha256:" + "0" * 64)
                    self.github.current = replace(
                        self.github.current,
                        assets=(bad, *self.github.current.assets[1:]),
                    )
                else:
                    self.github.contents[asset.name] = b"x" * asset.size
                with self.assertRaisesRegex(ValueError, "differs|differ"):
                    self.publish()
                self.assertEqual(self.github.writes, [])

    def test_missing_digest_still_requires_matching_downloaded_bytes(self) -> None:
        self.seed_release()
        if self.github.current is None:
            self.fail("Missing fixture")
        self.github.current = replace(
            self.github.current,
            assets=tuple(
                replace(asset, digest=None) for asset in self.github.current.assets
            ),
        )
        self.assertIn("Already published", self.publish())
        self.github.contents["seedance-2-5.zip"] = b"tampered"
        with self.assertRaisesRegex(ValueError, "bytes differ"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_corrupted_upload_stops_before_publication(self) -> None:
        self.github.corrupt_upload = True
        with self.assertRaisesRegex(ValueError, "metadata differs"):
            self.publish()
        self.assertNotIn("publish", self.github.writes)

    def test_permission_failure_does_not_become_success(self) -> None:
        self.github.deny_create = True
        with self.assertRaisesRegex(PermissionError, "permission"):
            self.publish()
        self.assertEqual(self.github.writes, [])
        self.assertIsNone(self.github.current)

    def test_draft_or_tag_alone_does_not_count_as_published(self) -> None:
        self.github.tag_commit = self.sha
        self.github.leave_draft = True
        with self.assertRaisesRegex(ValueError, "not publicly published"):
            self.publish()
        self.assertIsNotNone(self.github.current)

    def test_published_release_without_tag_is_not_accepted(self) -> None:
        self.seed_release()
        self.github.tag_commit = None
        with self.assertRaisesRegex(ValueError, "no commit tag"):
            self.publish()
        self.assertEqual(self.github.writes, [])

    def test_github_commands_bind_commit_repo_and_native_latest_policy(self) -> None:
        github = release_skill.GitHub(self.root)
        notes = self.root / "notes.md"
        notes.write_text("Notes")
        with patch.object(release_skill, "command", return_value=b"") as run:
            github.create("v1.0.0", self.sha, notes)
            args = run.call_args.args[0]
            self.assertEqual(args[args.index("--target") + 1], self.sha)
            self.assertEqual(args[args.index("--repo") + 1], release_skill.REPOSITORY)
            self.assertIn("--draft", args)
            self.assertIn("--generate-notes", args)
            github.upload("v1.0.0", [notes])
            self.assertNotIn("--clobber", run.call_args.args[0])
            github.publish(release_skill.Release(7, "v1.0.0", self.sha, True, ()))
            request = json.loads(run.call_args.args[2])
            self.assertEqual(request, {"draft": False, "make_latest": "legacy"})

    def test_github_read_failure_never_creates_a_release(self) -> None:
        github = release_skill.GitHub(self.root)
        with patch.object(github, "api", side_effect=RuntimeError("HTTP 403")) as read:
            with self.assertRaisesRegex(RuntimeError, "403"):
                release_skill.publish(self.root, self.environment, github)
            read.assert_called_once_with(
                f"repos/{release_skill.REPOSITORY}/releases?per_page=100",
                "--paginate",
                "--slurp",
            )

    def test_tag_lookup_handles_exact_names_and_annotated_tags(self) -> None:
        github = release_skill.GitHub(self.root)
        tag_object = "a" * 40
        refs = [
            {"ref": "refs/tags/v1.0.00", "object": {"type": "commit", "sha": "b" * 40}},
            {"ref": "refs/tags/v1.0.0", "object": {"type": "tag", "sha": tag_object}},
        ]
        with patch.object(
            github,
            "api",
            side_effect=[
                refs,
                {"object": {"type": "commit", "sha": self.sha}},
            ],
        ):
            self.assertEqual(github.tag_sha("v1.0.0"), self.sha)
        with patch.object(github, "api", return_value=refs[:1]):
            self.assertIsNone(github.tag_sha("v1.0.0"))

    def test_malformed_or_incomplete_github_responses_are_rejected(self) -> None:
        for response in [None, {}, {"draft": False, "assets": "missing"}]:
            with self.subTest(response=response):
                with self.assertRaises(ValueError):
                    release_skill.parse_release(response)

    def test_paginated_release_and_incomplete_upload_are_checked(self) -> None:
        github = release_skill.GitHub(self.root)
        response = {
            "id": 7,
            "tag_name": "v1.0.0",
            "target_commitish": self.sha,
            "draft": True,
            "assets": [
                {
                    "id": 1,
                    "name": "SHA256SUMS",
                    "size": 0,
                    "digest": None,
                    "state": "uploaded",
                },
            ],
        }
        with patch.object(github, "api", return_value=[[], [response]]):
            found = github.release("v1.0.0")
            self.assertIsNotNone(found)
            if found is None:
                self.fail("Missing release")
            self.assertEqual(found.assets[0].digest, None)
        with patch.object(github, "api", return_value=[[response], [response]]):
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                github.release("v1.0.0")
        incomplete = {
            **response,
            "assets": [
                {
                    "id": 1,
                    "name": "SHA256SUMS",
                    "size": 0,
                    "digest": None,
                    "state": "starter",
                },
            ],
        }
        with self.assertRaisesRegex(ValueError, "incomplete"):
            release_skill.parse_release(incomplete)


if __name__ == "__main__":
    unittest.main()
