---
name: design-playbooks
description: Use when doing ANY frontend/UI design work — building a new page or component, restyling or editing existing frontend, choosing a visual direction, making an app icon or OG image, or when the user asks for design references, a DESIGN.md, or "make it look like <brand>". Provides evidence - real-site profiles, page-type playbooks, style playbooks, and screenshots from a local corpus of 400+ analyzed sites.
---

# Design References & Intelligence

Library root: `~/.claude/design-library/` (call it $LIB). Machine index: `$LIB/catalog.json`
(v2 — search it with `scripts/find.py`, don't hand-grep). Complements the official
frontend-design skill: that one sets aesthetic direction; this one supplies evidence —
real palettes, layouts, and rules synthesized from a corpus of 407 analyzed sites,
248 design works, 93 app icons, 49 OG images.

The corpus is a July-2026 snapshot; sites redesign. Trust the live URL over an old
profile when they disagree, and offer to re-run Live Analyzer.

## Routing — decide the task type first

| Task | Do |
|---|---|
| New page/site design | Steps 1-5 below |
| Edit existing frontend | Step 0 first, then 1-5 |
| "Make DESIGN.md for my project / like <brand>" | Generator (below) |
| Analyze a live URL | Live Analyzer (below) |
| App icon | Read `$LIB/playbooks/domains/app-icons.md` + `$LIB/profiles/icons.md`, view 3 refs from `$LIB/media/app-icons/` |
| OG / share image | Read `$LIB/playbooks/domains/og-images.md` + `$LIB/profiles/og.md`, view 3 refs from `$LIB/media/og-images/` |
| Motion/branding/print inspiration | grep `$LIB/profiles/design.md` by tag, view refs from `$LIB/media/design/` |
| "Show me references for X" | Steps 1-3, present candidates with paths + URLs, stop |

## Style codes

ML=minimal-light · DT=dark-tech · DN=dark-neon · CP=colorful-playful · IL=illustration ·
BT=big-type · EL=elegant-serif · PH=photo-driven · GR=gradient-mesh
Playbook file = `$LIB/playbooks/styles/<full-name>.md` (e.g. DT → dark-tech.md).

**Valid filter values** (use these exactly — don't invent):
- **category:** developer-tools · ai-ml · productivity · design-creative · crypto-web3 ·
  media-consumer · fintech · marketing-sales · hardware · health · data-analytics ·
  ecommerce-retail · security · hr-people
- **tone:** light · dark   · **page:** home pricing blog product about resources solutions
  company features use-cases (others live in `misc.md`)

## Core flow

0. **Existing project?** Read its styling source (tailwind.config, globals.css, design
   tokens) → infer the current style code. Match it — don't fight the existing language.
1. **Classify the request:** page type, style code, category (from the lists above),
   tone (light/dark). Missing style? Infer from product type or ask one short question.
2. **Playbooks first:** Read `$LIB/playbooks/pages/<type>.md` (fallback `misc.md`)
   and `$LIB/playbooks/styles/<style>.md`. These carry the rules — treat their
   Do/Don't lists as constraints, not suggestions.
3. **Find reference sites** with the search tool (never hand-grep):
   ```
   python3 $LIB/scripts/find.py --style DT --category fintech --page pricing --diverse
   python3 $LIB/scripts/find.py --tone dark --category crypto-web3 --on-disk pricing
   python3 $LIB/scripts/find.py --keyword gradient --tag animation
   python3 $LIB/scripts/find.py --like stripe          # siblings of a known site
   ```
   Add `--diverse` when picking references to build from — it spreads candidates across
   palettes so your output doesn't converge on the same few sites as everyone else.
   `--on-disk <page>` = only sites whose screenshot of that page actually exists.
   If a filter is too tight the tool auto-loosens and prints a ⚠ note. Rows marked 📷
   have local screenshots. Read the top 2–4 profiles: `$LIB/profiles/sites/<slug>.md`.
4. **Look at real pixels:** for a 📷 site, list its real folders first
   (`ls $LIB/media/<slug>/`) then Read 2–3 images. Two layouts exist:
   `media/<slug>/<page>/<page>.<ext>` (most sites) OR flat `media/<slug>/shot-01.jpg…`
   (recent.design sites — check `pages_on_disk` in the catalog, empty list ⇒ flat shots).
   No 📷 → WebFetch the live `website`, or Live Analyzer. `<slug>` and `<slug>-recent`
   are the same brand captured twice — check both.
5. **Apply:** take tokens (palette hex, type families, radius) from ONE primary
   reference profile; structure from the page playbook; mood from the style playbook.
   Never average palettes across sites — pick one and commit.

## Reference, don't replicate (anti-sameness)

The corpus exists to escape generic design, not to make every project look identical.
A reference is a **starting point you adapt**, never a template you clone.

- **Diversify the source.** Use `find.py --diverse` so you don't default to the same
  famous sites every time. Two different projects in the same style should read as
  *siblings, not twins* — rotate which reference you anchor on.
- **Shift the palette.** Don't ship a recolor of the reference. Move the primary's
  hue/saturation toward the user's brand, keep the *relationships* (one CTA color,
  canvas/ink contrast, accent scarcity) — not the exact hexes. The profile's palette
  is a proven structure, not a paint bucket to copy.
- **Adapt the structure.** Take the page playbook's *anatomy* (what sections, what
  order) but vary the execution — section count, hero treatment, component shapes.
  Never reproduce one reference's layout, copy, or components 1:1.
- **Mix, don't mirror.** Tokens from one reference + a signature idea from another +
  the user's own content = something new. Cloning a single site is the failure mode.
- If the user asks for "like <brand>", match the *language* (its signature moves),
  then make it theirs — different content, adjusted color, their name. Not a reskin.

## DESIGN.md Generator

On "make a DESIGN.md": pick the closest reference profile (`find.py --like <brand>` or
Live-Analyze the named brand), then fill `$LIB/scripts/design-md-template.md` for the
USER'S project. Copy hex/font facts from the reference; write all prose yourself for the
user's brand; apply requested hue shifts; substitute proprietary fonts with a free
alternative and note it. Never copy a reference's prose verbatim.

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
