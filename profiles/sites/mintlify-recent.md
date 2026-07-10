---
name: mintlify-recent
kind: site
style: ML
category: developer-tools
website: https://www.mintlify.com/
pages: [landing]
palette:
  canvas: "#FFFFFF"
  ink: "#1A1A1A"
  primary: "#141414"
  accents: ["#3DDC6A", "#B8E94C", "#F7F4EE", "#F04E23", "#8FA5F0"]
typography:
  display: "Neo-grotesque (Inter/Söhne family) · normal-to-medium weight at very large sizes · tight letter-spacing"
  body: "Same neo-grotesque (Inter-like) · regular · neutral spacing"
radius: "medium 8-14px (buttons ~8px, cards 12-16px, metric badges ~4px)"
---
## Overview
Warm minimal-light system: pure white canvas, cream (#F7F4EE) card panels, near-black ink, and a single recurring decorative motif — thin mint-to-lime gradient line waves that flow through the hero and feature cards. CTAs are solid black, never green; green is reserved for data highlights and the wave graphic. Occasional saturated brand-color breakouts (orange Anthropic card, periwinkle Coinbase card) punctuate an otherwise restrained page.

## Layout
Fixed white top nav: logo left, centered text links with chevron dropdowns, right-aligned ghost "Sign in" + solid black "Contact sales". Hero is left-aligned text (badge pill, 3-line display heading, one-line subhead, dual CTA row) with a large product screenshot bleeding off the bottom-right edge. Sections sit inside a hairline-bordered content column (thin vertical rules at the edges). Section headers use a two-tone device: first line black, second line gray, with a small green tick mark at the left margin and a black CTA button floated right. Content below is bento grids — a wide 2-up row over a 3-up row over a full-width card — plus an 8-logo customer grid and a horizontal live-metrics strip. Generous whitespace; rhythm is header-then-bento repeated.

## Components
Buttons: solid black fill, white text, ~8px radius, trailing chevron/arrow; secondary is white with 1px gray border (Google sign-up, "Read the story" on colored cards); tiny square icon-buttons for carousel prev/next. Cards: cream #F7F4EE fill with 1px slightly darker border, 12-16px radius, label text bottom-left, illustration/screenshot filling the top; no drop shadows anywhere. Case-study cards use full-bleed brand colors (orange, periwinkle) with white text and a photo half. Badges/metrics: light-mint pill with monospaced green numbers (e.g. "62.9326%", "129,951"). Search input: pill-shaped, light gray fill. Skeleton-style UI mockups (gray bars, avatars) illustrate features instead of real screenshots.

## Signature
- Thin multi-strand gradient line waves (mint → lime → teal) sweeping diagonally across hero and cards — the one decorative flourish on the page.
- Cream #F7F4EE bento cards on pure white, separated by hairline borders instead of shadows.
- Monospaced green numbers in mint pills for live agent metrics.
- Two-tone section headings (black first line, gray second) with a small green tick at the left rule.

## Do / Don't
**Do**
- Keep all primary CTAs solid black with a trailing arrow; use green only for data accents and the wave graphic.
- Use cream (#F7F4EE) card fills with 1px borders and 12-16px radius; rely on hairline rules, not shadows, for structure.
- Set display type large, tight, and left-aligned; split section headings into black + gray lines.
- Render live numbers in monospace inside pale mint pills.
- Allow one saturated brand-color breakout section (case-study cards) against the neutral base.

**Don't**
- Don't use green as a button fill or heavy background block — it appears only as thin gradient strokes and small highlights.
- Don't add drop shadows, glassmorphism, or dark sections; the page stays flat and light throughout.
- Don't center hero copy or CTAs; everything anchors to the left column edge.
- Don't mix typefaces — one grotesque family carries display, body, and nav; only metrics switch to mono.
- Don't crowd sections; each bento group gets a full-width header band and generous vertical padding.
