---
name: wordpress-publishing
description: Complete workflow for publishing blog posts to a WordPress site via the REST API — covering authentication with Application Passwords, uploading featured and in-body media, creating draft/scheduled/published posts, setting categories and tags, populating Yoast SEO and RankMath meta fields, adding JSON-LD schema, updating the sitemap, pinging search engines after publish, and handling common errors. Use this skill whenever the task involves uploading content to WordPress, scheduling a post, attaching images to a WP post, setting SEO meta on a WP post, regenerating sitemaps, or fixing a failed publish. Trigger this skill for any task that touches the tecorb.com WordPress backend or any other WordPress site, including read operations (fetching post lists, checking taxonomies, listing existing posts before insert). Do not write WordPress integration code from memory — consult this skill for current endpoints and payload shapes.
---

# WordPress Publishing — Tecorb Pipeline

This skill governs all programmatic interactions with the Tecorb WordPress instance (and serves any other WordPress site). It covers the full publish workflow: auth → media upload → post creation → SEO meta → schema → categorization → publish → post-publish notifications.

The Tecorb publisher agent uses these patterns end-to-end. Code examples are shown in `curl`, Python, and Node.js — pick the one that fits the calling agent.

---

## 1. Prerequisites and one-time setup

### Application Password
WordPress 5.6+ ships with Application Passwords — the right auth method for API publishing. Do **not** use basic-auth-with-user-password or JWT plugins.

**Setup (one-time, in WP admin):**
1. Users → Profile → scroll to **Application Passwords**
2. Name: `tecorb-content-pipeline` (or per-environment name)
3. Click **Add New Application Password**
4. **Copy the 24-character generated password immediately** — it's shown only once
5. Store securely (env var, password manager, vault)

The auth header for every request:
```
Authorization: Basic base64(username:application_password)
```

In code:
```bash
# bash
USER="contenteditor"
APP_PASS="xxxx xxxx xxxx xxxx xxxx xxxx"  # paste the 24-char string with or without spaces
AUTH=$(echo -n "${USER}:${APP_PASS}" | base64)
```

```python
# Python
import base64, os
user = os.environ["WP_USER"]
app_pass = os.environ["WP_APP_PASS"]
auth = base64.b64encode(f"{user}:{app_pass}".encode()).decode()
HEADERS = {"Authorization": f"Basic {auth}"}
```

```javascript
// Node
const auth = Buffer.from(`${process.env.WP_USER}:${process.env.WP_APP_PASS}`).toString('base64');
const headers = { Authorization: `Basic ${auth}` };
```

### Environment variables (Tecorb convention)
```
WP_BASE_URL=https://www.tecorb.com
WP_API_BASE=https://www.tecorb.com/wp-json/wp/v2
WP_USER=<content-editor-username>
WP_APP_PASS=<24-char application password>
WP_DEFAULT_AUTHOR_ID=<author ID for the agent-published posts>
```

### Required plugins (verify before first run)
- **Yoast SEO** OR **RankMath** (Tecorb uses one — check `/wp-admin/`)
- One of: **Yoast SEO REST API** (built-in for newer Yoast versions) OR **RankMath PRO** REST endpoints OR a meta-fields exposure approach (see Section 5)
- A **sitemap generator** — Yoast and RankMath both ship XML sitemaps automatically

---

## 2. API base and common endpoints

Base: `{WP_BASE_URL}/wp-json/wp/v2/`

| Operation | Endpoint | Method |
|---|---|---|
| List posts | `/posts` | GET |
| Get single post | `/posts/{id}` | GET |
| Create post | `/posts` | POST |
| Update post | `/posts/{id}` | POST or PUT |
| Delete post | `/posts/{id}` | DELETE |
| Upload media | `/media` | POST |
| Get media | `/media/{id}` | GET |
| List categories | `/categories` | GET |
| Create category | `/categories` | POST |
| List tags | `/tags` | GET |
| Create tag | `/tags` | POST |
| List users | `/users` | GET |
| Yoast meta (per-post) | `/posts/{id}` (in `meta` or `yoast_head_json`) | POST |
| RankMath meta | `/posts/{id}/meta` (custom fields) | POST |

