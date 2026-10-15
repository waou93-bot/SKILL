---
name: seo-site-preproduction
description: >-
  Use when a user asks to structure, plan, create, resume, take over, or refactor an SEO
  editorial, comparison, affiliate, or content-led site, or to adapt the bundled
  website template to a requested niche. Combines the actual design-dna and
  redaction-editoriale-web skills with the included example site. Make the
  requested niche the source of every page, UX choice, proof, claim, and conversion;
  never carry the sofa demo into a different niche. Align deliverables to SEO Studio 2
  when it is coordinating the project.
---

# SEO site preproduction

Turn the SEO site example into a niche-specific preproduction package. Use the
bundled pages as examples of useful relationships between architecture, interface,
content and conversion. The example is not a universal site or a replacement for
the user's project decisions.

## Priority rule: adapt to the requested niche

Read [`assets/template-demo/TEMPLATE_RULES.md`](assets/template-demo/TEMPLATE_RULES.md)
before reusing any bundled page or asset. The sofa comparison site is fictional
demonstration material. Unless the user explicitly requests a sofa site, rebuild
its taxonomy, page types, criteria, filters, tools, examples, vocabulary, visual
direction, evidence and conversion around the niche stated in the current request.
Do not make a mechanical word replacement. Keep only structure that serves the
new audience's task, and remove everything else. Never carry over fabricated
products, prices, reviews, results, expertise or affiliate relationships.

For affiliate work, the bundled homepage is specifically **not** a passing landing
example: it leads with a measuring tool and its products are synthetic, without real
images, prices or merchant offers. Do not inherit that order. Use the verified
catalogue and the affiliate contracts in SEO Studio 2 references 24 and 26 to put
real product choices and usable affiliate CTAs in the first useful viewport, then
place relevant tools and editorial routes around that choice. If the catalogue is
not verified, keep the project blocked; do not fill the component with demo items.

## When SEO Studio 2 coordinates

Use SEO Studio 2 as the project orchestrator and its current dossier as the single
source of truth. Do not restart F0–F3, overwrite accepted decisions, duplicate its
state/workflow registers, or create competing versions of its deliverables. Apply this skill for a creation or whenever a reprise/refonte touches architecture,
experience, content or conversion. On a targeted reprise, first inspect R29 and the
existing evaluation; reuse it only while its scope and evidence remain current. Reopen
the first affected G2/G3 phase when the niche, audience, tasks or existing site have
changed. Update the existing artifacts and link evidence through Studio registers. Read
[`references/seo-studio-2-integration.md`](references/seo-studio-2-integration.md)
for the file-by-file mapping and [`references/27-template-site-preproduction.md`](references/27-template-site-preproduction.md)
for its G2–G5 structure. Keep SEO Studio 2's permissions, gates, review and handoff
rules in force.

## Workflow

1. **Set scope.** Extract niche, site type, audience, visitor task, geography,
   language, business model, constraints and requested level of completion from the
   brief and existing project files. Separate evidence, assumptions and unknowns.
   Ask only for information that blocks a material decision; do independent work
   meanwhile.
2. **Read the real companion skills.** Before shaping the visual system, apply the
   installed `design-dna` skill. Before drafting or revising reader-facing prose,
   apply `redaction-editoriale-web`. Do not copy their bodies into this skill or
   claim to have run them if unavailable; record the dependency and continue only
   with work that does not rely on it.
3. **Ground the architecture.** Use the requested niche, search intent, evidence
   and business constraints to choose page families, URL policy, navigation,
   taxonomy and internal links. Treat the page patterns in
   [`references/preproduction-map.md`](references/preproduction-map.md) as a menu
   of possible structures, not a fixed sitemap.
4. **Specify the experience.** Define the key user journeys, responsive templates,
   navigation, tools, filters, product/service facts, empty/error states,
   accessibility and interaction behavior for this niche. Make the interface help
   the visitor decide before asking for a conversion.
5. **Set the design direction.** Create a project-specific `PROJECT_SKIN.yaml` and
   describe visual concept, tokens, typography, asset direction, motion, responsive
   composition, fallbacks and quality gates. Do not reuse the sofa palette or
   measurement-table concept by default.
6. **Set the editorial and selling system.** Define audience vocabulary, page
   intent, answer-first structure, evidence rules, tone, proof limits, CTA language,
   commercial disclosure and maintenance. Write one complete representative brief
   or pilot only when the scope asks for it; attach claims to sources or mark them
   `[À VÉRIFIER]`.
7. **Map the handoff.** Give each page and component an owner, source of truth,
   evidence, dependencies, acceptance criteria and next gate. Keep the backlog
   separate from V1. Do not declare a design approved, a test executed, or a page
   ready when it has not been checked.
8. **Build only on request.** This skill prepares preproduction by default. Generate
   or adapt site code only when the user asks for implementation; never publish,
   contact a partner, spend money, submit a form or deploy implicitly.

## Preproduction deliverables

When working within SEO Studio 2, fill its canonical files rather than creating a
second dossier:

- `03_ARCHITECTURE.md`: niche-adapted page map, intent, URL/indexing policy,
  taxonomy, navigation, relationships and internal-link destinations.
- `04_DESIGN.md` and `PROJECT_SKIN.yaml`: journey, responsive templates, component
  states, visual system, asset rights, accessibility and planned visual checks.
- `05_CONTENU.md`, `BRIEFS/` and `PILOTES/`: prose doctrine, page briefs, audience
  language, answer/evidence/limitation/action coverage, CTA rationale and sourced
  pilots when applicable.
- `06_PARTENAIRES.md`: actual conversion model, partner status and disclosures only
  when commercial partners apply; otherwise state the reason and exclude them.
- `10_DECISIONS.md`, `11_QA.md` and `12_HANDOFF.md`: adaptation decisions, review
  evidence, unresolved checks and versioned handoff.
- `state.json` and `workflow.json`: current requirements, artifacts, sources,
  evidence, gates and workflow events as SEO Studio 2 defines them. Mark R29 verified
  only after the assessment and its evidence are recorded.

For work outside SEO Studio 2, create a similarly traceable dossier with one
canonical file per concern. Never treat this sample as evidence or as validated
design for the next niche.

## Release checklist

- [ ] The user's requested niche determines the actual page map, design, prose and conversion.
- [ ] No sofa-specific product, measurement, label, asset or sales claim remains unless requested.
- [ ] Every page has a distinct reader task, search intent, owner and internal-link role.
- [ ] Every material claim has a source or a visible verification status.
- [ ] The visual direction is project-specific and the skin records its fallbacks and review state.
- [ ] CTA and partner treatment match the confirmed business model.
- [ ] Existing SEO Studio 2 decisions, evidence, IDs and gates remain intact.
- [ ] R29 records template applicability for new work and reprises; stale decisions reopen only affected phases.
- [ ] Open questions, non-applicable items and unverified checks are explicit.
