#!/usr/bin/env python3
"""Create an idempotent MASTER project skeleton from an inspected context."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from inspect_context import inspect_context
    from asset_registry import load_registry, search_entries
except ImportError:  # pragma: no cover - useful when imported from elsewhere
    from scripts.inspect_context import inspect_context
    from scripts.asset_registry import load_registry, search_entries


VERSION = "1.1.0"
PROFILES = {"software", "artistic", "hybrid"}

BASE_FILES = [
    ("README.md", "README.md"),
    ("AGENTS.md", "AGENTS.md"),
    ("docs/00_MASTER_BRIEF.md", "MASTER_BRIEF.md"),
    ("docs/01_REGISTRE_DES_DECISIONS.md", "DECISIONS.md"),
    ("docs/02_REGISTRE_DES_REJETS.md", "REJECTIONS.md"),
    ("docs/03_INVENTAIRE_DES_ASSETS.md", "ASSETS.md"),
    ("docs/04_BACKLOG_PRIORISE.md", "BACKLOG.md"),
    ("docs/05_CRITERES_D_ACCEPTATION.md", "ACCEPTANCE.md"),
    ("docs/06_RISQUES_ET_INCERTITUDES.md", "RISKS.md"),
    ("docs/reprise/IMPORT-MANIFEST.md", "IMPORT_MANIFEST.md"),
    ("docs/reprise/FICHE-DE-TRANSFERT.md", "TRANSFER_SHEET.md"),
]

PROFILE_FILES = {
    "software": [
        ("docs/07_ARCHITECTURE_TECHNIQUE.md", "ARCHITECTURE.md"),
        ("docs/08_CONVENTIONS_DE_CODE.md", "CODE_CONVENTIONS.md"),
    ],
    "artistic": [
        ("docs/07_DIRECTION_ARTISTIQUE.md", "ART_DIRECTION.md"),
        ("docs/08_BIBLE_DES_ASSETS.md", "ASSET_BIBLE.md"),
    ],
    "hybrid": [
        ("docs/07_ARCHITECTURE_TECHNIQUE.md", "ARCHITECTURE.md"),
        ("docs/08_DIRECTION_ARTISTIQUE.md", "ART_DIRECTION.md"),
        ("docs/09_BIBLE_DES_ASSETS.md", "ASSET_BIBLE.md"),
        ("docs/10_CONVENTIONS_DE_CODE.md", "CODE_CONVENTIONS.md"),
    ],
}

PROFILE_LABELS = {
    "software": "logiciel",
    "artistic": "artistique",
    "hybrid": "hybride",
}

SLICE_PROPOSALS = {
    "software": (
        "Parcours minimal complet : entree -> action principale -> resultat visible -> "
        "validation observable, sur un seul cas nominal."
    ),
    "artistic": (
        "Artefact court mais presentable : intention -> realisation -> export ou "
        "presentation, avec une seule direction artistique coherente."
    ),
    "hybrid": (
        "Parcours vertical reliant une interaction logicielle a un resultat artistique "
        "visible, presentable et mesurable sur un cas nominal."
    ),
}


def safe_component(value: str) -> str:
    value = value.strip()
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    if not value:
        return "PROJECT"
    if value.upper() in {"CON", "PRN", "AUX", "NUL"}:
        return f"{value}-project"
    return value


def normalize_profile(value: str, classification: str) -> str:
    value = value.lower().strip()
    if value == "auto":
        value = classification
    aliases = {"software": "software", "logiciel": "software", "artistic": "artistic", "artistique": "artistic", "hybrid": "hybrid", "hybride": "hybrid"}
    value = aliases.get(value, value)
    if value not in PROFILES:
        raise ValueError(
            "Profil indetermine. Choisir --project-type software, artistic ou hybrid."
        )
    return value


def render_template(template_path: Path, variables: dict[str, str]) -> str:
    text = template_path.read_text(encoding="utf-8")
    for key, value in variables.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def render_asset_shortlist(entries: list[dict], requested: bool) -> str:
    if not requested:
        return "Aucune shortlist demandee. Utiliser `python scripts/asset_registry.py --query \"...\"` pour rechercher."
    if not entries:
        raise ValueError("Aucun asset ne correspond aux filtres du registre.")
    lines = []
    for entry in entries:
        formats = ", ".join(entry.get("formats", []))
        lines.append(
            f"- `{entry['id']}` - **{entry['name']}** ; formats : {formats} ; "
            f"licence : {entry['license']} ; [source]({entry['url']}) ; "
            f"[licence]({entry['license_url']})"
        )
    return "\n".join(lines)


def write_if_missing(path: Path, content: str, dry_run: bool) -> str:
    if path.exists():
        return "preserved"
    if dry_run:
        return "planned"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return "created"


def build_variables(
    *,
    project_name: str,
    profile: str,
    objective: str,
    hard_constraints: str,
    source_root: Path,
    output_root: Path,
    context: dict,
    created_at: str,
    asset_shortlist: str,
) -> dict[str, str]:
    evidence = context["classification"].get("evidence", [])
    facts = "\n".join(f"- {item}" for item in evidence) or "- Aucun fait structurel detecte automatiquement."
    extensions = ", ".join(
        f"{key}: {value}" for key, value in context.get("extensions", {}).items()
    ) or "Aucune extension recensee."
    return {
        "PROJECT_NAME": project_name,
        "PROJECT_TYPE": profile,
        "PROJECT_TYPE_LABEL": PROFILE_LABELS[profile],
        "OBJECTIVE": objective or "[A ARBITRER - objectif principal]",
        "HARD_CONSTRAINTS": hard_constraints or "[A ARBITRER - contrainte non negociable]",
        "SOURCE_ROOT": str(source_root),
        "OUTPUT_ROOT": str(output_root),
        "CREATED_AT": created_at,
        "GIT_DETECTED": "oui" if context.get("git_detected") else "non",
        "FILE_COUNT": str(context.get("file_count", 0)),
        "EXTENSIONS": extensions,
        "CLASSIFICATION_EVIDENCE": facts,
        "ASSET_REGISTRY_SHORTLIST": asset_shortlist,
        "VERTICAL_SLICE": SLICE_PROPOSALS[profile],
        "NEXT_ACTION": "Valider le Master Brief 0.1 et la tranche verticale proposee.",
        "NO_PRODUCTION": "Aucune production n'a ete lancee pendant ce bootstrap.",
    }


def report_markdown(
    *,
    project_name: str,
    profile: str,
    output_root: Path,
    source_root: Path,
    context: dict,
    created: list[str],
    preserved: list[str],
    questions: list[str],
    objective: str,
    hard_constraints: str,
    asset_shortlist: str,
    dry_run: bool,
) -> str:
    evidence = context["classification"].get("evidence", [])
    evidence_lines = "\n".join(f"- {item}" for item in evidence) or "- Aucun indice structurel fort."
    created_lines = "\n".join(f"- `{item}`" for item in created) or "- Aucun nouveau fichier."
    preserved_lines = "\n".join(f"- `{item}`" for item in preserved) or "- Aucun fichier existant preserve."
    question_lines = "\n".join(f"- {item}" for item in questions) or "- Aucun blocage structurel restant."
    mode = "PREVISUALISATION - aucune ecriture" if dry_run else "BOOTSTRAP EFFECTUE"
    return f"""# Rapport de bootstrap - {project_name}

