#!/usr/bin/env python3
"""Fail if the catalog references anything that doesn't exist or drifts from disk."""
import json, os, sys

LIB = os.path.expanduser("~/.claude/design-library")
cat = json.load(open(os.path.join(LIB, "catalog.json")))
errors, warns = [], []

VALID_STYLES = set(cat["meta"]["styles"])
VALID_CATS = set(cat["meta"]["categories"])

for slug, s in cat["sites"].items():
    if not os.path.exists(os.path.join(LIB, s["profile"])):
        errors.append(f"profile missing: {slug}")
    if s["style"] not in VALID_STYLES:
        errors.append(f"bad style {s['style']!r}: {slug}")
    if s.get("style_alt") and s["style_alt"] not in VALID_STYLES:
        errors.append(f"bad style_alt {s['style_alt']!r}: {slug}")
    if s["category"] not in VALID_CATS:
        errors.append(f"bad category {s['category']!r}: {slug}")
    # has_media must reflect reality
    if s["has_media"] and not (s["media"] and os.path.isdir(os.path.join(LIB, s["media"]))):
        errors.append(f"has_media true but no dir: {slug}")
    # pages_on_disk must actually be folders with images
    for p in s.get("pages_on_disk", []):
        d = os.path.join(LIB, "media", slug, p)
        if not os.path.isdir(d):
            errors.append(f"pages_on_disk ghost: {slug}/{p}")

for sub, names in cat["playbooks"].items():
    for n in names:
        p = os.path.join(LIB, "playbooks", sub, n + ".md")
        if not os.path.exists(p):
            errors.append(f"playbook missing: {sub}/{n}")
        elif "Coverage:" not in open(p, encoding="utf-8").read():
            warns.append(f"no coverage badge: {sub}/{n}")

print(f"{len(errors)} errors, {len(warns)} warnings")
for e in errors[:20]:
    print("  ✗", e)
for w in warns[:20]:
    print("  ⚠", w)
sys.exit(1 if errors else 0)
