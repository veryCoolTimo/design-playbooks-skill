# Design Intelligence Skill — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a knowledge library (profiles + playbooks + catalog) from the 914 MB design-reference corpus and a global Claude Code skill that uses it for frontend work.

**Architecture:** Layered library at `~/.claude/design-library/` (catalog.json → profiles → playbooks → media), produced by a calibrated multi-agent vision pipeline (Workflow tool), consumed by one router skill at `~/.claude/skills/design-refs/`. Knowledge layer is public-shippable; media layer is local-only.

**Tech Stack:** Python 3 (stdlib only) for scripts, Claude Code Workflow tool for vision agents, Markdown+YAML for knowledge artifacts.

## Global Constraints

- Library root: `~/.claude/design-library/` (abbreviated `$LIB` below). Media at `$LIB/media/` — never committed (`.gitignore` already covers it).
- All knowledge artifacts (profiles, playbooks, catalog, SKILL.md) are written in **English** (public-ready). User conversation stays Russian.
- The 75 getdesign.md DESIGN.md files (`$LIB/media/<slug>/DESIGN.md`) are calibration ground truth only — never copied into `profiles/`, never committed.
- Profile format must be valid YAML frontmatter + Markdown body (schema fixed in Task 2).
- Vision agents must Read actual screenshot files; profiles must never be invented from the slug/name alone.
- Every playbook carries a coverage badge: `> Coverage: N examples from corpus` (≥15 examples → own playbook; <15 → goes to `pages/misc.md`).
- Resumability: every generation stage skips outputs that already exist and are non-empty.
- Commit to `$LIB` git after every task.

## Corpus facts (verified in session, use as given)

- `$LIB/media/`: 407 site folders (page subfolders `home/`, `pricing/`, … with jpg/webp screenshots; 28 recent-design sites use flat `shot-NN.jpg` + `meta.json`), plus flat `design/` (248 images), `app-icons/` (93), `og-images/` (49), `REFERENCE.md`, `INDEX.md`.
- 75 folders contain an authoritative `DESIGN.md`. 11 slugs have BOTH screenshots and DESIGN.md: `cohere figma framer mintlify miro notion raycast resend shopify supabase superhuman` — calibration set comes from these.
- 64 slugs are MD-only (no screenshots): profile is distilled from their DESIGN.md text (private-use ok; profile text must be our own words).
- Style codes (9): ML, DT, DN, CP, IL, BT, EL, PH, GR (assignments exist in session scratchpad `style_map.json`; Task 1 copies it into `$LIB/data/`).
- recent.design items have `meta.json` with tags (style/color/framework/interaction), title, description, url.

---

### Task 1: Scaffolding, data imports, page-coverage inventory

**Files:**
- Create: `$LIB/{profiles/sites,playbooks/{pages,styles,domains},scripts,data}/` (dirs)
- Create: `$LIB/data/style_map.json` (copy from scratchpad)
- Create: `$LIB/scripts/build_coverage.py`
- Create: `$LIB/data/page_coverage.json` (script output)

**Interfaces:**
- Produces: `page_coverage.json` — `{"<page-type>": {"count": int, "examples": ["<slug>/<page>/<file>", ...]}}`, sorted by count desc. Task 3 consumes it. `style_map.json` — `{"<slug>": "<STYLE_CODE>"}`. Tasks 4–5 consume it.

- [ ] **Step 1: Create directories and import style map**

```bash
LIB=~/.claude/design-library
mkdir -p $LIB/profiles/sites $LIB/playbooks/pages $LIB/playbooks/styles $LIB/playbooks/domains $LIB/scripts $LIB/data
cp /private/tmp/claude-501/-Users-timo-Downloads-frontanalysis/919dfc46-ecdb-4ffe-b16e-50ee9e80dafc/scratchpad/style_map.json $LIB/data/style_map.json
python3 -c "import json;d=json.load(open('$HOME/.claude/design-library/data/style_map.json'));print(len(d),'style assignments')"
```
Expected: `380 style assignments` (379 folders + 1 duplicate slug entry is fine).
If the scratchpad file is gone (session GC), regenerate from `$LIB/media/REFERENCE.md`: each site line sits under a style `<a id="XX">` section — parse section→slug pairs.

- [ ] **Step 2: Write `scripts/build_coverage.py`**

```python
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
```

- [ ] **Step 3: Run and verify**

