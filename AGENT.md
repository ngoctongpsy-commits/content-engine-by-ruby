# AGENT.md — content-engine-by-ruby

How this plugin covers the five components of an AI agent.

| Component | How this plugin covers it |
|-----------|----------------------------|
| **Model** | Claude (Cowork/Code). Per-skill notes recommend depth where it matters (research + verify for blog/reel/analytics; lighter for packet/distribution). No model is hardcoded. |
| **Harness** | Commands are the entry points (`/plan-month`, `/write-blog`, `/post-weekly`, `/report`, ...). Skills chain: plan -> create (blog / weekly-social-packet / video-production / **reel-production** / **carousel-production**) -> **social-distribution** (publish). Guardrails: Telegram review-first approval gate + per-route Make filters + Skip error handlers + timezone-scheduled slots. |
| **Tools & Skills** | 14 skills (content-ops router, content-planning, brand-locked-blog-writing, seo-optimization, weekly-social-packet, video-production, **reel-production**, **carousel-production**, competitor-trend-research, email-marketing, paid-ads, campaign-planning, analytics-reporting, social-distribution). Connectors chosen cost-first (Make webhook default; upload-post.com free fallback for hard platforms). Scripts: build_carousel.py, distribute.py, distribution-tick.py, publish-blog.py, etc. |
| **Runtime** | Cowork desktop / Claude Code. Secrets live only in gitignored `config/.*` files or env (Make webhook, Telegram token, CMS token) — never in the repo. Rendering of reels uses the user's own HTML->MP4 engine (not bundled). |
| **Memory** | `knowledge/` is the durable asset: playbook.md, MARKETING-KPIS.md, DISTRIBUTION-GOTCHAS.md, FAILURE-MODES.md, google-seo-standards.md, **carousel-templates.md**, **reel-slide-blocks.md**, **reel-render-rules.md**, **per-platform-captions.md**, **format-strategy.md**. Between runs, content state lives in `outputs/` (calendars, drafts, queues) + `config/`. |

> Knowledge is the asset; the plugin is the container; the brand's specifics (config + knowledge) are the edge.
