---
name: luroapp
kind: site
style: DT
category: design-system-tools
website: https://luroapp.com/
pages: [home, pricing, blog]
palette:
  canvas: "#1E0714"
  ink: "#FFFFFF"
  primary: "#EC2C8C"
  accents: ["#F9A03F", "#8A2BE2", "#211F1F", "#3A0F2A"]
typography:
  display: "compact heavy grotesque (Helvetica Now / Founders Grotesk feel) · extra-bold · tight, near-zero tracking"
  body: "neutral humanist grotesque (Graphik / GT America feel)"
radius: "buttons pill; cards medium-large 12-16px"
---
## Overview
Dark-tech landing system built around a magenta-to-orange gradient signature on near-black plum and charcoal canvases. Heavy, tightly-set grotesque headlines in pure white (or pure black on light pages) carry most of the personality; everything else stays quiet and monochrome so the hot gradient reads as the single energy source. The site freely flips polarity per page — pricing is fully dark plum, home is dark hero over white body, blog is white with dark plum image cards — but the gradient thread ties them together.

## Layout
Sparse top nav: logo left, two or three text links plus one gradient pill CTA right, no mega-menus. Hero is centered stacked text: giant two-line headline, a thin horizontal gradient divider bar directly beneath it, short subhead, single CTA — no hero imagery except a large light-mode app screenshot that bleeds across the dark/light boundary below the fold. Mid-page sections use a roomy 2-column feature grid (small line icon, bold heading, two-line body). Pricing is a classic 3-card row with soft magenta glow halos around each card. Blog is a single-column list: fixed-width plum illustration card left, title/excerpt/date right, generous vertical gaps. Whitespace is generous throughout; content max-width is fairly narrow and centered.

## Components
Buttons: two species — the primary gradient pill (magenta #EC2C8C to orange #F9A03F left-to-right fill, white bold label, trailing arrow glyph) and a ghost/outline rectangle (1px white border on dark, transparent fill, e.g. "Join waitlist"). Pricing cards: dark plum (#2A0A1E-ish) fill, ~14px radius, no visible border, soft pink outer glow; internal feature rows separated by faint 1px hairlines with small pink circular check badges. Blog cards: deep plum rounded rectangles containing flat gradient-toned illustrations or white app screenshots. App screenshot framed in a browser chrome with traffic-light dots. A pill "Early Bird Price" badge with thin outline. No drop shadows on light sections — flat white with hairline separation.

## Signature
- The magenta→orange gradient used everywhere: CTA fills, divider bars under headlines, illustration palettes, check badges.
- Thin horizontal gradient "underline bar" centered beneath hero and page-title headlines.
- Dark plum (not neutral gray) as the dark-mode base, giving the black a warm magenta cast, plus glowing pink halos around pricing cards.
- Ultra-bold, tightly-tracked grotesque display type at very large sizes with minimal supporting copy.

## Do / Don't
Do:
- Reserve the magenta→orange gradient for CTAs, the headline divider bar, and small badges; keep large surfaces monochrome.
- Set headlines extra-bold and tight in pure white on dark (or pure black on white), sized much larger than everything else.
- Use pill-shaped gradient buttons with a trailing arrow for primary actions; a thin white-outline rectangle for secondary.
- Tint dark sections toward warm plum/maroon rather than neutral charcoal, and add a soft pink glow behind featured cards.
- Keep nav minimal: a few text links and exactly one gradient CTA.

Don't:
- Add blues, greens, or cool tones as UI accents — the rainbow spectrum appears only inside product screenshots and one hero divider, never on controls.
- Use drop shadows on light sections; separate content with whitespace and 1px hairlines instead.
- Fill hero backgrounds with photography or busy patterns — heroes are flat dark canvas plus type.
- Mix radius languages: buttons are always full pills, cards always moderately rounded, never sharp-cornered.
- Crowd sections; every block gets generous vertical padding and a narrow centered measure.
