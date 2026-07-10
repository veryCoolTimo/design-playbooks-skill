---
name: linear.app
kind: site
style: DT
category: dev-tools
website: null
pages: [home, pricing, contact-sales, changelog, intake]
palette:
  canvas: "#010102"
  ink: "#f7f8f8"
  primary: "#5e6ad2"
  accents: ["#828fff", "#0f1011", "#141516", "#23252a", "#8a8f98", "#27a644"]
typography:
  display: "Linear Display (custom sans; sub: Inter/SF Pro Display) · semibold 600 · strong negative tracking (up to -3px at 80px)"
  body: "Linear Text (custom sans; sub: Inter), regular 400, slight negative tracking"
radius: "buttons small 8px · cards medium 12px, screenshot panels 16px · pills only for tabs/badges"
---
## Overview
The darkest canvas in the library: an almost-black background (#010102, faintly blue-tinted, deliberately not pure #000) with pale gray type and a single lavender-blue accent doled out sparingly. Depth comes from a stepped ladder of charcoal surfaces edged with 1px hairlines instead of shadows or gradients. High-fidelity screenshots of the Linear app itself are the visual centerpiece; the marketing chrome exists mainly to frame them.

## Layout
Sticky 56px top nav on the raw canvas: wordmark left, links center, "Sign in" (charcoal) plus lavender primary CTA right; collapses to hamburger under 768px. Hero opens with an 80px/600 headline and heavily negative tracking, followed by a full-width product-screenshot panel. Sections repeat that pattern — screenshot panel first, copy second — spaced ~96px apart within a ~1280px container. Card grids run 3-up, dropping to 2-up at 1024px and 1-up under 768px. The dark canvas itself acts as whitespace; sections are distinguished by lifting content onto lighter surfaces, not by background color changes.

## Components
- Buttons: compact 8px 14px padding, 8px corners, 14px/500 labels. Primary is flat lavender #5e6ad2 (hover lightens to #828fff, pressed #5e69d1); secondary is charcoal #0f1011 with a hairline border; an occasional pure-white inverse button appears on section openers. Never pill-shaped.
- Cards: #0f1011 fills, 1px #23252a borders, 12px corners, 24px padding; featured/hovered variants lift one surface step to #141516. Screenshot panels get 16px corners and a faint white top-edge highlight. No drop shadows.
- Inputs: same charcoal fill and 8px corners; focus is a 2px lavender outline at ~50% opacity, not a fill change.
- Small parts: pill toggles for pricing tabs (selected = surface lift), pill status badges, hairline-ruled changelog rows.

## Signature
- Near-black #010102 canvas with a five-level charcoal surface ladder plus hairlines carrying all depth — zero shadows, zero gradients.
- One chromatic color total: lavender-blue reserved for the CTA, brand mark, focus rings, and link emphasis.
- Product UI screenshots framed in 16px-radius dark panels lead every section.
- Display type at 600 weight with aggressive negative tracking, contrasted by positively tracked 13px eyebrows.

## Do
- Keep #010102 (blue-tinted near-black) as the only page background; step up through #0f1011 → #141516 → #18191a for hierarchy without skipping levels.
- Spend lavender only on the primary button, brand mark, focus states, and rare link emphasis.
- Cap display weight at 600 against 400 body, and track display sizes hard negative (~4% of size).
- Give every section a real product screenshot as its lead visual.
- Border cards with 1px hairlines (#23252a) instead of shadows.

## Don't
- Don't substitute true #000000 for the canvas or offer a light theme.
- Don't fill sections or cards with lavender, or add any second accent hue on marketing surfaces.
- Don't add glows, atmospheric gradients, or spotlight-style cards — depth is surface steps only.
- Don't pill-round CTAs; pills belong only to tab toggles and status badges.
- Don't push display type to 700+ weight or loosen its tracking to neutral.
