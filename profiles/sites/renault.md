---
name: renault
kind: site
style: PH
category: automotive
website: null
pages: [home, vehicle-listing, configurator, campaign]
palette:
  canvas: "#ffffff"
  ink: "#000000"
  primary: "#ffed00"
  accents: ["#000000", "#e6d200", "#f7f7f7", "#111111"]
typography:
  display: "NouvelR (subs: Inter Tight / Manrope) · bold 700 · zero tracking, very tight 0.95 line-height"
  body: "NouvelR · regular 400"
radius: "small 2-6px (buttons at 2px); none on cards/tiles; pill reserved for sub-nav chips and badges"
---
## Overview
A hard black-on-white automotive system where full-bleed car photography does the talking and a single Sunlight Yellow (#ffed00) marks only the most important actions. Every character on the page is set in one proprietary grotesque (NouvelR) at either 400 or 700, headlines compressed to a 0.95 line-height. Depth comes from swapping entire bands between white and black, not from shadows or gradients.

## Layout
White 60px top bar with the diamond mark left, nav links center, account/language right; collapses to hamburger under 1024px. Full-bleed dark hero with a 56px bold headline stacked left over photography. Below, sections alternate white catalogue bands and black storytelling bands at ~80px vertical rhythm, with an occasional solid-yellow tile as punctuation. Homepage uses a 2-up square promo-tile grid; vehicle ranges run 3-4 cards per row. Configurator splits ~60/40: fixed visual pane left, scrolling option rows (hairline-divided) right. Max width ~1440px; bands extend edge to edge beyond it.

## Components
Buttons: 48px tall, 2px corners, bold ~14px labels with hairline letter-spacing; primary is yellow fill with black text (pressed darkens to #e6d200), secondary is solid black, tertiary a 1px black outline on white. Pills (46px radius) exist only as sub-nav filter chips and "NEW" badges. Cards and promo tiles are perfectly square-cornered, shadow-free, photo on top with copy stacked below — never overlaid. Inputs are borderless except a single black bottom hairline, square, 48px tall. Circular shapes appear only as 56px configurator paint swatches.

## Signature
- One yellow element per viewport, always carrying black text — CTAs, "NEW" badges, or a lone accent tile
- Monofont discipline: NouvelR everywhere, 400/700 only, display lines packed at 0.95 leading
- Square-cornered full-bleed car photography; elevation via white/black band inversion instead of shadows
- Catalogue precision on white: #f2f2f2 hairline row dividers, dense but ordered

## Do
- Keep yellow scarce: main CTA, NEW badge, at most one accent tile per band, always with black text on it
- Alternate full-width white and black sections for pacing; close every page on a black footer
- Set headlines bold 700 with line-height clamped to ~0.95, body strictly 400
- Give all standard buttons the 2px corner; keep cards and photos at 0px
- Place copy below vehicle photos inside cards, not on top of them

## Don't
- Don't add a second accent color or use semantic reds/greens decoratively
- Don't round car cards, promo tiles, or photography — square edges are the brand
- Don't put white text on yellow, or use 500/600 weights for body copy
- Don't cast drop shadows on tiles or cards; the catalogue layer is flat
- Don't use mid-grey section backgrounds or faint grey body text on white
