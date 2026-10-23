---
name: design-dna
description: >-
  Design system and art-direction router for every visual project: website, web app,
  desktop software, mobile app, SaaS, portfolio, interactive experience, hybrid product,
  dashboard or product UI. Load this skill before proposing or implementing visual design.
  It preserves Nicolas's design DNA while creating a project-specific skin so projects
  share quality and authorship without looking like the same template.
---

# DESIGN DNA

## Mission

Never start a visual project from generic UI conventions.
Start from this Design DNA, then create a project-specific skin.

The objective is:

> Same authorial DNA. Different project identity. No template feeling.

Use the following ratio by default:

- 70% stable design logic and quality standards.
- 25% project-specific visual skin.
- 5% distinctive project exception or signature interaction.

This ratio is a design heuristic, not a rigid layout quota.

## When this skill is mandatory

Load this skill before any task involving:

- website or landing page design;
- web/mobile/desktop application UI;
- SaaS or dashboard;
- software or hybrid product;
- portfolio or case-study page;
- interactive/immersive experience;
- visual redesign or visual audit;
- design-system work;
- component styling;
- art direction, motion direction, image direction or design implementation.

Do not bypass this skill because the project already has a framework, component library,
AI-generated mockup or existing codebase.

## Core principle

Architecture before technology.

The order is:

1. Product intent.
2. Art direction concept.
3. Composition.
4. Typography.
5. Grid and spatial rhythm.
6. Imagery.
7. Interaction.
8. Motion.
9. Components.
10. Technology.

Never invert this into: component library -> cards -> gradient -> animation -> content.

## Required workflow

### 1. Read the context

Identify:

- project type;
- audience;
- user goal;
- content density;
- emotional register;
- brand maturity;
- existing approved assets and interactions;
- performance constraints;
- accessibility constraints;
- whether immersive motion/3D creates real value.

Preserve previously approved visual elements unless the user explicitly asks to replace them.
Prefer targeted correction over gratuitous redesign.

