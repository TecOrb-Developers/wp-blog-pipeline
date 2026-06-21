# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A Claude Code-native content pipeline for publishing SEO-optimized blog posts to any WordPress site via the REST API. There is no application code to build, test, or lint — the "code" is a set of agent definitions, slash commands, and skills that orchestrate the writing and publishing workflow.

## Pipeline overview

```
User writes blog_content.md
         ↓
     /blog command
         ↓
  seo-writer agent
  (enrich content, SEO pass)
  → drafts/<slug>/content.md
  → drafts/<slug>/metadata.json
         ↓
  Image selection
  (hero image from AI_Blog_1280_720)
  → drafts/<slug>/images/<slug>-featured.png
  → drafts/<slug>/images/manifest.json
         ↓
  wp-publisher agent
  → WP draft (or live with --live)
  → drafts/<slug>/publish-log.json
```

**All draft output lives under `drafts/<slug>/`.** The slug is kebab-case derived from the blog title with stop words removed.

## Slash commands

| Command | Purpose |
|---|---|
| `/blog [--live]` | Full pipeline — reads `blog_content.md`, enriches content, selects image, publishes to WP (draft by default). |
| `/publish <slug> [--live] [--schedule=ISO]` | Push a previously created draft to WordPress. Default creates a WP draft; add `--live` to publish immediately. |

## Sub-agents

Defined in `.claude/agents/`. Each agent reads the relevant skill files every invocation:

| Agent | Trigger | Key output |
|---|---|---|
| `seo-writer` | `/blog` command | `content.md`, `metadata.json` |
| `wp-publisher` | After image selection in `/blog`, or via `/publish` | `publish-log.json`, post created in WP |
| `style-matcher` | Manual refresh only | Style baseline for seo-writer calibration |

## Skills

Located in `.claude/skills/`. Agents **must** read the full skill file before acting:

- `seo-blog-writing/SKILL.md` — keyword strategy, intent matching, E-E-A-T, GEO
- `tecorb-style-guide/SKILL.md` — brand voice, heading cadence, CTA placement, callout box syntax (customize this for your brand)
- `wordpress-publishing/SKILL.md` — REST API endpoints, Gutenberg block structure, Yoast/RankMath meta keys, IndexNow
- `images_names/SKILL.md` — predefined image library catalog: 30 hero images (1280×720), with titles, filenames, and thematic descriptions
- `image-prompts/SKILL.md` — image selection workflow: how to choose the hero image, manifest format, alt text conventions

## Environment setup

Copy `.env.example` to `.env` and populate before running any command. The `.env` file is gitignored — never commit it.

Required variables:

```
WP_BASE_URL, WP_API_BASE, WP_USER, WP_APP_PASS, WP_DEFAULT_AUTHOR_ID
```

`INDEXNOW_KEY` is optional — only used during live publish to notify search engines.

## Input

The user writes raw blog content into `blog_content.md` at the project root. The file can be a rough draft, bullet points, or a full article — the seo-writer agent enriches it. The file must not be empty.

## Draft folder contract

A complete draft ready for `/publish` must have:
- `content.md`
- `metadata.json`
- `images/manifest.json` + the featured PNG (copied from `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/`)

`publish-log.json` is written by wp-publisher after a successful run and acts as a resume point if the publish fails mid-way.

## WordPress credentials

The WP user must be **Editor** or **Administrator**. The Application Password is generated at `wp-admin → Users → Profile → Application Passwords`. If auth returns 401/403, rotate the password — do not attempt to debug it in place.

SEO meta fields (`_yoast_wpseo_*` or `rank_math_*`) must be registered for the REST API. If they come back empty after post creation, the fix is in `wordpress-publishing/SKILL.md` Section 5.

## Spec

See `spec/new-updates.md` for the full requirements spec of this pipeline version.
