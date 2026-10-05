#!/usr/bin/env python3
"""Offline triage of supplied HTML/HTTP captures. Not a crawler or RFC conformance test."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit

SEARCH_BOTS = ("OAI-SearchBot", "PerplexityBot", "Claude-SearchBot", "Googlebot", "bingbot")


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.lang = ""
        self.h1 = 0
        self.canonicals: list[str] = []
        self.meta: list[tuple[str, str]] = []
        self.links: list[str] = []
        self.jsonld: list[str] = []
        self.ld: str | None = None
        self.text: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang") or ""
        if tag == "title": self.in_title = True
        if tag == "h1": self.h1 += 1
        if tag == "meta": self.meta.append(((a.get("name") or "").lower(), a.get("content") or ""))
        if tag == "link" and "canonical" in (a.get("rel") or "").lower().split():
            self.canonicals.append(a.get("href") or "")
        if tag == "a" and a.get("href"): self.links.append(a["href"])
        if tag in ("script", "style", "template"): self.hidden_depth += 1
        if tag == "script" and (a.get("type") or "").lower() == "application/ld+json": self.ld = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "title": self.in_title = False
        if tag == "script" and self.ld is not None:
            self.jsonld.append(self.ld)
            self.ld = None
        if tag in ("script", "style", "template"):
            self.hidden_depth = max(0, self.hidden_depth - 1)

    def handle_data(self, data: str) -> None:
        if self.in_title: self.title += data
        if self.ld is not None: self.ld += data
        if not self.hidden_depth: self.text.append(data)


def robots_hint(text: str, bot: str, url: str) -> dict:
    """Common ASCII rules only; deliberately return unknown for advanced/ambiguous input."""
    groups: list[tuple[list[str], list[tuple[str, str]]]] = []
    agents: list[str] = []
    rules: list[tuple[str, str]] = []
    saw_rule = False
    for raw in text.lstrip("\ufeff").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line: continue
        name, value = (v.strip() for v in line.split(":", 1))
        name = name.lower()
        if name == "user-agent":
            if saw_rule:
                groups.append((agents, rules)); agents, rules, saw_rule = [], [], False
            agents.append(value.lower())
        elif name in ("allow", "disallow") and agents:
            rules.append((name, value)); saw_rule = True
    if agents: groups.append((agents, rules))
    # Only exact product tokens + wildcard. Partial matches need a reference parser.
    if any(a not in ("*", bot.lower()) and a and a in bot.lower() for aa, _ in groups for a in aa):
        return {"allowed_hint": None, "reason": "partial-agent-token-needs-reference-parser"}
    selected = [rr for aa, rr in groups if bot.lower() in aa]
    if not selected: selected = [rr for aa, rr in groups if "*" in aa]
    parsed = urlsplit(url)
    path = (parsed.path or "/") + (("?" + parsed.query) if parsed.query else "")
    all_rules = [r for rr in selected for r in rr]
    if any(ord(c) > 127 for c in path) or "%" in path or any("%" in v or any(ord(c) > 127 for c in v) for _, v in all_rules):
        return {"allowed_hint": None, "reason": "encoded-or-unicode-path-needs-reference-parser"}
    matches: list[tuple[int, bool, str]] = []
    for action, value in all_rules:
        if not value: continue
        if not value.startswith("/"):
            return {"allowed_hint": None, "reason": "invalid-path-rule"}
        anchored = value.endswith("$")
        core = value[:-1] if anchored else value
        pattern = "^" + ".*".join(re.escape(part) for part in core.split("*")) + ("$" if anchored else "")
        if re.search(pattern, path):
            matches.append((len(core.replace("*", "")), action == "allow", value))
    winner = max(matches, default=None)
    return {"allowed_hint": winner[1] if winner else True,
            "matched_rule": winner[2] if winner else None, "reason": "simplified-offline-rule-match"}


def audit(data: dict) -> dict:
    if not isinstance(data, dict) or not isinstance(data.get("pages"), list):
        raise ValueError("Expected object with pages array")
    robot = data.get("robots", {})
    reports = []
    for page in data["pages"]:
        if not isinstance(page, dict) or not isinstance(page.get("url"), str):
            raise ValueError("Every page needs an absolute URL")
        url = page["url"]
        if urlsplit(url).scheme not in ("http", "https") or not urlsplit(url).netloc:
            raise ValueError("Invalid page URL")
        if type(page.get("intended_public")) is not bool:
            raise ValueError("Every page needs boolean intended_public")
        if not isinstance(page.get("html", ""), str): raise ValueError("html must be text")
        public = page["intended_public"]
        parsed = Page(); parsed.feed(page.get("html", "")); parsed.close()
        headers = {str(k).lower(): str(v) for k, v in page.get("headers", {}).items()}
        issues: list[dict] = []
        def issue(code: str, detail: str, priority: str = "P1") -> None:
            issues.append({"code": code, "priority": priority, "detail": detail})
        if page.get("status") != 200: issue("HTTP_NOT_200", str(page.get("status")), "P0" if public else "INFO")
        if not parsed.title.strip(): issue("TITLE_MISSING", "No title in capture")
        if not parsed.lang: issue("LANG_MISSING", "No html lang in capture")
        if parsed.h1 != 1: issue("H1_REVIEW", f"Observed {parsed.h1}; review semantics, not a ranking threshold")
        if len(parsed.canonicals) != 1:
            issue("CANONICAL_REVIEW", f"Observed {len(parsed.canonicals)} canonical links")
        elif urljoin(url, parsed.canonicals[0]) != url.split("#", 1)[0]:
            issue("CANONICAL_DIFFERENT", urljoin(url, parsed.canonicals[0]))
        directives = [{"scope": n, "value": v} for n, v in parsed.meta if n == "robots" or "bot" in n]
        if "x-robots-tag" in headers: directives.append({"scope": "x-robots-tag-review-scope", "value": headers["x-robots-tag"]})
        for directive in directives:
            if re.search(r"\b(?:noindex|none|nosnippet)\b|max-snippet\s*:\s*0\b", directive["value"], re.I):
                issue("RESTRICTIVE_DIRECTIVE_REVIEW", str(directive), "P0" if public else "INFO")
        for block in parsed.jsonld:
            try:
                value = json.loads(block)
                if not isinstance(value, (dict, list)): raise ValueError("Expected object/array")
            except ValueError:
                issue("INVALID_JSONLD", "JSON syntax/shape invalid; no schema validation performed")
        access = {}
        same_origin = urlsplit(url)[:2] == urlsplit(str(data.get("origin", "")))[:2]
        if same_origin and robot.get("status") == 200 and isinstance(robot.get("text"), str):
            for bot in SEARCH_BOTS:
                access[bot] = robots_hint(robot["text"], bot, url)
                if public and access[bot]["allowed_hint"] is False:
                    issue("ROBOTS_BLOCK_HINT", bot + ": verify with provider-compatible parser", "P0")
        else:
            access = {bot: {"allowed_hint": None, "reason": "robots-response-not-analyzed"} for bot in SEARCH_BOTS}
        reports.append({"url": url, "intended_public": public, "issues": issues,
                        "robots_hints": access, "directives_observed": directives,
                        "text_characters_heuristic": len(" ".join(parsed.text).strip()),
                        "links_observed": len(parsed.links), "jsonld_blocks": len(parsed.jsonld)})
    return {"schema_version": "1.0", "synthetic": data.get("synthetic", False),
            "observed_at": data.get("observed_at"), "pages": reports,
            "not_verified": ["live access", "WAF or bot identity", "indexation", "rendered DOM", "schema semantics", "sitemap", "provider-specific robots behavior", "citation or recommendation"],
            "notice": "Local capture triage only. No GEO score. Do not change private exclusions from this report."}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    try:
        if args.input.stat().st_size > 20_000_000: raise ValueError("Input exceeds 20 MB")
        text = json.dumps(audit(json.loads(args.input.read_text(encoding="utf-8-sig"))), ensure_ascii=False, indent=2) + "\n"
        if args.out:
            with args.out.open("x", encoding="utf-8") as handle: handle.write(text)
        else: print(text, end="")
        return 0
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        p.error(str(exc))
    return 2


if __name__ == "__main__": raise SystemExit(main())
