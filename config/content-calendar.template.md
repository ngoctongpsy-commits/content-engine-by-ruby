# Content Calendar — Template

Editable monthly content plan. The blog-writing skill reads this file to pick which topic to write today.

## Format

Each row = one blog. Calendar covers next 30-90 days.

```
| Date | Slot | Pillar | Topic | Target keyword | Notes |
|---|---|---|---|---|---|
| YYYY-MM-DD | A/B/C | <pillar-name> | <one-sentence topic> | <SEO keyword> | <optional> |
```

## Slot definitions

- **Slot A** — 10:30 publish. Foundational/educational. 2200-2500 words, 3 figures, full APA references.
- **Slot B** — 14:30 publish. Comparison/how-to. 1500-1800 words, 2 figures, partial references.
- **Slot C** — 18:30 publish. News/commentary. 1000-1400 words, 1 figure, current-event refs.

## Pillars

Define 3-5 pillars representing core content domains. Skill rotates equally across pillars.

```
| Pillar | Sub-topics |
|---|---|
| pillar-1 | ... |
| pillar-2 | ... |
```

## Feature rotation (for weekly social)

The weekly social pipeline rotates between:
- 3 weeks/month: **blog_driver** — drives traffic to a published blog
- 1 week/month (last Monday): **feature_promo** — promotes a product feature, customer proof, or regulatory angle

Customize per-month override schedule below:

```
| Month | Last Monday | Angle | Specific topic |
|---|---|---|---|
| YYYY-MM | YYYY-MM-DD | copilot / customer_proof / deployment_moat / regulatory | <specific> |
```

## See also

- `examples/luna-base/config/content-calendar.md` for a worked example
