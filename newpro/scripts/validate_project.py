#!/usr/bin/env python3
"""Validate the structural contract of a newpro MASTER project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


BASE_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/00_MASTER_BRIEF.md",
    "docs/01_REGISTRE_DES_DECISIONS.md",
    "docs/02_REGISTRE_DES_REJETS.md",
    "docs/03_INVENTAIRE_DES_ASSETS.md",
    "docs/04_BACKLOG_PRIORISE.md",
    "docs/05_CRITERES_D_ACCEPTATION.md",
    "docs/06_RISQUES_ET_INCERTITUDES.md",
    "docs/reprise/IMPORT-MANIFEST.md",
    "docs/reprise/FICHE-DE-TRANSFERT.md",
]

PROFILE_FILES = {
    "software": ["docs/07_ARCHITECTURE_TECHNIQUE.md", "docs/08_CONVENTIONS_DE_CODE.md"],
    "artistic": ["docs/07_DIRECTION_ARTISTIQUE.md", "docs/08_BIBLE_DES_ASSETS.md"],
    "hybrid": [
        "docs/07_ARCHITECTURE_TECHNIQUE.md",
        "docs/08_DIRECTION_ARTISTIQUE.md",
        "docs/09_BIBLE_DES_ASSETS.md",
        "docs/10_CONVENTIONS_DE_CODE.md",
    ],
}

REQUIRED_DIRS = ["docs", "docs/reprise", "assets", "prototype", "src", "tests"]


def load_manifest(root: Path) -> tuple[dict | None, list[str]]:
    path = root / ".newpro-manifest.json"
    if not path.exists():
        return None, ["Manifeste .newpro-manifest.json absent."]
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"Manifeste illisible: {exc}"]


def validate(root: Path, requested_profile: str | None = None) -> dict:
    root = root.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []
    manifest, manifest_issues = load_manifest(root)
    errors.extend(manifest_issues)

    profile = requested_profile or (manifest or {}).get("profile")
    if profile not in PROFILE_FILES:
        errors.append("Profil absent ou invalide; attendu: software, artistic ou hybrid.")
        profile = "software"

    for directory in REQUIRED_DIRS:
        if not (root / directory).is_dir():
            errors.append(f"Dossier requis absent: {directory}/")

    required_files = BASE_FILES + PROFILE_FILES[profile] + ["BOOTSTRAP_REPORT.md"]
    for relative in required_files:
        path = root / relative
        if not path.is_file():
            errors.append(f"Fichier requis absent: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            errors.append(f"Fichier illisible: {relative} ({exc})")
            continue
        if "{{" in text or "}}" in text:
            errors.append(f"Variable de template non resolue: {relative}")

    brief = root / "docs/00_MASTER_BRIEF.md"
    if brief.exists():
        brief_text = brief.read_text(encoding="utf-8", errors="replace")
        for expected in ("Objectif", "Profil", "Tranche verticale", "Production"):
            if expected.lower() not in brief_text.lower():
                warnings.append(f"Le Master Brief ne contient pas de section clairement identifiable: {expected}")

    report = root / "BOOTSTRAP_REPORT.md"
    if report.exists():
        report_text = report.read_text(encoding="utf-8", errors="replace")
        if "Aucune production" not in report_text:
            errors.append("Le rapport ne confirme pas l'absence de production lancee.")

    if manifest:
        if manifest.get("production_started") is not False:
            errors.append("Le manifeste indique que la production a commence.")
        listed = set(manifest.get("generated_files", []))
        missing_from_manifest = [relative for relative in required_files if relative not in listed]
        if missing_from_manifest:
            warnings.append("Fichiers requis absents du manifeste: " + ", ".join(missing_from_manifest))
        if requested_profile and manifest.get("profile") != requested_profile:
            errors.append("Le profil demande ne correspond pas au profil du manifeste.")

    return {
        "status": "valid" if not errors else "invalid",
        "master_root": str(root),
        "profile": profile,
        "errors": errors,
        "warnings": warnings,
        "checked_files": len(required_files),
        "production_started": (manifest or {}).get("production_started", False),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a newpro MASTER project.")
    parser.add_argument("--master", required=True, help="MASTER project directory")
    parser.add_argument("--project-type", choices=["software", "artistic", "hybrid"])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(Path(args.master), requested_profile=args.project_type)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"{result['status'].upper()}: {result['master_root']}")
        for item in result["errors"]:
            print(f"ERROR: {item}")
        for item in result["warnings"]:
            print(f"WARNING: {item}")
        print(f"Checked files: {result['checked_files']}")
    return 0 if result["status"] == "valid" else 1


if __name__ == "__main__":
    raise SystemExit(main())
