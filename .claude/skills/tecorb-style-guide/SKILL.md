---
name: tecorb-style-guide
description: The definitive style and design system for Tecorb Technologies' blog content — covering brand voice, audience persona, tone modulation, sentence rhythm, heading conventions, vocabulary preferences, CTA patterns, internal linking, author bylines, and the modern blog UI/UX template that replaces Tecorb's legacy blog design. Use this skill on every Tecorb blog post, page, or long-form deliverable. Trigger this skill whenever drafting content for tecorb.com, generating blog HTML/markdown for WordPress, designing the visual structure of a post, or evaluating whether copy "sounds like Tecorb." Do not write Tecorb-bound content without consulting this skill — voice and visual consistency define the brand more than any logo.
---

# Tecorb Technologies — Editorial & Design Style Guide

This guide replaces Tecorb's legacy blog style. The previous template (used in posts like the on-demand fuel delivery guide, Flutter widgets guide, OTT app features, etc.) is dated: long uniform paragraphs, weak hierarchy, generic stock images, minimal callouts, no TL;DR, and CTAs that don't convert. **This guide defines the new standard.**

Apply this skill alongside `seo-blog-writing`. SEO governs what to write; this guide governs how it sounds and how it looks.

---

## 1. Brand voice

Tecorb writes like a **senior technical partner**, not like an agency selling services or a tech blog chasing trends.

### Three voice attributes (in order of priority)

1. **Substantive** — Every paragraph teaches something specific. Tecorb's edge is 135+ engineers shipping production systems for Fortune 500s, funded startups, and government bodies. The writing must show that, not claim it. Specifics over adjectives, every time.

2. **Decisive** — Tecorb is the firm clients hire to *make a call*. Posts make recommendations, not hedge them. "It depends" is acceptable only when followed immediately by "Here's how to decide."

3. **Approachable** — The audience includes solo founders evaluating their first stack and CTOs at Fortune 500s. Use plain English. Acronyms get spelled out on first use. No academic posturing.

### Voice anti-patterns (do not do)

- "In today's fast-paced digital landscape..." — banned
- "Look no further!" — banned
- "Game-changer", "revolutionary", "cutting-edge" — banned outside direct quotes
- "Studies show..." with no link — banned
- "Hire us!" said directly — replaced by competence demonstration
- Hedge-stacking: "It may potentially be possible to perhaps..." — pick one
- Throat-clearing: "Before we dive in, let's first establish what..." — just dive in

### Voice exemplars

**Wrong:** "In the ever-evolving world of mobile app development, choosing the right framework has become a critical decision that can make or break your project's success."

**Right:** "Picking React Native or Flutter is a six-figure decision. The wrong choice doesn't just slow you down — it costs you a rewrite 18 months in. Here's how to decide."

**Wrong:** "Our team of expert developers leverages cutting-edge AI technologies to deliver world-class solutions."

**Right:** "We've shipped 14 production LLM features in the last 18 months, including fine-tuned domain models for a Fortune 500 logistics client and a voice agent for a HealthTech platform serving 2M users in Latin America."

---

## 2. Audience persona

Tecorb's blog readers split into three personas. Most posts target one primary; the other two are tertiary.

| Persona | Reads to... | Decides based on... |
|---|---|---|
| **Startup CTO / Founder-Engineer** (primary for AI, mobile, web stack posts) | Pick a stack, vendor, or pattern fast | Concrete trade-offs, real cost ranges, hiring difficulty, time-to-MVP |
| **Enterprise IT / Product Director** (primary for industry guides, comparison posts, cost guides) | De-risk a vendor decision, justify a recommendation internally | Case studies, scale claims with proof, compliance, support model |
| **Senior Engineer / Tech Lead** (primary for deep technical posts, tutorials) | Solve a specific problem, evaluate a tool | Code quality, specifics, gotchas, performance numbers |

Always know which persona the post is written for. Write the intro as if speaking directly to that one person.

---

## 3. Tone modulation by post type

Voice is constant; tone shifts with format.

| Post type | Tone | Example opener |
|---|---|---|
| Technical tutorial | Direct, instructional, second-person | "You'll build a voice agent that handles..." |
| Industry guide | Authoritative, third-person, data-led | "On-demand fuel delivery is a $3.4B market growing at 17% CAGR..." |
| Comparison / vs post | Decisive, balanced, opinionated at the end | "Both frameworks ship production apps. The right one for *your* project depends on three things." |
| Trends / opinion | Confident, slightly contrarian, named POVs | "Most AI agent frameworks won't survive 2026. Here's what to bet on." |
| Case study | First-person plural, specific, results-led | "When Ejaro hit 10x usage, the monolith couldn't keep up. We rebuilt the search layer in 6 weeks." |
| Listicle / top-N | Light editorial voice, ranked with criteria | "We compared 12 vector databases on cost, latency, and recall. Here are the 7 worth your time." |

