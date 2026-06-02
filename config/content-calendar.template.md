# Content Calendar (template)

Copy to `config/content-calendar.md` and fill. Each row is one piece. The **Format** column
makes a row a blog or a VIDEO; for video rows set the **Platform** (drives aspect ratio).

## Week of YYYY-MM-DD

| Date | Slot | Format | Platform | Pillar | Topic | Target keyword | Notes |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | A | blog |  | <pillar> | <topic> | <keyword> |  |
| YYYY-MM-DD | B | blog |  | <pillar> | <topic> | <keyword> |  |
| YYYY-MM-DD | C | video | reels | <pillar> | <short hook topic> | <keyword> | 9:16, <=15s |

- **Format** = `blog` or `video`. Empty defaults to `blog`.
- **Platform** (video only) = one of your enabled `video.platforms` (tiktok / reels / shorts / facebook / linkedin / youtube). Aspect comes from config.
- A `video` row is produced by the `video-production` skill in calendar mode. With `video.automation.mode = review`, it auto-creates the clip into `outputs/video/pending` and waits for your approval before posting (it does NOT auto-post).

## Feature Rotation (last Monday each month)

| Month | Last Monday | Angle | Specific |
|---|---|---|---|
| YYYY-MM | YYYY-MM-DD | <angle> | <topic> |
