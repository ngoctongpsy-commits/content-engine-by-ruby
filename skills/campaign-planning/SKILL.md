---
name: campaign-planning
description: Plan a full marketing campaign - objective, audience, message, channels, a phased + campaign-mapped content calendar, KPIs, and optional budget - then hand the calendar off to the content/blog/video/social skills to execute. Use when launching a campaign, a product launch, a seasonal push, or any multi-channel effort bigger than the regular content calendar. Brand-neutral and config-driven; nothing about industry or channels is assumed.
---

# Campaign Planning

A campaign sits ABOVE the regular 30-day calendar: one objective + message driving coordinated
content across channels over a fixed window. This skill writes the brief AND produces a
campaign content calendar that `content-planning` / `write-blog` / `make-video` /
`post-weekly` then execute. Brand-neutral: read everything from config.

## When to use

- Launch / product release / seasonal push / lead-gen drive / re-engagement - anything that needs a coordinated multi-channel plan, not just a steady content cadence.

## Step 1 - Read config + inputs

Read `config/brand.json`: `company`, `content_model.pillars`, `content_model.slots`, `voice.*`, `format.*`, `video.*`, `seo.*`, and `content_model.campaign_defaults` (default objectives, KPI templates, budget currency). Read `config/channels.json` for the brand's ENABLED channels (blog/CMS, social platforms, video) - the campaign only uses channels the brand actually has.

Ask the user (if not given): campaign GOAL, AUDIENCE, TIMELINE (+ any fixed date), and optional BUDGET. Optionally pull a `competitor-trend-research` brief for positioning.

## Step 2 - Build the brief on the O-A-M-C-Measure framework

1. **Objective** (SMART): pick awareness / consideration / conversion / retention / advocacy. State one specific measurable goal + timeframe.
2. **Audience**: a short profile - "[role] at [type] struggling with [pain], wants [outcome], found via [channels], cares about [priorities]." No assumed industry.
3. **Message**: core message (1 sentence) + 3-4 supporting points + proof points (honor `content_model.stat_rigor` - no fabricated numbers) + differentiation. Follow the hierarchy: why care -> the solution -> why you -> the CTA. Use brand `voice`.
4. **Channels**: choose from the brand's ENABLED owned channels (blog, social platforms, video, email when present) + earned + paid (Meta/Facebook ads via the connected ads tool if available; Google later). For each: why it fits, content format, effort (low/med/high), and budget share if a budget was given.
5. **Measure**: KPIs aligned to the objective (1 primary with a target + 3-5 secondary), how each is tracked, reporting cadence. If an analytics tool is connected, anchor targets to real benchmarks.

## Step 3 - Campaign content calendar (the hand-off)

Produce a phased, dated calendar mapped to the campaign - this is what the other skills execute. Use the same columns as the regular calendar PLUS a Campaign column, and respect `Format` (blog/video) + `Platform`:

```
| Date | Phase | Format | Platform/Channel | Pillar | Topic | Target keyword | Notes |
```

Phases: typically Pre-launch (tease/build) -> Launch -> Sustain -> Wind-down. Work backward from the fixed date; note dependencies ("landing page live before paid ads"). Balance channels (don't over-index one). Keep every topic tied to a pillar + the campaign message.

## Step 4 - Assets list + budget + risks + next steps

- **Assets needed**: every piece (blog, video, social set, ad creative, landing page, email) + must-have vs nice-to-have + when.
- **Budget allocation** (only if a budget was given): split by channel, production vs distribution, 10-15% contingency, in `campaign_defaults.currency`.
- **Risks + mitigations**: 2-3.
- **Next steps**: immediate actions + approvals needed.

## Step 5 - Output + hand-off

Write the brief to `outputs/campaigns/<campaign-slug>.md` and the campaign calendar so `content-planning` can merge it (or append to `config/content-calendar.md`). Then offer to:
- Generate the calendar into the working calendar (`/plan-month`), or
- Start drafting the first asset (`/write-blog`, `/make-video`), or
- Pull a competitor brief (`/research`) to sharpen the message, or
- Plan + draft the paid portion as PAUSED ads via the `paid-ads` skill (Meta/Facebook now, Google when connected) - drafts only, you launch.

## Anti-patterns

- A "campaign" that is just a content list with no single objective/message.
- Channels the brand has not enabled, or an assumed audience/industry.
- Fabricated KPIs/benchmarks or stats (honor stat_rigor).
- Over-indexing one channel; no phasing; ignoring the fixed date / dependencies.
