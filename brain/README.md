# Brain skill

`brain/` is a reusable skill named `brain`, intended to be invoked as `/brain`.

It operationalizes the supplied standing instructions: intent reading, checkable decomposition, effort placement, independent verification, `Certain`/`Likely`/`Assuming`/`Unknown` status handling, self-attack, completeness, refusal to guess, answer-first delivery, the 10 fake-competence patterns, and the mandatory FINAL GATE.

To install it, copy this directory to the local skills directory used by the host (for example `.agents/skills/brain` or `.codex/skills/brain`). Keep `SKILL.md` at the root of the directory. Then start a new task and invoke `/brain` explicitly, or use a substantive request that matches the description in the frontmatter.

The included `evals/evals.json` contains three smoke-test prompts for future iteration; it is not required for normal invocation.
