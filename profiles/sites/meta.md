---
name: meta
kind: site
style: ML
category: consumer-hardware
website: null
pages: [homepage, product-detail, buy-now-configurator, accessory-subpage]
palette:
  canvas: "#ffffff"
  ink: "#1c1e21"
  primary: "#0064e0"
  accents: ["#000000", "#0457cb", "#a121ce", "#f7b928", "#f1f4f7", "#0a1317"]
typography:
  display: "Optimistic VF (proprietary; nearest: Montserrat) · medium 500 with light-300 editorial subheads · neutral tracking, ss01+ss02 alternates on"
  body: "Optimistic VF · 16px/1.5 · slight negative tracking (-0.16px)"
radius: "pill (100px) buttons and chips; medium-to-large cards (16px standard tiles, 32-40px photo showcases); small 8px inputs"
---
## Overview
A white-canvas hardware storefront where oversized product photography does the visual heavy lifting and everything else stays quiet. One proprietary typeface (Optimistic VF) runs from 64px heroes down to 12px legal copy, and the whole geometry vocabulary is soft: pill buttons, heavily rounded photo tiles, circular swatches. The trick that makes it Meta is a split CTA color code — black pills sell the story on marketing pages, cobalt blue pills close the sale in checkout flows.

## Layout
Sticky white top bar (~64px, hairline bottom border) with the wordmark left, pill-shaped category tabs center, and a pill search field plus circular icon buttons right; a dark or yellow promo strip can sit above it. Heroes are full-bleed photos filling 50-70% of the viewport with white overlaid headline and a dual-CTA pair (black filled + outlined ghost). Content runs in a ~1280px container with 80px gaps between marketing sections, tightening to 64px on product pages. PDPs split roughly 58/42: thumbnail strip + large gallery on the left, sticky purchase card on the right (collapsing to a sticky bottom bar under 768px). Feature content lands in 3- and 4-up grids with 24px gutters.

## Components
Buttons are always pills, never squared: black fill (#000000, white label, 14px/700 text) for marketing, cobalt #0064e0 fill strictly inside buy flows (pressed → #0457cb), 2px ink-outlined ghost as the paired secondary. Cards come in two registers — chromeless 32px-radius photo tiles where the image is the whole surface, and bordered (1px #dee3e9) 16px-radius tiles for icons/FAQ/testimonials; shadows appear only on the sticky checkout summary. Inputs are 44px tall, 8px radius, 1px gray border that turns 2px blue on focus. Selection controls (radio cards, SKU tiles) signal state with a 2px deep-cobalt or ink border. Badges are tiny colored pills (yellow promo, green stock, red error).

## Signature
- Two-tier CTA color code: black pill = marketing, cobalt pill = commerce; cobalt never leaks onto brand pages
- Chromeless photo cards with 32-40px corner rounding — no borders or shadows, photography is the surface
- One variable typeface everywhere, with a distinctive light-300 weight for editorial subheads between 500 displays and 400 body
- Pill everything: buttons, nav tabs, search field, badges all at 100px radius

## Do
- Keep #0064e0 exclusive to purchase actions (add to cart, configure); use black pills for all marketing CTAs
- Round every button, tab, and badge to a full pill; give photographic cards at least 32px corners
- Enable ss01+ss02 stylistic sets together on all Optimistic VF headings
- Use the 300-weight 28px subhead to break rhythm between heavy display lines and body copy
- Let product photos own the space — flat surfaces, hairline #dee3e9 dividers, shadows only on sticky purchase panels

## Don't
- Don't put cobalt buttons on marketing pages or black buttons in the checkout rail — the split is the brand code
- Don't add accent colors beyond cobalt and the Quest purple; the chrome stays monochrome, color lives in photos
- Don't square off buttons or drop card rounding below 16px anywhere
- Don't shadow marketing cards — elevation reads as "checkout" in this system
- Don't tighten 16px body below 1.5 line-height; its negative tracking already runs snug
