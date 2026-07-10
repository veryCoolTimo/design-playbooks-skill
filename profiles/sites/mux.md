---
name: mux
kind: site
style: BT
category: dev-infra
website: https://www.mux.com/
pages: [home, product, pricing, blog, team]
palette:
  canvas: "#E3E2DA"
  ink: "#232323"
  primary: "#232323"
  accents: ["#FB4E0D", "#F553B8", "#2160FD", "#1FA05A", "#FFB200"]
typography:
  display: "techno grotesque with squared, machined letterforms (custom, PP Neue Machina-like) · medium-bold · uppercase, normal-to-tight tracking"
  body: "neutral grotesque (Akkurat/Helvetica-like); monospace for microcopy labels"
radius: "mixed: pill buttons; small 4-12px cards; section blocks sharp 0"
---
## Overview
Industrial-brutalist developer branding on a warm greige canvas: visible hairline grid rules divide every section, uppercase techno-grotesque headlines sit next to monospace micro-labels, and saturated accent blocks (orange, magenta, cobalt, green, amber) punch through an otherwise near-monochrome charcoal-and-greige system. It reads like a spec sheet crossed with a print poster — engineered, loud in bursts, quiet in between.

## Layout
Sticky top nav on charcoal (home) or greige (inner pages) with monospace-uppercase links and a pill CTA at the far right, often accent-filled (orange). Content lives in a centered column with exposed vertical hairlines running the full page height, so every section reads as cells in one continuous grid. Heroes are text-led: giant uppercase headline, short paragraph, one or two pill buttons; some pages flood the whole hero with a solid accent (hot pink on Mux Video). Section rhythm alternates full-bleed bands — greige, charcoal, and occasional solid orange/blue/amber — separated by 1px rules rather than whitespace alone. Logo strips, feature lists, and footers are laid out as bordered table cells. Every page ends with the same oversized charcoal pill CTA ("Start building for free") stretched nearly full-width on an accent band, above a dense multi-column charcoal footer with a monospace "STATUS: GOOD" chip.

## Components
Buttons: full pills throughout — charcoal fill with white label for primary actions, thin 1px outlined pills (transparent or cream fill) for secondary, accent-filled pills (orange, green, blue) for nav signups and highlighted CTAs; labels are small uppercase monospace. Cards: white or cream fills with 1px charcoal borders, small radii (4-12px), no shadows; pricing tiers get a colored top edge (green/amber/orange), feature-category cards are flat solid accent blocks with an icon and arrow. Inputs: pill search field with 1px border and inline magnifier icon; the pricing calculator uses thin slider tracks, bordered number fields, and radio dots with green fill on charcoal. Blog entries are full-width bordered table rows (thumbnail / meta+title / excerpt), not floating cards. Accordions are hairline-divided rows with plus icons. Metadata everywhere is monospace uppercase with dot separators.

## Signature
- Exposed hairline grid: 1px rules columnizing the entire page, footer and logo strips rendered as literal table cells.
- Uppercase machined display face for headlines paired with monospace uppercase micro-labels ("MUX IS TRUSTED BY", "STATUS: GOOD").
- Full-bleed solid accent bands — hot pink hero, orange CTA band, cobalt join band — dropped into a restrained greige/charcoal base.
- The recurring oversized charcoal pill CTA spanning nearly the full content width at page bottom.

## Do / Don't
- Do keep the base palette to warm greige (#E3E2DA) + charcoal (#232323) and deploy the five accents as full-bleed blocks or card fills, one dominant accent per section.
- Do draw real 1px borders and column rules; structure should be visible, not implied by whitespace.
- Do set headlines in uppercase with a squared techno grotesque, and set all metadata, nav links, and button labels in small uppercase monospace.
- Do use pill-shaped buttons everywhere, scaling the final CTA up to banner size on an accent band.
- Don't use drop shadows, gradients, or glassmorphism — every surface here is flat with hard edges.
- Don't soften the layout with large card radii or floating white space; content sits inside the ruled grid.
- Don't render blog/list content as isolated cards; use bordered full-width rows with monospace date/read-time metadata.
- Don't introduce pastel or muted accents — Mux's accents are fully saturated print-ink orange, magenta, cobalt, green, and amber.
- Don't use mixed-case or lightweight hero type; display copy is uppercase, chunky, and mechanical.
