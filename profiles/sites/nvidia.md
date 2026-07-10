---
name: nvidia
kind: site
style: DT
category: semiconductors-ai-computing
website: null
pages: [homepage, industry-landing, solutions-landing, product-landing]
palette:
  canvas: "#ffffff"
  ink: "#000000"
  primary: "#76b900"
  accents: ["#5a8d00", "#f7f7f7", "#cccccc", "#0046a4", "#1a1a1a"]
typography:
  display: "NVIDIA-EMEA (proprietary; Inter 400/700 is the closest open substitute, Arial official fallback) · bold 700 · zero tracking"
  body: "NVIDIA-EMEA, regular 400, falls back Arial → Helvetica"
radius: "small 2-6px (2px on buttons, cards, inputs, chips; 0px on nav, hero, footer chapters)"
---
## Overview
A monochrome engineering aesthetic where black hero/footer "chapters" bookend white body content, and a single hyper-saturated green (#76b900) does every job an accent can do: CTAs, active tabs, focus rings, and tiny decorative squares. Geometry stays rigidly angular at 2px radius everywhere, with hairline gray borders instead of shadows. The result reads like technical documentation with strong art direction — dense, gridded, and disciplined.

## Layout
Three-tier chrome: a 32px black utility bar, a 64px black primary nav (wordmark left, centered links, search + login + green CTA right), then a light-gray breadcrumb or sub-nav strip on interior pages. Heroes are full-bleed dark 16:9 imagery with copy pinned to the left third, a 48px/700 headline, and one green button. Body sections stack at a strict 64px vertical rhythm on white, punctuated by black CTA strips, and every page closes with a 6-column black footer. Content caps at ~1280px; card grids run 4-up → 3 → 2 → 1 with 24px gutters. Whitespace comes from the dark/light section alternation, not from oversized padding.

## Components
Primary button: solid #76b900 fill, black text, 700 weight, 44px tall, 2px radius; pressed state darkens to #5a8d00. Secondary: transparent with a green border on light, white-bordered on dark; tertiary is a green "Learn More →" text link. Cards (product, feature, resource) are flat white rectangles with a 1px #cccccc border, 24-32px padding, no shadow, often tagged with a 12px solid-green corner square; resource cards carry uppercase gray badge labels ("WHITE PAPER"). Tabs invert to black-fill/white-text when active. Inputs are 44px, hairline-bordered, 2px radius; focus is signaled solely by a 2px green border. The only shadow anywhere is a faint 5px ambient under sticky nav.

## Signature
- One accent color total: NVIDIA green owns every CTA, active state, and ornament; inline prose links are the lone blue (#0046a4)
- 12px green corner squares anchored to card corners — the system's identity mark
- 2px radius on literally every interactive element; nothing pill-shaped, nothing soft
- Black hero + black footer framing white, hairline-ruled body grids

## Do / Don't
**Do**
- Alternate black chapter blocks and white body sections in a predictable page rhythm
- Keep green scarce — one solid-green CTA per fold, demote others to green-outline buttons
- Build hierarchy purely from size and 400/700 weight contrast; body text stays black/near-black
- Tag reusable cards with a small green corner square
- Separate everything with 1px #cccccc hairlines instead of elevation

**Don't**
- Don't add drop shadows to cards or content — flat hairline borders only
- Don't swap in other greens (#3f8500, #bff230) for the CTA color; #76b900 is exact
- Don't round anything past 2px except avatar/icon circles
- Don't use the link blue on buttons or chrome; it exists only inside body prose
- Don't center hero copy — text hugs the left third while imagery fills the right
