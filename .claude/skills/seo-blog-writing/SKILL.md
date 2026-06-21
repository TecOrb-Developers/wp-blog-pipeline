---
name: seo-blog-writing
description: Authoritative reference for writing SEO-optimized long-form blog posts that rank in Google and surface in AI Overviews, ChatGPT Search, and Perplexity. Use this skill whenever the task involves drafting, outlining, editing, or critiquing a blog post intended for organic search traffic — including topic research, keyword strategy, search-intent matching, headline writing, meta descriptions, schema markup, internal linking, featured-snippet optimization, E-E-A-T signals, content depth calibration, and generative engine optimization (GEO). Trigger this skill even when the user only says "write a blog," "create an article," "SEO post," or hands over a title + brief expecting expansion. Do not write blog content without consulting this skill — the rules here are non-negotiable for Tecorb's content quality bar.
---

# SEO Blog Writing — Tecorb Technologies

This skill governs how every blog post is researched, structured, and written for the Tecorb website. Apply it in this order: **intent first, structure second, prose third, optimization fourth.** Writers who optimize before they've nailed intent produce content that ranks for nothing.

## When this skill applies

- Any new blog post draft from a title + brief
- Rewriting or refreshing an existing blog
- Outlining a content cluster or pillar page
- Auditing a published blog for ranking issues
- Generating meta titles, descriptions, slugs, or schema for any web content

## The non-negotiables

1. **Match search intent before anything else.** Wrong intent = zero rankings regardless of word count.
2. **Write for the reader, optimize for the engine.** In that order, every time.
3. **Earn the position, don't pad to it.** A 1,200-word post that answers the query beats a 3,000-word post that buries it.
4. **Demonstrate experience.** Tecorb's edge is 135+ engineers shipping real products — show that in examples, not adjectives.
5. **Every claim cites a source or names a project.** "Studies show" without a link is content debt.

---

## 1. Search intent — the foundation

Before writing a single sentence, classify the target query into one of four intents. The structure, depth, and CTAs differ for each.

| Intent | Query pattern | Reader wants | Format match |
|---|---|---|---|
| **Informational** | "what is", "how does", "guide to" | Definition, explanation, mental model | Long-form guide, definitions, diagrams |
| **Commercial investigation** | "best X", "X vs Y", "top X for Y" | Comparison, trade-offs, recommendations | Comparison post, ranked list with criteria |
| **Transactional** | "hire", "cost of", "X development services" | Vendor, price, contact | Service-page style with proof + CTA |
| **Navigational** | Brand or product name | Specific destination | Don't write blogs for these |

**How to verify intent:** Run the target query in Google. Look at the top 5 results. If they're all listicles, your post is a listicle. If they're all tutorials, yours is a tutorial. If they're all comparison posts, don't write a "what is" guide and expect to rank. The SERP tells you what Google has decided readers want — argue with it at your own cost.

**Tecorb-specific intent layer:** Most Tecorb readers ultimately have **commercial intent even when their query looks informational**. A search for "how does LLM fine-tuning work" from a startup CTO is two clicks away from "who can fine-tune an LLM for us." Structure informational posts so they end on a competence demonstration → soft CTA, not a hard sell.

---

## 2. Keyword strategy

### Primary keyword
One focus keyword per post. Place in:
- URL slug (kebab-case, ≤60 chars)
- H1 / title tag (front-load it, ideally in first 3 words)
- First 100 words of body
- At least one H2
- Meta description
- Image alt text on featured image
- Slug of one internal anchor pointing to this post

### Secondary keywords (LSI / semantic)
2–5 related terms that share the topic's entity graph. Find them in:
- "People Also Ask" section of the SERP
- "Related searches" at bottom of SERP
- Auto-complete suggestions
- Competitor H2s in the top 5 results

Sprinkle naturally across H2s and body. **Do not force keyword density** — modern search uses neural matching; topical coverage matters more than repetition. Aim for 0.5–1.5% density on primary; ignore density entirely for secondary.

### Entity coverage
Google's Knowledge Graph operates on entities (concepts, products, people, places). A blog about "React Native" should also mention: Meta, JavaScript, mobile framework, cross-platform, iOS, Android, JSX, hot reload, Expo, Hermes engine. Listing related entities tells the algorithm you know the topic deeply. Pull entity lists from Wikipedia's first two paragraphs on the topic plus the right-rail Knowledge Panel.

