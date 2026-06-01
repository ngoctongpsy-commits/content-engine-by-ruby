# SVG Patterns — Brand-Locked Figure Vocabulary

This file defines the 12 patterns + layout invariants. All colors / fonts / wordmark text are placeholders — the skill reads actual values from `config/brand.json` at generation time. NEVER hardcode brand specifics here.

---

## STEP 0 — MANDATORY: Pattern selection algorithm (do this BEFORE writing SVG)

### Step 0.1 — Map topic shape to ONE primary pattern

| Topic / argument shape | Primary pattern |
|---|---|
| Comparing 2 approaches ("X vs Y") | **Versus Split** |
| Provocative question ("Is your AI guessing?") | **Question Hook** |
| Anti-pattern warning ("Stop doing X") | **Anti-Pattern Callout** |
| Layered model / hierarchy / N items in a stack | **Tier Diagram** |
| Single shocking number ("80%", "26x", "$10M") | **Stat Bomb** |
| Countdown / sequence of N events | **Timeline Marker** |
| Agents around a center | **Orbital Particles** |
| Process flow / pipeline transformation | **Data Streams** |
| Single dominant idea | **Pulsing Core** |
| Connection sequence / handoffs | **Connection Lines** |

### Step 0.2 — Within-batch variety check

When generating multiple figures in one batch (Slot A=3, B=2, C=1, total up to 6 across the day's blogs), every figure MUST use a DISTINCT primary pattern.

### Step 0.3 — Cross-day variety check

Read 3 most recent draft or published HTML files in `outputs/blogs/`. Detect their patterns. Do NOT reuse any pattern from those 3 in today's Slot A Figure 1.

### Step 0.4 — Hard rule: Slot A Figure 1 vs yesterday's Slot A Figure 1

The most-visible asset on the blog index page. Two consecutive days of same pattern = damaging monotony. Enforce.

---

## CRITICAL — viewBox + safe-margin rule

Read `svg_figure.viewbox_width` and `svg_figure.viewbox_height` from `config/brand.json`. Use exactly those values: `viewBox="0 0 {width} {height}"`.

Critical text elements must satisfy `x >= svg_figure.safe_margin_left_px` and end at `x <= svg_figure.safe_margin_right_px` (typically 60 and width-60).

Decorative elements (background gradient, particles, grid pattern) may extend full width.

---

## CRITICAL — color palette enforcement

ONLY colors from `config/brand.json` `palette.*` are allowed.

Read these palette anchors:
- Backgrounds: `palette.background_dark`, `palette.background_dark_2`, `palette.background_dark_3`
- Primary accent: `palette.primary`, `palette.primary_dark`, `palette.primary_light`
- Secondary: `palette.secondary`
- Text on dark: `palette.text_on_dark`, `palette.text_on_dark_muted`
- Urgency / warning: `palette.urgency` (use ONLY for "do not do" / coral warnings)
- Logo orb gradient: `palette._logo_orb_gradient.stop_0` to `palette._logo_orb_gradient.stop_100`

**FORBIDDEN:** read `palette._forbidden_colors.hex` list. Every hex in that list MUST NOT appear in any output SVG. Same for `palette._forbidden_colors.rgba_prefixes`.

---

## CRITICAL — Illustrations + drawings, not data cards

Figures must be **illustrations**. Use `<path>`, `<symbol>`, glow halos around drawn icons. AVOID 4-card or 6-card `<rect>` grids with text inside (looks templated). Test: cover all `<text>` elements with your hand — reader should still grasp the main idea from the drawings alone.

---

## CRITICAL — Animation only for PROCESS patterns

**PROCESS patterns (DO animate, max 6-12 `<animate>` elements):**
- Orbital Particles
- Data Streams
- Connection Lines

**STATIC patterns (0 `<animate>` elements):**
- Versus Split, Question Hook, Anti-Pattern Callout, Tier Diagram, Stat Bomb, Timeline Marker
- Pulsing Core may have 1-2 animations on the central element only

Stacking 16+ animations across multiple layers exhausts viewers. ONE primary pattern → ONLY that pattern's animations.

---

## CRITICAL — Layout invariants (prevents text overlap)

The renderer is `cairosvg` (server-side Python, NOT a browser). Known limitations.

### Rule 1 — NEVER inline `<tspan>` mixed-color when parent has `text-anchor="middle"`

cairosvg renders incorrectly. Words overlap.

**WRONG:**
```svg
<text x="600" text-anchor="middle">Word1 <tspan fill="#X">Word2</tspan> Word3</text>
```

**CORRECT — 2 lines:**
```svg
<text x="600" y="100" text-anchor="middle" fill="#A">Word1 Word3</text>
<text x="600" y="135" text-anchor="middle" fill="#B">subline</text>
```

### Rule 2 — Vertical zone separation

Read y-zones from `svg_figure.zones.*` in brand.json:
- Title cluster zone (default y=30-180): kicker, headline, subhead
- Main visual zone (default y=200-680): central element, illustrations
- Footer zone (default y=700-740): wordmark + tagline

Min gap between zones: 20px.

### Rule 3 — Vertical spacing minimums

- Two title lines (38-42px font): 28px gap
- Title subhead to main visual top: 30px
- Orb circle bottom to orb label: 18px
- Last main-visual element to footer top: 20px

### Rule 4 — Horizontal safe rules

- `text-anchor="middle"`: `x ± width/2` must stay within `[safe_margin_left_px, safe_margin_right_px]`
- `text-anchor="start"`: starting x ≥ safe_margin_left_px
- `text-anchor="end"`: ending x ≤ safe_margin_right_px

### Rule 5 — Connection lines stay BEHIND text

Draw connection lines BEFORE orb groups in source order (z-order: behind). Max `stroke-opacity="0.20"`.

### Rule 6 — Self-check before saving figure

5 mental render questions:
1. 2 text elements with overlapping bounding boxes?
2. Text exits safe horizontal margin?
3. Any element crosses zone boundary?
4. Footer positioned below lowest orb label?
5. Inline `<tspan>` with `text-anchor="middle"`?

If any check fails, redo BEFORE saving.

### Rule 7 — Canonical footer pattern (COPY EXACT — do not improvise)

Every figure MUST end with this exact footer, reading values from `config/brand.json`:

```svg
<defs>
  <linearGradient id="lb-orb-grad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="{palette._logo_orb_gradient.stop_0}"/>
    <stop offset="100%" stop-color="{palette._logo_orb_gradient.stop_100}"/>
  </linearGradient>
</defs>
<circle cx="70" cy="710" r="13" fill="url(#lb-orb-grad)"/>
<text x="92" y="716" font-family="{typography.primary_font}" font-size="15" font-weight="700" fill="{palette.text_on_dark}" letter-spacing="0.3">{company.domain}</text>
<text x="1140" y="716" text-anchor="end" font-family="{typography.primary_font}" font-size="11" font-weight="600" fill="{palette.text_on_dark_muted}" letter-spacing="2.5">{company.tagline}</text>
```

### Rule 8 — Source citation color

If figure shows a stat, include source citation at y=685. Color MUST be `palette.text_on_dark_muted`. NEVER use any hex darker than that on dark background.

---

## 12 Patterns (composition specs)

### Pattern 1 — Orbital particles
Central focal node + 6-12 ambient orbiting particles using `<animateMotion>` on `<path>` orbit. Use for "many things around a center."

### Pattern 2 — Data Streams
Horizontal flow left-to-right. 3-5 stage labels. Animated dashed lines (`stroke-dashoffset`). Arrowheads at transitions.

### Pattern 3 — Pulsing Core
Single large central element with pulse animation. Concentric halo rings. 4-6 ambient supporting elements at edges.

### Pattern 4 — Background grid + particles
NOT a primary pattern — use beneath one of Patterns 1-3, 7-12 as the lowest layer.

### Pattern 5 — Glass-morphism cards
Sub-grouping within other patterns. Rounded `<rect>` with translucent fill, subtle aqua border, soft shadow.

### Pattern 6 — Connection Lines (sequenced)
Animated dashed lines between elements. Use for handoff / sequence visuals.

### Pattern 7 — Versus Split
Vertical split at center. LEFT: losing approach (urgency color), key stat. RIGHT: winning approach (primary color), key stat. Title at top with 2 colors. Bottom: shared takeaway.

### Pattern 8 — Question Hook
Massive "?" (320-400pt, gradient + glow). Question text 3 lines. 3 "answer hint" chips at bottom. Vortex rings spiral from "?".

### Pattern 9 — Anti-Pattern Callout
Large X mark / `do-not-enter` in `palette.urgency` with glow. 3 numbered bullets of consequences. Bottom card: solution preview in `palette.primary`.

### Pattern 10 — Tier Diagram
3-6 horizontal bands stacked. Each: aqua left border, label in `palette.text_on_dark`, description in `palette.text_on_dark_muted`. Top tier highlighted.

### Pattern 11 — Stat Bomb
Hero stat HUGE (320-400pt) center, multi-stop gradient + glow. 3 small stat cards top row. Mixed-color 3-line title below hero. Source citation at bottom.

### Pattern 12 — Timeline Marker / Numbered List
Title 3 lines top. Hero number (the count) HUGE (320-380pt). Two columns of numbered items (5 left + 5 right if N=10) with colored number badges + labels.

---

## Anti-patterns (things that make figures look cheap)

- Flat `palette.background_dark` solid fill — always use radial or linear gradient
- Tailwind defaults (`palette._forbidden_colors.hex`) anywhere
- 6+ rectangles in flat grid with no animation — looks like Excel
- Single-color title — always use 2+ colors via separate `<text>` elements
- Decorative ellipses with glow overlapping content text
- Defaulting to Pattern 1 (orbital) when topic shape calls for Stat Bomb / Versus / Tier
- Stacking ambient particles + orbital + streams + pulse all together — pick ONE primary pattern
