---
name: brand-locked-blog-writing
description: Generate fully brand-compliant HTML blog articles whose layout, voice, colors, fonts and structure all come from config/brand.json. Triggered whenever the user asks to write a blog post, article, or long-form content. Self-contained and brand-neutral - no company, layout, color, or font is hardcoded. The visual format (hero style, body style, numbering, references, figures) is chosen by format.preset / format.blog.* so the same skill works for a B2B SaaS, a restaurant, an agency, or a law firm.
---

# Brand-Locked Blog Writing

This skill is a brand-NEUTRAL engine. It contains no house style of its own. Every
structural and visual decision is read from `config/brand.json`. Do not assume a dark
hero, a serif body, numbered headings, APA references, or SVG figures - all of those are
configurable and may be off for the active brand.

## When to use

Whenever the user asks for: blog post, article, long-form content, blog draft, SEO content piece, thought leadership article, or any content destined for a blog or website.

## Workflow (READ THIS FIRST)

### Step 1 - Read brand config

Before writing ANY content, read `config/brand.json` (or `examples/<brand>/config/brand.json` if working with a specific brand example). Single source of truth for:

- `company.*` - name, domain, tagline, url
- `palette.*` - every hex color you may use; `palette._forbidden_colors.*` - colors that MUST NOT appear (hard reject)
- `typography.*` - fonts + sizing
- `format.*` - THE LAYOUT. preset + per-field overrides for hero, body, numbering, references, figures, footer, SEO, social card. See Step 2.
- `format.images.*` - where the THUMBNAIL comes from: provider `canva` (clickbait image via Canva) or `svg` (legacy). See Step 8.5.
- `seo.*` - region, language, E-E-A-T identity (author + credentials, organization, sameAs), indexing settings, and `quality_gate`. Drives the Google quality gate in Step 7.6 and the byline/JSON-LD.
- `content_model.*` - slots (label/intent/word counts), pillars, feature angles, stat_rigor
- `voice.*` - account voices (`voice.default_account` picks the active one), forbidden phrases/chars
- `svg_figure.*` - figure viewBox + zones (only if figures enabled)
- `validated_stats.entries` - pre-approved stats (used when stat_rigor is strict)
- `core_arguments.list` - optional thesis statements (may be empty)

### Step 2 - Resolve the format (CRITICAL - this replaces all old house style)

Read `references/format-presets.md`. Resolve the active layout:

1. Read `format.preset` (editorial-dark | magazine-light | minimal-clean | custom).
2. For each layout field, if `format.blog.<field>` is non-null use it; else take it from the preset table; else (custom + null) use the neutral fallback.

You end up with resolved values for: `hero_style`, `body_style`, `heading_numbering`,
`references_style`, `cta.enabled`, `figures.enabled`, `figures.type`,
`figures.count_by_slot`, `figures.footer_branding`, `seo.*`.

Everything you build in Step 5 MUST follow these resolved values. There is no default
"dark hero / white serif body" anymore - that is simply what `editorial-dark` resolves to.

### Step 3 - Read content calendar + slot

Read `config/content-calendar.md` to find today's topic by date + slot label (A/B/C) + pillar. If no calendar exists, ask the user for the topic.

If a competitor/trend brief exists for this topic (from the `competitor-trend-research` skill), use its angle, outline, keywords, and "original value to add" so the piece matches intent and beats the current SERP (never a copy).

Pull slot length + intent from `content_model.slots.<A|B|C>`:
- `label`, `intent` - what this slot is for (brand-defined, NOT assumed to be foundational/comparison/news)
- `word_count_min` / `word_count_max` - target length

### Step 4 - Figures (only if enabled)

If resolved `figures.enabled` is false: skip figures entirely. The brand uses photos or no imagery. Do not invent SVG figures.

If `figures.enabled` is true:
- `figures.type` = `svg-data`: data-driven charts/diagrams. Read `references/svg-patterns.md` for the 12 patterns + rotation algorithm. Numeric content obeys `content_model.stat_rigor` (Step 7).
- `figures.type` = `svg-decorative`: mood / brand illustration only. NO numeric claims, no fake charts. Use `references/svg-patterns.md` patterns that are non-data (Question Hook, Orbital, Connection Lines, Glass Cards) or original illustration.
- Count per slot from resolved `figures.count_by_slot`.

