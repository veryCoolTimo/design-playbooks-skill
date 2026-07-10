---
name: holograph
kind: site
style: DT
category: crypto-infrastructure
website: https://www.holograph.xyz/
pages: [home, community, developers, ecosystem, governance]
palette:
  canvas: "#000000"
  ink: "#EDEDED"
  primary: "#0E0E0E"
  accents: ["#7DE8C3", "#8E7A9C", "#B9C4B0"]
typography:
  display: "Neue Haas / Helvetica-style neogrotesque · bold · tight, slightly negative tracking"
  body: "Same grotesque for paragraphs; monospace (OCR/IBM Plex Mono feel) for labels, captions, and button text"
radius: "none"
---
## Overview
Pure-black terminal-brutalist protocol site. Massive white grotesque headlines sit against #000 with iridescent, holographic-foil 3D renders (purple/mint/chrome ribbons) as the only color. Secondary text, nav items, and buttons are set in small monospace inside hairline-bordered boxes, giving the whole site a schematic, engineering-document character.

## Layout
Top nav: logo left, four monospace links right, each in its own thin-bordered rectangular cell (segmented, table-like). Heroes are left-aligned: an oversized 2-3 line grotesque headline where the last word is filled with holographic foil texture, plus a small right-column monospace annotation prefixed with a glyph. Sections alternate full-bleed 3D/iridescent imagery bands with black content bands; a huge stat ("2 Million+") gets its own band with a tab strip below. Layouts are dense grids of bordered cells (3-up feature cards, an alphabetical ecosystem directory grid, an isometric wireframe architecture diagram on dark). Recurring pre-footer: full-width DISCORD / X / MIRROR cell strip, then a giant extruded-3D HOLOGRAPH wordmark band, then a centered "Omnichain Tokenization Infrastructure" footer with three link columns separated by hairlines.

## Components
Buttons: sharp rectangles, near-black fill (#0E0E0E), 1px light-gray border, small monospace label ("Start Integrating", "Join Discord"); no shadows, no gradients. One selected tab state uses a solid mint (#7DE8C3) fill with black mono text. Cards: black fill, 1px gray hairline border, occasionally a 45-degree notched/clipped corner; internal hairline dividers split header/body/CTA rows. Ecosystem cards: logo top-left, tiny mono category tag top-right, name, description, "Visit X" mono link at bottom. Feature cards on governance use thin outlined isometric wireframe icons (mint, lavender, red line colors). Code block shown on true black with green/purple syntax. No visible inputs; no soft shadows anywhere.

## Signature
- Holographic-foil texture filling the final word of each hero headline, and the extruded chrome/foil 3D HOLOGRAPH wordmark band before every footer
- Everything boxed: nav links, buttons, cards, and social strips all live in 1px hairline-bordered cells on pure black, some with notched corners
- Two-voice typography: huge tight grotesque display vs. tiny monospace for all UI chrome, annotations, and CTAs
- Isometric wireframe architecture diagrams and 3D iridescent ribbon renders as the sole imagery language

## Do / Don't
- Do keep the canvas true #000 and draw structure with 1px gray hairlines instead of background-color shifts
- Do set all buttons, nav items, tags, and captions in small monospace inside sharp bordered rectangles
- Do reserve color for holographic-foil textures, partner logos, and thin wireframe line icons; keep everything else grayscale
- Do use the foil-filled-word treatment on the last line of hero headlines and pair heroes with a small right-side mono annotation
- Don't add border-radius, drop shadows, or gradient buttons — every edge is square (at most a notched corner)
- Don't introduce a saturated solid brand color for CTAs; the only solid fill accent seen is the mint selected-tab state
- Don't use photography or illustration — imagery is strictly 3D renders and isometric wireframes
- Don't center hero copy or loosen headline tracking; heroes are left-aligned, tight, and oversized
- Don't mix in friendly rounded UI kits; the aesthetic is terminal/schematic, not consumer-soft
