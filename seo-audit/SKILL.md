---
name: seo-audit
description: When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO health check," "my traffic dropped," "lost rankings," "not showing up in Google," "site isn't ranking," "Google update hit me," "page speed," "core web vitals," "crawl errors," or "indexing issues." Use this even if the user just says something vague like "my SEO is bad" or "help with SEO" — start with an audit. For building pages at scale to target keywords, see programmatic-seo. For adding structured data, see schema. For AI search optimization, see ai-seo.
metadata:
  version: 2.2.0
  reviewed_at: "2026-10-13"
---

# SEO Audit

<!-- GOOGLE_STARTER_GUIDE:BEGIN -->
## Socle Google Search Central

Lire et appliquer [les bonnes pratiques du guide SEO Google](../seo/references/google-starter-guide.md) avant les étapes concernées, dans un périmètre proportionné. Use this baseline in every applicable audit check. Treat character ranges, keyword placement and heading counts as editorial heuristics, never Google ranking requirements. Separate demonstrated defects, accessibility issues and optional improvements.

Source consultée le 8 octobre 2026. Le socle prime sur les recettes rigides contradictoires ; il nʼétend aucune autorisation.


Pour les controles specialises (rendu, sitemap, liens, medias, international, recherche generative et mesure), lire uniquement les sections pertinentes des [controles avances Google](../seo/references/google-advanced-practices.md). Verifier les sources actuelles avant application et distinguer exigences, recommandations et options.
<!-- GOOGLE_STARTER_GUIDE:END -->

<!-- AFFILIATE_AUDIT:BEGIN -->
## Sites affiliés et audits contradictoires

Pour un site de guides d’achat ou une relecture d’audit externe, lire les [contrôles affiliation, preuves produit et comparaison d’audits](../seo/references/affiliate-audit.md). Vérifier chaque remarque sur les gabarits réels, distinguer défaut Google, partage social et recommandation éditoriale, rechercher les pages existantes avant de proposer des créations. Ne pas déduire une pénalité de l’absence d’essai, d’une animation, d’images générées ou d’un éditeur commun. Les corrections conservent les URL, données, parcours et consentements ; comparer sources et production avant livraison.
<!-- AFFILIATE_AUDIT:END -->


You are an expert in search engine optimization. Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before auditing, understand:

1. **Site Context**
   - What type of site? (SaaS, e-commerce, blog, etc.)
   - What's the primary business goal for SEO?
   - What keywords/topics are priorities?

2. **Current State**
   - Any known issues or concerns?
   - Current organic traffic level?
   - Recent changes or migrations?

3. **Scope**
   - Full site audit or specific pages?
   - Technical + on-page, or one focus area?
   - Access to Search Console / analytics?

---

## Mandatory Page-Level SEO Checks

For a complete editorial audit, combined SEO/AI audit, fan-out review, or republication
check, read [coverage, journeys and release evidence](references/fanout-and-release-evidence.md).
Audit the decision behind each page and its useful subquestions: observed need or
editorial hypothesis → existing owner URL/section → actual answer and proof → next action.
Reuse or enrich existing answers before proposing a distinct page. Do not treat a
topic map as observed internal AI queries or a count of keywords as useful coverage.
Use [the page audit worksheet](assets/page-audit.md) or equivalent fields in the
existing report; a targeted audit does not require a new document hierarchy.

Apply this checklist to each in-scope URL or representative template. State whether coverage is exhaustive or sampled, list the URLs and templates inspected, and separate the public response from repository/build output. Keep the audit read-only unless the user explicitly asks for corrections.

### Internal linking and discoverability

- Build a source-to-destination inventory from crawlable HTML links. Separate contextual links in the main content from global navigation, footer, product widgets, and links that appear only after interaction.
- For priority URLs, record incoming links, outgoing links, useful anchor text, destination status/final URL, and depth from a declared entry point. Flag an orphan only when the declared crawl has exhausted its reachable graph and the URL is in the expected page population.
- Check that the anchor describes the destination and makes sense in its sentence; identify generic, ambiguous, misleading, repeated, or over-optimized anchors. Do not enforce a link-count or click-depth quota.
- Verify important journeys and content relationships (for example: hub → guide/article → relevant product list). Inspect fragments, pagination, filters, accordions, and other interactive destinations in the rendered page when initial HTML cannot establish that they work. A fragment absent from initial HTML is a review item, not automatically a broken link.
- Report broken links, redirects, orphan findings, and missing contextual links with source URL, destination URL, response evidence, and the relevant interaction state. Do not infer ranking penalties from graph shape alone.

### Title and heading relevance

For every in-scope page, compare the HTML title, visible H1, section headings, URL, main content, and the page's stated role. Record the actual text and assess:

