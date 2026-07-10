---
name: oxide-computer
kind: site
style: DT
category: cloud-infrastructure
website: https://oxide.computer/
pages: [home, product, blog, careers, events]
palette:
  canvas: "#080F11"
  ink: "#A9B2B0"
  primary: "#48D597"
  accents: ["#F5B944", "#BE95EB", "#E86886"]
typography:
  display: "Suisse Intl-style neutral grotesque · light-to-regular weight · normal tracking"
  body: "same neutral grotesque for prose; GT America Mono-style monospace for all labels, nav, badges, and metadata"
radius: "small 2-6px (buttons ~2-3px, cards/rows ~4-6px)"
---
## Overview
Terminal-grade dark UI for server hardware: a near-black green-tinted canvas, hairline 1px borders, and mint-green (#48D597) as the single dominant accent. Every functional element — nav, buttons, badges, section labels, spec values — is set in uppercase monospace, while headings stay in a quiet light-weight grotesque. Product imagery is dark technical renders of racks and sleds with green wireframe/schematic overlays, so the marketing site reads like the product console itself.

## Layout
Sticky slim top nav: green monospace logo left, uppercase monospace dropdown links center, two small CTAs right (outlined "CONTACT US", green-filled "TRY IT NOW"). Heroes are compact and centered — a pixel-style green icon tile, one large light-weight heading, one short subline — no oversized hero blocks. Sections alternate between centered headings and two-column splits (text left, UI screenshot or hardware render right). Long pages are divided by full-width 1px horizontal rules; the events page is a literal data table with monospace column headers (NAME / DATE / CATEGORY / LOCATION). Footer repeats the pattern: large muted tagline "Servers as they should be," monospace link columns, newsletter input.

## Components
Buttons: small, uppercase monospace, ~2-3px radius; primary is solid #48D597 with near-black text, secondary is transparent with a 1px gray border. Cards and table rows: transparent or barely-lighter fill (#0E1517-ish) with 1px hairline borders, no shadows anywhere. Badges: monospace uppercase text in a thin colored border/tint — green OXIDE, purple CONFERENCE/VIRTUAL, yellow EXTERNAL. FAQ accordions are stacked bordered rows with a small chevron. Inputs (newsletter) are dark bordered fields with a small green arrow-square submit. Spec tables use alternating hairline-divided rows, label left in sentence case, value right in monospace.

## Signature
- Uppercase monospace as the system voice: nav, buttons, badges, table headers, timestamps, spec values — sans-serif is reserved for headings and prose only.
- Single mint green #48D597 doing nearly all accent work on a green-black canvas, with yellow/purple appearing only as semantic badge colors.
- Hairline 1px borders instead of shadows or fills; zero elevation, everything flat.
- Schematic/wireframe green line diagrams and pixel-grid icon tiles that echo hardware engineering drawings.

## Do / Don't
**Do**
- Set every UI label, button, badge, and data value in uppercase monospace with wide tracking; keep headings light-weight grotesque in sentence case.
- Use #48D597 sparingly but exclusively: filled primary CTA, logo, links, icons, chart lines — one green, everywhere.
- Separate sections with full-width 1px rules and build cards/tables from hairline borders on the dark canvas.
- Show product UI as embedded dark screenshots that match the site palette, and hardware as dark renders with green schematic annotations.
- Keep radii tight (2-6px) and buttons small and dense.

**Don't**
- Don't add drop shadows, glows, or gradient fills — the entire site is flat hairline-on-dark.
- Don't use large bold display type; Oxide headings are light/regular weight and modest in size even in heroes.
- Don't introduce blue or generic SaaS gradients; secondary colors (yellow, purple, pink) appear only as small badges and chart series.
- Don't round buttons into pills or inflate padding — components stay compact and terminal-like.
- Don't use photography outside the careers page; product pages rely on renders, diagrams, and console screenshots.
