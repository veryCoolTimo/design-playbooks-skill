---
name: tome
kind: site
style: DN
category: ai-saas
website: https://tome.app/
pages: [home, feature, blog, templates, use-cases]
palette:
  canvas: "#000000"
  ink: "#E7E7E7"
  primary: "#FF00BF"
  accents: ["#8A5CF6", "#5B7CFA", "#2FD05E"]
typography:
  display: "neo-grotesque sans (Graphik/Söhne-like) · medium · tight; editorial serif for set-piece headings"
  body: "same neo-grotesque sans, small size, muted gray"
radius: "small 2-6px on buttons; medium 8-14px on cards and media frames"
---
## Overview
Near-total black canvas with restrained gray typography, punctuated by a single loud magenta CTA and vivid purple-blue gradient imagery. The page itself stays monochrome; all color lives inside embedded product screenshots, template thumbnails, and AI-generated art. Occasional serif set-pieces ("Tome Blog", "Substance. Structure. Style.") add an editorial counterpoint to the otherwise cool, technical grotesque.

## Layout
Slim top nav on black: tiny magenta logomark left, center-aligned text links, "Sign in" plus a compact "Try Tome" button right. Heroes are centered stacked text (short two-line headline, small subcopy, one magenta button) followed by a full-bleed gradient or collage visual. Sections alternate: left-aligned label + heading blocks, 2-3 column card grids, huge full-width product-UI screenshots in rounded dark frames, and a dense masonry of template thumbnails. Very generous vertical whitespace — long black gaps between sections. Every page closes with the same centered "Craft your next great idea." + magenta CTA outro.

## Components
Buttons: solid magenta (#FF00BF) fill, black or white label, small corner radius, no border or shadow; secondary buttons are dark gray fills or thin-outline ghosts on black. Cards: near-black (#121212-ish) panels with medium radius, no visible border, image on top, small gray meta line (category · date), white title, gray excerpt — flat, shadowless. Template thumbnails are light or colored rectangles that pop against black. Inputs (AI prompt bar): dark rounded field with light placeholder text and small pill toggles. Success states use a small green check-in-circle. Blog filter row uses quiet text tabs with one highlighted pill.

## Signature
- Absolute black background with exactly one saturated brand color (magenta) reserved for CTAs and the logomark
- Color arrives only through content: purple/blue gradient renders, AI imagery, and multicolored template cards floating on black
- Serif interludes inside a sans system — oversized editorial serif for blog titles and philosophical statements
- Recurring closing ritual: centered "Craft your next great idea." with a lone magenta button on empty black

## Do / Don't
Do:
- Keep the page chrome monochrome (black, grays) and let screenshots/thumbnails carry all the color
- Use one magenta CTA per viewport; repeat the same small solid button style everywhere
- Give sections long black breathing room; separate them with whitespace, not rules or background shifts
- Frame product UI in large rounded dark containers spanning most of the content width
- Switch to an elegant serif only for editorial or manifesto-style headlines

Don't:
- Add gradients, glows, or neon strokes to the interface itself — the DN energy comes from imagery, not chrome
- Use magenta for links, icons, or decorative elements; it is CTA-only
- Put visible borders or drop shadows on cards; they should dissolve into the black
- Brighten the canvas to dark gray or introduce light-mode sections mid-page
- Use large or pill button radii; buttons stay compact with barely-rounded corners
