---
name: imgs-so
kind: site
style: ML
category: photo-community
website: https://imgs.so/
pages: [home]
palette:
  canvas: "#ffffff"
  ink: "#1a1a1a"
  primary: "#ffffff"
  accents: ["#9b9b9b", "#e5e5e5"]
typography:
  display: "serif italic paired with neutral grotesque · regular weight · normal tracking"
  body: "neutral grotesque (Helvetica/Inter-like), very small sizes"
radius: "none on images/cards; pill on the single button"
---
## Overview
An almost invisible interface: pure white canvas, tiny near-black text, and one small outlined pill button. All color and visual weight comes from the photographs themselves; the chrome is deliberately mute so the community's images are the entire design. The hero is a two-line editorial statement ("Show & tell / for photographers") rather than a marketing block.

## Layout
Ultra-minimal nav: a tiny underlined "Index" wordmark top-left, plain "Sign in" text link top-right, no menu, separated by a hairline rule. Hero is left-aligned, small: an italic-serif line stacked over a sans line, a short gray paragraph (~3 lines), then a single pill CTA. Below, the page is one continuous masonry-style photo grid, roughly 4 columns, with images of varied aspect ratios staggered vertically. Column gutters are wide and vertical whitespace between rows is generous; no section breaks, headings, or footer visible — the feed IS the page.

## Components
- Button: one "Request an invite" pill — white fill, 1px light-gray border, dark text with a small envelope glyph, very compact height. No shadow, no color fill.
- Cards: none in the boxed sense. Each photo is a bare, square-cornered image with a caption block below: title in small dark text, then username · date in smaller light-gray text. No borders, shadows, hover chrome, or like/comment icons visible.
- Inputs: none on this page.
- Links: plain text; the wordmark is underlined, "Sign in" is not.

## Signature
- Square-cornered photographs on pure white doing all the visual work; UI reduced to hairlines and micro-type.
- Italic serif + sans pairing in the hero headline ("Show & tell" / "for photographers").
- Caption pattern under every image: title, then "username · date" in ~10px gray.
- A single tiny outlined pill CTA — no filled, colored buttons anywhere.

## Do / Don't
Do:
- Keep the canvas pure white and let photographs supply 100% of the color.
- Set headings small and left-aligned; mix an italic serif line with a plain sans line for the hero.
- Use hairline rules and 1px light-gray borders as the only structural chrome.
- Caption images with a two-tier hierarchy: dark title, lighter "author · date" metadata.
- Stagger image heights in a wide-guttered masonry grid with lots of vertical air.

Don't:
- Don't add filled or colored buttons, brand tints, or gradients — the sole CTA is a white outlined pill.
- Don't round or shadow images/cards; corners stay square and flat.
- Don't add engagement chrome (likes, counts, avatars, hover overlays) to the grid.
- Don't enlarge type for drama; the whole system runs on small text sizes, including the hero.
- Don't break the feed with banners, section headers, or a heavy footer.
