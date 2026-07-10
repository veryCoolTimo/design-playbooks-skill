---
name: apple
kind: site
style: PH
category: consumer-electronics
website: null
pages: [homepage, environment, store, product-buy, accessories]
palette:
  canvas: "#ffffff"
  ink: "#1d1d1f"
  primary: "#0066cc"
  accents: ["#f5f5f7", "#272729", "#000000", "#2997ff", "#0071e3"]
typography:
  display: "SF Pro Display (Inter as fallback) · semibold 600 · tight negative tracking"
  body: "SF Pro Text, system-ui, -apple-system, sans-serif"
radius: "pill on all CTAs and inputs; large 18px on utility/store cards; small 8px on nav utility buttons; 0 on full-bleed tiles"
---
## Overview
Product photography is the entire show; the interface stays out of the way. Pages are stacks of full-bleed viewport-height tiles that flip between white/off-white and near-black, each holding a centered headline, a short tagline, one or two small blue pill CTAs, and a crisp product render. One blue (#0066cc) handles all interactivity; there are no decorative gradients, and the only shadow in the system sits under product imagery.

## Layout
Two-row nav: a 44px true-black global bar with 12px links, plus a 52px frosted (blurred parchment) sub-nav carrying the product name and a right-aligned pill CTA. Sections are edge-to-edge tiles with ~80px vertical padding and zero gap — the light/dark surface flip is the divider. Content locks around 1440px for grids and ~980px for prose; store and accessories use 3-5 column card grids with 20-24px gutters. Whitespace is generous everywhere except the footer, which goes intentionally dense with relaxed 2.41 line-height link columns.

## Components
Primary button: Action Blue pill, white 17px regular text, 11x22px padding, presses with scale(0.95), keyboard focus gets a 2px #0071e3 outline. Secondary CTA is a ghost pill — blue text, 1px blue border. Nav utility buttons are dark #1d1d1f rects at 8px radius. Store/accessory cards: white, 1px #e0e0e0 hairline, 18px radius, 24px padding, no shadow — the render inside carries the lone product shadow (rgba(0,0,0,0.22) 3px 5px 30px). Configurator chips and the search input are pills too; a translucent gray 44px circle handles controls floating over photos. Sticky bars use 80%-opacity parchment with backdrop blur.

## Signature
- Alternating full-bleed light/dark tiles where the color change itself is the section break — no borders, no dividers.
- Exactly one accent (blue #0066cc) and exactly one shadow (under product renders), everything else flat.
- Headlines at weight 600 with negative letter-spacing; body at 17px (not 16) with 1.47 leading — the "tight display, roomy body" pairing.
- Pill shape as the universal "this is actionable" cue: CTAs, chips, even the search field.

## Do / Don't
Do:
- Route every link, CTA, and focus signal through #0066cc; swap to #2997ff only for links sitting on dark tiles.
- Track display headlines tight (roughly -0.28 to -0.37px) at weight 600, never 700.
- Break section rhythm by switching surface (white -> #f5f5f7 -> #272729) instead of adding chrome.
- Use scale(0.95) as the press state on every button.
- Keep pure black for the global nav and video frames only.

Don't:
- Don't put shadows on cards, buttons, or text — the drop-shadow belongs to product photography alone.
- Don't add gradients; atmosphere must come from the imagery itself.
- Don't use weight 500 anywhere — the ladder is 300/400/600/700.
- Don't round the full-bleed tiles or squeeze body line-height below 1.47.
- Don't invent a second accent color or mix radius grammars (pill for actions, 18px for cards, 8px for utility).
