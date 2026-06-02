# Content Engine by Ruby

A brand-locked content automation plugin for Claude. Plan a 30-day calendar, draft long-form blog articles, generate matching LinkedIn and Facebook social posts, validate everything against your brand rules, and auto-publish to your CMS. Every output reads brand identity from a single `config/brand.json` file, so the same skills work for any company.

**Built by Ruby.**

---

## What you get

- **3 skills** that drive the full content workflow:
  - `brand-locked-blog-writing` - drafts a full HTML blog whose layout (hero style, body style, heading numbering, references, figures) is chosen by a `format` preset, against your palette + voice rules. Dark hero + APA is just one preset (`editorial-dark`); a restaurant can use `magazine-light` and a simple blog `minimal-clean`.
  - `content-planning` - generates or updates a 30-day calendar with 3 slots per day across your pillars
  - `weekly-social-packet` - generates one LinkedIn + one Facebook + one clickbait SVG per week, with stat-trace validation
- **4 slash commands** for one-tap workflows:
  - `/setup-pipeline` - 5-minute onboarding from templates
  - `/plan-month` - regenerate or extend the calendar
  - `/write-blog A` (or B / C) - draft today's blog
  - `/post-weekly` - generate this week's social packet
- **2 generic scripts** that the pipeline calls:
  - `scripts/publish-blog.py` - validate, render best figure as thumbnail, POST to CMS
  - `scripts/post-weekly-social.py` - render clickbait SVG, fire Make.com webhooks, verify, alert
- **2 working examples** showing how different the same engine looks per brand:
  - `examples/luna-base/` - B2B tenant on the `editorial-dark` preset (Electric Mint `#00FFA3` + Deep Navy `#0A0E27` + Inter), real calendar + sample blog HTML + LinkedIn post.
  - `examples/restaurant/` - a restaurant on the `magazine-light` preset, proving the engine is not locked to LunaBase's look.

Everything is **brand-neutral by construction**. The skills and scripts contain no hardcoded brand AND no hardcoded layout. Every color, font, voice rule, forbidden phrase, validated stat, channel destination, AND the entire visual layout (`format`) + editorial model (`content_model`) read from `config/brand.json` + `config/channels.json`. Switching brands means swapping config, never editing a skill.

---

## Quick Start (5 minutes)

### 1. Install the plugin

Install from a Claude Plugin marketplace, or clone this repo into your project workspace.

### 2. Run `/setup-pipeline`

Inside Claude, type `/setup-pipeline`. It walks you through filling `config/brand.json` and `config/channels.json` from templates, one question at a time. You will be asked:

- Company name, domain, tagline
- Author byline name
- Primary brand color hex + background color hex
- Font family
- 3-5 forbidden phrases to flag
- CMS provider (or "skip CMS for now")
- Social channels you want enabled
- Telegram alerts on/off

This takes about 4 minutes. The setup command never asks for tokens; you create those manually in the next step.

### 3. Drop in your secrets

Create these files manually (the templates and `.gitignore` already exclude them from version control):

| File | What goes in it |
|---|---|
| `config/.cms-token` | Single-line bearer token for your CMS |
| `config/.make-webhook-url` | Single-line Make.com webhook URL (only if you use Make) |
| `config/.notify-config` | JSON: `{"bot_token": "...", "chat_id": ...}` for Telegram |

If you do not use one of these channels, skip its secret file - the script reads the `enabled` flag in `channels.json` and skips disabled channels.

### 4. Try it

```
/plan-month                          # generate next month's calendar
/write-blog A                        # draft Slot A blog for today
python scripts/publish-blog.py --slot A --dry-run    # validate, render thumbnail, do not post
```

You can also run `/post-weekly` to generate one week's social content packet.

### 5. Schedule it (optional)

To run the full pipeline automatically, install the Windows Task Scheduler tasks (or your OS equivalent) using the cron schedules already in `channels.json`:

- Daily 02:02 - generate next-day drafts
- Daily 09:30 / 13:30 / 17:30 IST - publish Slot A / B / C
- Monday 21:00 - generate weekly social packet
- Tuesday 11:30 - fire weekly social to LinkedIn and Facebook

---

## Folder structure

```
content-engine-by-ruby/
├── .claude-plugin/plugin.json      Plugin manifest
├── .mcp.json                       Optional MCP server hints
├── .gitignore                      Excludes secrets + per-tenant config
├── LICENSE                         MIT
├── README.md                       This file
├── config/                         YOUR live config (gitignored)
│   ├── brand.template.json         Copy to brand.json and edit
│   ├── channels.template.json      Copy to channels.json and edit
│   └── content-calendar.template.md   Copy to content-calendar.md and edit
├── commands/                       Slash commands
│   ├── setup-pipeline.md
│   ├── plan-month.md
│   ├── write-blog.md
│   └── post-weekly.md
├── skills/                         Brand-locked skills
│   ├── brand-locked-blog-writing/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── svg-patterns.md
│   │       ├── format-presets.md
│   │       └── brand-voice-rules.md
│   ├── content-planning/SKILL.md
│   └── weekly-social-packet/SKILL.md
├── scripts/                        Generic config-driven runtime
│   ├── publish-blog.py
│   └── post-weekly-social.py
└── examples/
    ├── luna-base/                  B2B tenant - editorial-dark preset
    │   ├── config/
    │   │   ├── brand.json
    │   │   ├── channels.json
    │   │   └── content-calendar.md
    │   ├── sample-output/
    │   │   ├── blog-post.html
    │   │   └── linkedin-post.md
    │   └── README.md
    └── restaurant/                 Lifestyle tenant - magazine-light preset
        └── config/
            └── brand.json
```