Read [Nicolas's preference profile](references/personal-preferences.md). Separate current explicit
general instructions, lessons supported by multiple projects and decisions local to one project.
Apply the relevant preferences without importing another site's palette, font pair or composition.
Preserve approved choices unless a newer instruction explicitly covers their replacement.
An audit only reports findings; a skill update does not authorize changes to a site or publication.

### 2. Create a Project Skin

For Nicolas, first apply [the niche, depth and cinematic craft contract](references/cinematic-craft.md).

Before producing final UI, create or update a `PROJECT_SKIN.yaml` using
`templates/project-skin.template.yaml`.

The skin may change:

- palette;
- image treatment;
- display type treatment;
- density;
- contrast;
- surface depth;
- motion intensity;
- texture;
- iconography;
- experimental level.

The skin must not silently change the Core Design DNA.

### 3. Establish one visual idea

Every project needs one sentence explaining its visual concept.

Good:

- "An editorial exhibition that behaves like a product interface."
- "A calm professional tool with cinematic hierarchy, not cinematic effects."
- "A music experience built as a sequence of visual chapters."

Bad:

- "Modern, clean and premium."
- "Glassmorphism with gradients."
- "Minimal SaaS style."

### 4. Compose before componentizing

Establish page/screen rhythm before deciding cards, accordions, tabs or component variants.

Prioritize:

- asymmetric but intentional composition;
- strong hierarchy;
- meaningful negative space;
- visual rhythm;
- scale contrast;
- clear focal points;
- fewer, stronger modules over repeated identical blocks.

### 5. Apply typography rules

Read `references/typography.md`.

Typography must carry part of the identity.
Never treat type as a final cosmetic layer.
Do not select Plus Jakarta Sans, Inter or a condensed grotesque automatically. Explain the
choice through this project's identity, content and reading needs; neutral UI/body text may be
appropriate. Preserve approved families unless their replacement is part of the request.

### 6. Apply motion rules

Read `references/motion.md`.

Motion is allowed when it clarifies hierarchy, creates spatial continuity, reveals content,
or strengthens the project's narrative.

Motion is not decoration.
Do not add decorative arrows to CTA buttons, including arrows revealed or animated on hover.
Keep directional/state icons when they convey an actual action or state, with accessible labels
and controls. A disclosure chevron is not a decorative CTA arrow.

### 7. Apply image direction

Read `references/image-direction.md`.

Images must feel selected or created for the project, not inserted to fill a rectangle.

### 8. Run the Anti-Slop Gate

Read `references/anti-slop.md` and remove every unmotivated generic pattern.

### 9. Run the Quality Gate

Read `references/quality-gates.md`.

Do not call a screen finished because it works technically.
It must also pass the visual, motion, performance and authorship gates.

## Core Design DNA

### A. Premium does not mean decorative

Premium means:

- precise hierarchy;
- good type;
- deliberate composition;
- controlled spacing;
- clean assets;
- crisp implementation;
- coherent motion;
- restraint;
- intentional detail.

Do not simulate premium with blur, glow, glass, gradients, noise or excessive rounding.

### B. Editorial + product

When appropriate, combine product clarity with editorial confidence:

- large typographic moments;
- full-bleed imagery;
- strong chapter breaks;
- oversized labels or numbers;
- restrained but visible art direction;
- product screenshots or real interface content where useful.

The interface must remain usable.

### C. Immersion is a tool, not the default

Immersive techniques are welcome when the project benefits from them:

- scroll-driven reveals;
- spatial transitions;
- cinematic sequencing;
- custom cursor behavior;
- parallax;
- 2.5D;
- WebGL/3D;
- sound-reactive or audio interactions.

Do not add them simply because they are technically possible.

### D. Maximum perceptual effect, minimum unnecessary complexity

Prefer a convincing 2D/2.5D illusion over expensive 3D when the user perceives the same value.
Prefer DOM/CSS for essential functionality.
Use WebGL/3D as a threshold, navigation device or meaningful scene when justified.
Always provide a robust fallback when an effect is non-essential.

### E. Keep navigation simple when the experience is visually rich

Complex content may have strong visual direction, but navigation should remain obvious.
Do not make users solve the interface.

### F. Strong visual difference between projects

Do not reuse the same hero composition, card structure, color logic or signature animation
across unrelated projects.

Reuse rules, not finished compositions.

## Preferred implementation posture

- Custom CSS/Tailwind styling is preferred over default library appearance.
- Component libraries may provide primitives, not the visual identity.
- shadcn/ui or similar libraries are acceptable for functional primitives only.
- Preserve approved third-party motion/components unless redesign was explicitly requested.
- Use progressive enhancement.
- Respect `prefers-reduced-motion`.
- Provide low-power / no-WebGL fallbacks where relevant.
- Optimize images instead of relying on low-quality assets or aggressive upscaling.
- Keep critical copy, headings, links and factual content in accessible HTML rather than images, canvas or interaction-only states.
- Preserve a logical DOM reading order and semantic heading hierarchy even when the composition is asymmetric.
- Give informative media useful alt text, captions or transcripts; keep decorative media silent to assistive technology.
- Keep visible content, metadata and structured data consistent. Do not distort the visual concept for an unverified SEO or GEO tactic.

## Handoff output for every project

A complete Design DNA handoff should include, when relevant:

1. `PROJECT_SKIN.yaml`
2. one-sentence visual concept;
3. typography choice;
4. palette and contrast model;
5. layout/grid principles;
6. image direction;
7. motion intensity and signature behaviors;
8. explicit anti-slop exclusions;
9. one distinctive project-specific visual idea;
10. implementation constraints and fallbacks;
11. semantic reading order and multimodal discoverability notes for public surfaces.

For a targeted correction, update the existing skin and return only the relevant changed
decisions, observed checks and limits; do not produce a new art direction just to fill this list.
For maintenance of this skill, consult [the decision scenarios](references/scenarios.md).
Their author walkthrough is not independent testing or proof of a site's rendered behavior.

## Organisation integration

When used with `Organisation`, this skill must run before any visual production route.

Recommended routing:

`Organisation -> Design DNA -> Project Skin -> visual concept/wireframe -> production -> Anti-Slop Gate -> Design Quality Gate`

For public surfaces intended for organic or generative discovery, continue through `seo` and, when relevant, `ai-seo` before release. Design DNA owns visual meaning; SEO owns crawl, indexation and structured data; AI SEO owns generative-platform controls and measurement. None may silently override another.

For `New Site`, `New App`, `New Pro` or equivalent project bootstrap skills:

- inherit Design DNA automatically;
- create `PROJECT_SKIN.yaml` during project setup;
- never invent a generic DA from scratch;
- never copy a previous project's skin unless explicitly requested.

## Project-specific learning

The preference profile records general instructions and local exceptions with their sources.
When working on Accord Raccord, also read `references/accord-raccord.md` if available in the
installed/project package. Preserve its approved disclosure, typography and destination rules;
do not impose that project's palette, CTA order or chevron shape on unrelated sites. If the
reference is absent, use the current project's evidence instead of inventing its decisions.

For pattern detection, `no-slop` complements the gates here: read its `references/web-review.md`
when available for a web/UI review. Design DNA owns preferences and identity, No Slop diagnoses
unmotivated patterns, and `human` handles pixel-level asset review when applicable. Do not
recursively launch these skills or present a cited skill as an executed review.


## Loading and propagation contract

Calling skills must read this actual SKILL.md before visual decisions or production, including image prompts, SVG/chart creation, UI implementation and user-visible previews. A name mention or remembered summary does not count. Read the relevant image-direction and quality-gates references before illustration/diagram work, resolving paths from this skill directory. If this skill cannot be read, report that blocker and continue only authorized non-visual work.

Apply the professional-only rule to calling-skill references, examples, default exports and any authorized delegated production. Each visual executor must read the skill and applicable approved skin before producing its part. Internal rough studies may aid reasoning; every visual presented to the user requires professional execution at its intended size. Simple or grayscale wireframes can be professional; low fidelity must never mean careless composition or unreadable labels.


## Professional illustrations and diagrams only

Never produce or deliver a cheap, crude little diagram. Only professionally executed illustrations or diagrams are acceptable, including small inline visuals, prototypes shown to the user, presentation slides, document figures and animated explainers. This is Nicolas's explicit quality constraint.

- Small or minimal can be professional: judge precision and readability, not size, ornament or complexity. Do not inflate a simple explanation into an elaborate infographic.
- Reject makeshift box-and-arrow arrangements, emoji or stock-icon collages, generic pictograms used as filler, ASCII art presented as a finished visual, inconsistent line work and tiny unreadable labels.
- Design each visual around its actual subject: clear information hierarchy, intentional composition, coherent geometry and line weights, aligned labels, controlled spacing, restrained palette and typography matching the project.
- For explanatory or data diagrams, verify relationships, directions, scales, units and labels. Never fabricate data or let generated artwork invent factual details. Keep critical text and data editable where practical.
- Choose the medium that can meet the standard: art-directed raster illustration, precise SVG/vector diagram, professionally styled chart or interactive visual. SVG, Canvas, CSS and Mermaid are tools, not evidence of quality; inspect their rendered output.
- Internal sketches may support reasoning, but must never be presented as finished illustrations or diagrams. A polished hand-drawn style is allowed when deliberately requested; careless execution is not.
- Inspect at the real display/export size and in its page, slide or document. Correct clipping, crossings, crowded labels, artifacts and weak composition before delivery. If professional production or inspection is unavailable, report the limitation and provide a clear textual explanation rather than substituting a low-grade visual.

Apply the illustration/diagram checks in `references/image-direction.md` and `references/quality-gates.md`. A failed visual blocks final visual acceptance; effects, animation and the word "premium" cannot excuse it.


## Button labels

Do not add small decorative arrows to buttons or call-to-action links. Use a clear text label without arrow glyphs or arrow icons. Preserve functional direction controls only when direction itself is the action (for example previous/next navigation). This is Nicolas's explicit design preference.


## Nicolas's mandatory finish: niche, depth and cinematic direction

For Nicolas's projects, read references/cinematic-craft.md before choosing the skin,
components or motion. This explicit preference applies across websites and product UI:
a polished, authored result with perceptible depth and cinematic composition appropriate
to the actual niche. A flat generic template or an off-topic visual universe fails.
Cinematic means deliberate framing, layers, light/material, typography, pacing and
continuity; it does not require dark mode, 3D, a video intro or constant animation.

Preserve approved controls and prior project work. Inspect the actual existing buttons,
cards/tiles, inputs and selection states before replacing them. Reuse their demonstrated
interaction quality, while deriving imagery, palette and composition from this niche.
Never claim to have studied unavailable earlier examples.

The skin and design-system must document niche evidence, depth strategy, cinematic
sequence, component states, selected tools and reduced-motion/performance fallbacks.
At template pilot and final acceptance, inspect rendered desktop/mobile screens and
interactions against those decisions. Fix niche mismatch, flatness and unfinished
controls before visual acceptance. A successful build is not visual acceptance.


## Hero illustré par défaut — instruction du 15 octobre 2026

Sur tous les sites, le hero utilise par défaut une illustration de niche au format
source 16:9, en fond sur toute la surface du hero, bord à bord. Ce n'est pas une
vignette ni un visuel dans une colonne. Choisir un sujet et un cadrage cohérents avec
la niche ; préserver des zones calmes derrière les textes et CTA.
Le format 16:9 qualifie le média source : la hauteur du hero reste responsive.
Utiliser une couverture cover et un point focal explicite ; prévoir le recadrage mobile.
Ne pas étirer l'image ni imposer un hero mobile si haut qu'il cache les produits.
Préserver lisibilité, contraste et accès immédiat aux actions. Optimiser le média LCP,
réserver son espace et ne pas charger tardivement l'image principale.
Une illustration ne constitue pas une photo d'un produit exact ni une preuve de test.
Le choix du média respecte les droits/provenance et ne nécessite aucun outil payant.
Consigner dans le skin source, ratio, point focal desktop/mobile, traitement de contraste
et contrôle du cadrage. En refonte, intégrer cette préférence dans le design validé.
