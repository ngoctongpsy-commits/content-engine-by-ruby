# USAGE — Content Engine by Ruby

A brand-neutral marketing engine. The same skills work for any company because everything
reads from `config/brand.json` (identity, voice, layout, content model, images, video, SEO,
ads) and `config/channels.json` (publishing destinations). Point it at a brand's config and go.

## Install

```
/plugin marketplace add ngoctongpsy-commits/content-engine-by-ruby
/plugin install content-engine-by-ruby@ruby-content-tools
```

(Or clone the repo into your workspace.)

## First-time setup (per brand)

```
/setup-pipeline
```
Copies `config/brand.template.json` → `config/brand.json` and
`config/channels.template.json` → `config/channels.json`, then walks you through filling
identity, voice, pillars, format preset, image/video/SEO/ads settings, and channel routing.
Live configs are git-ignored; only the templates are committed.

## Everyday commands

| Command | What it does |
|---------|--------------|
| `/research <topic>` | Competitor + live-SERP + trend research → a beat-the-SERP brief |
| `/plan-month` | Generate / update a 30-day content calendar across your pillars |
| `/write-blog <A\|B\|C>` | Draft a brand-locked HTML blog for a calendar slot |
| `/seo-audit <file>` | Keyword + intent + Google quality gate (E-E-A-T, Helpful Content, human voice) |
| `/post-weekly` | This week's packet: LinkedIn + Facebook + card image |
| `/make-video <topic>` | Short-form video (script + clip via the video MCP + caption) |
| `/video-today` | Produce the video scheduled in the calendar for today (review queue) |
| `/campaign-plan <goal>` | Full campaign brief + phased calendar handed to the content skills |
| `/ads-plan <brief>` | Plan + draft Meta/Google ads as PAUSED drafts (never spends) |

Skills also fire automatically from natural language (e.g. "viết bài blog cho nhà hàng" →
blog skill). You don't have to type the slash command.

## Connectors (all optional, tool-agnostic)

See `CONNECTORS.md`. Skills name a category (`~~video`, `~~design`, `~~SEO`, `~~ads`,
social publishing) so any MCP in that category works. Defaults: Higgsfield (video),
Canva (design), Make.com + Upload-Post (publishing), Meta + Google Ads (paid). You
authenticate each with your own account; cost notes are in `CONNECTORS.md`.

## Safety

- Paid ads are created as **PAUSED drafts only** — the engine never launches or spends.
- Publishing is opt-in via a connector you wire; review modes save drafts first.
- No credentials/accounts are ever entered by the engine.

Engine-wide rules: `knowledge/playbook.md`. Per-brand edge: `config/brand.json`.

## Video + carousel (0.16.0)
- `/carousel <topic>` — 7-slide carousel (3 templates). Renders PNGs via `scripts/build_carousel.py`.
- `/reel <topic>` — compose a deep-teaching reel bundle (render with your own HTML->MP4 engine).
- Distribution: fill `config/channels.json` (`distribution.caption_files` maps channel -> caption file).
  `python scripts/distribute.py <video> "<caption>" --caption-dir <bundle> --channel facebook_reel --channel instagram_reel --channel linkedin_video --channel linkedin_personal --channel youtube_short`
