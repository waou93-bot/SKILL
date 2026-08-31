---
name: svelte-motion-effects
description: Select, integrate, or review animated Svelte 5 components from Svelte Animations and loading indicators from Svelte Dot Matrix. Use for deliberate UI motion and async feedback; do not activate for video animation or unrelated CSS transitions.
---

# Svelte Motion Effects

Use [Svelte Animations](https://sv-animations.vercel.app/) for content and interaction effects. Use [Svelte Dot Matrix](https://sv-matrix.vercel.app/) for loading indicators. Do not use QBlocks merely because its hostname contains `particles`.

## Select motion by purpose

- Use entrance or emphasis effects to explain hierarchy, continuity, or state change.
- Use a loader only where work is actually pending; prefer local feedback near the triggering control over a blocking full-screen animation.
- Keep one motion language per surface. Avoid combining multiple attention-seeking effects in the same viewport.

## Integration workflow

1. Inspect existing motion utilities, Svelte version, Tailwind setup, SSR boundaries, and performance constraints.
2. Verify the current upstream registry payload, dependency versions, license, and attribution before adding a component.
3. For Dot Matrix, install its documented shared foundation before an individual loader and avoid duplicating that foundation.
4. Expose meaningful parameters through project tokens or typed props; do not scatter arbitrary durations, easing curves, or colors.
5. Remove showcase-only effects and ensure completion, cancellation, navigation, and repeated-trigger behavior remain correct.

## Motion requirements

- Honor `prefers-reduced-motion` with a static or substantially reduced alternative.
- Do not delay access to content for decorative animation.
- Prefer transform and opacity animation; measure expensive blur, shadow, filter, and large matrix effects on target devices.
- Prevent layout shifts by reserving final geometry and avoid animation loops that consume resources off-screen.
- Give loaders accessible status semantics without repeatedly announcing decorative frame changes.
- Test hydration, route changes, rapid toggles, background tabs, and animation cleanup after component destruction.
