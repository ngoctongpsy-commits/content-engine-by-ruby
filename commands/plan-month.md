---
description: Generate or update the next 30-day content calendar. Invokes the content-planning skill.
---

# Plan Month

Invoke the `content-planning` skill to produce a 30-day calendar with 3 slots per day (A, B, C), balanced across pillars, with feature rotation suggestions appended for the last Monday of each month.

## Inputs to read

- `config/brand.json` -> company context, core arguments
- `config/channels.json` -> publish slot times
- `config/content-calendar.md` (if exists) -> recent topics to avoid repeating

## What to ask the user

Only if NOT already in the existing calendar:

1. Pillars (3-5 core domains). Skip if calendar already lists pillars.
2. Target month to plan (default: next month from today).

Do not ask about anything else - the skill handles slot mapping, keyword variety, rotation rules.

## Output

Write the calendar to `config/content-calendar.md`. If a calendar already exists, APPEND the new month as a new section - never overwrite past months.

## After writing

Show the user a summary:

- N blog drafts scheduled across N days
- Pillar distribution (count per pillar)
- Feature rotation for last Monday of each month covered
- Suggested next command: `/write-blog A` to draft the first slot

Built by Ruby.
