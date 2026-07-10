---
name: glyphy
kind: site
style: CP
category: text-utility
website: https://glyphy.io/
pages: [home, tool-index (font generator), symbol-browser, name-generator, emoticon-browser, blog]
palette:
  canvas: "#F5F0DB"
  ink: "#111111"
  primary: "#111111"
  accents: ["#F2A93B", "#E13A22", "#C81E3C", "#A31C33", "#6E1E3C"]
typography:
  display: "ultra-bold condensed grotesque (Druk-like) · heavy/black · tight, all-caps"
  body: "monospace (Space Mono / JetBrains Mono feel) · regular · wide mono spacing"
radius: "pill on buttons/chips/inputs; large 16px+ on cards and tiles"
---
## Overview
Glyphy is a cream-and-black brutalist-playful utility site: a warm off-white canvas, near-black ink everywhere, and a hot amber-to-maroon stripe gradient reserved for the home hero. Headlines are shouty ultra-bold condensed caps; all UI copy, labels, and breadcrumbs are set in monospace, giving a terminal-meets-poster feel. Small katakana eyebrow labels (フォント, シンボル, もっと見る) sit above section headings as a decorative signature. The characters themselves — fancy fonts, symbols, kaomoji — do the visual heavy lifting inside mostly monochrome frames.

## Layout
Sticky black top bar with white mono nav links, active link shown as a cream pill; EN/ES language pills at right. Home hero is a stack of full-width horizontal color bars (amber, red, crimson, maroon), one per tool, each with a "TRY NOW" pill at the right edge. Every section follows the same rhythm: katakana eyebrow + giant condensed all-caps heading, then either a dense grid (symbol tables, emoticon chips) or a mosaic of alternating black/cream showcase cards with tiny "VIEW ->" pills. Tool pages open with an H1, a full-width pill-shaped text input, then the content grid; each page closes with an "EXPLORE ..." cross-link card grid. Link lists are 3-4 column rows with small circular arrow buttons. Black footer bar mirrors the header.

## Components
Buttons: black pill with cream mono text ("GENERATE", "TRY NOW", "COPY", "VIEW ->"), inverted to cream-on-black inside dark cards; no shadows anywhere. Inputs: full-width pill with 1px black border on cream, mono placeholder. Cards: large-radius rectangles, either solid black with cream glyph art or cream with a thin 1px black border; corner metadata in tiny mono caps (label top-left, pill CTA top-right, caption bottom-left). Symbol browser is a hairline-ruled table grid, one glyph per cell. Emoticon and filter chips are outlined pills; selected filter chip fills black. Circular icon buttons (arrow, plus) accompany list links.

## Signature
- Stacked full-width color bars (amber → red → crimson → maroon) as the home hero navigation
- Ultra-bold condensed all-caps display type paired with monospace for literally everything else
- Katakana eyebrow labels above English section headings
- Flat 1px-border cream/black cards with corner-anchored mono labels and pill CTAs; zero shadows
- Pixel/bitmap display font for @username showcase cards

## Do
- Keep the palette to cream + black by default and spend the warm accent colors only on large flat bands or fills, never on small UI details
- Set all microcopy, nav, labels, and breadcrumbs in monospace caps or lowercase mono
- Alternate solid-black and bordered-cream cards within the same grid for rhythm
- Use pill shapes for every interactive element: buttons, inputs, chips, language toggles
- Let the content glyphs (symbols, kaomoji, fancy fonts) be the imagery; frame them large and centered in cards

## Don't
- Don't add drop shadows, gradients, or glassmorphism — the site is strictly flat with 1px hairlines
- Don't use colored text links or colored buttons; CTAs are black (or inverted cream) pills only
- Don't introduce a humanist or rounded body face — the mono/condensed-grotesque pairing is the identity
- Don't soften the density: symbol and emoticon grids are tightly packed tables, not airy card layouts
- Don't use photography except as small inset media (blog thumbnails, ad slots); the canvas stays typographic
