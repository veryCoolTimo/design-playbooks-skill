#!/usr/bin/env python3
"""Fetch/restore the media layer from public CDNs.

Usage:
  python3 fetch_media.py --dry-run     # print the download plan
  python3 fetch_media.py               # download missing files only
  python3 fetch_media.py --all         # re-check every catalog site

getdesign.md sites:  https://cdn.getdesign.md/catalog/<slug>/<page>.<ext>
recent.design sites: URLs recorded in each site's meta.json (media/<slug>/meta.json)
Requires a Chrome UA header — the CDNs 403 default urllib UAs.
"""
import argparse, json, os, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

LIB = os.path.expanduser("~/.claude/design-library")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 Chrome/125.0 Safari/537.36")
GD_CDN = "https://cdn.getdesign.md/catalog"
EXTS = ("webp", "jpg", "png", "jpeg")


def head_ok(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Range": "bytes=0-0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status in (200, 206)
    except Exception:
        return False


def fetch(job):
    url, dest = job
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "skip"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
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


def plan_site(slug, site):
    """Return [(url, dest)] for one catalog site with missing media."""
    jobs = []
    mdir = os.path.join(LIB, "media", slug)
    meta_path = os.path.join(mdir, "meta.json")
    if os.path.exists(meta_path):  # recent.design site — URLs are recorded
        meta = json.load(open(meta_path))
        for i, m in enumerate(meta.get("media") or []):
            url = m.get("poster") or m.get("url")
            if not url:
                continue
            ext = url.split("?")[0].rsplit(".", 1)[-1][:4]
            jobs.append((url, os.path.join(mdir, f"media-{i+1:02d}.{ext}")))
        return jobs
    # getdesign site — probe page names from the profile's pages list
    pages = site.get("pages") or []
    ext = None
    for e in EXTS:
        if head_ok(f"{GD_CDN}/{slug}/home.{e}"):
            ext = e
            break
    if not ext:
        return jobs
    for page in pages or ["home"]:
        url = f"{GD_CDN}/{slug}/{page}.{ext}"
        dest = os.path.join(mdir, page, f"{page}.{ext}")
        if not os.path.exists(dest):
            jobs.append((url, dest))
    for extra, exts in (("thumb", EXTS), ("favicon", ("png", "svg", "ico", "jpg"))):
        if not any(os.path.exists(os.path.join(mdir, f"{extra}.{e}")) for e in exts):
            for e in exts:
                u = f"{GD_CDN}/{slug}/{extra}.{e}"
                if head_ok(u):
                    jobs.append((u, os.path.join(mdir, f"{extra}.{e}")))
                    break
    return jobs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--all", action="store_true", help="re-check every site, not just has_media:false")
    args = ap.parse_args()

    cat = json.load(open(os.path.join(LIB, "catalog.json")))
    targets = {s: v for s, v in cat["sites"].items()
               if args.all or not v.get("has_media")}
    print(f"checking {len(targets)} sites...")
    jobs = []
    with ThreadPoolExecutor(max_workers=12) as ex:
        for site_jobs in ex.map(lambda kv: plan_site(*kv), targets.items()):
            jobs.extend(site_jobs)
    print(f"{len(jobs)} files to download")
    if args.dry_run:
        for u, d in jobs[:20]:
            print("  ", u, "->", os.path.relpath(d, LIB))
        if len(jobs) > 20:
            print(f"   ... and {len(jobs)-20} more")
        return 0
    ok = skip = err = 0
    with ThreadPoolExecutor(max_workers=20) as ex:
        for res in ex.map(fetch, jobs):
            if res == "ok":
                ok += 1
            elif res == "skip":
                skip += 1
            else:
                err += 1
                print(" ", res)
    print(f"done: ok={ok} skip={skip} err={err}")
    return 1 if err else 0


if __name__ == "__main__":
    sys.exit(main())
