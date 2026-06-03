---
description: Build a marketing performance report (content, social, SEO, ads, email) from publish logs + connected analytics, with trends and prioritized optimizations. Read-only - never changes anything.
---

# Report

Invoke the `analytics-reporting` skill.

## Argument parsing

- `/report <period> [focus]` -> e.g. `/report last 30 days, ads` builds that report.
- `/report` with no argument -> ask for the period and focus (content / social / SEO / ads / email / all).

## What the skill does

Reads `config/brand.json` (`analytics` KPI targets, pillars, seo, ads) + `config/channels.json`, then gathers numbers cost-first: the engine's own publish logs ($0), any connected `~~analytics` tool (Google Analytics / Search Console - free) and the connected Meta/Google Ads MCPs for paid metrics. Produces a snapshot vs targets, by-channel breakdown, trends, what's working, and 3-6 prioritized optimizations - each naming the next skill to execute it. NEVER fabricates a metric: missing sources are marked "no data". Read-only.
