---
name: meech213
kind: site
style: ML
category: photography-portfolio
website: https://www.meech213.com/
pages: [home]
palette:
  canvas: "#F1EFE7"
  ink: "#141414"
  primary: "#141414"
  accents: ["#8C8A82", "#E8D9CE"]
typography:
  display: "high-contrast didone serif (Playfair/Didot feel) · regular weight at large size · normal-to-slightly-tight tracking"
  body: "neutral grotesque sans (Helvetica/Inter feel)"
radius: "none"
---
## Overview
A gallery-as-canvas portfolio: editorial photos and magazine covers float as slightly rotated, print-style cards drifting across a warm off-white field. Chrome is nearly absent — a bold condensed "213 MEECH" logotype top center, tiny uppercase social links top right, and a ghosted fan of serif nav words at bottom center. The imagery itself carries all the color; the interface stays cream, black, and quiet.

## Layout
No header bar. Fixed corner anchors: a rotated handwritten-style "IT'S MEECH'S TIME" tag top-left, stacked uppercase sans links (EMAIL / TWITTER / FACEBOOK / INSTAGRAM, right-aligned) top-right, logo centered at top, and a one-line footer (copyright left, "Site by TBP" right). The center of the viewport is a free-form spatial collage: 3-5 photo cards per view at varying scale, each tilted 2-8 degrees, some cropped by the viewport edges to imply an infinite pannable canvas. Navigation is a radial fan of large serif words (PHOTO / VIDEO / HOME / ABOUT / BOOK) at bottom center — the active item ("HOME") in solid ink, the rest ghosted to roughly 10-15% opacity, with a thin compass-needle line pointing from a center dot toward the active item. Whitespace dominates; there is no grid, no sections, no scroll rhythm — spatial drift replaces vertical flow.

## Components
No conventional buttons, inputs, or CTAs anywhere on the home page — links are bare text. Cards are the sole component: sharp-cornered (0 radius) photo rectangles with either no border or a thin white print-style border (seen on the black-and-white portrait, shot-02, and the beauty crop, shot-04), a soft diffuse drop shadow suggesting paper lifted off the surface, and a slight rotation transform. Nav words behave as text links with an opacity state model: active = full ink, inactive = ghosted. Social links are small uppercase sans, no underline.

## Signature
- Tilted, shadowed "print on a table" photo cards scattered on a cream void, some bleeding off-screen — a pannable collage instead of a page.
- Radial fan navigation: five big didone-serif words arranged in an arc at bottom center with a needle line indicating the active one.
- Extreme chrome minimalism: zero buttons, zero fills, zero rules — hierarchy done entirely with opacity, scale, and rotation.
- A rotated, offhand "IT'S MEECH'S TIME" mark in the top-left corner as a persistent personality stamp.

## Do / Don't
Do:
- Keep the canvas a warm paper cream (#F1EFE7), never pure white, and let photos supply all saturation.
- Rotate every image card a few degrees, give it a soft drop shadow, and let some cards crop off the viewport edge.
- Render nav as large serif words differentiated only by opacity (active near-black, inactive ~12%).
- Keep utility text (socials, footer) tiny, uppercase or sentence-case grotesque sans, pinned to corners.
- Use thin white matte borders on select photos to reinforce the printed-photograph metaphor.

Don't:
- Add filled buttons, pills, outlines, or any conventional CTA styling — this site has none.
- Introduce rounded corners on cards or images; everything is razor-edged print stock.
- Lay content out in a vertical section grid or add dividing rules — the composition is free-floating and spatial.
- Use accent colors in the UI chrome; ink black on cream is the entire interface palette.
- Center-align body copy blocks or add hero headlines — the logo and floating imagery are the hero.
