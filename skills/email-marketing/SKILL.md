---
name: email-marketing
description: Draft email marketing - newsletters, nurture sequences, drip/onboarding flows, and broadcast campaigns - in the brand's voice, then stage them as DRAFTS for the user to review and send. Use when the user asks to write a newsletter, an email sequence, a nurture/drip/onboarding flow, a launch email, or to turn a blog/campaign into email. Brand-neutral and tool-agnostic (~~email, default Brevo/Mautic); never sends on its own - it drafts and hands off for approval. Closes the nurture loop after content is published.
---

# Email Marketing (nurture)

Turns the engine's content + campaigns into email that nurtures and converts. Brand-neutral:
voice, offers, audience, and cadence come from config. **SAFETY: this skill DRAFTS only - it
never sends, never schedules a live send, never imports a list.** Sending is the user's action.

## When to use
- Newsletter, nurture/drip/onboarding sequence, launch/announcement email, re-engagement, "biến bài blog này thành email".

## Step 1 - Read config + inputs
Read `config/brand.json`: `email.*` (provider, from-name/address, sequence defaults, cadence, compliance footer), `voice.*` (tone, forbidden phrases/chars), `content_model.pillars`, `validated_stats`, `core_arguments`. Read `config/channels.json` for the email destination/provider. Ask (if not given): email TYPE (newsletter / nurture / drip / broadcast), GOAL, AUDIENCE/segment, and any source asset (a blog, a campaign, an offer).

## Step 2 - Choose the structure
- **Newsletter**: 1 lead story + 2-3 short items + 1 CTA.
- **Nurture/drip**: a numbered sequence (e.g. 3-5 emails) with one job each (welcome → value → proof → offer → nudge), spacing from `email.sequence_defaults`.
- **Broadcast/launch**: single focused email, one CTA.
Map each email to a pillar + the funnel stage.

## Step 3 - Write each email (brand voice)
For every email produce: **subject line** (+ 1-2 A/B alternates), **preview text**, **body** (skimmable, one clear CTA), and **plain-text fallback**. Honor `voice` (no forbidden phrases/chars - EVAL A3) and `content_model.stat_rigor` (only `validated_stats`/cited numbers - EVAL A4). Include the brand's compliance footer + an unsubscribe placeholder (required - legitimate marketing email).

## Step 4 - Stage as drafts (never send)
Write the sequence to `outputs/email/<name>/` using `templates/email-sequence.template.md`. If an `~~email` MCP/connector is present (Brevo, Mautic, Make.com), create the campaign/sequence as a **DRAFT / paused** in that tool for the user to review and send. If none is connected, output paste-ready content + a send checklist. Either way: **never trigger a live send**.

## Step 5 - decision_trace + hand-off
End with a short trace: email type, segment, pillar mapping, provider used (or "export only"), draft location. Offer to: feed performance back via `/report`, align with `/campaign-plan`, or repurpose into `/post-weekly`.

## Anti-patterns
- Sending, scheduling a live send, or importing/uploading a contact list (all forbidden - user does these).
- Spam patterns (misleading subject, no unsubscribe, fake urgency).
- Fabricated stats/claims; forbidden phrases; assumed industry/audience.

## Worked example
Input: `/email nurture, goal=book a demo, from the launch campaign` for a B2B brand.
Output: a 4-email drip (Welcome → Problem+proof → Case/feature → Demo CTA), each with subject + 2 A/B variants + preview + body + footer; staged as a PAUSED sequence draft in Brevo (or exported if not connected); trace: type=nurture, segment=new signups, provider=Brevo draft, no live send.

## Engine-wide operating rules
Before acting, follow `knowledge/playbook.md` (publishing/sending is opt-in and user-triggered, no invented facts, brand voice rules) and `knowledge/FAILURE-MODES.md`. Brand specifics come from `config/brand.json`; never hardcode offers/voice.
