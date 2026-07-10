---
name: mistral.ai
kind: site
style: GR
category: ai-foundation-models
website: null
pages: [home, product, solutions, news-article, contact, services]
palette:
  canvas: "#ffffff"
  ink: "#1f1f1f"
  primary: "#fa520f"
  accents: ["#ffd900", "#ffa110", "#ff8105", "#fff8e0", "#cc3a05"]
typography:
  display: "PP Editorial Old · regular (400) at huge sizes · tight negative tracking (-1.5px on hero)"
  body: "Inter"
radius: "buttons small-medium 8px; cards medium 12px; pills only on badges"
---
## Overview
A sunset-themed gradient system: warm oranges, mustard yellows, and cream layered over photographic mountain landscapes. White canvas carries most content while cream-yellow panels warm up forms, feature cards, and the footer. The voice comes from an editorial serif/sans split — classical PP Editorial Old for giant hero lines, Inter for everything functional. Restrained, magazine-like geometry rather than playful SaaS rounding.

## Layout
Sticky white top nav (~64px, hairline bottom border) with an optional black promo strip above it; logo plus horizontal links left, contact link and dark CTA right. Hero is a two-column split — massive serif headline and button row on the left, atmospheric sunset/mountain photography on the right — with very deep padding (~120px). Content sits in a 1280px container with 32px gutters; marketing sections breathe on 96px rhythm, denser pages drop to 64px. Product pages run 3-up feature grids, services uses a 4-tier card row, contact centers a single ~520px cream form panel. Every page ends the same way: a full-width horizontal gradient stripe (red → orange → yellow → cream) just above a cream 5-column footer.

## Components
Buttons: 8px radius, 10px/20px padding, 14px medium Inter. Variants: saturated orange fill with white text (primary; pressed darkens to #cc3a05), solid black on cream surfaces, cream fill with beige border, and transparent outlined secondary. Explicitly not pills. Cards: 12px radius, 1px soft hairline borders, mostly flat — shadows stay whisper-light (rgba 0.04) and are saved for product mockups; featured pricing card gets a cream fill plus 2px orange border. Inputs: 44px tall, white, 1px gray border that swaps to a 2px orange border on focus, hosted inside a cream form panel. Badges are fully rounded pills in orange, cream, or black; tabs come as pill chips (black when active) or underline tabs with an orange 2px indicator. Dark near-black code blocks in JetBrains Mono provide the only heavy contrast surfaces.

## Signature
- The closing "sunset stripe": a full-width multi-stop gradient band (#fa520f → #ffa110 → #ffb83e → #ffd900 → #fff8e0) at the bottom of every page — the single strongest brand marker
- Mountain photography bathed in orange-red sunset light behind the hero headline
- PP Editorial Old serif at 84px/1.05 with -1.5px tracking against workmanlike Inter body copy
- Cream-yellow (#fff8e0) surfaces with beige (#e6d5a8) hairline borders on forms, feature panels, and the footer

## Do
- End every page with the sunset stripe gradient band above the footer, full-width at all breakpoints
- Keep #fa520f exclusive to primary CTAs, active states, links, and the stripe
- Set hero and stat callouts in the editorial serif (or a close near-serif) at 400 weight with tight leading; keep all UI text in Inter
- Use cream panels with beige borders for forms, tier cards, and the footer instead of gray neutrals
- Stay flat: hairline borders on cards, reserving real shadows for dark IDE/product mockups

## Don't
- Don't make buttons pill-shaped — 8px radius is the rule; full rounding belongs to badges only
- Don't add accent hues outside the orange/yellow/cream sunset range
- Don't set the hero headline in the sans face or bold it up; the light serif contrast is the identity
- Don't stack heavy drop shadows on content cards; the depth budget lives in photography
- Don't loosen display leading past ~1.05–1.15 or drop the negative tracking at large sizes
