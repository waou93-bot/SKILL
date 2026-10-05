#!/usr/bin/env python3
"""Offline, conservative referral signal classifier. No network or persistent IDs."""
from __future__ import annotations
import argparse
import json
import re
from urllib.parse import parse_qs, urlsplit

DOMAINS = {"chatgpt.com": "ChatGPT", "chat.openai.com": "ChatGPT",
           "perplexity.ai": "Perplexity", "claude.ai": "Claude",
           "gemini.google.com": "Gemini", "copilot.microsoft.com": "Copilot"}
ALIASES = {**DOMAINS, "chatgpt": "ChatGPT", "perplexity": "Perplexity",
           "claude": "Claude", "gemini": "Gemini", "copilot": "Copilot"}
BOT = re.compile(r"(?:^|[^a-z0-9])(?:OAI-SearchBot|GPTBot|ChatGPT-User|PerplexityBot|Perplexity-User|ClaudeBot|Claude-User|Claude-SearchBot|Googlebot|bingbot)(?:[/\s;)]|$)", re.I)


def host_of(url: str) -> str:
    try:
        parsed = urlsplit(url)
        if parsed.scheme.lower() not in ("http", "https") or parsed.username or parsed.password:
            return ""
        return (parsed.hostname or "").lower().rstrip(".")
    except ValueError:
        return ""


def platform_for_host(host: str) -> str | None:
    return next((p for domain, p in DOMAINS.items()
                 if host == domain or host.endswith("." + domain)), None)


def classify(landing_url: str, referrer: str = "", user_agent: str = "") -> dict:
    if not host_of(landing_url):
        raise ValueError("landing-url must be an absolute HTTP(S) URL without credentials")
    params = parse_qs(urlsplit(landing_url).query, keep_blank_values=True, max_num_fields=100)
    sources = [v.strip().lower() for v in params.get("utm_source", [])]
    duplicate = len(sources) > 1
    source = sources[0] if len(sources) == 1 else ""
    utm_platform = ALIASES.get(source)
    ref_host = host_of(referrer)
    ref_platform = platform_for_host(ref_host)
    conflict = duplicate or bool(source and ref_platform and utm_platform != ref_platform)
    bot = bool(BOT.search(user_agent))
    # Preserve a non-AI campaign rather than replacing it with an assistant referrer.
    if bot:
        channel = "machine_user_agent_signal"
    elif conflict:
        channel = "conflicting_signals"
    elif source and not utm_platform:
        channel = "other_campaign"
    elif utm_platform:
        channel = "declared_ai_campaign"
    elif ref_platform:
        channel = "observed_ai_referral"
    elif ref_host:
        channel = "other_referral"
    else:
        channel = "unknown"
    return {"channel": channel, "platform_signal": utm_platform or ref_platform,
            "utm_platform_signal": utm_platform, "referrer_platform_signal": ref_platform,
            "referrer_host": ref_host or None, "conflict": conflict,
            "machine_user_agent_signal": bot, "human_verified": False,
            "organic_verified": False, "recommendation_verified": False,
            "notice": "Declarative signals only; absent referrer stays unknown. Domains require periodic review."}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--landing-url", required=True)
    p.add_argument("--referrer", default="")
    p.add_argument("--user-agent", default="")
    args = p.parse_args()
    try:
        print(json.dumps(classify(args.landing_url, args.referrer, args.user_agent), indent=2))
        return 0
    except ValueError as exc:
        p.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
