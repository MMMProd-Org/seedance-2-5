"""Build or check the portable skill using only the Python standard library."""

from __future__ import annotations

import argparse
import io
import re
import stat
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKILL_NAME = "seedance-2-5"


def local_target(document: Path, target: str, boundary: Path) -> Path | None:
    address = urlsplit(target.strip("<>"))
    if address.scheme or address.netloc or not address.path:
        return None
    path = (document.parent / unquote(address.path)).resolve()
    if not path.is_relative_to(boundary.resolve()) or not path.exists():
        raise ValueError(f"Invalid local link in {document.name}: {target}")
    return path


def check_links(document: Path, boundary: Path) -> int:
    text = document.read_text(encoding="utf-8")
    # shortcut: inline Markdown and HTML links only; extend if other forms appear.
    targets = re.findall(r"!?\[[^\]\n]*\]\(([^)\s]+)(?:\s+[^)]*)?\)", text)
    targets += re.findall(r"\b(?:href|src)=[\"']([^\"']+)[\"']", text)
    return sum(
        local_target(document, target, boundary) is not None for target in targets
    )


def collect_source(root: Path) -> tuple[dict[str, bytes], int]:
    source = root / "skills" / SKILL_NAME
    if source.is_symlink() or not source.resolve().is_relative_to(root.resolve()):
        raise ValueError("Symlink or source path outside repository")
    files: dict[str, bytes] = {}
    links = 0
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink in skill source: {path.name}")
        relative = path.relative_to(source)
        if any(
            part.startswith(".") or "\\" in part or ":" in part
            for part in relative.parts
        ):
            raise ValueError(f"Unsafe source path: {relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError(f"Not a regular source file: {relative}")
        files[f"{SKILL_NAME}/{relative.as_posix()}"] = path.read_bytes()
        if path.suffix == ".md":
            links += check_links(path, source)
    required = ["SKILL.md", "LICENSE", "agents/openai.yaml", "assets/icon.svg"]
    if any(f"{SKILL_NAME}/{name}" not in files for name in required):
        raise ValueError("Missing required skill file")
    skill = files[f"{SKILL_NAME}/SKILL.md"].decode("utf-8")
    # shortcut: this skill uses a folded description; extend before changing YAML shape.
    metadata = re.match(
        r"\A---\nname: ([a-z0-9-]+)\ndescription: >-\n((?:  [^\n]*\n)+)---\n",
        skill,
    )
    if metadata is None or metadata[1] != SKILL_NAME:
        raise ValueError("Invalid skill metadata or folder/name mismatch")
    description = " ".join(line.strip() for line in metadata[2].splitlines()).strip()
    if (
        not description
        or len(description) > 1024
        or "<" in description
        or ">" in description
    ):
        raise ValueError("Description must contain 1–1024 characters without XML tags")
    license_path = root / "LICENSE"
    if (
        license_path.is_symlink()
        or files[f"{SKILL_NAME}/LICENSE"] != license_path.read_bytes()
    ):
        raise ValueError("License in skill must match repository LICENSE")
    icons = re.findall(
        r"^\s+icon_(?:small|large):\s*(.+?)\s*$",
        files[f"{SKILL_NAME}/agents/openai.yaml"].decode("utf-8"),
        re.MULTILINE,
    )
    for icon in icons:
        icon_path = local_target(
            source / "agents/openai.yaml", "../" + icon.strip("\"'"), source
        )
        if icon_path is None or not icon_path.is_file():
            raise ValueError("Icon must refer to a file within the skill")
    return files, links


def build_archive(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    # Stored entries avoid differences between compression library versions.
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, content)
    return buffer.getvalue()


def run(root: Path, *, check: bool) -> tuple[int, int]:
    files, links = collect_source(root)
    content = build_archive(files)
    downloads = root / "downloads"
    destinations = [
        downloads / f"{SKILL_NAME}{suffix}" for suffix in [".skill", ".zip"]
    ]
    if downloads.is_symlink() or any(path.is_symlink() for path in destinations):
        raise ValueError("Symlink in download destination")
    if check:
        for path in destinations:
            if path.read_bytes() != content:
                raise ValueError(f"Rebuild {path.name}: archive differs from source")
    else:
        downloads.mkdir(exist_ok=True)
        for path in destinations:
            path.write_bytes(content)
    for name in ["README.md", "README.fr.md", "docs/verification.md"]:
        links += check_links(root / name, root)
    return len(files), links


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Validate without writing files"
    )
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        files, links = run(root, check=arguments.check)
    except (OSError, ValueError) as error:
        parser.exit(1, f"ERROR: {error}\n")
    operation = "checked" if arguments.check else "built"
    print(f"OK: {files} source files; {links} local links; .skill and .zip {operation}")


if __name__ == "__main__":
    main()
