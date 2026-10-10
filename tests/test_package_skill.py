from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import package_skill


class PackageSkillTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.skill = self.root / "skills" / "seedance-2-5"
        (self.skill / "references").mkdir(parents=True)
        (self.skill / "agents").mkdir()
        (self.skill / "assets").mkdir()
        self.description = "Write a video prompt when asked for a Seedance scene."
        self.write_skill()
        (self.skill / "references" / "guide.md").write_text("# Guide\n")
        (self.skill / "assets" / "icon.svg").write_text("<svg/>\n")
        (self.skill / "agents" / "openai.yaml").write_text(
            "interface:\n  icon_small: assets/icon.svg\n  icon_large: assets/icon.svg\n"
        )
        (self.root / "LICENSE").write_text("MIT License\n")
        (self.skill / "LICENSE").write_text("MIT License\n")
        (self.root / "README.md").write_text(
            "[Download](downloads/seedance-2-5.zip?raw=true)\n"
            '<img src="skills/seedance-2-5/assets/icon.svg">\n'
        )
        (self.root / "README.fr.md").write_text("[English](README.md)\n")
        (self.root / "docs").mkdir()
        (self.root / "docs" / "verification.md").write_text("# Checks\n")

    def write_skill(self, name: str = "seedance-2-5") -> None:
        (self.skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: >-\n  {self.description}\n---\n\n"
            "# Skill\n[Guide](references/guide.md)\n"
        )

    def package(self, *, check: bool = False) -> tuple[int, int]:
        return package_skill.run(self.root, check=check)

    def test_archives_match_sources_and_include_license(self) -> None:
        self.package()
        skill_archive = self.root / "downloads" / "seedance-2-5.skill"
        zip_archive = skill_archive.with_suffix(".zip")
        self.assertEqual(skill_archive.read_bytes(), zip_archive.read_bytes())
        with zipfile.ZipFile(zip_archive) as archive:
            self.assertIsNone(archive.testzip())
            for path in self.skill.rglob("*"):
                if path.is_file():
                    name = "seedance-2-5/" + path.relative_to(self.skill).as_posix()
                    self.assertEqual(archive.read(name), path.read_bytes())
            self.assertEqual(
                archive.read("seedance-2-5/LICENSE"),
                (self.root / "LICENSE").read_bytes(),
            )
        self.package(check=True)

    def test_check_never_creates_or_changes_files(self) -> None:
        with self.assertRaises(FileNotFoundError):
            self.package(check=True)
        self.assertFalse((self.root / "downloads").exists())
        self.package()
        before = {
            path: (path.read_bytes(), path.stat().st_mtime_ns)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.package(check=True)
        after = {
            path: (path.read_bytes(), path.stat().st_mtime_ns)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(before, after)

    def test_rebuilding_twice_is_reproducible(self) -> None:
        self.package()
        archive = self.root / "downloads" / "seedance-2-5.zip"
        first = hashlib.sha256(archive.read_bytes()).hexdigest()
        self.package()
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), first)

    def test_changed_source_requires_rebuilding(self) -> None:
        self.package()
        (self.skill / "references" / "guide.md").write_text("# Updated guide\n")
        with self.assertRaisesRegex(ValueError, "Rebuild"):
            self.package(check=True)

    def test_rejects_tampered_and_unsafe_archives(self) -> None:
        self.package()
        archive = self.root / "downloads" / "seedance-2-5.zip"
        for member in ["../outside.txt", "seedance-2-5/unexpected.txt"]:
            with self.subTest(member=member):
                with zipfile.ZipFile(archive, "w") as altered:
                    altered.writestr(member, "unapproved content")
                with self.assertRaisesRegex(ValueError, "Rebuild"):
                    self.package(check=True)

    def test_rejects_symlinks_before_writing_outside_repo(self) -> None:
        outside = self.root / "outside.txt"
        outside.write_text("keep me\n")
        (self.skill / "references" / "linked.md").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.package()
        self.assertEqual(outside.read_text(), "keep me\n")
        self.assertFalse((self.root / "downloads").exists())

    def test_rejects_symlinked_download_destination(self) -> None:
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / "downloads").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.package()
        self.assertEqual(list(outside.iterdir()), [])

    def test_rejects_broken_links_and_paths_outside_bundle(self) -> None:
        for target in ["references/missing.md", "../README.md"]:
            with self.subTest(target=target):
                self.write_skill()
                with (self.skill / "SKILL.md").open("a") as document:
                    document.write(f"[Invalid]({target})\n")
                with self.assertRaises(ValueError):
                    self.package()

    def test_rejects_metadata_name_and_description_errors(self) -> None:
        for name, description in [
            ("another-skill", self.description),
            ("seedance-2-5", ""),
            ("seedance-2-5", "x" * 1025),
            ("seedance-2-5", "<instruction>"),
        ]:
            with self.subTest(name=name, description_length=len(description)):
                self.description = description
                self.write_skill(name)
                with self.assertRaises(ValueError):
                    self.package()

    def test_rejects_missing_icon_and_different_license(self) -> None:
        (self.skill / "agents" / "openai.yaml").write_text(
            "interface:\n  icon_small: assets/missing.svg\n"
        )
        with self.assertRaises(ValueError):
            self.package()
        (self.skill / "agents" / "openai.yaml").write_text("interface:\n")
        (self.skill / "LICENSE").write_text("Another license\n")
        with self.assertRaisesRegex(ValueError, "License"):
            self.package()


if __name__ == "__main__":
    unittest.main()
