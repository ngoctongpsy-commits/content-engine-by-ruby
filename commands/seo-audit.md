---
description: Optimize a post for SEO or run an SEO audit - keyword + intent research, on-page checks, and a strict Google quality/indexability gate (E-E-A-T, Helpful Content, human voice).
---

# SEO Audit / Optimize

Invoke the `seo-optimization` skill.

## Argument parsing

- `/seo-audit <draft path or URL>` -> OPTIMIZE that draft against the Google quality gate.
- `/seo-audit <topic or keyword>` -> keyword + intent research + content recommendation.
- `/seo-audit` with no argument -> ask: optimize a specific draft, research keywords for a topic, or audit a page.

## What the skill does

Reads `config/brand.json` `seo.*`, researches keywords by intent (via a connected `~~SEO` tool if present, else web search), then applies `references/google-seo-standards.md` (indexability, E-E-A-T, Helpful Content, AI-compliance, human voice, keyword/intent) and returns a PASS/FIX gate verdict with concrete fixes.

## Goal

The blogs this engine writes must actually get INDEXED by Google and RANK - not just read well. Use this before publishing any SEO-targeted post.
