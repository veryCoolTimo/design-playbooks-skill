---
name: astro-build
kind: site
style: DT
category: developer-tools
website: https://astro.build/
pages: [home, about, blog, careers, integrations, showcase, themes]
palette:
  canvas: "#17191E"
  ink: "#BFC1C9"
  primary: "#883AEA"
  accents: ["#F041FF", "#4AF2C8", "#FF5D01", "#3245FF"]
typography:
  display: "Obviously-style semi-condensed geometric grotesque · medium weight · normal-to-slightly-wide tracking"
  body: "Inter (neutral grotesque); monospace for eyebrows, labels, and footer headings"
radius: "buttons pill; cards small 4-8px"
---
## Overview
Near-black space-dark canvas lit by soft multicolor "light streak" and aurora-glow artwork — violet, magenta, teal, and amber blooms floating in darkness. Type is quiet and light-on-dark; color arrives almost exclusively through glows, gradient CTAs, and vivid integration/theme icons. Monospace micro-labels ("Belief 01", footer column heads) give it an engineering log feel. The archived home page shows an earlier hybrid: purple starfield hero over a white body; the 2023 pages are fully dark.

## Layout
Slim dark top nav: logo left, 5 text links, social icons (Twitter/Discord/GitHub) right — no nav CTA button. Heroes are centered display headlines over dark texture (faint grid or blurred prism streaks) with a short subline; catalog pages (integrations, themes, blog) drop straight into content. Catalogs use a left sidebar (search input, mono-labeled "Filter" accordions, a "Submit" promo card) beside a 3-column card grid with numbered pill pagination. Marketing pages alternate centered sections with two-column text-plus-glow-artwork rows. Generous vertical padding; dense grids inside sections. Footer: three mono-headed link columns plus social icons, hairline-divided legal row.

## Components
Primary CTAs are pill buttons filled with a violet-to-blue/magenta gradient ("Submit integration", "Join us"); secondary CTA on the careers page is a white pill with dark text. The old home hero pairs a small rounded "Get Started" button with a dark `npm create astro@latest` code pill. Cards are slightly-lighter charcoal panels (#1E2129-ish) with 1px low-contrast borders, 4-8px corners, no visible shadows; integration cards lead with a colorful circular icon plus a download-count badge, theme cards with a screenshot, author avatar, and a small Free/Paid tag. Inputs are dark fields with 1px borders and a search-icon prefix. Belief cards on About use mono numbering ("Belief 01") over gradient-streak illustrations.

## Signature
- Blurred prismatic light streaks and radial aurora glows as the only large-scale imagery on a near-black field
- Obviously-style semi-condensed display face with subtly techy letterforms for every headline
- Monospace eyebrow/label layer (Belief 01, Filter categories, footer headings) against grotesque body text
- Gradient pill CTAs (violet→blue/magenta) as the sole saturated UI chrome; everything else is charcoal + hairlines

## Do / Don't
Do:
- Keep the canvas near-black (#16-18 range) and let color enter only via glow artwork, icons, and gradient CTAs
- Use pill-shaped gradient buttons for primary actions and white pills for secondary ones
- Set eyebrows, filter labels, and footer column heads in monospace at small sizes
- Give cards a barely-lighter fill and a 1px low-contrast border instead of shadows
- Center large hero headlines over faint grid/streak textures with lots of breathing room

Don't:
- Add a CTA button to the nav — Astro's nav is text links plus social icons only
- Use hard-edged or heavily shadowed cards; corners stay small and elevation stays flat
- Render illustrations sharp — signature art is deliberately blurred, glowing, out of focus
- Introduce a single flat brand color; accents are always multicolor (magenta/teal/amber/blue) or gradients
- Set headlines in a plain default sans — the distinctive semi-condensed display face carries the identity