### Long-tail capture
For every post, list 5–10 specific long-tail queries the post should also rank for. Address each as an H3 or a paragraph with a clear question-style heading. Example for a flutter widgets post:
- "what are the most used flutter widgets"
- "stateful vs stateless widget"
- "how to create a custom flutter widget"

---

## 3. Title tag and H1

**Title tag (≤60 characters, ideally 50–58):** Appears in SERP, browser tab, social cards.
- Front-load the primary keyword
- Include a power modifier: number, year, "Complete Guide," "(2026)", "Step-by-Step"
- Add brand suffix sparingly: `| Tecorb` — only when title is short
- One emotional or curiosity hook per title — don't overdo it

**H1 (on-page title):** May be longer than the title tag. Can be more conversational.

### Title formulas that work for Tecorb's topics

| Formula | Example |
|---|---|
| `[Number] [Things] for [Outcome] in [Year]` | "10 AI Agent Frameworks Powering Production Apps in 2026" |
| `[Subject]: A Complete Guide for [Audience]` | "LLM Fine-Tuning: A Complete Guide for Engineering Teams" |
| `How to [Outcome] with [Method]` | "How to Build a Voice AI Agent with LiveKit and Vapi" |
| `[X] vs [Y]: Which to Choose in [Year]` | "React Native vs Flutter: Which to Choose in 2026" |
| `The Real Cost of [Thing] in [Year]` | "The Real Cost of On-Demand App Development in 2026" |
| `Why [Subject] [Verb] — and What to Do About It` | "Why Most LLM Pilots Fail — and What to Do About It" |

Avoid: clickbait without payoff, all-caps, excessive punctuation (!!!), brackets stuffed with secondary keywords.

---

## 4. Meta description

**130–155 characters.** Not a direct ranking factor but drives CTR, which is.

Structure:
1. Hook the searcher's pain or question (≤8 words)
2. Promise what they'll learn or get (≤12 words)
3. Soft action verb ("Learn", "See", "Explore") — never "Read this article"

Include the primary keyword once, naturally.

**Good:** *"Confused between React Native and Flutter? Compare performance, ecosystem, hiring cost, and use cases to pick the right stack for 2026."*

**Bad:** *"In this article we will discuss React Native vs Flutter and learn about which one is better for mobile app development in 2026."*

---

## 5. URL slug

- Kebab-case, all lowercase
- Primary keyword + 1–2 modifiers, max 5–7 words total
- Remove stop words (a, the, to, of, for, and, in) when possible
- No dates unless the post is year-specific evergreen
- No category prefix (`/blog/` is enough)

**Good:** `react-native-vs-flutter-2026`
**Bad:** `the-comprehensive-guide-to-react-native-vs-flutter-in-the-year-2026-by-tecorb`

---

## 6. Article structure

### Above the fold (first 200 words)
This decides bounce rate. Within the first scroll, the reader must know:
1. They're in the right place (problem stated in their words)
2. The post is credible (data point, stat, named project, or contrarian claim)
3. What they'll get if they keep reading (preview the value)

**The TL;DR block** sits between H1 and the first H2. 3–5 bullets summarizing the post. This serves three purposes: rewards skimmers, gets pulled into AI Overviews, and feeds featured snippets.

### Body structure by intent

**Informational (1,500–2,500 words):**
- Hook → TL;DR → What is X (definition, ~150 words)
- Why X matters (1–2 H2s)
- How X works (mechanics, with diagram)
- When to use X / when not to (criteria table)
- Common pitfalls (3–5, named)
- Tools/frameworks (named, linked)
- Real example (one Tecorb project anonymized if needed)
- FAQ (5–8 questions from PAA)
- Conclusion with single clear CTA

**Comparison (1,800–2,800 words):**
- Hook → TL;DR with verdict ("Pick X if Y; pick Z if W")
- Quick-glance comparison table (above the fold)
- Criteria framework (5–7 dimensions)
- Each option scored against criteria
- Use-case recommendations (3–4 scenarios)
- Cost & hiring reality
- Verdict restated
- FAQ

**How-to / tutorial (1,200–2,500 words):**
- Hook → What you'll build → Prerequisites
- Numbered steps (each as H2 or H3)
- Code blocks with comments
- Screenshots / diagrams at decision points
- "Common errors" section
- Next steps + repo link

