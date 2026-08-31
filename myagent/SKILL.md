---
name: myagent
description: Local Agentic Harness launcher for controlled software missions. Use this skill whenever the user says /myagent, $myagent, myagent, "lance le harness", "mission agentique", "run sous harness", or wants Codex to run or prepare an auditable agent task on an existing or future Git project with worktrees, ledger, policy gates, verification commands, and a final report.
---

# MyAgent

Use this skill to run the local Agentic Harness instead of improvising a raw agent session.

The harness is a control layer for software missions: it creates an isolated Git worktree, writes a task prompt, records a SQLite ledger, checks command policy, optionally runs an agent command, runs verification, and produces a Markdown report.

## Default Harness Location

Read `references/harness-location.md` before running commands. It records the default harness path and the portable override variables.

Prefer the bundled script:

```powershell
python scripts/run_harness.py --help
```

If `python` is unavailable, use the Codex bundled Python path from the current environment when known.

## Workflow

1. Identify the target Git repository.
   - If the current workspace is a Git repo, use it.
   - If not, ask for the repo path unless the user already gave it.
   - Do not initialize or mutate a repo just to make the harness run unless the user explicitly asks.

2. Capture a bounded objective.
   - Prefer one mission with one observable result.
   - If the request touches bank, billing, legal, production deploy, secrets, customer data, destructive deletes, or mass messaging, keep it as a proposal/report unless the user explicitly approves the next gate.

3. Choose the mode.
   - `prepare`: create a worktree, prompt, ledger entry, and report without starting an agent process.
   - `verify`: run the mission setup plus the configured check command.
   - `execute`: run an external agent command through the harness, then verify if a check is provided.

4. Use a verification command whenever possible.
   - For unknown projects, start with a harmless check such as `git status --short`.
   - For real code changes, prefer the repo's existing test, lint, typecheck, or build commands.
   - Do not invent a destructive or network-heavy check.

5. Run the wrapper script from the skill directory.

Prepare-only example:

```powershell
python scripts/run_harness.py prepare --repo "C:\path\to\repo" --objective "Audit the onboarding flow" --check "git status --short"
```

Verify example:

```powershell
python scripts/run_harness.py verify --repo "C:\path\to\repo" --objective "Check the project health" --check "npm test"
```

Execute example:

```powershell
python scripts/run_harness.py execute --repo "C:\path\to\repo" --objective "Implement the pricing copy change" --agent-command "your-agent --cwd {worktree} --prompt-file {prompt_file}" --check "npm test"
```

6. Report back with:
   - the run id;
   - the report path;
   - final status;
   - verification result;
   - any policy block or approval needed;
   - the next human decision.

## Safety Defaults

Treat these as human-gated even if a user asks for broad autonomy:

- bank connection, payouts, refunds, charge creation;
- production deploys and domain/DNS changes;
- secrets, tokens, keychains, credentials;
- legal terms, privacy policy, customer contracts;
- real customer data exports or mass edits;
- ad spend, mass emailing, support auto-replies;
- recursive deletes or irreversible Git operations.

The harness may prepare a plan around those areas, but it should not execute them without an explicit, narrow approval.

## If The Harness Is Missing

If the wrapper cannot find the harness, tell the user exactly which path was checked and suggest either:

- setting `MYAGENT_HARNESS_PATH` to the harness folder;
- copying/installing the harness into a stable location;
- recreating it from the project MASTER.

Do not silently fall back to a raw agent run when the user asked for `/myagent`.

