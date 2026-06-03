# Google SEO + Quality Standards (so AI-written content gets INDEXED and RANKS)

Every blog this engine produces must (1) be technically INDEXABLE by Google, (2) pass Google's
quality + helpfulness bar (E-E-A-T + Helpful Content system) with genuine HUMAN VOICE, and
(3) target keywords by search INTENT. Google permits AI authoring as long as the result is
helpful, original, and people-first; it penalizes "scaled content abuse" (mass low-value AI
pages). Rule of thumb: AI for speed + structure, then add real expertise, sources, and voice.

Read `config/brand.json` `seo` for region, language, E-E-A-T identity, and indexing settings.

## A. Indexability gate (technical - if this fails, it cannot rank at all)

- Page returns HTTP 200, not blocked by robots.txt, no `noindex` (handled on publish side).
- Exactly ONE `<h1>`. Clean, readable URL slug containing the primary keyword.
- `<title>` 50-60 chars including the primary keyword; meta description 150-160 chars with intent + a reason to click.
- Canonical URL set; Open Graph + Twitter Card; JSON-LD `Article` with a real `author` and `publisher`.
- The post is a canonical, indexable URL that belongs in the XML sitemap; it links to and from related posts (no orphan).
- Every image has descriptive alt text.
- Note: meeting these makes a page ELIGIBLE for indexing; indexing is never guaranteed. Quality (below) decides whether it ranks.

## B. E-E-A-T (Experience, Expertise, Authoritativeness, Trust)

- EXPERIENCE: include first-hand, specific detail a real practitioner would know - a concrete scenario, a real example, a number from actual practice. This is what most separates the piece from generic AI text.
- EXPERTISE: a named author byline with a real role/credentials; JSON-LD `author` = a real Person/Organization from `seo.eeat`. Demonstrate accurate depth on the topic.
- AUTHORITATIVENESS: cite credible primary sources for claims and stats; link out where it helps the reader; author bio / org "About" is reachable.
- TRUST: factual accuracy, no fabricated numbers (honor `content_model.stat_rigor`), clear publisher identity, reachable contact/About, and clickbait that the body actually delivers on.

## C. Helpful, people-first content (Helpful Content system, now part of core ranking)

- Written for a specific human audience, not for the algorithm.
- Fully satisfies the search intent - the reader should not need to go back and click another result.
- Adds ORIGINAL value: insight, analysis, first-hand experience, or data beyond restating what is already on page 1.
- Makes "who, how, and why" clear (who made it, how it was produced, why it exists).

## D. AI-content compliance (avoid the scaled-content-abuse penalty)

- Use AI for speed and structure, then add human expertise, original insight, verified sources, natural language, and editorial judgement.
- Do NOT mass-produce thin, near-duplicate pages; each piece must stand on unique value.
- Never publish content "primarily to manipulate rankings" with little value for users.

## E. Human-voice gate (so it does not read as generic AI)

- Vary sentence length and rhythm; mix short, punchy lines with longer ones.
- Use concrete, specific nouns and real examples, not vague filler.
- Take a clear point of view where appropriate; use first-hand framing.
- NO `voice.forbidden_phrases.ai_tells`, no generic openers, no em/en dash if forbidden.
- "Read aloud" test: would a knowledgeable human actually say this? Cut padding such as "In today's fast-paced world", "plays a crucial role", "it is important to note", "when it comes to".

## F. Keyword + search intent (intent-first)

- Classify intent: informational / commercial / transactional / navigational. Match the content TYPE to what already ranks for the query (guide vs comparison vs product page) - search the query and look at the top results.
- Primary keyword in: title, H1, URL slug, first 100 words, and naturally throughout (no stuffing / no unnatural density).
- Use secondary, long-tail, and question ("how/what/why") variants naturally in H2/H3.
- Put a direct, clear answer in the first 1-2 paragraphs (this also makes it extractable for AI Overviews).
- Internal links: connect the post to related pillar/cluster pages with descriptive anchor text.

## Sources (verified June 2026)

- Google Search Central: "Creating Helpful, Reliable, People-First Content".
- Google Search Central: "Search Essentials - Technical requirements" (indexability).
- Google Search Central blog: guidance about AI-generated content.
- Google Search Central: "General Structured Data Guidelines".
- Industry analysis of the March 2026 core update + scaled-content-abuse policy and 2026 E-E-A-T / intent-first keyword practice.
