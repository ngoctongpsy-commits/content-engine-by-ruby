---
description: Draft a single blog post (A, B, or C slot) using the brand-locked-blog-writing skill.
---

# Write Blog

Invoke the `brand-locked-blog-writing` skill to draft ONE blog post for the specified slot.

## Argument parsing

Invoked as `/write-blog A`, `/write-blog B`, or `/write-blog C`. Default is A if no slot given.

Slot meaning is brand-defined - read `content_model.slots.<A|B|C>` in `config/brand.json` for each slot's `label`, `intent`, and word counts. Do NOT assume foundational/comparison/news; that was one brand's choice.

## What to ask the user

If `config/content-calendar.md` has a topic for today's date + this slot, USE it. Do not ask.

If no calendar entry exists for today, ask ONE question: "What topic / target keyword for this slot?"

Do not ask anything else - the skill reads voice, palette, layout (`format`), figures, references, and SEO from config.

## What the skill does

1. Reads `config/brand.json` (palette, `format`, `content_model`, voice, validated stats).
2. Resolves the layout from `format.preset` + overrides (hero, body, numbering, references, figures).
3. Reads `config/channels.json` for the publish URL pattern (OG metadata).
4. Reads recent posts in `outputs/blogs/` to avoid repeating SVG patterns (if figures enabled).
5. Researches the topic (web tools if available).
6. Drafts full HTML honoring the resolved format - not any fixed house style.
7. Self-validates against brand rules.
8. Saves to `outputs/blogs/draft-YYYY-MM-DD-slot-X-{slug}.html`.

## After draft

Tell the user: word count, figure count (if any), patterns used, the draft path, and the suggested next step (review in browser, then `python scripts/publish-blog.py --slot X` or wait for scheduled publish).