- whether the topic and intended decision are explicit, precise, natural, and understandable without guessing;
- whether the title and H1 accurately describe the content that follows and distinguish this page from related guides, articles, categories, and product lists;
- whether near-duplicates, vague labels, mismatches, keyword stuffing, or competing page intents are demonstrated;
- whether the title, H1, and page content agree. Check the relevant query/search intent only when reliable query or SERP evidence is available.

Give a page-specific proposed title or heading only when the evidence supports a useful change. Character counts and display-width estimates are editorial clues, not pass/fail requirements or ranking rules. Do not assert traffic gain, cannibalization, or ranking loss without supporting evidence.

### HTML tags, structured data, and accessibility

Inspect the delivered HTML head and body, not only source files. For each URL/template, record:

- title, canonical, meta robots and X-Robots-Tag, html lang, applicable hreflang, and viewport;
- Open Graph (og:title, og:description, og:url, og:image) and Twitter card tags when social previews are in scope; verify that image URLs resolve and represent the page;
- semantic heading levels, useful image alt text (including intentional empty alt for decoration), and crawlable anchor links;
- every JSON-LD block: parse validity, type and property requirements for the relevant supported search feature, consistency with visible page content, canonical URL, language, and dates.

Compare initial HTML with rendered DOM when scripts or interactions may add, remove, or alter content or markup. Use the current official rich-results validator for applicable structured data. Report syntax validity separately from required-property errors, optional warnings, policy/content mismatch, eligibility, and actual search appearance. A parser that cannot see a script or an initial-HTML-only check does not prove that markup is absent.

### Metadata and page-level evidence

Check title and description presence, useful uniqueness, accuracy, and consistency with the actual page; verify canonical and robots directives against the intended indexability and sitemap; and confirm social metadata agrees with the page. Do not treat a missing canonical by itself, description length, or deprecated meta keywords as a demonstrated Google ranking defect. A canonical tag and a sitemap are signals, not proof of the URL Google selected or indexed it.

For each finding, include the exact URL/template, observed value or source/destination, dated evidence and method, status (VERIFIED, NEEDS_CORRECTION, NOT_VERIFIED, or NOT_APPLICABLE), reader/search consequence, a scoped recommendation, and a recheck criterion. Separate proven defects, accessibility/comprehension concerns, editorial opportunities, and unverified hypotheses. Do not silently edit or publish during an audit.

Also identify the inspected environment/version and the state of each change:
proposed, local, pushed, published or measured. For editorial proposals, keep title,
H1 and description before/after with the reason and actual body coverage. Metadata
must not promise a fan-out answer absent from the page. Inspect decorative versus
informative media and interactive fragments in the rendered page before flagging them.

---
## Audit Framework

For indexing issues or republication, apply the [repository, production and indexation checks](../seo/references/production-indexation.md). Compare the main branch, open PRs and actual deployment; preserve newer public routes and interactions. Check absolute canonical, og:url, JSON-LD and sitemap origins in the build and on the final domain. Keep intentional noindex exclusions. Date global Search Console reports and individual inspections separately; an older excluded URL may now be indexed. A live test proves present eligibility, not index membership. Audit permission alone does not authorize deployment; an explicit request to correct and publish does within its stated scope.

Identify the authoritative source/commit or artifact and public version before
republication. Preserve useful public routes missing from an older snapshot. Trace
lastmod/dateModified to a significant change in the published content: review the
Git diff or editorial record; a build, clone, restore or sitemap date alone is not
evidence of editorial freshness. Omit optional unknown dates rather than inventing them.

### Schema Markup Detection

Raw HTML can reveal server-rendered JSON-LD. Text conversions may remove script elements, and raw HTML cannot reveal markup injected only by JavaScript. Check both initial HTML and rendered DOM where relevant, then the Google Rich Results Test. Record unobserved markup as unknown rather than absent. Separate syntax, required properties, optional warnings and qualitative eligibility; automated validation does not guarantee an enhanced search result.

### Priority Order
1. **Crawlability & Indexation** (can Google find and index it?)
2. **Technical Foundations** (is the site fast and functional?)
3. **On-Page Optimization** (is content optimized?)
4. **Content Quality** (does it deserve to rank?)
5. **Authority & Links** (does it have credibility?)

---

## Technical SEO Audit

### Crawlability

**Robots.txt**
- Check for unintentional blocks
- Verify important pages allowed
- Check sitemap reference

**XML Sitemap**
- If present, accessible and valid; a sitemap is useful but not universally required
- Submitted to Search Console
- Contains only canonical, indexable URLs
- Reflects significant changes; accurate lastmod, not routine date refreshes
- Proper formatting

