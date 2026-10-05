---
name: site-checklist
description: "Audit an existing website's launch readiness or verify it after deployment across technical SEO, UX, accessibility, mobile browsers, consent, legal facts and analytics. Use for Site Checklist, a cross-functional readiness review, or requested checklist fixes. Inspect the actual project, report evidence and implement fixes only when requested. A targeted SEO or IA acquisition request can use its specialist skill directly; a checklist audit does not authorize deployment, submissions or content production."
compatibility: "Works with static HTML/CSS/JS and common frontend frameworks. Use the repository's existing stack and available browser/build tools; do not introduce a framework just for this checklist."
---

# Site Checklist

Use this skill to turn a website launch checklist into an evidence-based audit and, when the user asks for changes, a verified implementation. The checklist is intentionally cross-functional: technical SEO, conversion, accessibility, responsive behavior, UX states, legal/compliance, analytics, trust, and performance.

## Operating rules

1. Inspect the project before changing anything. Identify the framework, routes/pages, shared layout or document shell, asset pipeline, forms, analytics, cookie mechanisms, legal content, and available scripts.
2. Preserve the existing stack, visual language, copy, and user changes. Prefer the smallest coherent change that solves the requirement across all pages.
3. Treat real business data as required input, not something to invent. Never fabricate a domain, contact address, company identity, analytics ID, legal entity, retention period, consent vendor, testimonials, or compliance claim. Use a clearly marked placeholder only when the user explicitly accepts placeholders, and list it as blocked before launch.
4. Separate implementation from legal validation. You may implement the mechanics of a cookie banner, consent state, privacy page, or terms page, but do not present generic text as legal advice or claim RGPD compliance without the necessary facts and a human/legal review.
5. Prefer accessible, progressive, and resilient behavior: semantic HTML, keyboard access, visible focus, sufficient contrast, reduced-motion support, no-JavaScript fallback where practical, and useful feedback for loading, errors, and success.
6. Verify both source and rendered behavior. A file existing in the repository is not proof that a browser receives it correctly.
7. Match the mandate: audit = read-only; requested fixes = relevant local implementation and verification. Deployment, DNS/WAF changes, search submissions, account creation, public form submissions, CMS writes, content campaigns and recurring monitoring require authorization covering those actions. Reuse valid authorization already given; the checklist and its companion skills do not expand it. Prefer local fixtures or an authorized test environment for form and analytics tests.

## Scope, phase and companion skills

Identify the requested phase: pre-launch, post-deploy verification, or both. Record the exact local/preview/production origin, expected canonical host, deployment/version, languages, priority routes, business type, conversion and available access. Reuse the project's decisions and existing SEO records. If the production origin is unknown, do the local audit and mark origin-dependent checks `BLOCKED`; do not invent a domain or make the preview indexable.

Before using a companion, read its actual available `SKILL.md` and relevant references. Pass the site, phase, findings, evidence, authorized actions and expected result. Select only the needed module and report whether it was consulted, executed or unavailable. Avoid circular calls: if Newsit SEO or another coordinator called this checklist, return findings to it instead of relaunching that coordinator.

| Companion | Use when | Boundary |
|---|---|---|
| `seo-post-deploy` | Production is published and discovery/indexation checks or authorized Google/Bing/IndexNow actions are needed | Pre-launch prepares prerequisites only. An audit can inspect public readiness and existing records; it does not submit, verify ownership or deploy. Receipt, sitemap processing, indexation and visibility are separate results. |
| `ai-seo` | IA search access, citations, recommendations or acquisition are part of the requested scope | Use a focused diagnosis; preserve training/privacy choices. No universal bot opening, WAF change, panel experiment or full channel strategy from a basic checklist. |
| `seo-content-engine` | The user requests an editorial backlog, content batches, CMS workflow or recurring SEO program | Checklist findings may become proposed briefs/tickets. No automatic generation, CMS draft, publication, backlink outreach or scheduled job; apply its real modes and access requirements for an authorized program. |
| `newsit-seo` | The user asks for construction, broad reprise or migration beyond checklist fixes | Reuse its type/architecture/SEO contract when it is the coordinator. Do not restart stack selection, impose personal preferences from another project, bootstrap another MASTER or rebuild a site from an audit. |

