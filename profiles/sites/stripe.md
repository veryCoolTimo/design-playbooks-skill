---
name: stripe
kind: site
style: GR
category: fintech-infrastructure
website: null
pages: [home, product, pricing, signup]
palette:
  canvas: "#ffffff"
  ink: "#0d253d"
  primary: "#533afd"
  accents: ["#1c1e54", "#ea2261", "#f96bee", "#f5e9d4", "#f6f9fc"]
typography:
  display: "Sohne (sub Inter/SF Pro Display) · thin 300 · tight negative tracking (-1.4px at 56px)"
  body: "Sohne 300 (sub Inter), ss01 globally, tnum on numerics"
radius: "buttons pill 9999px; cards medium-large 12px; inputs small 6px"
---
## Overview
A light, atmospheric fintech language: white canvas, deep-navy text (never black), and one electric-indigo pill CTA per section. The top third of every marketing page carries a blurred multi-hue gradient mesh (cream, orange, lavender, indigo, ruby) that doubles as the brand's depth system. Below it, the page settles into white and cool off-white bands, punctuated by composited dark-navy product-UI mockups. Type is thin (300) with aggressively negative tracking on headlines — editorial density over boldness.

## Layout
Nav floats over the gradient hero: wordmark left, links center, sign-in plus one filled indigo pill right. Content centers at ~1200px while the mesh runs edge-to-edge. Sections alternate white / #f6f9fc / occasional warm cream bands, with roomy 64–96px gaps that tighten to ~32px on pricing and dashboard views. Pricing steps 4-up to 2-up to 1-up at 1024/768; feature sections pair copy with a static multi-panel product mockup (IDE + table + chart).

## Components
Buttons: pill-shaped, compact 8px 16px padding, weight-400 label; primary is #533afd fill with white text, pressing darkens to #2e2b8c; secondary is white with indigo text/border; dark surfaces use a #1c1e54 fill. Cards: white, 12px radius, 32px padding, 1px #e3e8ee hairline, faint blue-tinted shadow (rgba(0,55,112,.08)); the featured pricing tier inverts to deep navy #1c1e54. Inputs: 6px radius, 8px 12px padding, cool #a8c3de hairline that turns indigo on focus. Small tags are pale-indigo (#b9b9f9) pills with tiny all-caps labels.

## Signature
- Gradient-mesh hero band (organic SVG blobs, not flat CSS gradients) on every marketing page — it IS the depth system.
- Weight-300 display type with negative letter-spacing (-1.4px at hero size) plus ss01 stylistic set applied site-wide.
- Tabular figures (tnum) on every money/numeric cell — a quiet financial tell.
- Deep-navy composited dashboard/IDE mockups floating over the white canvas as the main product argument.

## Do / Don't
**Do**
- Put the gradient mesh behind every marketing hero; a bare-canvas hero reads off-brand.
- Limit indigo #533afd to one filled pill per section plus inline links.
- Keep headlines at weight 300 with proportional negative tracking (-1.4px at 56px down to -0.2px at 20px).
- Set tnum on any number that represents money or counts; enable ss01 on the body element.
- Pair each feature claim with a rendered product-UI mockup in a 12px-radius, softly shadowed frame.

**Don't**
- Don't thicken display type to 400+ — the thin editorial feel is the identity.
- Don't invent accents beyond the mesh stops (cream/orange/lavender/indigo/ruby/magenta); ruby and magenta never become buttons.
- Don't set body copy in indigo — it is strictly a CTA/link color.
- Don't swap button pills for rounded rectangles or pad them tighter than 8px 16px.
- Don't render pure-black text; ink is always deep navy #0d253d.
