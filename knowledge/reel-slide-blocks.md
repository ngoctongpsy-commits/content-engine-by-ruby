# Daily Reel — SLIDE BLOCKS library (compose every reel from these)

> Goal: compose a fresh `index.html` each day by picking DISTINCT blocks, so reels stay varied,
> dense, on-brand, and rule-compliant — never templated-looking. Reuse this folder's style.css/app.js.
> Render via the HQ wrapper (record_video_playwright → 1080×1920). NEVER the default tab-capture.

## HARD RULES (from REEL-RENDER-RULES.md — obey every time)
- WHITE + CLAY (#D97757) only. NO dark theme. Brand bg (bg.png cube field) + cards carry quality.
- FILL the frame: 2–3 `.slide-element` per slide (≈ one per narration sentence). No empty voids.
- VISUALIZE concretely (code-card / file-tree / diagram / chips / before-after) — never text-only.
- EACH slide = a DISTINCT block. Don't reuse the same block twice in one reel.
- HERO title ≤ 38px, ≤ 2 lines, no stroke/shadow. Never collide with the burned karaoke subtitle.
- NO static bottom captions — engine burns its own karaoke subtitle. Don't add `.scene-caption`.
- Wrap/auto-fit ALL text inside safe margins. Never cut off, never overlap a drawing.
- reveals per slide == sentences for that slide in script-90s.txt (avoid reveal/​sentence mismatch).
- 8–12 slides for ~60–75s. Structure: HOOK → problem → insight → how (2–4 steps, visualized) → result → CTA.

## SLIDE SKELETON (every slide)
```html
<div class="slide" data-slide="N">
  <div class="slide-bg slide-bg-K"></div><canvas class="fx-canvas" data-fx="FX"></canvas>
  <div class="slide-content pixelle-slide-content">
    <div class="slide-element fade-up"> ...block part 1... </div>
    <div class="slide-element scale-in"> ...block part 2... </div>
  </div>
</div>
```
- `slide-bg-K`: rotate K=1..6 across slides (different tint per slide).
- `data-fx`: rotate `scan` / `particles` / `flow` / `rings` / `noise` / `lorenz` (subtle bg motion).
- First slide gets `class="slide active"`. CTA slide adds `conclusion-content` to slide-content.

## TITLE (use on most slides; keep ≤38px via style)
```html
<span class="step-badge"><i class="fa-solid fa-plug"></i> Kicker label</span>
<h2 class="slide-title">Short line<br/><span class="gradient-text">clay word</span></h2>
```

## BLOCKS (pick a DIFFERENT one per slide)
**1. Tool/connector chips row** — "connects to X":
```html
<div class="blind-row">
  <div class="bt"><i class="fa-brands fa-github"></i><span>GitHub</span><div class="bt-x"><i class="fa-solid fa-link-slash"></i></div></div>
  <div class="bt"><i class="fa-solid fa-database"></i><span>Database</span><div class="bt-x"><i class="fa-solid fa-link-slash"></i></div></div>
  <div class="bt"><i class="fa-solid fa-inbox"></i><span>Inbox</span><div class="bt-x"><i class="fa-solid fa-link-slash"></i></div></div>
</div>
```
Lit/on variant: `<div class="lit-row">` with `<div class="bt on">…<div class="bt-ok"><i class="fa-solid fa-bolt"></i></div></div>`.

**2. Big definition + chips**:
```html
<div class="big-def">A <strong>one-line definition</strong> in plain words.
  <div class="def-chips"><span><i class="fa-solid fa-lock-open"></i> open source</span><span><i class="fa-solid fa-bolt"></i> fast</span></div></div>
```

**3. Before / After (two cards)** — split across 2 reveals:
```html
<div class="ba-card ba-before"><div class="ba-tag">Before</div><div class="ba-body"><i class="fa-solid fa-paste"></i><span>the slow manual way</span></div></div>
<!-- reveal 2 -->
<div class="ba-card ba-after"><div class="ba-tag">After</div><div class="ba-body"><i class="fa-solid fa-bolt"></i><span>Claude does it directly</span></div></div>
```

**4. Three-up cards** (e.g. 3 concepts / 3 steps):
```html
<div class="prim-row">
  <div class="prim pr-tool"><i class="fa-solid fa-bolt"></i><b>Label</b><span>desc</span></div>
  <div class="prim pr-res"><i class="fa-solid fa-table-list"></i><b>Label</b><span>desc</span></div>
  <div class="prim pr-prm"><i class="fa-solid fa-comment-dots"></i><b>Label</b><span>desc</span></div>
</div>
```

**5. Code card** (JSON / command / config — for technical how-to):
```html
<div class="code-card"><div class="code-head"><span class="cd r"></span><span class="cd y"></span><span class="cd g"></span><span class="cf">file.json</span><span class="cf-tag">tag</span></div>
  <div class="code-body"><span class="cl"><span class="tok-key">"key"</span>: <span class="tok-str">"value"</span></span><span class="cl hl">  highlighted line</span></div></div>
```

**6. File tree** (plugin/skill structure):
```html
<div class="file-tree"><div class="ft-row"><i class="fa-solid fa-folder"></i>my-plugin/</div>
  <div class="ft-row ind"><i class="fa-solid fa-folder"></i>skills/</div>
  <div class="ft-row ind ft-new"><i class="fa-solid fa-file-lines"></i>SKILL.md</div></div>
```

**7. Sequence / flow** (A → B → result):
```html
<div class="seq">
  <div class="seq-row"><span class="seq-a">Claude</span><span class="seq-arrow">step →</span><span class="seq-b">Tool</span></div>
  <div class="seq-row res"><span class="seq-a">Claude</span><span class="seq-arrow">← result</span><span class="seq-b ok"><i class="fa-solid fa-check"></i></span></div>
</div>
```

**8. Architecture diagram** (host → clients → servers): use `.arch` block (see mcp-explained slide 4).

**9. Logo grid** (many integrations): `.logo-grid` with `<span class="lg xx"><i …></i></span>` × ~12.

**10. Prompt card + fan-out** (one prompt → many tools):
```html
<div class="prompt-card"><i class="fa-solid fa-quote-left"></i> the example prompt text.</div>
<div class="fanout"><span class="fo"><i class="fa-brands fa-jira"></i> Jira</span><span class="fo"><i class="fa-brands fa-github"></i> GitHub</span></div>
```

**11. Transport / two-option rows**: `.tport.tp-local` and `.tport.tp-remote` (icon + label + desc), 1 per reveal.

**CTA (always last slide)**:
```html
<div class="slide-content pixelle-slide-content conclusion-content">
  <div class="slide-element fade-up"><div class="glowing-conclusion"><div class="glowing-orb"></div><div class="icon-badge icon-badge-large icon-badge-success"><i class="fa-solid fa-circle-check"></i></div><h2 class="slide-title">Punchy payoff line.</h2></div></div>
  <div class="slide-element fade-up"><div class="split-panel active"><span>For your team</span><strong>Want this built<br/>for your tools?</strong><i class="fa-solid fa-screwdriver-wrench"></i></div></div>
  <div class="slide-element fade-up"><div class="source-tag"><i class="fa-solid fa-link"></i> YourBrand · yourbrand.com</div></div>
</div>
```

## RENDER
Compose `index.html` + `script-90s.txt` here, then render to a 1080x1920 MP4 with YOUR OWN HTML->MP4 engine
(e.g. a headless-Chromium slide recorder + TTS + burned karaoke subtitles). The plugin does not bundle a
render engine. Keep the asset references (style.css / app.js / logo / fonts) stable for your engine.