**Listicle / ranked list (1,500–2,500 words):**
- Hook → How we ranked them (transparency = trust)
- N items, each ~200 words with: what it does, best for, limitations, screenshot/example
- Comparison table at end
- Honorable mentions
- Pick guide ("Choose X if...")

### Heading hierarchy
- One H1 per page (the title)
- H2 for major sections (5–9 per post)
- H3 for sub-points under an H2
- Avoid H4+ unless it's a tutorial with deep nesting
- Headings should read like a table of contents — a skimmer should grasp the whole argument from H2s alone

### Paragraph rhythm
- 1–4 sentences per paragraph
- Vary sentence length (short, then medium, then long) — this is how readable prose breathes
- No "wall of text" sections; break up long explanations with lists, callouts, diagrams
- One idea per paragraph

---

## 7. Featured snippet optimization

Featured snippets sit above position 1. Four formats:

| Format | How to win it |
|---|---|
| **Paragraph** (~40–60 words) | Answer the question in the H2/H3, then give a clean 40–60 word paragraph immediately after, no fluff |
| **List** | Use H3s or numbered/bulleted list directly under a "How to..." or "Steps to..." H2 |
| **Table** | Comparison or attribute data in clean `<table>` markup |
| **Video** | Out of scope for blog posts |

**Pattern that works:** Phrase the H2 as the exact question, then in the first sentence after the H2 give a definitional answer in 1–2 sentences. Then elaborate.

Example:
> ## What is LLM fine-tuning?
> **LLM fine-tuning is the process of further training a pre-trained large language model on a smaller, task-specific dataset to specialize its behavior for a particular domain or use case.** Unlike training from scratch, fine-tuning starts from existing weights and adjusts them with techniques like LoRA, full fine-tuning, or DPO...

The bolded sentence is what Google lifts into the snippet.

---

## 8. People Also Ask (PAA)

PAA boxes appear in 60%+ of SERPs. Each PAA expansion is a ranking opportunity.

**Workflow:**
1. Search your target query
2. Screenshot or note the PAA questions
3. Add each as an H3 inside a "FAQ" H2 near the bottom
4. Answer in 40–80 words (snippet length)
5. Mark up with FAQPage schema (see Schema section)

Include 5–8 FAQ items per post. Pull questions from PAA, Reddit, Quora, and Tecorb's actual sales call objections.

---

## 9. E-E-A-T signals

**Experience, Expertise, Authoritativeness, Trustworthiness.** Google's helpful-content systems weight these heavily.

### How Tecorb posts demonstrate E-E-A-T

| Signal | How to show it |
|---|---|
| **Experience** | First-person plural where appropriate: "When we built X for client Y, we found..." Concrete numbers from real projects. Named tools the team actually uses. |
| **Expertise** | Technical specificity. Don't say "AI helps with personalization" — say "we used a two-tower neural ranker trained on 6 months of session data, achieving NDCG@10 of 0.74." |
| **Authoritativeness** | Author bio links to LinkedIn, lists credentials. Cite primary sources (Google docs, framework GitHub READMEs, research papers) over secondary blogs. |
| **Trustworthiness** | Last-updated date visible. Author byline visible. Source links. No undisclosed affiliate links. Show the trade-offs, not just the wins. |

### Author byline
Every Tecorb blog has a named human author with a photo, role, and LinkedIn link. "Tecorb Team" is acceptable only for company-announcement posts, never for technical content.

### Citation rules
- Statistics: link to original source (not a roundup blog)
- Tool claims: link to official docs
- Code snippets: cite the framework version
- Industry data: prefer Gartner, Forrester, IDC, Statista, official government reports
- Never cite a competitor's blog as a primary source

---

## 10. Schema markup

Schema.org JSON-LD is non-negotiable. Every Tecorb blog ships with:

### `Article` schema (or `BlogPosting`)
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Article Title (≤110 chars for Google News)",
  "image": ["https://www.tecorb.com/.../featured.webp"],
  "datePublished": "2026-05-19T09:00:00+05:30",
  "dateModified": "2026-05-19T09:00:00+05:30",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://www.tecorb.com/author/slug/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Tecorb Technologies",
    "logo": { "@type": "ImageObject", "url": "https://www.tecorb.com/logo.png" }
  },
  "description": "Meta description text"
}
```

### `FAQPage` schema
For posts with an FAQ section (which is most):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question text?",
      "acceptedAnswer": { "@type": "Answer", "text": "Answer text." }
    }
  ]
}
```

