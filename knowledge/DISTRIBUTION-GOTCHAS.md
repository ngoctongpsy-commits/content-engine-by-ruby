# Distribution Gotchas — hard-won lessons for auto-posting (read before any social/video publish)

Brand-neutral. These are real failures hit in production and how to avoid them. The distribution
script and the `social-distribution` skill MUST honor every rule here.

## Video / Reels
- **Frame rate 24–60 fps or it is rejected.** Facebook/Instagram Reels reject anything < 24 fps with a
  vague "bad input value" (HTTP 422). Many renderers output 20 fps. ALWAYS re-encode to 30 fps before
  publishing a Reel/short:
  `ffmpeg -i in.mp4 -r 30 -c:v libx264 -profile:v high -pix_fmt yuv420p -g 60 -movflags +faststart -c:a aac -ar 48000 -ac 2 -b:a 128k out.mp4`
- **Specs:** mp4 H.264, 9:16, 1080x1920 recommended (min 540x960), 3–90 s, AAC 48kHz stereo.

## Hosting a video for the platform to fetch (THE big one)
- Facebook's Reels Publishing API (and similar) **fetch the video by URL** and **respect robots.txt**.
  If the host's `robots.txt` blocks crawlers (e.g. a Directus/CMS at `Disallow: /`), the platform
  REFUSES to fetch -> 422, even though the file is reachable by curl. (Images via the Photos API do
  NOT check robots.txt — which is why image posts work from the same host but Reels fail.)
- **Fix:** host the video on a crawler-friendly URL just for the few seconds the platform ingests it.
  After ingest the Reel lives on the platform permanently, independent of the source. A free, no-account,
  crawler-friendly host (e.g. catbox.moe) works; or fix the CMS robots.txt to allow `facebookexternalhit`.
- Verify before publishing: `curl -A "facebookexternalhit/1.1" -sI <url>` must return 200 + video/mp4,
  and the host's robots.txt must not block that agent.

## Make.com routing
- One Custom Webhook -> Router -> one route per channel, **each route MUST have an exact filter**
  (`channel = <value>`). A route with NO filter fires on EVERY payload -> e.g. a reel route hit by a
  photo payload (no video_url) -> "Missing required parameter url" -> Make DEACTIVATES the whole scenario.
- Add an **error handler ("Skip"/Ignore)** on every publish module so one failed post never deactivates
  the scenario.
- LinkedIn: "Create a **Company** Video/Image Post" (company page) vs "Create a **User** ... Post"
  (personal profile) — pick deliberately; the Company module has a `Company` field.
- Make discontinued its native X (Twitter) app (Apr 2025). X needs a 3rd-party connector or paid API.

## What you CANNOT auto-post
- **Facebook Groups** cannot be auto-posted via official API (Groups API deprecated 2024). Make/n8n only
  do Pages + LinkedIn. Group = manual / cross-post from the Page.

## Approval gate (Telegram)
- Two-way approval: propose the post to the user on Telegram (caption + media link + "post/skip"), hold
  it, then publish at the scheduled time only after approval. Telegram `sendMessage` with `parse_mode`
  Markdown 400s on captions containing `#`, `(`, `—` etc — send PLAIN text.
- Only act on a reply that arrived AFTER the proposal (compare message date vs item created time), and
  advance the getUpdates offset, or a stale old reply gets misapplied.

## Scheduling
- Anchor post times to the AUDIENCE timezone, not the operator's. Hold approved items and publish at the
  slot. A timer that runs in the Cowork scheduled sandbox CAN reach catbox + Make + Telegram (verified);
  only some hosts (e.g. a private CMS) may be blocked there.