> Etat : **{mode}**  
> Genere le : {datetime.now(timezone.utc).isoformat()}

## Synthese

- Profil retenu : `{profile}` ({PROFILE_LABELS[profile]}).
- Source inspectee : `{source_root}`.
- MASTER : `{output_root}`.
- Fichiers inspectes : {context.get('file_count', 0)}.
- Git detecte dans la source : {"oui" if context.get("git_detected") else "non"}.
- Objectif fourni : {objective or "[A ARBITRER]"}.
- Contraintes fournies : {hard_constraints or "[A ARBITRER]"}.

## Preuves de classification

{evidence_lines}

## Shortlist d'assets du registre

{asset_shortlist}

## Fichiers crees ou planifies

{created_lines}

## Fichiers preserves

{preserved_lines}

## Arbitrages et questions restantes

{question_lines}

## Tranche verticale proposee

{SLICE_PROPOSALS[profile]}

Inclus : un cas nominal complet, les preuves de resultat et les criteres d'acceptation associes.  
Exclus : production generale, multiplication des cas, finition exhaustive, lancement commercial et decisions irreversibles non validees.

Risques a tester : valeur reelle du parcours, faisabilite du socle, coherence UX ou artistique, charge de validation et qualite observable.

## Prochaine action

{ "Valider le plan ci-dessus avant d'ecrire." if dry_run else "Valider le Master Brief 0.1 et la tranche verticale proposee." }

