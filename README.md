# WP Blog Pipeline

A [Claude Code](https://claude.ai/code)-native content pipeline that turns rough notes into SEO-optimized WordPress blog posts with a single command.

## What it does

Write rough notes in `blog_content.md`. Run `/blog`. The pipeline:

1. **Enriches content** — fixes weak introductions, adds missing H2 sections, writes a FAQ
2. **SEO pass** — extracts focus keyword, derives slug, writes meta description, assigns categories and tags, generates JSON-LD schema
3. **Selects hero image** — picks the best match from your image library
4. **Publishes to WordPress** — converts Markdown to Gutenberg blocks, uploads media, sets Yoast/RankMath meta fields, creates the post as a WP draft

Everything lands in `drafts/<slug>/` for review before going live.

## Prerequisites

- [Claude Code](https://claude.ai/code) (CLI or IDE extension)
- A self-hosted WordPress site with the REST API enabled (WordPress 5.0+)
- A WordPress Application Password for an Editor or Administrator user
- [Yoast SEO](https://yoast.com/wordpress/plugins/seo/) or [RankMath](https://rankmath.com/) installed on your WordPress site

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/wp-blogs.git
cd wp-blogs
```

### 2. Configure credentials

```bash
cp .env.example .env
```

Edit `.env`:

```env
WP_BASE_URL=https://your-site.com
WP_API_BASE=https://your-site.com/wp-json/wp/v2
WP_USER=your-editor-username
WP_APP_PASS=xxxx xxxx xxxx xxxx xxxx xxxx
WP_DEFAULT_AUTHOR_ID=1
```

**Generate a WordPress Application Password:**
1. Go to `wp-admin → Users → Profile`
2. Scroll to **Application Passwords**
3. Enter a name (e.g. `Claude Pipeline`) and click **Add New Application Password**
4. Copy the 24-character string (shown only once)

**Find your user ID:**
```bash
curl -s -u "your-username:your-app-password" \
  https://your-site.com/wp-json/wp/v2/users/me | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])"
```

### 3. Add your image library

The pipeline selects hero images from a local folder. Add your images (1280×720 PNG) to:

```
drafts/images_to_use/images/pre_images/AI_Blog_1280_720/
```

Then update `.claude/skills/images_names/SKILL.md` with your catalog — each image needs a title, filename, and description so the agent can select the right one. See the existing entries for the format.

### 4. Customize your style guide

Edit `.claude/skills/tecorb-style-guide/SKILL.md` to match your brand voice, audience personas, and formatting preferences. The included guide is a working example — replace the brand name and specifics with your own.

### 5. Open Claude Code

```bash
claude
```

## Usage

### Write a post

Create or edit `blog_content.md` at the project root. It can be bullet points, rough notes, or a full draft — the pipeline enriches whatever you give it:

```markdown
Title: My Post Title
Target Keyword: my focus keyword

Rough notes or full draft here...
- bullet points work fine
- or write full paragraphs
```

### Run the full pipeline

```
/blog
```

Creates a WordPress draft. You get back the admin edit URL and preview URL.

To publish immediately instead of drafting:

```
/blog --live
```

This requires a `yes` confirmation before going live.

### Publish an existing draft

```
/publish <slug>           # create WP draft
/publish <slug> --live    # publish live + ping IndexNow
```

### Command-line publishing (without Claude Code)

```bash
pip install requests

python publish_draft.py <slug>          # WP draft
python publish_draft.py <slug> --live   # publish live
```

## Pipeline architecture

```
blog_content.md
      │
      ▼
  seo-writer agent
  ├── Enriches content (intro, missing sections, FAQ)
  ├── SEO pass: focus keyword, slug, meta description, schema
  └── Output: drafts/<slug>/content.md + metadata.json
      │
      ▼
  Image selection
  ├── Reads images_names skill (your catalog)
  ├── Picks best-match hero image (1280×720)
  └── Output: drafts/<slug>/images/manifest.json + <slug>-featured.png
      │
      ▼
  wp-publisher agent
  ├── Verifies WP auth
  ├── Uploads featured image → WP Media Library
  ├── Converts Markdown → Gutenberg HTML blocks
  ├── Injects JSON-LD schema (BlogPosting + FAQPage)
  ├── Resolves/creates categories and tags
  ├── Creates WP post (draft or live)
  ├── Pings IndexNow (live mode only, if INDEXNOW_KEY is set)
  └── Output: drafts/<slug>/publish-log.json
```

## Draft folder structure

```
drafts/<slug>/
├── content.md          ← enriched blog body (Markdown)
├── metadata.json       ← SEO fields, categories, tags, schema
├── publish-log.json    ← post ID, URLs, warnings (written after publish)
└── images/
    ├── manifest.json   ← hero image metadata and alt text
    └── <slug>-featured.png
```

## Agents

Defined in `.claude/agents/`:

| Agent | Role |
|---|---|
| `seo-writer` | Content enrichment and SEO pass |
| `wp-publisher` | WordPress publishing via REST API |
| `style-matcher` | Scrapes your existing posts to calibrate the style guide |

## Skills

Defined in `.claude/skills/`:

| Skill | Role | Customize? |
|---|---|---|
| `seo-blog-writing` | Keyword strategy, E-E-A-T, GEO, featured snippets | No — generic SEO rules |
| `tecorb-style-guide` | Brand voice, heading cadence, CTA placement | **Yes** — replace with your brand |
| `wordpress-publishing` | WP REST API patterns, Gutenberg blocks, Yoast/RankMath | No — generic WP rules |
| `images_names` | Your image library catalog | **Yes** — add your images |
| `image-prompts` | Hero image selection workflow | No — generic workflow |

## WordPress setup notes

**Authentication**
- The WP user must be **Editor** or **Administrator**
- If you get 401/403 errors, regenerate the Application Password in WP admin

**SEO meta fields**
- Yoast SEO or RankMath must be installed for meta fields to persist via the REST API
- If SEO meta fields come back empty after post creation, see `wordpress-publishing/SKILL.md` Section 5 for the `register_post_meta()` fix

**Gutenberg**
- The pipeline requires Gutenberg (the WordPress block editor). It must not be disabled by a Classic Editor plugin.

## IndexNow (optional)

IndexNow notifies Bing and Yandex immediately when you publish. To enable:

1. Install the [IndexNow plugin](https://wordpress.org/plugins/indexnow/) in WP admin
2. Go to **Settings → IndexNow** — copy the key shown
3. Set `INDEXNOW_KEY=<your-key>` in `.env`

Every `/publish <slug> --live` run will ping `api.indexnow.org` automatically.

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `WP_BASE_URL` | Yes | Your WordPress site URL |
| `WP_API_BASE` | Yes | REST API base: `<WP_BASE_URL>/wp-json/wp/v2` |
| `WP_USER` | Yes | WordPress username |
| `WP_APP_PASS` | Yes | WordPress Application Password |
| `WP_DEFAULT_AUTHOR_ID` | Yes | Numeric author ID for published posts |
| `INDEXNOW_KEY` | No | Key for IndexNow search engine pings |
| `GSC_SERVICE_ACCOUNT_JSON` | No | Path to Google Search Console service account JSON |

## Contributing

Contributions welcome. Some ideas:
- Add support for RankMath meta fields alongside Yoast
- Add a `style-matcher` agent that calibrates to your existing posts
- Add diagram generation support
- Add scheduled publish (`--schedule=YYYY-MM-DDTHH:MM:SS`)

Open a pull request or file an issue.

## License

MIT — see [LICENSE](LICENSE).
