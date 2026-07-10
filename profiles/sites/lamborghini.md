---
name: lamborghini
kind: site
style: EL
category: automotive
website: null
pages: [home, event, news]
palette:
  canvas: "#000000"
  ink: "#FFFFFF"
  primary: "#FFC000"
  accents: ["#917300", "#FFCE3E", "#29ABE2", "#3860BE", "#1EAEDB", "#202020", "#7D7D7D"]
typography:
  display: "LamboType (custom neo-grotesque, 12° angled terminals) · regular weight, huge scale · normal tracking, tight leading"
  body: "LamboType, fallback Roboto/Helvetica Neue; Open Sans in some form contexts"
radius: "none (0px on buttons and cards; 20px toggles are the lone exception)"
---
## Overview
A pitch-black, cinematic showroom: the entire site sits on true #000000 with white type and a single gold accent doing all the work. Full-viewport video heroes and giant uppercase headlines set in a bespoke neo-grotesque give it the feel of cars presented under spotlights at night. Depth comes from stepping between dark surface tones, never from shadows or gradients.

## Layout
Header is chrome-free: transparent over black, bull logo centered, "MENU" hamburger left, search/bookmark icons right — hamburger at every breakpoint. Heroes are 100vh video with dimmed edges and a thin white progress line at the bottom. Content sits in a Bootstrap 12-column grid capped around 1200-1440px; heroes break full-bleed. Sections breathe via large black gaps (48-56px vertical padding) — darkness serves the role whitespace plays elsewhere. Grids collapse 3 → 2 → 1 columns; display type scales 120 → 80 → 40px.

## Components
Buttons are hard-edged rectangles, zero radius. Primary CTA: solid #FFC000 fill, black text, 24px padding, darkens to #917300 on hover. Secondary: transparent ghost with 1px white border at 50% opacity, uppercase small text, hover fills #1EAEDB. Color-only state changes — no scale/translate motion. Cards: #202020 panels or full-bleed photos with white overlay text, no radius, no shadow; elevation is expressed by lightening the surface (#000 → #181818 → #202020). Tiny gray badges (#969696, 2px radius) and a hexagon-outlined video pause control are the only ornament. Forms are nearly absent; toggles are the sole pill-shaped element.

## Signature
- True black canvas everywhere, with gold (#FFC000) reserved strictly for the primary CTA
- ALL-CAPS display type at extreme sizes (up to 120px) with sub-1.0 line-height, set at weight 400
- Zero border-radius across buttons, cards, and images — deliberately angular
- Hexagonal geometry recurring in icons and the video pause button, echoing the custom typeface's construction

## Do
- Keep the background pure #000000 — never substitute a soft dark gray
- Spend gold only on the main action button; everything else stays black/white/gray
- Set headlines uppercase at regular weight with very tight leading (0.92-1.19)
- Convey elevation by lightening surface color instead of adding shadows
- Let full-bleed video and photography carry the drama; keep UI minimal and flat

## Don't
- Don't round corners on buttons or cards, or add gradients/glows to surfaces
- Don't introduce a second accent hue — the black-plus-gold system is the identity
- Don't animate hovers with scale or movement; shift only color/opacity
- Don't use bold weights or italics for headlines — scale and caps do the shouting
- Don't crowd sections with many small elements; each block should be one bold statement
