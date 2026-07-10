#!/usr/bin/env python3
"""Pull new items from recent.design feeds into the library.

Usage:
  python3 update_recent.py --dry-run   # show what's new
  python3 update_recent.py             # download new items

Feeds: websites (site folders), all→design flat, og-images flat, app-icons flat.
State: data/recent_state.json (seen item ids). New website slugs are appended to
data/profile_worklist.json so the next profile run picks them up.
"""
import argparse, json, os, re, sys, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

LIB = os.path.expanduser("~/.claude/design-library")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 Chrome/125.0 Safari/537.36")
API = "https://api.recent.design/trpc/items.list?batch=1&input="
FEEDS = [("websites", "site"), ("all", None), ("og-images", "og"), ("app-icons", "app_icon")]


def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", s or "").strip("-").lower()
    return s or "item"


def api_page(feed, fmt, cursor=None):
    inp = {"0": {"limit": 100, "feed": feed, "sort": "recent", "direction": "forward"}}
    if fmt:
        inp["0"]["format"] = fmt
    if cursor:
        inp["0"]["cursor"] = cursor
    url = API + urllib.parse.quote(json.dumps(inp))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    j = json.load(urllib.request.urlopen(req, timeout=40))
    d = j[0]["result"]["data"]
    return d.get("json", d)


def collect(feed, fmt, seen):
    """Fetch items until a page contains only already-seen ids."""
    out, cursor = [], None
    while True:
        d = api_page(feed, fmt, cursor)
        items = d.get("items", [])
        fresh = [it for it in items if it["id"] not in seen]
        out.extend(fresh)
        if not fresh or not d.get("nextCursor"):
            break
        cursor = d["nextCursor"]
    return out


def media_jobs(item, feed):
    slug = slugify(item.get("slug") or item.get("title") or item["id"])
    jobs = []
    if feed == "websites":
        folder = os.path.join(LIB, "media", slug)
        if os.path.isdir(folder):
            folder = os.path.join(LIB, "media", f"{slug}-recent")
        for i, m in enumerate(item.get("media") or []):
            url = (m.get("posterUrl") if m.get("mediaType") == "video" else m.get("url")) \
                  or m.get("posterUrl") or m.get("url")
            if not url:
                continue
            ext = url.split("?")[0].rsplit(".", 1)[-1][:4]
            jobs.append((url, os.path.join(folder, f"media-{i+1:02d}.{ext}")))
        meta = {k: item.get(k) for k in
                ("id", "slug", "title", "description", "tags", "category")}
        meta["url"] = (item.get("source") or {}).get("url")
        jobs.append(("__META__" + json.dumps(meta, ensure_ascii=False),
                     os.path.join(folder, "meta.json")))
    else:
        dest_dir = {"all": "design", "og-images": "og-images", "app-icons": "app-icons"}[feed]
        m = next(iter(item.get("media") or []), None)
        if m:
            url = (m.get("posterUrl") if m.get("mediaType") == "video" else m.get("url")) \
                  or m.get("posterUrl") or m.get("url")
            if url:
                ext = url.split("?")[0].rsplit(".", 1)[-1][:4]
                jobs.append((url, os.path.join(LIB, "media", dest_dir, f"{slug}.{ext}")))
    return jobs


def fetch(job):
    url, dest = job
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if url.startswith("__META__"):
        open(dest, "w").write(url[len("__META__"):])
        return "ok"
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "skip"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        tmp = dest + ".part"
        open(tmp, "wb").write(data)
        os.replace(tmp, dest)
        return "ok"
    except Exception as e:
        return f"err {dest}: {e}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state_path = os.path.join(LIB, "data", "recent_state.json")
    seen = set(json.load(open(state_path))) if os.path.exists(state_path) else set()
    bootstrap = not seen

    all_new, jobs, new_site_slugs = [], [], []
    for feed, fmt in FEEDS:
        fresh = collect(feed, fmt, seen)
        # first run against an already-complete library: just record ids
        print(f"{feed}: {len(fresh)} new item(s)")
        for it in fresh:
            all_new.append(it["id"])
            if not bootstrap:
                jobs.extend(media_jobs(it, feed))
                if feed == "websites":
                    new_site_slugs.append(slugify(it.get("slug") or it["id"]))
    if bootstrap:
        print("(first run: recording current feed state as baseline, no downloads)")
    print(f"total: {len(all_new)} new, {len(jobs)} files to fetch")
    if args.dry_run:
        for u, d in jobs[:15]:
            print("  ", (u[:80] if not u.startswith('__META__') else 'meta.json'),
                  "->", os.path.relpath(d, LIB))
        return 0
    ok = err = 0
    with ThreadPoolExecutor(max_workers=16) as ex:
        for res in ex.map(fetch, jobs):
            if res.startswith("err"):
                err += 1
                print(" ", res)
            else:
                ok += 1
    seen.update(all_new)
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    json.dump(sorted(seen), open(state_path, "w"))
    if new_site_slugs:
        wl_path = os.path.join(LIB, "data", "profile_worklist.json")
        wl = json.load(open(wl_path)) if os.path.exists(wl_path) else []
        have = {w["slug"] for w in wl}
        wl += [{"slug": s, "mode": "vision"} for s in new_site_slugs if s not in have]
        json.dump(wl, open(wl_path, "w"), indent=1)
        print(f"worklist: +{len(new_site_slugs)} site(s) queued for profiling")
    print(f"done: ok={ok} err={err}; state={len(seen)} ids")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
