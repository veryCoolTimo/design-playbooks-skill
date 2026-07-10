---
name: tana
kind: site
style: ML
category: productivity-saas
website: https://tana.inc/
pages: [home, features, use-case-individuals, use-case-teams, pricing]
palette:
  canvas: "#F5F5F7"
  ink: "#0B0C11"
  primary: "#96409B"
  accents: ["#D9F09E", "#FDBC3A", "#5693FE", "#131419"]
typography:
  display: "neutral grotesque (Inter/Helvetica Now feel) · medium-to-semibold · tight, near-default tracking"
  body: "same grotesque family, regular weight, quiet gray-black"
radius: "small 2-6px on buttons; small-to-medium 6-12px on cards and screenshot frames"
---
## Overview
A restrained, near-monochrome light system (#F5F5F7 canvas, #0B0C11 ink) that swaps in one saturated accent per page: purple for features/pricing, lime green for home, amber for the individuals page, blue for teams. Use-case pages invert to a dark #131419 canvas while keeping the same typographic scale. Product screenshots inside colorful frames or on abstract gradient art carry most of the visual energy; the chrome around them stays flat and quiet.

## Layout
Slim single-row top nav: small logo left, plain text links with chevrons center, "Log in" ghost button and one filled "Start Free Trial" CTA right (CTA color changes per page theme). Heroes are left-aligned or centered short headlines with a one-color accent phrase ("The glue that binds everything together.", "your life.") over 2-3 lines, small supporting paragraph, single CTA. Section rhythm alternates: heading + short paragraph, then a large full-width product screenshot in a colored frame, then a 2-3-column row of gray quote cards with tiny avatars. Home uses full-bleed lime band sections as CTA breaks. Generous vertical whitespace between sections; four-column link footer on the page canvas with icon-prefixed links.

## Components
Buttons: compact, small-radius (~4-6px) rectangles; filled purple (#96409B) plan CTAs on pricing, filled near-black (#0B0C11) with white text on home, per-theme fills (amber #FDBC3A, blue #5693FE, pale pink) in the nav. No visible shadows or gradients on buttons. Cards: flat light-gray (#ECECEE-ish) testimonial blocks and white pricing panels with hairline or no border, no drop shadow; the highlighted plan gets a lavender tint strip ("2000 AI credits included") under the CTA and a lavender "Most powerful" pill badge. Feature tags render as tiny bordered chips (Tasks, Projects, OKRs). FAQ is a plain divider-line accordion with chevron carets. A Monthly/Yearly pill toggle in purple appears on pricing.

## Signature
- One accent color per page over an otherwise gray/black system — purple, lime, amber, blue — all anchored by the same #F5F5F7 / #0B0C11 pair.
- Product screenshots framed in thick saturated color blocks (purple, pink, blue) or set on painterly gradient/marbled art.
- Flat, shadowless surfaces: quotes, pricing cards, and CTAs rely on tone contrast and whitespace instead of elevation.
- Headline accent phrases colored mid-sentence ("# Supertags. The glue that...") with a leading hash glyph nodding to the product's tags.

## Do / Don't
Do:
- Keep the canvas at #F5F5F7 and body ink near-black; let a single accent color own each page.
- Frame app screenshots in bold solid-color borders or place them over abstract gradient imagery.
- Use small-radius, compact buttons with flat fills — purple for conversion pages, black on light marketing pages.
- Set testimonials as flat gray cards in 2-3 column rows with small avatar + name + role.
- Mirror the light system on dark pages by flipping to #131419 and switching the accent (amber, blue).

Don't:
- Add drop shadows, glassmorphism, or gradient buttons — every surface here is flat.
- Use pill-shaped or large-radius (16px+) buttons; corners stay tight.
- Mix multiple accent colors within one page's UI chrome; the multi-color story lives across pages, not within them.
- Introduce decorative serif or display faces — everything runs on one grotesque at varying weights.
- Crowd sections; each heading + screenshot pair gets a full screen's worth of breathing room.
