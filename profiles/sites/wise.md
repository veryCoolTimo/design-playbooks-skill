---
name: wise
kind: site
style: BT
category: fintech
website: null
pages: [home]
palette:
  canvas: "#e8ebe6"
  ink: "#0e0f0c"
  primary: "#9fe870"
  accents: ["#e2f6d5", "#163300", "#ffc091", "#38c8ff"]
typography:
  display: "Wise Sans (proprietary; sub with Inter 900 / Manrope 800-900) · black 900, chunky geometric · neutral tracking"
  body: "Inter · 400/600, tight negative tracking on Inter headings"
radius: "large 16px+ (24px on buttons AND cards; 12px inputs; pill badges)"
---
## Overview
A money-transfer brand that dresses like a calm Scandinavian editorial rather than a bank. One lime-green accent (#9fe870) does all conversion work against sage-tinted neutrals and a warm olive-cast near-black. Headlines land at 900 weight in a proprietary display face scaled up to 126px, while Inter quietly handles everything below hero level.

## Layout
White sticky nav over a sage (#e8ebe6) hero band; hero splits headline-left / currency-converter-card-right on desktop, stacking on mobile. Sections alternate as full-bleed color bands — sage hero, white content band, dark ink footer — with ~48px vertical padding and a ~1200px centered container. Feature grids run 2-up or 3-up; elevation comes from surface contrast (white cards floating on sage), not shadows. Photography is rare; illustrative SVGs and product mockups fill cards instead.

## Components
Primary button: lime #9fe870 fill, near-black label, 24px radius, ~48px tall. Secondary reuses the sage surface; tertiary is white with a 1px ink outline. Cards are 24px-radius rectangles in four skins: white, sage, pale green (#e2f6d5), and a polarity-flipped dark card with lime text. Inputs sit at 12px radius with a 1px ink border on white. Status badges are full pills; the bordered currency-converter card is the one interactive hero widget. Nothing carries a drop shadow by default.

## Signature
- Weight-900 display type at extreme scale (64-126px) — the hero is never set lighter
- Lime #9fe870 as the single, exclusive action color; no competing accent exists
- Sage-green-tinted canvas with white cards — surface contrast replaces shadows as elevation
- Polarity flips: dark ink surfaces with lime headlines for promotional moments

## Do
- Keep every primary CTA on lime #9fe870 with near-black text; it is the only conversion color
- Set hero headlines at weight 900 (Inter Black or Manrope 800+ as substitutes)
- Round buttons and cards to 24px uniformly; inputs step down to 12px
- Alternate sage bands and white cards so contrast, not shadow, signals depth
- Use the separate semantic green (#2ead4b family) for success states, not the brand lime

## Don't
- Don't add a second accent color; orange/cyan appear only inside illustrations
- Don't drop hero weight to 700 or below — the black weight IS the identity
- Don't square off CTAs or cards; sharp corners break the friendly voice
- Don't place the lime CTA on a green background — it always sits on sage, white, or ink
- Don't reach for drop shadows; the system is flat with hairline borders at most
