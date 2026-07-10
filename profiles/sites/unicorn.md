---
name: unicorn
kind: site
style: DN
category: design-utility-saas
website: https://www.unicorn.studio/
pages: [home, resources-docs]
palette:
  canvas: "#0a0a0c"
  ink: "#b9b9c3"
  primary: "#a78bfa"
  accents: ["#e879f9", "#f59e0b", "#5b6cff", "#e5e5ea"]
typography:
  display: "neo-grotesque sans (Inter/Suisse-like) · medium weight · near-normal tracking, with an italic chrome serif flourish for accent words"
  body: "same neo-grotesque sans, regular"
radius: "buttons small 4-6px; cards near-none (hairline-divided grid); docs callout small 6-8px"
---
## Overview
Near-black canvas where the WebGL demos themselves supply all the color: a hero framed by a glowing dot-matrix border shifting from orange to magenta to purple, surrounded by restrained gray typography. UI chrome is deliberately quiet — hairline borders, muted grays, one soft-lavender CTA — so the neon effect imagery reads as the product. An italic metallic serif ("Magic", "Make it pop") punctuates the otherwise plain grotesque type.

## Layout
Slim top nav: wordmark left, two text links plus a small filled Sign up pill right. Hero is a full-width bordered "screen" containing the animated effect, with centered title, one-line subhead, and a single CTA inside it. Below: a centered app screenshot, then a strict 2-column feature grid divided by 1px hairlines (no gaps, no card shadows), collapsing to a 4-up icon row for smaller features. Testimonials in a 3-column hairline grid, then a 3-up showcase gallery of customer sites, then a minimal centered footer CTA over a light-burst image. Docs page uses classic 3-pane docs layout: left sidebar nav, wide article column, right table of contents, dark search input in the header.

## Components
- Buttons: small-radius (4-6px) rectangles; primary is soft lavender (#a78bfa) fill with near-black text; secondary is dark gray fill with white text. No gradients or glows on buttons themselves.
- Cards/sections: no discrete cards — cells in a hairline-bordered (#222-ish, 1px) grid on the same black canvas; each cell holds centered heading, muted one-line caption, and a large effect image.
- Docs callout: dark navy-tinted panel with a thin blue border, small radius, bold white text and a circular blue icon.
- Inputs: docs search is a dark charcoal rounded rectangle with magnifying-glass icon and gray placeholder.
- Links: light purple (#8b7cf6-family) text, as in "Learn more" and docs "Next:" links.

## Signature
- Glowing dot-matrix/LED hero frame cycling orange → magenta → purple around a black stage.
- Product effects (chrome text, halftone shapes, neon shaders) carry all the color; the UI itself is grayscale plus one lavender.
- Hairline-divided bento grid with centered titles and muted captions — no card backgrounds, no shadows.
- Plain grotesque headings interrupted by italic liquid-chrome serif words for emphasis.

## Do / Don't
Do:
- Keep the canvas a flat near-black (#0a0a0c) and let embedded imagery/demos provide saturation.
- Use 1px hairline borders to structure feature grids instead of card fills or shadows.
- Reserve the lavender fill for the single primary CTA; secondary actions get dark gray fills.
- Set headings in a clean grotesque at modest sizes; center-align section titles and captions.
- Use an italic metallic serif sparingly — one accent word or a short standalone graphic phrase.

Don't:
- Add colored backgrounds, gradients, or glassmorphism to cards — cells sit directly on the black canvas.
- Use neon color on text or buttons; neon lives only in the effect artwork and hero frame.
- Round corners past ~8px or use pill buttons; radii stay small and boxy.
- Set body copy in pure white — it's a muted gray around #b9b9c3 with generous line height.
- Crowd sections — each grid cell holds only a heading, one caption line, and one visual.
