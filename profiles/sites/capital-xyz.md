---
name: capital-xyz
kind: site
style: DT
category: fintech
website: https://capital.xyz/
pages: [home]
palette:
  canvas: "#0D0C0B"
  ink: "#F2EFE9"
  primary: "#F15B40"
  accents: ["#F2EFE9", "#1A1A18"]
typography:
  display: "neutral grotesque (Neue Haas / Suisse-like) · regular-to-medium weight · tight, near-default tracking"
  body: "same grotesque family, small sizes; micro-labels in uppercase monospace-feel caps"
radius: "buttons pill (nav CTA) to full circle (footer CTA); cards medium 8-14px"
---
## Overview
Near-black editorial fintech page that alternates full-bleed black sections with warm cream ones, all typeset in a single quiet grotesque. Color is rationed to one coral-red CTA that recurs from a tiny nav pill to a giant circular "Start" button at the foot of the page. Product UI screenshots (cream/white dashboard, black payment buttons) do most of the visual storytelling; decoration is nearly absent.

## Layout
Minimal centered nav: small square logo mark + wordmark top center; a slim sticky utility bar (icons left, text links + red Start pill right) appears on scroll. Hero is a huge centered two-line headline over a large tablet mockup that bleeds past the section edge. Sections alternate black / cream / black in full-width bands, each with generous vertical padding. Feature sections use asymmetric two-column splits (large UI card left, short heading + two-column small body text right, or vice versa) and oversized left-aligned headings ("Hold", "Crypto connection"). Social proof is a centered logo strip on cream; team/testimonial row is a 3-up grid of B&W portraits on black. Footer is nearly empty: giant coral circle CTA, then one line of tiny legal text.

## Components
- Primary CTA: coral-red (#F15B40) filled pill with white text in the nav bar; the same action rendered as an enormous perfect circle before the footer — no border, no shadow, flat fill.
- In-product buttons (inside mockups): black pill "Send a payment" with icon, white bordered pill "Account Details" — pill shapes throughout.
- Cards: cream (#F2EFE9) rounded rectangles (~10-12px) floating on black, containing the account-balance UI; inner list rows with tiny avatars and right-aligned amounts.
- Small crypto toggle card: dark rows with pill toggles on a faint grid-line background motif.
- Imagery: grayscale portrait photos in hard-edged (unrounded) rectangles; device mockups (tablet, iPhone) as primary illustration.
- No visible inputs, gradients, or drop shadows; separation is done purely by background-color banding.

## Signature
- One accent color only: the coral-red Start button, escalating from nav pill to a full-viewport-width circle at page end.
- Black / cream section banding with the product's own cream dashboard UI reused as the card language.
- Short punchy verbs as section heads ("Hold", "Start") set very large in a plain grotesque with a period-terminated hero sentence.
- Grayscale founder portraits in a strict 3-up grid — no color photography anywhere.

## Do
- Keep the palette to black, warm cream, and a single coral CTA; let real product UI supply all remaining color and detail.
- Alternate full-width black and cream bands instead of using borders or shadows for section separation.
- Set headlines large and plain (regular/medium grotesque, sentence case, ending period); pair with very small two-column body text.
- Use pill-shaped buttons everywhere, and consider one oversized circular CTA as the page's closing moment.
- Convert photography to black-and-white and crop it into sharp-cornered rectangles.

## Don't
- Don't introduce gradients, glows, or drop shadows — every surface here is flat fill.
- Don't add a second accent color or color-tinted links; coral is reserved for the Start action.
- Don't use heavy/bold display weights or uppercase headlines; the voice is quiet and bookish.
- Don't round the corners of photos or make cards float with elevation — only UI cards get radius, and only ~10px.
- Don't crowd the nav: keep it to a centered mark plus a slim utility strip; no mega-menus.
