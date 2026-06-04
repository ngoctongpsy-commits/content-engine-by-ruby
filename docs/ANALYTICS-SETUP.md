# Analytics Setup — connect YOUR OWN accounts

The Content Engine ships as a **blank frame**: no accounts, no credentials, no API keys
travel with this plugin. Every data source below is connected by YOU, on YOUR machine,
with YOUR accounts. Skills are tool-agnostic — anything not connected simply reports
"no data" instead of breaking.

> Safety: live configs (`config/brand.json`, `config/channels.json`) and every token file
> are git-ignored. Never commit credentials.

## What connects where (the hybrid map)

| Source | Feeds | How to connect | Cost |
|---|---|---|---|
| Meta Ads | paid social metrics + paused ad drafts | Claude → Settings → Connectors → **Meta Ads** | $0 |
| Google Ads | paid search metrics + paused campaign drafts | Connectors → a creation-capable Google Ads MCP (e.g. MCPBundles) | $0 tier |
| HubSpot | funnel/CRM (leads, deals, CAC) | Connectors → **HubSpot** (free CRM tier) | $0 |
| **Google Analytics 4** | web traffic, conversions | local MCP — guide below | $0 |
| **Search Console** | SEO impressions/clicks/position | local MCP — guide below | $0 |
| Email (Brevo/Mautic) | email metrics + draft sequences | API key in `config/.brevo-key` | $0 tier |
| One-stop alternative | GA4+GSC+social+ads in one | **Windsor.ai** connector (official, Claude directory) | paid (~$19+/mo) |

If you prefer zero setup, use the Windsor.ai connector and skip the rest of this guide.

## GA4 + Search Console — free self-hosted MCPs (~20 minutes, one time)

You will create your own (free) Google Cloud OAuth app and log in once with the Google
account that owns your GA4 property and Search Console site.

### Step 1 — Google Cloud (browser)
1. Go to console.cloud.google.com → create (or pick) a project.
2. Enable 3 APIs: **Google Analytics Admin API**, **Google Analytics Data API**,
   **Google Search Console API** (APIs & Services → Library).
3. **OAuth consent**: Google Auth Platform → Get started → app name + your email →
   Audience: **External** → finish. Then **Audience → Test users → add your own email**.
4. **Create client**: Auth Platform → Clients → Create → type **Desktop app** → Create.
   Copy the **Client ID** and **Client secret** (add a secret if not shown).

### Step 2 — Install uv (runs both MCPs)
- Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Step 3 — One-time Google login
Run the bundled helper (needs Python 3.10+):
```
pip install google-auth-oauthlib
python scripts/google-analytics-oauth-helper.py --client-id YOUR_CLIENT_ID --client-secret YOUR_SECRET --project YOUR_PROJECT_ID
```
A browser opens → log in with the Google account that owns GA4/GSC → "Continue" through
the unverified-app screen (it's YOUR app) → Allow. The helper writes two files to your
home folder: `google-oauth-client.json` and `google-marketing-user.json` (includes a
permanent refresh token).

### Step 4 — Register the MCPs in Claude Desktop
Open your Claude Desktop config (Settings → Developer → **Edit Config**) and add:
```json
{
  "mcpServers": {
    "analytics-mcp": {
      "command": "FULL_PATH_TO_uvx",
      "args": ["analytics-mcp"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "FULL_PATH_TO/google-marketing-user.json",
        "GOOGLE_PROJECT_ID": "YOUR_PROJECT_ID"
      }
    },
    "gscServer": {
      "command": "FULL_PATH_TO_uvx",
      "args": ["mcp-search-console"],
      "env": { "GSC_OAUTH_CLIENT_SECRETS_FILE": "FULL_PATH_TO/google-oauth-client.json" }
    }
  }
}
```
Fully quit Claude (system tray → Quit) and reopen. Settings → Developer should show both
servers running. First Search Console call opens one more browser login — same account.

### Troubleshooting (hard-won)
- **Servers don't appear after restart** → always use the **Edit Config** button to find
  the real config file. Microsoft-Store installs of Claude read a *virtualized* path
  (`...\Packages\Claude_*\LocalCache\Roaming\Claude\`), not `%APPDATA%\Claude`.
- **`spawn uvx ENOENT`** → use the full path to `uvx` (e.g. `C:\Users\YOU\.local\bin\uvx.exe`).
- **"file does not have a valid type"** → your user-credentials JSON must contain
  `"type": "authorized_user"` (the bundled helper adds it automatically).
- **"This email doesn't match a Google Account"** when adding a service account in GA4/GSC →
  don't fight it; use this OAuth route instead. It needs no user-adding at all.

### Verify
Ask Claude: *"List my Search Console properties"* and *"Show my GA4 account summaries"*.
Then run `/report` — the engine pulls everything automatically.