**Site Architecture**
- Important pages easy to discover through useful internal links; no universal three-click ranking requirement
- Logical hierarchy
- Internal linking structure
- No orphan pages

**Crawl Budget Issues** (for large sites)
- Parameterized URLs under control
- Faceted navigation handled properly
- Infinite scroll with pagination fallback
- Session IDs not in URLs

### Indexation

**Index Status**
- site:domain.com as a partial visibility clue, not an exhaustive index inventory
- Search Console coverage report
- Compare indexed vs. expected

**Indexation Issues**
- Noindex tags on important pages
- Canonicals pointing wrong direction
- Redirect chains/loops
- Soft 404s
- Duplicate content without canonicals

**Canonicalization**
- Canonical signals consistent where needed; missing a tag alone is not a universal defect
- Self-referencing canonicals on unique pages
- HTTP → HTTPS canonicals
- www vs. non-www consistency
- Trailing slash consistency

### Site Speed & Core Web Vitals

**Core Web Vitals**
- LCP (Largest Contentful Paint): <= 2.5s at the 75th percentile of field data
- INP (Interaction to Next Paint): <= 200ms at the 75th percentile of field data
- CLS (Cumulative Layout Shift): <= 0.1 at the 75th percentile of field data

**Speed Factors**
- Server response time (TTFB)
- Image optimization
- JavaScript execution
- CSS delivery
- Caching headers
- CDN usage
- Font loading

**Tools**
- PageSpeed Insights
- WebPageTest
- Chrome DevTools
- Search Console Core Web Vitals report

### Mobile-Friendliness

- Responsive design (not separate m. site)
- Tap target sizes
- Viewport configured
- No horizontal scroll
- Same content as desktop
- Mobile-first indexing readiness

### Security & HTTPS

- HTTPS across entire site
- Valid SSL certificate
- No mixed content
- HTTP → HTTPS redirects
- HSTS header (bonus)

### URL Structure

- Readable, descriptive URLs
- Keywords in URLs where natural
- Consistent structure
- No unnecessary parameters
- Lowercase and hyphen-separated

---

## International SEO & Localization

When multiple languages or regions are in scope, read the [International SEO reference](references/international-seo.md). Audit actual rendered annotations, access and indexed canonical choices.

- Separate language URLs; no mandatory prefix on the default language. Avoid forced location/language redirects that hide alternatives.
- HTML, HTTP and sitemap hreflang are equivalent. Check self-reference, return links, valid codes and absolute destinations. `x-default` is optional. Do not infer that one broken relationship invalidates every variant.
- Distinguish different-language translations from same-language regional duplicates before recommending canonicals. Preserve intentional exclusions.
- Validate sitemap namespaces, alternates and real size; no arbitrary 2K-5K URL cap or mandatory split strategy.
- Review the usefulness and accuracy of localized main content. Do not infer a site-wide penalty from thin locale pages alone.
- Report URL-level evidence, affected relationships and measured language/country visibility; verify framework output rather than assuming version-specific behavior.

---

## On-Page SEO Audit

### Title Tags

**Check for:**
- Page-specific titles where useful; shared titles may be valid within paginated series
- Clear, accurate topic in natural language; no mandatory keyword position
- Clear and concise; character ranges are editorial guides, not fixed display or ranking limits
- Compelling and click-worthy
- Brand name placement (end, usually)

**Common issues:**
- Duplicate titles
- Too long (truncated)
- Too vague to communicate the page purpose (length alone is not a defect)
- Keyword stuffing
- Missing entirely

### Meta Descriptions

**Check for:**
- Page-specific descriptions where useful; pagination can share descriptions
- Short, page-specific summary; no fixed Google character requirement
- Describes the relevant page content naturally, without keyword stuffing
- Clear value proposition
- Call to action

**Common issues:**
- Duplicate descriptions
- Auto-generated garbage
- Unhelpful or inaccurate summary; length alone is not a demonstrated SEO issue
- No compelling reason to click

### Heading Structure

**Check for:**
- Useful page heading and accessible semantic structure; no universal single-H1 ranking rule
- Page heading clearly describes the subject in natural language
- Logical hierarchy (H1 → H2 → H3)
- Headings describe content
- Not just for styling

**Common issues:**
- Confusing heading structure; multiple H1s alone are not proof of a Google ranking defect
- Skipped levels that impair accessibility or comprehension; distinguish from ranking claims
- Headings used for styling only
- No H1 on page

### Content Optimization

**Primary Page Content**
- Explain the topic promptly when useful; no keyword placement quota
- Related keywords naturally used
- Sufficient useful detail for the intent; no magical minimum word count
- Answers search intent
- Better than competitors

**Thin Content Issues**
- Pages with little unique content
- Tag/category pages with no value
- Doorway pages
- Duplicate or near-duplicate content

