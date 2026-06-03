---
name: analytics-reporting
description: Measure marketing performance and recommend what to do next - build a complete, structured marketing report (executive summary, goals vs KPIs, channel performance, funnel, attribution, budget/ROI, insights, next steps) from the engine's own publish logs plus any connected analytics (Google Analytics / Search Console, platform-native insights, Meta/Google Ads). Use when the user asks for a performance report, "how did our content/ads/email/video do", weekly/monthly marketing numbers, what to double down on, or what to cut. Brand-neutral and tool-agnostic (~~analytics); works from logs + manual inputs when no analytics MCP is connected. Completeness is enforced by knowledge/MARKETING-KPIS.md. Closes the measure loop.
---

# Analytics & Reporting (observability)

The engine's **measure -> optimize** loop. It is **complete by structure, not memory**: it always
reads `knowledge/MARKETING-KPIS.md` first and builds the report against that rulebook's 8 sections +
AARRR x channel matrix. It never invents a number - missing sources are marked **"no data"**.

## Step 0 - Load the rulebook (required)
Read `knowledge/MARKETING-KPIS.md`. The report MUST cover its 8 sections and run its
completeness checklist before finishing. Read `config/brand.json` `analytics.*` (KPI targets,
cadence, providers, report sections) and `config/channels.json` (which channels are live).

## Step 1 - Scope
Ask (if not given): the **period** (e.g. last 7/30 days), the **focus** (all / a channel / funnel / ads), and whether this is **B2B** (include funnel + pipeline) or **e-commerce/local** (include AOV etc.).

## Step 2 - Check the foundation FIRST (Part 5 of the rulebook)
Before any metric: are UTMs, GA4 key events/conversions, and pixel/server-side tracking in place? If the foundation is missing or unknown, say so plainly - numbers built on broken tracking are unreliable. This check goes at the top of the report.

## Step 3 - Gather data per the HYBRID source map (`analytics.sources` + CONNECTORS.md)
1. **Engine publish logs** (`outputs/`) - always available, $0.
2. **Web/SEO** - GA4 MCP + Search Console MCP (free, self-host) if connected.
3. **Paid** - Meta + Google Ads MCPs (connected).
4. **Funnel/CRM** - HubSpot MCP (free tier) if connected. **Email** - Brevo.
5. **Social organic** - social MCP or Windsor.ai if connected.
6. Anything not connected = **"no data"**. NEVER fabricate (EVAL A4/A7), never ask the user to paste as the primary path - recommend connecting the missing source instead.

## Step 4 - Build the report in the 8 sections (use templates/report.template.md)
1. **Executive summary** - 5-9 core KPIs vs target, revenue/ROI, biggest move, top action.
2. **Goals vs KPIs** - target/actual/delta/status from `analytics.kpi`.
3. **Channel performance** - walk the AARRR x channel matrix for every ENABLED channel (SEO/web, social, email, paid, video, content); fill or mark N/A.
4. **Funnel & conversion** - stage conversion + pipeline velocity + CAC payback (B2B) or e-com funnel.
5. **Attribution** - which model; which channels created vs closed demand; marketing-influenced revenue.
6. **Budget & ROI** - spend by channel, CAC, ROAS, ROI.
7. **Insights** - what the numbers MEAN; demote vanity metrics; pair leading + lagging.
8. **Recommendations & next steps** - 3-6 prioritized actions, each naming the next skill (`/write-blog`, `/ads-plan` PAUSED, `/email`, `/seo-audit`...).

## Step 5 - Run the completeness checklist + decision_trace
Before delivering, tick the rulebook's checklist (all 8 sections? every AARRR row per channel or N/A? funnel/attribution/business KPIs present? every number has a target or "no data"?). End with a trace: period, data sources used vs "no data", KPI targets applied, attribution model. Save to `outputs/reports/<period>.md`. Offer to feed findings into `/plan-month`, `/campaign-plan`, `/ads-plan`, `/email`.

## Anti-patterns
- Skipping the rulebook / sections (the old "just list a few metrics" failure).
- Inventing or estimating a metric with no source (use "no data").
- Vanity metrics with no tie to a KPI; recommendations not grounded in the period's data.
- Reporting metrics built on a broken/unknown tracking foundation without flagging it.

## Worked example
Input: `/report last 30 days, all, B2B`, `analytics.kpi.sql_target=20`.
Output: 8-section report - foundation OK (GA4+CAPI live); exec summary (SQLs 16/20 YELLOW, ROAS 3.1, blog drove +38% organic clicks); channel matrix filled (TikTok = no data, not connected); funnel MQL->SQL 22% + velocity 41 days + CAC payback 9mo; attribution = data-driven, organic created demand / paid closed; budget: CAC down 12%; insights + 4 next steps (each -> a skill); trace: sources = logs + GA4 + Meta/Google Ads; no data = TikTok, email (no ESP connected).

## Engine-wide operating rules
Read `knowledge/MARKETING-KPIS.md` (the completeness rulebook), `knowledge/playbook.md` (no invented facts/metrics, ads = paused, publishing opt-in), and `knowledge/FAILURE-MODES.md` (a source offline = say so + degrade, never fake numbers). Brand specifics come from `config/brand.json`.
