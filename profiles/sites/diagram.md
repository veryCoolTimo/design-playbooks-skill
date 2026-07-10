---
name: diagram
kind: site
style: DT
category: ai-design-tools
website: https://diagram.com/
pages: [home]
palette:
  canvas: "#0B0B0D"
  ink: "#A6A6AD"
  primary: "#232327"
  accents: ["#7B5CFA", "#3B82F6", "#F97316", "#22C55E"]
typography:
  display: "Inter-like geometric grotesque · bold/heavy · tight"
  body: "Inter-like grotesque, small sizes, muted gray"
radius: "pill buttons; large 16px+ cards"
---
## Overview
Near-black cosmic canvas with a faint starfield and orbital ring illustration; the whole page reads as a product universe at night. Color is rationed: neutral charcoal cards and gray text everywhere, with saturated violet, orange, blue, and green reserved for 3D product icons and glowing hero objects. Typography is quiet and small; the 3D renders (planets, magic wand with violet light spill, gradient orb) carry the personality.

## Layout
Minimal top nav: wordmark left, four centered text links (Magician, Genius, Automator, UI-AI), small "Login" pill right. Hero is fully centered: two-line bold headline with the second line dimmed to gray, short subcopy, one dark pill CTA, then a large 3D orbital illustration. The page is a vertical chain of product chapters, each opening with a centered 3D icon, product name, tagline, and a small pill CTA ("magician.design", "Coming soon"), followed by a bento grid of feature cards — mixed 1/3 + 2/3 and half-width spans on a contained (~1100px) grid with consistent ~16px gutters. Generous dark whitespace between chapters; four-column footer on the same black.

## Components
Buttons: small pill-shaped, dark charcoal fill (#232327) with subtle 1px lighter border, white text, often a leading "+" or icon; one blue (#2D8CFF) filled pill appears inside a UI mockup. Cards: #141416–#1A1A1E fills, 16-20px radius, hairline borders barely lighter than the fill, no visible drop shadows; each card holds a small bold white title, 1-2 lines of gray body text at top, and imagery below. Imagery inside cards includes embedded UI screenshots, emoji/icon grids, and 3D objects with colored glow. Inputs (in mockups): dark pill fields with icon and placeholder gray text.

## Signature
- Starfield-black background with a planetary orbit hero — product icons rendered as 3D "planets"
- Bento-grid feature sections repeated per product, each anchored by a centered 3D emblem and name
- Violet light-spill from a rendered 3D magic wand — glow used as illustration, not as UI chrome
- CTAs styled as understated dark pills (domain names as labels), never loud colored buttons

## Do / Don't
Do:
- Keep the canvas near-black (#0B0B0D) and let 3D renders/icons supply all saturated color
- Dim the second half of headlines to gray for the two-tone headline effect
- Compose features as bento grids of charcoal cards with hairline borders and 16-20px radius
- Center every section opener: 3D emblem, product name, one-line tagline, small pill CTA
- Keep body text small, gray (#A6A6AD), and limited to 1-2 lines per card

Don't:
- Use bright filled CTA buttons at page level — primary actions stay dark charcoal pills
- Add drop shadows or elevation; separation comes from fill steps and hairline borders
- Flood cards or backgrounds with gradient color; glow belongs to objects, not surfaces
- Use white or light section backgrounds anywhere, including the footer
- Left-align hero or section intros — the page rhythm is strictly center-axis