Read `references/brand-voice-rules.md` for voice enforcement specifics.

### Step 5 - Generate blog HTML (build from resolved format, not from memory)

Assemble in this order, honoring resolved values:

1. **Hero** per `hero_style`:
   - `dark`: full-width band `palette.background_dark`, single `<h1>` in `palette.text_on_dark`, accents `palette.primary`.
   - `light`: band `palette.background_light`/white, `<h1>` in `palette.text_on_light`.
   - `image`: full-bleed hero image + darkening overlay, `<h1>` overlaid in `palette.text_on_dark`.
   - `none`: no band; `<h1>` sits at top of body column.
   Exactly ONE `<h1>` total.
2. **Body** per `body_style` (`serif-editorial` | `sans-clean` | `magazine`) using `typography.*`, max-width `typography.body_max_width_px`. See format-presets.md "Body style details".
3. **Headings** `<h2>`/`<h3>` in `typography.primary_font`, weight `typography.headline_weight`.
4. **Heading numbering** ONLY if `heading_numbering` is true (`1.`, `2.` for H2 skipping the first body H2 and any "Conclusion"; `1.1`, `1.2` for H3). If false, plain headings with no numbers.
5. **Figures** inserted per Step 4, each with a numbered `<figcaption>` ("Figure N." in `palette.primary`) - only if figures enabled.
6. **CTA** section before the end if `cta.enabled` (uses `company.url`).
7. **References** per `references_style`:
   - `apa`: APA 7th edition list with live URLs.
   - `simple`: a short "Sources" list of named links.
   - `none`: omit the reference section entirely.
8. **SEO meta** per `format.blog.seo`: Open Graph if `open_graph`, Twitter Card if `twitter_card`, JSON-LD Article if `json_ld`, canonical URL from `seo.indexing.canonical_base`. JSON-LD `author` = `seo.eeat.author_name` (+ credentials) and `publisher` = `seo.eeat.organization` (fall back to `company.name`). Title 50-60 chars with the primary keyword; meta description 150-160 chars.

### Step 6 - Figure footer branding (only if figures enabled)

Apply footer per resolved `figures.footer_branding`:

- `orb-wordmark`: gradient orb + domain wordmark + tagline (snippet below).
- `wordmark`: domain text only, no orb, no tagline.
- `logo`: brand logo image if provided, else fall back to wordmark.
- `none`: no footer branding on figures.

orb-wordmark snippet (replace `{...}` with config values inline):

```svg
<defs>
  <linearGradient id="brand-orb-grad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{palette._logo_orb_gradient.stop_0}"/>
    <stop offset="100%" stop-color="{palette._logo_orb_gradient.stop_100}"/>
  </linearGradient>
</defs>
<circle cx="70" cy="710" r="13" fill="url(#brand-orb-grad)"/>
<text x="92" y="716" font-family="{typography.primary_font}" font-size="15" font-weight="700" fill="{palette.text_on_dark}">{company.domain}</text>
<text x="1140" y="716" text-anchor="end" font-family="{typography.primary_font}" font-size="11" font-weight="600" fill="{palette.text_on_dark_muted}" letter-spacing="2.5">{company.tagline}</text>
```

### Step 7 - Stat rigor (from content_model.stat_rigor)

- `strict`: every numeric claim (`\d+%`, `\d+x`, `$\d+[KMB]?`) in body AND figures must be in `validated_stats.entries` or cited inline to a real source. Reject invented numbers.
- `cited`: numbers allowed if cited inline `(Source: <name>, <year>)` to a real source. Never invent.
- `off`: no numeric-claim enforcement (lifestyle/brand content). Still never fabricate facts.

### Step 7.6 - SEO + Google quality gate (must get indexed AND rank)

Read `references/google-seo-standards.md` and run the gate (this is what stops the post from being unindexed or treated as thin AI content). Confirm:
- INDEXABLE: one H1, keyworded readable slug, title 50-60 chars, meta description 150-160 chars, canonical, OG/Twitter, JSON-LD Article with real author+publisher, image alt text, internal links to related posts.
- E-E-A-T: real author byline + credentials from `seo.eeat`; first-hand specifics + concrete examples; cited credible sources for claims; factual (honor `content_model.stat_rigor`).
- HELPFUL + people-first: fully answers the search intent; original value beyond restating page 1; a direct answer in the first 1-2 paragraphs.
- NOT thin/scaled AI: genuine added expertise, not a near-duplicate filler page.
- HUMAN VOICE: varied sentence rhythm, concrete detail, a point of view, none of `voice.forbidden_phrases.ai_tells`, no padding.
- KEYWORD/INTENT: primary keyword in title/H1/slug/first-100-words + natural throughout; secondary/long-tail/question variants in H2/H3.

