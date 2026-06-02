---
name: weekly-social-packet
description: Generate a weekly social packet (1 LinkedIn post + 1 Facebook post + 1 social card SVG) reading brand identity, voice, format and content_model from config/brand.json and destinations from config/channels.json. Two post types on rotation: blog_driver (drives traffic to a published post) and feature_promo (uses the brand's own feature angles, last Monday of month). Triggered weekly by a scheduled task, or on demand when the user asks "generate this week's social post". Brand-neutral: card branding and promo angles come from config, never hardcoded.
---

# Weekly Social Packet Generation

Brand-neutral. Card branding, voice, and promo angles all come from config. No industry
or house style is assumed.

## When to use

- Scheduled (recommended): weekly per `channels.json` `schedule.weekly_social_generation`
- On demand: "generate this week's social post" / "make next week's LinkedIn"

## Workflow

### Step 1 - Read configs

Read `config/brand.json` for `voice.*`, `palette.*`, `format.social.*`, `format.images.*`, `content_model.*`, `validated_stats.*`.

Read `config/channels.json` for enabled `social.channels.*` destinations and `social.make_webhook_url_file`.

Read `config/content-calendar.md` feature rotation table (if present).

### Step 2 - Determine post type

```
today = current date
next_monday = today + 7 days
if next_monday.month != today.month AND content_model.feature_rotation_angles.list is non-empty:
    post_type = "feature_promo"     # last Monday of month
else:
    post_type = "blog_driver"
```

### Step 3a - blog_driver

Pick the highest-scoring post from the last 7 days (`outputs/blogs/`). Read it. Identify the sharpest claim (must be in the post body), its source, the thesis, and the argument shape (drives card pattern selection).

### Step 3b - feature_promo

Read the current month's row in the content-calendar feature rotation table. Extract `angle` + `specific` (these are the brand's OWN angles from `content_model.feature_rotation_angles.list`). Build the message around that angle and link to the relevant page. Do not assume B2B angles - use whatever the brand defined (e.g. new_menu, chef_story for a restaurant; product_spotlight, customer_proof for SaaS).

### Step 4 - Generate posts (per ENABLED platform, native format)

Write a separate post for EACH enabled channel in `channels.json` `social.channels`, in the brand voice (`voice.accounts.<voice.default_account>`). Each platform has its own native format:

- **LinkedIn** - professional. 900-1400 chars. 3-5 hashtags at end. blog_driver: link in first comment; feature_promo: link in body.
- **Facebook** - friendly, lighter. 300-600 chars. No hashtags. URL in body.
- **Instagram** - visual-first caption, punchy first line, 1-2 short paras, 5-10 hashtags, "link in bio" (IG kills in-caption links). Needs an image/video.
- **Threads** - conversational, short (<=500 chars), 1-2 lines, minimal/no hashtags, can be a hot take or question.
- **X / Twitter** - tight (<=280 chars), one sharp hook, 1-2 hashtags max, link allowed.
- **TikTok / YouTube (Shorts)** - these are VIDEO posts: a short caption/title + 3-5 tags; the clip comes from the `video-production` skill. YouTube also gets a title (<=60 chars) + description.
- **Pinterest** - a keyword-rich title + 1-2 sentence description; pin = image + link.

Adapt audience/register to the brand's tone - do not assume any specific audience. Keep numbers truthful (honor `content_model.stat_rigor`). Only write posts for channels that are `enabled`.

### Step 5 - Generate the social image (provider-aware)

Resolve `format.images.provider`:

**`canva` (clickbait images, recommended):** generate TWO clickbait images with the connected Canva tools - one for LinkedIn, one for Facebook - sized per `format.images.sizes` (LinkedIn `linkedin_px` default 1200x1200; Facebook `facebook_px` default 1080x1350). Read `references/canva-images.md` for the prompt recipe and steps. In short: compose a fresh clickbait prompt from this week's angle (the blog's sharpest claim for blog_driver, or the feature angle for feature_promo), generate + resize to the exact size, export PNG, and save:
- `outputs/social/pending/weekly-YYYY-MM-DD.linkedin.png`
- `outputs/social/pending/weekly-YYYY-MM-DD.facebook.png`

The two can share the same concept/headline, just re-laid-out for each aspect ratio. The post script auto-detects these PNGs and posts them (one per channel), falling back to SVG only if missing.

**`svg` (legacy):** generate one social card SVG. Size from `format.social.card_size_px` (default 1080) and `format.social.card_aspect`. Use `palette.*` colors and a pattern (Stat Bomb / Versus Split / Anti-Pattern / Tier Diagram / Question Hook / Timeline Marker). Apply footer branding per `format.social.card_branding` (`orb-wordmark` | `wordmark` | `logo` | `none`).

### Step 6 - Output JSON

Write packet to `outputs/social/pending/weekly-YYYY-MM-DD.json`:

```json
{
  "post_type": "blog_driver | feature_promo",
  "feature_angle": "...",
  "feature_specific": "...",
  "blog_slug": "...",
  "blog_title": "...",
  "blog_url": "...",
  "blog_description": "...",
  "blog_html": "<first 3000 chars>",
  "hero_stat": "...",
  "hero_source": "...",
  "linkedin_post": "...",
  "facebook_post": "...",
  "image_alt": "...",
  "image_title": "...",
  "image_provider": "canva | svg",
  "image_linkedin_path": "outputs/social/pending/weekly-YYYY-MM-DD.linkedin.png",
  "image_facebook_path": "outputs/social/pending/weekly-YYYY-MM-DD.facebook.png",
  "image_pattern": "stat_bomb|versus_split|...  (svg provider only)",
  "clickbait_svg": "<full SVG XML>  (svg provider only; omit for canva)"
}
```

### Step 7 - Self-validate

Brand validators (forbidden phrases, forbidden colors). Numeric claims honor `content_model.stat_rigor`:
- `strict`/`cited`: any number shown in the image must be real - for blog_driver it must appear in `blog_html`; for feature_promo in `validated_stats.entries`. If you cannot source a number, use a curiosity/headline angle with no number.
- `off`: no numeric enforcement.

If provider is `canva`: confirm both PNGs exist at the configured sizes, headline <= 8 words, no fabricated stats, no emoji (if forbidden). If provider is `svg`: validate the SVG as before.

Reject + regenerate on any failure.

## Anti-patterns

- Assuming B2B angles or a CTO audience - read them from config.
- Inventing stats when stat_rigor is strict/cited.
- Same concept/headline as last week's image.
- Mixing two account voices in one post.
- Forbidden chars (em/en dash, emoji) when `voice.forbidden_chars` enables them.