```bash
python3 $LIB/scripts/build_coverage.py
```
Expected: prints ~190 page types; `home` ≈ 200, `pricing` ≈ 120, `blog` ≈ 60, `about` ≈ 45; a dict of roughly 8–14 types with ≥15 examples. `data/page_coverage.json` exists and is valid JSON.

- [ ] **Step 4: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: scaffolding, style map import, page-coverage inventory"
```

---

### Task 2: Calibrate the profile-generation prompt (Phase 0)

**Files:**
- Create: `$LIB/scripts/profile-prompt.md` (the calibrated prompt template)
- Create: `$LIB/data/calibration-report.md`
- Create: `$LIB/profiles/sites/figma.md`, `supabase.md`, `raycast.md` (calibration by-products)

**Interfaces:**
- Produces: `profile-prompt.md` — prompt template with placeholder `{{SCREENSHOT_PATHS}}`, `{{SLUG}}`, `{{KNOWN_META}}`. Task 4 consumes it verbatim.
- Produces: the **profile schema** (below) — Tasks 4, 5, 7 depend on its field names.

**Profile schema (fixed here, do not drift):**

```markdown
---
name: <slug>
kind: site
style: <ML|DT|DN|CP|IL|BT|EL|PH|GR>
category: <industry slug>
website: <url or null>
pages: [<page types seen>]
palette:
  canvas: "#hex"        # dominant background
  ink: "#hex"           # dominant text
  primary: "#hex"       # main CTA/brand color
  accents: ["#hex", ...] # 0-4 supporting colors
typography:
  display: "<family or closest guess> · <weight feel> · <letter-spacing feel>"
  body: "<family or closest guess>"
