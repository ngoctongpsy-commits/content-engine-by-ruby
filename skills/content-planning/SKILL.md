---
name: content-planning
description: Generate or update a 30-day content calendar with topics balanced across the brand's own pillars. Reads config/brand.json for company context, content_model (slots, pillars, feature angles) and config/channels.json for schedule. Triggered when the user asks to "plan content", "make content calendar", "what should I write next month", or similar. Output is a markdown calendar with date + slot + pillar + topic + target keyword rows. Brand-neutral: pillars and angles come from config, never hardcoded.
---

# Content Planning Skill

Brand-neutral planner. It does NOT assume any industry. Pillars, slot meanings, and
feature angles all come from `content_model` in `config/brand.json`.

## When to use

User asks to: plan next month's content, update the calendar, suggest topics, decide what to write next, or audit pillar balance.

## Workflow

### Step 1 - Read brand context

Read `config/brand.json`:
- `company.name` + `company.tagline` - what the brand is about
- `content_model.pillars.list` - the brand's content domains (see Step 2 if empty)
- `content_model.slots.<A|B|C>` - the `label` + `intent` + word counts for each daily slot (brand-defined; do NOT assume foundational/comparison/news)
- `content_model.feature_rotation_angles.list` - the brand's recurring promo angles
- `core_arguments.list` - optional thesis statements
- `voice.accounts.<voice.default_account>.tone` - desired tone

Read the active `config/channels.json` (or template) for `schedule.blog_publish_slot_a/b/c.cron`.

### Step 2 - Establish pillars

If `content_model.pillars.list` is non-empty, use those pillars. If empty, ask the user for 3-5 core content domains for their brand, then offer to save them into `content_model.pillars.list`.

### Step 3 - Read existing calendar

If `config/content-calendar.md` exists, read it. Note pillars in rotation, recent topics, and sub-topic exhaustion (avoid the same sub-topic 3 weeks running). If none exists, start fresh.

### Step 4 - Generate next 30 days

Three slots per day, using each slot's brand-defined intent from `content_model.slots`:

```markdown
## Week of YYYY-MM-DD

| Date | Slot | Pillar | Topic | Target keyword | Notes |
|---|---|---|---|---|---|
| YYYY-MM-DD | A | <pillar> | <one-line topic fitting slot A intent> | <SEO keyword> |  |
| YYYY-MM-DD | B | <pillar> | <one-line topic fitting slot B intent> | <SEO keyword> |  |
| YYYY-MM-DD | C | <pillar> | <one-line topic fitting slot C intent> | <SEO keyword> |  |
```

### Step 5 - Apply rotation rules

- **Pillar balance:** distribute evenly across the brand's pillars over 30 days.
- **Slot match:** each topic must fit that slot's `intent` from `content_model.slots` (whatever the brand defined - e.g. Cornerstone vs Practical vs Timely, or a restaurant's Story vs Menu vs Event).
- **Anti-cannibalization:** no two posts target the same SEO keyword within the 30-day window.
- **Mix:** balance evergreen and timely angles per pillar.

### Step 6 - Feature rotation (monthly)

If `content_model.feature_rotation_angles.list` is non-empty, append a rotation for the last Monday of each month, cycling through the brand's own angles:

```markdown
## Feature Rotation (last Monday each month)

| Month | Last Monday | Angle | Specific |
|---|---|---|---|
| YYYY-MM | YYYY-MM-DD | <angle from content_model.feature_rotation_angles.list> | <specific topic> |
```

If the list is empty, skip feature rotation (do not invent B2B angles like "customer_proof" or "compliance" unless the brand defined them).

### Step 7 - Output

Write the calendar to `config/content-calendar.md` (or append a new section). Notify the user with a short summary.

## Anti-patterns

- Assuming a B2B/SaaS frame. Slots and angles are whatever the brand defined.
- Generic topics ("AI is the future"). Be specific.
- Same pillar 3 days in a row.
- Inventing feature angles the brand never configured.
- More than ~30% of slots on the shortest/timeliest slot - keep evergreen depth.
