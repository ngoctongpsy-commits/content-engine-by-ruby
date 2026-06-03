# Failure Modes — degrade loud, never silent

Harness rule: when a dependency fails, the engine must **say so and degrade safely** —
never silently continue with fabricated or stale data. One place to look when something
doesn't work.

| Dependency | Failure | Correct behavior |
|---|---|---|
| `knowledge/playbook.md` missing | can't load engine rules | Skill flags + refuses to improvise engine-wide rules. |
| `config/brand.json` missing | no brand identity | Skill prompts `/setup-pipeline`; never invents a brand. |
| A `references/`/`knowledge/` doc missing | rulebook gone | Skill that needs it stops and names the missing file (e.g. SEO gate without `google-seo-standards.md`). |
| `~~analytics` source offline (GA4/GSC) | no metrics | Report marks those rows **"no data"**; never estimates a number. |
| Meta/Google Ads MCP error | no paid metrics / can't draft | Report shows "ads data unavailable"; `paid-ads` exports a paste-ready plan instead. |
| `~~email` provider not connected | can't stage in tool | `email-marketing` outputs paste-ready content + a send checklist (export_only). Never sends. |
| Social publisher (Make) errors | post not sent | Auto-failover to `fallback_publisher` (Upload-Post); if both fail, save draft + alert. |
| Video MCP (Higgsfield) out of credits | no clip | Save the script + storyboard, flag "needs credits"; don't fake a clip. |
| Stale config (old offers/stats) | wrong facts | Skill notes "config may be stale" rather than trusting blindly (EVAL E3). |

> Golden rule: a missing metric is **"no data"**, never a guess. A blocked action is
> **reported**, never silently skipped.
