---
name: bmw
kind: site
style: ML
category: automotive
website: null
pages: [home, model-detail, configurator, dealer-inventory]
palette:
  canvas: "#ffffff"
  ink: "#262626"
  primary: "#1c69d4"
  accents: ["#1a2129", "#f7f7f7", "#fafafa", "#0653b6", "#0066b1", "#e22718"]
typography:
  display: "BMW Type Next Latin (sub: Inter) · heavy 700 · zero tracking"
  body: "BMW Type Next Latin Light 300 (sub: Inter Light)"
radius: "none (0px buttons, cards, inputs; circles only for icon buttons)"
---
## Overview
A restrained corporate-automotive system: white pages punctuated by a single dark-navy (#1a2129) hero band per page, with BMW blue (#1c69d4) as the lone action color. Everything is rectangular — zero radius on buttons, cards, inputs — and no element ever casts a shadow; depth is carried by photography and light/dark band contrast. The one licensed typeface does all the work through a stark 700-vs-300 weight split.

## Layout
White sticky top nav (64px) with the roundel left, 14px/400 menu center, utility icons right. One full-bleed hero band per page — dark navy or light with edge-to-edge vehicle photography at cinematic ratios. Body sections rotate light/dark surfaces at a fixed 80px vertical rhythm inside a ~1440px 12-column container. Model cards run 4-up or 5-up grids (2-up tablet, 1-up mobile); dealer/configurator pages reuse the same tokens at higher density. Footer sits on soft grey #f7f7f7 with a 4-column link list.

## Components
- Primary button: solid #1c69d4 fill, white 14px/700 label with 0.5px tracking, 48px tall, 0px corners; pressed state darkens to #0653b6, disabled goes #d6d6d6.
- Secondary button: white fill with 1px #cccccc outline, same rectangular geometry; on dark heroes it becomes transparent with a white outline.
- Inline CTA: uppercase 13px/700 "LEARN MORE ›" link at 1.5px tracking.
- Model card: borderless white plate, photo on a #fafafa block, 18px/700 title, 14px Light tagline, uppercase link — no shadow.
- Inputs: 48px tall, 1px #e6e6e6 hairline, 0px radius; focus thickens the border to ink.
- Filter chips are rectangular too — active state inverts to ink fill with white text. Configurator tiles select via a 2px blue border.

## Signature
- Every interactive surface is a sharp rectangle — 0px radius is the brand's "engineered" dialect.
- One blue (#1c69d4) does all CTA work; the M tricolor stripe (blue-blue-red, 4px) appears only as an M-badge divider, never as a fill.
- 700-weight headlines against 300-weight Light body, never weight 500, never negative tracking.
- Shadowless depth: contrast comes from alternating white canvas and navy #1a2129 bands plus full-silhouette vehicle renders.

## Do / Don't
Do:
- Keep pages on pure white and spend #1a2129 only on hero and pre-footer CTA bands, alternating light/dark down the page.
- Fill primary CTAs with #1c69d4, white 700-weight label, square corners, 48px height.
- Pair 700-weight display with 300-weight Light body; let 400 appear only in captions and nav links.
- Set inline links as uppercase tracked "LEARN MORE ›" text buttons.
- Hold every major band to 80px vertical padding and 24px card padding.

Don't:
- Don't round buttons or cards — pill and soft-corner shapes break the dialect.
- Don't introduce a second action color or use the tricolor stripe as a button fill.
- Don't add drop shadows or card borders; photo plates rely on the #fafafa background alone.
- Don't tighten letter-spacing on headlines or bold the body copy.
- Don't stack two same-tone bands back to back — surface mode must flip between sections.
