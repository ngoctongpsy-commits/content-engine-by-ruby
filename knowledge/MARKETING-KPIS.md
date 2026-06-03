# Marketing KPIs & Report Standard (the analytics rulebook)

The rulebook `analytics-reporting` reads to build a **complete** marketing report. Completeness
is guaranteed by STRUCTURE, not memory: anchor on (1) the 8-section report anatomy and (2) the
AARRR x channel matrix. Every report fills all 8 sections; every metric cell is filled or marked
**N/A** / **no data** — never invented (EVAL A4/A7).

> Benchmarks are 2026 reference values; always compare to the brand's own `analytics` targets first.

---

## PART 1 — The 8 sections every report must have (Anchor 1)
1. **Executive summary** — 5-9 core KPIs only; performance vs target, revenue/ROI, biggest move, top action.
2. **Goals vs KPIs** — target / actual / delta / status (GREEN-YELLOW-RED) from `analytics.kpi`.
3. **Channel performance** — SEO/web, social, email, paid, video, content (Part 2 matrix).
4. **Funnel & lead/conversion** — stage-by-stage conversion + velocity (Part 3).
5. **Attribution** — which channels created vs closed demand (Part 4).
6. **Budget & ROI** — spend by channel, CAC, ROAS, ROI.
7. **Insights** — what the numbers MEAN (not just restate them).
8. **Recommendations & next steps** — 3-6 prioritized actions, each naming the next skill.

## PART 2 — Metric completeness matrix (Anchor 2: AARRR x channel)
Fill every cell or mark N/A. Columns = channels; rows = AARRR stage + foundation.

### Acquisition (attract)
- **SEO/Web:** organic clicks, keyword rankings, impressions (GSC)
- **Social:** reach, impressions, follower growth (1-2%/mo avg, >5% strong)
- **Email:** list / subscriber growth
- **Paid:** impressions, CTR (~1-3%), CPC, CPM, impression share
- **Video:** views, watch time, view rate

### Activation (first meaningful engagement)
- **SEO/Web:** avg engagement time (GA4; bounce rate retired 2023), scroll depth, pages/session
- **Social:** engagement rate (TikTok 4%+, IG 2%+, LinkedIn 3%+), comments, saves
- **Email:** open rate (~20.7%, Apple MPP inflates +15-20pts), CTOR (~6.8%)
- **Paid:** landing-page conversion rate, CTR
- **Video/Content:** completion rate (TikTok aim 75%+), time on page, assisted conversions

### Retention (come back)
- returning users · repeat engagement · email active-subscriber rate · retargeting performance · subscriber/cohort retention

### Referral (spread)
- backlinks (SEO) · shares, mentions, **share of voice**, sentiment (social) · forwards (email) · video shares

### Revenue (outcome)
- **SEO/Web:** organic conversions (~2.7-3% benchmark), organic revenue
- **Social:** social conversions, revenue per post
- **Email:** conversions, **revenue per email** (ROI $36-42/$1; flows ~41% of revenue)
- **Paid:** **ROAS**, CPA/CPL, conversions
- **Video:** conversion assists

### Foundation (is it even measurable?) — check FIRST
- UTM tags on every owned link + consistent campaign naming
- GA4 key events marked as conversions; goals defined
- Pixel + **server-side/CAPI** (client-side misses 30-50%); bot + internal-IP filtering
- A single data layer / source of truth
> If the foundation is missing, say so — numbers above it are unreliable.

## PART 3 — Funnel / pipeline + business KPIs (cross-cutting)
- **Funnel conversion by stage (B2B benchmarks):** Visitor->Lead 1-5% · Lead->MQL 25-35% · MQL->SQL 13-26% (behavioral 39-40%) · SQL->Opp 50-62% · Opp->Won 15-30%.
- **Pipeline velocity** = (Opps x Avg deal value x Win rate) / Sales-cycle length; track days per stage.
- **2026 shift:** "MQL is dead" -> prioritize **SQLs, pipeline created, CAC payback**.
- **Unit economics:** CAC · **CAC payback (months)** · CLV/LTV · LTV:CAC · ROI · ROAS.
- **Retention:** churn / logo churn · repeat-purchase · cohort retention · NPS/CSAT.
- **E-commerce (if relevant):** AOV, cart-abandonment, revenue per visitor.

## PART 4 — Attribution (don't trust one model)
- **Models:** first-click (demand creation), last-click (closing), linear, time-decay, position-based, **data-driven** (GA4/Google Ads).
- **MMM** (media mix modeling) for strategy; **incrementality tests** (exposed vs control) to prove causal lift.
- **2026 best practice = UMM** (Unified Marketing Measurement): MTA for tactics + MMM for strategy, because privacy/cookie loss hides 30-45% of touches.
- Report "marketing-influenced" and "marketing-originated" revenue, not just lead counts.

## PART 5 — Principles (apply to every report)
- **Vanity vs actionable:** demote follower count / raw impressions; lead with conversion, CAC, LTV, revenue.
- **Leading vs lagging:** pair early signals (traffic, engagement) with outcomes (revenue, retention).
- **Privacy reality:** Apple MPP inflates email opens; GA4 uses engagement time not bounce; dark/AI-search traffic under-counts referrals.
- **Benchmark + target:** every metric needs a target (from `analytics.kpi`) or a 2026 benchmark; a number with no target is noise.
- **Never fabricate:** missing source = "no data". Honesty over completeness theater.

## HYBRID data sources (where each matrix column comes from)
- **SEO/Web** -> official Google GA4 MCP + mcp-gsc (Search Console) - $0 self-host
- **Social** -> open-source social MCP (own API keys) or Windsor.ai (optional paid)
- **Email** -> Brevo (existing account)
- **Paid** -> Meta Ads MCP + Google Ads MCP (connected, $0)
- **Funnel/CRM** -> HubSpot MCP (free CRM tier)
- **Always** -> engine publish logs (outputs/, $0)
Missing source = "no data" - never estimate.

## COMPLETENESS CHECKLIST (run before finalizing a report)
- [ ] All 8 sections present?
- [ ] Foundation checked (tracking working)?
- [ ] Every AARRR row covered for each ENABLED channel (or N/A)?
- [ ] Funnel stages + velocity + CAC payback included (if B2B)?
- [ ] Attribution stated (which model)?
- [ ] Business KPIs (CAC, CLV, ROI/ROAS, churn) present?
- [ ] Every number has a target/benchmark, or is marked "no data"?
- [ ] Vanity metrics demoted; insights + next steps written?
