---
name: srcp
description: Safely create a Git backup and recovery checkpoint, then commit and push a repository. Use when the user asks to save, checkpoint, commit, or publish Git work and wants a recoverable state before the push.
---

# SRCP

Create a recoverable Git checkpoint before publishing work. Use this skill only for an explicitly requested save, commit, or push workflow; it changes the repository and its remote.

## Establish the scope

- Read the repository's applicable instructions before changing files.
- Identify the repository root, current branch, target remote, and `git status --short`.
- Make sure the user has authorized committing every listed change. If unrelated or surprising files are present, ask what to include rather than staging everything.
- Flag potentially sensitive files such as `.env`, credentials, private keys, or database dumps. Do not commit them merely because the user asked for a backup.
- Do not use `git reset --hard`, force-push, amend an existing commit, or overwrite a remote branch as part of SRCP.

## Recovery checkpoint

Before staging, SRCP records the current `HEAD` in two local recovery artifacts:

- an annotated tag named `srcp/checkpoint-<timestamp>`;
- a Git bundle and a status snapshot under `.git/srcp-backups/`.

The tag is pushed after a successful branch push. The bundle remains local, so it can recover the pre-operation history even if the remote is unavailable. If the repository has no first commit yet, explain that no pre-operation `HEAD` exists; create and push the checkpoint tag after the first successful commit instead.

## Execute

Use [scripts/srcp.ps1](scripts/srcp.ps1) for a consistent Windows workflow.

1. Run it without `-Execute` first. This is a read-only preview of the branch, remote, status, and planned checkpoint.
2. Run it with `-Execute` only after the commit scope and message are explicit. Its default is intentionally non-mutating.
3. Use a descriptive commit message supplied or approved by the user. If nothing is staged after the approved scope is selected, do not create an empty commit; report that no publication was needed.
4. If the remote rejects the push, stop and report the rejection. Do not rebase, merge, or force-push automatically.

Example:

```powershell
# Preview
& "$skillPath/scripts/srcp.ps1" -RepositoryPath "C:\path\to\repo" -Message "chore: save current work"

# Execute after the scope is confirmed
& "$skillPath/scripts/srcp.ps1" -RepositoryPath "C:\path\to\repo" -Message "chore: save current work" -Execute
```

`$skillPath` is the installed `srcp` skill directory. Agents may instead invoke the script with its absolute path.

## Optional Windows system restore point

A Git checkpoint is the default recovery point. Create a Windows system restore point only when the user specifically asks for one, using `-CreateSystemRestorePoint`. It must run in an elevated Windows session with System Protection available. If either requirement is unavailable, report it and continue with the Git checkpoint only if the user still wants that.

## Completion report

State the repository, branch, commit SHA (or that no commit was needed), checkpoint tag, local bundle path, whether an optional system restore point was created, and branch/tag push results. Mention any skipped sensitive files or remote rejection clearly.
