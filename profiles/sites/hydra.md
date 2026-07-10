---
name: hydra
kind: site
style: IL
category: dev-data-tools
website: https://www.hydra.so/
pages: [home, pricing, product, resources]
palette:
  canvas: "#101010"
  ink: "#E9E7E2"
  primary: "#F2731D"
  accents: ["#1C1C1C", "#FFFFFF", "#000000"]
typography:
  display: "geometric grotesque (Aeonik/Space Grotesk feel) · medium weight · tight, near-zero tracking"
  body: "same grotesque family · regular · airy line-height at small sizes"
radius: "pill (buttons, step badges); large 16-24px (cards and full-width section blocks)"
---
## Overview
Two-color world: near-black charcoal and one saturated orange, traded back and forth so entire sections flip from dark-on-orange to orange-on-dark. Greco-Roman line illustrations (war elephant with rider, amphorae, toga figures, meander/logo friezes) carry the brand, drawn as single-weight outlines in whichever color opposes the background. The effect is an antique-engraving-meets-terminal aesthetic for a Postgres analytics engine.

## Layout
Centered top nav (logo left, Product/Resources/Pricing center, social icons + white pill CTA right) on the dark canvas. Home hero is a full-bleed orange rounded block: black elephant illustration left, left-aligned display headline right, meander frieze strip along the bottom edge. Page rhythm alternates large rounded-corner slabs — dark section, orange section, dark section — each inset from the viewport edge so the black canvas shows as a gutter. Content sits in a comfortable centered column; feature rows pair illustration/screenshot with short copy blocks. Pricing is a stepped configurator (Step 1-4 outlined badges) with a sticky-feeling cost summary card at right. Resources is a two-column blog card grid with a full-width orange featured card.

## Components
Buttons: pill-shaped; primary CTA is solid orange with dark text plus a circular arrow chip (pricing "Create Hydra"), nav CTA is white pill with orange arrow circle; on orange sections buttons invert to black pills with white text. Secondary is a thin-outline pill. Cards: dark #1A1A1C rounded rectangles with subtle 1px borders, no shadows; selected state gets a 1px orange border (Pro plan). Step/tag badges are small orange-outlined rounded chips with orange text. Inputs: dark fields with thin borders or simple underlines (newsletter email is a bare underline); dropdowns are bordered dark rectangles with chevrons. Toggle groups are pill segments where the active segment fills orange. Bar charts render orange vs gray bars on dark panels with huge orange stat numerals (512x, 283x).

## Signature
- Strict two-color system: everything is orange, near-black, or white — no third hue anywhere in the UI chrome.
- Ancient-world line art (elephant + rider bearing the logo shield, amphora "data vase," toga figures) redrawn per background: black fill on orange, orange outline on black.
- Meander-style frieze borders built from the repeating Hydra logomark edging hero and footer blocks.
- Full-width rounded slabs that alternate orange/dark, giving the page a banded, poster-like rhythm.

## Do / Don't
**Do**
- Alternate whole sections between orange-filled and dark slabs with large (16-24px) corner radii and visible black gutters between them.
- Render illustrations as single-weight line engravings that invert color against their background; put the logomark inside the artwork (shield, vase).
- Use pill buttons everywhere, pairing text with a small circular arrow chip; invert button color scheme on orange sections.
- Mark selection and metadata with thin orange 1px outlines (chosen plan card, step badges, category tags) rather than fills or shadows.
- Set oversized orange numerals for performance stats against gray comparison bars.

**Don't**
- Introduce additional accent colors, gradients, or photographic hero imagery — the system is flat orange/black plus white text (blog thumbnails are the only photo exception).
- Use drop shadows or glassmorphism; depth comes only from surface-tone steps (#101010 vs #1A1A1C) and 1px borders.
- Round corners inconsistently — small 4-6px radii on cards would break the pill/large-slab language.
- Fill tag chips or step badges solid; they are outline-only.
- Center-align hero copy on the home page — display text sits left-aligned beside the illustration.
