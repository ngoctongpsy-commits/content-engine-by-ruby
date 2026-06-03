---
name: competitor-trend-research
description: Research competitors and what is currently ranking / trending for a topic, then turn it into a beat-the-SERP content brief the engine writes from. Use when the user asks to study competitors, see what is ranking or trending, find content gaps, "what should I write to beat X", or get inspired by top posts before planning or writing. Brand-neutral and tool-agnostic: uses a connected SEO/analytics tool if present, else web research. Output FEEDS the content-planning and blog-writing skills.
---

# Competitor + Trend Research

Goal: before planning or writing, learn what is already winning (competitors + the live SERP +
trending angles), then produce a brief to write something that MATCHES the intent and BEATS it
with original value. Never duplicate - Google rewards added experience/data, not copies
(see `../../knowledge/google-seo-standards.md`, sections C and D).

## When to use

- "Research my competitors" / "what is competitor X doing in content".
- "What is ranking / trending for <topic>" / "what should I write about this week".
- Content gap analysis; inspiration from top posts before writing a Slot A/B/C piece.

## Step 1 - Read config + scope

Read `config/brand.json` (`company`, `content_model.pillars`, `seo.*`) and `config/content-calendar.md`. Confirm: the topic/keyword (or pillar), and the competitors (user-named, or infer 3-5 from the brand's space via web search).

## Step 2 - Competitor deep-dive

For each competitor:
- If a `~~SEO` tool (Ahrefs/Semrush/Similarweb) is connected: pull their top organic pages, the keywords they rank for, traffic share, and most-linked content. Else use web search.
- Capture, per top piece: the topic/keyword + intent, the angle, format (guide/listicle/comparison/story), length/depth, heading structure, what they do WELL, and what they MISS or do thinly (your opening to win).
- Note their authority signals (who links to them, content cadence) at a high level.

## Step 3 - Live SERP + trending analysis (for the target topic)

- SEARCH the target query and read the current top 5-10 results: format Google rewards, depth, subtopics covered, the "People Also Ask" questions, and gaps none of them answer well.
- Find trending/timely angles: rising search interest, seasonal hooks, recent news/events in the niche (web search; or a `~~SEO`/trends tool if connected). Keep only trends relevant to the brand's pillars.
- Identify the "10x" opening: the angle, depth, first-hand experience, or data that would make a clearly better page than what ranks now.

## Step 4 - Synthesize a beat-the-SERP content brief

Produce, per recommended topic, a brief the blog skill can write straight from:
- Working title options (intent-matched, with the primary keyword)
- Primary + secondary + question keywords, and the search intent
- The unique angle + the ORIGINAL value to add (first-hand experience, data, opinion) so it is not derivative
- Outline: the H2/H3 subtopics to cover (union of what top results cover PLUS the gaps they miss), and the direct answer to put in the first 1-2 paragraphs
- Internal link targets (related pillar/cluster pages) and 2-3 credible external sources to cite
- Why it can win (the specific weakness in the current SERP this beats)

## Step 5 - Output

- Competitor table: Competitor | Top piece/topic | Format | Strength | Gap to exploit.
- Trending/SERP table: Query/angle | Intent | What ranks now | Opportunity.
- The content brief(s) from Step 4.
- Offer to: feed these into `/plan-month` (calendar) or write one now with `/write-blog`.

## Anti-patterns

- Copying a competitor or the top result. Match intent, then add real value (E-E-A-T / Helpful Content) - duplication is thin content and gets penalized.
- Chasing trends with no link to the brand's pillars.
- Recommending high-volume keywords whose intent does not fit the business.
- Citing competitor stats as fact without verifying the primary source.

## Engine-wide operating rules

Before acting, follow the cross-cutting red-lines and routing in
`knowledge/playbook.md` (ads = paused drafts only / never spend, SEO human-voice + E-E-A-T
gate, publishing is opt-in, no invented facts, publisher fallback routing). Brand-specific
rules still come from `config/brand.json`; the playbook governs what applies to every brand.
