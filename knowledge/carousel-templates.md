# Carousel Templates — rotation pool & selection logic

3 reusable carousel templates, 4:5 (1080x1350), 7 slides: Hook -> Problem -> Inside -> Main x2 -> Conclusion -> CTA.
Brand colors come from the spec's `brand` block (default: cream bg + a single accent). Slide 1 is always a
scroll-stopping HOOK and doubles as the post thumbnail (never a separate off-brand clickbait image).

## The 3 templates
- **A - Spotlight**: airy, calm, premium. Centered headline + floating chip pills + soft accent glow. Default.
- **B - Bold Magazine**: high energy. Top accent->deep gradient block + huge left-aligned headline on cream.
- **C - Deep-tech Console**: futuristic/engineering. HUD corner brackets + ethereal bokeh bottom (NO grid lines)
  + a real dark terminal card (command/cron + cursor) + glowing pipeline nodes.

## Selection logic (content type decides first)
1. **C - Deep-tech** -> technical / how-it-works topics: commands, config, cron, pipelines, integrations, "dev".
2. **B - Bold Magazine** -> strong-statement / hot-take / "Stop-Don't" hooks: punchy, contrarian, announcements.
3. **A - Spotlight** -> concept / mindset / benefit ("why") topics; also the DEFAULT when a topic doesn't lean
   clearly technical or hot-take.

## Rotation rules (anti-boredom)
- Never use the same template on two consecutive posts.
- Aim to hit all 3 within a week.
- If a topic fits two templates, pick the one least recently used.

## How to render
`python scripts/build_carousel.py <spec.json> [out_dir]` -> writes slide_1.png .. slide_7.png + caption.txt.
Run with no args to render a 3-template demo (eyeball all A/B/C). Spec template: `templates/carousel-spec.template.json`.
Fonts ship in `scripts/fonts/` (Inter + JetBrains Mono). FontAwesome glyphs are avoided (drawn shapes instead)
to prevent missing-glyph tofu.
