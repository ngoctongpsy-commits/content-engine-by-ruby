---
description: Plan + draft a paid ad campaign (Meta/Facebook + Google) as PAUSED drafts for you to review and launch. Never spends.
---

# Ads Plan

Invoke the `paid-ads` skill.

## Argument parsing

- `/ads-plan <objective or product>` -> plan + draft ads for that.
- `/ads-plan` with no argument -> ask for platform, objective, audience, budget, landing URL.

## What the skill does

Reads `config/brand.json` `ads.*`, plans the campaign structure + targeting, writes on-brand ad copy + creatives (Canva image / Higgsfield video), and creates PAUSED drafts via the connected `~~ads` MCP (Meta = full draft creation; Google = draft if a creation-capable MCP is connected, else an export to paste into Google Ads). SAFETY: drafts only - it never launches, raises budget, or spends. You review in Ads Manager and launch yourself.
