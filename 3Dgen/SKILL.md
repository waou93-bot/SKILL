---
name: 3Dgen
description: Reconstruct a coherent game-ready low-poly 3D asset from one or more reference images. Use this skill whenever the user asks to turn an image into a 3D model, mesh, character, prop, object, game asset, GLB, OBJ, FBX, Blender model, Three.js model, or image-to-3D reconstruction—even if they do not explicitly mention `/3Dgen`.
compatibility: Requires an image input and a 3D modeling, mesh-generation, Blender, or code-generation capability. Prefer the project's existing 3D stack; if no export tool is available, provide the procedural model source and a clearly labeled preview or reconstruction specification.
---

# 3Dgen

Reconstruct the subject visible in the supplied image as a coherent, readable, game-ready low-poly 3D asset. Treat the image as evidence for shape and appearance, not as permission to invent arbitrary geometry. The most important result is a stable silhouette that holds together from multiple angles.

Apply `asset-continuity` to connect source images, reconstruction assumptions, model versions, materials, previews, turntables and exports. Reuse an existing continuity pack when the asset comes from `3Dimage`, `plancha`, a game, a comic, or another project workflow. The approved reference and locked assumptions remain canonical; an exported mesh or render cannot silently redefine them.

## Workflow

1. Confirm that an image is available and readable. If it is missing, ask the user to attach or provide it before modeling.
2. Determine the subject class: humanoid character, creature, prop, mechanical object, vehicle, environment piece, or hybrid. Apply human-specific topology rules only to humanoids; do not force a human topology onto an inanimate object.
3. Extract the evidence before building: primary silhouette, proportions, major volumes, recognizable accessories, visible seams and attachments, color blocks, materials, and the features hidden by the reference view.
4. Write down the key assumptions for unseen sides. If hidden geometry is important and cannot be inferred safely, request additional views. Otherwise use the simplest coherent continuation and label it as an approximation.
5. Build in passes: block out the major volumes, lock the silhouette and proportions, add recognizable accessories, then add colors and only the details that remain compatible with clean topology.
6. Use real geometry for silhouette-defining forms, hair masses, armor, coats, handles, rims, straps, and major accessories. Do not fake an important three-dimensional form with a flat texture or floating image plane.
7. Maintain a consistent polygon density. Keep parts connected where they should be connected and intentionally separate only when the reference shows a real assembly, articulated part, or removable accessory.
8. Review the model from the reference angle and at least two meaningful orbit angles. Correct floating parts, melted attachments, self-intersections, holes, inconsistent thickness, and accidental front/back contradictions before delivery.
9. Preserve uncertainty honestly. A single image cannot prove hidden topology, exact depth, or animation readiness; state what is measured, what is inferred, and what remains approximate.
10. Register units, axes, dimensions, hierarchy, pivots, material assignments, source-reference IDs and export versions. Compare the reference view and orbit previews to the same canon before marking the asset verified.

## Core reconstruction prompt

Use this prompt as the modeling brief. Fill in `{{reference_subject}}` and `{{target_output}}` from the user's request while keeping the priorities and failure constraints intact.

```text
You are a 3D mesh reconstruction specialist.

Reference subject:
{{reference_subject}}

Target output:
{{target_output}}

Reconstruct the subject as a coherent game-ready low poly model.

Priority order:

1. Preserve silhouette
2. Preserve proportions
3. Preserve recognizable accessories
4. Preserve colors
5. Preserve details only if topology remains clean

Rules:

- Use symmetrical human topology for humanoid characters. For non-human objects, use topology appropriate to the object's real construction and preserve symmetry only where the reference supports it.
- Produce a closed manifold mesh for every watertight part intended to be solid.
- Keep a low poly style with consistent polygon density and deliberate edge flow.
- Keep front, back, and side geometry coherent; do not design unseen sides as unrelated substitutes.
- Prefer real geometry over texture illusion for any form that affects the silhouette, volume, attachment, or gameplay readability.
- Preserve the hair silhouette when the subject has hair.
- Preserve the shoulder armor silhouette when the subject has shoulder armor.
- Preserve the coat silhouette when the subject has a coat or long garment.
- Maintain realistic or reference-consistent body proportions.
- Use a clean part hierarchy with named components, sensible pivots, and explicit attachment points when the asset is intended for a real-time scene.
- Keep materials and colors readable without allowing texture detail to hide poor geometry.

Avoid:

- spherical heads or over-rounded primary forms unless the reference clearly requires them
- floating eyes or facial parts
- melted accessories
- inflated armor
- disconnected geometry that should be attached
- random topology artifacts
- non-manifold holes, inverted normals, zero-area faces, or accidental internal shells
- flat planes pretending to be volumetric forms
- excessive subdivision that destroys the low-poly silhouette
- invented details that compete with the recognizable design

The final asset must read as the same subject from the reference angle and remain structurally coherent from other angles.
```

## Character-specific guidance

For humanoids and creatures, lock the head, torso, limb lengths, shoulder width, hip width, pose, hair mass, clothing silhouette, and accessory placement before adding surface detail. Use a mirror workflow for genuinely symmetrical anatomy, then introduce only the asymmetries visible in the reference. Keep eyes, facial features, armor, hair, straps, and coats attached to the correct parent surface rather than floating near it.

## Object-specific guidance

For props and mechanical objects, identify the primary manufactured volumes, cut lines, bevels, hinges, handles, fasteners, and contact surfaces. Prefer continuous surfaces for shells and bodies; use separate named parts for components that are visibly assembled or need independent interaction. Preserve negative spaces and openings because they often define the silhouette more strongly than surface texture.

## Quality gate

Before declaring the model complete, check:

- silhouette matches the reference at the main view
- proportions and major volumes remain stable in orbit views
- recognizable accessories are present, correctly attached, and not melted into the base form
- colors are preserved as broad readable regions
- topology is low-poly, consistent, and free of obvious artifacts
- solid parts are closed manifold meshes with usable normals
- no unintended floating pieces, gaps, intersections, duplicated limbs, or internal shells remain
- the output format and intended use are satisfied

If a gate fails, refine the geometry or request better reference images. Do not hide a geometry problem behind textures, extra smoothing, or a confident completion message.

## Delivery

When a 3D pipeline is available, produce the model in the project's native format and export a standard mesh format when requested. Include a preview or turntable if the environment supports it.

When the task is code-based, keep reconstruction data separate from rendering code, use deterministic parameters, name the generated parts, and provide the source needed to rebuild the asset.

Return a concise handoff stating the delivered files, the intended use, the main assumptions for hidden areas, and any remaining limitations.
