---
name: playstation
kind: site
style: DT
category: gaming
website: null
pages: [home, product-listing, game-detail, support]
palette:
  canvas: "#000000"
  ink: "#ffffff"
  primary: "#0070d1"
  accents: ["#d53b00", "#ffce21", "#f5f7fa", "#53b1ff"]
typography:
  display: "PlayStation SST (sub: Roboto Light/Inter) · light 300 · near-neutral, -0.1 to +0.1px"
  body: "PlayStation SST (sub: Inter) · 18px/1.5 regular"
radius: "pill buttons (9999px); small 4px inputs; medium 8px cards"
---
## Overview
A chaptered marketing surface where full-bleed bands in pure black, pure white, or PlayStation Blue alternate down the page like scenes in a launch trailer. Chrome stays deliberately quiet — no gradients, no resting shadows, no ornament — so console renders and game key art carry 60-90% of every band. The one loud choice is typographic: display headlines set in a light 300 weight, giving a gaming brand an unexpectedly airy, editorial voice.

## Layout
Black primary nav (~48px) with centered link row, plus an optional black sub-nav strip on deeper pages. Hero bands run edge-to-edge at 96px vertical padding; sections stack on a strict 96px rhythm where the next band's background color IS the divider — no rules, no washes. Content caps near 1280px with ~24px gutters; text sits in a narrow left column (~520px) while imagery breathes across the right two-thirds. Game rails run 4-up 16:9 carousels; support pages use a 30/70 sidebar split; footer is a full blue band.

## Components
Buttons are always full pills, 48px tall, bold 18px labels with slight positive tracking: blue fill for every primary action (pressed drops to #0064b7), a dedicated orange #d53b00 pill only for buy/pre-order, and transparent hairline-outlined pills for secondary actions on either canvas. Cards are 8px-radius, flat, borderless-or-hairline: cool blue-gray #f5f7fa on white pages, #181818 on black; game tiles are pure 16:9 art with an overlaid caption. Inputs break the pill rule at 4px radius with a 2px blue border on focus (no halo); the support search is the lone pill-shaped field. Filter chips flip from translucent to opaque white when active. A single gold gradient (#ffce21 → #ee8e00) exists, welded to the PS Plus banner.

## Signature
- Three-canvas band rhythm: black / white / #0070d1 chapters with color change as the only section divider
- Feather-light 300-weight display type next to heavy 700 pill labels — dramatic weight contrast in one line
- Two-radius shape grammar: pill for anything clickable, 8px for anything that holds content, 0 for structure
- Color discipline: blue means "act," orange means "buy," gold means "PS Plus" — nothing bleeds across roles

## Do / Don't
**Do**
- Cap PlayStation Blue at one full-bleed band per page (footer or the single action strip); use it for CTA pills otherwise
- Set all display sizes (54/44/35/28/22) at weight 300; save 600-700 for card labels and button text
- Let 16:9 key art and product renders dominate each band; compress copy into a small left-aligned slot
- Keep cards shadowless at rest — depth comes from band color contrast, with lift only on press
- Hold the 96px section cadence and let bands run full-bleed edge to edge

**Don't**
- Don't put the orange commerce pill on marketing or hero moments — it is store-action-only
- Don't add gradients to chrome; the gold PS Plus bar and the one dark hero fade are the only exceptions
- Don't swap in medium-radius buttons — every CTA is a full pill, no in-between shapes
- Don't nudge the blue: #0070d1 default, #0064b7 pressed, exactly
- Don't mix in a second typeface, italics, or mono — one sans family covers every role