### `HowTo` schema
For step-by-step tutorial posts only. **Do not use HowTo on non-tutorial content** — Google has cracked down on misuse.

### `BreadcrumbList` schema
For navigation hierarchy. Helpful for SERP appearance.

Validate every post with Google's Rich Results Test before publish.

---

## 11. Internal linking strategy

Internal links pass authority and help Google understand topical structure.

**Per-post requirements:**
- 3–5 internal links to other Tecorb blogs (related topics)
- 1–2 internal links to relevant Tecorb service pages (e.g., AI development, mobile app development)
- 1 link to the portfolio when referencing real work
- Anchor text: use descriptive, varied phrases — not "click here" or naked URLs

**Anchor text rules:**
- 40% exact-match keyword anchors (when the linked page targets that keyword)
- 40% partial-match / related-term anchors
- 20% branded or generic anchors ("Tecorb's approach to...")

**Hub-and-spoke pattern:** Each major service area (AI/ML, Mobile, Web, Enterprise) has a pillar page. Blog posts on related topics link up to the pillar; the pillar links down to specific blogs. This builds topical authority.

---

## 12. External linking

Yes, link out. Refusing to link externally is an old, broken instinct.

- Link to authoritative sources for claims (research papers, official docs)
- Link to tools you reference (their official site)
- 2–5 external links per post is normal
- Set `rel="noopener"` on `target="_blank"` links
- Use `rel="nofollow"` only for paid/sponsored links

Linking out to high-authority sources is a positive trust signal.

---

## 13. Image SEO

Every image:
- File name: descriptive kebab-case, includes keyword if relevant (`react-native-vs-flutter-performance-chart.webp`)
- Alt text: describes the image for screen readers AND for image search; 8–15 words; includes keyword only if natural
- Format: WebP preferred; AVIF for hero; PNG only for logos/transparency; never raw JPEG over 200KB
- Dimensions: featured 1200×630 (OG ratio); in-body 1200×800 max; lazy-load all below the fold
- Captions: optional but help engagement when the image is non-obvious

Images are pre-selected from the predefined library — see the `images-names` skill for the catalog and the `image-prompts` skill for the selection and upload workflow. No AI image generation is used.

---

## 14. Generative Engine Optimization (GEO)

AI Overviews (Google), ChatGPT Search, Perplexity, and Claude Search are now traffic sources. They pull from content differently than blue-link SERP.

**What gets cited by AI engines:**
1. **Direct, declarative sentences** — AI engines prefer "X is Y because Z" over "Many experts believe that X might be considered Y in some cases."
2. **Structured answers** — TL;DR blocks, FAQ blocks, comparison tables, numbered lists
3. **Recent dates** — A `dateModified` within 6 months matters more than ever
4. **Named entities and statistics** — "According to Statista's 2025 report" gets cited; vague "studies show" does not
5. **Direct quotes from experts** — Quote a real engineer in the post (a Tecorb tech lead works perfectly)

**Anti-patterns that kill AI citation:**
- Throat-clearing intros ("In today's fast-paced world of technology...")
- Hedged claims with no commitment
- Generic listicles with no original analysis
- Walls of text without subheadings

**Practical GEO checklist per post:**
- [ ] First paragraph contains a one-sentence definition or thesis
- [ ] At least 3 H2s phrased as questions
- [ ] At least one comparison table OR numbered list
- [ ] FAQ section with 5+ Q&A
- [ ] Named author + dateModified within last 6 months on refreshes
- [ ] One direct quote from a named Tecorb engineer or referenced expert

---

## 15. Content depth and word count

There is no universal "longer = better." Match depth to intent.

| Intent | Target range | Notes |
|---|---|---|
| Quick definition / "what is" | 800–1,200 | Don't pad; answer fast |
| Standard informational guide | 1,500–2,500 | Most Tecorb posts |
| Comparison / "X vs Y" | 1,800–2,800 | Tables + criteria |
| Comprehensive pillar page | 3,500–6,000 | Once per topic cluster |
| Tutorial / how-to | 1,200–2,500 | Word count varies with complexity |
| Listicle (top N) | 1,500–2,500 | ~150–200 words per item |

