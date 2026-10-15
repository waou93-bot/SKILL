# SEO Studio 2 integration

## Operating relationship

SEO Studio 2 owns F0–F3, project orchestration, the shared state, evidence,
requirements, reviews and final handoff. `seo-site-preproduction` is a focused
G2–G5 helper. When it is invoked inside Studio, it fills existing canonical
artifacts and never creates parallel source-of-truth files.

Load this skill after the niche and site type are clear enough for architecture.
Reuse the current `00_REFLEXION.md`, `01_RECHERCHE.md`, `02_POSITIONNEMENT.md`,
`workflow.json` and `state.json`. Preserve IDs, accepted decisions and provenance.
If the brief changes, record that change in Studio's requirements before updating
dependent artifacts. Every site creation, reprise or refonte records R29 in
`03_ARCHITECTURE.md`, including template source/version, applicability, patterns
retained/adapted/rejected, evidence and impacts. On a targeted reprise, reuse a
validated current assessment or reopen only the first affected G2/G3 phase; do not
create an extra gate.

## Canonical mapping

| Skill work | SEO Studio 2 artifact |
|---|---|
| Template applicability/version, retained/adapted/rejected patterns, evidence and reprise impact (R29) | `03_ARCHITECTURE.md` |
| Search intent → page families → URL ownership → links | `03_ARCHITECTURE.md` |
| User journeys, mobile hierarchy, components, states, accessible interaction | `04_DESIGN.md` |
| Visual concept, tokens, assets, motion, fallbacks and review state | `PROJECT_SKIN.yaml` |
| Voice, claims, proof, limits, maintenance and conversion copy | `05_CONTENU.md` |
| Complete page-specific instructions | `BRIEFS/` |
| Representative article/page copy if authorized | `PILOTES/` |
| Confirmed commercial model, partner status and disclosures | `06_PARTENAIRES.md` |
| Decisions, objections and corrections | `10_DECISIONS.md` |
| Actual checks, deferred checks and visual evidence | `11_QA.md` |
| Versioned project instructions and open questions | `12_HANDOFF.md` |

In each artifact, explicitly separate niche facts, research observations,
assumptions and examples. The package's fictional sofa demo is not evidence and
does not set the next project's colors, taxonomy, product fields or business model.

## Proposed insertion for the SEO Studio 2 router

Add to Studio 2's phase-reading instructions:

> For a new SEO editorial or comparison site, load the installed
> `seo-site-preproduction` skill during G2–G3. Use its template only as an example
> of relationships between architecture, UI/UX, prose and conversion. At the start
> of each mission, adapt page families, tools, criteria, visual direction, language,
> proof and calls to action to the niche explicitly requested. Map the result to
> Studio's existing `03_ARCHITECTURE.md`, `04_DESIGN.md`, `PROJECT_SKIN.yaml`,
> `05_CONTENU.md`, `BRIEFS/`, `PILOTES/` and current evidence registers. Do not
> copy sample-specific products or claims, create a second dossier, or override
> Studio's existing gates.

This helper supplements the existing Studio contracts. It does not relax agent,
human approval, affiliate, source, security, QA or publication gates.
