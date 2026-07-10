---
name: kraken
kind: site
style: DT
category: crypto-exchange
website: null
pages: [landing]
palette:
  canvas: "#ffffff"
  ink: "#101114"
  primary: "#7132f5"
  accents: ["#5741d8", "#5b1ecf", "#149e61", "#9497a9", "#dedee5"]
typography:
  display: "Kraken-Brand (IBM Plex Sans fallback) · bold 700 · tight negative tracking (-0.5 to -1px)"
  body: "Kraken-Product (Helvetica Neue fallback)"
radius: "medium 8-14px (buttons 12px standard; badges 6-8px)"
---
## Overview
A light, purple-driven exchange aesthetic: pure white surfaces, near-black ink, and one saturated violet doing all the brand work. Contrast comes from color and bold type rather than shadows or texture. The overall feel is precise and financial — friendly enough for consumers, restrained enough to signal trust.

## Layout
Sections sit on flat white with generous breathing room; depth is nearly absent (shadows at 3-4% black opacity only). Type scale steps cleanly from a 48px hero down through 36/28px section heads to 16px body, all on a tight spacing scale built from small increments (4/8/12/16/24px). Responsive breakpoints run from 375px up to 1536px.

## Components
Buttons come in five flavors, all sharing a 12px radius: solid purple fill with white text (the main CTA), white with a #5741d8 1px outline, a translucent purple wash (16% opacity purple bg with purple text), a shadowed white button, and a faint gray secondary. Badges use tinted backgrounds — green at 16% opacity with dark-green text for success — at 6-8px radius. Dividers are a light #dedee5; borders often use gray at reduced opacity rather than solid strokes.

## Signature
- One purple (#7132f5) carries the whole identity: CTAs, links, and tinted washes derived from it
- Dual proprietary font stack: Kraken-Brand for bold, negatively tracked headings; Kraken-Product for everything else
- Whisper-quiet elevation — shadows barely register (rgba(0,0,0,0.03))
- Consistent 12px button radius across every variant, never pill

## Do
- Fill the main CTA with #7132f5, white label, ~13px 16px padding, 12px radius
- Derive secondary states from the same purple via opacity (16% washes, #5741d8 outlines)
- Track display headings tight: -1px at 48px, -0.5px at 36/28px, weight 700
- Signal success with green-on-green tints (#149e61 at 16% bg, #026b3f text)
- Keep shadows at 3-4% opacity or drop them entirely

## Don't
- Don't round buttons past ~12px — no pill shapes anywhere
- Don't introduce purples outside the #7132f5 / #5741d8 / #5b1ecf scale
- Don't put headings in the body font; the Brand/Product split is strict
- Don't add heavy drop shadows or gradient depth — surfaces stay flat white
- Don't use warm grays; the neutral scale is cool and blue-leaning (#686b82, #9497a9)
