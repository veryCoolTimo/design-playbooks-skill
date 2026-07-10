---
name: x.ai
kind: site
style: DT
category: ai-research
website: https://x.ai
pages: [home, product-features, announcements, pricing, auth]
palette:
  canvas: "#0a0a0a"
  ink: "#ffffff"
  primary: "#ffffff"
  accents: ["#ff7a17", "#7c3aed", "#c4b5fd", "#a0c3ec"]
typography:
  display: "Universal Sans (proprietary; Inter is the nearest substitute) · regular 400 only, never bold · heavy negative tracking (-2.4px at 96px)"
  body: "Universal Sans / Inter, with Geist Mono for uppercase eyebrows and labels"
radius: "pill (9999px) for all buttons; small 8px for cards and inputs"
---
## Overview
An austere research-lab surface: one near-black background (#0a0a0a) everywhere, white text, and translucent-white outline pills as the whole interactive vocabulary. Emphasis comes from scale and tight negative letter-spacing, never from weight or color. A muted sunset/dusk accent set (orange, purple, violet, blue) exists in the tokens but stays confined to product illustrations, not chrome. The effect is deliberately unmarketed — announcements, not sales pitches.

## Layout
Sticky top nav on the same black canvas with plain white body-sm links. Hero is a flat dark band with a 96px regular-weight headline; no gradient backdrop, no screenshots, no photography — only sparse SVG illustrations. Sections repeat a fixed rhythm: uppercase Geist Mono eyebrow, then a 48px display headline, separated by 1px hairline dividers (#212327). Content centers around ~1200px with 64px vertical band padding; feature grids run 2-up on desktop, 1-up on mobile.

## Components
- Buttons: pill-shaped always. The dominant style is a transparent pill with a 1px translucent-white border and white 14px label; a white-filled pill with near-black text exists but is reserved for a single sign-up CTA.
- Cards: 8px-radius charcoal rectangles (#191919) with a 1px hairline border, 24px padding, zero shadows — borders do all the elevation work.
- Inputs: slightly lighter dark fill (#1a1c20), hairline border, 8px radius.
- Data/table headers and section labels use uppercase tracked mono type.

## Signature
- White outline pill on near-black — every CTA shares one identical shape.
- Display type at weight 400 only, with aggressive negative tracking; the brand never bolds anything.
- Geist Mono uppercase eyebrows (+1.4px tracking) that read like code comments above each section.
- Shadowless depth: hairline borders are the only elevation cue.

## Do
- Keep #0a0a0a as the sole page surface, edge to edge.
- Set every button as a 9999px pill; use the translucent-white outline variant by default.
- Apply strong negative tracking (~-0.025em) to any large heading, staying at weight 400.
- Pair sentence-case sans headings with UPPERCASE mono labels for eyebrows, counters, and table headers.
- Confine the sunset/dusk accents to illustrations and icons, never to buttons or text.

## Don't
- Don't build a light mode — the system has no light counterpart.
- Don't bold headlines or vary font weight for hierarchy; size and tracking carry it.
- Don't scatter filled CTAs; the white-filled pill is a one-off exception.
- Don't add drop shadows to cards, modals, or toasts.
- Don't swap in a generic sans without re-adding the negative letter-spacing.
