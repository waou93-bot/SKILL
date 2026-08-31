#!/usr/bin/env python3
"""Inspect a project context without modifying it.

The module is intentionally dependency-free so it can run from a personal
Codex skill on a fresh Windows or Unix installation.
"""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".turbo",
    "node_modules",
    "dist",
    "build",
    "out",
    "target",
    "coverage",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
}

SOFTWARE_MARKERS = {
    "package.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "package-lock.json",
    "pyproject.toml",
    "setup.py",
    "requirements.txt",
    "cargo.toml",
    "go.mod",
    "composer.json",
    "pom.xml",
    "build.gradle",
    "makefile",
    "tsconfig.json",
    "next.config.js",
    "next.config.mjs",
    "vite.config.js",
    "vite.config.ts",
}

SOFTWARE_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".css",
    ".go",
    ".h",
    ".html",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".sql",
    ".swift",
    ".tsx",
    ".ts",
    ".vue",
}

ARTISTIC_EXTENSIONS = {
    ".3ds",
    ".aep",
    ".ase",
    ".blend",
    ".fbx",
    ".flac",
    ".gif",
    ".kra",
    ".m4a",
    ".mp3",
    ".mp4",
    ".mov",
    ".ogg",
    ".png",
    ".psd",
    ".svg",
    ".tif",
    ".tiff",
    ".wav",
    ".webm",
    ".webp",
    ".xcf",
}

ARTISTIC_DIR_NAMES = {
    "animation",
    "art",
    "audio",
    "assets",
    "design",
    "footage",
    "media",
    "music",
    "renders",
    "storyboard",
    "video",
    "visuals",
}

GENERIC_NAMES = {".", "", "project", "projet", "workspace", "work", "src", "new"}


def _iter_files(root: Path, max_files: int) -> tuple[list[Path], bool]:
    """Return files and whether the scan was truncated."""

    files: list[Path] = []
    truncated = False
    for current, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = sorted(
            name for name in dirnames if name.lower() not in EXCLUDED_DIRS
        )
        for filename in sorted(filenames):
            path = Path(current) / filename
            if path.is_symlink():
                continue
            files.append(path)
            if len(files) >= max_files:
                truncated = True
                return files, truncated
    return files, truncated


def _read_first_heading(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in text.splitlines()[:30]:
        line = line.strip()
        if line.startswith("# ") and len(line) > 2:
            return line[2:].strip()
    return None


def classify_project(files: Iterable[Path], root: Path) -> dict:
    files = list(files)
    marker_names = {path.name.lower() for path in files}
    extension_counts = Counter(path.suffix.lower() for path in files if path.suffix)
    directory_names = {part.lower() for path in files for part in path.relative_to(root).parts[:-1]}

    software_score = sum(3 for marker in SOFTWARE_MARKERS if marker in marker_names)
    software_score += min(6, sum(extension_counts[ext] for ext in SOFTWARE_EXTENSIONS))
    software_score += sum(1 for name in {"src", "app", "tests", "test"} if name in directory_names)

    artistic_score = min(10, sum(extension_counts[ext] for ext in ARTISTIC_EXTENSIONS))
    artistic_score += sum(2 for name in ARTISTIC_DIR_NAMES if name in directory_names)
    artistic_score += sum(2 for marker in {".blend", ".psd", ".kra", ".aep"} if marker in marker_names)

    if software_score >= 3 and artistic_score >= 3:
        classification = "hybrid"
    elif software_score >= 3 and software_score > artistic_score:
        classification = "software"
    elif artistic_score >= 3 and artistic_score > software_score:
        classification = "artistic"
    else:
        classification = "undetermined"

    evidence: list[str] = []
    for marker in sorted(SOFTWARE_MARKERS & marker_names):
        evidence.append(f"software marker: {marker}")
    for ext in sorted(ARTISTIC_EXTENSIONS):
        count = extension_counts.get(ext, 0)
        if count:
            evidence.append(f"artistic media: {ext} x{count}")
    for name in sorted(ARTISTIC_DIR_NAMES & directory_names):
        evidence.append(f"artistic directory: {name}")

    return {
        "classification": classification,
        "software_score": software_score,
        "artistic_score": artistic_score,
        "evidence": evidence[:40],
    }


def inspect_context(root: Path, max_files: int = 5000) -> dict:
    root = root.expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(f"Context root does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Context root is not a directory: {root}")

    files, truncated = _iter_files(root, max_files)
    relative_files = [path.relative_to(root).as_posix() for path in files]
    extension_counts = Counter(path.suffix.lower() or "[none]" for path in files)
    classification = classify_project(files, root)
    heading = _read_first_heading(root / "README.md") if (root / "README.md").exists() else None
    root_name = root.name.strip()
    name_candidate = root_name if root_name.lower() not in GENERIC_NAMES else None
    suggested_name = name_candidate or heading
    suggested_output = str(root.parent / f"{suggested_name or 'PROJECT'} - MASTER")

    questions: list[str] = []
    optional_followups: list[str] = []
    if not suggested_name:
        questions.append("Quel nom court faut-il donner au projet ?")
    questions.append("Quel resultat principal le projet doit-il produire ?")
    if classification["classification"] == "undetermined":
        questions.append("Le profil est-il logiciel, artistique ou hybride ?")
    if files:
        optional_followups.append(
            "Quels fichiers ou decisions historiques faut-il importer explicitement ? "
            "Par defaut, ils seront seulement inventaries."
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "root_name": root_name,
        "name_candidate": suggested_name,
        "suggested_output": suggested_output,
        "git_detected": (root / ".git").exists(),
        "file_count": len(files),
        "scan_truncated": truncated,
        "extensions": dict(sorted(extension_counts.items())),
        "top_level_entries": sorted(path.name for path in root.iterdir()),
        "files_sample": relative_files[:80],
        "classification": classification,
        "readme_heading": heading,
        "questions": questions,
        "optional_followups": optional_followups,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a project context without modifying it.")
    parser.add_argument("--root", default=".", help="Directory to inspect")
    parser.add_argument("--max-files", type=int, default=5000)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a summary")
    args = parser.parse_args()
    try:
        report = inspect_context(Path(args.root), max_files=max(1, args.max_files))
    except (FileNotFoundError, NotADirectoryError) as exc:
        parser.error(str(exc))
        return 2

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    print(f"Context: {report['root']}")
    print(f"Files inspected: {report['file_count']}" + (" (truncated)" if report["scan_truncated"] else ""))
    print(f"Classification: {report['classification']['classification']}")
    print(f"Suggested MASTER: {report['suggested_output']}")
    if report["classification"]["evidence"]:
        print("Evidence:")
        for item in report["classification"]["evidence"][:12]:
            print(f"- {item}")
    print("Questions:")
    for question in report["questions"]:
        print(f"- {question}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
