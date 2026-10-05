# Design DNA Skill

A reusable cross-project art-direction skill.

## Purpose

Use one stable design DNA across websites, apps, desktop software, SaaS, portfolios and hybrid experiences without making every project look identical.

## Install

Copy the `design-dna-skill` folder into the skills directory used by your agent/Codex setup.
The entry point is `SKILL.md`.

If your setup supports project bootstrap hooks, load `design-dna` before any visual task.

## Suggested Organisation hook

Add a routing rule equivalent to:

```text
IF task affects visual UI, UX presentation, art direction, motion, imagery, layout, styling or design implementation:
  LOAD design-dna
  CREATE/UPDATE PROJECT_SKIN.yaml
  RUN anti-slop gate before approval
  RUN design quality gate before marking complete
```

## Project use

At the start of a project, duplicate:

`templates/project-skin.template.yaml`

as:

`PROJECT_SKIN.yaml`

Then fill only the project-specific layer.

Do not copy an old project's skin as a shortcut unless the user explicitly requests a shared visual universe.