If a skill or connector is absent, finish the checks possible here and name the specific remaining responsibility. Reading a skill is not execution; an exposed connector is not proof of login, rights or ownership. Do not install dependencies or change the site's stack simply to activate these routes.

## Checklist to audit

Evaluate every item as `PASS`, `PARTIAL`, `FAIL`, `BLOCKED`, or `N/A`, with evidence.

### SEO and discoverability

- Custom 404 page: an intentional branded page, correct 404 status where the host supports it, useful recovery links, and no accidental indexing.
- Meta title on every indexable page: unique, descriptive, and appropriate to the page.
- Meta description on every indexable page: unique, useful, and aligned with the page content.
- `robots.txt`: present at the site root, syntactically valid, and pointing to the canonical sitemap when appropriate.
- Sitemap: present or generated in a format supported by the target engine (XML commonly, or another documented format), containing canonical public URLs only and using the real production origin. Validate indexes/children, access, size limits and accurate lastmod where used; exclude previews, private/noindex pages and obsolete redirects.
- Production prerequisites: authoritative DNS resolves the intended host, HTTPS certificate is valid for it, HTTP/alternate-host redirects lead to the intended final origin without loops, and representative routes return the intended status. Check the public version, not just build configuration. A tools/network failure is not proof of DNS or site failure.
- Indexability and canonical: inspect initial HTML and response headers as well as rendered output, meta robots, X-Robots-Tag, canonical and internal links on representative templates/languages. Preserve deliberate noindex and authentication. robots.txt controls crawl, not private access; blocking crawl can prevent a noindex from being read. Canonical targets should be coherent, reachable and eligible; intentional cross-domain cases require the project's decision, not automatic replacement.
- Search readiness: distinguish eligibility from submission, sitemap read/processing, URL indexation, impressions/clicks and IA citations. Use public evidence and authorized Search Console/Bing records where available. Without those records, do not assert indexation or ownership; a site: query is not an exhaustive index inventory.
- Open Graph image: configured with a real, accessible image and sensible `og:title`, `og:description`, `og:url`, and `og:type` values.
- Alt text on every meaningful image: descriptive alternatives, empty alt for decorative images, and no filename or placeholder text.

### Conversion and interaction

- CTA above the fold: the primary action is visible without scrolling on common desktop and mobile viewports and has a concrete label.
- Sticky mobile CTA: the primary action remains reachable on mobile without covering content, respecting safe areas and keyboard/focus behavior.
- Loading states: asynchronous forms, navigation, submissions, and dynamic content expose progress and prevent duplicate actions.
- Form error states: field-level and summary errors are clear, associated with inputs, announced accessibly, and preserve entered values.
- Thank-you page or success state: successful submission has a distinct, share-safe confirmation experience and a sensible next step.

### Responsive and media quality

- Mobile breakpoints: key pages are usable at narrow, medium, and wide widths; no overflow, clipped content, broken tap targets, or unreadable typography.
- Compressed images: images use an appropriate format and dimensions, avoid needless bytes, and use responsive/lazy loading when appropriate without harming above-the-fold content.

### Mobile browser verification gate

Verify Safari on iOS/iPhone and Chrome on Android separately when auditing mobile readiness. Cover representative pages and their actual interaction states: rendering, typography, touch targets, navigation, scrolling, Three.js scenes, video playback, choice-dependent CTAs, accordions, comparisons, verified bundles, forms and consent. Check portrait and landscape where relevant, including safe areas, browser chrome, keyboard behavior and horizontal overflow.

For each platform, record browser/OS/device or emulation details, routes, states checked, evidence and remaining failures. Distinguish real-device/browser testing, browser/device emulation and a simple viewport resize. A narrow Chromium viewport does not verify Safari/iOS or Chrome/Android compatibility. If the required browser/device tools are unavailable, report that platform as `BLOCKED` or explicitly not verified, give the remaining manual checks, and do not claim mobile compatibility or install additional tools without necessity. Mobile readiness requires these platform checks or an explicit unresolved limitation in the report.
### Legal, privacy, and trust

