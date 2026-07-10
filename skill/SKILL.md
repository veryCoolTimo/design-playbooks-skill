---
name: design-refs
description: Use when doing ANY frontend/UI design work — building a new page or component, restyling or editing existing frontend, choosing a visual direction, making an app icon or OG image, or when the user asks for design references, a DESIGN.md, or "make it look like <brand>". Provides evidence - real-site profiles, page-type playbooks, style playbooks, and screenshots from a local corpus of 400+ analyzed sites.
---

# Design References & Intelligence

Library root: `~/.claude/design-library/` (call it $LIB). Machine index: `$LIB/catalog.json`.
Complements the official frontend-design skill: that one sets aesthetic direction;
this one supplies evidence — real palettes, layouts, and rules synthesized from a corpus
of 407 analyzed sites, 248 design works, 93 app icons, 49 OG images.

## Routing — decide the task type first

| Task | Do |
|---|---|
| New page/site design | Steps 1-5 below |
| Edit existing frontend | Step 0 first, then 1-5 |
| "Make DESIGN.md for my project / like <brand>" | Generator (below) |
| Analyze a live URL | Live Analyzer (below) |
| App icon | Read `$LIB/playbooks/domains/app-icons.md` + grep `$LIB/profiles/icons.md`, view 3 refs from `$LIB/media/app-icons/` |
| OG / share image | Read `$LIB/playbooks/domains/og-images.md` + grep `$LIB/profiles/og.md`, view 3 refs from `$LIB/media/og-images/` |
| Motion/branding/print inspiration | grep `$LIB/profiles/design.md`, view refs from `$LIB/media/design/` |
| "Show me references for X" | Steps 1-3, present candidates with paths + URLs, stop |

## Style codes

ML=minimal-light · DT=dark-tech · DN=dark-neon · CP=colorful-playful · IL=illustration ·
BT=big-type · EL=elegant-serif · PH=photo-driven · GR=gradient-mesh
Playbook file = `$LIB/playbooks/styles/<full-name>.md` (e.g. DT → dark-tech.md).

## Core flow

0. **Existing project?** Read its styling source (tailwind.config, globals.css, design
   tokens) → infer the current style code. Match it — don't fight the existing language.
1. **Classify the request:** page type (home/pricing/blog/product/about/…), style code,
   industry. Missing style? Infer from product type or ask one short question.
2. **Playbooks first:** Read `$LIB/playbooks/pages/<type>.md` (fallback `misc.md`)
   and `$LIB/playbooks/styles/<style>.md`. These carry the rules — treat their
   Do/Don't lists as constraints, not suggestions.
3. **Pick 2-4 reference sites:** grep catalog.json by style+category, e.g.
   `python3 -c "import json,os;c=json.load(open(os.path.expanduser('~/.claude/design-library/catalog.json')));[print(s,v['category'],v['palette']['primary'],v['website'] or '') for s,v in c['sites'].items() if v['style']=='DT' and 'fintech' in (v['category'] or '')]"`
   Prefer sites whose `pages` include the target page type. Read their
   `$LIB/profiles/sites/<slug>.md`.
4. **Look at real pixels:** if `has_media`, Read 2-3 screenshots from
   `$LIB/media/<slug>/<page>/`. No media → WebFetch the live `website` URL or Live Analyzer.
5. **Apply:** take tokens (palette hex, type families, radius) from ONE primary
   reference profile; structure from the page playbook; mood from the style playbook.
   Never average palettes across sites — pick one and commit.

## DESIGN.md Generator

On "make a DESIGN.md": pick the closest reference profile (or Live-Analyze the named
brand), then write a DESIGN.md for the USER'S project: YAML frontmatter with token
blocks (colors / typography / rounded / spacing / components) + prose sections
(Overview, Colors, Typography, Layout, Components, Do's and Don'ts). Use the library
profile schema as the base, expand with the user's brand name, requested hue shifts,
and their framework. Never copy a reference's prose verbatim.

## Live Analyzer

For any live URL: screenshot it (Playwright MCP: navigate + take_screenshot at
1440×900, scroll 3-4 viewports, screenshot each) and write a profile using the schema
in `$LIB/scripts/profile-prompt.md`. Offer to save it to
`$LIB/profiles/sites/<slug>.md` so the corpus grows.

## Verify loop

After building UI from references: screenshot the result (run the app / Playwright),
Read it next to the reference screenshots, list mismatches (palette drift, spacing,
type scale), fix, re-check once.

## Budget rules

Load at most: 2 playbooks + 4 profiles + 3 screenshots per task. Playbooks and
profiles are small text; screenshots are the expensive part — view only finalists.

## Maintenance

`python3 $LIB/scripts/update_recent.py` pulls new recent.design items;
`python3 $LIB/scripts/fetch_media.py` restores missing media;
`python3 $LIB/scripts/validate_library.py` checks integrity.
