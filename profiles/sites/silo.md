---
name: silo
kind: site
style: ML
category: ecommerce-hardware
website: https://www.silosilosilo.com/
pages: [home, product-configurator, cart-bar]
palette:
  canvas: "#ffffff"
  ink: "#757575"
  primary: "#6e6e6e"
  accents: ["#d8d8d8", "#bfbfbf"]
typography:
  display: "Helvetica Neue / neutral grotesque · light-to-regular · wide tracking on uppercase labels"
  body: "Same neutral grotesque (Helvetica Neue-like), regular, gray rather than black"
radius: "none (rows, bars, steppers all square); small 2-6px only on outlined icon glyphs"
---
## Overview
An almost content-free storefront: white pages, silver aluminum product renders floating on the canvas, and a single muted gray for every piece of text. There is no black anywhere — ink, prices, labels, and the checkout bar all live in the same mid-gray band, so the metallic product photography is the only "color." The whole site reads like a spec sheet crossed with a vending machine.

## Layout
- No conventional nav. A small outlined "SILO" monogram sits top-center over a full-bleed hero photo (soft-focus lifestyle shot of the aluminum canisters).
- Below the hero, the page is one vertical scroll of full-width product rows: centered product render, centered uppercase name or size number ("ALUMINUM EDITION", "60", "90"), then a hairline-divided price row.
- Each price row is a three-part strip: large light price ("$19", "$39") flush left, minus / quantity / plus stepper flush right, 1px gray hairlines above and below. Enormous horizontal empty space between them.
- A sticky full-width dark-gray bar pins to the bottom: running total ("$0") left, "CHECKOUT" in tracked uppercase right. Footer has two small outlined icons (logo, Instagram) left and "INFO" right.
- Whitespace is extreme; each product gets roughly a full viewport of air.

## Components
- Primary CTA: the sticky checkout bar itself — flat #6e6e6e fill, white/near-white text, square corners, no shadow, edge-to-edge.
- Quantity stepper: bare "−  0  +" glyphs in the ink gray, no borders, no button chrome, sized as large as the price.
- No cards: products separated only by 1px hairline rules and whitespace; no borders around images, no shadows anywhere.
- No visible inputs or forms in these views; icons are 1.5px-stroke outlines matching the ink gray.

## Signature
- Everything text is the same muted gray — zero black, zero brand color; the silver aluminum is the palette.
- Price + stepper hairline rows that look like a receipt or order form rather than product cards.
- Persistent bottom checkout bar with live total, acting as the only strong block of tone on the page.
- Centered, wide-tracked uppercase labels ("ALUMINUM EDITION", "CHECKOUT") in a light neutral grotesque.

## Do
- Keep all text in one mid-gray (#6e6e6e–#7a7a7a) and let product imagery carry the contrast.
- Separate list items with 1px hairlines and generous vertical padding instead of card borders or shadows.
- Make prices and steppers display-sized (comparable to headings) and push them to opposite edges of the row.
- Use a full-width flat gray sticky bar as the single CTA, with tracked uppercase text.
- Center product renders on pure white with a full viewport of breathing room each.

## Don't
- Don't introduce accent colors, gradients, or black text — the system collapses if anything outcolors the aluminum.
- Don't add button chrome to the steppers (borders, fills, circles); they are bare typographic glyphs.
- Don't round corners on bars or rows; the geometry is strictly rectilinear.
- Don't add a conventional header nav, menus, or breadcrumbs — wayfinding is scroll plus the bottom bar and a lone "INFO" link.
- Don't use bold weights; hierarchy comes from size and tracking, not weight or color.
