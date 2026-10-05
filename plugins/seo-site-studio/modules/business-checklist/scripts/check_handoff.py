#!/usr/bin/env python3
"""Check declared consistency, not truth or authorization. Python 3.10+, stdlib only."""
from __future__ import annotations

import argparse
from datetime import date
import json
import math
from pathlib import Path
from typing import Any

DECISIONS = {"TESTER", "PIVOTER", "GO_PILOTE", "LANCER_PROGRESSIVEMENT", "STOP_VERSION_ACTUELLE", "BLOQUE_INFORMATION"}
GO = {"GO_PILOTE", "LANCER_PROGRESSIVEMENT"}
MODES = {"NOUVEAU_PROJET", "AUDIT_EXISTANT", "MISE_A_JOUR", "FINANCEMENT", "PRE_LANCEMENT"}
TYPES = {"FAIT_SOURCE", "OBSERVATION_TERRAIN", "CALCUL", "HYPOTHESE", "INCONNU"}
RESULTS = {"NON_EVALUE", "FAVORABLE", "DEFAVORABLE", "NON_CONCLUANT", "NON_APPLICABLE"}
CHECK_STATES = {"A_EVALUER", "ETAYE", "A_TESTER", "NON_CONFORME", "BLOQUE", "NON_APPLICABLE"}
TOP_FIELDS = {
    "kind", "schema_version", "run_id", "project_id", "as_of", "entrypoint", "mode",
    "evidence_basis", "decision", "decision_rationale", "evidence", "gates", "blocking_issues",
    "unknowns", "next_step", "permissions", "finance", "seo", "checklist_ref", "next_actions",
    "artifacts", "limitations",
}