---

## Brand rules the skills enforce

Everything below reads from `config/brand.json`. You change the rules by editing the config, never by editing the skills.

- **Palette**: only colors in `palette.*` may appear in HTML or SVG. `palette._forbidden_colors.hex` lists Tailwind defaults that the validator hard-rejects.
- **Typography**: `typography.primary_font` for headings, `typography.body_font` for article body, `typography.body_max_width_px` for max article width.
- **Layout (`format`)**: a `preset` (editorial-dark / magazine-light / minimal-clean / custom) plus per-field overrides choose hero style, body style, heading numbering, reference style, whether figures exist, and footer branding. This is what makes one engine fit many industries. See `skills/brand-locked-blog-writing/references/format-presets.md`.
- **Content model (`content_model`)**: per-brand slot meanings, pillars, monthly feature angles, and stat rigor. No B2B framing is assumed.
- **SEO (`seo` + `seo-optimization` skill)**: keyword + search-intent research and a Google quality gate (E-E-A-T with real author in JSON-LD, Helpful Content / people-first, human-voice, indexability: title/meta/canonical/structured data/internal links) so AI posts get indexed and rank. `seo.quality_gate` strict blocks publish until all checks pass.
- **Images (`format.images`)**: `provider` chooses where the thumbnail + social images come from - `canva` (Claude writes a clickbait prompt per piece and generates the image via the Canva connector at verified 2026 sizes: blog 1200x630, LinkedIn 1200x1200, Facebook 1080x1350) or `svg` (built-in figures). In-article blog figures stay SVG regardless.
- **Voice**: one or more accounts under `voice.accounts` (the template ships an example `personal`/`company`/`newsletter` set), each with pronoun, tone, and product-promotion permission. `voice.default_account` picks the active one. Rename or reduce them to fit your brand.
- **Forbidden phrases**: `voice.forbidden_phrases.ai_tells`, `overclaims`, `generic_openers` are removed before publish. Validator rejects post text containing them.
- **Approved phrasings**: `voice.required_phrasings.approved_only_phrasings` lists exact phrases that look like overclaims but are explicitly approved for your brand.
- **Forbidden chars**: em dash, en dash, emoji all toggleable.
- **Validated stats**: `validated_stats.entries` lists pre-approved numeric claims with citations. The weekly-social skill's stat-trace validator requires every number in the clickbait SVG to trace either to this table (feature_promo posts) or to the blog body (blog_driver posts). This is the single most-important defense against AI hallucination.

---

## How the pipeline runs in production

```
[Cowork / Claude session]                 generation tier
  daily scheduled task at 02:02
  -> brand-locked-blog-writing skill
  -> drafts 3 next-day blog HTML to outputs/blogs/

[Host machine - Windows Task Scheduler]   publish tier
  daily 09:30 / 13:30 / 17:30 IST
  -> scripts/publish-blog.py --slot {A|B|C}
  -> validate, render thumbnail, POST to CMS, Telegram alert

[Cowork - weekly]
  Mon 21:00
  -> weekly-social-packet skill
  -> JSON packet to outputs/social/pending/

[Host machine - Windows Task Scheduler]
  Tue 11:30 IST (LinkedIn India peak)
  -> scripts/post-weekly-social.py
  -> render PNG, upload to CMS, fire Make.com webhooks
  -> Make.com routes to LinkedIn and Facebook
  -> verify via Make API (Fix 1)
  -> Telegram alert
```

You can swap any tier. The skills do not care which orchestrator triggers them, and the scripts do not care which CMS or webhook router sits downstream as long as the `provider` keys in `channels.json` map to a supported implementation.

---

## Extending

- **No CMS?** Set `cms.provider` to `none`. `publish-blog.py` validates + inlines the HTML and writes it to `outputs/blogs/ready/` for you to commit to GitHub or upload manually. Nothing is posted.
- **Add a CMS provider**: edit `scripts/publish-blog.py` `upload_thumbnail()` and `post_blog()` to branch on `cms.provider`. Wordpress and Ghost are good first additions.
- **Add a social channel**: add a key under `social.channels.*` in `channels.json` with `"enabled": true`. The post-weekly-social script will include it in the webhook payload; the rest is Make.com routing.
- **Add a skill**: drop a new folder under `skills/` with a `SKILL.md`. Frontmatter triggers do the rest. Consider following the same "read brand.json first" pattern so your skill stays generic.
- **Change SVG patterns**: edit `skills/brand-locked-blog-writing/references/svg-patterns.md`. There are 12 patterns documented with composition specs and a STEP 0 selection algorithm.

---

## License

MIT. Copyright (c) 2026 Ruby.

---

## Credits

Built by Ruby. The Luna Base example is the live production tenant - thanks to Andy Pham (founder, Luna Base) for letting the real configuration ship as marketplace reference material.