---

## 4. Sentence and paragraph rhythm

### Sentences
- **Average length: 15–22 words.** Mix short and long deliberately.
- One idea per sentence. If you need two clauses joined by "and," consider splitting.
- Start sentences with the noun, not the throat-clearer. Cut "Furthermore," "Additionally," "In conclusion," "It is important to note that."
- Use active voice. Passive voice ≤10% of sentences.

### Paragraphs
- **1–4 sentences each.** Anything longer is a sign the paragraph is doing too much.
- One claim per paragraph, supported by example or evidence in the same paragraph.
- Vary opening: not every paragraph starts with "The" or "When."
- White space is a feature, not a waste.

### Rhythm pattern that works
A heading. A punchy 1-sentence claim. A 3-sentence elaboration with a specific example. A short transitional sentence. Move on.

---

## 5. Heading conventions

### H1
- Title-case (initial caps on major words)
- 50–70 characters
- Contains primary keyword, front-loaded
- One per page

### H2
- Title-case
- Scannable on its own — reading only H2s should reveal the post's argument
- 6–9 H2s per typical post
- Phrase as a question where it fits intent ("Why does this matter?", "When should you use X?")

### H3
- Sentence-case (only first word + proper nouns capitalized)
- Used inside an H2 for sub-points, list items, or FAQ questions
- 3–6 H3s under each major H2

### H4 and below
- Avoid unless the post is a deep technical tutorial with multi-level nesting.

### Heading-writing rules
- No questions ending with double punctuation
- No emojis in headings (allowed sparingly in body callouts)
- No all-caps
- No vague headings — "Conclusion" is fine; "Final Thoughts and Wrap-Up" is filler

---

## 6. Vocabulary preferences

### Always use
- "build" (not "develop" when "build" fits)
- "ship" (when describing release / delivery)
- "team" (not "resources" referring to people)
- "engineers" (not "developers" in formal claims)
- "platform," "system," "stack" (precise)
- "we" when describing Tecorb's work
- "you" when addressing the reader

### Avoid
- "Solutions" used generically ("our solutions help you...") — name the actual thing
- "Leverage" — use "use"
- "Utilize" — use "use"
- "Cutting-edge", "next-generation", "world-class" — show, don't claim
- "In today's [adjective] world" — banned across the entire site
- "Robust" — pick a specific attribute (fast, fault-tolerant, horizontally scalable)
- "Synergy" — banned
- "Stakeholder" — use the actual role (founder, PM, ops lead)

### Numbers
- Spell out 1–9; use numerals for 10+, except in stats and tables (always numerals)
- Use commas in 4-digit numbers (1,200 not 1200)
- Percent: use the symbol after the number (24%)
- Currency: include the symbol and ISO if non-USD ($120K, ₹1.2L, €80K)
- Year references: "in 2026" not "in the year 2026"

### Capitalization
- "AI" (always all caps)
- "ML" (always all caps)
- "iOS" (lowercase i)
- "MacOS" → "macOS"
- "Github" → "GitHub"
- "Javascript" → "JavaScript"
- "Typescript" → "TypeScript"
- "WordPress" (one word, CamelCase)
- "Node.js" (dot, lowercase js)
- "React Native" (two words, both caps)
- "open-source" as adjective; "open source" as noun
- Tecorb Technologies (or "Tecorb" after first mention)

---

## 7. The new blog template — UI/UX

The legacy template uses generic Featured Image → big H1 → wall of paragraphs → image → more paragraphs → end. The new template is built for skimmers, snippet capture, and conversion.

### Above-the-fold layout

