#!/usr/bin/env python3
"""Read-only validation of package structure, templates, relative links and optional manifest."""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

from check_handoff import read_json, validate_bundle


def main() -> int:
    skill = Path(__file__).resolve().parents[1]
    root = skill.parent
    errors: list[str] = []
    checks: list[str] = []
    required = ["SKILL.md", "agents/openai.yaml", "assets/04-business-plan.md", "assets/05-decision-handoff.json", "assets/08-checklist.json", "references/integrations.md", "references/sources.md", "tests/test_handoff.py"]
    for name in required:
        if not (skill/name).is_file():
            errors.append("Missing: " + name)
    try:
        text=(skill/"SKILL.md").read_text(encoding="utf-8")
        header=re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not header or not re.search(r"^name: business-checklist$", header[1], re.M) or not re.search(r"^description:", header[1], re.M):
            errors.append("Invalid SKILL frontmatter for this package.")
        if len(text.splitlines())>500:
            errors.append("SKILL.md exceeds the chosen 500-line readability limit.")
        checks.append("Core frontmatter, name and length")
        meta=(skill/"agents/openai.yaml").read_text(encoding="utf-8")
        for token in ('interface:', 'display_name: "Business Checklist"', 'policy:', 'allow_implicit_invocation: true'):
            if token not in meta: errors.append("Missing UI token: "+token)
        checks.append("Expected UI metadata fields (not a general YAML parser)")
        bp=(skill/"assets/04-business-plan.md").read_text(encoding="utf-8")
        headings=re.findall(r"^## (\d+)\. ",bp,re.M)
        if headings!=[str(i) for i in range(1,11)]:
            errors.append("Business plan must have exactly the 10 ordered numbered parts.")
        checks.append("Ten ordered business-plan sections")
        for file in sorted(root.rglob("*")):
            if file.is_symlink():
                errors.append("Unexpected symlink: "+str(file.relative_to(root)))
            if not file.is_file() or "__pycache__" in file.parts: continue
            if file.suffix==".json":
                read_json(file)
            if file.suffix==".py":
                ast.parse(file.read_text(encoding="utf-8"),filename=str(file))
            if file.suffix==".md":
                text=file.read_text(encoding="utf-8")
                text=re.sub(r"```.*?```","",text,flags=re.S)
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)",text):
                    if urlparse(target).scheme or target.startswith("#"): continue
                    target=unquote(target.split("#",1)[0])
                    if target and not (file.parent/target).exists():
                        errors.append(f"Broken local link in {file.relative_to(root)}: {target}")
        checks.append("JSON parse, Python syntax, local Markdown links and symlink absence")
        handoff=read_json(skill/"assets/05-decision-handoff.json")
        checklist=read_json(skill/"assets/08-checklist.json")
        e,w=validate_bundle(handoff,checklist)
        errors+=e
        if len(checklist["checks"])!=60:
            errors.append("Expected the 60-control master checklist.")
        checks.append("Template handoff and 60-control checklist consistency")
        sources=read_json(skill/"references/sources.json")["sources"]
        if len({s["id"] for s in sources})!=len(sources):
            errors.append("Duplicated source IDs.")
        checks.append("Source register identities")
        manifest=root/"MANIFEST_SHA256.json"
        if manifest.exists():
            entries=read_json(manifest)["files"]
            declared={x["path"] for x in entries}
            actual={str(p.relative_to(root)).replace("\\", "/") for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.name!="MANIFEST_SHA256.json"}
            if declared!=actual:
                errors.append("Manifest file list differs from the package contents.")
            for entry in entries:
                file=root/entry["path"]
                if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=entry["sha256"]:
                    errors.append("Manifest checksum mismatch: "+entry["path"])
            checks.append("SHA-256 manifest and exact file list")
        else:
            checks.append("Manifest not yet present: checksum step not executed")
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as exc:
        errors.append(str(exc))
    print(json.dumps({"ok":not errors,"checks":checks,"errors":errors,
                      "limits":"Does not execute an agent, validate real markets, install on a PC or authenticate source claims."}, ensure_ascii=False, indent=2))
    return int(bool(errors))

if __name__=="__main__":
    raise SystemExit(main())
