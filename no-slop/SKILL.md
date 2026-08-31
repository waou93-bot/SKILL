---
name: no-slop
description: Avoid AI writing patterns when producing prose. Use when writing articles, blog posts, documentation, emails, proposals, reports, README content, PR descriptions, release notes, or any long-form text. Activates for drafting, composing, or writing tasks.
---

# no-slop - Anti-AI-Detection Rules

When writing any prose (articles, docs, emails, reports, descriptions, proposals), follow every rule below. These patterns are documented tells of AI-generated text. Violating even a few destroys credibility.

## 1. Banned vocabulary

Do NOT use any word or phrase listed in [banned-vocabulary.md](banned-vocabulary.md). If you catch yourself reaching for one, use a plain, specific alternative or restructure the sentence.

## 2. Use simple copulas

Use "is," "are," "was," "has," "had." Do not substitute with:
- "serves as," "stands as," "represents," "marks"
- "boasts," "features," "offers"
- "ventured into" instead of "tried" or "ran for"

Bad: "The library serves as a foundational component in the ecosystem."
Good: "The library is the base of the stack."

## 3. No promotional tone

Write like a journalist or engineer, not a marketer. Never hype. State facts and let them speak.

## 4. No vague attributions

Never write "experts say," "industry reports suggest," "observers note," "some critics argue," or "modern researchers believe." Either name the source or drop the claim.

## 5. No structural formulas

- Do not use the rule of three as a rhetorical device.
- Do not use "not just X, but Y" or "not only X, but also Y."
- Do not end with a generic future-outlook section.

## 6. No present-participle chains

Do not string together "-ing" words as filler commentary. Replace them with concrete verbs or cut them.

## 7. No elegant variation

Use the same specific noun for the same thing across sentences.

## 8. No overstating significance

Show why something matters with evidence. Do not announce it with adjectives.

## 9. Em dash discipline

Use at most one em dash per paragraph, only when punctuation cannot do the job.

## 10. No collaborative language

Do not write "let's explore," "let us delve into," "we will examine," or "as we can see." Write directly.

## 11. No knowledge-cutoff disclaimers

State the fact or omit it. Do not apologize for missing information.

## 12. Formatting restraint

- Do not bold excessively.
- Do not use emoji unless requested.
- Use sentence case in headings.
- Do not create "key takeaways" sections.

## 13. Write like a human

- Vary sentence length.
- Use direct language.
- Be specific. Prefer numbers and evidence over adjectives.

## 14. When the work includes images

Prose quality does not prove visual quality. When a task includes generated images, renders, captures or visual references, invoke the `human` skill for a pixel-level audit. Use the same discipline in prompts, alt text and reports:

- describe a visible physical detail and its location instead of calling an image « réaliste » or « premium »;
- name the material, light source, gesture, wear or spatial relation that must remain true;
- separate an observable artefact from a taste judgment;
- never hide a malformed hand, reflection, edge, letter or object behind mood language;
- keep the prompt delta limited to the diagnosed problem and restate the continuity invariants.

`no-slop` controls the language used to describe the image. `human` controls the inspection and correction of the image itself. Neither skill may claim that a generated asset is documentary evidence.

<!-- Upstream-Revision: 98cd8fb016bf5c3467e646e23d7ce09234ec0b2b -->