- Privacy policy page: reachable from the site, identifies the responsible entity and contact channel, and accurately describes collection, purposes, legal bases, recipients, retention, rights, transfers, and request handling for the actual site.
- Terms and conditions: present when relevant, linked from the site, and reviewed for the real business, offer, jurisdiction, and service terms.
- Cookie banner: shown before non-essential cookies or trackers run, offers a genuine reject path, supports granular choices where needed, records consent, and provides a way to change or withdraw consent.
- RGPD: check data minimisation, purpose limitation, lawful basis, transparency, rights requests, consent proof, processor/subprocessor disclosures, international transfers, retention, security, and privacy-by-design. Mark unknown facts as `BLOCKED`; do not infer them from boilerplate.
- Real contact address: the public address, email, and phone details are real, consistent, and usable; never ship fake placeholder contact details.

### Measurement and operations

- Analytics installed: the chosen analytics tool is configured correctly, respects consent requirements, excludes sensitive form data, and has a documented measurement owner and purpose. Non-essential analytics must not fire before valid consent when required.
- Measurement verified: distinguish configuration from actual event delivery; check consent/rejection/withdrawal and duplicate-event behavior in an authorized test context. A CTA click is not a successful form, order or revenue; record event definitions, tested states and reporting access. Missing reporting access is unknown, not zero activity. Avoid deploying a second tracker to compensate.

## Workflow

### 1. Build the inventory

Use fast repository search to locate routes, page shells, `<head>` or metadata configuration, images, forms, error handlers, robots/sitemap files, legal pages, cookie code, analytics IDs, and build/test commands. Record the relevant files and the pages covered. If a browser is available, inspect representative routes at desktop and mobile widths.

Create a page matrix with at least: route, page type, indexability, title, description, canonical, primary CTA, form/state requirements, social metadata, and legal/footer links.

Attach environment/version, coverage (all routes or sample), test date, source of facts and access limits to the matrix. Include a route for each relevant template/language and critical error/conversion state; declare exclusions rather than silently extending a sampled result to the whole site.

### 2. Audit before implementation

For each checklist item, record:

- status: `PASS`, `PARTIAL`, `FAIL`, `BLOCKED`, or `N/A`;
- evidence: exact route, file, selector, command, or observed behavior;
- impact: `High`, `Medium`, or `Low`;
- fix: the smallest actionable change;
- owner/input needed when blocked.

Use `PASS` only for the criterion actually verified in the stated environment; `PARTIAL` for incomplete or mixed coverage, `FAIL` for an observed defect, `BLOCKED` for missing access/data/tool, and `N/A` for an inapplicable criterion with a reason. Public HTTP checks may pass while authenticated indexation checks remain blocked. A lack of Search Console access need not prevent the rest of the audit.

Do not mark an item `PASS` merely because a similarly named file or component exists. Check scope, content, runtime behavior, and production configuration.

### 3. Implement safe fixes when asked

Prioritize in this order:

1. blockers to access or conversion: broken routes, 404 handling, forms, error/success states, mobile layout, and primary CTA;
2. indexation and sharing: page metadata, canonical URLs, robots, sitemap, and Open Graph;
3. privacy and legal mechanics: consent gating, cookie preferences, legal navigation, and data-handling disclosures;
4. accessibility and performance: alt text, focus/error announcements, image compression, loading behavior, and responsive polish;
5. analytics and verification: consent-aware events and a documented measurement setup.

Use shared metadata helpers/layouts for repeated page concerns. Keep titles and descriptions page-specific. Generate robots and sitemap from the real origin or leave an explicit production-origin blocker. Preserve existing supported sitemap generation. Use placeholders only with the user's approval.

For cookies and analytics, classify technologies as strictly necessary or non-essential before deciding when they may run. A banner that merely hides a visual prompt while trackers already load does not satisfy the requirement. Store only the consent data needed for the selected mechanism, expose a settings/revoke control, and avoid collecting form fields or sensitive personal data in analytics.

