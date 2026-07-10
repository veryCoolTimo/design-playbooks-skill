---
name: spacex
kind: site
style: PH
category: aerospace
website: null
pages: [home, shop, vehicle-detail, human-spaceflight, mission]
palette:
  canvas: "#000000"
  ink: "#ffffff"
  primary: "#000000"
  accents: ["#f0f0fa", "#0a0a0a", "#3a3a3f"]
typography:
  display: "D-DIN-Bold (condensed industrial DIN sans) · heavy 700 · wide positive tracking (0.96-1.6px), compressed 0.95 leading, always uppercase"
  body: "D-DIN regular (Arial fallback), 16px, relaxed 1.5-1.7 leading"
radius: "pill 32px buttons; small 4-8px inputs and shop cards"
---
## Overview
A near-total reduction: pure black pages where full-viewport rocket and Mars photography (or autoplay launch video) does all the decorative work, topped by one uppercase D-DIN-Bold headline and one outlined pill CTA per band. No accent hue exists — black, white, and the imagery itself form the whole palette. The effect is a film title card rather than a product page: engineered, austere, mission-first.

## Layout
Fixed top nav rendered transparent over the hero photo — white wordmark left, caps micro-links right, no opaque bar, collapsing to hamburger under 768px. Marketing pages skip containers entirely: each section is a full-bleed, roughly viewport-height photo/video band with a centered ~1200px type column laid directly on the image. Whitespace is photographic (dark sky, empty Martian terrain), not padding. The shop is the exception: white canvas, a 4/2/1-up product grid, and conventional 48-64px section padding. Display type stair-steps 80 → 60 → 48 → 40px across breakpoints.

## Components
Buttons: a single ghost pill per marketing band — transparent fill, 1px white border, white uppercase 13px/700 label with ~1.17px tracking, 18x24px padding, 32px radius; never filled, never doubled. Filled buttons (pale cool #f0f0fa fill, black text, same pill) appear only on shop product cards. Shop cards: white, 8px radius, 1px #e0e0e8 hairline, 16px padding, photo-top with bold price — no shadow anywhere on the site. Inputs: white, 4px radius, hairline border, 12x16px padding. Links keep a persistent underline in the surface's text color. Zero drop shadows, glows, or gradient scrims; when type needs contrast the photo itself is graded darker.

## Signature
- 80px uppercase D-DIN-Bold hero headline with wide positive tracking and crushed 0.95 line-height, set straight onto ungraded-looking photography with no scrim.
- One ghost-outlined white pill CTA per band — the only marketing button that exists.
- Transparent nav floating over imagery; every chrome label (nav, eyebrows, buttons) is all-caps microtext with positive tracking.
- Strict black/white chromatics — every other color on screen comes from a photograph.

## Do / Don't
Do:
- Make every marketing section a full-bleed photo or autoplay video band; the image is the section.
- Set all display type uppercase in a condensed DIN-style bold (or Inter 700 + 1.6px tracking as a stand-in) with tight leading.
- Limit each band to exactly one outlined pill CTA with an uppercase tracked label.
- Keep the nav transparent white-on-image, including when fixed on scroll.
- Grade the photograph darker when text needs contrast instead of adding an overlay layer.

Don't:
- Don't add any accent color — the black/white-only rule is structural to the brand.
- Don't apply shadows, glows, or gradient scrims over the dark canvas.
- Don't set headlines in sentence or title case, or in a humanist/serif face.
- Don't place filled or paired CTAs on marketing bands; fills belong only to shop cards.
- Don't inset marketing photography into cards or enforce aspect ratios — imagery always runs edge to edge.
