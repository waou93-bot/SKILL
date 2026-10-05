#!/usr/bin/env python3
"""Create missing acquisition working documents, never replace an existing project."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from install import no_symlinks


def initialize(root: Path, output: str = "SEO/AI_ACQUISITION", apply: bool = False) -> dict:
    root = root.expanduser().absolute()
    no_symlinks(root, recursive=False)
    if not root.is_dir(): raise ValueError("Project root must already exist")
    relative = Path(output)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Output must be a relative path within the project")
    destination = root / relative
    no_symlinks(destination, recursive=False)
    if destination == root: raise ValueError("Choose a dedicated acquisition subdirectory")
    for candidate in (root / "AI_ACQUISITION", root / "SEO/AI_ACQUISITION", root / "docs/AI_ACQUISITION"):
        if candidate.exists() and candidate != destination:
            raise ValueError(f"Existing acquisition folder: {candidate}; review/reuse before creating another")
    templates = Path(__file__).resolve().parents[1] / "templates/project"
    files = sorted(templates.glob("*.md"))
    if not files: raise ValueError("Project templates missing")
    planned = [f.name for f in files if not (destination / f.name).exists()]
    report = {"mode": "apply" if apply else "dry-run", "destination": str(destination),
              "missing": planned, "preserved": [f.name for f in files if (destination / f.name).exists()], "created": []}
    if apply:
        destination.mkdir(parents=True, exist_ok=True)
        for source in files:
            target = destination / source.name
            try:
                with target.open("x", encoding="utf-8") as handle:
                    handle.write(source.read_text(encoding="utf-8"))
                report["created"].append(source.name)
            except FileExistsError:
                continue
    return report


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--project-root", required=True, type=Path)
    p.add_argument("--output", default="SEO/AI_ACQUISITION")
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    try:
        print(json.dumps(initialize(args.project_root, args.output, args.apply), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    return 2


if __name__ == "__main__": raise SystemExit(main())
