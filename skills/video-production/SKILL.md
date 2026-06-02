---
name: video-production
description: On-demand short-form video for social posts. Writes a script/storyboard, generates the clip with the connected video MCP (default Higgsfield), and writes platform captions. Use when the user asks to make a video, a Reel/Short/TikTok, a video post, or "turn this into a video". Brand-neutral and tool-agnostic (~~video). Per-platform aspect ratios from config. NOT auto-scheduled - runs only on request.
---

# Video Production (on-demand)

Make a short-form social video end to end: SCRIPT -> VIDEO (via the connected ~~video MCP,
default Higgsfield) -> CAPTION. Read `config/brand.json` `video.*` first. Generating video
consumes the user's Higgsfield credits (free plan = 0 -> it will fail; tell the user to top up).

## When to use

- "Make a video / Reel / Short / TikTok about X", "turn this blog into a video", "video post for <platform>".
- On request only. This skill is NOT part of the auto content calendar.

## Step 1 - Read config + scope

Read `config/brand.json`: `video.*` (provider, default_model, style, platforms + aspect), `company`, `palette`, `voice`, `seo` (for intent/keywords if repurposing a blog).
Confirm with the user: the topic (or the blog/brief to repurpose) and the TARGET platform(s). Use only `video.platforms` where `enabled` is true; each gives the aspect + max_seconds.

## Step 2 - Write the script / storyboard

Produce a tight script for a <= max_seconds clip:
- HOOK in the first 1 second (a bold visual + a curiosity line) - this decides watch-through.
- 2-4 BEATS/SHOTS: for each, a one-line visual description + short on-screen text + the spoken/voiceover line (if `video.voiceover`).
- END: a clear CTA + the `company.domain` wordmark.
- Match `voice` (tone, no forbidden phrases/chars). Clickbait but truthful - no fabricated claims/stats (honor `content_model.stat_rigor`).
On-screen TEXT must be short and CORRECT; treat it like the image rule - prefer adding it as a reliable caption/overlay, never trust the generator to spell long text.

## Step 3 - Generate the clip (via ~~video MCP, default Higgsfield)

If no ~~video MCP is connected: stop and tell the user to connect one (Higgsfield: add custom connector `https://mcp.higgsfield.ai/mcp`, then authenticate). 

With Higgsfield connected:
1. Check `balance`/`show_plans_and_credits`; if 0 credits, warn that generation needs credits.
2. Pick a model: use `video.default_model` if set, else `models_explore` (action recommend) with the goal (text-to-video or image-to-video) and chosen aspect.
3. For EACH enabled target platform, generate at that platform's `aspect` and within `max_seconds`. Build the generation prompt from the storyboard shots (style, palette mood, motion). If you have a brand image/thumbnail, you can do image-to-video for consistency.
4. Use `job_display` / `show_generations` to poll and retrieve the finished clip URL(s). Optionally `reframe` to produce other aspects from one render, and `virality_predictor` to sanity-check the hook before finalizing.

## Step 4 - Captions per platform

Write a caption + hashtags per target platform in the brand voice (LinkedIn = professional; TikTok/Reels/Shorts = punchy; Facebook = friendly). Include the CTA + link. Keep numbers truthful.

## Step 5 - Output a video packet

Return: the script/storyboard, the generated clip URL(s) per platform/aspect, and the captions. Save a JSON packet to `outputs/video/pending/video-YYYY-MM-DD-<slug>.json`. Offer to hand the captions + clip to the weekly social flow for posting (the user posts; this skill does not auto-publish).

## Anti-patterns

- Generating without confirming target platform/aspect (wrong crop = unusable).
- Trusting the generator to render long on-screen text (gibberish) - keep text short / add as overlay.
- Fabricated stats or claims in the script.
- Auto-posting - this skill is on-demand; the user reviews and posts.
- Ignoring credits - a free Higgsfield plan has 0 credits and generation will fail.
