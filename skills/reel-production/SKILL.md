---
name: reel-production
description: Compose a DEEP, teaching short-form vertical REEL (1080x1920, up to ~2-3 min) that transfers a real skill - one small, concrete part of a topic per reel, visualized with real artifacts (files, code, trees, terminals), plus per-platform captions. Use when the user wants a reel/Short that actually teaches "how to do X", a how-to or build-walkthrough video, or a daily-reel content pipeline. Outputs a render-ready bundle (index.html + script + 4 captions); the user renders it with their own HTML->MP4 engine, then posts via social-distribution. Brand-neutral. NOT for one-off AI-clip videos (use video-production) and NOT for image carousels (use carousel-production).
---

# Reel Production (deep-teaching vertical reel)

Composes a reel that TEACHES one concrete slice of a topic so the viewer can actually do it - not a generic
"AI is amazing" overview. Reels are the REACH format (discovery); pair with carousels (engagement). See
`knowledge/format-strategy.md`.

> Read `knowledge/reel-slide-blocks.md` (the block library + HARD RULES) and `knowledge/reel-render-rules.md`
> (IG-safe layout, reveals==sentences, white+accent, fill-frame, visualize-not-decorate) EVERY run.

## When to use
- "Make a reel that teaches X", a step-by-step how-to video, a component/feature deep-dive, or a recurring
  daily/weekly reel pipeline.

## Flow
1. **Narrow the topic** to ONE concrete teachable piece (one component / one step / one pattern). Verify every
   fact (file names, fields, commands, numbers) against primary sources - never invent.
2. **Write `script-90s.txt`**: ONE line per slide, ~2 sentences each (CTA may be 3). Depth is allowed (12-24
   slides, up to ~2-3 min) - depth means more real steps/artifacts shown, never filler. Reveals == sentences.
3. **Compose `index.html`** from the block library: one slide per beat, each a DISTINCT block (code-card,
   file-tree, sequence, prompt-card...). VISUALIZE the real artifact. Obey the HARD RULES (hero <=38px, wrap all
   text, no static captions, IG-safe padding). Keep the asset references stable for your render engine.
4. **Write 4 captions** per `knowledge/per-platform-captions.md`: caption-fb.txt, caption-li.txt,
   caption-personal.txt, caption-yt.txt.
5. **Save the bundle** to `outputs/reels/<date>-<slug>/` (index.html, script-90s.txt, caption-*.txt, sources.txt).
6. **Render = bring-your-own engine.** This skill produces the HTML bundle; render it to a 1080x1920 MP4 with
   your own HTML->MP4 recorder (e.g. a headless-Chromium slide recorder + TTS + burned karaoke subtitles).
   The plugin does not bundle a commercial render engine.
7. **Distribute** via `social-distribution` (facebook_reel + instagram_reel + linkedin_video + linkedin_personal
   + youtube_short), review-first, per-platform captions.

## Hard rules (full list in knowledge/reel-render-rules.md)
- White + single accent only (a code/terminal card may be dark); fill the frame; one DISTINCT block per slide.
- VISUALIZE concretely; never text-in-a-box. Hero <=38px, <=2 lines. Wrap all text inside IG-safe margins.
- Reveals per slide == sentences in that slide's script line. No invented facts.

## Files
- `knowledge/reel-slide-blocks.md`, `knowledge/reel-render-rules.md`, `knowledge/per-platform-captions.md`,
  `knowledge/format-strategy.md`. Output bundle consumed by your render engine + `social-distribution`.
