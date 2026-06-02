---
name: paid-ads
description: Plan and draft paid ad campaigns (Meta/Facebook + Google) from a campaign brief - structure, targeting, ad copy, and creatives - and create them as PAUSED drafts via the connected ~~ads MCP for the user to review and launch. Use when the user asks to run/plan ads, create a Facebook or Google ad, set up a paid campaign, or budget paid media. Brand-neutral and config-driven. SAFETY: never launches or spends - drafts only.
---

# Paid Ads (plan + draft, never launch)

Plan paid campaigns and create them as PAUSED DRAFTS for the user to review and launch
themselves. Read `config/brand.json` `ads.*` first. Tool-agnostic `~~ads` (default Meta + Google).

## CRITICAL SAFETY (read first)

- Create campaigns/ad sets/ads in **PAUSED / draft** state ONLY.
- NEVER unpause, launch, set live, raise/confirm budget, or enter payment details. Spending money is ALWAYS the user's manual step in Ads Manager.
- Present the draft + the exact budget/targeting you propose, and tell the user to review + launch. If a tool would spend or go live, stop and ask.

## When to use

- "Run/plan ads", "create a Facebook/Google ad", "set up a paid campaign", "budget for paid media", or the paid portion of a `campaign-planning` brief.

## Step 1 - Read config + inputs

Read `ads.*` (providers, currency, safety, meta/google account ids + defaults), `voice.*`, `palette.*`, `seo.*` (keywords for Google search ads), and any `campaign-planning` brief (objective, audience, message, budget). Ask the user for: platform(s), objective, audience, budget, and the landing URL if not in the brief.

## Step 2 - Plan the ad structure

- **Objective -> structure.** Meta: campaign (objective from `ads.meta.default_objective` or the brief) -> ad set (audience, placements, budget) -> ad (creative). Google: campaign (`search` / `performance_max` / etc.) -> ad group (keywords/themes) -> ad (RSA / assets).
- **Targeting** from the brief (no assumed demographics): audience (interests/segments), GEO (countries/regions/cities/radius), languages, device, and schedule/daypart. For Google search also build a keyword list (intent-first, from `seo` + `competitor-trend-research`), grouped into ad groups, with match types + negatives.
- **Budget**: use the brief/`ads` defaults in `ads.default_currency`; propose daily/lifetime; never exceed what the user set.

## Step 3 - Write copy + creatives (on-brand, truthful)

- Ad copy in brand `voice`: Meta primary text + headline + description; Google RSA = up to 15 headlines (<=30 chars) + 4 descriptions (<=90 chars). No fabricated claims/stats (honor `content_model.stat_rigor`); follow ad-policy basics (no unsupported superlatives).
- Creatives: image via Canva (`~~design`, clickbait rules + correct sizes), video via Higgsfield (`video-production`) for video placements. Multiple variants for testing.

## Step 4 - Create PAUSED drafts via ~~ads

- **Meta** (connected): use the Meta Ads tools to create the campaign, ad set, creative, and ad - all PAUSED. List accounts first (ads_get_ad_accounts) if `ads.meta.ad_account_id` is empty. Show the created draft ids + a preview.
- **Google**: if a CREATION-CAPABLE Google Ads MCP is connected (official MCP with ADS_MCP_ENABLE_MUTATIONS=true, or MCPBundles / Synter), create the FULL campaign PAUSED - campaign + budget + ad group(s) + keywords (match types + negatives) + RSA ads + GEO targeting (regions/locations) + AUDIENCE targeting + device/daypart as specified. If only the read-only official MCP is connected, instead EXPORT a ready-to-paste plan (same fields incl. geo/audience) for the Google Ads UI.
- If no `~~ads` MCP is connected for a platform, deliver the full plan + copy + creatives and tell the user to connect the MCP or paste into the platform.

## Step 5 - Hand off

Summarize: what was drafted (ids/links), proposed budget + targeting, and the explicit next step: "Review in Ads Manager, confirm budget, and launch yourself." Offer A/B variant ideas and a measurement plan (tie KPIs to the campaign brief).

## Anti-patterns

- Launching, unpausing, confirming budget, or entering payment - NEVER. Drafts only.
- Assumed audience/industry; keyword stuffing; fabricated claims/stats; policy-risky superlatives.
- Creating live spend "to test". Always paused; the user launches.

## Engine-wide operating rules

Before acting, follow the cross-cutting red-lines and routing in
`knowledge/playbook.md` (ads = paused drafts only / never spend, SEO human-voice + E-E-A-T
gate, publishing is opt-in, no invented facts, publisher fallback routing). Brand-specific
rules still come from `config/brand.json`; the playbook governs what applies to every brand.
