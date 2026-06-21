#!/usr/bin/env python3
"""
publish_draft.py — CLI publisher for the WP Blog Pipeline.

Usage:
    python publish_draft.py <slug>          # create WP draft
    python publish_draft.py <slug> --live   # publish immediately + ping IndexNow

Reads:
    .env                                    (credentials)
    drafts/<slug>/content.md                (blog body in Markdown)
    drafts/<slug>/metadata.json             (SEO metadata)
    drafts/<slug>/images/manifest.json      (hero image info)

Writes:
    drafts/<slug>/publish-log.json          (post ID, URLs, warnings)

Requirements:
    pip install requests
"""

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
from datetime import datetime, timezone

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except ImportError:
    print("ERROR: 'requests' not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)

# ── CLI arguments ─────────────────────────────────────────────────────────────

parser = argparse.ArgumentParser(description="Publish a blog draft to WordPress.")
parser.add_argument("slug", help="Draft slug, e.g. my-post-title")
parser.add_argument("--live", action="store_true", help="Publish immediately (default: WP draft)")
args = parser.parse_args()

SLUG = args.slug
MODE = "publish" if args.live else "draft"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DRAFT_DIR = os.path.join(PROJECT_ROOT, "drafts", SLUG)

# ── Load .env ─────────────────────────────────────────────────────────────────

def load_env(path):
    env = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip('"').strip("'")
    except FileNotFoundError:
        print(f"ERROR: .env file not found at {path}", file=sys.stderr)
        print("Copy .env.example to .env and fill in your WordPress credentials.", file=sys.stderr)
        sys.exit(1)
    return env

env = load_env(os.path.join(PROJECT_ROOT, ".env"))

WP_API   = env.get("WP_API_BASE", "").rstrip("/")
WP_BASE  = env.get("WP_BASE_URL", "").rstrip("/")
WP_USER  = env.get("WP_USER", "")
WP_PASS  = env.get("WP_APP_PASS", "")
AUTHOR_ID = int(env.get("WP_DEFAULT_AUTHOR_ID", "1"))
INDEXNOW_KEY = env.get("INDEXNOW_KEY", "")

if not all([WP_API, WP_USER, WP_PASS]):
    print("ERROR: WP_API_BASE, WP_USER, and WP_APP_PASS must all be set in .env", file=sys.stderr)
    sys.exit(1)

AUTH_TOKEN = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH_TOKEN}", "User-Agent": "WPBlogPipeline/1.0"}

# ── HTTP session with retry ───────────────────────────────────────────────────

_session = requests.Session()
_retry = Retry(total=4, backoff_factor=1.5, status_forcelist=[429, 500, 502, 503, 504],
               allowed_methods=["GET", "POST"])
_session.mount("https://", HTTPAdapter(max_retries=_retry))
_session.mount("http://", HTTPAdapter(max_retries=_retry))
_session.verify = False
_session.headers.update(HEADERS)

def _req(method, url, **kwargs):
    kwargs["verify"] = False
    return getattr(_session, method)(url, **kwargs)

# ── Validate draft folder ─────────────────────────────────────────────────────

def require_file(path, label):
    if not os.path.exists(path):
        print(f"ERROR: Missing {label}: {path}", file=sys.stderr)
        sys.exit(1)

require_file(DRAFT_DIR, f"draft folder drafts/{SLUG}/")
require_file(os.path.join(DRAFT_DIR, "content.md"), "content.md")
require_file(os.path.join(DRAFT_DIR, "metadata.json"), "metadata.json")
require_file(os.path.join(DRAFT_DIR, "images", "manifest.json"), "images/manifest.json")

warnings = []
media_ids = {}

# ── Step 1: Load inputs ───────────────────────────────────────────────────────

print(f"\n=== Publishing draft: {SLUG} (mode={MODE}) ===\n")
print("Step 1: Loading inputs ...", flush=True)

with open(os.path.join(DRAFT_DIR, "metadata.json")) as f:
    metadata = json.load(f)
with open(os.path.join(DRAFT_DIR, "images", "manifest.json")) as f:
    img_manifest = json.load(f)
