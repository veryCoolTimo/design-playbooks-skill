---
name: june
kind: site
style: ML
category: product-analytics
website: https://www.june.so/
pages: [home, features, pricing, customers, changelog]
palette:
  canvas: "#FFFFFF"
  ink: "#16161D"
  primary: "#5E5CE6"
  accents: ["#EEEDFB", "#0B0B33", "#6B7280", "#F97316"]
typography:
  display: "Inter (grotesque sans) · bold 700 · tight, slightly negative tracking"
  body: "Inter"
radius: "buttons small 6px · cards medium 8-14px"
---
## Overview
Clean minimal-light SaaS language built on white canvas, near-black headlines, and a single indigo-violet brand hue used sparingly for CTAs and highlight words. Product screenshots (soft-shadowed dashboard cards) do most of the visual selling. One dramatic exception: the features page drops into a deep navy (#0B0B33) scrolling section where white dashboard cards float against darkness.

## Layout
Centered nav bar: logo left, 4 text links center, outlined Login + solid indigo Sign up right. Heroes are center-aligned: two-line headline with the second phrase in indigo, one-sentence gray subhead, single indigo CTA, then a large floating product screenshot with annotation callouts. Section rhythm alternates white canvas with pale lavender (#EEEDFB) panel blocks holding "eyebrow-label + heading + chart screenshot" pairs in a two-column split. Customers page is a strict 3-column card grid with logo tiles. Pricing is a 4-column card row with the recommended tier outlined in indigo. Generous vertical whitespace throughout; content column ~1100px. Recurring pre-footer CTA banner: lavender-tinted panel with subtle grid texture, "Set up June in 2 minutes" (indigo phrase), indigo button.

## Components
Buttons: solid indigo fill, white text, ~6px radius, no shadow; secondary is white with thin indigo or gray border. Cards: white or pale-lavender fill, 1px light gray border, 8-14px radius, minimal or no shadow; product-screenshot cards get a soft diffuse drop shadow. Pricing tiers use checkmark lists in indigo; featured tier gets an indigo outline instead of a fill change. Testimonials render as tweet-style cards in a masonry grid with avatars and timestamps. FAQ is a plain divider-separated accordion with +/- toggles. Small pill "eyebrow" labels (icon + uppercase text) introduce feature sections.

## Signature
- Two-tone headlines: black sans with one phrase flipped to indigo ("A new way to do **product analytics**")
- Real dashboard screenshots as hero art, floating with soft shadows and hand-drawn arrow annotations
- Pale lavender section panels (#EEEDFB) instead of gray for rhythm on white
- The abrupt deep-navy full-bleed scroll section on the features page — the only dark moment in the system
- Tweet-card masonry as social proof ("Loved by product people")

## Do
- Keep indigo (#5E5CE6) reserved for CTAs, highlight words, and checkmarks; everything else stays black/gray/white
- Use lavender-tinted panels, not neutral gray, to separate sections
- Sell with actual product UI screenshots in bordered, soft-shadowed cards
- Center-align heroes and CTA banners; left-align feature copy in two-column splits
- Mark the recommended pricing tier with an indigo border and filled button while other tiers stay outlined

## Don't
- Don't use gradients, illustration mascots, or decorative imagery — the product screenshot is the artwork
- Don't add heavy shadows or thick borders; cards live on 1px light strokes
- Don't introduce a second accent color for CTAs (orange appears only in the YC badge)
- Don't oversize the border radius — nothing here reads as pill-shaped except tiny eyebrow labels
- Don't put dark sections everywhere; the navy block works because it is a single contrast moment