For forms, use native validation as a baseline and add accessible custom feedback only where needed. On submit, expose a busy state, prevent duplicate submissions, handle network/server failure, and show a success route or success state. Do not log or send unnecessary personal data.

### 4. Verify

Run the project's existing lint, typecheck, test, and build commands when available. Then verify:

- every public route has the expected title, description, canonical/social tags, and one clear H1 where applicable;
- the 404 route renders intentionally and recovery links work;
- robots and sitemap are reachable and use correct absolute URLs in production configuration;
- images have correct alt behavior and reasonable transfer sizes;
- the primary CTA is visible above the fold and sticky only where appropriate on mobile;
- loading, validation, server-error, and success states work with keyboard and screen-reader-friendly messaging;
- non-essential analytics and cookies are blocked before consent and stop or respect withdrawal where the mechanism supports it;
- privacy, terms, contact, and cookie settings links are reachable from the relevant pages;
- no placeholder domain, address, analytics ID, legal entity, or copied dummy content remains.

If automated browser checks are unavailable, state that limitation and provide a manual verification list instead of claiming runtime validation.

### 5. Verify after an authorized deployment

When the site is already public or a separately authorized deployment has completed, compare the served version with the reviewed change and repeat the affected public HTTP/metadata, robots/sitemap, conversion, consent and browser checks. A local fix remains local until this verification. Do not change DNS or redeploy as part of a read-only audit.

Read the existing per-domain discovery record if relevant. For operational submissions within an authorized mandate, use `seo-post-deploy` and keep its evidence/statuses alongside the checklist rather than translating every receipt into `PASS` for indexation. If a write has an unknown result, reconcile its actual state before a repeat; unavailable state remains unresolved. Indexation awaiting a search engine is follow-up, not necessarily a technical launch blocker. Propose useful follow-up checks; schedule nothing without a request.

For changes to this skill, use the [decision scenarios](references/scenarios.md) to check scope and routing. Their manual walkthrough is not independent behavioral testing or a site's browser validation.

## Required output

Use this report structure unless the user requests another format:

# Site checklist report

## Summary

State the phase/environment and overall readiness, the number of `PASS`, `PARTIAL`, `FAIL`, `BLOCKED`, and `N/A` items, and the top launch blockers. Separate locally ready, publicly verified, and discovery/measurement pending; counts describe assessed items, not a compliance score.

## Page matrix

Provide the inspected routes and their metadata/CTA/form coverage.

## Findings

For every checklist item, provide status, evidence, impact, and recommended fix. Group findings under SEO, Conversion, Responsive/Media, Legal/RGPD, and Measurement/Trust.

## Changes made

List files changed and summarize behavior added. If no implementation was requested, say that the audit was read-only.

## Verification

List commands and browser/manual checks run, their environment/version and coverage, including any checks that could not be performed. Give separate Safari iOS and Chrome Android outcomes. Name companions consulted/executed and the work they actually supplied; do not count a cited skill as a passed check.

## Before launch

List only the remaining blockers and the exact owner input or review needed. Call out real-domain, real-address, analytics credentials, cookie inventory, retention periods, transfer locations, and legal review explicitly when unknown.

For a published site, replace this section with remaining production blockers and follow-up: distinguish local fixes, deployment verification, access prerequisites, submission receipts, indexation pending and measurement limitations.

## Completion rule

The site is ready only when there are no unresolved High-impact `FAIL` or `BLOCKED` items, all required legal/business facts are verified, and the rendered site passes the relevant responsive, accessibility, consent, form, and metadata checks. Preserve the separate Safari iOS and Chrome Android gate: an unavailable platform remains explicitly unverified and prevents an unqualified mobile-ready claim. State the environment of readiness; source/build success is not public deployment verification, legal mechanics are not legal approval, and launch readiness does not guarantee future indexation or IA visibility. If the user asks for an audit only, do not modify code; if they ask to fix or implement the checklist, make the changes and verify them within the authorized scope.
