---
name: svelte-ui-compose
description: Select and integrate Svelte 5 marketing blocks or application UI from sv-blocks, Svelte Efferd, and Svelte QBlocks. Use when a request names these catalogs or asks to combine them; do not activate for unrelated generic frontend work.
---

# Svelte UI Compose

Build a coherent interface from the three overlapping catalogs without turning the result into a collage of demos.

## Choose the source

- Use [sv-blocks](https://sv-blocks.vercel.app/) for the broadest marketing coverage and its Normal, Mist, and Veil families.
- Use [Svelte Efferd](https://sv-efferd.pages.dev/) when a smaller, visually consistent marketing collection is preferable.
- Use [Svelte QBlocks](https://sv-particles.vercel.app/) for application primitives and patterns such as inputs, menus, accordions, avatars, and tables. The `sv-particles` hostname is historical; do not treat it as a particle-animation library.

Prefer one visual family for a page. Mix catalogs only when a missing interaction materially justifies it, then normalize typography, spacing, radii, borders, and motion.

## Integration workflow

1. Inspect the existing Svelte, Tailwind, and shadcn-svelte setup. Preserve its package manager, aliases, theme tokens, and component conventions.
2. Translate the requested page into semantic sections or interaction needs before selecting blocks.
3. Check the current upstream page, registry payload, dependencies, attribution, and license before installation. Do not rely on remembered component counts or URLs.
4. Add only the selected components through the documented `shadcn-svelte` or `jsrepo` registry flow. Treat copied source as project code and adapt it locally.
5. Replace all demo copy, placeholder links, stock identities, fake prices, and decorative images with project-appropriate content.
6. Verify mobile and desktop layouts, light and dark themes when supported, keyboard access, focus visibility, landmarks, heading order, and meaningful alternative text.

Do not overwrite existing shared primitives merely because an upstream block ships another copy. Diff overlapping files first and integrate the smallest compatible change.

## Licensing boundary

`sv-blocks` and Svelte Efferd advertise MIT licensing. The `sv-particles`/QBlocks repository may not expose an explicit license; verify its current license before copying it into commercial work. Preserve relevant upstream credits when a block is itself a port or adaptation.
