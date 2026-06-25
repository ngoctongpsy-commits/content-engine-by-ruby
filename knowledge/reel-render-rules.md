# Reel render rules (engine-agnostic)

The HARD rules a composed reel must satisfy so it renders well and reads on every platform. These are
independent of which HTML->MP4 engine you use.

## Layout & style
- WHITE / cream background + a SINGLE brand accent. No dark slide backgrounds (a code/terminal card may be dark).
- FILL the frame: ~2-3 reveal elements per slide (about one per narration sentence). No empty voids.
- VISUALIZE concretely (code-card / file-tree / diagram / chips / before-after / nodes) — never text-in-a-box.
- Each slide = a DISTINCT block; don't reuse the same block type twice in a row.
- Hero title <= 38px, <= 2 lines, no stroke/shadow. Never collide with the burned subtitle.

## Safe zone (IG/TikTok crop)
- The 9:16 file is correct, but IG/TikTok overlay ~220px top + ~400px bottom (handle, caption, buttons).
- Keep titles/cards inside that safe zone (top padding ~170px, bottom padding ~400px) and place burned
  karaoke subtitles around 420px from the bottom so the platform UI never covers them.

## Timing
- One line per slide in `script-90s.txt`, ~2 sentences (CTA may be 3). Reveals per slide == sentences for that
  slide. A reveal/sentence mismatch breaks the pacing.
- 8-24 slides depending on depth (a deep how-to may run ~2-3 min). Depth = more real steps shown, never filler.

## Output
- 1080x1920, >= 24fps (re-encode to 30fps before posting if lower). Burned subtitles, brand-consistent.
- Render with your own engine; this plugin supplies the composition rules + block library, not the engine.
