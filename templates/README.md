# Templates

Output forms the skills fill in. These define **what each deliverable looks like** so
output stays consistent across brands. They are brand-neutral — the skill injects values
from `config/brand.json` at runtime.

| File | Filled by | Deliverable |
|------|-----------|-------------|
| `campaign-brief.template.md` | campaign-planning (`/campaign-plan`) | A full campaign brief |
| `ads-plan.template.md` | paid-ads (`/ads-plan`) | Paid-ad plan + paused-draft summary |
| `social-packet.template.md` | weekly-social-packet (`/post-weekly`) | Weekly LinkedIn + Facebook + card |
| `report.template.md` | analytics-reporting (`/report`) | Marketing performance report |
| `email-sequence.template.md` | email-marketing (`/email`) | Email newsletter / nurture sequence (drafts) |

Input/config templates live in `config/` (`brand.template.json`, `channels.template.json`,
`content-calendar.template.md`). Worked sample outputs live in `examples/`.
