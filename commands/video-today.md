---
description: Produce the video scheduled in the content calendar for today (or a given date) into the review queue. Does not auto-post.
---

# Video Today (calendar-driven)

Invoke the `video-production` skill in CALENDAR-DRIVEN mode.

## Argument parsing

- `/video-today` -> today's date. `/video-today YYYY-MM-DD` -> that date.

## What it does

Reads `config/content-calendar.md`, finds the row for the date whose `Format` is `video`, and produces it (script + clip via the connected `~~video` MCP / Higgsfield at the row's platform aspect + caption). With `video.automation.mode = review` (default) it saves the packet to `outputs/video/pending` and notifies you to approve + post; it never auto-posts. If there is no video row for the date, it does nothing.

## Scheduling (for hands-off use)

To run this automatically, set up a Cowork scheduled task (NOT the headless cron, because Higgsfield runs over MCP which needs a Claude session). Example prompt for the task: "Run /video-today for today; if a video is scheduled, create it into the review queue and notify me." The Claude app must be open for the task to run on time (otherwise it runs at next launch). Each run consumes Higgsfield credits.
