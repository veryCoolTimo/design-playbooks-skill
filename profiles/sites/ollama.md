---
name: ollama
kind: site
style: ML
category: ai-developer-tools
website: null
pages: [home, pricing]
palette:
  canvas: "#ffffff"
  ink: "#000000"
  primary: "#000000"
  accents: ["#fafafa", "#737373", "#e5e5e5", "#171717"]
typography:
  display: "SF Pro Rounded (fallback Nunito/system-ui) · medium 500-600 · no tracking"
  body: "ui-sans-serif / system-ui"
radius: "pill for all interactive elements; medium 12px for cards"
---
## Overview
A README rendered as a website: pure white sheet, black text, gray prose, and exactly one illustration (a hand-drawn llama). The hero is a centered 36px rounded-sans headline over a curl install command in a gray pill — the install snippet, not a banner, is the star. No gradients, no shadows, no photography, no second brand color anywhere.

## Layout
Single narrow reading column (~720px) with 88px of plain white air between sections — whitespace does all the separating; there are no colored bands or divider graphics. 56px flat nav: llama logo, three text links, a centered gray search pill, then "Sign in" plus a black pill CTA. Pricing widens to a ~960px 3-up card grid; one section splits 50/50 text/terminal-mockup. FAQ is a plain stack of hairline-divided rows, always expanded.

## Components
Buttons are 36px-tall black pills (white text, 14px/500 label); pressed state darkens only to #090909; secondary is a white pill with a 1px #d4d4d4 border. Inputs and the search field are pills too — soft #fafafa fill or 1px hairline, browser-default blue focus ring. Cards (pricing, terminal mockup) are the sole 12px-radius shapes, defined by a 1px #e5e5e5 border, never a shadow. The terminal card carries macOS traffic-light dots (#ff5f56/#ffbd2e/#27c93f) as the palette's only chromatic notes. The top-tier pricing card inverts to #171717 with a white pill CTA — the single emphasis device on the page.

## Signature
- Inline `curl ... | sh` install command in a full-round gray pill directly under the hero headline
- Strict two-shape vocabulary: 9999px pills for anything clickable, 12px hairline-bordered rectangles for cards
- One dark inverted surface (#171717) per page as the only "look here" cue; everything else flat white
- Hand-drawn llama mascot as the entire illustration budget, reused at logo, hero, and card-eyebrow sizes

## Do
- Keep every CTA a black pill; scarcity is the emphasis system — roughly one black pill per viewport fold
- Separate sections with ~88px of bare whitespace instead of bands, rules, or background shifts
- Render CLI examples as first-class UI: code-font pill snippets and a bordered terminal card with traffic lights
- Use a rounded-terminal face (SF Pro Rounded or Nunito) only for headings 24px and up; drop to plain system sans below that
- Invert to the dark #171717 surface at most once per page

## Don't
- Don't add a hue: no blue links, no green success buttons, no tinted sections — black/white/gray only (focus ring excepted)
- Don't use drop shadows or gradients anywhere; depth comes from 1px #e5e5e5 borders or the dark inversion, nothing else
- Don't mix radii: no 8px buttons, no fully-round cards
- Don't collapse FAQs into accordions or box answers in cards — questions and gray body prose stay open on the bare canvas
- Don't add illustrations or stock imagery beyond the llama and a stroke-only lock icon
