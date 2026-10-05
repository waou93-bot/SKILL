#!/usr/bin/env python3
"""Summarize observed JSONL answers, never an assistant's universal ranking."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime
import json
from pathlib import Path

DIMENSIONS = ("platform", "surface", "branded", "language", "country", "search_enabled", "context_control", "synthetic")
OUTCOMES = ("mentioned", "cited", "recommended")


def summarize(rows: list[dict]) -> dict:
    seen: set[str] = set()
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for index, original in enumerate(rows, 1):
        if not isinstance(original, dict):
            raise ValueError(f"Row {index}: expected object")
        row = {"synthetic": False, **original}
        for field in ("run_id", "query_id", "platform", "surface", "language", "country", "context_control", "observed_at", "status"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Row {index}: missing string {field}")
        for field in ("branded", "search_enabled", "synthetic"):
            if type(row.get(field)) is not bool:
                raise ValueError(f"Row {index}: {field} must be boolean")
        try:
            date = datetime.fromisoformat(row["observed_at"].replace("Z", "+00:00"))
            if date.tzinfo is None:
                raise ValueError("timezone missing")
        except ValueError as exc:
            raise ValueError(f"Row {index}: observed_at must include timezone") from exc
        if row["run_id"] in seen:
            raise ValueError(f"Duplicate run_id: {row['run_id']}")
        seen.add(row["run_id"])
        if row["status"] not in ("ok", "error", "not_tested"):
            raise ValueError(f"Row {index}: invalid status")
        if row["status"] == "ok":
            if not isinstance(row.get("evidence_ref"), str) or not row["evidence_ref"].strip():
                raise ValueError(f"Row {index}: observed answer needs evidence_ref")
            for field in OUTCOMES:
                if type(row.get(field)) is not bool:
                    raise ValueError(f"Row {index}: {field} must be boolean")
        groups[tuple(row[key] for key in DIMENSIONS)].append(row)
    output = []
    for key, observations in groups.items():
        valid = [r for r in observations if r["status"] == "ok"]
        item = {"stratum": dict(zip(DIMENSIONS, key)), "observations": len(observations),
                "valid_answers": len(valid), "status_counts": dict(Counter(r["status"] for r in observations)),
                "unique_queries": len({r["query_id"] for r in observations}),
                "unique_valid_queries": len({r["query_id"] for r in valid})}
        for field, name in zip(OUTCOMES, ("mention", "citation", "recommendation")):
            count = sum(r[field] for r in valid)
            item[name + "_count"] = count
            item[name + "_rate"] = count / len(valid) if valid else None
        output.append(item)
    return {"schema_version": "1.0", "strata": output,
            "notice": "Observed panel only. Errors/not_tested excluded from rates; repeats are not independent users. Evidence references require human verification."}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    try:
        if args.input.stat().st_size > 20_000_000:
            raise ValueError("Input exceeds 20 MB")
        rows = [json.loads(line) for line in args.input.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        text = json.dumps(summarize(rows), ensure_ascii=False, indent=2) + "\n"
        if args.out:
            with args.out.open("x", encoding="utf-8") as handle:
                handle.write(text)
        else:
            print(text, end="")
        return 0
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
