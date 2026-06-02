# Content Engine — Operating Playbook

This is the engine's **cross-cutting playbook**: the rules that hold true for *every*
brand the engine runs. Brand-specific knowledge (voice, colors, pillars, thresholds,
accounts) lives per-tenant in **`config/brand.json`** and **`config/channels.json`** —
the skills read those at runtime and must never hardcode them. This playbook captures
the rules that sit *above* any single brand.

> How the two layers relate:
> - **This playbook** = engine-wide red-lines + routing that apply to all tenants.
> - **`config/brand.json`** = the edge for ONE brand (voice, forbidden phrases, pillars,
>   image/video/SEO/ads settings, thresholds). Filled per company from `brand.template.json`.
> - When they ever conflict, the **safety red-lines in this playbook win**.

---

## 1. Safety red-lines (never cross — apply to every brand)

- **Paid ads = PAUSED drafts only.** The engine creates campaigns/ad sets/ads in a
  **paused** state. It NEVER launches, NEVER raises budget, NEVER spends. Launching is
  always the user's manual action in Ads Manager. (`ads.safety.create_paused=true`,
  `never_launch_or_spend=true`.)
- **No credentials, no account creation.** The engine never enters passwords, API keys,
  OAuth, or payment details. Each MCP/connector is authenticated by the user with their
  own account.
- **Publishing is opt-in.** Social/blog publishing only fires through a connector the user
  has wired (Make.com / Upload-Post / CMS). Nothing is posted silently; review modes
  (e.g. `video.automation.mode=review`) save drafts for approval first.
- **No invented facts.** Stats, prices, and claims in any deliverable must be verifiable.
  Use `config/brand.json` `validated_stats` / `core_arguments`; if a number isn't verified,
  don't print it. (See the SEO human-voice + E-E-A-T gate.)

## 2. SEO quality gate (every published blog must pass)

Before a blog is considered done, run it through `seo-optimization`:
- **Indexability** — unique value, not thin/duplicate, not scaled-content-abuse.
- **E-E-A-T** — experience, expertise, authority, trust signals present.
- **Helpful Content** — written for people first, satisfies search intent.
- **Human voice** — no AI boilerplate, no forbidden phrases/chars from `brand.json.voice`.
- Verdict is **PASS / FIX**; a FIX verdict blocks publishing until resolved.

## 3. Brand compliance (every visual + word)

- Layout, colors, fonts, hero/body style come from `config/brand.json.format` — the engine
  is a **blank canvas**; no company's look is hardcoded.
- Voice obeys `voice.accounts`, `forbidden_phrases`, `forbidden_chars`.
- Images: only the wordmark from `images` config may appear as brand text; no junk/garbled
  text baked into AI images (audit + clean via the design connector).

## 4. Publisher routing (resilient multi-platform)

- Each channel in `config/channels.json` has a `publisher` + `fallback_publisher`.
- **Default Make.com** for the easy platforms (LinkedIn, Facebook, Instagram, YouTube).
- **Upload-Post as fallback** for the hard ones (TikTok, Threads, X) — cheapest path
  (free 10/mo). Auto-failover: if the primary publisher errors, try the fallback.
- Accounts/webhooks live in the user's router, **never in the plugin**.

## 5. Cost discipline (Rule 3)

- Always prefer the **$0 / open-source / free-tier** path first, then the cheapest paid
  option only if needed. Connector choices and their costs are documented in `CONNECTORS.md`.
- Video (Higgsfield) and ads spend are user-funded and user-triggered.

## 6. Multi-business model

- One engine, many brands. Each business = its own **config profile** pointing to its own
  accounts/router. Switching brand = switching `config/brand.json` + `config/channels.json`,
  not editing skills.

---

## TODO — Andy to fill / confirm per rollout

- [ ] Confirm the default publisher per channel for each business (Make vs Upload-Post).
- [ ] Confirm per-brand daily ad budget caps (VND) used in paid-ads drafts.
- [ ] List each business's verified stats pool in `brand.json.validated_stats`.
- [ ] Confirm the SEO region/language per brand in `brand.json.seo`.
- [ ] Note any brand-specific red-lines beyond the engine-wide ones above.
