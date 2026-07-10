---
name: gregor-collienne
kind: site
style: ML
category: photography-portfolio
website: https://gregorcollienne.com/
pages: [home]
palette:
  canvas: "#F2F0EA"
  ink: "#141414"
  primary: "#141414"
  accents: ["#F2F0EA"]
typography:
  display: "heavy condensed grotesque (Druk-like) · black/ultra-bold · tight, near-zero tracking, all caps"
  body: "not shown; interface reduces to a single display wordmark and a thin '+' glyph"
radius: "none"
---
## Overview
A warm off-white canvas carries an endless scrolling collage of photographs in a loose staggered grid, with the photographer's name set in enormous black condensed caps pinned to the vertical center of the viewport. Images scroll past and behind the fixed wordmark, so photos continuously occlude and reveal the letters. There is no visible chrome beyond a small "+" crosshair glyph at top center — the work and the name are the entire interface.

## Layout
- Nav: no menu bar; a single "+" icon centered at the top (presumed menu/index toggle). No logo block, no footer seen across six full viewport heights.
- Hero: the whole page is the hero — a fixed, viewport-centered "GREGOR COLLIENNE" wordmark spanning roughly half the screen width, layered under/over drifting photos.
- Grid: roughly six loose columns of portrait- and landscape-oriented photos at varied sizes (~250–320px wide), staggered vertically with generous irregular gaps; outer columns bleed off the left and right edges.
- Rhythm: continuous vertical scroll with no section breaks, headings, or copy — pure image stream. Whitespace between images is large and uneven, giving a pinboard/contact-sheet feel.

## Components
- Buttons: none observed; the only control is a thin 1px-stroke "+" glyph (~30px) in ink black.
- Cards: photos are bare rectangles — zero border, zero shadow, zero radius, no captions, no hover chrome visible in stills.
- Inputs: none.
- Imagery itself is the component system: mixed color and black-and-white editorial/documentary photography at consistent small-to-medium scale.

## Signature
- Fixed giant condensed-caps wordmark that images scroll over and behind, constantly cropping the name.
- Edge-bleeding staggered photo collage on a warm paper-white (#F2F0EA) field with no UI chrome.
- Radical reduction: one glyph of navigation, no text content, no footer, no buttons.
- Strict monochrome interface (black on cream) that lets the photography supply all color.

## Do / Don't
Do:
- Keep the interface to two colors: near-black ink on warm off-white; let photographs be the only saturation.
- Set the identity/wordmark in an ultra-bold condensed grotesque, all caps, tight tracking, and fix it to the viewport center.
- Let images overlap and occlude the wordmark; z-layering is the core visual trick.
- Use hard-edged, shadowless, caption-free images at varied sizes in a loose 5–6 column stagger, bleeding off both edges.
- Leave large, irregular whitespace gaps — the grid should feel scattered, not modular.

Don't:
- Don't add nav bars, footers, labels, or captions — the site shows none.
- Don't round corners, add borders, or drop shadows on images.
- Don't use a pure white (#FFFFFF) background; the canvas is a warm paper tone.
- Don't introduce accent colors, filled buttons, or link styling — there is no CTA anywhere.
- Don't align images to a strict uniform grid or equalize their sizes; uniformity would kill the collage character.
