# Publishing & Updating this plugin (marketplace flow)

This repo is BOTH the plugin and a Claude plugin marketplace
(`.claude-plugin/marketplace.json`, marketplace name `ruby-content-tools`). Subscribe once,
then every future change is a one-click update in the Claude app.

## The golden rule of updates

The Claude app shows an update ONLY when the `version` number goes up. Every change must bump
the version in TWO files to the same value:
- `.claude-plugin/plugin.json` -> "version"
- `.claude-plugin/marketplace.json` -> plugins[0]."version"

Semver: 0.2.0 -> 0.2.1 (small fix) -> 0.3.0 (feature) -> 1.0.0 (stable).

## One-time setup (~5 min)

1. Create an empty GitHub repo, e.g. `content-engine-by-ruby` (public or private both fine).
2. Push this repo:
   ```
   cd content-engine-by-ruby
   git remote add origin https://github.com/<your-account>/<repo>.git
   git push -u origin main --tags
   ```
3. In the Claude desktop app: Settings -> Plugins/Marketplaces -> Add marketplace -> paste the
   repo URL. The plugin appears -> Install.
4. Remove any older copy (the 0.1.0 installed from elsewhere) so there is a single source.

## Recurring update loop (each change)

1. Ask Claude to make the change AND bump the version in both files.
2. Claude gives you the updated files / a fresh repo zip.
3. From your local clone:
   ```
   git add -A
   git commit -m "vX.Y.Z - what changed"
   git tag vX.Y.Z
   git push --tags
   ```
4. The Claude app shows "Update available" -> click Update. Synced on every machine.

## Notes

- Live per-tenant config (`config/brand.json`, secret token files) is gitignored and never
  published. The repo ships only templates + the two examples (luna-base, restaurant).
- Clone to a normal local folder (not a network drive); git is unreliable on network mounts.