**Padding is more harmful than under-writing.** A 1,400-word post that answers cleanly outranks a 3,000-word post that buries the answer in transitional fluff. If a section adds no information, delete it.

---

## 16. Readability

Targets:
- **Flesch Reading Ease: 55–70** for technical blogs (above 70 = too casual for B2B)
- Average sentence length: **15–22 words**
- Average paragraph length: **3–4 sentences**
- Passive voice: **<10% of sentences**
- Reading grade level (Flesch-Kincaid): **8–11**

Tools: Hemingway Editor for sentence-level fixes; Yoast/RankMath in WordPress for inline feedback.

**Style notes specific to Tecorb's audience (CTOs, senior engineers, product leaders):**
- Don't dumb down concepts; do explain abbreviations on first use
- Acronyms: spell out once → "Large Language Model (LLM)" → use abbreviation after
- Code blocks count as content, not as text — they don't break flow

---

## 17. Pre-publish quality checklist

Before any post is submitted to WordPress, verify:

**Content**
- [ ] Title tag ≤60 chars, contains primary keyword
- [ ] Meta description 130–155 chars, has soft hook + value promise
- [ ] H1 differs from title tag (can; doesn't have to)
- [ ] One H1, hierarchical H2/H3 structure
- [ ] TL;DR block under H1
- [ ] Primary keyword in first 100 words
- [ ] FAQ section with 5+ items
- [ ] Author byline present and accurate
- [ ] Date published / modified visible
- [ ] Word count appropriate for intent
- [ ] All claims sourced or self-disclosed as opinion

**Technical SEO**
- [ ] Slug ≤60 chars, kebab-case, no stop words
- [ ] Featured image set, ≤200KB, WebP/AVIF, with alt text
- [ ] All in-body images have alt text and descriptive file names
- [ ] All external links open in new tab with `rel="noopener"`
- [ ] At least 3 internal links + 1 link to service/portfolio page
- [ ] Schema markup added (Article + FAQPage minimum)
- [ ] No broken links (run a quick check)
- [ ] Mobile preview looks clean (no overflow, readable on 375px width)

**Originality and quality**
- [ ] At least one insight not found in top 5 SERP competitors
- [ ] Real example or named project referenced (where applicable)
- [ ] No AI-generated "throat-clearing" intros
- [ ] No filler transitions ("Furthermore, it is important to note that...")
- [ ] Read aloud once — does it sound human?

---

## 18. Common mistakes to avoid

1. **Writing the post before checking the SERP.** You'll mismatch intent. Always SERP-first.
2. **Keyword stuffing.** Neural matching makes this counterproductive.
3. **No original insight.** If your post is the average of the top 10, it'll rank 11th.
4. **AI-default intros.** "In today's fast-paced digital landscape..." dies on contact.
5. **Listicle padding.** "10 Best X" with items 8–10 obviously phoned in.
6. **Vague claims with no source.** "Studies show 73% of businesses..." — which studies? Cite or cut.
7. **One CTA shouting on the page.** Embed soft CTAs in context; one hard CTA near the end.
8. **Forgetting the FAQ.** Easiest snippet/PAA wins, often skipped.
9. **No diagram for explainable mechanics.** Use the `mermaid-diagrams` skill; visuals dramatically increase dwell time.
10. **Publishing without updating the sitemap and pinging search engines.** See `wordpress-publishing` skill.

---

## Reference workflow

1. Receive title + brief from user
2. **SERP analysis** — review top 5 results for the target query; note intent, structure, depth, gaps
3. **Keyword + entity research** — primary, 3–5 secondaries, entity list, 5–10 long-tails, PAA questions
4. **Outline** — TL;DR + 6–9 H2s + FAQ section, with intended internal links pre-marked
5. **First draft** — write in passes (skeleton → flesh → polish), not top-to-bottom
6. **Optimization pass** — title, meta, slug, schema, alt text, internal/external links
7. **Quality checklist** (section 17)
8. **Hand off to `wordpress-publishing` skill** for upload

The output of this skill is always a publish-ready Markdown file + a metadata JSON sidecar with title tag, meta description, slug, focus keyword, secondary keywords, internal links, schema blocks, and image alt texts.