```
┌─────────────────────────────────────────────────────────┐
│  Category tag    •   Reading time   •   Date            │  ← micro-meta strip
│                                                         │
│  ARTICLE TITLE (large, 48–64px on desktop)             │  ← H1
│                                                         │
│  One-sentence subhead in a lighter weight (20–22px)    │  ← deck
│                                                         │
│  ┌──────┐                                              │
│  │ 👤   │  Author Name • Role • [in] LinkedIn icon     │  ← author chip
│  └──────┘                                              │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  HERO IMAGE (16:9, 1200×675 displayed)         │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ╔═══════════════════════════════════════════════╗     │  ← TL;DR card
│  ║ TL;DR                                         ║     │   subtle gradient
│  ║                                               ║     │   left border accent
│  ║ • 3–5 bullet summary of the post              ║     │
│  ║ • Each bullet is a complete takeaway          ║     │
│  ║ • Specific, not vague                         ║     │
│  ╚═══════════════════════════════════════════════╝     │
└─────────────────────────────────────────────────────────┘
```

### Reading view (desktop, ≥1024px)

```
┌──────────────┬─────────────────────────────────┬──────────┐
│              │                                 │          │
│  Sticky TOC  │   Main content (max 720px      │  Empty / │
│  (260px)     │   column, ~70ch line length)   │   subtle │
│              │                                 │   share  │
│  • Section 1 │   ## H2 heading                │   icons  │
│  • Section 2 │                                 │          │
│    – Sub a   │   Paragraph text in a readable │          │
│    – Sub b   │   serif or modern sans-serif   │          │
│  • Section 3 │   at 18–19px / 1.7 line-height │          │
│  • FAQ       │                                 │          │
│              │   Callouts, code blocks,       │          │
│  ┌─────────┐ │   tables, images inline.       │          │
│  │ Reading │ │                                 │          │
│  │ progress│ │                                 │          │
│  │ bar     │ │                                 │          │
│  └─────────┘ │                                 │          │
│              │                                 │          │
└──────────────┴─────────────────────────────────┴──────────┘
```

### Mobile (<768px)

- TOC collapses into a tap-to-expand drawer pinned below the hero
- Reading progress = thin bar at top of viewport
- Author chip stays
- Pull-quotes and callouts go full-width
- Tables become horizontally scrollable with a soft fade

### Visual elements every blog uses

**1. TL;DR card** — Required. Top of post, after deck/hero. 3–5 bullets. Distinct background (subtle gradient or muted brand-tinted card). Sets the contract.

**2. Pull quote** — One per ~800 words. Italicized or in a distinct typeface. Either a key insight from the post or a direct quote from a named expert/engineer. Half-width on desktop, full-width on mobile.

**3. Stat callout** — Single-number emphasis for striking data points. Example:
```
┌─────────────────┐
│      73%        │
│  ───────────    │
│  of AI pilots   │
│  fail to reach  │
│  production     │
│  (Gartner 2025) │
└─────────────────┘
```

**4. Callout boxes** — Three types, each with a distinct icon and color tint:
- 💡 **Insight** — non-obvious observation
- ⚠️ **Watch out** — common mistake or risk
- ✅ **Pro tip** — actionable shortcut

These break up text density and are highly scannable.

**5. Comparison table** — At least one per comparison or evaluation post. Clean rows, no zebra-striping (use whitespace), bold the winner per row, footnote criteria.

**6. Inline diagram (Mermaid)** — When explaining process, flow, architecture, or hierarchy. See `mermaid-diagrams` skill. Always include a one-sentence caption.

**7. Code block** — Language label, copy button, syntax highlighting. Add a one-line comment above the block explaining what it does. Never dump >40 lines uncommented.

**8. Image with caption** — Every non-decorative image has a caption (italic, 14px, muted). Captions describe context, not just what's in the image.

**9. CTA card (end-of-section)** — One soft inline CTA at mid-post; one explicit CTA card before the related-posts section.

