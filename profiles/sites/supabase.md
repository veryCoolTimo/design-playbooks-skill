---
name: supabase
kind: site
style: DT
category: developer-tools
website: https://supabase.com
pages: [home, pricing, blog, product, developers, launch-week]
palette:
  canvas: "#121212"
  ink: "#b4b4b4"
  primary: "#3ecf8e"
  accents: ["#242424", "#3e3e3e", "#ededed", "#006239"]
typography:
  display: "custom geometric grotesque (Circular-like) · medium weight · slightly tight"
  body: "same grotesque family, regular, small sizes (13-15px); monospace (Source Code Pro-like) for labels, prices, and code"
radius: "small 4-6px buttons, medium 8-12px cards"
---
## Overview
Near-black developer aesthetic where a single brand green does all the work: green CTA, green checkmarks, green code-highlight glow, everything else grayscale. Density is high and type is small; the page reads like a well-organized terminal dressed up with soft cards. The launch-week page inverts to white with monospace labels, proving the system works in both polarities.

## Layout
Slim sticky top nav (logo left, Product/Developers dropdowns, GitHub star count, Sign in ghost button, green CTA pill-ish button right); product pages add a second sub-nav row of icon tabs (Database, Auth, Storage...). Hero is centered, two-line headline with the second line in green, short gray subcopy, dual CTA (green primary + dark secondary), then a monochrome logo cloud. Sections alternate feature-card bento grids (3-up and 2-up, cards with faint diagrams inside), split rows pairing prose with live code panels, community/testimonial card grids, and a full-width table on pricing with green check dots per column. Generous vertical padding between sections but tight, dense content inside them. Massive multi-column footer.

## Components
Primary button: solid green (#3ecf8e) fill, dark text, small 4-6px radius, compact height. Secondary: near-black fill with 1px gray border, light text, same radius. Cards: #1c1c1c-#242424 surface, 1px low-contrast border (#2e2e2e-ish), 8-12px radius, no visible shadows; illustrations inside are thin-line gray/green wireframe diagrams. Code panels: darker inset blocks with green/blue syntax highlighting and small tab pills above. Pricing tiers: bordered columns, the popular Pro tier gets a lifted card with badge; feature matrix uses filled green circle-check icons vs dim dashes. Blog index is a plain hairline-divided list with tiny category pills and dates, almost no chrome. Filter/search inputs: dark fill, 1px border, small radius.

## Signature
- One green (#3ecf8e) against a near-black grayscale field; the hero's second headline line set in that green.
- Bento feature cards containing thin-line schematic illustrations (elephant wireframe, globes, node graphs) in gray with green highlights.
- Real code as a design element: syntax-highlighted panels sit beside marketing copy on nearly every page.
- Monospace micro-labels (LAUNCH WEEK 12, MON 12 AUGUST, Custom pricing) used as structural accents on both dark and light pages.

## Do / Don't
Do:
- Keep every surface grayscale and spend green only on CTAs, checkmarks, syntax highlights, and one headline phrase.
- Use 1px low-contrast borders instead of shadows to separate cards from the near-black canvas.
- Pair each feature claim with a concrete artifact: code snippet, table editor screenshot, or wireframe diagram.
- Keep body type small and dense; let large section padding, not large text, create breathing room.
- Use monospace for tiny uppercase labels, dates, and anything numeric or technical.

Don't:
- Don't introduce a second accent hue (blue/purple gradients) on marketing surfaces; third-party logos are the only multicolor allowed.
- Don't use pill or large-radius buttons; corners stay tight and rectangular.
- Don't add glows, heavy drop shadows, or glassmorphism; elevation is flat border-on-dark.
- Don't decorate the blog list; it stays a bare hairline-ruled index with dates right-aligned.
- Don't use pure black or pure white text on dark pages; headings are off-white (#ededed) and body copy is mid-gray.
