---
description: Generate this week's social packet (1 LinkedIn + 1 Facebook + 1 clickbait SVG). Invokes the weekly-social-packet skill.
---

# Post Weekly Social

Invoke the `weekly-social-packet` skill to produce one week's social content packet.

## What the skill does

1. Reads `config/brand.json` + `config/channels.json` + `config/content-calendar.md`.
2. Determines post type:
   - **blog_driver** (3 of 4 weeks) - picks highest-scoring published blog from last 7 days, drives traffic to it.
   - **feature_promo** (last Monday of month) - reads feature rotation table from calendar, promotes a product feature / customer proof / regulatory angle.
3. Drafts LinkedIn post (company voice, 900-1400 chars, 3-5 hashtags).
4. Drafts Facebook post (300-600 chars, casual hook, URL inline).
5. Generates 1080x1080 clickbait SVG (one of 6 patterns: Stat Bomb, Versus Split, Anti-Pattern, Tier Diagram, Question Hook, Timeline Marker).
6. Stat-trace validates: every number in SVG must trace to source (blog_html for blog_driver, validated_stats for feature_promo).
7. Self-validates against brand rules.
8. Writes packet JSON to `outputs/social/pending/weekly-YYYY-MM-DD.json`.

## What to ask the user

Only if BOTH of these are missing:

1. No published blogs in `outputs/blogs/` from last 7 days, AND
2. `config/content-calendar.md` has no feature rotation entry for this month.

In that case, ask: "No blog driver available and no feature rotation set. What angle should I write?" and offer Question Hook / Tier Diagram (numberless patterns).

Otherwise, just run the skill.

## After generation

Tell the user:

- Post type chosen (blog_driver / feature_promo) and why
- SVG pattern chosen and why (argument shape match)
- Character counts for LinkedIn + Facebook posts
- Path of the JSON packet
- Suggested next step: review packet, then run `python scripts/post-weekly-social.py` (or wait for scheduled posting).

Built by Ruby.
