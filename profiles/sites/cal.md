---
name: cal
kind: site
style: ML
category: scheduling-saas
website: null
pages: [home, pricing, features, testimonials]
palette:
  canvas: "#ffffff"
  ink: "#111111"
  primary: "#111111"
  accents: ["#3b82f6", "#fb923c", "#ec4899", "#8b5cf6", "#34d399", "#f5f5f5", "#101010"]
typography:
  display: "Cal Sans (custom geometric; fallback Inter 600 or Manrope 700) · semibold 600 · tight negative tracking (-0.5 to -2px)"
  body: "Inter"
radius: "small-medium 8px on buttons/inputs; medium 12px on cards, 16px on hero mockup; pill for nav groups and badges"
---
## Overview
A near-monochrome SaaS marketing language: pure white pages, near-black (#111111) CTAs and headlines, and quiet #f5f5f5 gray cards. Distinctiveness comes from the custom Cal Sans display face with tight tracking and from real product UI (calendar grids, booking widgets) embedded inside marketing cards instead of illustrations. Color is rationed — a blue link accent and pastel avatar fills are the only chroma. Every page closes with a #101010 footer, the sole dark band in the layout.

## Layout
64px white top nav: wordmark left, horizontal menu center, "Sign in" link plus black CTA right; collapses to a full-screen hamburger sheet under 768px. Hero is a 7/5 split — Cal Sans headline and button row on the left, a bordered 16px-radius product mockup card on the right. Sections run on a 96px vertical rhythm inside a ~1200px container, alternating surface modes (white → gray cards → white → mockup → dark footer) and never repeating a mode twice in a row. Grids are 3-up features, 4-up pricing, 4-column footer, all shedding columns rather than shrinking cards.

## Components
Primary button: #111111 fill, white Inter 600 14px label, 8px radius, 40px tall, darkening to #242424 on press. Secondary: white with a 1px #e5e7eb hairline, same geometry. Cards come in two intentional flavors — flat #f5f5f5 gray for abstract feature claims, white-with-hairline for actual product screenshots — both 12px radius with 24-32px padding and at most a faint shadow (0 1px 2px / 0 4px 12px at low alpha). Featured pricing tier inverts to #101010 with white text; the dark fill alone signals emphasis. Inputs: 40px, white, hairline border, 8px radius, border darkening to ink on focus. A signature pill-in-pill segmented switcher sits on a #f8f9fa pill wrapper with a white shadowed pill for the active tab. Avatars are 36px circles, occasionally pastel-filled with initials.

## Signature
- Cal Sans headlines: geometric, weight locked at 600, always negative-tracked — instantly reads as Cal.com.
- Genuine product chrome (booking calendar, workflow editor) shown small-scale inside marketing cards.
- Monochrome action layer: black button on white canvas; accent colors never touch CTAs.
- One deliberate dark inversion per page — the #101010 footer (plus the featured pricing card).

## Do / Don't
**Do**
- Keep every CTA #111111 on white; reserve blue and pastels for inline links, badges, and avatar fills.
- Track display type -0.5 to -2px at weight 600; scale size up, not weight, for emphasis.
- Split card semantics: gray #f5f5f5 for feature claims, white bordered cards for real product UI.
- Alternate band surfaces down the page and finish with the dark footer.
- Use the pill-group switcher (soft-gray wrapper, white active pill) for sub-navigation.

**Don't**
- Don't push display weight to 700 — the brand voice lives at 600.
- Don't exceed 16px card radius; larger corners read consumer-app, not booking software.
- Don't place dark surfaces anywhere except the footer and the single featured pricing tier.
- Don't color primary buttons with the blue accent or badge pastels.
- Don't stack two same-surface sections back to back — the white/gray/dark cadence is the pacing.
