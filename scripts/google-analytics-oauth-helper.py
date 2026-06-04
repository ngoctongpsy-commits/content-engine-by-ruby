"""One-time Google login for the Content Engine analytics MCPs.

Creates (in your HOME folder):
  - google-oauth-client.json     : OAuth client file (for the Search Console MCP)
  - google-marketing-user.json   : authorized-user credentials with refresh token (for the GA4 MCP)

Usage:
  pip install google-auth-oauthlib
  python google-analytics-oauth-helper.py --client-id XXX --client-secret YYY --project YOUR_PROJECT_ID

Your credentials stay on YOUR machine. Nothing is sent anywhere except Google's OAuth.
"""
import argparse, json, os, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-id", required=True)
    ap.add_argument("--client-secret", required=True)
    ap.add_argument("--project", required=True, help="Google Cloud project ID")
    args = ap.parse_args()

    home = os.path.expanduser("~")
    client_path = os.path.join(home, "google-oauth-client.json")
    user_path = os.path.join(home, "google-marketing-user.json")

    client = {"installed": {
        "client_id": args.client_id,
        "project_id": args.project,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": args.client_secret,
        "redirect_uris": ["http://localhost"]}}
    with open(client_path, "w") as f:
        json.dump(client, f, indent=2)
    print(f"[1/3] client file written: {client_path}")

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit("Missing dependency. Run:  pip install google-auth-oauthlib")

    flow = InstalledAppFlow.from_client_secrets_file(client_path, scopes=[
        "https://www.googleapis.com/auth/analytics.readonly",
        "https://www.googleapis.com/auth/webmasters.readonly",
        "https://www.googleapis.com/auth/cloud-platform"])
    print("[2/3] opening browser - log in with the Google account that owns GA4/Search Console...")
    creds = flow.run_local_server(port=0, prompt="consent")

    data = json.loads(creds.to_json())
    data["type"] = "authorized_user"          # required by ADC loaders
    data["quota_project_id"] = args.project
    with open(user_path, "w") as f:
        json.dump(data, f, indent=2)
    ok = "yes" if data.get("refresh_token") else "NO (rerun with prompt=consent)"
    print(f"[3/3] user credentials written: {user_path}  (refresh_token: {ok})")
    print("\nDone. Now register the two MCP servers in Claude Desktop - see docs/ANALYTICS-SETUP.md Step 4.")

if __name__ == "__main__":
    main()
