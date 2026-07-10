---
name: shopify-editions-spring-26
kind: site
style: DT
category: ecommerce
website: https://www.shopify.com/editions/spring2026
pages: [landing, feature-showcase]
palette:
  canvas: "#0a0a0a"
  ink: "#d4d4d4"
  primary: "#ffffff"
  accents: ["#c8f04e", "#df5fc8", "#8f7bd8"]
typography:
  display: "Shopify Sans / Inter-like grotesque · light-to-regular weight at very large sizes · slightly tight tracking"
  body: "Same grotesque (Shopify Sans / Inter-like) · regular · normal tracking, muted gray"
radius: "pill on buttons and the floating section-nav chip; small 2-6px on media cards and embedded UI frames"
---
## Overview
A near-black, cinematic long-scroll release showcase. Note: metadata said ML, but the screenshots are unambiguously dark-tech. Vast fields of #0a0a0a canvas carry oversized light-weight grotesque headlines, muted gray body copy, and full-bleed media tiles filled with aurora/starfield motion footage. Color arrives only inside the imagery — acid-lime product renders, magenta/green terminal-style data overlays — never in the chrome itself, which stays strictly black and white.

## Layout
Sticky slim black nav: logo + edition name left, "Editions" dropdown and search center-left, "Shopify.com" link and a white pill CTA right. Page opens on a pure-black loader with a tiny particle cluster before content reveals. Sections alternate: a two-column header row (huge 2-line headline left, ~1/3-width gray description + underlined text link right), then a full-width 16:9 video tile with centered white play pill, then a 3-column card grid of media tiles with underlined titles and gray captions beneath. Hairline rules separate grid rows; some rows are text-only 3-column feature lists with no media. Whitespace is generous and vertical rhythm is long — headings get an entire viewport band. A floating white pill ("Agentic" + hamburger) sits fixed at bottom-center as a section jump menu.

## Components
- Primary CTA: solid white pill, black text, no border or shadow ("Start for free").
- Floating section-nav: white pill with current-section label and hamburger icon, subtle drop shadow, fixed bottom-center.
- Cards: borderless media tiles with small (2-6px) rounding; the image IS the card — no card background, padding, or shadow; caption text sits below on the page canvas.
- Links: white/light-gray text with thin underline, both as card titles and inline demo links; no colored link text.
- Video tiles: dark footage with a centered white circular/pill play button containing a black triangle, sometimes paired with a white label pill.
- Embedded product UI shown as light-mode admin screenshots framed inside the dark tiles, creating strong light-on-dark contrast pops.

## Signature
- Total black canvas where all color is quarantined inside media tiles (acid-lime sneaker, magenta/green mono-spaced data overlays, aurora gradients).
- Massive light-weight grotesque headlines ("Your products optimized for AI") occupying a full viewport band against emptiness.
- Underlined plain-text links as the universal secondary action — no ghost buttons, no arrows, no colored links.
- Persistent bottom-center white pill acting as a chaptered table of contents for the long scroll.

## Do / Don't
Do:
- Keep the page background flat #0a0a0a everywhere; let full-bleed video/imagery supply all color and texture.
- Set headlines huge and light-weight in a neutral grotesque, sentence case, max ~2 lines, left-aligned with a narrow right-column description.
- Use exactly one solid-white pill CTA in the nav; render every other action as an underlined light-gray text link.
- Present features as borderless 3-column media tiles with slight rounding and caption text directly on the canvas.
- Use mono-spaced neon (lime/magenta) type only inside imagery to signal data/API content.

Don't:
- Don't add colored buttons, colored links, or brand-green chrome — the interface layer is strictly black and white.
- Don't put cards in boxes: no visible card backgrounds, borders, or drop shadows around grid items.
- Don't crowd sections; each headline block owns a viewport-scale band of empty black.
- Don't use heavy or condensed display weights — the headline voice is light and airy despite the dark theme.
- Don't introduce light-mode page sections; light UI appears only as framed screenshots inside dark media tiles.