with open(os.path.join(DRAFT_DIR, "content.md")) as f:
    content_md = f.read()

print("  OK", flush=True)

# ── Step 2: Verify WP auth ────────────────────────────────────────────────────

print("Step 2: Verifying WordPress credentials ...", flush=True)
r = _req("get", f"{WP_API}/users/me", params={"context": "edit"})
if r.status_code in (401, 403):
    print(f"ERROR: Auth failed ({r.status_code}). Rotate your Application Password in WP admin.", file=sys.stderr)
    sys.exit(1)
r.raise_for_status()
user = r.json()
print(f"  Authenticated as: {user.get('name')} (ID {user.get('id')})", flush=True)

# ── Step 3: Check for slug collision ─────────────────────────────────────────

print("Step 3: Checking for slug collision ...", flush=True)
r = _req("get", f"{WP_API}/posts", params={"slug": metadata["slug"], "status": "any"})
hits = r.json() if r.ok else []
if hits:
    print(f"  WARNING: Post with slug '{metadata['slug']}' already exists (ID {hits[0]['id']}). "
          "Proceeding — this will create a second post.", flush=True)
    warnings.append(f"Slug collision: '{metadata['slug']}' already exists as post {hits[0]['id']}")
else:
    print("  No collision.", flush=True)

# ── Step 4: Upload featured image ─────────────────────────────────────────────

print("Step 4: Uploading featured image ...", flush=True)
feat = img_manifest["featured"]
img_local_path = os.path.join(PROJECT_ROOT, feat["local_copy"])

if not os.path.exists(img_local_path):
    print(f"ERROR: Featured image not found: {img_local_path}", file=sys.stderr)
    sys.exit(1)

filename = os.path.basename(img_local_path)
mime, _ = mimetypes.guess_type(filename)
mime = mime or "image/png"

with open(img_local_path, "rb") as f:
    img_data = f.read()

upload_headers = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "User-Agent": "WPBlogPipeline/1.0",
    "Content-Disposition": f'attachment; filename="{filename}"',
    "Content-Type": mime,
}
r = _session.post(f"{WP_API}/media", headers=upload_headers, data=img_data, verify=False)
if not r.ok:
    print(f"ERROR: Image upload failed [{r.status_code}]: {r.text[:400]}", file=sys.stderr)
    sys.exit(1)

media_obj = r.json()
featured_id = media_obj["id"]
featured_url = media_obj["source_url"]
media_ids["featured"] = featured_id
print(f"  Uploaded -> media ID {featured_id}: {featured_url}", flush=True)

# Set alt text
_req("post", f"{WP_API}/media/{featured_id}", json={"alt_text": feat.get("alt", ""), "caption": ""})

# ── Step 5: Markdown → Gutenberg HTML ────────────────────────────────────────

print("Step 5: Converting Markdown to Gutenberg blocks ...", flush=True)

def process_inline(text):
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def convert_blockquote_inner(text):
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^[-*]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^[-*]\s+', lines[i]):
                items.append(f'<li>{process_inline(re.sub(r"^[-*]\s+", "", lines[i]))}</li>')
                i += 1
            result.append(f'<ul>{"".join(items)}</ul>')
        elif line.strip():
            result.append(f'<p>{process_inline(line)}</p>')
            i += 1
        else:
            i += 1
    return "\n".join(result)