**{ "Aucune ecriture n'a ete effectuee." if dry_run else "Aucune production n'a ete lancee pendant ce bootstrap." }**
"""


def bootstrap(args: argparse.Namespace) -> tuple[int, dict]:
    source_root = Path(args.root).expanduser().resolve()
    context = inspect_context(source_root)
    project_name = safe_component(args.project_name or context.get("name_candidate") or source_root.name)
    profile = normalize_profile(args.project_type, context["classification"]["classification"])
    objective = (args.objective or "").strip()
    hard_constraints = (args.hard_constraints or "").strip()
    asset_query = (args.asset_query or "").strip()
    asset_category = (args.asset_category or "").strip()
    asset_format = (args.asset_format or "").strip()
    asset_priority = (args.asset_priority or "").strip()
    asset_filter_requested = bool(asset_query or asset_category or asset_format or asset_priority)
    asset_entries = []
    if asset_filter_requested:
        registry = load_registry()
        asset_entries = search_entries(
            registry.get("entries", []),
            query=asset_query,
            category=asset_category,
            file_format=asset_format,
            priority=asset_priority,
        )[: max(1, args.asset_limit)]
    asset_shortlist = render_asset_shortlist(asset_entries, asset_filter_requested)
    remaining_questions = list(context.get("questions", []))
    if objective:
        remaining_questions = [
            item for item in remaining_questions if "resultat principal" not in item
        ]
    if args.project_name or context.get("name_candidate"):
        remaining_questions = [item for item in remaining_questions if "nom court" not in item]
    if args.project_type != "auto":
        remaining_questions = [item for item in remaining_questions if "profil" not in item]

    if args.out:
        output_root = Path(args.out).expanduser().resolve()
    else:
        output_root = source_root.parent / f"{project_name} - MASTER"
    if output_root == source_root:
        raise ValueError("La destination MASTER ne peut pas etre le dossier source inspecte.")

    existing_entries = sorted(output_root.iterdir(), key=lambda path: path.name.lower()) if output_root.exists() else []
    manifest_path = output_root / ".newpro-manifest.json"
    existing_manifest: dict | None = None
    if manifest_path.exists():
        try:
            existing_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"Manifeste existant illisible: {manifest_path} ({exc})") from exc
        if existing_manifest.get("profile") and existing_manifest["profile"] != profile:
            raise ValueError(
                f"Le MASTER existe deja avec le profil {existing_manifest['profile']}; "
                "ne pas changer de profil silencieusement."
            )
    elif existing_entries and not args.adopt_existing:
        raise ValueError(
            f"La destination existe et n'est pas vide: {output_root}. "
            "Utiliser --out ailleurs ou --adopt-existing apres verification explicite."
        )

    created_at = (existing_manifest or {}).get("created_at") or datetime.now(timezone.utc).isoformat()
    variables = build_variables(
        project_name=project_name,
        profile=profile,
        objective=objective,
        hard_constraints=hard_constraints,
        source_root=source_root,
        output_root=output_root,
        context=context,
        created_at=created_at,
        asset_shortlist=asset_shortlist,
    )
    template_root = Path(__file__).resolve().parents[1] / "assets" / "templates"
    planned_files = BASE_FILES + PROFILE_FILES[profile]
    statuses: dict[str, str] = {}

    for directory in ("assets", "prototype", "src", "tests"):
        directory_path = output_root / directory
        if directory_path.exists() and not directory_path.is_dir():
            raise ValueError(f"Le chemin requis n'est pas un dossier: {directory_path}")
        if not args.dry_run:
            directory_path.mkdir(parents=True, exist_ok=True)

    for relative_path, template_name in planned_files:
        template_path = template_root / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template manquant: {template_path}")
        target = output_root / relative_path
        content = render_template(template_path, variables)
        unresolved = re.findall(r"\{\{[^}]+\}\}", content)
        if unresolved:
            raise ValueError(f"Variables non resolues dans {template_name}: {unresolved}")
        statuses[relative_path] = write_if_missing(target, content, args.dry_run)

    report_path = output_root / "BOOTSTRAP_REPORT.md"
    report_content = report_markdown(
        project_name=project_name,
        profile=profile,
        output_root=output_root,
        source_root=source_root,
        context=context,
        created=[path for path, status in statuses.items() if status in {"created", "planned"}],
        preserved=[path for path, status in statuses.items() if status == "preserved"],
        questions=remaining_questions,
        objective=objective,
        hard_constraints=hard_constraints,
        asset_shortlist=asset_shortlist,
        dry_run=args.dry_run,
    )
    statuses["BOOTSTRAP_REPORT.md"] = write_if_missing(report_path, report_content, args.dry_run)

    manifest = {
        "newpro_version": VERSION,
        "created_at": created_at,
        "project_name": project_name,
        "profile": profile,
        "source_root": str(source_root),
        "master_root": str(output_root),
        "generated_files": [path for path, _ in planned_files] + ["BOOTSTRAP_REPORT.md"],
        "asset_registry_ids": [entry["id"] for entry in asset_entries],
        "production_started": False,
    }
    if manifest_path.exists():
        statuses[".newpro-manifest.json"] = "preserved"
    else:
        statuses[".newpro-manifest.json"] = "planned" if args.dry_run else "created"
        if not args.dry_run:
            output_root.mkdir(parents=True, exist_ok=True)
            manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    result = {
        "status": "dry-run" if args.dry_run else "bootstrapped",
        "project_name": project_name,
        "profile": profile,
        "master_root": str(output_root),
        "source_root": str(source_root),
        "created": [path for path, status in statuses.items() if status in {"created", "planned"}],
        "preserved": [path for path, status in statuses.items() if status == "preserved"],
        "questions": remaining_questions,
        "asset_registry_ids": [entry["id"] for entry in asset_entries],
        "production_started": False,
    }
    return 0, result


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap an idempotent MASTER project skeleton.")
    parser.add_argument("--root", default=".", help="Source context directory")
    parser.add_argument("--out", help="MASTER destination; defaults to a sibling directory")
    parser.add_argument("--project-name", help="Project name; inferred from the context when omitted")
    parser.add_argument("--objective", help="Known project objective; unknown values remain explicit")
    parser.add_argument("--hard-constraints", help="Known non-negotiable constraints")
    parser.add_argument("--asset-query", help="Search words for the bundled asset registry")
    parser.add_argument("--asset-category", help="Exact registry category, e.g. models, textures, characters")
    parser.add_argument("--asset-format", help="Required asset format, e.g. glb or gltf")
    parser.add_argument("--asset-priority", choices=["A", "B", "TEST"], help="Limit shortlist to a registry priority")
    parser.add_argument("--asset-limit", type=int, default=5, help="Maximum assets in the shortlist")
    parser.add_argument("--project-type", default="auto", choices=["auto", "software", "artistic", "hybrid", "logiciel", "artistique", "hybride"])
    parser.add_argument("--adopt-existing", action="store_true", help="Explicitly adopt a non-empty destination without a newpro manifest")
    parser.add_argument("--dry-run", action="store_true", help="Plan writes without modifying files")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output")
    args = parser.parse_args()
    try:
        code, result = bootstrap(args)
    except (FileNotFoundError, NotADirectoryError, RuntimeError, ValueError, OSError) as exc:
        if args.json:
            print(json.dumps({"status": "error", "error": str(exc)}, indent=2, ensure_ascii=False))
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"{result['status']}: {result['master_root']}")
        print(f"Profil: {result['profile']}")
        print(f"Created/planned: {len(result['created'])}; preserved: {len(result['preserved'])}")
        print("Aucune production n'a ete lancee.")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
