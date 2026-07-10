---
name: airbnb
kind: site
style: PH
category: travel-marketplace
website: null
pages: [home, listing-detail, search-results, footer]
palette:
  canvas: "#ffffff"
  ink: "#222222"
  primary: "#ff385c"
  accents: ["#e00b41", "#f7f7f7", "#dddddd", "#6a6a6a"]
typography:
  display: "Airbnb Cereal VF (Circular fallback; Inter as substitute) · modest 500-700, small display sizes (22-28px) · near-neutral tracking, slightly negative on larger heads"
  body: "Airbnb Cereal VF, 400 at 14-16px"
radius: "buttons small 8px; cards medium ~14px; search bar and badges pill"
---
## Overview
Photography does the heavy lifting on an almost entirely white page: near-black #222222 text, hairline gray dividers, and exactly one hot color — Rausch #ff385c — reserved for primary CTAs, the circular search orb, and saved-heart states. Headlines are deliberately quiet (28px max on the homepage), because listing photos and card grids carry the hierarchy. Every interactive surface is rounded; the only right angles are in the layout grid itself.

## Layout
An 80px white top nav holds the wordmark left, three centered product tabs (Homes / Experiences / Services) with 32px illustrated icons and tiny "NEW" pills, and account utilities right; the active tab gets a 2px ink underline. The hero is not a banner but a giant pill search bar segmented by hairlines into Where / When / Who, capped by a Rausch orb. Below, dense photo-card grids (4-up desktop, 16px gutters) alternate with 64px section bands — open at the top, packed with inventory below. Listing pages run two columns: content at ~64% and a sticky bordered reservation card at ~32%. Content maxes around 1280px; the footer is white like the page, three text columns with no contrast band.

## Components
Primary buttons: Rausch fill, white 16px/500 label, 8px radius, 48px tall; press state darkens to #e00b41, disabled fades to #ffd1da. Secondary buttons are white with a 1px ink outline; tertiary actions are plain underlined-on-hover ink text. Cards are photo-first: ~14px corner clipping on the image, carousel dots, a white pill "Guest favorite" badge top-left, heart top-right, then 4-5 short meta lines — no card border or resting shadow. Inputs are 56px white fields with 8px radius and a 1px hairline that thickens to 2px ink on focus (no glow ring). Exactly one shadow recipe exists (a soft three-layer lift) shared by hovered cards, the search bar, and dropdowns; everything else is flat.

## Signature
- One brand color (#ff385c) used sparingly — most screens are 90% white and ink with a single Rausch moment.
- The pill search bar terminating in a circular red orb; the most recognizable search UI in consumer travel.
- Small, mid-weight headlines that defer to photography; the lone typographic flex is a 64px rating number flanked by laurel ornaments on listing pages.
- Star ratings rendered in ink, never gold.

## Do / Don't
**Do**
- Keep the canvas pure white end to end, including the footer, and separate sections with 1px #dddddd hairlines instead of tinted bands.
- Round everything interactive: 8px buttons, ~14px card corners, full pills for search, badges, and icon buttons.
- Let photos carry weight — clip images to the card radius and keep meta text to a few 14px lines beneath.
- Reserve Rausch for the primary CTA, search orb, and saved hearts; use #222222 for nearly all other emphasis.
- Cap elevation at the single soft shadow tier, applied only on hover, the search bar, and dropdowns.

**Don't**
- Don't inflate headlines past ~28px or push weights to 800+ — the system reads wrong with typographic muscle.
- Don't introduce a second accent color or gradients; sub-brand purples/magentas stay out of mainline pages.
- Don't use gold/yellow stars or colored rating chips — ratings are ink.
- Don't stack multiple shadow depths or give resting cards borders and shadows.
- Don't add a dark or tinted footer; Airbnb's footer matches the page canvas.