### Image Optimization

**Check for:**
- Descriptive file names
- Useful alt text for informative images; empty alt for decorative images
- Alt text describes image
- Compressed file sizes
- Modern formats (WebP)
- Lazy loading implemented
- Responsive images

### Internal Linking

**Check for:**
- Important pages well-linked
- Descriptive anchor text
- Logical link relationships
- No broken internal links
- Reasonable link count per page

**Common issues:**
- Orphan pages (no internal links)
- Over-optimized anchor text
- Important pages buried
- Excessive footer/sidebar links

### Keyword Targeting

**Per Page**
- Clear primary keyword target
- Title, H1, URL aligned
- Content satisfies search intent
- Not competing with other pages (cannibalization)

**Site-Wide**
- Keyword mapping document
- No major gaps in coverage
- No keyword cannibalization
- Logical topical clusters

---

## Content Quality Assessment

### E-E-A-T Quality Considerations

E-E-A-T is not a single Google ranking factor or measurable Google score. Evaluate evidence and trust for the reader.

**Experience**
- First-hand experience demonstrated
- Original insights/data
- Real examples and case studies

**Expertise**
- Author credentials visible
- Accurate, detailed information
- Properly sourced claims

**Authoritativeness**
- Recognized in the space
- Cited by others
- Industry credentials

**Trustworthiness**
- Accurate information
- Transparent about business
- Contact information available
- Privacy policy, terms
- Secure site (HTTPS)

### Content Depth

- Comprehensive coverage of topic
- Answers follow-up questions
- Better than top-ranking competitors
- Updated and current

### User Engagement Signals

- Time on page
- Bounce rate in context
- Pages per session
- Return visits

---

## Common Issues by Site Type

### SaaS/Product Sites
- Product pages lack content depth
- Blog not integrated with product pages
- Missing comparison/alternative pages
- Feature pages thin on content
- No glossary/educational content

### E-commerce
- Thin category pages
- Duplicate product descriptions
- Missing product schema
- Faceted navigation creating duplicates
- Out-of-stock pages mishandled

### Content/Blog Sites
- Outdated content not refreshed
- Keyword cannibalization
- No topical clustering
- Poor internal linking
- Missing author pages

### Multilingual / Multi-Regional Sites
- Broken reciprocal language annotations or wrong destinations
- Canonical choices inconsistent with the intended language/regional content
- Main content insufficiently localized or inaccurate
- Forced redirects hiding alternate language URLs
- Unsupported claims of cluster rejection or site-wide penalties; require evidence

### Local Business
- Inconsistent NAP
- Missing local schema
- No Google Business Profile optimization
- Missing location pages
- No local content

---

## Output Format

### Audit Report Structure

**Executive Summary**
- Overall health assessment
- Top 3-5 priority issues
- Quick wins identified

**Technical SEO Findings**
For each issue:
- **Issue**: What's wrong
- **Impact**: SEO impact (High/Medium/Low)
- **Evidence**: How you found it
- **Fix**: Specific recommendation
- **Priority**: 1-5 or High/Medium/Low

**On-Page SEO Findings**
Same format as above

**Content Findings**
Same format as above

**Prioritized Action Plan**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins (easy, immediate benefit)
4. Long-term recommendations

---

## References

- [AI Writing Detection](references/ai-writing-detection.md): Common AI writing patterns to avoid (em dashes, overused phrases, filler words)
- [International SEO](references/international-seo.md): Evidence and sources for hreflang, canonical + i18n, sitemaps, URL structure, and content quality across locales
- For AI search optimization (AEO, GEO, LLMO, AI Overviews), see the **ai-seo** skill

---

## Tools Referenced

**Free Tools**
- Google Search Console (essential)
- Google PageSpeed Insights
- Bing Webmaster Tools
- Rich Results Test (**use this for schema validation — it renders JavaScript**)
- Chrome DevTools responsive checks and PageSpeed Insights (Mobile-Friendly Test retired in December 2023)
- Schema Validator

> **Schema:** inspect raw HTML and rendered markup as needed; validation cannot establish all quality-policy requirements.

**Paid Tools** (if available)
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- ContentKing

---

## Task-Specific Questions

1. What pages/keywords matter most?
2. Do you have Search Console access?
3. Any recent changes or migrations?
4. Who are your top organic competitors?
5. What's your current organic traffic baseline?

---

## Related Skills

- **ai-seo**: For optimizing content for AI search engines (AEO, GEO, LLMO)
- **programmatic-seo**: For building SEO pages at scale
- **site-architecture**: For page hierarchy, navigation design, and URL structure
- **schema**: For implementing structured data
- **cro**: For optimizing pages for conversion (not just ranking)
- **analytics**: For measuring SEO performance
