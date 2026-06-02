---
description: Generate a full marketing campaign brief (objective, audience, message, channels, phased content calendar, KPIs, optional budget) and hand the calendar to the content skills.
---

# Campaign Plan

Invoke the `campaign-planning` skill.

## Argument parsing

- `/campaign-plan <goal or product>` -> build a campaign around that.
- `/campaign-plan` with no argument -> ask for goal, audience, timeline, and optional budget.

## What the skill does

Reads `config/brand.json` (pillars, voice, channels, video, seo, campaign_defaults) + `config/channels.json` (enabled channels), then writes a brief on the Objective-Audience-Message-Channel-Measure framework PLUS a phased, campaign-mapped content calendar that `/plan-month`, `/write-blog`, `/make-video`, and `/post-weekly` execute. Brand-neutral; uses only channels the brand has enabled. Paid portion uses the connected ads tool (Meta/Facebook) when available.
