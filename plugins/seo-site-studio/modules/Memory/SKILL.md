---
name: Memory
description: Apply the user's general working preferences across projects and tasks. Use whenever the user states, corrects, or relies on a recurring preference about style, quality, communication, workflow, output format, or decision-making. Treat explicit user preferences as durable guidance until the user changes them.
---

# Memory

Use this skill as a cross-project preference layer. It is not a database and must not invent preferences. Extract durable preferences only from explicit user statements or repeated, unambiguous corrections.

## Core behavior

- Apply known preferences proactively across projects when they are relevant.
- When the user corrects a preference, use the latest correction and stop applying the superseded version.
- Do not treat a one-off request as a global preference unless the user clearly generalizes it.
- Do not claim a preference was stored globally unless this skill is actually available and loaded.
- If preferences conflict, prioritize the newest explicit instruction, then the more specific one.
- When a preference materially affects a deliverable, mention the effect briefly rather than reciting the whole memory.

## Current explicit preferences

### Visual and image generation

- Favor clean, controlled surfaces and readable forms.
- When an image is requested with a transparent background, use real alpha transparency; never draw or retain a checkerboard, grid, gray square, or other fake transparency background.
- Avoid excessive grain, noisy texture, stray micro-strokes, malformed shapes, and other artifacts that make an image look generically AI-generated.
- Do not add unnecessary decorative details or visual clutter; keep future drawings focused, clean, and visually intentional.
- Keep details intentional and subordinate to the subject, composition, and readability.
- Preserve attractive illustration quality while reducing artificial-looking visual noise.
- Avoid circular CTA buttons or decorative UI gestures that read as amateur or template-driven; prefer restrained, editorial calls to action with precise typography and spacing.

### Interface copy

- Do not add decorative arrows to button labels; keep button text plain and direct.
- Keep all button labels free of small arrow symbols or arrow icons unless the user explicitly requests one; use arrows only in separate text links when they convey navigation or an external destination.

### Portfolio presentation

- Project galleries must show screenshots of the websites and the web work, not product, brand, or campaign imagery.

### Project workflow

- When a request leaves a material design, spatial, technical, or reference
  choice ambiguous, ask for the missing element before producing a solution.
- Before changing scenes in a narrative/game project, check all objects handled or acquired in that scene and prepare the relevant inventory descriptions.
- Distinguish spoken dialogue, internal thoughts, exploration monologues, and inventory monologues when planning narrative content.
- Maintain continuity with decisions already validated by the user and flag contradictions instead of silently replacing them.
- When a project uses Three.js, consult the shared Three.js Stack Bible before making rendering, interaction, architecture, or performance decisions.
- For image-to-Three.js asset reconstruction, use the installed `img2threejs` skill and its quality gates when the source image is available.

## Updating this skill

When the user explicitly states a new general preference, add a concise entry under the most relevant category. When they revoke or revise a preference, update the entry rather than duplicating conflicting guidance. Keep this file lean and practical.
