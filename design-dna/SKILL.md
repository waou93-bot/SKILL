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

### 2. Create a Project Skin

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

### 6. Apply motion rules

Read `references/motion.md`.

Motion is allowed when it clarifies hierarchy, creates spatial continuity, reveals content,
or strengthens the project's narrative.

Motion is not decoration.

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
10. implementation constraints and fallbacks.

## Organisation integration

When used with `Organisation`, this skill must run before any visual production route.

Recommended routing:

`Organisation -> Design DNA -> Project Skin -> visual concept/wireframe -> production -> Anti-Slop Gate -> Design Quality Gate`

For `New Site`, `New App`, `New Pro` or equivalent project bootstrap skills:

- inherit Design DNA automatically;
- create `PROJECT_SKIN.yaml` during project setup;
- never invent a generic DA from scratch;
- never copy a previous project's skin unless explicitly requested.