Sanity check on first run:
```bash
curl -s -H "Authorization: Basic $AUTH" \
  "https://www.tecorb.com/wp-json/wp/v2/users/me" | jq .
```
If this returns the editor user, auth is working.

---

## 3. Media upload (always happens first)

Featured and in-body images must be uploaded to the WP Media Library **before** they can be attached to a post. The media endpoint returns a media `id` you'll reference.

### Upload a single image
```bash
curl -X POST \
  -H "Authorization: Basic $AUTH" \
  -H "Content-Disposition: attachment; filename=\"featured-image.webp\"" \
  -H "Content-Type: image/webp" \
  --data-binary @./drafts/my-post/images/featured.webp \
  "$WP_API_BASE/media"
```

```python
import requests

def upload_media(file_path, alt_text, caption=None, title=None):
    filename = file_path.split("/")[-1]
    mime = "image/webp" if filename.endswith(".webp") else "image/jpeg"
    headers = {
        **HEADERS,
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": mime,
    }
    with open(file_path, "rb") as f:
        r = requests.post(f"{WP_API_BASE}/media", headers=headers, data=f.read())
    r.raise_for_status()
    media = r.json()
    media_id = media["id"]

    # Update alt text / caption / title (separate PATCH-style call)
    update = {
        "alt_text": alt_text,
        "caption": caption or "",
        "title": title or alt_text,
    }
    requests.post(f"{WP_API_BASE}/media/{media_id}", headers=HEADERS, json=update).raise_for_status()
    return media_id, media["source_url"]
```

**Important:** The initial upload accepts only the binary; metadata (`alt_text`, `caption`) must be set in a second call against `/media/{id}`. Don't skip that second call — alt text is required for SEO and accessibility.

### Image source
Images are **not AI-generated**. They are pre-selected from the predefined library at `default/images/pre_images/` — one hero image from `AI_Blog_1280_720/` and two in-body images from `AI_Blog_450_450/`. Confirm each file exists in that folder before uploading. See the `images-names` skill for the catalog and the `image-prompts` skill for the selection and manifest workflow.

### File format and size guardrails
- Format: WebP preferred; PNG originals from the library are acceptable; never raw uncompressed JPEG
- Featured image: 1280×720 (from the library). Display max 1200px wide.
- In-body images: 450×450 (from the library); compress to <100KB
- File names before upload: rename to kebab-case with post slug prefix (`{post-slug}-featured.png`, `{post-slug}-inline-01.png`), never upload with the original library filename

---

## 4. Creating the post

Minimum viable post payload:

```json
{
  "title": "Article Title Here",
  "slug": "article-slug-here",
  "content": "<rendered HTML or block markup>",
  "excerpt": "Short excerpt (≤155 chars).",
  "status": "draft",
  "author": 12,
  "featured_media": 4567,
  "categories": [8, 12],
  "tags": [34, 56, 78],
  "comment_status": "closed",
  "ping_status": "closed",
  "format": "standard"
}
```

### Status values
| Value | Meaning |
|---|---|
| `draft` | Default for new posts — recommended for human review |
| `pending` | Awaiting review (editor workflow) |
| `future` | Scheduled — requires `date` and `date_gmt` set in the future |
| `publish` | Live immediately |
| `private` | Visible only to logged-in admins |

**Tecorb workflow default:** Create as `draft`, let a human approve in WP admin, then transition to `publish` with a second PATCH call. Only use `publish` directly when the calling agent has explicit authorization for live publish.

### Scheduling a post
```python
from datetime import datetime, timezone, timedelta

# Publish 2 days from now at 09:00 IST (= 03:30 UTC)
publish_at = datetime.now(timezone.utc) + timedelta(days=2)
publish_at = publish_at.replace(hour=3, minute=30, second=0, microsecond=0)

payload["status"] = "future"
payload["date_gmt"] = publish_at.isoformat().replace("+00:00", "")
payload["date"] = publish_at.astimezone().isoformat()  # site timezone
```

