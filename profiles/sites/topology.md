---
name: topology
kind: site
style: DT
category: venture-capital
website: https://www.topology.vc/
pages: [home, about, principles, team, public-goods]
palette:
  canvas: "#131313"
  ink: "#C9C6BF"
  primary: "#E8E6E0"
  accents: ["#E8955C", "#8FB8E8", "#B9A7E0", "#A8C98F"]
typography:
  display: "neo-grotesque sans (Helvetica Now / Neue Haas feel) · light-to-regular weight · tight, near-default tracking"
  body: "monospace (IBM Plex Mono / JetBrains Mono feel) for paragraphs and nav; small caps nav with wide tracking"
radius: "none"
---
## Overview
An immersive, cinematic venture site built on full-bleed 3D iridescent topology renders — grainy, holographic contour ripples that fill the viewport edge to edge. The hero opens light and washed-out, then the site settles into a near-black charcoal canvas where warm off-white type carries everything. There is almost no chrome: no cards, no filled buttons, no borders — just type, numbers, and the 3D field.

## Layout
- Nav: minimal top bar — wordmark "Topology" left, five uppercase monospace links right (ABOUT / PRINCIPLES / TEAM / PUBLIC GOODS / CAREERS), active link underlined. Nav floats directly over the 3D render with no background bar.
- Hero: full-viewport 3D render with a huge light-weight grotesque headline bottom-left ("Meet us at the edge.") and a short mono-adjacent subline beside it; footer strip with "TOPOLOGY ©2026" left and "EXPLORE ↓" right, separated by a thin hairline rule.
- Scroll narrative: sequential full-screen 3D scenes with single centered phrases ("You jump…", "We jump…") that fade in/out — story told one line per viewport.
- Content sections alternate left/right in a staggered two-column rhythm: numbered index ("01.", "02.", "03.") beside a large grotesque heading, with a narrow monospace paragraph below. Enormous vertical whitespace between blocks; each section gets most of a viewport.
- Section titles ("Team", "Public goods") appear as lone centered light-weight headings floating in dark space. Team members shown as dim, desaturated portrait cutouts in a three-across row. Custom thin scrollbar indicator on the right edge.

## Components
- Buttons: effectively none — CTAs are plain uppercase mono text links ("EXPLORE ↓") or headings with a trailing thin arrow glyph ("Neuro Map →"). No fills, no borders, no radius.
- Cards: none; list items are number + heading + mono paragraph, separated purely by whitespace.
- Links: nav links dim by default, active state underlined; arrows are hairline-weight.
- Text reveals: paragraphs animate in with a per-line brightness ramp (later lines dimmer), giving a scroll-progress feel.
- Rules: single hairline horizontal divider above the hero footer strip; otherwise no borders anywhere.

## Signature
- Full-bleed grainy iridescent 3D contour/ripple renders (pastel rainbow spectral edges on white-to-dark surfaces) as the entire background of every scene.
- Pairing of a light-weight neo-grotesque display face with monospace body and nav text.
- Numbered editorial sections ("01. What we do") staggered left/right across huge dark whitespace.
- Light-to-dark arc: washed-out bright hero dissolving into a near-black interior world.

## Do
- Use one full-viewport 3D/generative visual per scene and let type float directly on it — no panels or overlays boxes.
- Set body copy and nav in monospace at small sizes; reserve the grotesque for large display lines only.
- Keep CTAs as bare uppercase mono text with arrows or underlines — never filled buttons.
- Number sections (01., 02., 03.) in small mono and alternate their horizontal alignment.
- Add film grain/noise to imagery and keep accent color inside the artwork, not the UI.

## Don't
- Don't introduce cards, borders, shadows, or rounded containers — the site has zero box chrome.
- Don't use saturated UI accent colors for text or controls; type stays warm off-white on charcoal.
- Don't use bold or heavy display weights; headlines are light/regular even at 100px+ sizes.
- Don't pack sections — each content block earns most of a viewport of empty dark space.
- Don't put a solid background behind the nav; it sits transparently on the artwork.
