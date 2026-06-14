---
name: content-ops
description: Front door and router for the content engine. Use for broad or end-to-end content requests such as setting up posting for a brand, deciding what to post, or running a brand content operation, rather than one specific task. It reads the brand and channels config, decides which stage is needed (research, planning, writing, video, distribution, or reporting), and routes to the right skill including the publish stage. Not for a clearly specific request, which goes straight to its skill.
---

# Content Ops (front door / router)

The entry point for the content engine when the request is **broad or about the whole pipeline**, not a
single skill. It prevents the most common failure: a reusable capability (especially **publishing**) sitting
in the plugin but never getting called because no specific skill description matched the user's vague ask.

## When to use
- Open/ambiguous content requests, or "set up / run content for a brand", "what should I post", "publish this".
- The moment a NEW brand/product is onboarded and the user wants the content operation stood up.

## What it does
1. **Check setup.** Read `config/brand.json` + `config/channels.json` (and the active `examples/<profile>` if
   profiles are used). If missing/placeholder, route to `setup-pipeline` first.
2. **Inventory what already exists** — before building anything, list the relevant skills + any prior outputs
   so we reuse, never rebuild (this is the lesson: discover existing assets first).
3. **Classify intent and route** to the right stage:
   - research / trends            -> `competitor-trend-research`
   - plan / calendar              -> `content-planning` / `campaign-planning`
   - write a blog / article       -> `brand-locked-blog-writing` (+ `seo-optimization`)
   - make a video / Reel / short  -> `video-production`
   - weekly social pack           -> `weekly-social-packet`
   - email                        -> `email-marketing`
   - **PUBLISH / auto-post / schedule / approve** -> `social-distribution`  (the publish stage)
   - measure / report             -> `analytics-reporting`
4. **Hand off** with the context gathered so the target skill doesn't re-ask.

## Pipeline doctrine
Research -> Plan -> Create (blog / video / social) -> **Distribute (publish + Telegram approval + schedule)** ->
Measure. Distribution is a first-class stage, not an afterthought. Always make sure a created asset has a
distribution path (`social-distribution`) rather than ending at a draft.

## Hard rule
Never rebuild a capability the plugin already has. If unsure whether something exists, inventory the skills +
`scripts/` + `knowledge/` first, then act.
