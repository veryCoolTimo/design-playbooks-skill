#!/usr/bin/env python3
"""Build catalog.json from profiles + media. Stdlib-only YAML-lite parser."""
import json, os, re

LIB = os.path.expanduser("~/.claude/design-library")

def frontmatter(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("---"):
        return {}
    fm = t.split("---", 2)[1]
    d = {}
    m = re.search(r'^style:\s*(\S+)', fm, re.M)
    d["style"] = m[1] if m else None
    m = re.search(r'^category:\s*(.+)', fm, re.M)
    d["category"] = m[1].strip().strip('"') if m else None
    m = re.search(r'^website:\s*(\S+)', fm, re.M)
    d["website"] = None if not m or m[1] in ("null", "~") else m[1].strip('"')
    m = re.search(r'^pages:\s*\[([^\]]*)\]', fm, re.M)
    d["pages"] = [p.strip() for p in m[1].split(",") if p.strip()] if m else []
    m = re.search(r'primary:\s*"(#[0-9a-fA-F]{3,8})"', fm)
    d["primary"] = m[1] if m else None
    return d

def main():
    sites = {}
    pdir = os.path.join(LIB, "profiles", "sites")
    for f in sorted(os.listdir(pdir)):
        if not f.endswith(".md"):
            continue
        slug = f[:-3]
        fm = frontmatter(os.path.join(pdir, f))
        media = os.path.join(LIB, "media", slug)
        sites[slug] = {
            "style": fm.get("style"), "category": fm.get("category"),
            "website": fm.get("website"), "pages": fm.get("pages", []),
            "palette": {"primary": fm.get("primary")},
            "profile": f"profiles/sites/{f}",
            "media": f"media/{slug}/" if os.path.isdir(media) else None,
            "has_media": os.path.isdir(media),
        }
    pb = lambda sub: sorted(f[:-3] for f in os.listdir(os.path.join(LIB, "playbooks", sub)) if f.endswith(".md"))
    flats = {b: len([f for f in os.listdir(os.path.join(LIB, "media", b))
                     if not f.startswith(".")]) if os.path.isdir(os.path.join(LIB, "media", b)) else 0
             for b in ("design", "app-icons", "og-images")}
    catalog = {"sites": sites,
               "playbooks": {"pages": pb("pages"), "styles": pb("styles"), "domains": pb("domains")},
               "flats": flats}
    json.dump(catalog, open(os.path.join(LIB, "catalog.json"), "w"), indent=1)
    print(f"catalog: {len(sites)} sites, playbooks {sum(len(v) for v in catalog['playbooks'].values())}, flats {flats}")

if __name__ == "__main__":
    main()
