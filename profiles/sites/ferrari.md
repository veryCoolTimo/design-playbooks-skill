---
name: ferrari
kind: site
style: EL
category: luxury-automotive
website: null
pages: [homepage, model-pages, f1-racing, preowned-listings, pricing, lifestyle]
palette:
  canvas: "#181818"
  ink: "#ffffff"
  primary: "#da291c"
  accents: ["#303030", "#969696", "#f6e500", "#fff200"]
typography:
  display: "FerrariSans (sub: Inter) · medium 500, never bold · tight negative tracking (-0.36 to -1.6px)"
  body: "FerrariSans (sub: Inter), 400, secondary text in #969696 on dark"
radius: "none (0px buttons and cards); small 4px on form inputs only; pill reserved for tiny badges"
---
## Overview
Dark cinematic editorial: a near-black warm canvas carries white display type at medium weight, with full-viewport photography doing the emotional work while typography stays restrained. Rosso Corsa red appears only where it counts — CTAs, the horse mark, race-position numbers. White bands surface only for utilitarian editorial content like preowned listings and pricing. The whole system reads like a printed luxury magazine translated to screen.

## Layout
Slim 64px top nav (logo left, uppercase menu with 0.65px tracking, utilities right; hamburger below 768px). Pages open on a chromeless full-bleed hero photo with an 80px/500 headline floating over the lower edge, paired with one red CTA plus one outline CTA. Below, a ~1280px 12-column editorial body alternates dark bands, an occasional full-width red "livery" band, and white listing/pricing bands. Sections breathe on a named 8px ladder (4→128px), with 96px band padding as the norm. Card grids run 4/3/2/1-up down the breakpoints. Depth comes from photography and brightness steps (#181818 → #303030 → white), not shadow stacks; dividers are 1px hairlines.

## Components
Buttons: 48px tall, hard 0px corners, 14px/700 uppercase labels tracked 1.4px; primary fills #da291c (pressed #b01e0a), secondary is transparent with a 1px white (or ink-on-light) border, tertiary is a tracked uppercase text link. Cards: sharp-cornered, either photo-first flush to the edge on #181818, or #303030 elevated panels (driver cards) with 24px padding — hairline outlines, one soft hover shadow at most. Inputs: 48px, 4px radius, hairline border, dark or light variants. Badges are the sole pill shape (11px/600 uppercase on #303030). Big-number spec cells set values at 80px/700; F1 finishing positions render the same numerals in brand red.

## Signature
- Full-bleed cinematic car photography acting as the page chrome itself — heroes have zero padding and no competing UI.
- One red (#da291c) used with extreme scarcity against a warm near-black floor; nothing else saturated.
- Display type stays at weight 500 with negative tracking — confidence without shouting — while CTAs/nav go uppercase with wide tracking.
- Razor-sharp 0px corners on every button, card, and band.

## Do / Don't
Do:
- Keep #da291c exclusively for primary CTAs, the brand mark, and race-position highlights.
- Cut every CTA and card at 0px corners; set button labels uppercase, 700, 1.4px tracking.
- Lead each page with an edge-to-edge photograph and let the headline float over its lower third.
- Stick to the named 8px spacing ladder (96px for major bands, 128px for hero depth).
- Hold display headings at weight 500; save 700 for buttons, small titles, and giant spec numerals.

Don't:
- Don't add a second saturated hue — yellow belongs only to the Hypersail sub-brand and focus rings.
- Don't round or pill any CTA; pills exist only as tiny badges.
- Don't bold headline copy or let type compete with the photography.
- Don't drop to pure #000000 — the canvas is a slightly warm #181818.
- Don't build shadow-tier elevation; step surface brightness and use 1px hairlines instead.
