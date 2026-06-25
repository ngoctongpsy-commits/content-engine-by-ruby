> **LOCKED 2026-06-24 (Andy) — OVERRIDES the rotation below):**
> - **REEL = every day, automatic** (compose 05:36 -> render 07:00 -> Telegram review -> FB + LinkedIn).
> - **CAROUSEL = on-demand only.** No daily carousel auto-generation. Andy requests it; we build it by hand
>   (so he can add trending music and post it himself). One topic/day -> reel only; we do NOT also repurpose
>   it into a carousel unless Andy asks.

# Reel vs Carousel — daily format decision rule (locked 2026-06-24)

Goal: a research-backed MIX (reels = reach, carousels = engagement) that stays consistent and not robotic.
Sources: 2026 IG data — Reels reach ~3–5× more cold audience; Carousels have the highest engagement/saves;
winning brands use BOTH; **consistency beats volume bursts.**

## Layer 1 — Default rotation (1 post/day)
Pattern weighted **2 reels : 1 carousel** (~67% reels) — YourBrand is early-stage (needs REACH/discovery).
Example week: Reel · Reel · Carousel · Reel · Carousel · Reel · Reel  (= 5 reels + 2 carousels).
As the audience grows, shift toward ~50/50 (carousels convert existing followers → yourbrand.com).

## Layer 2 — Content-fit override (content beats the calendar)
- **REEL** when the topic is: a hooky/surprising fact, a quick tip, news/announcement, a demo or
  before→after, anything motion + voice + music carry well for cold viewers. (Reel's job = get discovered.)
- **CAROUSEL** when the topic is: a framework / checklist / multi-step how-to / comparison / deep
  "save-for-later" teaching — each step = one slide, people SAVE + swipe. (Carousel's job = saves + trust.)
- If a topic is clearly a save-worthy framework/steps → make it a CAROUSEL even if rotation said reel,
  and vice-versa. **Content type wins over the rotation slot.**

## Tie to funnel
- Reels → Explore/Reels tab → NEW people (top of funnel for the Community).
- Carousels → saves/shares/DMs from followers → deepen trust → toward yourbrand.com.

## How the daily pipeline applies it
1. Cron picks the topic + decides format = (rotation slot) unless (content is clearly framework/steps → carousel, or punchy/news → reel).
2. Reel → compose index.html from SLIDE-BLOCKS + render with your own HTML->MP4 engine.
3. Carousel → render 7 slides (PIL, rotate templates A/B/C) + caption.
4. Save to output/<type>/YYYY-MM-DD-<slug>/ with caption.txt → notify Andy "ready".
