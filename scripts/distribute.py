#!/usr/bin/env python3
"""
distribute.py — config-driven DISTRIBUTION stage for the Content Engine plugin.

Prepares a finished asset (video/Reel or image) and queues it for publishing, with an optional
Telegram approval gate and timezone-aware scheduling. Reads config/channels.json (distribution block)
+ social.publishers (Make webhook). Brand-agnostic: forks just edit config/.

Usage:
  python distribute.py <media> "<caption>" --channel facebook_reel [--channel linkedin_video] \
        [--profile NAME] [--now]

  --channel  Make channel value (e.g. facebook_reel, linkedin_video, facebook, linkedin). Repeatable.
  --profile  examples/<profile>/config (multi-brand). Omit to use config/ at plugin root.
  --now      ignore the schedule; publish as soon as approved.
"""
import argparse, json, os, subprocess, sys, tempfile, urllib.request, urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
try:
    from zoneinfo import ZoneInfo
except Exception:
    ZoneInfo = None

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm"}
VIDEO_CHANNELS = {"facebook_reel", "linkedin_video"}
WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def plugin_root() -> Path:
    here = Path(__file__).resolve()
    for a in [here.parent, *here.parents]:
        if (a / ".claude-plugin" / "plugin.json").exists():
            return a
    return here.parent.parent


def cfg_dir(root: Path, profile: str) -> Path:
    return (root / "examples" / profile / "config") if profile else (root / "config")


def load_channels(root: Path, profile: str) -> dict:
    p = cfg_dir(root, profile) / "channels.json"
    if not p.exists():
        sys.exit("channels.json not found at %s — fill from config/channels.template.json first." % p)
    return json.load(open(p, encoding="utf-8"))


def read_secret(root: Path, profile: str, filename: str) -> str:
    p = cfg_dir(root, profile) / filename
    if not p.exists():
        sys.exit("Secret file missing: %s" % p)
    return p.read_text(encoding="utf-8").strip()


def tg(root, profile, dist, method, **params):
    token = read_secret(root, profile, dist["approval"]["telegram_token_file"])
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request("https://api.telegram.org/bot%s/%s" % (token, method), data=data)
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode())


def fps_of(path):
    try:
        o = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", path], text=True).strip()
        n, d = (o.split("/") + ["1"])[:2]
        return float(n) / float(d or 1)
    except Exception:
        return None


def ensure_fps(path, target):
    f = fps_of(path)
    if f is not None and f >= 24:
        return path
    out = os.path.join(tempfile.gettempdir(), "reel_%dfps.mp4" % target)
    subprocess.run(["ffmpeg", "-y", "-i", path, "-r", str(target), "-c:v", "libx264", "-profile:v",
        "high", "-pix_fmt", "yuv420p", "-g", "60", "-movflags", "+faststart", "-c:a", "aac",
        "-ar", "48000", "-ac", "2", "-b:a", "128k", out], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out


def upload_host(path, host):
    if host == "catbox":
        o = subprocess.check_output(["curl", "-s", "--max-time", "180", "-F", "reqtype=fileupload",
            "-F", "fileToUpload=@" + path, "https://catbox.moe/user/api.php"], text=True).strip()
        if not o.startswith("http"):
            sys.exit("catbox upload failed: " + o[:200])
        return o
    sys.exit("Unsupported video_host '%s' (add it to upload_host)." % host)


def next_slot_utc(slot, tz_name, now=None):
    now = now or datetime.now(timezone.utc)
    tz = ZoneInfo(tz_name) if ZoneInfo else timezone.utc
    ln = now.astimezone(tz)
    hh, mm = [int(x) for x in slot["time"].split(":")]
    days = slot["days"]
    ok = (lambda d: True) if days == "daily" else (lambda d: WD[d] in days)
    for i in range(0, 14):
        cand = (ln + timedelta(days=i)).replace(hour=hh, minute=mm, second=0, microsecond=0)
        if cand > ln and ok(cand.weekday()):
            return cand.astimezone(timezone.utc).isoformat()
    return now.isoformat()


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("media"); ap.add_argument("caption")
    ap.add_argument("--channel", action="append", required=True)
    ap.add_argument("--profile", default="")
    ap.add_argument("--now", action="store_true")
    a = ap.parse_args(argv)

    root = plugin_root(); ch = load_channels(root, a.profile)
    dist = ch.get("distribution") or sys.exit("No 'distribution' block in channels.json (add it).")
    qdir = root / dist.get("queue_dir", "outputs/distribution/queue"); qdir.mkdir(parents=True, exist_ok=True)

    is_video_file = Path(a.media).suffix.lower() in VIDEO_EXT
    prepared = ensure_fps(a.media, int(dist.get("ensure_fps", 30))) if is_video_file else a.media
    url = upload_host(prepared, dist.get("video_host", "catbox"))

    import time as _t
    made = []
    for chan in a.channel:
        is_video = chan in VIDEO_CHANNELS or is_video_file
        if a.now or chan not in dist["schedule"]["slots"]:
            post_at = datetime.now(timezone.utc).isoformat()
        else:
            post_at = next_slot_utc(dist["schedule"]["slots"][chan], dist["schedule"]["timezone"])
        jid = str(int(_t.time() * 1000)) + "-" + chan
        approved = not dist["approval"]["enabled"]
        job = {"id": jid, "media_url": url, "caption": a.caption, "channel": chan,
               "is_video": is_video, "post_at_utc": post_at,
               "status": "approved" if approved else "awaiting",
               "created": int(_t.time()), "profile": a.profile}
        json.dump(job, open(qdir / (jid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        made.append((chan, post_at))

    if dist["approval"]["enabled"]:
        lines = "\n".join("- %s @ %s" % (c, p) for c, p in made)
        txt = "Bai cho duyet\n\n%s\n\nLink: %s\nKenh:\n%s\n\nTra loi:  post = duyet  |  skip = bo" % (
            a.caption, url, lines)
        tg(root, a.profile, dist, "sendMessage",
           chat_id=read_secret(root, a.profile, dist["approval"]["telegram_chat_file"]), text=txt)
    print("enqueued:", [c for c, _ in made], "| approval:", dist["approval"]["enabled"])


if __name__ == "__main__":
    main(sys.argv[1:])
