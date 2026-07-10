#!/usr/bin/env python3
"""Fail if catalog references anything that doesn't exist."""
import json, os, sys

LIB = os.path.expanduser("~/.claude/design-library")
cat = json.load(open(os.path.join(LIB, "catalog.json")))
errors = []
for slug, s in cat["sites"].items():
    if not os.path.exists(os.path.join(LIB, s["profile"])):
        errors.append(f"profile missing: {slug}")
    if s["has_media"] and not os.path.isdir(os.path.join(LIB, s["media"])):
        errors.append(f"media missing: {slug}")
    if not s["style"]:
        errors.append(f"no style: {slug}")
for sub, names in cat["playbooks"].items():
    for n in names:
        p = os.path.join(LIB, "playbooks", sub, n + ".md")
        if not os.path.exists(p):
            errors.append(f"playbook missing: {sub}/{n}")
        elif "Coverage:" not in open(p, encoding="utf-8").read():
            errors.append(f"no coverage badge: {sub}/{n}")
print(f"{len(errors)} errors")
for e in errors[:20]:
    print(" -", e)
sys.exit(1 if errors else 0)
