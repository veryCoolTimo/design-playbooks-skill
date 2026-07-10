---
name: fasthtml
kind: site
style: CP
category: dev-tools
website: https://fastht.ml/
pages: [home]
palette:
  canvas: "#F0F0F0"
  ink: "#000000"
  primary: "#000000"
  accents: ["#615AE9", "#38DA78", "#FCB929", "#DE82D1", "#FABEC0", "#2C1728"]
typography:
  display: "bold geometric grotesque (Inter/Aeonik-like) · heavy · slightly tight"
  body: "same grotesque family, regular weight"
radius: "pill buttons; large 16px+ cards"
---
## Overview
A colorful, block-party take on a developer landing page: full-bleed candy-colored section bands (amber, green, periwinkle, orchid pink, dark plum) stacked over a neutral light-gray canvas, with pure black text and black pill CTAs holding it all together. Playful geometric confetti shapes (rounded rectangles, bars, blobs) decorate the hero and footer. Despite the color, content stays centered, sparse, and typographically disciplined.

## Layout
Minimal floating nav: just a black pill logo chip and a "Read docs" pill at top center — no traditional nav bar. Hero is fully center-aligned: three-line bold headline, short paragraph, then a black pill CTA paired with a white pill "Watch intro" video chip. Sections are full-width solid-color bands, each with a tiny uppercase monospace-feel kicker (e.g. "GET STARTED IN MINUTES", "TECH STACK"), a centered bold heading, and either a 3-card row, a stacked accordion, or an icon-tile row. The FAQ band breaks symmetry with a left-aligned heading and right-hand column of question pills. Footer is black with a giant multicolor "FastHTML" wordmark bleeding off the bottom edge.

## Components
Buttons: solid black pills with white text (primary), white pills with dark text (secondary/video chip); small pill tab group ("Components / Dynamic / Reusable / Databases") on the dark section. Cards: flat, shadowless, large-radius (~16-20px) rounded rectangles in lighter tints of their section color (cream cards on amber, mint-white cards on green, lavender pills on periwinkle, pale-pink cards on orchid). FAQ questions are full-width rounded pills. Code sample shown in a dark rounded panel with syntax-colored monospace text. Sample links are large rounded-square icon tiles in alternating brand colors. No visible borders or drop shadows anywhere except the soft-shadowed video chip.

## Signature
- Stacked full-bleed color bands — amber, green, periwinkle, pink, plum — each a self-contained scene with tint-matched cards.
- Abstract rounded-geometry confetti (bars, squares, blobs) in the brand palette scattered around the hero.
- Black pill buttons and a pill-shaped logo chip as the constant anchor across every colorful band.
- Footer with an oversized cropped multicolor wordmark overlapping playful shapes.

## Do / Don't
Do:
- Give each section one saturated fill color and derive its cards as lighter tints of that same hue (cream on amber, pale pink on orchid).
- Keep all text pure black or pure white for contrast against the loud backgrounds; reserve color for surfaces, not type.
- Use pill shape consistently: CTAs, tabs, FAQ rows, and the logo chip are all fully rounded.
- Center content in a narrow column with generous vertical padding inside each band; label sections with tiny uppercase kickers.
- Show real runnable code in a dark rounded panel with syntax highlighting as proof of the product.

Don't:
- Add borders, gradients, or drop shadows to cards — surfaces are flat tint-on-color.
- Use a conventional multi-link nav bar; the header is just a logo chip and one docs pill.
- Color the body text or headings — accent hues never appear in type on this site.
- Let two adjacent bands share a hue; the rhythm depends on alternating contrasting colors.
- Use small or medium radii; anything rounded here is either a large-radius card or a full pill.
