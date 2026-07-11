#!/usr/bin/env python3
"""Build catalog.json v2 from profiles + media + curated data.

Adds over v1: normalized category (+ raw subcategory), light/dark bucket from
canvas luminance, accents, radius, recent.design tags, signature keywords,
curated style_alt when the calibrated style map disagrees with the profile,
sanitized pages (only page-folders that actually exist on disk), analyzed_at,
and a runtime-checked has_media. Stdlib-only YAML-lite parser.
"""
import json, os, re, datetime
from taxonomy import normalize

LIB = os.path.expanduser("~/.claude/design-library")

STOP = set("the a an and or of for with your you our are is to in on at by as it this that "
           "page site design brand color colors type font fonts real not never always plus "
           "one two three every each into over under above below left right top bottom center "
           "dark light white black gray grey warm cool soft hard big small large heavy thin "
           "bold weight text body headline nav hero card cards button buttons pill radius".split())

def parse_profile(path):
    t = open(path, encoding="utf-8").read()
    fm = t.split("---", 2)[1] if t.startswith("---") else ""
    d = {}
    g = lambda pat: (re.search(pat, fm, re.M) or [None, None])[1]
    d["style"] = g(r'^style:\s*(\S+)')
    d["category"] = (g(r'^category:\s*(.+)') or "").strip().strip('"') or None
    w = g(r'^website:\s*(\S+)')
    d["website"] = None if not w or w in ("null", "~") else w.strip('"')
    m = re.search(r'^pages:\s*\[([^\]]*)\]', fm, re.M)
    d["pages"] = [p.strip() for p in m[1].split(",") if p.strip()] if m else []
    d["canvas"] = g(r'canvas:\s*"(#[0-9a-fA-F]{3,8})"')
    d["ink"] = g(r'ink:\s*"(#[0-9a-fA-F]{3,8})"')
    d["primary"] = g(r'primary:\s*"(#[0-9a-fA-F]{3,8})"')
    ac = re.search(r'accents:\s*\[([^\]]*)\]', fm)
    d["accents"] = re.findall(r'#[0-9a-fA-F]{3,8}', ac[1]) if ac else []
    d["radius"] = (g(r'^radius:\s*"?(.+?)"?\s*$') or "").strip('"') or None
    # signature keywords from the ## Signature section
    sig = re.search(r'## Signature\s*(.+?)(?:\n## |\Z)', t, re.S)
    kws = []
    if sig:
        words = re.findall(r'[a-zA-Z][a-zA-Z-]{3,}', sig[1].lower())
        seen = set()
        for w in words:
            if w in STOP or w in seen:
                continue
            seen.add(w)
            kws.append(w)
    d["keywords"] = kws[:12]
    return d

def luminance(hexcol):
    if not hexcol:
        return None
    h = hexcol.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    except ValueError:
        return None
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255

def recent_tags(slug):
    p = os.path.join(LIB, "media", slug, "meta.json")
    if not os.path.exists(p):
        return []
    try:
        meta = json.load(open(p))
    except Exception:
        return []
    return sorted({t["n"] for t in (meta.get("tags") or []) if t.get("n")})

def real_page_dirs(slug):
    d = os.path.join(LIB, "media", slug)
    if not os.path.isdir(d):
        return set()
    return {x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))}

def has_real_media(slug):
    """True only if there is at least one actual image on disk (not just DESIGN.md)."""
    d = os.path.join(LIB, "media", slug)
    if not os.path.isdir(d):
        return False
    exts = (".jpg", ".jpeg", ".png", ".webp", ".avif", ".svg")
    for root, _, files in os.walk(d):
        for f in files:
            if f.lower().endswith(exts) and not f.startswith("favicon"):
                return True
    return False

def main():
    style_map = json.load(open(f"{LIB}/data/style_map.json"))
    today = datetime.date.today().isoformat()
    pdir = os.path.join(LIB, "profiles", "sites")
    sites, cat_counts = {}, {}

    for f in sorted(os.listdir(pdir)):
        if not f.endswith(".md"):
            continue
        slug = f[:-3]
        p = parse_profile(os.path.join(pdir, f))
        canon, sub = normalize(p["category"])
        lum = luminance(p["canvas"])
        tone = None if lum is None else ("light" if lum >= 0.5 else "dark")
        real = real_page_dirs(slug)
        pages_have = sorted(real) if real else []          # verified on disk
        pages_claimed = p["pages"]                          # from vision (may include unseen)
        has_media = has_real_media(slug)
        # curated style disagreement -> record as alternate, don't overwrite
        curated = style_map.get(slug)
        style_alt = curated if (curated and curated != p["style"]) else None

        sites[slug] = {
            "style": p["style"],
            "style_alt": style_alt,
            "category": canon,
            "subcategory": sub,
            "tone": tone,
            "website": p["website"],
            "pages": pages_claimed,
            "pages_on_disk": pages_have,
            "palette": {"canvas": p["canvas"], "ink": p["ink"],
                        "primary": p["primary"], "accents": p["accents"]},
            "radius": p["radius"],
            "keywords": p["keywords"],
            "tags": recent_tags(slug),
            "profile": f"profiles/sites/{f}",
            "media": f"media/{slug}/" if os.path.isdir(os.path.join(LIB, "media", slug)) else None,
            "has_media": has_media,
            "analyzed_at": today,
        }
        cat_counts[canon] = cat_counts.get(canon, 0) + 1

    pb = lambda sub: sorted(x[:-3] for x in os.listdir(os.path.join(LIB, "playbooks", sub)) if x.endswith(".md"))
    flats = {b: len([x for x in os.listdir(os.path.join(LIB, "media", b))
                     if not x.startswith(".")]) if os.path.isdir(os.path.join(LIB, "media", b)) else 0
             for b in ("design", "app-icons", "og-images")}

    catalog = {
        "meta": {
            "version": 2,
            "built": today,
            "sites": len(sites),
            "categories": dict(sorted(cat_counts.items(), key=lambda kv: -kv[1])),
            "styles": {"ML": "minimal-light", "DT": "dark-tech", "DN": "dark-neon",
                       "CP": "colorful-playful", "IL": "illustration", "BT": "big-type",
                       "EL": "elegant-serif", "PH": "photo-driven", "GR": "gradient-mesh"},
        },
        "sites": sites,
        "playbooks": {"pages": pb("pages"), "styles": pb("styles"), "domains": pb("domains")},
        "flats": flats,
    }
    json.dump(catalog, open(os.path.join(LIB, "catalog.json"), "w"), indent=1)
    dark = sum(1 for v in sites.values() if v["tone"] == "dark")
    light = sum(1 for v in sites.values() if v["tone"] == "light")
    with_media = sum(1 for v in sites.values() if v["has_media"])
    with_tags = sum(1 for v in sites.values() if v["tags"])
    alt = sum(1 for v in sites.values() if v["style_alt"])
    print(f"catalog v2: {len(sites)} sites | {len(cat_counts)} categories | "
          f"tone dark={dark} light={light} | has_media={with_media} | tags={with_tags} | style_alt={alt}")
    print(f"categories: {catalog['meta']['categories']}")

if __name__ == "__main__":
    main()