Mid-post soft CTA (example):
> *Need this kind of system built? [See how Tecorb approaches LLM platform engineering](#).*

End CTA card:
```
┌─────────────────────────────────────────────┐
│  Building a [topic]?                        │
│  Tecorb's team has shipped [N] of these    │
│  for clients like [Client A, Client B].    │
│                                             │
│  [ Book a 30-min architecture call → ]     │
└─────────────────────────────────────────────┘
```

**10. Author bio card** — End of article. Photo, name, role, 2-sentence bio, LinkedIn icon, links to other posts by author.

**11. Related posts** — 3-card grid. Cards show: thumbnail, title (clamped at 2 lines), category tag, reading time. No excerpt text — keep cards tight.

**12. Newsletter signup** — Inline, after related posts. Single email field + one button. No popup, ever.

### Typography spec

- **Body text**: 18–19px on desktop, 16–17px on mobile. Line-height 1.65–1.75. Max 70 characters per line.
- **Headings**: A modern geometric sans (Inter, Manrope, or similar) at clear scale (H1 48–64, H2 32–36, H3 24–26).
- **Body face**: Either a high-readability sans (Inter, Source Sans, IBM Plex Sans) or an editorial serif (Source Serif, Charter, Lora). Pick one and stick with it across the site.
- **Code**: A monospace pair (JetBrains Mono, Fira Code) at 14–15px in blocks; 90% body size inline.
- **Pull quotes**: Either italic serif at 22–26px or larger sans at lighter weight.

### Color and surface

(The brand should supply exact hex values; this guide specifies *roles*, not values.)

- **Surface**: Off-white (#FAFAFA range) or pure white background; near-black (#0E0E10 range) text — never pure black on pure white
- **Accent**: One brand accent for links, callout borders, and CTAs (Tecorb's primary brand color)
- **Muted**: Soft gray for meta info, captions, dividers
- **Callout tints**: Insight = soft blue; Watch out = warm amber; Pro tip = soft green — all at low saturation (background tint, not vivid)
- **Dark mode**: Required. Invert surface; reduce contrast slightly (true white text on true black causes halation — use #ECECEC on #121214)

### Spacing rhythm
- Section spacing: 48px top margin on H2, 32px on H3
- Paragraph spacing: 16–20px between paragraphs
- Image vertical margin: 32px top and bottom
- Callouts/quotes: 40px vertical margin

---

## 8. CTA patterns

### Inline soft CTAs
One per ~800 words. Phrased as helpful pointer, not sales pitch.

- *"Tecorb's AI team has built [specific thing] for [specific client type] — [link]."*
- *"This is the architecture we used on [Project Name]. [See the case study]."*
- *"Stuck on [problem]? [How Tecorb approaches X]."*

Do **not** drop "Hire us!" or "Contact us today!" mid-paragraph.

### End-of-article CTA card
Specific to the post's topic. Mentions named clients or concrete capability. Single primary action.

### Service-page links
Each post should link to ONE Tecorb service page that maps to the topic:
- AI / ML topics → `/services/ai-ml-development/`
- Mobile app topics → `/services/mobile-app-development/`
- Web full-stack → `/services/web-development/`
- Enterprise software → `/services/enterprise-software/`
- LLM / AI agents → `/services/llm-development/`

### Portfolio links
When referencing real work, link to `/portfolio/` or the specific case study page if it exists.

---

## 9. Internal linking patterns (Tecorb-specific)

Beyond the general rules in `seo-blog-writing`, Tecorb has these internal linking conventions:

- Every AI/ML post links to at least one other AI/ML post + the AI services page
- Every mobile post mentions a relevant Tecorb mobile project (Learn Autism, Caregiver Finder, etc.) and links to portfolio
- Every comparison post links to the Tecorb services page for both compared technologies
- Posts citing scale link to the "About" or "Why Choose Us" page where claims (135+ engineers, Fortune 500 clients) are listed
- Each post is linked from at least one other post within 30 days of publication (avoid orphan content)

---

## 10. Author bylines

Real human author with:
- **Name** (e.g., "Aakash Rana")
- **Role** (e.g., "Senior AI Engineer, Tecorb")
- **Photo** (round, 80px in bio card, 40px in author chip)
- **LinkedIn link**
- **2-sentence bio** in the bio card
- **Specialization tags** (e.g., "LLMs", "RAG", "Voice AI")

Bylines map authors to topic areas — AI engineers author AI posts; mobile leads author mobile posts. Marketing-only bylines undermine E-E-A-T.

For company-announcement or company-history posts only, the byline may read **"The Tecorb Team"**.

---

## 11. Opening hooks — examples by post type

### Technical tutorial
> *"Voice AI agents that actually work in production share three things. We learned them the hard way after deploying agents for a HealthTech client serving 2M users in Latin America. Here's the build."*

### Industry guide
> *"India's on-demand fuel delivery market is projected to hit $1.6B by 2028 — but the unit economics break for anyone who doesn't get the routing math right. This guide covers what we've learned building these systems."*

### Comparison / vs post
> *"React Native and Flutter both ship apps that scale. The wrong choice still costs you 4–6 months of rework. After shipping 60+ apps on both, here's the decision framework we use."*

### Trends / opinion
> *"Eighty percent of the AI agent frameworks shipping in 2025 won't exist in 2027. We bet on three. Here's why."*

### Listicle / top-N
> *"We tested 14 vector databases against production workloads — RAG over 12M chunks, sub-100ms latency target. Seven are worth your time. The rest fail at scale."*

Each hook:
- Names a specific number, project, or claim in the first 20 words
- Establishes Tecorb's experience without bragging
- Promises the reader a clear payoff

---

## 12. Conclusion patterns

Conclusions are NOT summaries. They are decision points or next steps. Pick one of three patterns:

### A. Decision-maker close
> *"Pick React Native if [criteria]. Pick Flutter if [criteria]. If you're still unsure, the deciding factor is usually [thing]."*

### B. Next-step close
> *"The fastest path to a production voice agent: pick LiveKit + Deepgram, prototype on a single use case, instrument latency obsessively. Tecorb's voice AI team can take the build from prototype to production — [link]."*

### C. Forward-look close
> *"On-device LLMs will reshape mobile development in 2026. The teams who experiment now will own the next category of apps."*

End with the end-of-article CTA card immediately after.

---

## 13. Patterns to avoid (legacy template carryovers)

Looking at the older posts (the on-demand fuel delivery guide, Flutter widgets piece, OTT app features, Flutter vs React Native 2023, UI/UX importance), these specific patterns are **out** in the new style:

- ❌ Long uniform paragraphs with no callouts, quotes, or visual breaks
- ❌ Generic stock images at the top of each H2 section
- ❌ Numbered listicles that repeat "1. Feature Name — Lorem ipsum description..." with no visual differentiation
- ❌ "In conclusion," / "In summary," wrap-ups that restate the post
- ❌ CTAs at the bottom that read "Contact us today to develop your app!" with no specifics
- ❌ Author bylines reading "by Admin" or absent entirely
- ❌ FAQ sections written as Q: ... A: ... in plain text (no schema, no accordion)
- ❌ Date stamps showing the post is from 2021–2023 with no `dateModified` refresh
- ❌ Image alt text identical to file name (`image1.jpg` → alt="image1")
- ❌ No TL;DR, no inline diagrams, no comparison tables

The new template fixes all of these. Use this guide to refresh older posts when they're updated.

---

## 14. Pre-publish style checklist

Run before handing off to `wordpress-publishing`:

**Voice and tone**
- [ ] Reads like a senior technical partner, not an agency selling
- [ ] No banned phrases ("cutting-edge", "world-class", "in today's...")
- [ ] Specific examples — at least one named client, project, number, or tool per major section
- [ ] Tone matches post type (tutorial / guide / comparison / etc.)

**Structure**
- [ ] TL;DR card present, 3–5 bullets, specific
- [ ] Hero image set with caption
- [ ] H2 headings tell the story when read alone
- [ ] At least one pull quote, one callout box, one diagram (where topic allows)
- [ ] Comparison table present if post is a comparison/evaluation
- [ ] FAQ section with 5+ items
- [ ] Author byline with photo, role, LinkedIn
- [ ] One mid-post soft CTA, one end-of-article CTA card
- [ ] 3+ internal links to other Tecorb content
- [ ] 1+ link to relevant service page
- [ ] 1+ link to portfolio (where applicable)
- [ ] Related-posts section reflects truly related posts

**Visual**
- [ ] All non-decorative images have meaningful captions
- [ ] Code blocks have language labels and comments
- [ ] Tables don't break on mobile width
- [ ] No image is purely decorative without alt text (alt="" for purely decorative is OK)
- [ ] Dark-mode preview rendered without issues

---

## 15. Refreshing legacy content

When updating an older Tecorb blog (anything pre-2024 template):

1. Audit against this guide and the SEO checklist
2. Rewrite intro to current voice
3. Add TL;DR card
4. Restructure H2s for scannability and snippet capture
5. Select images from the predefined library (see `images-names` and `image-prompts` skills)
6. Add one diagram (see `mermaid-diagrams`)
7. Add FAQ section with schema
8. Update CTAs to current pattern
9. Add named author byline with photo
10. Set `dateModified` in WordPress
11. Notify Google via Search Console URL inspection / sitemap ping

A refresh isn't a tweak; it's a re-publication. Treat it that way.

---

## Reference: the Tecorb voice in one paragraph

> *Tecorb writes like the senior engineer at your weekly architecture review — the one who's shipped the thing you're trying to ship, who tells you the trade-offs without selling you, who points to the specific paragraph in the docs, and who, when you eventually ask "could you build this for us," already has a name and a timeline.*

That's the bar. Every post.