### Content format

WordPress accepts:
- **Classic HTML** in the `content` field (simplest; works on any theme)
- **Gutenberg block markup** (HTML with `<!-- wp:paragraph -->` comments) — required if the theme uses block templates and you want full block-editor compatibility

Tecorb default: Gutenberg block markup. Example block:
```html
<!-- wp:paragraph -->
<p>Body paragraph text here.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">Section Heading</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":4569,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large">
  <img src="https://www.tecorb.com/.../image.webp" alt="alt text here" class="wp-image-4569"/>
  <figcaption>Optional caption.</figcaption>
</figure>
<!-- /wp:image -->
```

A markdown → Gutenberg HTML converter step is part of the publisher agent's pipeline. Use a deterministic converter (Python `markdown` library with a custom Gutenberg renderer, or a Node lib like `unified` + custom remark plugin). Do not hand-write Gutenberg comments for body content.

### Full create-post example (Python)
```python
def create_post(post_data):
    """
    post_data is a dict with: title, slug, content (HTML), excerpt,
    featured_media (int), categories (list[int]), tags (list[int]),
    author (int), status, and optionally date / date_gmt.
    """
    r = requests.post(f"{WP_API_BASE}/posts", headers=HEADERS, json=post_data)
    r.raise_for_status()
    return r.json()  # contains the new post's id and link
```

---

## 5. SEO meta fields (Yoast and RankMath)

This is the most failure-prone area. Pick the right approach based on which plugin is active.

### Approach A: Yoast SEO (Tecorb's current setup, verify in WP admin)

**Modern Yoast (≥ 19.x)** exposes meta fields via the `meta` object in the post payload, **but only if registered**. Yoast registers these by default:

```json
{
  "meta": {
    "_yoast_wpseo_title": "Article Title | Tecorb",
    "_yoast_wpseo_metadesc": "Compelling 130–155 char meta description.",
    "_yoast_wpseo_focuskw": "primary keyword",
    "_yoast_wpseo_canonical": "https://www.tecorb.com/article-slug/"
  }
}
```

If the `meta` keys don't take effect, the fields aren't whitelisted in REST. Fix server-side by adding to `functions.php` or a small custom plugin:

```php
add_action('init', function() {
    register_post_meta('post', '_yoast_wpseo_title', [
        'show_in_rest' => true, 'single' => true, 'type' => 'string',
        'auth_callback' => function() { return current_user_can('edit_posts'); }
    ]);
    register_post_meta('post', '_yoast_wpseo_metadesc', [
        'show_in_rest' => true, 'single' => true, 'type' => 'string',
        'auth_callback' => function() { return current_user_can('edit_posts'); }
    ]);
    register_post_meta('post', '_yoast_wpseo_focuskw', [
        'show_in_rest' => true, 'single' => true, 'type' => 'string',
        'auth_callback' => function() { return current_user_can('edit_posts'); }
    ]);
});
```

### Approach B: RankMath

RankMath uses different meta keys:
```json
{
  "meta": {
    "rank_math_title": "Article Title | Tecorb",
    "rank_math_description": "Compelling 130–155 char meta description.",
    "rank_math_focus_keyword": "primary keyword",
    "rank_math_canonical_url": "https://www.tecorb.com/article-slug/",
    "rank_math_robots": ["index", "follow"]
  }
}
```

Same registration pattern in `functions.php` if fields don't accept via REST.

### Approach C: Schema markup as a custom field

For JSON-LD schema not auto-generated by the SEO plugin (FAQ, HowTo, etc.), inject directly into the post `content` as a `<script type="application/ld+json">` block at the end of the HTML body. This is theme-independent and reliable.

```html
<!-- end of content block -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [ ... ]
}
</script>
```

