---
name: social-distribution
description: Publish finished content to social channels via the Make webhook, with an optional Telegram approval step and timezone-aware scheduling. Handles video and Reels (auto 30fps plus crawler-friendly hosting) which the image-only weekly social packet does not. Use when content is ready and the user wants it posted, scheduled, or sent for approval. Brand-neutral and config-driven. Not for generating content and not for Facebook Groups.
---

# Social Distribution (publish + approve + schedule)

Brand-neutral publishing layer. This skill takes an already-produced asset (video/Reel, image, or
text+image) and gets it live on the configured channels — with an optional human approval step over
Telegram and timezone-aware scheduling. It complements `weekly-social-packet`/`video-production`
(which CREATE content) by adding the DISTRIBUTION stage.

> **Read `knowledge/DISTRIBUTION-GOTCHAS.md` first, every run.** It encodes the production failures this
> skill must avoid (30 fps, robots.txt/crawler hosting for video, per-route Make filters, error handlers,
> Telegram approval edge cases). Honor every rule there.

## When to use
- The user has a finished video/Reel, image, or post and says "post it", "publish", "schedule this",
  "đăng bài này", "send to Telegram for approval".
- Automatically as the publish step after a content skill produces a ready asset.

## Config (all from `config/channels.json` — never hardcode)
Reuse the existing `social` block (publishers + channels + `channel_field_value`). This skill adds a
`distribution` block:
```
"distribution": {
  "video_host": "catbox",                  // crawler-friendly host for Reels/video (CMS blocks crawlers)
  "ensure_fps": 30,                          // re-encode video below 24fps to this
  "approval": { "enabled": true,             // Telegram approval gate (default ON per brand)
                "telegram_token_file": ".telegram-token",
                "telegram_chat_file": ".telegram-chat" },
  "schedule": {                              // anchor to AUDIENCE timezone, hold then publish at slot
    "timezone": "America/New_York",
    "slots": { "facebook_reel": {"days":"daily","time":"12:30"},
               "linkedin":      {"days":["Tue"],"time":"10:30"},
               "linkedin_video":{"days":["Thu"],"time":"10:30"} } }
}
```
Secrets (Make webhook, Telegram token) live in gitignored `config/.*` files or env — NEVER in the repo.

## Flow
1. **Prepare the asset.** If video: ensure >= 24 fps (re-encode to `ensure_fps`); verify specs.
2. **Host it.** Image -> existing CMS/publisher path. Video/Reel -> upload to the crawler-friendly
   `video_host` and verify `curl -A facebookexternalhit/1.1` returns 200 video/mp4 (see gotchas).
3. **Approval (if enabled).** Send the user a Telegram proposal (caption + media URL + "post/skip",
   PLAIN text). Write the item to the queue with its scheduled `post_at` (audience-tz slot). Do not post yet.
4. **Publish at the slot.** A periodic tick reads Telegram replies (only those after the proposal),
   marks approved/skipped, and at `post_at` fires the Make webhook per channel (`channel_field_value`),
   then confirms on Telegram. Idempotent (awaiting -> approved -> posted/skipped).
5. If approval disabled: publish immediately at the slot (or now) via the same Make path.

## Scripts
- `scripts/distribute.py` — prepare + host + enqueue + Telegram propose (config-driven).
- `scripts/distribution-tick.py` — periodic: read approvals + publish due-approved items + confirm.
  Schedule it (e.g. every 15 min) so the user only taps approve in Telegram.

## Hard rules
- Never post into a Facebook Group (impossible via API) — Pages + LinkedIn only.
- Every Make route must be channel-filtered and carry a Skip error handler (see gotchas).
- Choose LinkedIn Company vs User module deliberately per the channel config.
