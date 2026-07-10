---
name: fal
kind: site
style: CP
category: ai-infrastructure
website: https://fal.ai/
pages: [home, explore, pricing]
palette:
  canvas: "#FFFFFF"
  ink: "#0E0E0E"
  primary: "#0E0E0E"
  accents: ["#7EDFF5", "#B49FE9", "#E9F14D", "#F6C7D2", "#E30D3E", "#6A2BE0"]
typography:
  display: "tight neo-grotesque (Helvetica Now / Neue Haas feel) · heavy 700-900 · tight, near-negative tracking"
  body: "same grotesque at regular weight; fine print and pricing microcopy set in a Computer Modern-style serif"
radius: "none"
---
## Overview
A hard-edged, poster-like developer brand: flat full-bleed color bands (sky cyan, lavender, white) on the marketing site, near-black (#0E0E0E) surfaces on the product pages (explore gallery, pricing). Huge black grotesque headlines sit on saturated backgrounds, decorated with dithered pixel-art sprites (planes, blobs, gears) in purple and yellow. Zero border radius anywhere — everything is a sharp rectangle. Playful color, austere geometry.

## Layout
Sticky top nav: gear logo + wordmark left, text links right, black Log-in and Get Started rectangles at the far right. Home hero is a full-width cyan band with a massive left/center headline, one short subline, and a Documentation + Get started button pair; pixel sprites scatter into the margins and rotate vertical micro-text runs along the edges. Sections alternate as full-bleed color slabs (cyan → white → lavender → white), each with its own strong H2. Feature content is a 2-column card grid; model gallery is a 3-4 column masonry of image tiles on black. Pricing uses a budget-chip row, a slider in a light gray panel, then GPU spec rows and a bordered billing table. Footer is a giant cyan slab with 4 link columns and an oversized ghosted logo/wordmark bleeding off the corner.

## Components
Buttons: sharp rectangles, no radius, no shadow; primary CTA is solid black (#0E0E0E) with white label, secondary is white with thin black border (inverted to white-fill on dark pages). Cards: flat rectangles with hairline borders or flat pastel fills (cyan, lavender) and black text; model tiles are edge-to-edge images with a title, one-line description, and small uppercase tag chips (image-to-image, inference) below. Code sample shown in a dark panel with language tabs and syntax colors. Pricing slider: cyan track with a black square handle inside a flat light-gray panel; budget presets as square chips with the active one filled. Tables use hairline row dividers on black. Small red "NEW" rectangle badges on gallery items.

## Signature
- Dithered pixel-art sprites (paper planes, blobs, gear marks) in violet/yellow scattered across flat cyan and lavender slabs
- Strictly zero border radius — buttons, cards, chips, panels, sliders are all hard rectangles
- Split personality: bright poster-color marketing pages vs. near-black utilitarian product pages, unified by the same type and sharp geometry
- Oversized ghosted gear logo + "fal" wordmark filling the cyan footer
- Serif (Computer Modern-style) fine print against grotesque headings, giving a technical-paper flavor to pricing math

## Do / Don't
Do:
- Build sections as full-bleed flat color slabs (cyan #7EDFF5, lavender #B49FE9, white) with black type
- Keep every corner square: 0px radius on buttons, cards, chips, inputs
- Set headlines huge, heavy, and tightly tracked in black; let them take 3 lines
- Use pixel/dither sprites and rotated micro-text as edge decoration, not as content
- Switch to a near-black canvas for dense tool surfaces (galleries, pricing tables) while keeping the same components

Don't:
- Add rounded corners, gradients, or drop shadows — nothing here is soft or elevated
- Color the primary CTA — it stays solid black (or white on dark), never cyan/purple
- Use the accent colors for text; they are backgrounds and decorations only
- Center-pad content into a narrow column on marketing pages — slabs run edge to edge
- Smooth or anti-alias the decorative sprites; the chunky pixel dithering is the point
