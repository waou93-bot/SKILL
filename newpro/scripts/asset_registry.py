#!/usr/bin/env python3
"""Search the bundled free-asset registry without external dependencies."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REGISTRY_PATH = Path(__file__).resolve().parents[1] / "references" / "ASSET_REGISTRY.json"
PRIORITY_ORDER = {"A": 0, "B": 1, "TEST": 2}


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Impossible de lire le registre: {path} ({exc})") from exc


def search_entries(
    entries: list[dict],
    *,
    query: str = "",
    category: str = "",
    file_format: str = "",
    priority: str = "",
    entry_id: str = "",
) -> list[dict]:
    query_terms = [term.casefold() for term in query.split() if term.strip()]
    category = category.casefold().strip()
    file_format = file_format.casefold().lstrip(".").strip()
    priority = priority.upper().strip()
    entry_id = entry_id.casefold().strip()

    def matches(entry: dict) -> bool:
        if category and entry.get("category", "").casefold() != category:
            return False
        if priority and entry.get("priority", "").upper() != priority:
            return False
        if entry_id and entry.get("id", "").casefold() != entry_id:
            return False
        formats = {str(value).casefold().lstrip(".") for value in entry.get("formats", [])}
        if file_format and file_format not in formats:
            return False
        haystack = " ".join(
            [
                entry.get("id", ""),
                entry.get("name", ""),
                entry.get("category", ""),
                " ".join(entry.get("tags", [])),
                entry.get("notes", ""),
            ]
        ).casefold()
        return all(term in haystack for term in query_terms)

    return sorted(
        [entry for entry in entries if matches(entry)],
        key=lambda entry: (PRIORITY_ORDER.get(entry.get("priority", ""), 9), entry.get("name", "").casefold()),
    )


def compact_entry(entry: dict) -> dict:
    return {
        "id": entry.get("id"),
        "name": entry.get("name"),
        "category": entry.get("category"),
        "formats": entry.get("formats", []),
        "license": entry.get("license"),
        "priority": entry.get("priority"),
        "three_ready": entry.get("three_ready"),
        "url": entry.get("url"),
        "license_url": entry.get("license_url"),
        "notes": entry.get("notes"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the newpro free-asset registry.")
    parser.add_argument("--query", default="", help="Words to search in name, tags, category, or notes")
    parser.add_argument("--category", default="", help="Exact category, e.g. models, textures, characters")
    parser.add_argument("--format", dest="file_format", default="", help="Required file format, e.g. glb or gltf")
    parser.add_argument("--priority", choices=["A", "B", "TEST"])
    parser.add_argument("--id", dest="entry_id", default="", help="Exact registry entry id")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        registry = load_registry()
        entries = search_entries(
            registry.get("entries", []),
            query=args.query,
            category=args.category,
            file_format=args.file_format,
            priority=args.priority or "",
            entry_id=args.entry_id,
        )[: max(1, args.limit)]
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({"registry": str(REGISTRY_PATH), "count": len(entries), "entries": [compact_entry(entry) for entry in entries]}, indent=2, ensure_ascii=False))
    else:
        if not entries:
            print("Aucun asset ne correspond a ces filtres.")
            return 1
        for entry in entries:
            formats = ", ".join(entry.get("formats", []))
            print(f"[{entry.get('priority')}] {entry.get('id')} | {entry.get('name')} | {entry.get('category')} | {formats} | {entry.get('license')}")
            print(f"    {entry.get('url')}")
            print(f"    {entry.get('notes')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
