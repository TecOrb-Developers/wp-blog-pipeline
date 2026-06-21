---
description: Push a finalized draft to WordPress — uploads media, sets categories/tags/SEO meta, creates the post (as WP draft by default, or live with --live). Optionally pings IndexNow.
argument-hint: <slug-or-draft-path> [--live] [--schedule=ISO_DATETIME]
---

# /publish — Hand off to WordPress

You are running the **publish** command for the Tecorb Technologies content pipeline. Your job: take a finalized local draft and push it to WordPress via the `wp-publisher` sub-agent.

## Arguments
- `$1` = slug or path to draft folder (e.g., `top-vector-databases-rag-2026` or `drafts/top-vector-databases-rag-2026`)
- Optional flags in `$ARGUMENTS`:
  - `--live` → create the post as `publish` status (live immediately). Without this, default is `draft` status (you click Publish in WP admin).
  - `--schedule=YYYY-MM-DDTHH:MM:SS+00:00` → schedule for future publish (creates as `future` status). Mutually exclusive with `--live`.
  - `--update=<post_id>` → update an existing WordPress post instead of creating new (use when refreshing content). Requires explicit confirmation.

If `$1` is missing, ask the user which draft to publish. List candidates:
```bash
ls -d drafts/*/  # show available draft folders
```

## Step 0: Resolve the path and validate readiness

Normalize `$1`:
- If it starts with `drafts/`, use as-is
- Otherwise, prefix `drafts/`

Verify the draft folder exists and contains:
- `spec.json` with `"approved": true`
- `content.md`
- `metadata.json`
- `images/manifest.json` with at least the `featured` image entry (images are pre-selected from the library by `image-creator`)
- If `metadata.json` has non-empty `diagram_specs[]`, also `diagrams/manifest.json`

If any required file is missing, stop and tell the user exactly what's missing and how to fix it (re-run `/blog`, manually create the file, etc.). Do not proceed with a partial draft.

## Step 1: Resolve mode

Determine `mode` based on flags:
- Default → `draft`
- `--live` → `publish`
- `--schedule=...` → `schedule` (also extract the datetime into `schedule_at_gmt` in metadata.json before passing to publisher)
- `--update=<id>` → set update mode and capture the target post ID

If `mode == publish` (live), **confirm with the user once** before proceeding:
> "About to publish LIVE to `https://www.tecorb.com`. The post will be visible immediately and submitted to IndexNow. Reply `yes` to continue, anything else to abort."

If user replies anything but explicit yes (`y`, `yes`, `confirm`, `ship it`), abort and tell them to run without `--live` to create a WP draft first.

For `mode == draft`, no confirmation needed.

## Step 2: Verify WP credentials are loaded

```bash
[ -z "$WP_APP_PASS" ] && echo "WP_APP_PASS not set" && exit 1
[ -z "$WP_USER" ] && echo "WP_USER not set" && exit 1
```

If env vars aren't loaded, tell the user to ensure `.env` is sourced (Claude Code should pick it up automatically if at the project root; otherwise `source .env` before running).

Do not echo the password value back to chat under any circumstance.

## Step 3: Dispatch the wp-publisher sub-agent

Invoke the **wp-publisher** sub-agent with the draft path and mode.

Instruct the agent:
> "Use the wp-publisher subagent. Inputs: draft folder at `<path>`, mode = `<draft|publish|schedule|update>`. Read `metadata.json`, `images/manifest.json`, and `diagrams/manifest.json` (if exists). Follow your skill's workflow: verify auth, check slug collisions, upload media (featured → inline → diagrams), convert markdown to Gutenberg HTML rewriting media paths, inject JSON-LD schema, resolve categories/tags, create the post. If mode is `publish`, also submit to IndexNow. Save `publish-log.json` to the draft folder. Report back with post ID, post URL, admin edit URL, and any warnings."

If the agent reports the slug is already taken in WordPress:
- Print the conflict to the user
- Ask whether to append a numeric suffix (`-2`), pick a new slug, or update the existing post
- Do not proceed without explicit instruction

If the agent reports a SVG MIME-type rejection:
- The publisher will fall back to PNG automatically
- Surface the warning to the user with a one-line recommendation (install Safe SVG plugin or update allowed MIME types)

If the agent reports the SEO meta fields didn't take effect (Yoast/RankMath not registering in REST):
- Print the exact `register_post_meta` PHP snippet from `wordpress-publishing` SKILL.md Section 5
- Tell the user to add it to a small custom plugin or `functions.php`, then re-run `/publish`

## Step 4: Report results

Print to chat:
- ✓ Post created — ID `<id>`, status `<status>`
- **Admin edit URL:** `<url>` — open this to QA before going live
- **Preview URL:** `<url>` (for drafts)
- **Public URL:** `<url>` (if live)
- Media uploaded: `<count>` images, `<count>` diagrams
- IndexNow submitted: yes/no/skipped (only happens on live publish)
- Warnings (if any)

For draft mode, end with:
> "Open the admin edit URL, click Preview, verify the rendering. When happy:
> - Click **Publish** in WP admin yourself (recommended), OR
> - Run `/publish $1 --live` and I'll transition it to published and submit to IndexNow."

For live mode, end with:
> "Live at `<public_url>`. Submitted to IndexNow. Consider also submitting to Google Search Console manually (https://search.google.com/search-console) for the first few posts to confirm indexing behavior."

## Step 5: Save the run log

The wp-publisher writes `drafts/<slug>/publish-log.json`. Confirm it exists. This file:
- Tracks the post ID for future updates
- Records uploaded media IDs (useful for re-uploads if images change)
- Notes warnings encountered
- Enables resume-on-failure for future runs

## Constraints
- **Default to draft mode.** Never publish live without an explicit `--live` flag AND user confirmation.
- **Never echo `WP_APP_PASS`** to chat. Reference it only via the environment.
- **Never overwrite an existing post** without `--update=<id>` AND user confirmation.
- **If auth fails** (401/403), stop and tell the user to rotate the Application Password and verify the user role (must be Editor or Administrator).
- **If the IndexNow submission fails**, that's a soft failure — log it but don't fail the whole publish. The post is live; the search engine notification is best-effort.
- If you cannot find a way to confirm a step succeeded (e.g., post creation response is malformed), do not pretend it worked. Report the actual state.