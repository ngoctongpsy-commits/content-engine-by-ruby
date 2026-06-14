#!/usr/bin/env python3
"""
distribution-tick.py — run every ~15 min (scheduled). Config-driven.
  1) If approval enabled: read Telegram; 'post' approves ALL awaiting items, 'skip' cancels them
     (only replies that arrived AFTER an item was proposed affect it).
  2) Publish APPROVED items whose post_at_utc has arrived -> Make webhook (per channel) -> Telegram confirm.
Idempotent: awaiting -> approved -> posted/skipped. Reads config/channels.json (distribution + social).

Usage: python distribution-tick.py [--profile NAME]
"""
import argparse, glob, json, os, sys, urllib.request, urllib.parse
from datetime import datetime, timezone
from pathlib import Path


def plugin_root() -> Path:
    here = Path(__file__).resolve()
    for a in [here.parent, *here.parents]:
        if (a / ".claude-plugin" / "plugin.json").exists():
            return a
    return here.parent.parent


def cfg_dir(root, profile):
    return (root / "examples" / profile / "config") if profile else (root / "config")


def load_channels(root, profile):
    p = cfg_dir(root, profile) / "channels.json"
    if not p.exists():
        sys.exit("channels.json not found: %s" % p)
    return json.load(open(p, encoding="utf-8"))


def read_secret(root, profile, filename):
    p = cfg_dir(root, profile) / filename
    return p.read_text(encoding="utf-8").strip() if p.exists() else None


def tg(token, method, **params):
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request("https://api.telegram.org/bot%s/%s" % (token, method), data=data)
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def make_webhook_url(root, profile, ch):
    social = ch["social"]
    f = (social.get("publishers", {}).get("make", {}).get("webhook_url_file")
         or social.get("make_webhook_url_file"))
    return read_secret(root, profile, f)


def post_webhook(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=30).read().decode()


def main(argv):
    ap = argparse.ArgumentParser(); ap.add_argument("--profile", default="")
    a = ap.parse_args(argv)
    root = plugin_root(); ch = load_channels(root, a.profile)
    dist = ch.get("distribution")
    if not dist:
        print("no distribution block"); return
    qdir = root / dist.get("queue_dir", "outputs/distribution/queue"); qdir.mkdir(parents=True, exist_ok=True)
    offp = qdir / "tg_offset.txt"
    items = sorted(glob.glob(str(qdir / "*.json")))
    load = lambda p: json.load(open(p, encoding="utf-8"))
    save = lambda p, j: json.dump(j, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    approval = dist["approval"]["enabled"]
    token = chat = None
    if approval:
        token = read_secret(root, a.profile, dist["approval"]["telegram_token_file"])
        chat = str(read_secret(root, a.profile, dist["approval"]["telegram_chat_file"]))
        off = None
        if offp.exists():
            try: off = int(offp.read_text().strip())
            except Exception: off = None
        params = {"timeout": 0}
        if off: params["offset"] = off
        ups = tg(token, "getUpdates", **params).get("result", [])
        decisions = []; last = off or 0
        for u in ups:
            last = max(last, u["update_id"] + 1)
            m = u.get("message") or {}
            if str(m.get("chat", {}).get("id")) != chat: continue
            t = (m.get("text") or "").strip().lower().lstrip("/").strip()
            d = int(m.get("date", 0))
            if t.startswith("post") or t in ("ok", "duyệt", "đăng", "dang"): decisions.append((d, "post"))
            elif t.startswith("skip") or t in ("bỏ", "bo", "hủy", "huy"): decisions.append((d, "skip"))
        if last: offp.write_text(str(last))
        na = ns = 0
        for p in items:
            j = load(p)
            if j.get("status") != "awaiting": continue
            rel = [(d, dec) for (d, dec) in decisions if d >= int(j.get("created", 0))]
            if not rel: continue
            d, dec = sorted(rel)[-1]
            j["status"] = "approved" if dec == "post" else "skipped"; save(p, j)
            na += dec == "post"; ns += dec == "skip"
        if na: tg(token, "sendMessage", chat_id=chat, text="Da duyet %d bai." % na)
        if ns: tg(token, "sendMessage", chat_id=chat, text="Da bo %d bai." % ns)

    url = make_webhook_url(root, a.profile, ch)
    now = datetime.now(timezone.utc)
    for p in items:
        j = load(p)
        if j.get("status") != "approved": continue
        try: due = datetime.fromisoformat(j["post_at_utc"])
        except Exception: due = now
        if due <= now:
            body = {"channel": j["channel"], "post_text": j["caption"], "image_url": j["media_url"]}
            if j.get("is_video"): body["video_url"] = j["media_url"]
            post_webhook(url, body)
            j["status"] = "posted"; save(p, j)
            if approval:
                tg(token, "sendMessage", chat_id=chat, text="Da dang: " + j["channel"])
    print("tick done")


if __name__ == "__main__":
    main(sys.argv[1:])
