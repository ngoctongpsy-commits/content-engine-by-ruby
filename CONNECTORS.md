# Connectors (optional, tool-agnostic)

This plugin works from files + skills alone. Connect any of these to extend the pipeline.
Skills refer to a CATEGORY (e.g. `~~video`, `~~SEO`) so any MCP in that category works; the
`.mcp.json` pre-configures a default, but you authenticate with your own account.

| Category | Used by | Default in .mcp.json | Other options |
|---|---|---|---|
| `~~video` | video-production (make-video) | Higgsfield (`https://mcp.higgsfield.ai/mcp`) | any video-generation MCP |
| `~~design` | Canva thumbnails + social images | Canva (connect separately) | Figma, Adobe |
| `~~SEO` | seo-optimization, competitor-trend-research | none (web search fallback) | Ahrefs, Semrush, Similarweb |

## Higgsfield (video)

1. In Claude: Settings -> Connectors -> Add custom connector -> URL `https://mcp.higgsfield.ai/mcp`.
2. Authenticate with your Higgsfield account. Video generation consumes Higgsfield credits (the free plan has 0).


## Social publishing (multi-platform)

Each social channel posts via its `publisher` (default `make`). Set `fallback_publisher` and the system auto-switches if the primary errors (and notifies you).

| Publisher | Cost | Covers | When to use |
|---|---|---|---|
| **make** (Make.com) | free tier / ~$9+/mo (ops) | LinkedIn, Facebook, Instagram, YouTube (easy via native modules) | Default. You already use it. Add IG/YouTube modules in your scenario. |
| **upload-post** (upload-post.com) | **FREE 10 posts/mo**, ~$16/mo unlimited | TikTok, Threads, X (the hard ones) + IG/YouTube/FB/LinkedIn | Cheapest fallback for hard platforms. Sign up, put API key in `config/.upload-post-key`, set `enabled: true`. |

Recommended: keep **Make** for the easy platforms; only enable **Upload-Post** as a fallback for TikTok/Threads/X when you need them. The native platform APIs (TikTok/Threads/IG) are free - upload-post just handles their app-approval for you.
