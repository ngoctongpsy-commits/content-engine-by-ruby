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

Read `config/brand.json` for `voice.*`, `palette.*`, `format.social.*`, `content_model.*`, `validated_stats.*`.

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

### Step 4 - Generate posts

**LinkedIn** - voice from `voice.accounts.<voice.default_account>` (or `company`). 900-1400 chars. 3-5 hashtags at end. blog_driver: link in first comment. feature_promo: link in body.

**Facebook** - same active voice, lighter register. 300-600 chars. No hashtags. URL in body.

Adapt audience and register to the brand's tone string - do not assume "CTOs / VP Engineering" unless that is the brand's audience.

### Step 5 - Generate social card SVG

Size from `format.social.card_size_px` (default 1080) and `format.social.card_aspect` (default square). Use `palette.*` colors. Choose a pattern based on argument shape (Stat Bomb / Versus Split / Anti-Pattern / Tier Diagram / Question Hook / Timeline Marker). Self-validate against brand rules (no forbidden colors, no forbidden chars).

Apply footer branding per `format.social.card_branding`:
- `orb-wordmark`: orb + `company.domain` + `company.tagline`
- `wordmark`: `company.domain` only
- `logo`: brand logo if available, else wordmark
- `none`: no footer branding

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
  "image_pattern": "stat_bomb|versus_split|...",
  "clickbait_svg": "<full SVG XML>"
}
```

### Step 7 - Self-validate

Brand validators (forbidden phrases, forbidden colors). Numeric claims honor `content_model.stat_rigor`:
- `strict`/`cited`: for blog_driver every number in the card must appear in `blog_html`; for feature_promo every number must be in `validated_stats.entries`. If you cannot source a number, pick a pattern without numbers (Question Hook, Tier Diagram).
- `off`: no numeric enforcement.

Reject + regenerate on any failure.

## Anti-patterns

- Assuming B2B angles or a CTO audience - read them from config.
- Inventing stats when stat_rigor is strict/cited.
- Same pattern as last week's card.
- Mixing two account voices in one post.
- Forbidden chars (em/en dash, emoji) when `voice.forbidden_chars` enables them.
