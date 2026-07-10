---
name: pirsch
kind: site
style: DT
category: analytics-saas
website: https://pirsch.io/
pages: [home, product, pricing, solution, blog]
palette:
  canvas: "#0a0a0a"
  ink: "#b8bdb9"
  primary: "#3fe0a1"
  accents: ["#f5d96d", "#8feebb", "#181c1a", "#ffffff"]
typography:
  display: "geometric grotesque (Poppins/Albert Sans family) · semibold · normal tracking"
  body: "same geometric sans · regular · relaxed line-height, small sizes"
radius: "pill buttons; medium 10-14px cards (blog covers up to 16px)"
---
## Overview
Near-black canvas with faint radial green glows, white geometric-sans headlines, and a single mint-green accent that carries every CTA. Content lives in slightly-lighter charcoal cards, so pages read as a dark grid of tiles punctuated by an embedded product dashboard screenshot glowing with green bar charts. A restrained secondary yellow marks the "Plus" tier and tags; everything else stays grayscale-plus-green.

## Layout
Sticky-feel top nav: logo left, center dropdown links (Product, Solution, Resources, Pricing), Log In plus a pill green "Try It for Free" button right. Heroes are centered: numbered-eyebrow or plain H1, 2-line muted subhead, green primary pill + dark ghost secondary pill side by side, avatar-row + star-rating social proof, then a full-width dark dashboard mockup. Sections alternate: centered numbered eyebrow labels ("1 · EASY START"), H2, then 2-3 column card grids of unequal spans (bento-ish). Grayscale customer-logo strip after the hero. Every page ends with the same centered logo mark + "Ready to Level up Your Analytics?" CTA block, then a multi-column footer with a GDPR-compliance badge bottom-left.

## Components
Buttons: fully pill; primary is solid mint green with near-black text, secondary is dark charcoal fill with light text and subtle 1px border; a yellow pill variant appears on the highlighted pricing tier. Cards: charcoal (#15-1a range) with very subtle lighter borders, 10-14px radius, no visible shadows — separation comes from fill contrast, not elevation. Feature cards on the product page carry small tier badges (green "Standard", yellow "Plus", gray "Enterprise") as tiny rounded chips. Pricing: three cards, middle "Plus" tier keyed yellow with "Best Value" badge and yellow CTA; long comparison table with green checkmarks and a highlighted middle column. FAQ: full-width dark accordion rows with plus icons. Blog cards: light-green duotone cover images (title overlaid in dark green) above a dark text block. Code blocks with syntax highlighting appear inside cards on the developer page.

## Signature
- One mint green (#3fe0a1-ish) doing all the work: CTAs, chart bars, checkmarks, eyebrow numbers — on an otherwise grayscale near-black page
- Numbered section eyebrows ("2 · INSTANT OUTPUT") pacing a long scrolling narrative
- Embedded real dashboard screenshots with green analytics charts as hero imagery
- Blog covers as flat green-duotone images with dark-green display type baked in
- Yellow reserved strictly as a tier/"Plus" signal, never as a general accent

## Do
- Keep the canvas near-black with only faint green radial glows; put content in slightly lighter charcoal cards
- Use pill buttons everywhere: solid green + dark text for primary, charcoal ghost for secondary, always paired in heroes
- Show the product via realistic dark dashboard mockups with green data visualizations
- Number section eyebrows and center all H2s; let card grids do the layout work below
- Use tiny rounded tier chips (green/yellow/gray) to encode plan levels on feature cards

## Don't
- Don't introduce blues, purples, or gradients beyond the subtle green glow — the palette is strictly gray + green (+ scoped yellow)
- Don't use drop shadows or heavy borders on cards; separation is fill-contrast only
- Don't use sharp-cornered or small-radius buttons — every button is a full pill
- Don't set headlines in serifs or condensed faces; everything is one geometric sans at modest weights
- Don't let yellow leak outside pricing/tier contexts or it dilutes the "Plus" signal
