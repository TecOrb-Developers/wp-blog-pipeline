---
name: image-prompts
description: Image selection workflow for Tecorb Technologies blog posts. The featured/hero image is pre-selected from a predefined local library — no AI image generation is used. Use this skill for every blog post image task — selecting the hero image, writing the manifest.json, preparing the file for upload, and setting alt text. Do not generate images with AI tools (DALL-E, Midjourney, Imagen, Stable Diffusion, FLUX, or any other provider) — all blog visuals come from the predefined library catalogued in the images_names skill.
---

# Image Selection — Tecorb Blog Visual System

Every Tecorb blog post uses one image selected from a predefined local library. No AI image generation is involved. This skill defines how to select the hero image, write the manifest, prepare the file for upload, and write alt text.

---

## 1. Image library and folder location

Images are stored in:

| Folder | Purpose | Dimensions |
|---|---|---|
| `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/` | Hero / featured image (WordPress featured image) | 1280 x 720 px |

The full catalog of available images — including titles, file names, and thematic descriptions — is in the `images_names` skill. Consult it before making any selection.

---

## 2. Per-blog image rule

Every blog post ships with exactly one image:

| Role | Source folder | Count | WordPress placement |
|---|---|---|---|
| **Featured / hero** | `AI_Blog_1280_720` | 1 | WordPress featured image field |

No in-body images. No diagrams. One hero image only.

---

## 3. Selection workflow

1. Read the completed blog draft and note:
   - Primary topic and technology focus
2. Open the `images_names` skill and consult the Summary Reference Table (Section 7) — filter by category and key technologies
3. For the top 1-2 candidates, read the **Image about** description to confirm thematic fit
4. Select 1 hero image whose topic matches the blog's primary subject
5. Verify the file exists at `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/<filename>`
6. Copy the file to `drafts/<slug>/images/<slug>-featured.png`
7. Write `images/manifest.json` (see Section 5)
8. Hand off to `wordpress-publishing` for upload

---

## 4. Selection criteria

- **Topic match** — Primary technology or subject area in the image description should align with the blog's focus
- **Category alignment** — If the blog covers a mobile topic, prefer images from the Mobile category; for AI posts, prefer AI & ML images

When the blog topic does not match any single image exactly, pick the closest thematic match. A DevOps post about monitoring fits Image 29 (Cloud Monitoring) even if it doesn't specifically cover every tool listed.

---

## 5. The manifest file

Each draft includes `images/manifest.json`. This is consumed by `wordpress-publishing` to set alt text during upload.

```json
{
  "featured": {
    "source_file": "1. Custom LLM & SLM Development_Hero_Page.png",
    "source_folder": "drafts/images_to_use/images/pre_images/AI_Blog_1280_720",
    "local_copy": "drafts/<slug>/images/<slug>-featured.png",
    "alt": "Cinematic illustration of a neural network being engineered inside a holographic workspace.",
    "caption": null,
    "role": "featured"
  }
}
```

Fields:
- `source_file` — exact filename as it appears in the source folder
- `source_folder` — path relative to project root
- `local_copy` — path to the copied file in the draft folder
- `alt` — descriptive alt text, 8-15 words, describes what is depicted
- `caption` — null for the featured image (captions are for in-body images)
- `role` — always `"featured"`

---

## 6. Alt text conventions

Alt text must describe what the image actually depicts, not what the blog post is about.

**Good:**
- "Isometric illustration of a CI/CD pipeline as an automated factory conveyor belt."
- "Split-screen showing native Android and iOS interfaces side by side with benchmark graphs."
- "Abstract 3D illustration of glowing data orbs being pulled toward a semantic search query."

**Bad:**
- "image", "featured image", "blog header"
- "LLM fine-tuning blog post image"
- "A cool AI illustration" (vague)

Rules:
- 8-15 words
- Describes the visual, not the concept it represents
- No emoji
- Include the primary keyword only if it appears naturally — do not force it

---

## 7. Filename convention for WordPress upload

When uploading to the WordPress Media Library, the file is renamed to kebab-case. The original library filename is preserved in the source folder; the draft copy uses the renamed version.

**Pattern:** `{post-slug}-featured.png`

| Role | Example upload filename |
|---|---|
| Featured | `llm-fine-tuning-guide-featured.png` |

This prevents filename collisions across posts in the WP Media Library.

---

## 8. Pre-upload checks

Before handing off to `wordpress-publishing`:

- [ ] File exists at the source path in `AI_Blog_1280_720/`
- [ ] Image number was looked up in the `images_names` catalog — correct thematic match confirmed
- [ ] File copied to `drafts/<slug>/images/<slug>-featured.png`
- [ ] Dimensions are 1280x720
- [ ] Alt text written, 8-15 words, describes the image specifically
- [ ] `manifest.json` written with all required fields

---

## Reference workflow

1. Read the blog draft — identify primary topic
2. Consult `images_names` skill — Summary Reference Table first, then Image about descriptions for candidates
3. Select 1 hero image (from `AI_Blog_1280_720/`)
4. Verify the file exists in the source folder
5. Copy to `drafts/<slug>/images/<slug>-featured.png`
6. Write alt text (8-15 words, describes the image)
7. Write `images/manifest.json` with the featured entry
8. Hand off to `wordpress-publishing`

The output of this skill: one image file ready for upload and a `manifest.json` describing it with alt text.
