---
name: human-reading
description: Human visual QA for final deliverables. Use when checking PDFs, slide decks, screenshots, dashboards, websites, images, documents, prototypes, or UI before delivery for text readability, contrast, tone-on-tone colors, text over images, dark-on-dark or light-on-light issues, clipping, visual hierarchy, and whether a human can comfortably read the artifact at final size.
---

# Human Reading

## Purpose

Perform a human-style reading pass on final visual artifacts. Do not rely on thumbnails, layout JSON, automated overflow checks, or “looks okay from far away.” Inspect the artifact as a person would consume it.

## Required Workflow

1. Render the final artifact to images at the actual delivery size.
   - PPTX: render every slide to PNG.
   - PDF/DOCX: render every page to PNG.
   - Website/app: capture desktop and mobile screenshots.
   - Image/dashboard: inspect the final exported image directly.
2. Inspect every page/screen individually at readable size, not only in a contact sheet.
3. Check all text against its immediate visual environment:
   - dark text on dark fills;
   - pale text on pale fills;
   - table headers;
   - badges, pills, and buttons;
   - captions and footers;
   - chart labels and legends;
   - text over screenshots or images;
   - small text inside embedded prototype screenshots.
4. When contrast is uncertain, sample or compute the foreground/background ratio with `scripts/contrast_ratio.py`.
5. Fix every readability failure, re-render, and inspect again.
6. In the final response, state that a page-by-page or screen-by-screen human reading pass was completed. If any renderer was unavailable, say exactly which visual check was skipped.

## Readability Standards

Use these as minimums:

- Normal body text: contrast ratio at least 4.5:1.
- Large text, headings, table headers, and UI labels: at least 3:1, preferably 4.5:1.
- Small text under 10 pt or dense table text: prefer 7:1.
- Text inside screenshots embedded in a PDF or slide must remain readable after embedding. If not, crop, enlarge, simplify, or replace with a redrawn view.
- White text on saturated color is acceptable only when the contrast ratio passes and anti-aliasing remains clear.
- Colored text on colored fills is high risk; compute contrast or switch to black/white.

## Human Checks

For each page or screen, answer:

- Can I read every important sentence without zooming beyond normal viewing?
- Are any letters disappearing into a similarly colored background?
- Are table headers readable against their fill?
- Are links, footers, notes, and captions readable enough for their purpose?
- Does any text sit over a busy image or screenshot without a solid backing?
- Are charts still understandable if printed or viewed on a mediocre display?
- Are prototype screenshots large enough to inspect, or are they just decorative?
- Does the visual hierarchy tell me where to read first, second, and third?

## Common Failures To Catch

- Dark navy table header with dark text due to paragraph styles overriding table text color.
- Blue or teal text on blue/teal fills.
- Gray footers or captions that become invisible after PDF compression.
- Screenshots embedded too small for dashboard numbers or labels to be legible.
- White text on light image regions.
- Text inside badges/pills clipped vertically.
- Body text placed over gradients or shaded cards with insufficient contrast.
- Contact sheet inspection passing while individual pages contain unreadable details.

## Fixing Rules

Prefer fixes in this order:

1. Change text color to black, near-black, white, or near-white.
2. Change the background fill.
3. Add a solid or translucent backing behind text on images.
4. Increase text size or crop/enlarge the embedded screenshot.
5. Simplify the table, chart, or prototype capture.
6. Rebuild the element if the exported artifact flattened styles incorrectly.

Never solve low contrast by merely saying it is “secondary text” unless the text is truly nonessential.

## Script

Use `scripts/contrast_ratio.py` for deterministic checks:

```bash
python scripts/contrast_ratio.py --fg "#102033" --bg "#0B2545"
python scripts/contrast_ratio.py --pairs "#102033,#0B2545" "#FFFFFF,#0B2545"
python scripts/contrast_ratio.py --sample page.png --fg-point 420,180 --bg-point 420,160
```

Treat the script as a helper, not a replacement for visual inspection.
