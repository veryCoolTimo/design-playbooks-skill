---
name: lovable
kind: site
style: GR
category: ai-dev-tools
website: null
pages: [landing]
palette:
  canvas: "#f7f4ed"
  ink: "#1c1c1c"
  primary: "#1c1c1c"
  accents: ["#fcfbf8", "#eceae4", "#5f5f5d"]
typography:
  display: "Camera Plain Variable (humanist sans) · semibold 600 · tight negative tracking (-0.9 to -1.5px)"
  body: "Camera Plain Variable, ui-sans-serif fallback"
radius: "buttons small 6px · cards medium 12-16px · icon actions pill"
---
## Overview
A warm, paper-like aesthetic that dodges the cold white of typical dev-tool sites: everything rests on a cream canvas with near-black charcoal type. Every gray on the page is the same charcoal at reduced opacity, giving the whole site one coherent tonal family. Softness comes from a faint multi-hue gradient wash (pinks, oranges, blues) behind the hero and footer rather than from bold color. The custom humanist typeface, run tight at large sizes, gives headlines an editorial, notebook-like confidence.

## Layout
Fixed horizontal nav on cream, wordmark left, dark CTA right, hamburger under 768px. Hero is a centered single column with heavy vertical padding and the atmospheric gradient behind it. Content caps around 1200px; feature areas run 2-3 column grids, template showcases as card galleries, plus a horizontal big-number stats bar. Section rhythm is lavish — 80-208px vertical gaps do the separating instead of divider lines.

## Components
Buttons: dark charcoal fill with off-white text, 6px radius, 8x16px padding, and a signature multi-layer inset shadow (hairline white highlight on top, dark 0.5px ring, faint drop); ghost variant uses a 1px charcoal-40% border; active state simply drops to 0.8 opacity; focus is a diffuse soft shadow, not an outline. Cards match the page background and are contained by 1px #eceae4 borders at 12px radius with no drop shadow. Inputs share the cream fill and #eceae4 border, 6px radius, blue Tailwind focus ring. Icon/action toggles (voice, plan mode) are full pills. Links stay charcoal and signal interactivity via underline, not color shift.

## Signature
- Cream #f7f4ed canvas everywhere — page, cards, and inputs all share it, so borders alone define containment
- One-hue gray system: every neutral is #1c1c1c at some opacity (0.03 to 0.83)
- Tactile inset shadow on dark buttons — pressed-in feel instead of floating elevation
- Camera Plain Variable at 48-60px, weight 600, aggressively negative letter-spacing; weight range never exceeds 600

## Do / Don't
Do:
- Keep the whole page on #f7f4ed and separate cards with 1px #eceae4 borders instead of shadows
- Build every gray by dialing #1c1c1c opacity, not by picking new hex values
- Recreate the layered inset shadow on primary dark buttons — it is the tactile hallmark
- Scale negative tracking with headline size: -1.5px at 60px down to -0.9px at 36px
- Reserve pill radius for icon buttons and toggles; standard buttons stay at 6px

Don't:
- Don't swap the cream for pure white — the warmth is the brand
- Don't add saturated accent colors; the palette is deliberately warm-neutral
- Don't go heavier than weight 600 or add drop shadows to cards
- Don't use hard focus outlines — focus is a soft diffuse shadow (ring blue only on form inputs)
- Don't mix border roles: #eceae4 for passive containment, rgba(28,28,28,0.4) for interactive edges
