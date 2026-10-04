#!/usr/bin/env python3
"""Install one ai-seo folder. Dry-run by default; reviewed upgrades get a verified backup."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", ".git")


def no_symlinks(path: Path, recursive: bool = True) -> None:
    for candidate in (path, *path.parents):
        if candidate.is_symlink(): raise ValueError(f"Symlink path refused: {candidate}")
    if recursive and path.exists() and path.is_dir():
        for candidate in path.rglob("*"):
            if candidate.is_symlink(): raise ValueError(f"Symlink content refused: {candidate}")


def inventory(root: Path) -> dict[str, str]:
    output = {}
    if not root.exists(): return output
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in ("__pycache__", ".git") for part in relative.parts) or path.suffix == ".pyc" or path.name == ".DS_Store": continue
        if path.is_file(): output[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return output


def install(source: Path, target: Path, backup_root: Path, apply: bool = False, upgrade_reviewed: bool = False) -> dict:
    source, target, backup_root = (p.expanduser().absolute() for p in (source, target, backup_root))
    for path in (source, target, backup_root): no_symlinks(path)
    source, target, backup_root = (p.resolve() for p in (source, target, backup_root))
    if target.name != "ai-seo" or not (source / "SKILL.md").is_file():
        raise ValueError("Source needs SKILL.md and target must end in ai-seo")
    if source == target or source in target.parents or target in source.parents:
        raise ValueError("Source and target must be separate, non-nested directories")
    if target.exists() and not target.is_dir(): raise ValueError("Target is not a directory")
    if backup_root == target.parent or target.parent in backup_root.parents or backup_root == target or backup_root in target.parents:
        raise ValueError("Backup root must be outside the active skills directory and not an ancestor of target")
    before, incoming = inventory(target), inventory(source)
    report = {"mode": "apply" if apply else "dry-run", "target": str(target),
              "added": sorted(incoming.keys() - before.keys()),
              "removed": sorted(before.keys() - incoming.keys()),
              "changed": sorted(k for k in before.keys() & incoming.keys() if before[k] != incoming[k]),
              "backup": None, "host_discovery_verified": False}
    if not apply: return report
    if target.exists() and not upgrade_reviewed:
        raise ValueError("Existing target: review customizations, then use --upgrade-reviewed")
    target.parent.mkdir(parents=True, exist_ok=True)
    lock = target.parent / ".ai-seo-install.lock"
    with lock.open("x", encoding="utf-8") as handle: handle.write("ai-seo install in progress\n")
    backup: Path | None = None
    changed = False
    try:
        with tempfile.TemporaryDirectory(prefix=".ai-seo-stage-", dir=target.parent) as stage_dir:
            stage = Path(stage_dir) / "payload"
            shutil.copytree(source, stage, ignore=IGNORE)
            if inventory(stage) != incoming: raise RuntimeError("Staging verification failed")
            if inventory(target) != before: raise RuntimeError("Target changed during preparation")
            if target.exists():
                backup_root.mkdir(parents=True, exist_ok=True)
                stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
                backup = backup_root / ("ai-seo-" + stamp)
                shutil.copytree(target, backup, ignore=IGNORE)
                if inventory(backup) != before: raise RuntimeError("Backup verification failed")
                report["backup"] = str(backup)
                changed = True
                shutil.rmtree(target)
            else:
                changed = True
            stage.rename(target)
            if inventory(target) != incoming: raise RuntimeError("Installed file verification failed")
    except Exception:
        if changed:
            if target.exists(): shutil.rmtree(target)
            if backup is not None and backup.exists(): shutil.copytree(backup, target)
        raise
    finally:
        lock.unlink(missing_ok=True)
    report["file_integrity_verified"] = True
    return report


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--target", type=Path, default=Path.home() / ".agents/skills/ai-seo")
    p.add_argument("--backup-root", type=Path, default=Path.home() / ".ai-seo-backups")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--upgrade-reviewed", action="store_true")
    args = p.parse_args()
    try:
        print(json.dumps(install(Path(__file__).resolve().parents[1], args.target, args.backup_root,
                                 args.apply, args.upgrade_reviewed), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        p.error(str(exc))
    return 2


if __name__ == "__main__": raise SystemExit(main())
