---
name: nike
kind: site
style: PH
category: sportswear-retail
website: null
pages: [home-category, product-listing, product-detail, membership, collection-landing]
palette:
  canvas: "#ffffff"
  ink: "#111111"
  primary: "#111111"
  accents: ["#f5f5f5", "#d30005", "#007d48", "#ed1aa0", "#0a7281"]
typography:
  display: "Nike Futura ND (sub: Bebas Neue/Anton) · medium, massive uppercase at 0.9 line-height · zero tracking"
  body: "Helvetica Now Text / Text Medium (sub: Inter 400/500)"
radius: "pill on all buttons/chips (30px+); none on cards, tiles, nav, imagery"
---
## Overview
A retail system where photography carries all the emotion and the UI stays deliberately mute. Giant uppercase Futura headlines are set directly over full-bleed campaign photos, while the surrounding chrome is pure black, white, and one soft gray. Chromatic color only shows up where it means something: red sale prices, green confirmations, small category-tint chips. The overall feel is a printed athletic catalog stacked vertically.

## Layout
Two-tier header: a 36px gray utility strip (store/help/sign-in) above a white 56-64px nav with centered links, swoosh left, and a gray search pill plus icons right; active nav link gets a 2px black underline. Pages stack in 48px section rhythm: cinematic hero with burned-in headline, then 3-4-up product grids with tight 8px gutters, horizontal-scroll sport rails, and a hairline-divided footer. Listing pages add a ~220px filter rail and a breadcrumb/sort sub-strip. Content maxes near 1440px; whitespace comes from the gray photo backdrops rather than layout padding.

## Components
Buttons are exclusively pills: black fill with white label (48px tall, the sole primary per fold), gray #f5f5f5 secondary, and a crisp white pill anchored bottom-left on imagery; pressed state shrinks and fades (scale 0.5, 50% opacity) rather than recoloring. Filter chips flip fully inverted (white to solid black) when selected — no intermediate state. Search is a 24px-radius gray pill that turns white on focus with a 2px black border and a soft gray halo. Product cards are radius-zero, shadow-zero, padding-zero: a square photo on #f5f5f5 with name, muted subtitle, and price stacked below at 8px gaps; 12px colorway dots get a concentric black-ring selected state. Depth is limited to 1px hairlines and an inset bottom line under sticky bars — no drop shadows anywhere.

## Signature
- Enormous 96px uppercase display type (0.9 line-height) composited straight onto hero photography, in white or black chosen per image
- Every product staged on the same #f5f5f5 "studio" square inside flat, borderless cards
- Two-shape button vocabulary only: pill and circle — nothing squared
- Red appears solely as sale-price text next to a struck-through gray original; never as a filled badge or chrome color
- "Tap collapse" pressed feedback (scale + opacity) instead of color-shift states

## Do
- Keep the 96px display tier for campaign heroes only; section headers drop straight to 32px medium Helvetica
- Allow one solid-black pill per viewport; demote extras to the gray secondary or white on-image pill
- Set photos full-bleed on the #f5f5f5 backdrop and let the bleed edge act as the section divider
- Hold 48px vertical rhythm between sections (32px tablet, 24px mobile) with no decorative separators
- Put the on-image CTA as a white pill at the tile's bottom-left, every time

## Don't
- Don't add drop shadows or card elevation — hairlines and the inset sticky-bar line are the only depth cues
- Don't use the pink/purple/teal category tints for buttons, text, or chrome; they live in swatches and soft editorial tiles
- Don't soften the CTA to charcoal — the primary pill is true #111111
- Don't pad or round product cards; the photo is the card
- Don't run two campaign lockups side by side at equal scale; alternate one editorial tile with a product/category grid
