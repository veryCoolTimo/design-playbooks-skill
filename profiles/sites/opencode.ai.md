---
name: opencode.ai
kind: site
style: DT
category: developer-tools
website: null
pages: [home, product (zen), enterprise]
palette:
  canvas: "#fdfcfc"
  ink: "#201d1d"
  primary: "#201d1d"
  accents: ["#007aff", "#30d158", "#ff9f0a", "#ff3b30"]
typography:
  display: "Berkeley Mono · bold (700) at only 38px · zero tracking"
  body: "Berkeley Mono (fallbacks: IBM Plex Mono, JetBrains Mono) · 16px/1.5"
radius: "small 2-6px (4px on all interactive elements); containers are 0px sharp"
---
## Overview
A manpage turned into a marketing site: one monospaced font (Berkeley Mono) covers every text role from the 38px hero down to footer legal copy, with no sans-serif, italic, or display face anywhere. Warm cream canvas, near-black ink, hairline dividers, and ASCII brackets standing in for icons. The lone visual set piece is a full-bleed near-black mockup of the product's own terminal UI, complete with a block-pixel ASCII wordmark.

## Layout
Slim ~56px nav on the cream canvas: pixel-ASCII wordmark left, text links center-right, one dark Download CTA far right (collapses to hamburger at 768px, CTA stays). Content lives in a ~960px single column; the enterprise page adds a text/form two-column split. Sections stack at a strict 96px rhythm separated only by 1px translucent hairlines — no bands, no alternating backgrounds. Text sits flush left with almost no internal indentation, so pages read like printed code listings.

## Components
Buttons: near-black fill (#201d1d) with cream label, ~36px tall, 4px radius; pressed state deepens to #0f0000; secondary is a cream, hairline-bordered twin. Tabs (curl/npm/brew install strip) are transparent with a bottom underline for the active state. Inputs: #f8f7f7 fill, 1px hairline border, 4px radius; focus flips to cream with an ink border — no glow or halo. Cards barely exist: feature rows are plain text lines prefixed with `[+]`/`[-]` markers, FAQ rows toggle with `+`/`−` characters, and the install snippet is a #f1eeee monospace pill. Zero drop shadows anywhere; the only "elevated" surface is the dark hero mockup.

## Signature
- Every glyph on the page is Berkeley Mono — the single-font commitment IS the brand
- Wordmark rendered as block-pixel ASCII art, in the nav and inside the hero terminal mockup
- ASCII bracket markers (`[+]`, `[-]`, `[x]`) replace all icons and bullets
- One near-black full-bleed TUI mockup per page; everything else is flat cream with hairlines
- Sparse-line "Fig N." ASCII-style stat charts instead of logos or screenshots

## Do / Don't
**Do:**
- Set all text — headings, buttons, footer — in one monospaced face at weights 400/500/700
- Keep #fdfcfc as the sole page background and separate sections with 1px hairlines at ~96px spacing
- Use bracketed ASCII characters as list markers, toggles, and status glyphs
- Limit the dark #201d1d surface to a single hero terminal mockup per page
- Give interactive elements a uniform 4px radius while containers stay square

**Don't:**
- Don't add a sans-serif, serif, or italic anywhere — the system tolerates exactly one font
- Don't use shadows, gradients, or photography; depth comes only from the one dark surface
- Don't color CTAs with the blue/green/orange semantic ramp — those hues live inside the product TUI, not the marketing chrome
- Don't swap ASCII markers for SVG icons or the pixel wordmark for a vector logo
- Don't inflate padding: list rows run 8px vertical, FAQ rows 12px, buttons 4px/20px
