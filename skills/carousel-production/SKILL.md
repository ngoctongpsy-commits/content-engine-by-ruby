---
name: carousel-production
description: Produce a multi-slide social CAROUSEL (7 image slides, 4:5 1080x1350) from a topic, using one of three rotating on-brand templates (A Spotlight, B Bold Magazine, C Deep-tech Console). Use when the user wants a carousel, slide post, swipe post, "make a carousel about X", or a save-worthy multi-step / framework / checklist post for Instagram, Facebook, or LinkedIn. Brand-neutral and config-driven (colors from the spec's brand block / config/brand.json). NOT for single images (use weekly-social-packet) and NOT for video/Reels (use reel-production / video-production).
---

# Carousel Production (7-slide, 3 templates)

Turns one topic into a polished 7-slide carousel that teaches/visualizes (not text-in-a-box), ready to post.
Carousels are the ENGAGEMENT format (highest saves); pair with reels (the REACH format). See
`knowledge/format-strategy.md` for when to choose carousel vs reel.

## When to use
- "Make a carousel about X", "turn this into a swipe post", a framework / checklist / multi-step how-to /
  comparison / "save-for-later" teaching where each step = one slide.

## Flow
1. **Pick the template** from `knowledge/carousel-templates.md` selection logic (content type decides):
   C = technical/how-it-works, B = hot-take/announcement, A = concept/benefit (default). Never repeat the
   template used on the previous carousel.
2. **Write the 7-slide spec** (Hook -> Problem -> Inside -> Main x2 -> Conclusion -> CTA) into a JSON file from
   `templates/carousel-spec.template.json`. VISUALIZE each slide (rows/cards/nodes/terminal), never plain text.
   Keep the hero line short; the hook slide is the thumbnail.
3. **Set brand colors** in the spec `brand` block to match `config/brand.json` (or omit for defaults).
4. **Render:** `python scripts/build_carousel.py <spec.json> outputs/carousels/<date>-<slug>/`.
   Produces slide_1.png .. slide_7.png + caption.txt.
5. **Audit** the rendered slides (contact sheet): distinct slides, text inside safe margins, on-brand, hook
   reads as a thumbnail. Then hand to `social-distribution` to post (or the user posts manually + adds music).

## Hard rules
- One topic -> 7 slides; each slide a distinct visual beat; never text-only.
- Brand color + accent only; no childish dot-grid patterns; hook slide = thumbnail.
- LinkedIn vs IG/FB changes only static-vs-animated, not the template style.
- Verify facts before they go in a slide (no invented numbers).

## Files
- `scripts/build_carousel.py` (all 3 templates), `templates/carousel-spec.template.json`,
  `knowledge/carousel-templates.md`, fonts in `scripts/fonts/`.
