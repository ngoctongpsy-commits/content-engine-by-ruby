---
name: seo-optimization
description: Make content rank on Google - keyword + search-intent research, on-page optimization, and a strict Google quality gate (E-E-A-T, Helpful Content, human voice, indexability) so AI-written posts actually get indexed and ranked. Use when the user asks to optimize a post for SEO, do keyword research, run an SEO audit, check if a blog will get indexed, or improve content quality for Google. Brand-neutral and tool-agnostic: keyword data comes from a connected SEO tool if present, else web research.
---

# SEO Optimization

Goal: every post is technically INDEXABLE, passes Google's quality bar (E-E-A-T + Helpful
Content) with real HUMAN VOICE, and targets keywords by INTENT. Read
`references/google-seo-standards.md` first - it is the rulebook this skill enforces.

## When to use

- Optimize a draft/blog for SEO before publishing.
- Keyword + search-intent research for a topic or pillar.
- SEO audit of a page/site or a content gap analysis.
- "Will this get indexed / why isn't this ranking" checks.

## Step 1 - Read config

Read `config/brand.json`:
- `seo.*` - region, language, E-E-A-T identity (author + credentials, organization, sameAs), indexing settings (canonical base, sitemap), quality_gate level.
- `content_model.pillars` + `content_model.stat_rigor`; `voice.forbidden_phrases`.
Read `config/content-calendar.md` for the target keyword/topic if relevant.

## Step 2 - Keyword + intent research (intent-first)

- If a `~~SEO` tool is connected (Ahrefs, Semrush, Similarweb, etc.), pull volume, difficulty, and current rankings. Else use web search to map the landscape. (Say: "connect an SEO tool via MCP for precise volume/difficulty.")
- For each candidate keyword: classify intent (informational / commercial / transactional / navigational), note difficulty (easy/moderate/hard) and a relative demand signal, and find long-tail + question ("how/what/why") variants.
- Confirm INTENT by searching the query and reading the top 5 results: match the content TYPE Google already rewards (guide vs comparison vs product). Pick ONE primary keyword + a few secondary.

## Step 3 - Optimize / write to the Google quality gate

Apply `references/google-seo-standards.md` sections A-F. The content must:
- Indexable on-page: one H1, slugged URL with the keyword, title 50-60 chars, meta description 150-160 chars, canonical, OG/Twitter, JSON-LD Article (real author + publisher), alt text, internal links.
- E-E-A-T: real author byline + credentials from `seo.eeat`; first-hand experience + concrete specifics; cite credible sources for claims; factual, no fabricated stats.
- Helpful + people-first: fully answers the intent, adds original value beyond restating page 1.
- AI-compliant: human expertise + sources + editorial judgement layered on; not thin scaled content.
- Human voice: varied rhythm, concrete detail, a point of view, none of `voice.forbidden_phrases.ai_tells`, no padding.
- Keyword: primary in title/H1/slug/first-100-words + naturally throughout; direct answer in the first 1-2 paragraphs; secondary/long-tail in H2/H3.

## Step 4 - Output (mode-dependent)

- OPTIMIZE mode: return the improved draft (or a precise change list) plus a short "why this now passes" note.
- AUDIT mode (broad site SEO health): produce
  - Executive Summary (biggest strength + top 3 priorities + overall verdict).
  - Keyword Opportunity table (Keyword | Intent | Difficulty | Opportunity | Recommended content type).
  - On-page Issues table (Page | Issue | Severity | Fix).
  - Technical / Indexability checklist (Check | Pass/Warn/Fail): indexation coverage, robots/sitemap/canonical, structured data, HTTPS, mobile-friendliness, broken links + redirect chains, page speed, and Core Web Vitals (LCP, INP, CLS).
  - Authority signals: backlink / referring-domain profile and content cadence (via a `~~SEO` tool if connected, else qualitative).
  - Competitor SEO comparison + content gap: keyword overlap, gaps the competitor ranks for that you do not, content depth and SERP-feature ownership. For a DEEP competitor/trend teardown that turns into a content brief, hand off to the `competitor-trend-research` skill.
  - Prioritized action plan: Quick Wins (under 2h) and Strategic Investments (this quarter).
- Always finish with the GATE VERDICT (see Step 5).

## Step 5 - Gate verdict (the point of this skill)

Score the piece against the gate and state PASS or FIX, listing any failures:
- [ ] Indexability A: one H1, title/meta lengths, canonical, JSON-LD author+publisher, alt text, internal links, keyworded slug
- [ ] E-E-A-T B: real author+credentials, first-hand specifics, cited sources, factual
- [ ] Helpful/people-first C: satisfies intent, original value
- [ ] AI-compliance D: not thin/scaled, real added value
- [ ] Human voice E: varied rhythm, concrete, no AI tells/padding
- [ ] Keyword/intent F: primary placed correctly, intent-matched, direct early answer, internal links

If `seo.quality_gate` is `strict`, do NOT mark a draft ready to publish until every box passes; fix and re-check.

## Anti-patterns

- Chasing high-volume keywords that do not match intent (traffic that never converts or never comes).
- Keyword stuffing / unnatural density.
- Generic AI prose with no first-hand experience (fails E-E-A-T + reads as AI).
- Mass thin near-duplicate posts (scaled content abuse - penalized).
- Fabricated stats or sources (breaks Trust; honor stat_rigor).

## Engine-wide operating rules

Before acting, follow the cross-cutting red-lines and routing in
`knowledge/playbook.md` (ads = paused drafts only / never spend, SEO human-voice + E-E-A-T
gate, publishing is opt-in, no invented facts, publisher fallback routing). Brand-specific
rules still come from `config/brand.json`; the playbook governs what applies to every brand.
