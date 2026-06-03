---
description: Draft email marketing - newsletter, nurture/drip sequence, or broadcast - in the brand voice, staged as DRAFTS for you to review and send. Never sends on its own.
---

# Email

Invoke the `email-marketing` skill.

## Argument parsing

- `/email <type + goal>` -> e.g. `/email nurture, book a demo` drafts that.
- `/email` with no argument -> ask for type (newsletter / nurture / drip / broadcast), goal, audience, and any source asset (a blog or campaign).

## What the skill does

Reads `config/brand.json` (`email` settings, voice, pillars, validated_stats) + `config/channels.json`, then writes the email(s) in the brand voice with subject + A/B variants + preview + body + compliance footer. Stages them as a DRAFT / paused sequence in the connected `~~email` tool (default Brevo / Mautic) or exports paste-ready content if none is connected. SAFETY: drafts only - it never sends, schedules a live send, or imports a list. You review and send.
