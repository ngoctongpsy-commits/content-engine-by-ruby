---
description: First-time setup. Walk the user through filling brand.json + channels.json from templates (5 min).
---

# Setup Pipeline

First-time setup for the Content Engine. Turn the templates into a working config in a few
minutes, asking ONE focused question per step. The engine is brand-neutral; this command is
where the brand's identity, layout, and content model get chosen.

## Step 1 - Detect setup state

Find the plugin root (`.claude-plugin/plugin.json`). Then:
- `config/brand.json` exists -> setup done. Ask: regenerate, edit a section, or quit?
- `config/brand.template.json` exists but `config/brand.json` missing -> new-user setup.
- Neither -> abort: "plugin install looks incomplete".

## Step 2 - Brand identity

Ask ONE question at a time:
1. Company name + domain + one-line tagline
2. Author name for byline (default company name)
3. Primary brand color (hex) + background color (hex)
4. Font family preference (default Inter)
5. 3-5 forbidden phrases to flag (default keeps template list)

## Step 3 - Layout (format preset)  <-- this is what makes it fit any brand

Ask: "Which layout fits your brand?" and explain the presets (see
`skills/brand-locked-blog-writing/references/format-presets.md`):
- **editorial-dark** - dark hero, serif body, numbered sections, APA refs, data figures. B2B / thought leadership.
- **magazine-light** - photo hero, magazine body, no numbering, simple sources, decorative imagery. Lifestyle / restaurant / agency.
- **minimal-clean** - light hero, clean sans body, no numbering/refs/figures. Simple company blog (default).
- **custom** - set each field yourself.

Set `format.preset` accordingly. If they want tweaks (e.g. "magazine-light but keep figures off"), set the specific `format.blog.*` override.

## Step 3.5 - Images (thumbnail + social)

Ask: "How should blog thumbnails and LinkedIn/Facebook images be made?"
- **canva** - Claude generates clickbait images via the connected Canva connector at verified sizes (blog 1200x630, LinkedIn 1200x1200, Facebook 1080x1350). Requires the Canva connector. Set `format.images.provider` to `canva`.
- **svg** - built-in SVG figures (no external tool). Default.

In-article blog figures stay SVG either way. Confirm the Canva connector is connected if they pick canva.

## Step 4 - Content model

Ask:
1. 3-5 content pillars (their core topics) -> `content_model.pillars.list`
2. What each daily slot A/B/C should be (or accept the neutral Cornerstone/Practical/Timely defaults) -> `content_model.slots`
3. Monthly feature angles, if any (e.g. new_menu, customer_proof) -> `content_model.feature_rotation_angles.list` (empty is fine)
4. Stat rigor: strict / cited / off (default cited; use off for lifestyle brands)

## Step 4.5 - SEO + Google quality

Ask:
1. Region + language for SEO (e.g. US / en).
2. Author identity for E-E-A-T: real author name + credentials + organization + profile/About URL + social links (sameAs). This powers the JSON-LD author/publisher and Google's trust signals -> `seo.eeat`.
3. Canonical base URL + sitemap URL -> `seo.indexing`.
4. Quality gate: strict (block publish until E-E-A-T / indexability / human-voice / intent all pass) or advisory. Default strict for SEO-driven brands.

Goal: posts must actually get INDEXED by Google and rank, not just read well. See skills/seo-optimization/references/google-seo-standards.md.

## Step 5 - Channels

Ask:
1. How do you publish? directus / other CMS / "no CMS - I publish manually or via GitHub" (sets `cms.provider`, use "none" for the no-CMS case)
2. If a CMS: base URL
3. Social channels enabled (linkedin_company / facebook_page / linkedin_personal / x_twitter)
4. Telegram alerts on/off (default on)

Copy `config/brand.template.json` -> `config/brand.json` and `config/channels.template.json` -> `config/channels.json`, editing only what the user provided. Leave template defaults otherwise.

## Step 6 - Secret files (never stored in config)

For each enabled provider, tell the user exactly which gitignored file to create:
- CMS: `config/.cms-token` (single-line bearer token) - skip if provider is "none"
- Make.com webhook: `config/.make-webhook-url`
- Telegram: `config/.notify-config` (JSON `{"bot_token": "...", "chat_id": ...}`)

Confirm `.gitignore` already excludes these.

## Step 7 - Smoke test

Offer: `python scripts/publish-blog.py --slot A --dry-run` (validates configs, renders a thumbnail if figures enabled, posts nothing). Report errors plainly.

## Step 8 - Next steps

Point them to `/plan-month`, `/write-blog A`, `/post-weekly`.

## Rules

- One question per message. Do not batch.
- Never write secret tokens into `brand.json`/`channels.json`.
- If a config already exists, default to "edit a section" - do not overwrite.
- Never invent fields not in the template schema.
