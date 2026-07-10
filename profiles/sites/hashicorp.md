---
name: hashicorp
kind: site
style: DT
category: devtools-infrastructure
website: null
pages: [home, product, pricing, resources]
palette:
  canvas: "#000000"
  ink: "#ffffff"
  primary: "#ffffff"
  accents: ["#7b42bc", "#ffcf25", "#e62b1e", "#14c6cb", "#1868f2", "#00ca8e", "#f24c53", "#2b89ff"]
typography:
  display: "hashicorpSans (Inter is closest substitute) · 600/700, no extremes · tight negative tracking (-0.6 to -2.5px)"
  body: "hashicorpSans at 500 weight, relaxed 1.50-1.71 line-height"
radius: "small-medium 8px (buttons/inputs), medium 12px (cards), 24px (CTA banners)"
---
## Overview
Pure-black enterprise marketing system where a single typeface at three weights carries the whole hierarchy. The chrome itself is monochrome — white type, white primary CTA, charcoal cards — while a fixed set of per-product colors (Terraform purple, Vault yellow, Consul red, Waypoint cyan, Vagrant blue, Nomad green, Boundary coral) function as identity markers, not decoration. Depth comes from stepping surfaces lighter (black → #15181e → #1f232b), never from shadows.

## Layout
Sticky 64px black nav with logo left, links center, white primary + charcoal secondary button pair right; collapses to hamburger under 768px with the CTA kept visible. Heroes pair display type with isometric 3D product illustrations in the right column. Sections repeat on a 96px vertical rhythm, each opened by a 12px uppercase eyebrow label. Content maxes around 1280px; card grids run 3-up → 2-up → 1-up. The dark ground itself acts as whitespace — bands alternate between canvas and charcoal rather than inserting gaps.

## Components
Buttons: 8px-radius rounded rects, 14px/600 label, 10x18px padding. Primary is solid white with black text; secondary is charcoal #1f232b; product pages get a CTA filled with that product's color (dark text on yellow/cyan). Cards: charcoal #15181e with a 1px translucent gray border (~rgba(178,182,189,0.1)), 12px radius, 24-32px padding; featured pricing tier lifts to #1f232b; product showcase cards swap the whole background to the product color. Inputs: charcoal fill, 8px radius, 1px blue #2b89ff focus outline. Small product-name chips are pill-shaped; CTA banners are big 24px-radius charcoal panels.

## Signature
- Per-product accent colors used as section identity tokens — a scroll-by glance tells you which tool a section covers.
- One family (hashicorpSans) everywhere; hierarchy carried by weight (500/600/700) and a stark line-height split: 1.17-1.21 display vs 1.50-1.71 body.
- Elevation by surface lift on black (three charcoal steps + hairline borders), zero drop shadows.
- Mandatory uppercase eyebrow (12px, 600, +0.6px tracking) above every section headline.

## Do / Don't
Do:
- Keep every page band on either pure black or #15181e charcoal — those two surfaces anchor the system.
- Apply one product color per section, consistently across its pill, CTA, and showcase card.
- Keep CTAs at 8px radius — the squarish shape is part of the engineered, developer-facing tone.
- Contrast tight display leading against loose body leading; that gap is the voice.
- Place dark text (#000000) on yellow and cyan product fills.

Don't:
- Don't render a light-mode version — the marketing brand exists only on black.
- Don't mix two product accents in one viewport; it destroys the "this section = this tool" signal.
- Don't add drop shadows on the dark ground; use surface steps instead.
- Don't use monospace type on marketing surfaces despite the developer audience.
- Don't invent gray text tones beyond #ffffff / #b2b6bd / #656a76.
