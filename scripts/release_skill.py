"""Check version transitions or publish a verified release from GitHub Actions."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

import package_skill

REPOSITORY = "MMMProd-Org/seedance-2-5"
VERSION_PATH = f"skills/{package_skill.SKILL_NAME}/VERSION"
PAYLOAD_PATHS = [
    f"skills/{package_skill.SKILL_NAME}",
    f"downloads/{package_skill.SKILL_NAME}.skill",
    f"downloads/{package_skill.SKILL_NAME}.zip",
]


def command(args: list[str], root: Path, content: bytes | None = None) -> bytes:
    result = subprocess.run(args, cwd=root, input=content, capture_output=True)
    if result.returncode:
        # Do not echo authentication details returned by an external command.
        operation = " ".join(args[:4])
        raise RuntimeError(f"{operation} failed (exit {result.returncode})")
    return result.stdout


def git(root: Path, *args: str) -> str:
    return command(["git", *args], root).decode("utf-8").strip()


def object_fields(value: object) -> dict[str, object]:
    if not isinstance(value, dict) or any(not isinstance(key, str) for key in value):
        raise ValueError("Invalid GitHub object")
    return {key: item for key, item in value.items()}


def text_field(value: dict[str, object], name: str) -> str:
    field = value.get(name)
    if not isinstance(field, str):
        raise ValueError(f"Invalid GitHub field: {name}")
    return field


def number_field(value: dict[str, object], name: str) -> int:
    field = value.get(name)
    if type(field) is not int or field < 0:
        raise ValueError(f"Invalid GitHub field: {name}")
    return field


@dataclass(frozen=True)
class Asset:
    id: int
    name: str
    size: int
    digest: str | None


@dataclass(frozen=True)
class Release:
    id: int
    tag: str
    target: str
    draft: bool
    assets: tuple[Asset, ...]


def parse_release(value: object) -> Release:
    fields = object_fields(value)
    draft = fields.get("draft")
    raw_assets = fields.get("assets")
    if not isinstance(draft, bool) or not isinstance(raw_assets, list):
        raise ValueError("Invalid release state or assets")
    assets = []
    for value in raw_assets:
        asset = object_fields(value)
        digest = asset.get("digest")
        if digest is not None and not isinstance(digest, str):
            raise ValueError("Invalid asset digest")
        if asset.get("state") != "uploaded":
            raise ValueError("Asset upload is incomplete")
        assets.append(
            Asset(
                number_field(asset, "id"),
                text_field(asset, "name"),
                number_field(asset, "size"),
                digest,
            )
        )
    return Release(
        number_field(fields, "id"),
        text_field(fields, "tag_name"),
        text_field(fields, "target_commitish"),
        draft,
        tuple(assets),
    )


class GitHub:
    def __init__(self, root: Path) -> None:
        self.root = root

    def api(self, path: str, *options: str) -> object:
        return json.loads(command(["gh", "api", path, *options], self.root))

    def release(self, tag: str) -> Release | None:
        pages = self.api(
            f"repos/{REPOSITORY}/releases?per_page=100", "--paginate", "--slurp"
        )
        if not isinstance(pages, list):
            raise ValueError("Invalid release listing")
        matches = []
        for page in pages:
            if not isinstance(page, list):
                raise ValueError("Invalid release page")
            for item in page:
                fields = object_fields(item)
                if fields.get("tag_name") == tag:
                    matches.append(parse_release(fields))
        if len(matches) > 1:
            raise ValueError("Duplicate release tag")
        return matches[0] if matches else None

    def tag_sha(self, tag: str) -> str | None:
        refs = self.api(f"repos/{REPOSITORY}/git/matching-refs/tags/{tag}")
        if not isinstance(refs, list):
            raise ValueError("Invalid tag listing")
        matches = [
            object_fields(item)
            for item in refs
            if object_fields(item).get("ref") == f"refs/tags/{tag}"
        ]
        if len(matches) > 1:
            raise ValueError("Duplicate tag")
        if not matches:
            return None
        target = object_fields(matches[0].get("object"))
        seen: set[str] = set()
        while True:
            sha = text_field(target, "sha")
            if re.fullmatch(r"[0-9a-f]{40}", sha) is None or sha in seen:
                raise ValueError("Invalid or cyclic tag target")
            seen.add(sha)
            if target.get("type") == "commit":
                return sha
            if target.get("type") != "tag" or len(seen) > 8:
                raise ValueError("Tag must resolve to a commit")
            annotated = object_fields(self.api(f"repos/{REPOSITORY}/git/tags/{sha}"))
            target = object_fields(annotated.get("object"))

    def create(self, tag: str, sha: str, notes: Path) -> None:
        command(
            [
                "gh",
                "release",
                "create",
                tag,
                "--repo",
                REPOSITORY,
                "--target",
                sha,
                "--draft",
                "--title",
                f"Seedance skill {tag}",
                "--generate-notes",
                "--notes-file",
                str(notes),
            ],
            self.root,
        )

    def upload(self, tag: str, paths: list[Path]) -> None:
        command(
            ["gh", "release", "upload", tag, "--repo", REPOSITORY, *map(str, paths)],
            self.root,
        )

    def asset_bytes(self, asset: Asset) -> bytes:
        return command(
            [
                "gh",
                "api",
                f"repos/{REPOSITORY}/releases/assets/{asset.id}",
                "-H",
                "Accept: application/octet-stream",
            ],
            self.root,
        )

    def publish(self, release: Release) -> None:
        command(
            [
                "gh",
                "api",
                f"repos/{REPOSITORY}/releases/{release.id}",
                "--method",
                "PATCH",
                "--input",
                "-",
            ],
            self.root,
            json.dumps({"draft": False, "make_latest": "legacy"}).encode(),
        )


def check_transition(root: Path, base: str | None = None) -> str:
    package_skill.run(root, check=True)
    version = package_skill.read_version(root)
    if base == "0" * 40:
        return version
    if not base:
        parents = git(root, "rev-list", "--parents", "-n", "1", "HEAD").split()
        base = parents[1] if len(parents) > 1 else None
    if base is None:
        return version
    if re.fullmatch(r"[0-9a-f]{40}", base) is None:
        raise ValueError("Base must be a full commit SHA")
    previous = git(root, "ls-tree", "--name-only", base, "--", VERSION_PATH)
    if not previous:
        return version
    old = package_skill.parse_version(
        command(["git", "show", f"{base}:{VERSION_PATH}"], root)
    )
    current_number = tuple(int(part) for part in version.split("."))
    old_number = tuple(int(part) for part in old.split("."))
    changed = git(root, "diff", "--name-only", base, "--", *PAYLOAD_PATHS)
    if current_number < old_number:
        raise ValueError("VERSION cannot go backwards")
    if changed and current_number == old_number:
        raise ValueError("Changed skill or downloads require a higher VERSION")
    return version


def checked_commit(root: Path, environment: Mapping[str, str]) -> str:
    required = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "push",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_REPOSITORY": REPOSITORY,
    }
    if any(environment.get(key) != value for key, value in required.items()):
        raise ValueError("Publication is restricted to this repository's main push")
    sha = environment.get("GITHUB_SHA", "")
    if (
        re.fullmatch(r"[0-9a-f]{40}", sha) is None
        or git(root, "rev-parse", "HEAD") != sha
    ):
        raise ValueError("Checkout does not match the checked commit")
    if git(
        root, "status", "--porcelain", "--untracked-files=all", "--", *PAYLOAD_PATHS
    ):
        raise ValueError("Publication payload must be committed and unchanged")
    return sha


def expected_assets(root: Path) -> dict[str, bytes]:
    assets = {
        f"{package_skill.SKILL_NAME}{suffix}": (
            root / "downloads" / f"{package_skill.SKILL_NAME}{suffix}"
        ).read_bytes()
        for suffix in [".skill", ".zip"]
    }
    assets["SHA256SUMS"] = "".join(
        f"{hashlib.sha256(content).hexdigest()}  {name}\n"
        for name, content in sorted(assets.items())
    ).encode()
    return assets


def verify_assets(
    github: GitHub, release: Release, expected: dict[str, bytes], *, complete: bool
) -> None:
    names = [asset.name for asset in release.assets]
    if len(set(names)) != len(names) or set(names) - expected.keys():
        raise ValueError("Duplicate or unexpected release assets")
    if complete and set(names) != expected.keys():
        raise ValueError("Release assets are missing")
    for asset in release.assets:
        content = expected[asset.name]
        digest = "sha256:" + hashlib.sha256(content).hexdigest()
        if asset.size != len(content) or asset.digest not in {None, digest}:
            raise ValueError(f"Release asset metadata differs: {asset.name}")
        if github.asset_bytes(asset) != content:
            raise ValueError(f"Release asset bytes differ: {asset.name}")


def publish(root: Path, environment: Mapping[str, str], github: GitHub) -> str:
    sha = checked_commit(root, environment)
    base = environment.get("BASE_SHA", "")
    if not base:
        raise ValueError("Publication requires BASE_SHA from the push event")
    version = check_transition(root, base)
    tag = f"v{version}"
    expected = expected_assets(root)
    release = github.release(tag)
    tag_sha = github.tag_sha(tag)
    if tag_sha is not None and git(
        root, "diff", "--name-only", tag_sha, "--", *PAYLOAD_PATHS
    ):
        raise ValueError("Existing tag contains a different skill or download")
    if release is not None:
        verify_assets(github, release, expected, complete=not release.draft)
        if not release.draft:
            if tag_sha is None:
                raise ValueError("Published release has no commit tag")
            return f"Already published {tag} at {tag_sha}; files verified"
        if release.target != sha or (tag_sha is not None and tag_sha != sha):
            raise ValueError("Draft belongs to another commit; rerun its original job")
    elif tag_sha is not None and tag_sha != sha:
        raise ValueError("Existing tag belongs to another commit")

    with tempfile.TemporaryDirectory(prefix="seedance-release-") as directory:
        staging = Path(directory)
        if release is None:
            notes = staging / "notes.md"
            notes.write_text(
                f"Skill version: **{version}** (target model: 2.5).\n\n"
                f"Checked commit: {sha}\n\n"
                "Download the ZIP or .skill; both contain the same files. "
                "VERSION identifies the installed skill. SHA256SUMS verifies the downloads.\n",
                encoding="utf-8",
            )
            github.create(tag, sha, notes)
            release = github.release(tag)
        if release is None or not release.draft or release.target != sha:
            raise ValueError("Expected draft for the checked commit")
        verify_assets(github, release, expected, complete=False)
        present = {asset.name for asset in release.assets}
        missing = []
        for name, content in expected.items():
            if name not in present:
                path = staging / name
                path.write_bytes(content)
                missing.append(path)
        if missing:
            github.upload(tag, missing)
        uploaded = github.release(tag)
        if (
            uploaded is None
            or not uploaded.draft
            or uploaded.id != release.id
            or uploaded.target != sha
        ):
            raise ValueError("Draft changed during upload")
        verify_assets(github, uploaded, expected, complete=True)
        tag_sha = github.tag_sha(tag)
        if tag_sha is not None and tag_sha != sha:
            raise ValueError("Tag changed before publication")
        github.publish(uploaded)
    published = github.release(tag)
    if published is None or published.draft or published.id != release.id:
        raise ValueError("Release is not publicly published")
    if github.tag_sha(tag) != sha:
        raise ValueError("Published tag does not match the checked commit")
    verify_assets(github, published, expected, complete=True)
    return f"Published {tag} at {sha}; tag and all three files verified"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Check locally without network or writes"
    )
    parser.add_argument(
        "--base",
        default="",
        help="Comparison base commit SHA; otherwise use HEAD's first parent",
    )
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        if arguments.check:
            print(check_transition(root, arguments.base or None))
        else:
            if arguments.base:
                raise ValueError("--base is only valid with --check")
            print(publish(root, os.environ, GitHub(root)))
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, f"ERROR: {error}\n")


if __name__ == "__main__":
    main()
