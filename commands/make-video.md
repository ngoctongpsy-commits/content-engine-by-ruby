---
description: Make a short-form social video (script + clip via Higgsfield + caption) for a topic or to repurpose a blog. On-demand.
---

# Make Video

Invoke the `video-production` skill.

## Argument parsing

- `/make-video <topic>` -> script + clip + caption for that topic.
- `/make-video <blog draft path or URL>` -> repurpose that blog into a short video.
- `/make-video` with no argument -> ask for the topic (or blog) and the target platform(s).

## What the skill does

Reads `config/brand.json` `video.*`, writes a <=15s script/storyboard, generates the clip per enabled platform aspect via the connected `~~video` MCP (default Higgsfield, `https://mcp.higgsfield.ai/mcp`), and writes platform captions. Generating video uses your Higgsfield credits (free plan = 0). On-demand only - it does not auto-schedule or auto-post.