def filled(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def number(value: Any) -> bool:
    return type(value) in (int, float) and math.isfinite(value) and value >= 0

def iso_date(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 10:
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False

def read_json(path: Path) -> Any:
    def reject_constant(value: str) -> None:
        raise ValueError(f"Non-finite JSON number: {value}")
    return json.loads(path.read_text(encoding="utf-8-sig"), parse_constant=reject_constant)

def validate_handoff(data: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return ["Handoff must be a JSON object."], warnings
    missing, extra = TOP_FIELDS - data.keys(), data.keys() - TOP_FIELDS
    if missing:
        errors.append("Missing fields: " + ", ".join(sorted(missing)))
    if extra:
        errors.append("Unknown top-level fields: " + ", ".join(sorted(extra)))
    if data.get("kind") not in {"TEMPLATE", "ASSESSMENT"}:
        errors.append("kind must be TEMPLATE or ASSESSMENT.")
    template = data.get("kind") == "TEMPLATE"
    if data.get("schema_version") != "2.0":
        errors.append("schema_version must be 2.0.")
    if data.get("mode") not in MODES:
        errors.append("Invalid mode.")
    if not filled(data.get("entrypoint")):
        errors.append("entrypoint must be documented.")
    if data.get("evidence_basis") not in {"DOCUMENTAIRE", "TERRAIN", "MIXTE"}:
        errors.append("Invalid evidence_basis.")
    decision = data.get("decision")
    if template:
        warnings.append("Template only: no project assessment or authorization established.")
        if decision is not None:
            errors.append("A TEMPLATE must not carry a project decision.")
    else:
        if decision not in DECISIONS:
            errors.append("ASSESSMENT requires a permitted decision.")
        for key in ("run_id", "project_id", "decision_rationale", "checklist_ref"):
            if not filled(data.get(key)):
                errors.append(f"ASSESSMENT requires {key}.")
        if not iso_date(data.get("as_of")):
            errors.append("ASSESSMENT requires an ISO as_of date.")

    evidence = data.get("evidence")
    if not isinstance(evidence, list):
        errors.append("evidence must be an array.")
        evidence = []
    by_id: dict[str, dict[str, Any]] = {}
    for item in evidence:
        if not isinstance(item, dict):
            errors.append("Each evidence item must be an object.")
            continue
        eid = item.get("id")
        if not filled(eid) or eid in by_id:
            errors.append("Evidence IDs must be non-empty and unique.")
        else:
            by_id[eid] = item
        if item.get("type") not in TYPES:
            errors.append(f"Invalid evidence type: {eid}.")
        if type(item.get("verified")) is not bool:
            errors.append(f"Evidence {eid} needs a boolean verified field.")
        if not filled(item.get("claim")):
            errors.append(f"Evidence {eid} needs a claim.")
        if item.get("verified") is True:
            if not filled(item.get("source_ref")) or not iso_date(item.get("observed_at")):
                errors.append(f"Verified evidence {eid} needs source_ref and observed_at.")
            if item.get("type") in {"HYPOTHESE", "INCONNU"}:
                errors.append(f"Hypothesis/unknown {eid} cannot be marked verified.")

    def refs_ok(refs: Any, label: str) -> list[str]:
        if not isinstance(refs, list) or any(not filled(x) for x in refs):
            errors.append(f"{label}: evidence_ids must be an array of IDs.")
            return []
        if len(set(refs)) != len(refs):
            errors.append(f"{label}: duplicated evidence references.")
        for ref in refs:
            if ref not in by_id:
                errors.append(f"{label}: unknown evidence reference {ref}.")
        return refs

    gates = data.get("gates")
    if not isinstance(gates, list):
        errors.append("gates must be an array.")
        gates = []
    gate_ids: list[Any] = []
    go_refs: set[str] = set()
    for gate in gates:
        if not isinstance(gate, dict):
            errors.append("Each gate must be an object.")
            continue
        gid = gate.get("id")
        gate_ids.append(gid)
        result = gate.get("result")
        if result not in RESULTS:
            errors.append(f"Gate {gid}: invalid result.")
        if type(gate.get("critical_for_next_scope")) is not bool:
            errors.append(f"Gate {gid}: critical_for_next_scope must be boolean.")
        refs = refs_ok(gate.get("evidence_ids"), f"Gate {gid}")
        if result != "NON_EVALUE" and not filled(gate.get("rationale")):
            errors.append(f"Gate {gid}: result requires rationale.")
        if result in {"FAVORABLE", "DEFAVORABLE"} and not refs:
            errors.append(f"Gate {gid}: result requires evidence references.")
        if decision in GO:
            if result == "NON_EVALUE":
                errors.append(f"GO requires gate {gid} to be reviewed.")
            if gate.get("critical_for_next_scope") is True and result != "FAVORABLE":
                errors.append(f"GO cannot bypass unresolved critical gate {gid}.")
            if result == "FAVORABLE":
                go_refs.update(refs)
                if not any(by_id.get(r, {}).get("verified") is True for r in refs):
                    errors.append(f"GO gate {gid} lacks a verified supporting reference.")
    if len(gate_ids) != 6 or sorted(str(x) for x in gate_ids) != [f"G{i}" for i in range(1, 7)]:
        errors.append("Exactly the six unique gates G1..G6 are required.")

    for key in ("blocking_issues", "unknowns", "next_actions", "artifacts", "limitations"):
        if not isinstance(data.get(key), list):
            errors.append(f"{key} must be an array.")
    blockers = data.get("blocking_issues") if isinstance(data.get("blocking_issues"), list) else []
    if decision == "STOP_VERSION_ACTUELLE":
        if not blockers or not any(x.get("verified") is True for x in by_id.values()):
            errors.append("STOP requires a documented blocker and verified evidence.")
    if decision == "BLOQUE_INFORMATION" and not data.get("unknowns"):
        errors.append("BLOQUE_INFORMATION requires the missing information to be stated.")

    step = data.get("next_step")
    perms = data.get("permissions")
    finance = data.get("finance")
    seo = data.get("seo")
    for name, obj in (("next_step", step), ("permissions", perms), ("finance", finance), ("seo", seo)):
        if not isinstance(obj, dict):
            errors.append(f"{name} must be an object.")
    step = step if isinstance(step, dict) else {}
    perms = perms if isinstance(perms, dict) else {}
    finance = finance if isinstance(finance, dict) else {}
    seo = seo if isinstance(seo, dict) else {}
    for label, obj in (("next_step", step), ("permissions", perms)):
        for key in ("max_cash_eur", "max_hours"):
            if obj.get(key) is not None and not number(obj[key]):
                errors.append(f"{label}.{key} must be finite, non-negative, not boolean.")
    if step.get("review_date") is not None and not iso_date(step["review_date"]):
        errors.append("review_date must be ISO date or null.")
    actions = perms.get("granted_actions")
    if not isinstance(actions, list) or any(not filled(x) for x in actions):
        errors.append("permissions.granted_actions must be an array of strings.")
    elif actions:
        if template:
            errors.append("A TEMPLATE must not grant permissions.")
        if not filled(perms.get("approval_ref")):
            errors.append("Permissions require a traceable approval_ref.")
        warnings.append("Approval authenticity and current scope require human/host verification.")
    else:
        warnings.append("No execution permission established: recommendation is not authorization.")
    if finance.get("status") not in {"NON_MODELISE", "PARAMETRIQUE", "CHIFFRE", "RECONCILIE"}:
        errors.append("Invalid finance status.")
    if type(finance.get("without_unsecured_funding_reviewed")) is not bool:
        errors.append("Finance stress-test flag must be boolean.")
    if finance.get("status") in {"PARAMETRIQUE", "CHIFFRE", "RECONCILIE"} and not filled(finance.get("model_ref")):
        errors.append("A financial model status requires model_ref.")
    if finance.get("status") == "RECONCILIE" and not filled(finance.get("checks_ref")):
        errors.append("Reconciled finance requires checks_ref.")
    if seo.get("status") not in {"NON_SOLLICITE", "ABSENT", "PRESENT_NON_EXECUTE", "EXECUTE_AVEC_TRACE"}:
        errors.append("Invalid SEO status.")
    if seo.get("status") == "EXECUTE_AVEC_TRACE":
        if not filled(seo.get("source_ref")):
            errors.append("Executed SEO requires a source_ref.")
        if seo.get("budget_double_count_checked") is not True:
            errors.append("Integrated SEO requires the budget double-count check.")

    if decision == "LANCER_PROGRESSIVEMENT" and finance.get("status") not in {"CHIFFRE", "RECONCILIE"}:
        errors.append("Progressive launch requires a quantified financial model.")
    if decision in GO:
        if data.get("evidence_basis") == "DOCUMENTAIRE":
            errors.append("Documentary-only evidence cannot support GO.")
        field = [by_id[r] for r in go_refs if r in by_id and by_id[r].get("type") == "OBSERVATION_TERRAIN" and by_id[r].get("verified") is True and by_id[r].get("relevance") == "PROJET"]
        if not field:
            errors.append("GO requires verified project field evidence linked to a favorable gate.")
        if blockers:
            errors.append("GO cannot coexist with blocking_issues.")
        for key in ("scope", "owner", "budget_evidence_ref"):
            if not filled(step.get(key)):
                errors.append(f"GO requires next_step.{key}.")
        for key in ("max_cash_eur", "max_hours"):
            if not number(step.get(key)):
                errors.append(f"GO requires a finite next_step.{key}.")
        if not (iso_date(step.get("review_date")) or filled(step.get("review_trigger"))):
            errors.append("GO requires a review date or explicit trigger.")
        if finance.get("without_unsecured_funding_reviewed") is not True:
            errors.append("GO requires review without unsecured funding.")
        if len(data.get("next_actions", [])) == 0:
            errors.append("GO requires an actionable next step.")
    return errors, warnings


def validate_checklist(data: Any, evidence_ids: set[str] | None = None) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Checklist must be an object."]
    if data.get("schema_version") != "2.0" or data.get("kind") not in {"TEMPLATE", "ASSESSMENT"}:
        errors.append("Checklist needs schema_version 2.0 and a valid kind.")
    checks = data.get("checks")
    if not isinstance(checks, list):
        return errors + ["Checklist checks must be an array."]
    ids: set[str] = set()
    for check in checks:
        if not isinstance(check, dict):
            errors.append("Checklist item must be an object.")
            continue
        cid = check.get("id")
        if not filled(cid) or cid in ids:
            errors.append("Checklist IDs must be unique and non-empty.")
        else:
            ids.add(cid)
        status = check.get("status")
        if status not in CHECK_STATES:
            errors.append(f"{cid}: invalid checklist status.")
        if data.get("kind") == "TEMPLATE" and status != "A_EVALUER":
            errors.append(f"{cid}: template must not claim an assessed status.")
        if data.get("kind") == "ASSESSMENT" and type(check.get("critical_for_next_scope")) is not bool:
            errors.append(f"{cid}: scope criticality must be explicitly assessed.")
        if status != "A_EVALUER" and not filled(check.get("rationale")):
            errors.append(f"{cid}: assessed status requires rationale.")
        refs = check.get("evidence_ids")
        if not isinstance(refs, list) or any(not filled(x) for x in refs):
            errors.append(f"{cid}: evidence_ids must be an array of IDs.")
            refs = []
        if status == "ETAYE" and not refs:
            errors.append(f"{cid}: ETAYE requires evidence references.")
        if evidence_ids is not None:
            for ref in refs:
                if ref not in evidence_ids:
                    errors.append(f"{cid}: unknown evidence reference {ref}.")
        if status in {"A_TESTER", "NON_CONFORME", "BLOQUE"} and not filled(check.get("next_action")):
            errors.append(f"{cid}: unresolved status requires next_action.")
    return errors


def validate_bundle(handoff: Any, checklist: Any) -> tuple[list[str], list[str]]:
    """Also compare identity and critical statuses between the two project outputs."""
    errors, warnings = validate_handoff(handoff)
    ids = {e["id"] for e in handoff.get("evidence", []) if isinstance(e, dict) and filled(e.get("id"))} if isinstance(handoff, dict) and isinstance(handoff.get("evidence"), list) else set()
    errors += validate_checklist(checklist, ids)
    if isinstance(handoff, dict) and isinstance(checklist, dict):
        if handoff.get("kind") == "ASSESSMENT":
            if checklist.get("kind") != "ASSESSMENT":
                errors.append("An assessment cannot use an unfilled checklist template.")
            for key in ("project_id", "run_id", "as_of"):
                if checklist.get(key) != handoff.get(key):
                    errors.append(f"Handoff/checklist identity mismatch: {key}.")
        if handoff.get("decision") in GO and isinstance(checklist.get("checks"), list):
            for check in checklist["checks"]:
                if isinstance(check, dict) and check.get("critical_for_next_scope") is True and check.get("status") != "ETAYE":
                    errors.append(f"GO conflicts with unresolved critical checklist item {check.get('id')}.")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff", type=Path)
    parser.add_argument("--checklist", type=Path)
    args = parser.parse_args()
    try:
        data = read_json(args.handoff)
        if args.checklist:
            errors, warnings = validate_bundle(data, read_json(args.checklist))
        else:
            errors, warnings = validate_handoff(data)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps({"ok": not errors, "errors": errors, "warnings": warnings,
                      "scope": "Declared field consistency only; evidence truth and permissions not authenticated."}, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