If `seo.quality_gate` is `strict`, do NOT write the draft as ready until every item passes - fix and re-check. (Use the `seo-optimization` skill for a full audit or keyword/intent research.)

### Step 8 - Self-validate before output

- [ ] Layout matches the RESOLVED format (hero_style, body_style, numbering, references, figures presence) - not any assumed default
- [ ] Exactly one `<h1>`
- [ ] If `voice.forbidden_chars.em_dash`/`en_dash`/`emoji` are true: none present
- [ ] No `voice.forbidden_phrases.ai_tells` / `overclaims` (unless in `required_phrasings.approved_only_phrasings`) / `generic_openers`
- [ ] No hex from `palette._forbidden_colors.hex`; no rgba prefix from `palette._forbidden_colors.rgba_prefixes`
- [ ] Numbering present ONLY if `heading_numbering` is true
- [ ] Reference section matches `references_style` (apa / simple / none)
- [ ] Figures present ONLY if `figures.enabled`; each has viewBox `0 0 {svg_figure.viewbox_width} {svg_figure.viewbox_height}` and the correct footer branding
- [ ] Stat rigor honored per `content_model.stat_rigor`
- [ ] If `format.images.provider` is `canva`: a `.thumb.png` sidecar was generated at the configured size
- [ ] SEO/Google gate (Step 7.6) passes: indexable on-page, E-E-A-T (real author + sources + first-hand specifics), helpful/people-first, human voice, intent-matched keyword placement

Fix any failure BEFORE writing output.

### Step 8.5 - Thumbnail image (provider-aware)

The thumbnail is SEPARATE from the in-article figures (those stay SVG, Step 4). Resolve `format.images.provider`:

- `svg` (legacy): do nothing here. The publish script derives the thumbnail from the best in-article SVG figure.
- `canva`: generate a CLICKBAIT thumbnail with the connected Canva tools. Read `references/canva-images.md`. In short: compose a fresh clickbait prompt from this blog's headline/angle, generate a design with Canva at `format.images.sizes.blog_thumbnail_px` (default 1200x630), export PNG, and save it as the sidecar `outputs/blogs/draft-YYYY-MM-DD-slot-{X}-{slug}.thumb.png` (same name as the draft, with `.thumb.png`). The publish script auto-detects this PNG and uses it as the thumbnail, falling back to an SVG figure only if it is missing.

Do this AFTER the HTML is written so the slug is final.

### Step 9 - Output

Write final HTML to `outputs/blogs/draft-YYYY-MM-DD-slot-{X}-{slug}.html`. If you generated a Canva thumbnail in Step 8.5, it sits next to it as `...{slug}.thumb.png`. The publishing pipeline picks both up.

## References

- `references/format-presets.md` - how `format.preset` expands into layout decisions (READ in Step 2)
- `references/svg-patterns.md` - 12 figure patterns + layout invariants (only when figures enabled)
- `references/brand-voice-rules.md` - voice enforcement detail
- `references/canva-images.md` - clickbait thumbnail via Canva (only when `format.images.provider` is `canva`)
- `references/google-seo-standards.md` - Google indexability + E-E-A-T + Helpful Content + human-voice gate (READ in Step 7.6)

## Anti-patterns

- Hardcoding ANY layout choice. Never assume dark hero / white body / numbered headings / APA / figures. Resolve them from `format` every time.
- Hardcoding colors like `#FF0000` - read from `palette.*`.
- Inventing stats when `stat_rigor` is strict/cited.
- Generating SVG figures when `figures.enabled` is false.
- Generic 4-card / 6-card rect grids in SVG - use illustration instead.
- Stacking 16+ animations in SVG - only process patterns animate (max 6-12); static patterns have 0.
- Same SVG pattern on consecutive days at the same slot - apply rotation per svg-patterns.md.
