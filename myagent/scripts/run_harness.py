#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


DEFAULT_HARNESS = Path(r"C:\Users\Nicolas JEZ\Documents\Codex\2026-08-08\tu\outputs\agentic-harness")
DEFAULT_PYTHON = Path(r"C:\Users\Nicolas JEZ\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe")
DEFAULT_GIT = Path(r"C:\Users\Nicolas JEZ\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe")


def existing_path(raw: str | None, fallback: Path) -> Path:
    if raw:
        return Path(raw)
    return fallback


def resolve_python() -> str:
    configured = existing_path(os.environ.get("MYAGENT_PYTHON"), DEFAULT_PYTHON)
    if configured.exists():
        return str(configured)
    return sys.executable


def resolve_harness() -> Path:
    return existing_path(os.environ.get("MYAGENT_HARNESS_PATH"), DEFAULT_HARNESS)


def resolve_git() -> str | None:
    configured = existing_path(os.environ.get("MYAGENT_GIT"), DEFAULT_GIT)
    if configured.exists():
        return str(configured)
    return None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the local Agentic Harness through the myagent skill.")
    sub = parser.add_subparsers(dest="mode", required=True)

    for mode in ("prepare", "verify", "execute", "list", "show", "policy-check"):
        cmd = sub.add_parser(mode)
        cmd.add_argument("--home", default=None, help="Harness state directory. Defaults to <harness>/.harness.")
        if mode in {"prepare", "verify", "execute"}:
            cmd.add_argument("--repo", required=True)
            cmd.add_argument("--objective", required=True)
            cmd.add_argument("--check", default=None)
            cmd.add_argument("--approve", action="append", default=[])
            cmd.add_argument("--timeout", type=int, default=900)
        if mode == "execute":
            cmd.add_argument("--agent", default="manual")
            cmd.add_argument("--agent-command", required=True)
        if mode == "show":
            cmd.add_argument("run_id")
        if mode == "policy-check":
            cmd.add_argument("--cmd", required=True)
            cmd.add_argument("--approve", action="append", default=[])

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    harness = resolve_harness()
    if not harness.exists():
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "harness_not_found",
                    "checked": str(harness),
                    "hint": "Set MYAGENT_HARNESS_PATH to the agentic-harness folder.",
                },
                indent=2,
            )
        )
        return 2

    python = resolve_python()
    home = Path(args.home) if args.home else harness / ".harness"

    command = [python, "-m", "agentic_harness"]
    env = os.environ.copy()
    git = resolve_git()
    if git:
        env["AGENTIC_HARNESS_GIT"] = git

    if args.mode == "prepare":
        command += ["run", "--home", str(home), "--repo", args.repo, "--objective", args.objective]
        if args.check:
            command += ["--check", args.check]
    elif args.mode == "verify":
        command += ["run", "--home", str(home), "--repo", args.repo, "--objective", args.objective, "--verify"]
        if args.check:
            command += ["--check", args.check]
    elif args.mode == "execute":
        command += [
            "run",
            "--home",
            str(home),
            "--repo",
            args.repo,
            "--objective",
            args.objective,
            "--execute",
            "--agent",
            args.agent,
            "--agent-command",
            args.agent_command,
        ]
        if args.check:
            command += ["--check", args.check, "--verify"]
    elif args.mode == "list":
        command += ["list", "--home", str(home)]
    elif args.mode == "show":
        command += ["show", "--home", str(home), args.run_id]
    elif args.mode == "policy-check":
        command += ["policy-check", "--home", str(home), "--cmd", args.cmd]

    for approval in getattr(args, "approve", []) or []:
        command += ["--approve", approval]

    result = subprocess.run(command, cwd=harness, env=env, text=True)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

