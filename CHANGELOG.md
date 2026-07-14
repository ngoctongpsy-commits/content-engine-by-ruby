# Changelog

## 0.16.1 — 2026-07-03
Reliability fix for video distribution (prevents a reel silently disappearing on a flaky upload host).
- **social-distribution `scripts/distribute.py`:** `upload_host()` now **retries** the primary host
  (catbox, 3x with backoff) and **always falls back** to a second host (0x0.st, 2x) so one free host being
  down never loses a post. On total failure it returns cleanly and the caller **exits loudly** ("upload
  failed on every host — re-run to retry") instead of dying with a cryptic error mid-pipeline. No config or
  secrets added; `video_host` still selects the primary.

## 0.16.0 — 2026-06-26
Added the short-form VIDEO + CAROUSEL production layer and upgraded multi-platform distribution.
- **NEW skill `carousel-production`** + `scripts/build_carousel.py` (3 rotating templates A/B/C, 7 slides,
  1080x1350, brand colors from spec/config) + `templates/carousel-spec.template.json` + fonts.
- **NEW skill `reel-production`** — compose a deep-teaching vertical reel bundle (index.html + script +
  4 captions) from a block library; render with your own HTML->MP4 engine.
- **Knowledge:** carousel-templates.md, reel-slide-blocks.md, reel-render-rules.md (IG-safe),
  per-platform-captions.md, format-strategy.md.
- **social-distribution upgraded:** per-platform captions (one render, several voices via
  `distribution.caption_files`), channels facebook_reel + instagram_reel + linkedin_video (company) +
  linkedin_personal (founder) + youtube_short (auto title). `distribute.py --caption-dir`.
- **AGENT.md** added (five agent components).

## 0.15.0
- social-distribution skill + distribute.py / distribution-tick.py (Make webhook, Telegram approval, scheduling).
