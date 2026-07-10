---
name: usetola
kind: site
style: ML
category: fintech-saas
website: https://usetola.com/
pages: [home, product, solutions, pricing, company]
palette:
  canvas: "#FFFFFF"
  ink: "#1A1A1A"
  primary: "#1E1E1C"
  accents: ["#F09A5C", "#8B75F2", "#F8F5C6", "#EDEDEB"]
typography:
  display: "Neue Haas Grotesk / Helvetica-style grotesque · regular-to-medium weight (never heavy) · slightly tight"
  body: "Same grotesque family, regular weight, muted gray-black"
radius: "pill (buttons) + large 16px+ (cards and section containers)"
---
## Overview
Restrained Swiss-flavored fintech minimalism: near-white canvas, near-black type set at regular weight even for very large headlines, and huge breathing room. Color arrives only through photography (deep green fabric hero, lifestyle testimonial shots) and small pastel accents — orange, violet, pale yellow. The whole page reads like a printed spec sheet with occasional warm product-UI vignettes.

## Layout
Sticky-feeling top nav: wordmark "TOLA" left, center-right link row with dropdown carets, pill "Sign in" (light gray) and pill "Try for free" (black) at far right. Heroes are text-first: left-aligned H1 in the top white band, then a full-width rounded-corner photo or product image block below. Sections alternate white and light-gray (#EDEDEB-ish) bands whose containers have large rounded corners, creating a stacked-card page rhythm. Feature areas use a 4-up icon+label strip, then 2-column rows (text left, floating product-UI card right). Pricing is a borderless 3-column table with em-dash-prefixed feature lists. Footer is a full-width black rounded slab with 4-column link grid and long compliance fine print.

## Components
Buttons: pills exclusively — solid near-black with white label and trailing arrow for primary ("Get started", "Try for free"); light-gray pill for secondary ("Sign in"); pricing tiers get colored pills (black, orange #F09A5C, violet #8B75F2). Cards: white, shadow-soft floating mock-UI snippets (invoice, payment, cashback) with ~12-16px radius sitting on gray or pastel-gradient panels; no visible borders anywhere. Testimonials: full-bleed color blocks — pale-yellow quote card with orange serif-free text and a small outlined category pill tag, flanked by photography tiles. FAQ: plain text rows with plus icons, hairline dividers only.

## Signature
- Big headlines at regular font weight — scale does the work, not boldness
- Stacked rounded "card sections" alternating white and warm light gray
- Investor/brand logo strip rendered as oversized rounded app icons (PayPal, Robinhood, Klarna, Cash App)
- Pale-yellow testimonial cards with orange quote text next to full-bleed lifestyle photos
- Black pill CTA with trailing arrow, repeated identically in nav, sections, and the "Try Tola for free" outro band

## Do / Don't
Do:
- Set headlines large (60-90px) but at 400-500 weight, left-aligned, near-black on white
- Use pill buttons for every CTA and add a trailing arrow on primary actions
- Round section containers generously (16-24px) and alternate white / #EDEDEB bands
- Let photography and small floating product-UI cards carry all the color; keep chrome monochrome
- Repeat the same "Try Tola for free" black-pill outro section before the black footer on every page

Don't:
- Use bold/heavy display weights or centered hero text — everything here is regular-weight and left-aligned
- Add borders, outlines, or hard drop shadows to cards; separation comes from background tone shifts
- Use the accent orange/violet as body-link or nav color — they appear only in pricing pills, tags, and quote text
- Introduce blue "fintech" gradients; the palette is warm neutrals plus muted pastels
- Crowd sections — each block gets a full viewport-scale band of whitespace