WordPress doesn't strip `<script>` tags from post content when posted by users with `unfiltered_html` capability (Administrator role). For Editor-level users, the agent must use a snippet plugin or a `wp_head` hook custom field. **Tecorb's content-editor user has Administrator role** — `<script>` tags pass through.

### SEO meta verification

After creating/updating a post, verify Yoast/RankMath fields stuck:
```bash
curl -s -H "Authorization: Basic $AUTH" \
  "$WP_API_BASE/posts/$POST_ID?context=edit" | jq '.meta'
```

If the values are empty, your meta registration is wrong (see above).

---

## 6. Categories and tags

### Resolve category by slug
```python
def get_or_create_category(slug, name=None):
    r = requests.get(f"{WP_API_BASE}/categories",
                     headers=HEADERS, params={"slug": slug})
    r.raise_for_status()
    results = r.json()
    if results:
        return results[0]["id"]
    # create
    r = requests.post(f"{WP_API_BASE}/categories",
                      headers=HEADERS,
                      json={"slug": slug, "name": name or slug.title()})
    r.raise_for_status()
    return r.json()["id"]
```

Same pattern for tags via `/tags` endpoint.

### Tecorb's blog taxonomy
Standard categories (verify against live site):
- `ai-ml` — AI / ML / LLM topics
- `mobile-app-development` — iOS, Android, React Native, Flutter
- `web-development` — Ruby on Rails, Next.js, MERN/MEAN
- `enterprise-software` — B2B platforms, government
- `industry-guides` — vertical-specific deep dives
- `comparisons` — X vs Y posts
- `tutorials` — how-to posts
- `trends` — opinion / future-looking

Tags are more granular (specific frameworks, technologies, industries). Don't create tags spuriously — check for existing tags first.

---

## 7. Full publish pipeline (orchestration)

```python
def publish_blog(draft_dir: str, mode: str = "draft"):
    """
    draft_dir contains:
      - content.md          (the blog markdown)
      - metadata.json       (title, slug, excerpt, focus_kw, secondary_kws,
                             category_slugs, tag_slugs, schema_blocks)
      - images/             (featured.webp + inline-*.webp)
      - images/manifest.json (alt text per image)
    mode: "draft" | "publish" | "schedule"
    """
    meta = load_json(f"{draft_dir}/metadata.json")
    image_manifest = load_json(f"{draft_dir}/images/manifest.json")

    # 1. Upload featured image
    featured_id, featured_url = upload_media(
        f"{draft_dir}/images/featured.webp",
        alt_text=image_manifest["featured"]["alt"],
        caption=image_manifest["featured"].get("caption"),
    )

    # 2. Upload in-body images and build a map (relative path → uploaded URL)
    url_map = {}
    for local_name, info in image_manifest.get("inline", {}).items():
        _, url = upload_media(
            f"{draft_dir}/images/{local_name}",
            alt_text=info["alt"],
            caption=info.get("caption"),
        )
        url_map[local_name] = url

    # 3. Convert markdown to Gutenberg HTML, rewriting image paths
    html = markdown_to_gutenberg(
        read_text(f"{draft_dir}/content.md"),
        image_url_map=url_map,
        schema_blocks=meta.get("schema_blocks", []),
    )

    # 4. Resolve categories/tags
    cat_ids = [get_or_create_category(s) for s in meta["category_slugs"]]
    tag_ids = [get_or_create_tag(s) for s in meta["tag_slugs"]]

    # 5. Build payload
    payload = {
        "title": meta["title"],
        "slug": meta["slug"],
        "content": html,
        "excerpt": meta["excerpt"],
        "status": "draft" if mode == "draft" else ("future" if mode == "schedule" else "publish"),
        "author": int(os.environ["WP_DEFAULT_AUTHOR_ID"]),
        "featured_media": featured_id,
        "categories": cat_ids,
        "tags": tag_ids,
        "comment_status": "closed",
        "ping_status": "closed",
        "format": "standard",
        "meta": {
            "_yoast_wpseo_title": meta["seo_title"],
            "_yoast_wpseo_metadesc": meta["meta_description"],
            "_yoast_wpseo_focuskw": meta["focus_keyword"],
        },
    }

    if mode == "schedule":
        payload["date_gmt"] = meta["schedule_at_gmt"]
        payload["date"] = meta["schedule_at_local"]

    # 6. Create post
    post = create_post(payload)
    post_id = post["id"]
    post_url = post["link"]

    # 7. Post-publish: notify search engines (only if actually published)
    if mode == "publish":
        ping_search_engines()

    return {"id": post_id, "url": post_url, "status": payload["status"]}
```

