---
name: hyperliquid
kind: site
style: DT
category: crypto-defi-exchange
website: https://hyperliquid.xyz/
pages: [home, blog-index, product-landing (vaults)]
palette:
  canvas: "#062A21"
  ink: "#EDF7F2"
  primary: "#98F1DE"
  accents: ["#DFF5EE", "#50E3C2", "#0B3B2E"]
typography:
  display: "high-contrast transitional serif (Tiempos/Freight-like) · regular weight at very large sizes · tight, with italic used for emphasis words"
  body: "neo-grotesque sans (Inter/Helvetica-like), small sizes, normal tracking"
radius: "pill on buttons and nav bar; small-to-medium 8-14px on cards"
---
## Overview
Deep forest-green surfaces punctuated by pale-mint sections and mint pill CTAs, with a large literary serif for every headline and a tiny grotesque sans for everything else. Faint concentric ripple/contour lines texture the dark backgrounds. The mood is "quiet luxury for a trading protocol": almost no chrome, huge type, two-tone green throughout — no reds, blues, or gradients outside price data.

## Layout
- Nav: a floating white pill bar containing wordmark left, sparse text links right, and one mint pill CTA ("Launch App"). It sits on the dark canvas with generous top margin.
- Hero: centered serif headline (italic on the key word), one short sans subline, single mint pill CTA, then a large product screenshot on the dark field.
- Sections alternate full-bleed dark green and pale mint (#DFF5EE) bands; each band is a single idea with lots of vertical air.
- Feature lists use thin 1px divider lines (grid of cells) rather than boxed cards; blog uses a 2-then-3 column masonry-ish card grid.
- Closing sections go oversized: a giant pill button ("START TRADING" / "VIEW VAULTS") spanning much of the container, and a footer-scale serif wordmark.

## Components
- Buttons: always pills, flat mint fill (#98F1DE) with dark-green text, no border, no shadow; small in nav, enormous (100px+ tall) as section-closing CTAs.
- Cards: blog cards pair a mint image panel (small radius) with a dark caption block — date in sans, title in italic serif. Vault rows are pale mint rounded rectangles with soft diffuse shadows on the light background.
- Data cells (token price grid): dark tiles with token icon, sans labels, green/red deltas; separated by hairlines, minimal radius.
- Inputs barely appear on marketing pages; embedded app screenshots show dark panels with mint action buttons.
- Iconography: thin-stroke outline icons in mint, no fills.

## Signature
- Serif display headlines with a single italicized word ("Trade perpetuals *seamlessly*", "The evolution of *copy trading*") over a grotesque sans body — a rare serif/sans inversion for crypto.
- Two-green world: everything is dark forest green or pale mint; the CTA color is a paler tint of the background hue, not a contrasting hue.
- Concentric ripple/contour-line background pattern faintly visible on dark sections.
- Floating white pill nav bar and comically oversized pill CTAs at section ends.

## Do
- Set all headlines in a high-contrast serif at large sizes, italicizing one emphasis word; keep body copy in a small neutral sans.
- Alternate full-bleed dark-green and pale-mint horizontal bands to create rhythm; keep each band to one message.
- Use pill shapes for every button, filled with pale mint and dark-green text; scale the final CTA up dramatically.
- Add the faint concentric-line texture to dark sections instead of gradients or imagery.
- Use thin hairline dividers to structure feature grids rather than boxed cards on dark sections.

## Don't
- Don't introduce hues outside the green family for UI (reserve red/green strictly for price deltas in data grids).
- Don't use sharp-cornered or bordered buttons — no outlines, no drop shadows, no gradient fills on CTAs.
- Don't set headlines in bold sans; the serif-at-scale is the identity.
- Don't crowd sections: whitespace is extreme, with single-CTA sections and no multi-column text walls.
- Don't attach the nav to the page edge — it floats as a detached white pill with its own rounding.
