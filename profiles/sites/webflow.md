---
name: webflow
kind: site
style: DT
category: saas-web-platform
website: null
pages: [landing, pricing]
palette:
  canvas: "#ffffff"
  ink: "#080808"
  primary: "#080808"
  accents: ["#7a3dff", "#ed52cb", "#3b89ff", "#ff6b00", "#00d722"]
typography:
  display: "WF Visual Sans Variable (Inter substitute) · semibold ceiling, 500-600 · tight negative tracking (-0.8px at hero scale)"
  body: "WF Visual Sans Variable / Inter, 400-500; Inconsolata for mono captions"
radius: "small 2-6px (buttons 4px); cards medium 8px"
---
## Overview
A white-canvas marketing surface where near-black #080808 does triple duty as CTA fill, heading ink, and brand mark. Color arrives only through a fixed five-hue accent set (purple, pink, blue, orange, green) applied as full-saturation card backgrounds, each tied to a product category. One proprietary sans handles everything from 80px heroes down to 12px mono captions, capped at weight 600. The result reads engineered and professional rather than playful.

## Layout
White sticky top nav with 14px/500 links, hamburger below tablet. Hero is a full-width white band with an 80px/600 headline; some campaign pages flip to a near-black hero. Sections follow a rhythm of eyebrow (15px uppercase, +1.5px tracking) then 44.8px headline then body. Grids: category cards 2-3-up with occasional 2-column spans, pricing 3-up, all collapsing to 1-up on mobile. 32px gutters, generous vertical air, effectively edge-to-edge containers.

## Components
Buttons: 4px radius, ~44px tall, 16px/500 labels; primary is solid #080808 with white text, secondary is white with a 1px #d8d8d8 hairline, plus underlined arrow text-links and circular icon buttons for carousels. Cards: 8px radius, 32px padding, hairline border on white; featured cards get a 5-stop layered drop-shadow (very low per-layer opacity); a dark polarity-flip variant exists for pricing emphasis. Inputs share the button geometry: white, hairline border, 4px radius. Badges use blue #146ef5 and a distinctive 12.8px weight-550 caption.

## Signature
- Five fixed accent hues used only as full-bleed category card fills — never on buttons or links
- Near-black #080808 as the sole conversion color: CTA, headings, wordmark
- Weight ceiling of 600 with negative display tracking; single typeface across all roles
- Tight 4px button radius vs 8px cards; pill shape reserved for circular icon buttons
- Multi-stop layered shadows as the only elevation effect

## Do
- Keep every primary CTA solid #080808 with white text and a 4px radius
- Deploy the five accents as saturated full-card fills, using ink text on green for contrast
- Open sections with an uppercase 15px eyebrow at +1.5px tracking before the headline
- Apply the layered 5-stop shadow recipe to featured/pricing cards, hairline borders elsewhere
- Track hero type negative (-0.8px at 80px) at weight 600

## Don't
- Don't color buttons with the accent hues — accents are surfaces, not actions
- Don't exceed weight 600 anywhere; no bold-700 headlines
- Don't round CTAs into pills; only circular icon containers use full radius
- Don't add a sixth accent or shift the five hues off their fixed values
- Don't swap in a second typeface for display vs body — one family carries all roles
