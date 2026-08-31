# Harness Location

Default harness path:

```text
C:\Users\Nicolas JEZ\Documents\Codex\2026-08-08\tu\outputs\agentic-harness
```

Default Git path used by the local Codex runtime:

```text
C:\Users\Nicolas JEZ\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\git\cmd\git.exe
```

Default Python path used by the local Codex runtime:

```text
C:\Users\Nicolas JEZ\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
```

Environment overrides:

- `MYAGENT_HARNESS_PATH`: points to the `agentic-harness` folder.
- `MYAGENT_PYTHON`: Python executable used to run the harness.
- `MYAGENT_GIT`: Git executable exposed to the harness as `AGENTIC_HARNESS_GIT`.

The wrapper script checks overrides first, then the defaults above.

