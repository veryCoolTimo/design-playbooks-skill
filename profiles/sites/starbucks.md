---
name: starbucks
kind: site
style: ML
category: food-beverage
website: null
pages: [home, rewards, gift-cards, product-detail, product-nutrition]
palette:
  canvas: "#f2f0eb"
  ink: "rgba(0,0,0,0.87)"
  primary: "#00754A"
  accents: ["#006241", "#1E3932", "#cba258", "#edebe9", "#d4e9e2"]
typography:
  display: "SoDoSans (proprietary; sub Inter/Manrope) · regular-to-semibold, hierarchy via weight not size · tight -0.16px"
  body: "SoDoSans / Helvetica Neue fallback, -0.01em tracking"
radius: "pill (50px) buttons; medium 12px cards"
---
## Overview
A warm cafe-retail system: cream and ceramic off-white canvases instead of stark white, with four calibrated greens each assigned a fixed job (deep green for headings, brighter green for CTAs, near-black green for bands and footer, mid green for decoration). One proprietary sans carries the whole voice at tight negative tracking; a serif appears only on Rewards headlines and a script only on Careers. Depth is whisper-quiet — stacked low-alpha shadows, no gradients anywhere.

## Layout
Fixed top nav that grows in height across breakpoints (64 to 99px) with a triple-layer soft shadow; logo left, a few inline links, outlined Sign-in plus black-filled Join pill on the right. Pages alternate solid color blocks: cream hero, white content, dark-green (#1E3932) feature band with white text, cream utility, dark-green footer. Heroes split asymmetrically 40% photo / 60% text, stacking on mobile. Spacing runs a rem scale anchored at 16px, with generous 40-64px section padding — whitespace separates sections, never divider lines. Gift-card grids reflow 5-up down to 1-up.

## Components
Buttons are always 50px full pills at roughly 7px 16px padding, in filled green (#00754A), outlined green, black filled, or white-on-dark-green variants; every one presses with scale(0.95) over 0.2s. A signature 56px circular floating "order" button sits fixed bottom-right with a two-layer shadow. Cards are white, 12px radius, dual whisper shadows (0.14/0.24 alpha). Inputs use floating labels with springy cubic-bezier animation, pale-mint valid tint and faint red invalid tint; PDP selects are 4px-radius outlined rectangles whose border turns green on focus. A gold-outlined pill marks Rewards-redeemable items.

## Signature
- Warm cream canvas (#f2f0eb / #edebe9) standing in for cafe materials — never pure white pages
- Four-green role system plus gold that appears only around Rewards status, nowhere else
- Universal 50px pill buttons with scale(0.95) press, and the floating circular green order button
- Espresso-dark green band rhythm bookending bright cream/white body sections

## Do / Don't
Do:
- Keep the page canvas warm cream and let cards be the only pure white
- Map each green to its role: #006241 headings, #00754A CTA fills, #1E3932 bands/footer
- Pill every button (50px) and give it the scale(0.95) active press
- Layer 2-3 faint shadows for lift instead of one heavy one
- Hold tracking tight (-0.01em body, -0.16px display) on the sans

Don't:
- Don't flatten the palette to a single green or use gold as a generic accent
- Don't introduce gradients — the system is strictly solid color blocks
- Don't set body text in pure black; use rgba(0,0,0,0.87)
- Don't separate h1 from h2 by size — they share 24px; weight and color do the work
- Don't let the Rewards serif or Careers script leak into the main shopping flow
