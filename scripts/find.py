#!/usr/bin/env python3
"""Search the catalog. The skill calls this instead of ad-hoc grep.

Examples:
  find.py --style DT --category fintech --page pricing
  find.py --tone dark --category crypto-web3 --has-media
  find.py --keyword gradient --keyword mesh
  find.py --tag animation --tag 3d
  find.py --like stripe            # sites sharing style+category with stripe
  find.py --category ai-ml --json  # machine-readable

Filters AND together. --keyword / --tag may repeat (OR within, AND across kinds).
Style codes: ML DT DN CP IL BT EL PH GR. Categories: developer-tools ai-ml
productivity design-creative crypto-web3 media-consumer fintech marketing-sales
hardware health data-analytics ecommerce-retail security hr-people. Tone: light|dark.
"""
import argparse, json, os, sys

LIB = os.path.expanduser("~/.claude/design-library")

def load():
    return json.load(open(os.path.join(LIB, "catalog.json")))

def match(slug, s, a):
    if a.style and s["style"] != a.style and s.get("style_alt") != a.style:
        return False
    if a.category and s["category"] != a.category:
        return False
    if a.tone and s["tone"] != a.tone:
        return False
    if a.has_media and not s["has_media"]:
        return False
    if a.page:
        pool = set(s["pages"]) | set(s.get("pages_on_disk", []))
        if not any(p in pool for p in a.page):
            return False
    if a.on_disk:  # page must have an actual screenshot folder
        if not any(p in set(s.get("pages_on_disk", [])) for p in a.on_disk):
            return False
    if a.keyword:
        kws = set(s.get("keywords", [])) | {w.lower() for w in s.get("tags", [])}
        blob = (s.get("subcategory") or "") + " " + slug
        if not all(any(k.lower() in x for x in (kws | {blob.lower()})) for k in a.keyword):
            return False
    if a.tag:
        tags = {t.lower() for t in s.get("tags", [])}
        if not all(t.lower() in tags for t in a.tag):
            return False
    return True

def main():
    ap = argparse.ArgumentParser(description="Search the design catalog.")
    ap.add_argument("--style")
    ap.add_argument("--category")
    ap.add_argument("--tone", choices=["light", "dark"])
    ap.add_argument("--page", action="append", help="page type in pages or on disk (repeatable)")
    ap.add_argument("--on-disk", action="append", dest="on_disk", help="page with a real screenshot folder")
    ap.add_argument("--keyword", action="append", help="signature/tag/slug keyword (repeatable, AND)")
    ap.add_argument("--tag", action="append", help="recent.design tag (repeatable, AND)")
    ap.add_argument("--has-media", action="store_true", dest="has_media")
    ap.add_argument("--like", help="slug: find siblings sharing its style+category")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cat = load()
    sites = cat["sites"]
    like_seed = None
    note = None
    if a.like:
        ref = sites.get(a.like)
        if not ref:
            print(f"unknown slug: {a.like}", file=sys.stderr)
            return 2
        like_seed = a.like
        a.style, a.category = ref["style"], ref["category"]

    def run():
        return [(slug, s) for slug, s in sites.items()
                if slug != like_seed and match(slug, s, a)]

    hits = run()
    if a.like and len(hits) < 3:
        # unique (style,category) pair — widen: same category, then same style
        seed = sites[like_seed]
        a.style = None
        cat_hits = run()
        if len(cat_hits) >= 3:
            hits, note = cat_hits, (f"few exact style+category siblings of {like_seed}; "
                                    f"showing same-category ({seed['category']}) matches — "
                                    f"read {like_seed}'s profile for its exact tokens.")
        else:
            a.category, a.style = None, seed["style"]
            hits, note = run(), (f"{like_seed} is nearly unique in the corpus; showing "
                                 f"same-style ({seed['style']}) matches instead.")
    if not hits and a.page:
        # graceful fallback: drop the page filter, keep style/category/tone
        want = a.page
        a.page = None
        hits = [(slug, s) for slug, s in sites.items() if match(slug, s, a)]
        if hits:
            note = (f"no site in this slice has a '{'/'.join(want)}' screenshot; "
                    f"showing the nearest matches — borrow structure from "
                    f"playbooks/pages/{want[0]}.md and tokens from one of these.")
    # prefer entries that actually have the requested page on disk, then has_media
    def rank(kv):
        slug, s = kv
        score = 0
        if a.page and any(p in set(s.get("pages_on_disk", [])) for p in a.page):
            score += 2
        if s["has_media"]:
            score += 1
        return -score
    hits.sort(key=rank)
    hits = hits[:a.limit]

    if a.json:
        print(json.dumps({slug: s for slug, s in hits}, indent=1))
        return 0
    if not hits:
        print("no matches. Loosen filters or try --like <slug>.")
        return 0
    if note:
        print(f"⚠ {note}\n")
    print(f"{len(hits)} match(es):")
    for slug, s in hits:
        prim = s["palette"]["primary"] or "?"
        alt = f"/{s['style_alt']}" if s.get("style_alt") else ""
        media = "📷" if s["has_media"] else "  "
        disk = ",".join(s.get("pages_on_disk", [])[:5])
        web = s["website"] or ""
        print(f"  {media} {slug:22s} {s['style']}{alt:3s} {s['category']:16s} {prim:8s} "
              f"[{disk}] {web}")
    print(f"\nread a profile: profiles/sites/<slug>.md · screenshots: media/<slug>/<page>/")
    return 0

if __name__ == "__main__":
    sys.exit(main())
