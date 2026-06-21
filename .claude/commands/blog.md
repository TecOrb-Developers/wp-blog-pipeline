---
description: Full pipeline — reads blog_content.md, enriches content, selects hero image, publishes to WordPress as draft (or live with --live).
argument-hint: "[--live]"
---

# /blog — Full Pipeline Orchestrator

You are running the **blog** command for the Tecorb Technologies content pipeline. Your job: read `blog_content.md`, enrich it, select a hero image, and publish to WordPress.

## Arguments

- `--live` — publish immediately as live post (requires explicit `yes` confirmation). Without this flag, the default is WP draft status.

## Step 0: Validate input

Read `blog_content.md` from the project root.

If the file is empty or has fewer than 3 meaningful lines of content, **stop immediately** and tell the user:
> "`blog_content.md` is empty. Add your blog content to this file, then re-run `/blog`."

Do not proceed.

## Step 1: Content enrichment and SEO pass

Invoke the **seo-writer** sub-agent. Pass the full path `blog_content.md` as input.

Instruct the agent:
> "Use the seo-writer subagent. Input: read the raw blog content from `blog_content.md` at the project root. Enrich the content: fix weak or missing introductions, add missing H2 sections a reader would expect, add a FAQ section if one is absent. Do NOT add a TL;DR block. Strip all emoji — none may appear anywhere in the output. Do NOT write the H1/post title inside content.md — the theme renders it from the post title field. Do NOT add any image markers — the featured image is set separately via the featured_media field. Run a full SEO pass: extract the focus keyword from the title and body theme, derive the slug, write the meta description, assign category and tag slugs. Produce `drafts/<slug>/content.md` and `drafts/<slug>/metadata.json`. Do not select images. Report back: slug, word count, reading time, and any assumptions made."

Wait for the seo-writer to complete. After it finishes:
- Read the slug from `metadata.json`
- Confirm `drafts/<slug>/content.md` and `drafts/<slug>/metadata.json` exist
- Print: slug, word count, reading time

If the agent surfaces any clarifying questions about factual claims, surface them to the user before continuing.

## Step 2: Hero image selection

Read `.claude/skills/images_names/SKILL.md` to access the full image catalog.

Select the **single best-matching hero image** (1280×720) from `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/` that matches the blog's primary topic:

1. Read `drafts/<slug>/content.md` — identify the primary technology/subject
2. Consult the Summary Reference Table in the `images_names` skill — filter by category and key technologies
3. Read the Image about description for the top 1-2 candidates to confirm thematic fit
4. Select 1 image
5. Verify the file exists at `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/<filename>`
6. Copy it to `drafts/<slug>/images/<slug>-featured.png`
7. Write `drafts/<slug>/images/manifest.json`:

```json
{
  "featured": {
    "source_file": "<exact filename from library>",
    "source_folder": "drafts/images_to_use/images/pre_images/AI_Blog_1280_720",
    "local_copy": "drafts/<slug>/images/<slug>-featured.png",
    "alt": "<8-15 word description of what the image depicts>",
    "caption": null,
    "role": "featured"
  }
}
```

Alt text must describe what is visually depicted (8-15 words). No emoji. No keyword stuffing.

Confirm both files exist before proceeding to Step 3.

## Step 3: Publish to WordPress

Resolve publish mode:
- If `--live` flag was passed → mode = `publish` (requires confirmation below)
- Otherwise → mode = `draft`

**If mode = publish (live):** Confirm with the user before proceeding:
> "About to publish LIVE to `https://www.tecorb.com`. The post will be visible immediately. Reply `yes` to continue, anything else to abort."
If the user replies anything other than `yes`, `y`, or `confirm` — abort. Do not publish.

Invoke the **wp-publisher** sub-agent.

Instruct the agent:
> "Use the wp-publisher subagent. Draft folder: `drafts/<slug>/`. Mode: `<draft|publish>`. Read `metadata.json`, `images/manifest.json`. Follow your skill's workflow: verify auth, check slug collisions, upload featured image to WP Media Library, convert `content.md` to Gutenberg HTML rewriting the image path to the uploaded WP URL, inject JSON-LD schema, resolve categories and tags, create the post. If mode is `publish`, submit to IndexNow. Save `publish-log.json`. Report: post ID, post URL, admin edit URL, any warnings."

Wait for completion.

## Step 4: Report results

Print to chat:
- Slug and post title
- Draft folder: `drafts/<slug>/`
- Post ID and status (draft / live)
- Admin edit URL — open this to QA the post
- Preview URL (for drafts) or public URL (for live posts)
- Hero image selected: filename
- Word count, reading time
- Any warnings from sub-agents

For draft mode, end with:
> "Open the admin edit URL, click Preview, verify the rendering. When ready: click Publish in WP admin, or run `/publish <slug> --live` to publish and submit to IndexNow."

For live mode, end with:
> "Post is live at `<public_url>`. Submitted to IndexNow."

## Constraints

- **Never skip Step 0.** If `blog_content.md` is empty, stop.
- **No emoji anywhere** — in content.md, metadata.json, image alt text, nothing.
- **Default to draft mode.** Live publish requires `--live` AND explicit `yes`.
- **Image source folder is `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/`** — not `default/`. Do not use any other path.
- **One hero image only.** No in-body images. No diagrams.
- **If seo-writer fails**, stop. Do not run image selection or publishing on incomplete content.
- **If image file is not found** in the source folder, tell the user which image was selected and that the file is missing — do not proceed to publish.
- **If WP auth fails** (401/403), stop and tell the user to rotate the Application Password in WP admin.
