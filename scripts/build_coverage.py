#!/usr/bin/env python3
"""Inventory page-type coverage across the media corpus."""
import json, os, sys

LIB = os.path.expanduser("~/.claude/design-library")
MEDIA = os.path.join(LIB, "media")
SKIP_DIRS = {"design", "app-icons", "og-images"}
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".avif"}

def main():
    coverage = {}
    for slug in sorted(os.listdir(MEDIA)):
        root = os.path.join(MEDIA, slug)
        if not os.path.isdir(root) or slug in SKIP_DIRS:
            continue
        for page in sorted(os.listdir(root)):
            pdir = os.path.join(root, page)
            if not os.path.isdir(pdir):
                continue
            imgs = [f for f in sorted(os.listdir(pdir))
                    if os.path.splitext(f)[1].lower() in IMG_EXT]
            if not imgs:
                continue
            entry = coverage.setdefault(page, {"count": 0, "examples": []})
            entry["count"] += 1
            entry["examples"].append(f"{slug}/{page}/{imgs[0]}")
    coverage = dict(sorted(coverage.items(), key=lambda kv: -kv[1]["count"]))
    out = os.path.join(LIB, "data", "page_coverage.json")
    json.dump(coverage, open(out, "w"), indent=1)
    big = {k: v["count"] for k, v in coverage.items() if v["count"] >= 15}
    print(f"page types: {len(coverage)}; with >=15 examples: {len(big)}")
    print(json.dumps(big, indent=1))

if __name__ == "__main__":
    sys.exit(main())
