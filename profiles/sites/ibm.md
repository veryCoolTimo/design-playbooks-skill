---
name: ibm
kind: site
style: ML
category: enterprise-technology
website: null
pages: [home, product, consulting, community]
palette:
  canvas: "#ffffff"
  ink: "#161616"
  primary: "#0f62fe"
  accents: ["#f4f4f4", "#e0e0e0", "#525252", "#0043ce", "#002d9c", "#da1e28", "#24a148"]
typography:
  display: "IBM Plex Sans · light (300) at 42-76px · slightly negative tracking (-0.4 to -0.5px)"
  body: "IBM Plex Sans · regular 400 with +0.16px tracking"
radius: "none (0px on buttons, cards, inputs alike)"
---
## Overview
A strict Carbon Design System execution: white pages, charcoal text, and exactly one chromatic accent — IBM Blue #0f62fe. Everything is square and flat; hierarchy comes from 1px hairlines and gray surface bands, never shadows. The typographic signature is Plex Sans at weight 300 for huge headlines, which makes the whole page feel restrained rather than shouty.

## Layout
Two-tier chrome: a slim 32px gray utility bar sits above a 48px sticky white nav with a bottom hairline. Page flow runs hero (light-weight headline) → 4-up feature card grid → customer logo marquee → product/tab sections → blue CTA banner → charcoal footer, the page's only dark surface. Built on Carbon's 16-column grid (max ~1584px) and a 4px spacing base; sections separate with subtle #f4f4f4 bands rather than big vertical air — content stays deliberately dense.

## Components
Buttons are square 0px-radius blocks, 14px/400 labels, 12x16px padding: blue solid primary (pressed shifts to #002d9c), charcoal solid secondary, white-with-blue-border tertiary, ghost text-plus-chevron, red danger. Cards are flat white or #f4f4f4 tiles with 1px #e0e0e0 borders and zero shadow, 24-48px interior padding by scale. Inputs sit on #f4f4f4 with square corners; focus swaps the bottom hairline for a 2px blue underline. Tabs use a bottom hairline, with a 2px blue underline plus 600-weight label when selected.

## Signature
- Absolute 0px corners everywhere — even a 4px radius reads as off-brand
- Display headlines at weight 300, not bold, in IBM Plex Sans
- Single blue accent rationed to CTAs, links, focus underlines, and one CTA banner
- Depth via 1px hairlines and canvas-to-gray surface swaps; no drop shadows or gradients (save a faint blue hero wash)

## Do / Don't
Do:
- Keep every button, card, input, and container at 0px radius
- Set 42px+ headlines in Plex Sans 300 and body in 400 with the +0.16px tracking
- Ration #0f62fe to primary CTAs, links, focus underlines, and the CTA banner
- Alternate #ffffff and #f4f4f4 bands for section rhythm; separate cards with 1px #e0e0e0 borders
- Write eyebrows and labels in sentence case at 14px
Don't:
- Don't use pill or even slightly rounded buttons — squares are the brand
- Don't set display type at 600-700 weight; it collapses into generic-enterprise
- Don't add drop shadows, gradient panels, or pastel section blocks
- Don't introduce a second brand color; green/yellow/red exist only as status semantics
- Don't dark-invert any surface except the #161616 footer
