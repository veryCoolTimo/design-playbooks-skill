---
name: privy
kind: site
style: ML
category: web3-dev-infrastructure
website: https://www.privy.io/
pages: [home, about, features, pricing, security]
palette:
  canvas: "#FBFAFC"
  ink: "#1B1B22"
  primary: "#4E46E5"
  accents: ["#FF6650", "#C9BDF4", "#F6D5D8", "#F1F0F5"]
typography:
  display: "ABC Favorit-like geometric grotesque · medium-to-semibold · slightly tight, with italic emphasis words"
  body: "same geometric grotesque family, regular weight, small sizes (13-15px)"
radius: "small 2-6px on buttons; medium 8-12px on cards and UI mockups"
---
## Overview
Minimal light SaaS language built on a near-white canvas with soft radial pastel washes (peach, pink, lavender) bleeding in from hero corners and section edges. Near-black grotesque type carries the page; a single saturated indigo owns every CTA, while a coral logo mark and candy-colored product icons add small warm pops. Floating product-UI mockups (login modals, wallet cards) with soft shadows stand in for photography.

## Layout
Slim sticky top nav: coral logomark left, center text links (About, Features, Docs, Security, Pricing), right side a text "Demo >" link plus a solid indigo "Dashboard" pill-adjacent button; features page adds a secondary sub-nav tab row with an underline on the active tab. Heroes are split: left-aligned display headline (with one italicized word) + short paragraph + indigo button and a text link, right side a floating UI mockup or 3D illustration over the pastel gradient wash. Section rhythm alternates white and very light gray (#F7F7F8) bands; mid-page sections use centered eyebrow (small text like "Enterprise-grade") over a large centered H2. Content sits in a narrow ~1100px column with generous vertical padding; 2x2 icon-feature grids with thin divider lines, zig-zag text/mockup rows, logo marquees ("TRUSTED BY..." and "BACKED BY" in letterspaced caps) bookend pages.

## Components
Buttons: solid indigo fill, white label, small ~6px radius, compact height, almost always suffixed with a chevron ">"; secondary action is a plain indigo text link with chevron, no outline-button style seen. Cards: white fill, 1px light gray border, 8-12px radius, essentially shadowless (audit cards, pricing tiers, blog cards); the highlighted pricing tier gets a 2px indigo border and a coral "First 1,000 MAUs FREE" tag. Audit/status cards carry small pill badges ("Status: Complete") with a check icon. Feature grids use small colorful 3D-ish icons on white tiles with thin hairline dividers between columns/rows. Pricing comparison table uses zebra-striped rows with tiny indigo checkmarks. Mockup modals inside artwork have larger radius (14-16px) and soft diffuse shadows.

## Signature
- Pastel radial gradient washes (peach-pink-lavender) melting into a white canvas at hero and section boundaries
- One indigo for every CTA, always paired with a ">" chevron; coral reserved for the logo and rare badges
- Display headlines that italicize a single word ("Onboard *all* of your users", "deserve *safer* data")
- Floating, layered login-modal and wallet-UI mockups as the primary imagery, plus playful candy-colored micro-icons
- Hairline dividers organizing icon-feature grids instead of boxed cards

## Do
- Keep CTAs to one indigo fill style with a trailing chevron; use plain indigo text links as the secondary action
- Let pastel gradient washes fade organically into white; keep body sections clean white or #F7F7F8 gray
- Italicize one emphasis word in major headlines; keep headlines short (2 lines max)
- Use thin 1px borders and hairline dividers instead of shadows to structure cards and grids
- Set logo strips and eyebrows in small letterspaced uppercase, flanked by "AND MANY MORE" style footnotes

## Don't
- Don't use coral/orange for buttons — it is logo and badge accent only
- Don't add heavy drop shadows to cards; only floating UI mockups inside artwork get soft shadows
- Don't use large border radii on buttons (no pills); keep them compact and squarish
- Don't crowd sections — every band gets generous vertical padding and a narrow content column
- Don't introduce dark sections; the whole system stays light with near-black type
