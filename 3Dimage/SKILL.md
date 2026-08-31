---
name: 3Dimage
description: Generate or refine professional orthographic character turnaround references for 3D reconstruction. Use this skill whenever the user asks for a 3D reference sheet, character turnaround, front/side/back views, orthographic views, an image-to-3D reference, a game-ready silhouette sheet, or a consistent multi-view character image—even if they do not explicitly mention the skill or use the term “turnaround.”
compatibility: Requires an image-generation or image-editing capability. If that capability is unavailable, return the finalized generation prompt instead.
---

# 3Dimage

Create technically useful character references for 3D reconstruction. The goal is readable, coherent geometry—not a beauty illustration, concept-art mood piece, or cinematic presentation.

Always apply `asset-continuity` because the four views describe one canonical asset. Register the supplied reference, the locked character specification, the turnaround, and any corrected version under stable IDs. Treat the resulting turnaround as canonical only after the cross-view quality gate passes; preserve earlier versions rather than silently replacing them.

## Operating procedure

1. Extract the user's character specification and preserve the identity-defining details: body type, clothing, armor, accessories, hairstyle, colors, materials, proportions, and any intentional asymmetry.
2. If the user provides a reference image, treat it as the source of truth for identity and proportions. Preserve the same character in every view; do not redesign the character between angles.
3. Choose a neutral pose. Use a T-pose by default; use an A-pose when it makes the silhouette or overlapping limbs easier to read, or when the user requests it.
4. Generate one clean turnaround image containing exactly four views in this order: front, left side, back, right side. Use a simple evenly spaced arrangement with no decorative board, no labels, and no captions.
5. Keep the camera orthographic and the framing identical across all views. Align the head height, foot baseline, body centerline, and overall scale so the views can be compared directly.
6. Inspect the result for reconstruction blockers before returning it: perspective distortion, cropped extremities, inconsistent clothing, missing back details, mirrored asymmetry, extra limbs, changing facial features, cast shadows, text, or decorative graphics. If an edit pass is available, correct those issues before delivery.
7. Record the invariant geometry, materials, intentional asymmetries, scale assumptions, and remaining unknowns in the continuity pack so `3Dgen` and later derivatives use the same canon.

## Generation brief

Build the final image from the following structure. Insert the user's character description where indicated, then keep the technical constraints intact.

```text
You are a professional 3D concept artist creating orthographic references for AI 3D reconstruction.

CHARACTER SPECIFICATION:
{{user_character_description}}

Create one professional character turnaround reference showing the exact same character in four views, in this exact order:
1. front view
2. left side view
3. back view
4. right side view

Technical requirements:
- orthographic projection in every view; no perspective and no converging lines
- the same exact character, proportions, pose, clothing, accessories, materials, colors, and asymmetries in all four views
- neutral T-pose by default, or a clear A-pose if specified
- full body visible from head to feet, with hands, feet, hair, clothing, and props fully inside the frame
- identical scale, vertical alignment, camera height, and foot baseline across all views
- front-facing and side-facing silhouettes must be easy to trace into 3D geometry
- symmetrical geometry unless the character specification intentionally includes asymmetry
- low-poly styling with large, clearly readable geometric forms and a game-ready silhouette
- show construction-relevant shapes clearly; avoid tiny surface detail that obscures the primary forms
- pure white background
- flat, even, neutral studio illumination only
- no cast shadows, contact shadows, ambient dramatic shading, depth of field, bloom, fog, rim light, or cinematic lighting

Layout requirements:
- four views only, evenly spaced, with generous separation
- no presentation board, border, frame, grid, decorative background, floor, pedestal, or props unrelated to the character
- no text, labels, arrows, logos, watermarks, captions, or measurements

Consistency checks:
- do not invent a second design for the back or side views
- do not mirror or remove an asymmetric item; show its correct position from each angle
- do not alter the pose, limb length, head shape, costume construction, or accessory placement between views
- do not crop any body part
- do not add extra characters, duplicate limbs, extra fingers, or anatomy errors

The result must look like a clean, production-ready 3D artist turnaround reference intended for reconstruction, not a finished illustration.
```

## Handling incomplete specifications

If the user has not supplied a character design, ask for a concise character description before generating when the missing information would materially change the model. At minimum, request the subject's species or human type, body proportions, outfit or armor, hairstyle, colors, and important accessories. If the user clearly wants you to invent the design, create a simple coherent low-poly character and keep every invented attribute fixed across all four views.

Do not add unnecessary lore, scenery, dramatic action, or visual effects. Any detail that is not useful for reconstructing the mesh should be omitted or kept subordinate to the major forms.

## Reference-image edits

When editing an existing character image, preserve the character's identity and use the edit only to improve multi-view consistency, orthographic framing, background cleanliness, missing angles, or reconstruction readability. Do not beautify, redesign, stylize into a different character, or replace the supplied costume unless the user explicitly asks for that change.

## Delivery

When image generation is available, generate the image and return it with a brief note confirming that it is a four-view orthographic reconstruction reference. Do not bury the result under a long explanation.

When image generation is unavailable, return the completed generation brief with the character specification filled in, ready to paste into an image model.