---

## 8. Sitemap and search engine notification

### Sitemap regeneration
If using Yoast or RankMath, the XML sitemap regenerates automatically on post publish. No manual action needed.

Sitemap URLs (verify which is live):
- Yoast: `https://www.tecorb.com/sitemap_index.xml`
- RankMath: `https://www.tecorb.com/sitemap_index.xml`
- WordPress core: `https://www.tecorb.com/wp-sitemap.xml`

### Pinging search engines

**Google:**
Google has deprecated the sitemap ping endpoint (as of mid-2023, `/ping?sitemap=` no longer triggers a fetch). The replacement is **Google Search Console URL Inspection API** — but that requires OAuth setup.

The practical Tecorb approach:
1. Ensure the sitemap is referenced in `robots.txt`:
   ```
   Sitemap: https://www.tecorb.com/sitemap_index.xml
   ```
2. After publish, use the **GSC URL Inspection API** to request indexing for the specific post URL (requires service account auth — see GSC API docs).
3. As a backup, submit the URL manually via Search Console once for the first 50 posts to confirm indexing behavior.

**Bing / IndexNow:**
IndexNow is still operational and works for Bing, Yandex, and others.

```python
def submit_to_indexnow(urls):
    """
    Submit one or more URLs via IndexNow. Requires an IndexNow key file
    hosted at https://www.tecorb.com/{key}.txt.
    """
    api_key = os.environ["INDEXNOW_KEY"]
    payload = {
        "host": "www.tecorb.com",
        "key": api_key,
        "keyLocation": f"https://www.tecorb.com/{api_key}.txt",
        "urlList": urls if isinstance(urls, list) else [urls],
    }
    r = requests.post("https://api.indexnow.org/IndexNow", json=payload)
    return r.status_code  # 200 or 202 = accepted
```

### robots.txt sanity
For a WordPress site, robots.txt is typically dynamically generated by the SEO plugin. Manual override goes in plugin settings, not on disk. The agent should:
- Verify `robots.txt` references the current sitemap URL
- Confirm no `Disallow: /` rules block the blog
- Update only when the site structure changes — not per blog post

---

## 9. Common errors and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| `401 Unauthorized` | Wrong username, bad app password, or app passwords disabled | Regenerate app password; confirm Users → Profile → Application Passwords section is visible |
| `403 Forbidden` | User lacks `edit_posts` capability | Use an Editor or Administrator account; not a Contributor |
| `rest_cannot_create` on `/media` | Upload exceeds PHP `upload_max_filesize` or `post_max_size` | Compress image; or raise php.ini limits |
| `featured_media` set but image not showing | Featured media ID belongs to a different attachment | Re-upload; confirm returned ID matches |
| `meta` fields silently empty after POST | Meta key not registered in REST | Add `register_post_meta` snippet (Section 5) |
| `slug` collisions appending `-2`, `-3` | An existing post or draft owns the slug | Check existing posts via GET `/posts?slug=` before publish |
| Gutenberg shows "block recovery" warning | Hand-written block markup is malformed | Always use a proven md→Gutenberg converter; never hand-edit block comments |
| Scheduled post stuck at "Missed schedule" | WP-Cron not firing | Set up real cron via server `wp cron event run --due-now` or install a "Missed Schedule" plugin |
| Image alt text empty after upload | Second metadata call skipped | Always call POST `/media/{id}` after binary upload to set alt/caption/title |
| Yoast title appears literal `%%title%%` | Yoast variables aren't resolved when set via REST | Use literal title strings, not Yoast variables, when writing via API |
| `application/ld+json` script stripped from content | Editor user lacks `unfiltered_html` | Grant Administrator role, or inject schema via `wp_head` filter instead |

