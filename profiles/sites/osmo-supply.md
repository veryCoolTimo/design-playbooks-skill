---
name: osmo-supply
kind: site
style: DT
category: dev-tools
website: https://www.osmo.supply/
pages: [home, pricing, faq]
palette:
  canvas: "#0a0a0a"
  ink: "#e8e6e3"
  primary: "#efedea"
  accents: ["#ff4c24", "#8a8a8a", "#1a1a1a"]
typography:
  display: "Neue Haas / Helvetica Now grotesque · medium weight · tight, slightly negative tracking"
  body: "Same neo-grotesque family, regular weight; monospace (uppercase, wide-tracked) for eyebrows and micro-labels"
radius: "small 2-6px on buttons and tabs; medium 8-14px on pricing cards and panels"
---
## Overview
Near-black studio-grade dark theme where almost everything is monochrome — off-white text on #0a0a0a — punctuated by a single blaze-orange accent used sparingly (hero flame imagery, the lifetime-plan card, a strike-through slash). Typography does all the branding: a tight neo-grotesque for headlines paired with tiny uppercase monospace metadata labels, giving a technical, print-catalog feel. Textural black-on-black photography (rock, smoke) adds depth without color.

## Layout
Sticky top nav split into zones: wordmark left, asterisk glyph mark offset left-center, centered text links (Home / Pricing / FAQ, active link underlined), Log in + white "Get Started" button right. Heroes are left-aligned or centered display headlines over dark photographic backgrounds. Sections alternate pure-black bands with embedded app-UI screenshots and card grids; generous vertical whitespace between bands. FAQ uses a two-column split: sticky tab group (General / Support / Account) on the left, hairline-divided accordion list on the right. Every page ends with the same centered sign-up CTA block ("Let's make this official") with avatar cluster + social proof, then a 4-column footer topped by monospace column labels, closing with a giant ghosted "Osmo" wordmark at ~10% opacity bleeding off the page bottom.

## Components
- Buttons: primary CTA is solid off-white (#efedea) with black label, small 4-6px radius, no shadow ("Get Started", "Become a member", "Sign up"); on the orange card the CTA inverts to solid black with white label.
- Cards: very dark gray (#141414-#1a1a1a) panels with subtle 1px darker borders, ~12px radius; the lifetime plan card is a full flood of #ff4c24 with black text.
- Accordions: full-width rows separated by 1px hairlines (~#2a2a2a), thin "+" icon right-aligned, no boxes.
- Tabs/toggles: segmented controls (FAQ categories, Quarterly/Annually) — bordered pill-ish rectangles where the active segment gets a lighter fill and border.
- Inputs: newsletter fields are borderless with only a bottom hairline, placeholder in gray; monospace status chips ("141/250 spots left") sit in small bordered rectangles.

## Signature
- One accent only: blaze orange (#ff4c24) reserved for a single hero flame and a single flooded pricing card — everything else grayscale.
- Uppercase wide-tracked monospace micro-labels (FAQS, PRICING, SITEMAP, "€75 BILLED QUARTERLY") acting as a second typographic voice against the grotesque.
- Giant ghost "Osmo" wordmark + asterisk glyph at low opacity filling the footer.
- Black-on-black textural photography (rock/smoke) under heroes instead of gradients or illustration.

## Do / Don't
Do:
- Keep the canvas at true near-black (#0a0a0a) and build hierarchy with gray steps (#141414 cards, #2a2a2a hairlines), not colored surfaces.
- Use white/off-white filled buttons as the primary CTA; invert to black-on-orange only when sitting on the accent surface.
- Pair every section headline with a tiny uppercase monospace eyebrow label.
- Flood exactly one element per view with the orange accent to create a focal point (as the lifetime plan card does).
- End pages with the ghosted oversized wordmark and the repeated sign-up CTA band.

Don't:
- Don't introduce blues, greens, or gradients — the palette is strictly black/white/one orange.
- Don't put borders or shadows around accordion items; hairline dividers only.
- Don't use large radii or pill buttons — corners stay crisp at 4-12px.
- Don't set headlines in bold-black weights; the display type is medium with tight tracking, never heavy.
- Don't decorate heroes with illustration or 3D renders; use dark textural photography or plain black.
