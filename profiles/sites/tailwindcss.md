---
name: tailwindcss
kind: site
style: DT
category: developer-tools
website: https://tailwindcss.com/
pages: [home, home-light-mode]
palette:
  canvas: "#030712"
  ink: "#999fad"
  primary: "#394053"
  accents: ["#38bdf8", "#ec4899"]
typography:
  display: "Inter · medium-to-semibold · very tight (tracking-tighter)"
  body: "Inter"
radius: "pill buttons; large 16px+ cards"
---
## Overview
A near-black (#030712) developer-tool landing page that turns its own layout system into decoration: hairline grid rule lines with diagonal-striped gutters stay visible across the whole page, and tiny monospace utility-class annotations (e.g. `text-8xl text-white tracking-tighter`) float above real headings. Typography does the heavy lifting — enormous, tightly tracked Inter headlines in pure white against deep navy-black. Color is disciplined: the UI itself is monochrome, with sky blue reserved for inline code tokens and vivid hues confined inside demo content. A light mode exists as an exact structural mirror on #ffffff with near-black ink.

## Layout
- Slim single-row nav: logo + small pill version badge ("v4.0") left; search field with ⌘K hint, Docs / Components / Blog / Showcase text links, GitHub icon right. No nav CTA button.
- Hero is left-aligned inside an exposed column grid: two-line text-8xl headline, short subhead with blue mono code tokens, then a pill CTA + pill quick-search input side by side. No hero imagery — a mac-chrome code editor panel with syntax-highlighted HTML sits directly below, paired with a live component preview.
- Section rhythm: small bold section kicker ("Built for the modern web.") + short gray paragraph, then a bento grid of feature cards in varied spans (1/2, 1/3, full-width). Rotated monospace labels run vertically along the page edge in accent colors.
- Mid-page: full-width dark code/terminal panel; masonry collage of real site screenshots for the showcase section; angled isometric spread of UI templates for the Tailwind UI promo; multi-column link footer.

## Components
- Primary CTA: fully rounded pill, neutral fill — gray-700 (#394053) with white label in dark mode, solid black (#0e0e0e) in light mode. Never brand-blue.
- Search input: pill, hairline border, left magnifier icon, right ⌘K keycap hint; reads as a twin of the CTA.
- Feature cards: rounded-2xl (~16px), 1px low-contrast border, flat — no drop shadows; each card embeds a working demo (photo listing card, dark-mode phone UI, color-palette grid, code editors, team combobox, gradient swatches).
- Code panels: darker inset surface (#101423-ish) with mac traffic-light dots, line numbers, blue/sky syntax highlighting; identical in both themes.
- Inline code in prose: monospace, sky blue (#38bdf8-range), no background chip.

## Signature
- The exposed grid: persistent hairline column/row rules with diagonal-striped gutter bands — the page looks like it is rendered on its own blueprint.
- Monospace utility-class captions annotating live elements, making the framework itself the visual motif.
- Massive tracking-tighter Inter headlines, sentence case with a period, flush left.
- Neutral pill CTA + pill search pair; sky blue appears only in code tokens and the logo, never as a button fill.
- Bento feature cards that are functioning product demos, not illustrations.

## Do / Don't
Do:
- Keep the canvas extremely dark (#030712) and let 1px borders, not shadows, separate surfaces.
- Set headlines huge (text-7xl/8xl scale) with strongly negative letter-spacing and pure white (or near-black in light mode) fill.
- Use pill radius for all interactive controls and ~16px radius for cards.
- Confine saturated color to code syntax, demo content, and small rotated section labels; keep chrome monochrome.
- Mirror dark and light modes structurally 1:1 — only surface and ink values flip.

Don't:
- Don't make the primary CTA blue or gradient — it stays neutral gray/black even though the brand color is sky blue.
- Don't add drop shadows, glows, or glassmorphism to cards; the aesthetic is flat hairline-bordered panels.
- Don't hide the grid — the visible rule lines and striped gutters are the identity, not a construction artifact.
- Don't use decorative stock imagery in the hero; the product (code + rendered result) is the hero.
- Don't center the hero; everything is left-aligned on the column grid.
