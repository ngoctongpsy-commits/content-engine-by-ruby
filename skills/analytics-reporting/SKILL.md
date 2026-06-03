---
name: analytics-reporting
description: Measure marketing performance and recommend what to do next - pull numbers from the engine's own publish logs plus any connected analytics (Google Analytics / Search Console, platform-native insights, Meta/Google Ads), then produce a report with trends, what's working, and concrete optimizations. Use when the user asks for a performance report, "how did our content/ads/email do", weekly/monthly marketing numbers, what to double down on, or what to cut. Brand-neutral and tool-agnostic (~~analytics); works from logs + manual inputs when no analytics MCP is connected. Closes the measure loop and feeds the next campaign/calendar.
---

# Analytics & Reporting (observability)

This is the engine's **measure → optimize** loop. It never guesses numbers: it reports only
figures it can source (a connected analytics/ads tool, the engine's own publish logs, or
numbers the user provides) and clearly marks anything missing as "no data" rather than
inventing it. Brand-neutral: read targets/KPIs from config.

## When to use
- "Báo cáo tuần/tháng", "content/ads/email chạy thế nào", "nên đẩy mạnh cái gì / cắt cái gì", post-campaign review.

## Step 1 - Read config + scope
Read `config/brand.json`: `analytics.*` (region, KPI targets, report cadence, connected providers), `content_model.pillars`, `seo.*`, `ads.*`. Read `config/channels.json` for which channels are live. Ask (if not given): the **period** (e.g. last 7/30 days) and the **focus** (content / social / SEO / ads / email / all).

## Step 2 - Gather data (cost-first, in this order)
1. **Engine publish logs** - `outputs/` packets, published posts, ad-draft records (always available, $0).
2. **Connected analytics MCP** (`~~analytics`) if present - Google Analytics 4 / Search Console (free), platform-native insights.
3. **Connected ads MCPs** - Meta Ads + Google Ads report tools (already connected) for paid metrics.
4. **User-provided numbers** - if a source isn't connected, ask for the figure or mark **"no data"**. NEVER fabricate a metric (EVAL group A4).

## Step 3 - Build the report
Use `templates/report.template.md`. Structure:
- **Snapshot** vs `analytics` KPI targets (target / actual / delta / status GREEN-YELLOW-RED).
- **By channel**: blog/SEO (impressions, clicks, position, indexed?), social (reach, engagement per platform), email (open/click), ads (spend, CPC/CPA, conversions - from the ads MCPs).
- **Trends**: up/down vs previous period; flag anything that moved >20%.
- **What's working / what's not**: tie back to `content_model.pillars` - which pillars/topics/formats win.

## Step 4 - Recommendations (the optimize loop)
3-6 concrete, prioritized actions tied to the data: double-down topics, cut underperformers, SEO fixes (hand to `seo-optimization`), reallocate ad budget (as a PAUSED change for `paid-ads`), email timing. Each rec names the **next skill** to execute it.

## Step 5 - decision_trace + hand-off
End every report with a short trace: data sources used, which were "no data", the period, KPI targets applied. Save to `outputs/reports/<period>.md`. Offer to feed findings into `/plan-month`, `/campaign-plan`, `/ads-plan`, or `/email`.

## Anti-patterns
- Inventing or estimating a metric with no source (use "no data").
- Reporting vanity numbers with no tie to a KPI/objective.
- Recommendations not grounded in the period's data.

## Worked example
Input: `/report last 30 days, focus all` for a brand whose `analytics.kpi.leads_target=40`.
Output: snapshot table (Leads 31/40 · YELLOW), blog top pillar = "how-to" (+38% clicks), TikTok flat (no data - not connected), Meta Ads CPA down 12%; recs: (1) 2 more how-to posts → `/write-blog`, (2) shift 15% budget to the winning ad set → `/ads-plan` PAUSED, (3) connect GA4 for TikTok/site data; trace: sources = publish logs + Meta Ads MCP; no data = TikTok, GA4.

## Engine-wide operating rules
Before acting, follow `knowledge/playbook.md` (no invented facts/metrics, ads = paused drafts only, publishing opt-in) and `knowledge/FAILURE-MODES.md` (if an analytics/ads source is offline, say so and degrade - never silently fill with fake numbers). Brand specifics come from `config/brand.json`.
