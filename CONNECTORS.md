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
