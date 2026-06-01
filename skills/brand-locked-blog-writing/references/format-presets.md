# Format Presets - Read from config/brand.json `format`

This file defines how a named `format.preset` expands into concrete layout decisions.
The blog and social skills read `format.preset`, expand it using the table below, then
apply any non-null override in `format.blog.*` / `format.social.*` on top.

**Golden rule:** a preset is just a set of defaults. An explicit (non-null) field in
`config/brand.json` ALWAYS wins. If `preset` is `custom`, ignore the table and use the
fields in `brand.json` directly (treat any null as the neutral fallback in the last column).

## Preset expansion table

| Field | editorial-dark | magazine-light | minimal-clean | neutral fallback (custom + null) |
|---|---|---|---|---|
| `blog.hero_style` | dark | image | light | light |
| `blog.body_style` | serif-editorial | magazine | sans-clean | sans-clean |
| `blog.heading_numbering` | true | false | false | false |
| `blog.references_style` | apa | simple | none | simple |
| `blog.cta.enabled` | true | true | true | true |
| `blog.figures.enabled` | true | true | false | false |
| `blog.figures.type` | svg-data | svg-decorative | none | none |
| `blog.figures.footer_branding` | orb-wordmark | wordmark | none | none |
| `social.card_branding` | orb-wordmark | wordmark | wordmark | wordmark |

`blog.figures.count_by_slot`: if null, derive from `content_model.slots` count (default A:3, B:2, C:1 for editorial-dark; A:1, B:1, C:0 for magazine-light; 0 for minimal-clean).

## Who each preset is for

**editorial-dark** - Thought-leadership and B2B. Dark hero band with light text, serif body for a "long read" feel, academically numbered sections, APA references, data-driven SVG figures with a branded orb + wordmark footer. This is the original Luna Base look. Pick it for SaaS, consulting, research, and analyst-style content.

**magazine-light** - Lifestyle, hospitality, retail, agency. Full-bleed photo hero with the title overlaid, large magazine lede, no section numbers, a simple "Sources" links list (or none), decorative (non-data) illustrations, light wordmark footer. Pick it for restaurants, hotels, fashion, food, travel, events.

**minimal-clean** - Simple company blogs, announcements, changelogs, docs-style posts. Light hero (or just an H1), clean sans body, no numbering, no reference section, no figures. Fastest to produce, reads like a modern product blog. Good default when in doubt.

**custom** - You set every `format.blog.*` field yourself. Any field left null uses the neutral fallback column above.

## How a skill applies this (pseudocode)

```
fmt = brand.format
preset = fmt.preset            # editorial-dark | magazine-light | minimal-clean | custom
resolved = {}
for each field F in [hero_style, body_style, heading_numbering, references_style,
                     figures.enabled, figures.type, figures.footer_branding,
                     social.card_branding, ...]:
    if fmt[F] is not null:
        resolved[F] = fmt[F]                 # explicit override wins
    elif preset != "custom":
        resolved[F] = PRESET_TABLE[preset][F]
    else:
        resolved[F] = NEUTRAL_FALLBACK[F]
```

Then build the HTML strictly from `resolved` plus `palette`, `typography`, `voice`,
and `content_model`. Never hardcode "dark hero" or "white body" - both are now just
two possible values of `resolved.hero_style` / `resolved.body_style`.

## Body style details

- **serif-editorial**: body in `typography.body_font` rendered as serif, generous line-height, drop or small-caps lede optional, max-width from `typography.body_max_width_px`. Headings in `typography.primary_font`.
- **sans-clean**: body and headings in sans (`typography.body_font` / `primary_font`), tighter line-height, product-blog feel. No drop cap.
- **magazine**: oversized opening lede paragraph, pull quotes allowed, image-led, mixed type sizes, editorial whitespace. Headings can be large and unnumbered.

## Hero style details

- **dark**: full-width band using `palette.background_dark`, H1 in `palette.text_on_dark`, accent in `palette.primary`.
- **light**: band using `palette.background_light` (or white), H1 in `palette.text_on_light`.
- **image**: full-bleed hero image (brand supplies the URL/asset) with a darkening overlay and H1 overlaid in `palette.text_on_dark`.
- **none**: no band at all, just the H1 at the top of the body column.