radius: "<none|small 2-6px|medium 8-14px|large 16px+|pill>"
---
## Overview
2-4 sentences: the visual language in essence.
## Layout
Nav pattern, hero structure, section rhythm, grid/whitespace character.
## Components
Buttons, cards, inputs: shape, borders, shadows, states seen.
## Signature
2-4 bullet points: what makes this site recognizable.
## Do / Don't
3-5 Do bullets, 3-5 Don't bullets grounded in what the screenshots show.
```

- [ ] **Step 1: Write the draft prompt template to `scripts/profile-prompt.md`**

````markdown
You are a design analyst. Read the screenshot files listed below with the Read tool,
then write a design profile for site "{{SLUG}}".

Screenshots (read ALL of them):
{{SCREENSHOT_PATHS}}

Known metadata (may be partial; trust the screenshots over it):
{{KNOWN_META}}

Return ONLY the profile markdown, exactly in this schema:
[schema from Task 2 header, inlined verbatim]

Rules:
- Hex colors: sample what you actually see; canvas/ink/primary are mandatory.
- Typography: name the family if recognizable (Inter, Geist, GT America, serif…),
  otherwise describe ("geometric grotesque", "humanist serif").
- Do/Don't must be specific to THIS site's language, not generic design advice.
- British no, American yes: use American spelling. No marketing fluff.
````

- [ ] **Step 2: Run calibration on 3 sites with ground truth**

For each of `figma`, `supabase`, `raycast`: launch one general-purpose agent with the prompt (fill placeholders: all screenshots under `$LIB/media/<slug>/*/`, meta = style code + category from REFERENCE.md). Save output to `$LIB/profiles/sites/<slug>.md`.

- [ ] **Step 3: Score against ground truth**

Compare each generated profile with `$LIB/media/<slug>/DESIGN.md`:
- palette.primary within perceptual distance of etalon primary (same hue family) — PASS/FAIL
- typography family matches or is a stated close substitute — PASS/FAIL
- radius class matches etalon `rounded` scale — PASS/FAIL
Record the 9 verdicts in `data/calibration-report.md`. If ≥2 FAILs on any site: adjust the prompt (typical fixes: force color sampling from hero AND button, ask for font inspection of headings vs body separately), regenerate, rescore. Iterate max 3 rounds; record each round.

- [ ] **Step 4: Verify all three profiles parse**

```bash
python3 - <<'PY'
import os,re
lib=os.path.expanduser("~/.claude/design-library/profiles/sites")
for f in ["figma.md","supabase.md","raycast.md"]:
    t=open(os.path.join(lib,f)).read()
    assert t.startswith("---"), f
    fm=t.split("---")[1]
    for key in ["name:","style:","palette:","primary:","typography:"]:
        assert key in fm, (f,key)
print("3 calibration profiles OK")
PY
```
Expected: `3 calibration profiles OK`

- [ ] **Step 5: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: calibrated profile prompt + 3 ground-truth profiles"
```

---

### Task 3: Page playbooks (Phase 1 — main product)

**Files:**
- Create: `$LIB/playbooks/pages/<type>.md` for every type with ≥15 examples in `data/page_coverage.json`
- Create: `$LIB/playbooks/pages/misc.md` (types with <15 examples, grouped)

**Interfaces:**
- Consumes: `data/page_coverage.json` (Task 1).
- Produces: playbook files; SKILL.md (Task 8) references them as `playbooks/pages/<type>.md`.

**Playbook schema (fixed):**

```markdown
# <Type> Page Playbook
> Coverage: N examples from corpus
## Anatomy          — ordered section skeleton observed across corpus (with % frequency for major variants)
## Patterns that work — 5-10 bullets, each naming ≥1 example site (slug)
## Variants by style  — how ML vs DT vs CP etc. treat this page (only styles with evidence)
## Anti-patterns     — mistakes/absences observed; things the corpus avoids
## Checklist         — 6-10 point build checklist for an agent making this page
## Best references   — 5-8 slugs with one-line why
```

- [ ] **Step 1: Launch the page-playbook workflow**

Use the Workflow tool. One agent per page type with ≥15 examples. Each agent prompt:

````
You are writing a design playbook for "<TYPE>" pages, synthesized from real screenshots.
Read these screenshot files (sample of the corpus, read ALL listed):
<20 example paths from page_coverage.json examples list, full $LIB/media/ prefix;
 if >20 available, take every k-th to spread across sites>
Then write playbooks/pages/<TYPE>.md following EXACTLY this schema:
[playbook schema inlined]
Coverage badge: "> Coverage: <COUNT> examples from corpus (analyzed <SAMPLED>)".
Every claim in "Patterns that work" must cite at least one slug you actually saw.
American English. No generic advice that ignores the screenshots.
Write the file with the Write tool, then return "DONE <TYPE>".
````

- [ ] **Step 2: Build misc.md**

One agent: for each type with 5–14 examples, read 3 examples each, write one compact section per type (Anatomy + 3 patterns + 2 references) into `playbooks/pages/misc.md` with per-section coverage counts. Types with <5 examples: list them at the bottom under "Thin coverage — use Live Analyzer".

- [ ] **Step 3: Verify**

```bash
ls $LIB/playbooks/pages/ && grep -L "Coverage:" $LIB/playbooks/pages/*.md; echo "files missing badge: ^ (empty = OK)"
grep -c "##" $LIB/playbooks/pages/home.md
```
Expected: one file per ≥15 type + misc.md; no file missing a coverage badge; home.md has ≥6 sections.

- [ ] **Step 4: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: page playbooks synthesized from corpus"
```

---

### Task 4: Site profiles for the full corpus (Phase 2)

**Files:**
- Create: `$LIB/profiles/sites/<slug>.md` for all 407 site folders (3 exist from Task 2)

**Interfaces:**
- Consumes: `scripts/profile-prompt.md` (Task 2), `data/style_map.json` (Task 1).
- Produces: profiles; Tasks 5 and 7 parse their YAML frontmatter (field names per Task 2 schema).

- [ ] **Step 1: Build the work list**

```bash
python3 - <<'PY'
import json,os
LIB=os.path.expanduser("~/.claude/design-library")
MEDIA=os.path.join(LIB,"media"); SKIP={"design","app-icons","og-images"}
done={os.path.splitext(f)[0] for f in os.listdir(f"{LIB}/profiles/sites")}
todo=[]
for slug in sorted(os.listdir(MEDIA)):
    d=os.path.join(MEDIA,slug)
    if not os.path.isdir(d) or slug in SKIP or slug in done: continue
    has_shots=any(os.path.isdir(os.path.join(d,p)) for p in os.listdir(d)) or \
              any(f.startswith("shot-") for f in os.listdir(d))
    has_md=os.path.exists(os.path.join(d,"DESIGN.md"))
    todo.append({"slug":slug,"mode":"vision" if has_shots else "distill" if has_md else "thumb"})
json.dump(todo,open(f"{LIB}/data/profile_worklist.json","w"),indent=1)
from collections import Counter
print(len(todo),"to do:",Counter(t["mode"] for t in todo))
PY
```
Expected: ~404 items; modes ≈ vision 340, distill 64 (MD-only brands), thumb 0.

- [ ] **Step 2: Run the profile workflow (resumable batches)**

Workflow over the worklist, agent per site:
- mode **vision**: profile-prompt.md with all screenshots of that site (page dirs' first image each + shot-*.jpg; cap 8 images). KNOWN_META = style code from style_map.json + category/tagline from `$LIB/media/REFERENCE.md` line + meta.json if present.
- mode **distill**: prompt variant — "Read `$LIB/media/<slug>/DESIGN.md` (authoritative analysis). Write the SAME schema profile in your own words, compressing it. Do not copy sentences verbatim."
Each agent writes `profiles/sites/<slug>.md` and returns `DONE <slug>`.
Run in batches of ~50; after each batch re-run Step 1's script — count must shrink; interrupted runs resume for free.

- [ ] **Step 3: Validate the full set**

```bash
python3 - <<'PY'
import os,re
LIB=os.path.expanduser("~/.claude/design-library")
MEDIA=os.path.join(LIB,"media"); SKIP={"design","app-icons","og-images"}
folders={s for s in os.listdir(MEDIA) if os.path.isdir(os.path.join(MEDIA,s)) and s not in SKIP}
profiles={os.path.splitext(f)[0] for f in os.listdir(f"{LIB}/profiles/sites") if f.endswith(".md")}
missing=folders-profiles
bad=[]
for p in sorted(profiles):
    t=open(f"{LIB}/profiles/sites/{p}.md").read()
    if not (t.startswith("---") and "primary:" in t and "## Signature" in t): bad.append(p)
print("missing:",len(missing),sorted(missing)[:10]); print("malformed:",len(bad),bad[:10])
assert not missing and not bad
print("ALL",len(profiles),"PROFILES VALID")
PY
```
Expected: `ALL 407 PROFILES VALID` (404 + 3 calibration).

- [ ] **Step 4: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: full site profile corpus (407 profiles)"
```

---

### Task 5: Style playbooks (Phase 3)

**Files:**
- Create: `$LIB/playbooks/styles/{minimal-light,dark-tech,dark-neon,colorful-playful,illustration,big-type,elegant-serif,photo-driven,gradient-mesh}.md`

**Interfaces:**
- Consumes: `profiles/sites/*.md` (Task 4), `data/style_map.json`.
- Produces: 9 playbooks; SKILL.md maps codes → filenames: ML→minimal-light, DT→dark-tech, DN→dark-neon, CP→colorful-playful, IL→illustration, BT→big-type, EL→elegant-serif, PH→photo-driven, GR→gradient-mesh.

- [ ] **Step 1: Run the style-synthesis workflow**

9 agents; each gets the list of its style's profile files (from style_map.json) and this prompt:

````
Read these design profiles (Read tool, ALL of them): <paths>
Synthesize playbooks/styles/<NAME>.md:
# <Human Name> Style Playbook
> Coverage: N sites from corpus
## Essence            — 3-5 sentences defining the style
## Palette formula    — how canvas/ink/primary/accents behave; 4-6 concrete example palettes (hex, cite slugs)
## Typography formula — families, weights, scales that recur; cite slugs
## Layout & shape     — grids, whitespace, radius, shadows typical here
## Do                 — 6-10 rules grounded in the profiles
## Don't              — 6-10 anti-rules (what would break the style)
## Canonical examples — 8-12 slugs with one-line why
American English. Every formula must cite real slugs.
Write the file, return "DONE <NAME>".
````

- [ ] **Step 2: Verify**

```bash
ls $LIB/playbooks/styles/ | wc -l   # expect 9
grep -L "Coverage:" $LIB/playbooks/styles/*.md; echo "^ empty = OK"
```

- [ ] **Step 3: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: 9 style playbooks"
```

---

### Task 6: Domain layer — design feed, icons, OG (Phase 4)

**Files:**
- Create: `$LIB/profiles/{design.md,icons.md,og.md}` (spec's `apps.md` renamed to `design.md` — matches the actual corpus: the recent.design feed is UI/motion/branding works, not app screenshots)
- Create: `$LIB/playbooks/domains/{websites.md,design-work.md,app-icons.md,og-images.md}`

**Interfaces:**
- Consumes: `$LIB/media/{design,app-icons,og-images}/` flats; REFERENCE.md recent-section for titles/tags.
- Produces: files referenced by SKILL.md domain routing.

- [ ] **Step 1: Sweep agents over the flats (batches of ~25 images)**

design/ (248): 10 agents × ~25 images → each returns entries `- **<file>** — style tags · palette hint · one-line what/why`. Concatenate into `profiles/design.md` grouped by category (from REFERENCE.md). Same pattern: app-icons/ (93, 4 agents) → `icons.md`; og-images/ (49, 2 agents) → `og.md`.

- [ ] **Step 2: Domain playbooks**

4 agents, one per domain: read the domain's profile file (+ for websites: 10 random site profiles) → `playbooks/domains/<domain>.md` with schema: `## When to use this corpus / ## Craft rules (8-12) / ## Best references`. app-icons.md = how to design an app icon (shape language, palette, scalability); og-images.md = how to design share images (contrast at 1200×630, text size, brand block).

- [ ] **Step 3: Verify + commit**

```bash
ls $LIB/profiles/{design,icons,og}.md $LIB/playbooks/domains/
cd $LIB && git add -A && git commit -m "feat: domain profiles and playbooks (design feed, icons, og)"
```

---

### Task 7: catalog.json + validation (Phase 5)

**Files:**
- Create: `$LIB/scripts/build_catalog.py`
- Create: `$LIB/catalog.json`
- Test: `$LIB/scripts/validate_library.py`

**Interfaces:**
- Consumes: profiles frontmatter (Task 2 schema), media dirs, playbooks.
- Produces: `catalog.json`: `{"sites": {"<slug>": {"style","category","website","pages":[],"palette":{"primary":..},"profile":"profiles/sites/<slug>.md","media":"media/<slug>/","has_media":bool}}, "playbooks": {"pages":[...],"styles":[...],"domains":[...]}, "flats": {"design":248,"app-icons":93,"og-images":49}}`. SKILL.md greps this file.

- [ ] **Step 1: Write `scripts/build_catalog.py`**

```python
#!/usr/bin/env python3
"""Build catalog.json from profiles + media. Stdlib-only YAML-lite parser."""
import json, os, re

LIB = os.path.expanduser("~/.claude/design-library")

def frontmatter(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("---"): return {}
    fm = t.split("---", 2)[1]
    d = {}
    d["style"] = (re.search(r'^style:\s*(\S+)', fm, re.M) or [None, None])[1]
    d["category"] = (re.search(r'^category:\s*(.+)', fm, re.M) or [None, None])[1]
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
        if not f.endswith(".md"): continue
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
```

- [ ] **Step 2: Write `scripts/validate_library.py`**

```python
#!/usr/bin/env python3
"""Fail if catalog references anything that doesn't exist."""
import json, os, sys

LIB = os.path.expanduser("~/.claude/design-library")
cat = json.load(open(os.path.join(LIB, "catalog.json")))
errors = []
for slug, s in cat["sites"].items():
    if not os.path.exists(os.path.join(LIB, s["profile"])): errors.append(f"profile missing: {slug}")
    if s["has_media"] and not os.path.isdir(os.path.join(LIB, s["media"])): errors.append(f"media missing: {slug}")
    if not s["style"]: errors.append(f"no style: {slug}")
for sub, names in cat["playbooks"].items():
    for n in names:
        p = os.path.join(LIB, "playbooks", sub, n + ".md")
        if not os.path.exists(p): errors.append(f"playbook missing: {sub}/{n}")
        elif "Coverage:" not in open(p).read(): errors.append(f"no coverage badge: {sub}/{n}")
print(f"{len(errors)} errors"); [print(" -", e) for e in errors[:20]]
sys.exit(1 if errors else 0)
```

- [ ] **Step 3: Run both; expect zero errors**

```bash
python3 $LIB/scripts/build_catalog.py && python3 $LIB/scripts/validate_library.py
echo "exit=$?"
```
Expected: `catalog: 407 sites …`, `0 errors`, `exit=0`. (Domain playbooks have no Coverage badge requirement per schema — if validator flags them, add badges to domain playbooks rather than weakening the validator.)

- [ ] **Step 4: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: catalog.json + library validator"
```

---

### Task 8: The skill — `~/.claude/skills/design-refs/SKILL.md`

**Files:**
- Create: `~/.claude/skills/design-refs/SKILL.md`

**Interfaces:**
- Consumes: everything above via `$LIB` paths.

- [ ] **Step 1: Write SKILL.md (≤150 lines)**

```markdown
---
name: design-refs
description: Use when doing ANY frontend/UI design work — building a new page or component, restyling or editing existing frontend, choosing a visual direction, making an app icon or OG image, or when the user asks for design references, a DESIGN.md, or "make it look like <brand>". Provides evidence: real-site profiles, page-type playbooks, style playbooks, and screenshots from a local corpus of 400+ analyzed sites.
---

# Design References & Intelligence

Library root: `~/.claude/design-library/` (call it $LIB). Machine index: `$LIB/catalog.json`.
Complements the official frontend-design skill: that one sets aesthetic direction;
this one supplies evidence — real palettes, layouts, and rules synthesized from a corpus.

## Routing — decide the task type first

| Task | Do |
|---|---|
| New page/site design | Steps 1-5 below |
| Edit existing frontend | Step 0 first, then 1-5 |
| "Make DESIGN.md for my project / like <brand>" | Generator (below) |
| Analyze a live URL | Live Analyzer (below) |
| App icon / OG image | Read `$LIB/playbooks/domains/{app-icons,og-images}.md` + `$LIB/profiles/{icons,og}.md`, pick 3 refs, view them |
| "Show me references for X" | Steps 1-3, present candidates with paths + URLs, stop |

## Core flow

0. **Existing project?** Read its styling source (tailwind.config, globals.css, tokens)
   → infer current style code (ML/DT/DN/CP/IL/BT/EL/PH/GR). Match, don't fight it.
1. **Classify the request:** page type (home/pricing/blog/…), style, industry.
   Missing style? Infer from product type or ask one short question.
2. **Playbooks first:** Read `$LIB/playbooks/pages/<type>.md` (fallback misc.md)
   and `$LIB/playbooks/styles/<style>.md`. These carry the rules — follow their
   Do/Don't lists as constraints, not suggestions.
3. **Pick 2-4 reference sites:** grep catalog.json by style+category
   (`python3 -c` one-liner or Grep on the file). Prefer sites whose `pages`
   include the target page type. Read their `profiles/sites/<slug>.md`.
4. **Look at real pixels:** if `has_media`, Read 2-3 screenshots from
   `$LIB/media/<slug>/<page>/`. No media → WebFetch the live `website` URL
   or use Live Analyzer.
5. **Apply:** take tokens (palette hex, type families, radius) from ONE primary
   reference profile; take structure from the page playbook; take mood from style
   playbook. Never average palettes across sites — pick one and commit.

## DESIGN.md Generator

On "make a DESIGN.md": pick the closest reference profile (or Live-Analyze the
named brand), then write a DESIGN.md for the USER'S project: YAML frontmatter
(colors/typography/rounded/spacing/components token blocks) + prose sections
(Overview, Colors, Typography, Layout, Components, Do's and Don'ts) following
the schema of $LIB profiles but expanded with the user's brand name, adjusted
hues they asked for, and their framework. Never copy a reference's text verbatim.

## Live Analyzer

For any live URL: screenshot it (Playwright MCP if available: navigate + take_screenshot
at 1440×900, scroll 3-4 viewports) and write a profile using the schema in
`$LIB/scripts/profile-prompt.md`. Offer to save it to `$LIB/profiles/sites/<slug>.md`
so the corpus grows.

## Verify loop

After building UI from references: screenshot the result (run the app / Playwright),
Read it next to the reference screenshots, list mismatches (palette drift, spacing,
type scale), fix, re-check once.

## Budget rules

Load at most: 2 playbooks + 4 profiles + 3 screenshots per task. Playbooks are
small; profiles ~1-2 KB; screenshots are the expensive part — view only finalists.
```

- [ ] **Step 2: Verify the skill is discoverable and paths resolve**

```bash
ls ~/.claude/skills/design-refs/SKILL.md
python3 - <<'PY'
import re,os
t=open(os.path.expanduser("~/.claude/skills/design-refs/SKILL.md")).read()
assert len(t.splitlines())<=150, f"too long: {len(t.splitlines())} lines"
for p in re.findall(r'\$LIB/([a-z/.\-{},]+)', t):
    for piece in (p.split("{")[0],):
        full=os.path.expanduser("~/.claude/design-library/"+piece)
        assert os.path.exists(full.rstrip("/")), full
print("SKILL.md OK, referenced paths exist")
PY
```
Expected: `SKILL.md OK, referenced paths exist`

- [ ] **Step 3: Commit (skills dir isn't the library repo — copy into repo for publishing)**

```bash
cp -r ~/.claude/skills/design-refs $LIB/skill
cd $LIB && git add -A && git commit -m "feat: design-refs skill (router over the library)"
```

---

### Task 9: Maintenance scripts — fetch-media + update-recent

**Files:**
- Create: `$LIB/scripts/fetch_media.py`
- Create: `$LIB/scripts/update_recent.py`

**Interfaces:**
- Consumes: `catalog.json` (Task 7); recent.design tRPC API (`https://api.recent.design/trpc/items.list?batch=1&input=<urlencoded {"0":{limit,feed,sort,direction,cursor}}>`, feeds: websites/all/og-images/app-icons; media at `cdn.recent.design`; getdesign CDN: `https://cdn.getdesign.md/catalog/<slug>/<page>.<webp|jpg>`).
- Produces: idempotent CLI scripts (`--dry-run` flag each).

- [ ] **Step 1: Write `fetch_media.py`** — walks catalog sites with `has_media:false` OR `--all`; for getdesign slugs downloads `cdn.getdesign.md/catalog/<slug>/{<page>.<ext>,thumb,favicon}` (ext detection: try webp/jpg/png with Range GET + Chrome UA — 403 without UA); for recent slugs reads their meta.json URL list. Skips existing non-empty files; `--dry-run` prints the download plan. Reuse the downloader shape from Task 9 reference implementation in session (ThreadPoolExecutor(20), UA header, `.part` + rename).

- [ ] **Step 2: Write `update_recent.py`** — pages the 4 feeds with cursor until known ids appear (state file `data/recent_state.json` holding seen ids), downloads new posters/images into the flat dirs + new site folders, appends stubs to `data/profile_worklist.json` so the next profile run picks them up. `--dry-run` prints what's new.

- [ ] **Step 3: Test both in dry-run**

```bash
python3 $LIB/scripts/fetch_media.py --dry-run | tail -3
python3 $LIB/scripts/update_recent.py --dry-run | tail -3
```
Expected: fetch: "0 files to download" (media complete); update: "N new items" (0+, no crash).

- [ ] **Step 4: Commit**

```bash
cd $LIB && git add -A && git commit -m "feat: media fetch + recent.design updater scripts"
```

---

### Task 10: End-to-end acceptance (spec success criteria)

**Files:** none (verification only; fixes committed where found)

- [ ] **Step 1: Scenario A — new page.** Prompt (fresh context or subagent): "Сделай pricing-страницу для dev-tools продукта в тёмном стиле". Verify the skill triggers, loads `playbooks/pages/pricing.md` + `playbooks/styles/dark-tech.md`, cites 2+ profiles, and the produced HTML uses a palette from a real profile (not invented purple-on-white).
- [ ] **Step 2: Scenario B — edit.** In any existing project with styling: "поправь hero-секцию". Verify Step 0 fires (reads project styling before choosing refs) and chosen refs match the project's style code.
- [ ] **Step 3: Scenario C — generator.** "Сгенери DESIGN.md для моего проекта как Linear". Verify output has YAML token blocks + prose sections and is NOT a copy of any library profile text.
- [ ] **Step 4: Scenario D — validator green.** `python3 $LIB/scripts/validate_library.py` → exit 0.
- [ ] **Step 5: Final commit + tag**

```bash
cd $LIB && git add -A && git commit -m "chore: acceptance pass" --allow-empty && git tag v0.1.0
```

---

## Self-review notes

- Spec coverage: page playbooks (T3), style playbooks (T5), profiles (T2+T4), generator+analyzer+verify (T8), catalog+validation (T7), maintenance/public scripts (T9), acceptance (T10). Cloud media install — out of scope per spec.
- Spec deviation recorded: `profiles/apps.md` → `profiles/design.md` (corpus reality), noted in Task 6.
- Type consistency: profile schema fields (style/category/website/pages/palette.primary) used identically in T2 schema, T4 validator, T7 parser, T8 skill.
```
