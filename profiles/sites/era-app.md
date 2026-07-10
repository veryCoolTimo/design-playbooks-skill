---
name: era-app
kind: site
style: ML
category: fintech-personal-finance
website: https://era.app/
pages: [home]
palette:
  canvas: "#EDECE4"
  ink: "#1C1C19"
  primary: "#1C1C19"
  accents: ["#C4D5D1", "#B8B5A0", "#C9C3E5", "#E0E36E", "#B9D9C6"]
typography:
  display: "neo-grotesque sans (Sohne/Helvetica Now feel) · medium weight · tight, near-default tracking"
  body: "same neo-grotesque sans, regular weight, small size"
radius: "pill on buttons/chips; medium 8-14px on in-app cards; large 16px+ on phone frames"
---
## Overview
A calm, editorial product page built from full-width muted pastel color bands stacked vertically, bookended by a near-black hero and footer. Almost all visual interest comes from photoreal iPhone mockups showing the app UI, annotated with floating chat bubbles. Color is desaturated and warm (sage, olive, lilac, chartreuse) rather than saturated brand color; type is quiet and small.

## Layout
Top nav is minimal text: lowercase "era" wordmark left, small text links (Home, Features, Pricing, FAQs), single pill "Sign in" button right, all on the black hero. Hero is a split layout: left-aligned headline + short paragraph + QR code ("Get the app") on the left, large centered phone mockup on the right with AI chat bubbles overflowing its edge. Each subsequent feature section repeats the identical formula on a new pastel band: heading + 2-3 line paragraph + QR code on the left, phone mockup right. Sections are tall with generous vertical padding; the band color itself is the section divider — no rules or shadows between sections. Pricing is a two-card comparison (Free vs $8.99/mo) with a Yearly/Monthly pill toggle; FAQ is a plain accordion list with plus icons; footer is black with a huge lowercase "era" wordmark and small link columns.

## Components
- Buttons: small pill shapes with solid fills — light/white "Sign in" pill on dark, black "Transfer" pill inside the app UI, black "New automation" pill. No borders, no shadows, no gradients.
- Chat bubbles: rounded-rectangle pills in white or the section's accent color, floating over/beside the phone mockup; AI replies carry a small black dot avatar.
- Cards: in-app cards and the suggested-action chips use ~8-14px radius, flat accent fills (mint, chartreuse), thin or no borders. Pricing tiers are flat white cards with checkmark feature lists, no elevation.
- Data viz: purple-tinted calendar heatmap grid; bar/area charts using diagonal hatching (black diagonal stripes) instead of solid fills for targets.
- QR codes appear as the primary "CTA" in every feature section instead of a download button.
- FAQ rows: full-width text + right-aligned plus icon, hairline-separated.

## Signature
- Stacked full-bleed pastel bands (sage → olive → lilac → off-white) between a black hero and black footer — the palette shift IS the page rhythm.
- One repeating module: left text + QR code, right iPhone mockup with overflowing chat bubbles.
- Diagonal-hatch chart fills and muted calendar heatmaps give the finance data a print/editorial feel.
- Tiny, restrained type everywhere except the oversized lowercase "era" footer wordmark.

## Do / Don't
**Do**
- Alternate full-width muted pastel section backgrounds (sage, olive-khaki, lilac) with near-black bookends; keep saturation low and slightly warm.
- Keep every CTA a small solid pill — black on light bands, white on dark — with no border or shadow.
- Show the product via phone mockups with chat bubbles breaking the frame edge; let one accent color per section echo inside the mockup UI.
- Use diagonal hatching for chart targets/projections and desaturated purples/greens for data fills.
- Left-align headings and keep body copy short (2-3 lines) at a small size.

**Don't**
- Don't add gradients, glows, glass blur, or drop shadows — every surface here is flat.
- Don't use a bright saturated brand blue/green; nothing on the page exceeds muted pastel intensity.
- Don't center hero copy or oversize the body text; scale drama is reserved for the footer wordmark only.
- Don't separate sections with borders, waves, or cards — the background color change alone does the work.
- Don't mix typefaces; a single neo-grotesque sans handles display, body, nav, and the wordmark.