---

## 10. Read operations (useful for pre-publish checks)

### List recent posts
```bash
curl -s -H "Authorization: Basic $AUTH" \
  "$WP_API_BASE/posts?per_page=20&status=publish,draft&orderby=date&order=desc" | jq '.[] | {id, title: .title.rendered, status, link}'
```

### Check if a slug is taken
```python
def slug_exists(slug):
    r = requests.get(f"{WP_API_BASE}/posts",
                     headers=HEADERS,
                     params={"slug": slug, "status": "any"})
    return len(r.json()) > 0
```

### Fetch author IDs
```bash
curl -s -H "Authorization: Basic $AUTH" \
  "$WP_API_BASE/users?per_page=50" | jq '.[] | {id, name, slug}'
```

---

## 11. Updating an existing post

Same endpoint as create, but POST to `/posts/{id}` with only the fields you want to change. To trigger a "modified" date refresh (important for SEO refreshes):

```python
def refresh_post(post_id, updates):
    # Force dateModified to update by including the modified field
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "")
    updates["modified_gmt"] = now
    r = requests.post(f"{WP_API_BASE}/posts/{post_id}", headers=HEADERS, json=updates)
    r.raise_for_status()
    return r.json()
```

For content refreshes, also submit the URL to IndexNow and request re-indexing in Search Console.

---

## 12. Safety guardrails (Tecorb conventions)

1. **Default to `draft`.** Direct `publish` mode requires explicit `--publish` flag from the calling user.
2. **Always check slug collisions** before creating a post.
3. **Always verify auth** with `/users/me` before any write.
4. **Never overwrite an existing post's content** without an explicit `--update {id}` flag.
5. **Log every API call's request/response status** to a local file in the draft directory for post-mortem.
6. **Dry-run mode** should be the default in CI: render the payload to a JSON file and skip the API call.
7. **Image filenames in WP Media Library are global.** Use slug-prefixed filenames (`blog-slug-featured.webp`) to avoid collisions across posts.

---

## 13. Quick-reference: minimum viable publish

The smallest correct invocation, end to end:

```python
# 1. Upload featured image
featured_id, _ = upload_media("featured.webp", alt_text="...")

# 2. Create draft post
r = requests.post(f"{WP_API_BASE}/posts", headers=HEADERS, json={
    "title": "Post Title",
    "slug": "post-slug",
    "content": "<p>Body HTML.</p>",
    "excerpt": "Short excerpt.",
    "status": "draft",
    "featured_media": featured_id,
    "categories": [get_or_create_category("ai-ml")],
    "tags": [get_or_create_tag("llm")],
    "meta": {
        "_yoast_wpseo_title": "SEO Title | Tecorb",
        "_yoast_wpseo_metadesc": "Meta description here.",
        "_yoast_wpseo_focuskw": "focus keyword",
    },
})
r.raise_for_status()
print(r.json()["link"])  # the new post's URL
```

If this works end-to-end, the rest is iteration.

---

## Reference workflow

1. Receive finalized markdown + metadata.json + images from `seo-blog-writing` output
2. Verify auth via `/users/me`
3. Upload featured image → record media ID
4. Upload inline images → build URL map
5. Convert markdown to Gutenberg HTML, rewriting image paths
6. Inject JSON-LD schema blocks into HTML body
7. Resolve category and tag IDs
8. POST to `/posts` with status=`draft` (default) or as specified
9. Return post ID + admin edit URL + preview URL to user
10. After human approval (separate command), transition status to `publish`
11. Ping IndexNow + submit to Google Search Console
12. Log result; mark draft as published locally

The output of this skill is the live (or scheduled) WordPress post URL and the admin edit URL for final QA.