---
name: fonts-ninja
kind: site
style: BT
category: design-tools
website: https://fonts.ninja/
pages: [home, catalog, about, product-tool, dark-mode]
palette:
  canvas: "#F4F3F0"
  ink: "#131313"
  primary: "#131313"
  accents: ["#92E3B8", "#FF4B21", "#E85C5C", "#5CA8E8", "#EDE59A"]
typography:
  display: "Aeonik-like geometric grotesque · very heavy (Black) · tight, near-negative tracking"
  body: "Same geometric grotesque · medium/semibold · normal tracking"
radius: "mixed — pill nav buttons, small 2-6px on cards and secondary buttons"
---
## Overview
Monochrome big-type utility site where typography is both the interface and the content. Enormous near-black headlines on warm off-white (inverted to near-black in dark mode) do all the expressive work; color appears only as tiny playful punctuation — a mint word set in a contrasting display face, multicolor cursor/file-icon stickers scattered over hero letters. The catalog itself is a dense grid of white specimen cards, each one a mini type poster.

## Layout
Slim single-row nav: small logo left, plain text links center-right, pill "Sign in" (outline) and "Sign up" (solid black) at far right. Hero is a left-aligned 3-4 line headline filling most of the viewport width, sometimes with inline icons embedded mid-sentence and a decorated word swapped into an alternate typeface. Below, a strict 3-column card grid with tight equal gutters runs uninterrupted for the full page. Marketing pages (tool) alternate left/right: bold paragraph blocks beside large overlapping product screenshots rotated/stacked with drop shadows. Footer is minimal: hairline rule, small text links, address, social icons — no heavy footer band.

## Components
- Buttons: two families — pill outline (Sign in) and pill solid black (Sign up) in nav; small-radius solid black rectangles with white label for section CTAs ("Download our browser extension"); one outlined rounded-rectangle CTA ("Download for free!") in ink on canvas.
- Cards: white (dark gray #1C1C1C in dark mode) specimen cards, thin light border, small radius, no shadow; interior split by hairline rules into specimen area / foundry meta / style-count + price rows in tiny text.
- Floating tooltip chips (extension UI shown in screenshots): white rounded rectangles with strong black borders and hard shadows, sticker-like.
- Inputs barely present; search is an icon-only affordance in nav.

## Signature
- Headline words interrupted by inline pictograms and one word restyled in a wildcard display face + mint color ("Discover AWESOME typefaces").
- Cursor-and-file-icon "stickers" in red/blue/yellow/peach with black outlines pinned onto giant hero letters.
- Catalog cards where every card uses a different typeface at poster scale — the grid itself is the visual identity.
- Perfect light/dark inversion: same layout, canvas and ink simply swap; cards go from white-on-light to dark-gray-on-black.

## Do / Don't
Do:
- Let the headline occupy 50-70% of viewport height, set black at heavy weight with tight leading and tracking.
- Keep the base palette strictly ink-on-off-white; inject color only through small icon stickers or a single accented word.
- Use hairline rules and tiny 11-12px meta text inside cards to separate specimen from metadata.
- Show product UI as overlapping, slightly offset screenshot cards with bordered tooltip chips on top.
- Mirror the whole system for dark mode by swapping canvas/ink, keeping mint accent identical.

Don't:
- Add gradients, background photography, or colored section bands — every section sits on the same flat canvas.
- Use box shadows on catalog cards; only the sticker/tooltip elements get hard shadows and thick outlines.
- Introduce a second brand color for CTAs — all primary buttons are plain black (or white on dark).
- Center the hero; headlines are left-aligned and ragged-right.
- Round cards heavily or make buttons anything between small-radius and pill — the system uses only those two ends.
