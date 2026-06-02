# Canva images (thumbnail + social) - shared guide

Used by BOTH the blog skill (thumbnail) and the weekly-social skill (LinkedIn + Facebook).
Read `config/brand.json` `format.images` first.

## When this applies

Only when `format.images.provider` is `"canva"`. If it is `"svg"`, skip this file and use
the legacy inline SVG path. In-article blog figures are ALWAYS SVG and are NOT affected by
this setting - this guide is only for the thumbnail and the social cards.

## The rule

Claude (in the session) generates the image with the connected Canva tools, then AUDITS and
CLEANS its text so the only words are a correct headline + the `company.domain` wordmark,
then exports a PNG at the exact size to a sidecar path the publish/post script reads.
Do not hardcode a specific Canva tool id - use whatever Canva tools are connected this session.


## Steps (per image)

1. Read the target size from `format.images.sizes` (blog thumbnail `blog_thumbnail_px` 1200x630; LinkedIn `linkedin_px` 1200x1200; Facebook `facebook_px` 1080x1350).
2. Generate the design (generate-design) with a prompt for: a strong visual + ONE short headline + the wordmark `company.domain` in a bottom-corner footer, and NO other text. See "Visual + text" below.
3. Convert the chosen candidate to a real design (create-design-from-candidate). Resize to the exact size if needed (resize-design custom WxH).
4. AUDIT + CLEAN the text (this is the step that kills gibberish like "billstepping"):
   - Open it: start-editing-transaction (it returns every text element with its `element_id` and current text + a preview thumbnail).
   - Keep exactly TWO text elements: the HEADLINE (header) and ONE wordmark reading exactly `company.domain` (footer).
   - If the headline wording is wrong/mangled, fix it: perform-editing-operations -> replace_text.
   - If a wordmark element is gibberish (e.g. "billstepping"), fix it to `company.domain` with replace_text; if there is ALSO a correct `company.domain` element, delete the junk one with delete_element.
   - Delete every other stray text element (extra labels, taglines, duplicate wordmarks, numbers) with delete_element.
   - Commit: commit-editing-transaction. (Changes are lost if not committed.)
5. Export PNG at the exact size (export-design, type png, width/height).
6. Save the PNG to the sidecar path (see "Output paths") so the publish/post script picks it up.


## Visual + text (header headline OK; the ONLY wordmark is company.domain, in the footer)

- VISUAL: ONE bold focal subject / metaphor for the piece, high contrast, palette colors on a dark/saturated background, dramatic premium mood.
- HEADER: one short, bold clickbait headline (<= 8 words) tied to the real angle. Allowed and encouraged.
- FOOTER: the ONLY brand text is the wordmark, EXACTLY `company.domain` (e.g. "lunabase.ai"), small, in a bottom corner. No tagline, no second wordmark.
- NOTHING ELSE: no random words, no labels, no numbers unless real, no misspelled brand text.

Why the audit step exists: the generator often mis-spells small text and adds junk wordmark
elements (it once produced "billstepping"). Text in these designs is EDITABLE, so always
open the design and fix/delete text instead of trusting the generator's spelling. There is
no "add new text" API operation - so let the generator place the headline + wordmark, then
correct them.


## Output paths

- Blog thumbnail: `outputs/blogs/draft-YYYY-MM-DD-slot-{X}-{slug}.thumb.png`
- Weekly social LinkedIn: `outputs/social/pending/weekly-YYYY-MM-DD.linkedin.png`
- Weekly social Facebook: `outputs/social/pending/weekly-YYYY-MM-DD.facebook.png`

## Self-check before finishing

- [ ] PNG is the exact size from `format.images.sizes`
- [ ] Headline (header) is correct, short (<= 8 words), legible, tied to the real angle
- [ ] Exactly ONE wordmark, reading exactly `company.domain`, in a bottom-corner footer
- [ ] No gibberish, no junk/extra text, no misspelled brand text, no fabricated numbers
- [ ] Edits were committed (commit-editing-transaction) before export
- [ ] Saved to the correct sidecar path
