# Luna Base - Example Profile

This folder is the **live brand profile for Luna Base** (lunabase.ai) - an enterprise AI-native SDLC platform. It demonstrates how a real production tenant of the Content Engine plugin (by Ruby) is configured.

## What is in here

```
examples/luna-base/
├── config/
│   ├── brand.json              Brand voice, palette, validated stats, core arguments
│   ├── channels.json           CMS (Directus), Make.com webhooks, Telegram, schedule
│   └── content-calendar.md     June 2026 calendar + feature rotation 2026-2028
└── sample-output/
    ├── blog-post.html          A real Slot A blog the pipeline produced
    └── linkedin-post.md        Matching LinkedIn company post + first-comment link
```

## How to run this profile

From the plugin root:

```bash
python scripts/publish-blog.py --slot A --profile luna-base --dry-run
python scripts/post-weekly-social.py --profile luna-base
```

The `--profile luna-base` flag tells the scripts to read `examples/luna-base/config/` instead of the root `config/` folder. Secrets must still be present in the same folder (`.cms-token`, `.make-webhook-url`, `.notify-config`) - they are gitignored and never shipped.

## What this profile shows you

- **Electric Mint `#00FFA3`** as primary accent against **Deep Navy `#0A0E27`**
- **Inter** font for headings, **ui-serif/Georgia** for article body
- A real **validated_stats** table (EU AI Act Articles 99(3), 99(4), 113)
- A real **core_arguments** list driving editorial angle
- **Three-account voice strategy** (personal "I", company "we", newsletter contrarian)
- **Six Copilots** of Luna Studio referenced in feature rotation
- A **content-calendar.md** with pillar balance + last-Monday feature rotation through 2028

## Use this as your starting point

Fork `examples/luna-base/` to a sibling folder (`examples/your-brand/`) and edit the three config files. The skills and scripts work unchanged.

Built by Ruby.
