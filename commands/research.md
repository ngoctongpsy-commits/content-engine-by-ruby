---
description: Research competitors and what is ranking / trending for a topic, then get a beat-the-SERP content brief to write from.
---

# Research (competitors + trends)

Invoke the `competitor-trend-research` skill.

## Argument parsing

- `/research <topic or keyword>` -> SERP + trending analysis for that topic + a content brief.
- `/research <competitor name or URL>` -> deep competitor content teardown.
- `/research` with no argument -> ask: a topic to research, or competitors to study.

## What the skill does

Reads `config/brand.json` (pillars, competitors, seo), studies competitors + the live SERP + trending angles (via a connected `~~SEO` tool if present, else web search), and returns competitor + trend tables plus a beat-the-SERP brief (intent-matched keywords, the unique angle + original value to add, outline, internal links, sources). The brief feeds `/plan-month` and `/write-blog`. Never duplicates competitors - it adds value to win.
