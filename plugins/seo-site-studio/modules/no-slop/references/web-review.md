# Focused web and UI pattern review

Design DNA chooses identity and stores personal preferences; this pass detects where a
pattern has no role or contradicts the actual content. Consult its preference profile when
available. A serif, glass surface, 3D scene or animation is not defective merely by category:
assess purpose, approved context, readability and evidence.

| Pattern to inspect | Observable evidence | Correction boundary |
|---|---|---|
| Decorative CTA arrows | Arrow contributes no direction/state information, including hover-only SVG, icon or pseudo-element | Remove embellishment within the requested fix. Preserve useful next/previous, disclosure, state and external-destination indicators with accessible controls. Do not treat every chevron as a CTA arrow. |
| Automatic typography | Family/pair copied from an unrelated template with no project reason; typography/hierarchy does not fit actual content | Flag selection/hierarchy and use Design DNA's choice process. Neutral UI/body can be justified. Do not purge approved Georgia/Times, Plus Jakarta Sans, Inter or all familiar fonts by name. |
| Commercial excess | Repeated combo/trial/offer prompts compete before users can understand or compare; wording implies benefits not demonstrated | Reduce repetition and subordinate prompts to useful content. Preserve real purchase routes and needed conditions. Exact CTA/promotion order belongs to the project. |
| Motion with no role or competing motion | Several visible effects draw attention simultaneously, hover ornament distracts, loader delays access, intro replays against approved behavior | Diagnose the visible sequence and simplify within scope. Preserve purposeful transitions and approved replay/positions; reduced-motion and usable fallbacks remain required. |
| Generic or misleading product imagery | Visible item type/color/orientation/proportions contradict label or source; generated illustration presented as exact product | Match authorized reference or label illustration/similarity honestly. Use human for pixel inspection if available/applicable; do not declare exactness from prompt text or generation success. |
| Compressed mobile reading | Actual tables/comparisons show cramped word spacing, arbitrary letter breaks, unsuitable forced line breaks, clipped labels or tiny text | Correct measure, spacing, wrapping and table treatment without removing necessary comparison information. Test final narrow/mobile states; source CSS alone is not evidence of a rendered pass. |

Readability and motion checks describe the actual browser/viewport/device. A resized desktop
viewport does not prove Safari iOS or Chrome Android compatibility; use site-checklist's
separate platform gate when mobile readiness is in scope. Do not install missing tools just
to turn an unverified result into a claimed pass.

Preserve successful parts and change only demonstrated problems. A text/DOM scan can locate
patterns but cannot determine every icon's purpose, imagery accuracy or visual hierarchy.
If context is missing, state the hypothesis and needed evidence instead of an absolute ban.
