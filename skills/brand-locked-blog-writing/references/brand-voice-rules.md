# Brand Voice Rules - Read from config/brand.json `voice`

All voice rules are configurable. Read them from `config/brand.json` `voice.*`. Nothing
here is specific to any one company.

## Account model (configurable)

A brand defines one or more "accounts" it posts as, under `voice.accounts`. The active
account for blog writing is `voice.default_account`. The template ships an EXAMPLE
three-account structure (personal / company / newsletter), but a brand may keep one,
rename them, or add others.

Each account has:
- `pronoun` - "I" or "we"
- `tone` - descriptive string (use this; do not assume a register like "CTO-to-CTO")
- `promote_product_directly` - boolean

Use `voice.accounts[voice.default_account]` by default. Switch only if the user explicitly asks for a different account's voice (e.g. a founder/personal post).

## Forbidden phrases (hard reject)

- `voice.forbidden_phrases.ai_tells` - LLM tells that signal "AI wrote this." Rewrite if any appear.
- `voice.forbidden_phrases.overclaims` - puffery / generic marketing. Use specific claims instead.
- `voice.forbidden_phrases.generic_openers` - formulaic starters. Replace with specific hooks.

## Approved exception phrasings

`voice.required_phrasings.approved_only_phrasings` - phrasings that look like overclaims but are explicitly approved for this brand. Use exactly as listed.

## Forbidden characters

`voice.forbidden_chars` - `em_dash`, `en_dash`, `emoji`. When true, never use them. (A brand can set any to false.)

## Research density per slot

Scale research depth with the slot's word count from `content_model.slots`, not with a fixed B2B model:
- Longest slot: deepest research, most named sources + quotes.
- Medium slot: moderate sourcing.
- Shortest slot: lighter, timelier sourcing.

Quality bar stays equal across slots; only density scales.

## Stat citation rules (honor content_model.stat_rigor)

For every numeric claim (`\d+%`, `\d+x`, `$\d+[KMB]?`):
- `strict`: must be in `validated_stats.entries`, or cited inline to a real source.
- `cited`: allowed if cited inline `(Source: <name>, <year>)` to a real source.
- `off`: no enforcement (still never fabricate).

Never invent stats.

## Author byline

`<meta name="author">` and JSON-LD Person schema use `voice.accounts[active].author_name` if defined, else `company.name`.

## Anti-patterns

- Mixing voices within a single post - pick one account, stick to it.
- Generic LLM openers.
- Reflexive "we" when writing a personal-voice post (should be "I").
- Assuming an industry register the brand never set.
