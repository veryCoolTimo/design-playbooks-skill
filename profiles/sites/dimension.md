---
name: dimension
kind: site
style: DT
category: developer-tools
website: https://www.dimension.dev/
pages: [home, about, blog, careers]
palette:
  canvas: "#0d0d21"
  ink: "#9a9ab0"
  primary: "#f97ba4"
  accents: ["#a78bfa", "#fbbf77", "#e879f9"]
typography:
  display: "Inter-like geometric grotesque · semibold-bold · tight"
  body: "Inter-like grotesque"
radius: "small 2-6px buttons/badges · medium 8-14px cards"
---
## Overview
A near-black indigo canvas washed with faint purple ambient glows, where nearly everything is dim gray except gradient highlights that sweep pink-to-orange-to-violet across key words, CTAs, and the app icon. The look is quiet, dense, and product-forward: real app UI screenshots float inside glowing frames while text stays low-contrast and small. Feels like a Linear-era developer tool with an Instagram-gradient personality injected sparingly.

## Layout
Fixed top nav: logo left, centered pill-shaped link group (About, Careers with count badge, Blog, Changelog), single "Join waitlist" button right. Heroes are centered: gradient-highlighted headline, one-line subhead, then a large product screenshot bleeding into darkness. Sections alternate a centered mini app-icon + short gradient-accented heading, followed by 2-3 column feature/bento cards; content pages (About, Careers) run a narrower left-aligned single column with faint hairline rules framing headings. Every page ends with the same CTA finale: glowing app icon over a dotted-particle horizon arc, "Ready to join a new Dimension?" headline, single gradient button, then a 4-column footer.

## Components
Buttons: small, compact padding, slightly rounded (~6px); primary CTA is a pink-to-orange gradient fill with a soft matching outer glow; secondary is dark translucent with a 1px light border. Cards: dark translucent panels barely lighter than the canvas, 1px low-opacity white borders, ~10-12px radius, no drop shadows — separation comes from borders and inner glows. Badges/tags (Announcement, Changelog, careers counts) are small pill outlines. Investor/team rows are two-column list cards with square-rounded photo thumbnails. Blog cards lead with a gradient artwork panel above meta rows.

## Signature
- Pink→orange→violet gradient applied to single words inside otherwise plain headlines ("Dimension?", "together.", "Private Beta")
- Glowing squircle app icon used as a recurring section marker and as the centerpiece of the closing CTA over a particle-dotted arc
- Extremely low-contrast surfaces: cards read as faint outlines on near-black indigo, no visible shadows
- Centered pill nav bar with count badges and one small gradient CTA button

## Do / Don't
Do:
- Keep the canvas near-black indigo (#0d0d21-ish) with subtle purple radial glows behind heroes and CTAs
- Reserve the pink-orange-violet gradient for one or two words per headline and the primary button only
- Build cards from 1px translucent white borders on slightly lighter dark fills; let borders, not shadows, define edges
- Repeat the app icon as a section-opener motif and close every page with the same gradient-CTA finale
- Keep body text small, muted gray, and generously line-spaced

Don't:
- Use flat solid brand colors for CTAs — the primary button is always a gradient with glow
- Add drop shadows or elevated white surfaces; nothing on this site is lighter than a faint translucent panel
- Left-align the nav links or make the header tall — it is a slim bar with a centered pill group
- Apply the gradient to whole paragraphs or large areas; it never exceeds a few words or a button
- Use large border radii or pill-shaped buttons; corners stay tight (4-6px buttons, ~12px cards)
