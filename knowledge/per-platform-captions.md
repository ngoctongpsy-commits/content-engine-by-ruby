# Per-platform caption strategy

Cross-posting the SAME original video to multiple platforms does NOT cut reach (different audiences, separate
algorithms). What raises reach is ADAPTING the caption per platform. The penalty surface is for non-native /
watermarked / recycled content within one platform, not for the same idea appearing elsewhere. So: one render,
several captions. Write one caption file per voice and let `social-distribution` send the right one per channel.

| Caption file     | Channels                         | Voice |
|------------------|----------------------------------|-------|
| caption-fb.txt   | facebook_reel, instagram_reel    | Punchy, human, emotional hook; 1-3 hashtags; <=1 soft CTA. Never open with "Most people...". |
| caption-li.txt   | linkedin_video (Company page)    | Professional, insight-led; reflective/strategic COMPANY voice; minimal hashtags; the concrete takeaway. |
| caption-personal.txt | linkedin_personal (founder)      | FIRST-PERSON founder sharing ("I", "we"): a real builder experience/lesson behind the topic. Warm, story-like, 1-2 short paragraphs, minimal/no hashtags, never salesy. |
| caption-yt.txt   | youtube_short                    | First line = a searchable TITLE with the key keyword (<=100 chars), then a 2-3 line description + a few tags incl #Shorts. |

The channel->caption-file mapping lives in `config/channels.json` (distribution.caption_files). YouTube also
needs a separate short `title` (first line of caption-yt, <=100 chars) — the distributor derives it automatically.