def convert_md_to_gutenberg(md_text):
    blocks = []
    lines = md_text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # Horizontal rule
        if re.match(r'^---+$', line.strip()):
            blocks.append('<!-- wp:separator -->\n<hr class="wp-block-separator has-alpha-channel-opacity"/>\n<!-- /wp:separator -->')
            i += 1
            continue

        # ATX headings
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            text = process_inline(m.group(2))
            blocks.append(
                f'<!-- wp:heading {{"level":{level}}} -->\n'
                f'<h{level} class="wp-block-heading">{text}</h{level}>\n'
                f'<!-- /wp:heading -->'
            )
            i += 1
            continue

        # Blockquote / callout boxes
        if line.startswith("> ") or line.strip() == ">":
            bq_lines = []
            while i < len(lines) and (lines[i].startswith("> ") or lines[i].strip() == ">"):
                bq_lines.append(lines[i][2:] if lines[i].startswith("> ") else "")
                i += 1
            bq_text = "\n".join(bq_lines).strip()
            first_line = bq_text.split("\n")[0].strip() if bq_text else ""
            css_class = "wp-callout"
            if "Watch out" in first_line:
                css_class += " wp-callout-warning"
            elif "Insight" in first_line:
                css_class += " wp-callout-insight"
            elif "Pro tip" in first_line:
                css_class += " wp-callout-pro-tip"
            inner_html = convert_blockquote_inner(bq_text)
            blocks.append(
                f'<!-- wp:group {{"className":"{css_class}"}} -->\n'
                f'<div class="wp-block-group {css_class}">\n{inner_html}\n</div>\n'
                f'<!-- /wp:group -->'
            )
            continue

        # Markdown table
        if "|" in line and i + 1 < len(lines) and re.match(r'^\|[\s\-|]+\|$', lines[i + 1].strip()):
            table_lines = []
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            header_cols = [c.strip() for c in table_lines[0].strip().strip("|").split("|")]
            data_rows = table_lines[2:]
            thead = "<thead><tr>" + "".join(f"<th>{process_inline(c)}</th>" for c in header_cols) + "</tr></thead>"
            tbody_rows = ""
            for dr in data_rows:
                cols = [c.strip() for c in dr.strip().strip("|").split("|")]
                tbody_rows += "<tr>" + "".join(f"<td>{process_inline(c)}</td>" for c in cols) + "</tr>"
            blocks.append(
                f'<!-- wp:table {{"hasFixedLayout":false}} -->\n'
                f'<figure class="wp-block-table"><table>'
                f'<thead>{thead}</thead><tbody>{tbody_rows}</tbody>'
                f'</table></figure>\n'
                f'<!-- /wp:table -->'
            )
            continue

        # Ordered list
        if re.match(r'^\d+\.\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i]):
                item_text = re.sub(r'^\d+\.\s+', '', lines[i])
                items.append(f'<li>{process_inline(item_text)}</li>')
                i += 1
            blocks.append(
                f'<!-- wp:list {{"ordered":true}} -->\n'
                f'<ol class="wp-block-list">{"".join(items)}</ol>\n'
                f'<!-- /wp:list -->'
            )
            continue

        # Unordered list
        if re.match(r'^[-*]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^[-*]\s+', lines[i]):
                items.append(f'<li>{process_inline(re.sub(r"^[-*]\s+", "", lines[i]))}</li>')
                i += 1
            blocks.append(
                f'<!-- wp:list -->\n'
                f'<ul class="wp-block-list">{"".join(items)}</ul>\n'
                f'<!-- /wp:list -->'
            )
            continue

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Regular paragraph
        para_lines = []
        while i < len(lines) and lines[i].strip() \
                and not lines[i].startswith("#") \
                and not lines[i].startswith(">") \
                and not re.match(r'^---+$', lines[i].strip()) \
                and not re.match(r'^[-*]\s+', lines[i]) \
                and not re.match(r'^\d+\.\s+', lines[i]) \
                and "|" not in lines[i]:
            para_lines.append(lines[i])
            i += 1
        if para_lines:
            blocks.append(
                f'<!-- wp:paragraph -->\n'
                f'<p>{process_inline(" ".join(para_lines))}</p>\n'
                f'<!-- /wp:paragraph -->'
            )
        else:
            i += 1

    return "\n\n".join(blocks)

gutenberg_html = convert_md_to_gutenberg(content_md)

# Inject JSON-LD schema blocks
for schema in metadata.get("schema_blocks", []):
    schema_json = json.dumps(schema, indent=2, ensure_ascii=False)
    gutenberg_html += (
        f'\n<!-- wp:html -->\n'
        f'<script type="application/ld+json">\n{schema_json}\n</script>\n'
        f'<!-- /wp:html -->'
    )

print(f"  Generated {len(gutenberg_html)} chars across Gutenberg blocks.", flush=True)

# ── Step 6: Resolve categories and tags ──────────────────────────────────────

print("Step 6: Resolving categories and tags ...", flush=True)

def get_or_create_term(taxonomy, slug):
    r = _req("get", f"{WP_API}/{taxonomy}", params={"slug": slug})
    hits = r.json() if r.ok else []
    if hits:
        return hits[0]["id"]
    display = slug.replace("-", " ").title()
    r2 = _req("post", f"{WP_API}/{taxonomy}", json={"slug": slug, "name": display})
    if not r2.ok:
        raise RuntimeError(f"Failed to create {taxonomy} '{slug}': {r2.text[:300]}")
    return r2.json()["id"]

cat_ids = [get_or_create_term("categories", s) for s in metadata.get("category_slugs", [])]
tag_ids = [get_or_create_term("tags", s) for s in metadata.get("tag_slugs", [])]
print(f"  Categories: {cat_ids}  Tags: {tag_ids}", flush=True)

# ── Step 7: Create WP post ────────────────────────────────────────────────────

print(f"Step 7: Creating post (status={MODE}) ...", flush=True)

payload = {
    "title":          metadata["title"],
    "slug":           metadata["slug"],
    "content":        gutenberg_html,
    "excerpt":        metadata.get("excerpt", ""),
    "status":         MODE,
    "author":         AUTHOR_ID,
    "featured_media": featured_id,
    "categories":     cat_ids,
    "tags":           tag_ids,
    "comment_status": "closed",
    "ping_status":    "closed",
    "meta": {
        "_yoast_wpseo_title":    metadata.get("seo_title", ""),
        "_yoast_wpseo_metadesc": metadata.get("meta_description", ""),
        "_yoast_wpseo_focuskw":  metadata.get("focus_keyword", ""),
    },
}

r = _req("post", f"{WP_API}/posts", json=payload)
if not r.ok:
    print(f"ERROR: POST /posts failed [{r.status_code}]: {r.text[:600]}", file=sys.stderr)
    sys.exit(1)

post = r.json()
post_id   = post["id"]
post_url  = post.get("link", f"{WP_BASE}/?p={post_id}")
admin_url = f"{WP_BASE}/wp-admin/post.php?post={post_id}&action=edit"
print(f"  Post created! ID: {post_id}", flush=True)

# ── Step 8: IndexNow (live only) ─────────────────────────────────────────────

indexnow_submitted = False
if MODE == "publish" and INDEXNOW_KEY:
    print("Step 8: Submitting to IndexNow ...", flush=True)
    r_ix = requests.post(
        "https://api.indexnow.org/indexnow",
        json={
            "host": WP_BASE.replace("https://", "").replace("http://", ""),
            "key": INDEXNOW_KEY,
            "keyLocation": f"{WP_BASE}/{INDEXNOW_KEY}.txt",
            "urlList": [post_url],
        },
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=15,
    )
    if r_ix.status_code in (200, 202):
        indexnow_submitted = True
        print(f"  IndexNow accepted (HTTP {r_ix.status_code}).", flush=True)
    else:
        warnings.append(f"IndexNow ping returned HTTP {r_ix.status_code}")
        print(f"  IndexNow warning: HTTP {r_ix.status_code}", flush=True)

# ── Step 9: Write publish-log.json ────────────────────────────────────────────

log = {
    "run_at":              datetime.now(timezone.utc).isoformat(),
    "mode":                MODE,
    "post_id":             post_id,
    "post_url":            post_url,
    "admin_edit_url":      admin_url,
    "media_ids":           media_ids,
    "indexnow_submitted":  indexnow_submitted,
    "warnings":            warnings,
}
log_path = os.path.join(DRAFT_DIR, "publish-log.json")
with open(log_path, "w") as f:
    json.dump(log, f, indent=2)

# ── Final report ──────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
print(f"Post ID:         {post_id}")
print(f"Status:          {MODE}")
print(f"Admin edit URL:  {admin_url}")
if MODE == "publish":
    print(f"Public URL:      {post_url}")
else:
    print(f"Preview URL:     {post_url}")
print(f"IndexNow pinged: {indexnow_submitted}")
if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")
print("=" * 60)
