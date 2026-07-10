---
name: herokit
kind: site
style: CP
category: design-utility-saas
website: https://herokit.design/
pages: [home, pricing]
palette:
  canvas: "#0A0A0A"
  ink: "#F2F2F2"
  primary: "#F2F79B"
  accents: ["#F5E04A", "#E63312", "#6FE39A", "#F27BB8", "#12225C"]
typography:
  display: "Neo-grotesque (Helvetica Now / Suisse Int'l feel) · regular-to-light weight at huge sizes · tight, near-zero tracking"
  body: "Same neo-grotesque, small size, regular weight"
radius: "pill on buttons; medium 8-14px on cards and embedded browser frames"
---
## Overview
A near-black stage punctuated by one loud lemon-yellow signature color and bursts of saturated demo artwork (3D blobs, gradients, vivid hero thumbnails). Headlines are enormous, plainly set grotesque type at light-to-regular weight, so the playfulness comes from color and imagery, not typographic quirks. The home page opens on a full-bleed yellow hero with glossy orange 3D spheres, then drops into long black sections; pricing is black throughout with a pale-yellow highlighted plan card.

## Layout
Slim top nav: wordmark + lightning glyph left, sparse text links right, pill "Try for free" CTA. Home hero is a full-width yellow gradient block with left-aligned display headline, short subcopy, small red pill CTA, and 3D sphere clusters framing both corners; a logo marquee strip (Squarespace, Framer, Wix, Webflow...) sits directly beneath. Sections are long and dark with generous vertical whitespace. A repeated three-line step headline ("Pick a Hero / Customize / Publish") acts as a progress device: the active line is white with an em-dash prefix, inactive lines are dim gray. Showcase content runs in edge-to-edge multi-column thumbnail grids and full-width app screenshots. A horizontally scrolling ticker of pill-shaped feature tags separates sections. FAQ is a right-aligned single column of hairline-divided accordion rows with plus icons. Footer is minimal: "Made by 14islands," social icon pills, yellow subscribe/get-started pill.

## Components
Buttons: pill-shaped, small; pale-yellow fill with black text for primary actions ("Try for free," "Get started"); inverse black fill with white text used inside the yellow highlighted pricing card; small red pill CTAs on the yellow home hero. Pricing cards: ~12px radius, black fill with thin dark-gray border, small circular icon badge top-left, checkmark-prefixed feature lists, full-width pill CTA at bottom; the recommended plan flips to a pale-yellow card with a "RECOMMENDED" outline chip. Monthly/Yearly pill toggle with a small yellow "20% OFF" chip. FAQ rows: text + plus icon separated by 1px hairlines, no card chrome. Demo heroes shown inside rounded mock-browser frames with traffic-light dots. No visible drop shadows anywhere — separation is done with color blocks and hairlines.

## Signature
- One-color branding: lemon yellow (#F2F79B–#F5E04A) is the only UI accent on an otherwise black/white interface; every other color lives inside demo artwork.
- Giant plainly-set grotesque headlines with an em-dash-prefixed active step and grayed-out sibling lines, repeated as a scroll narrative.
- Glossy 3D orange spheres on the flat yellow hero; vivid gradient-blob thumbnails as the product's own showcase.
- Pill everything interactive (buttons, chips, toggles, feature-tag ticker) against sharp-edged full-bleed color sections.

## Do / Don't
**Do**
- Keep the UI palette to black, off-white, and one lemon yellow; let saturated color enter only through showcased artwork.
- Set headlines very large in a plain neo-grotesque at regular weight; scale, not boldness, carries hierarchy.
- Use the dim-gray inactive / white active line trick (with an em-dash marker) for multi-step storytelling.
- Make all buttons small pills; invert to black-on-yellow when the surface itself is yellow.
- Separate FAQ and list rows with 1px hairlines instead of cards or shadows.

**Don't**
- Don't add drop shadows, glows, or gradients to UI chrome — surfaces are flat with thin borders.
- Don't introduce a second accent color for links or states; red appears only as a tiny CTA on the yellow hero.
- Don't use heavy/black font weights or condensed display faces for headings.
- Don't box the FAQ or feature lists into cards; the dark canvas plus hairlines is the pattern.
- Don't center the hero — headlines and copy blocks are left-aligned or deliberately offset right (FAQ, "Create your hero today" subcopy).
