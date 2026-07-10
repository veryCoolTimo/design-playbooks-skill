---
name: airtable
kind: site
style: ML
category: workflow-software
website: null
pages: [home, platform, pricing, articles]
palette:
  canvas: "#ffffff"
  ink: "#333840"
  primary: "#181d26"
  accents: ["#aa2d00", "#0a2e0e", "#f5e9d4", "#fcab79", "#a8d8c4", "#f4d35e", "#1b61c9"]
typography:
  display: "Haas Groot Disp (Neue Haas Grotesk family; Inter Display as substitute) · restrained 400-500, never heavier · zero tracking"
  body: "Haas Grotesk, 14px/400 throughout"
radius: "buttons large 12px; content cards medium 10px; inputs small 6px; pricing CTAs pill (sub-system only)"
---
## Overview
White-page editorial calm with near-black type and huge breathing room, interrupted every few screens by full-bleed color-block cards — dark coral, deep forest green, cream, dark navy — that carry all the brand energy. Headlines are big but light-weight; nothing shouts through boldness. The main CTA is a near-black 12px-rounded button, not blue. The pricing page speaks its own dialect: Inter Display at weight 475 and pill buttons that appear nowhere else.

## Layout
Light 64px top nav (wordmark left, menu center-left, demo link + dark signup button right) that never inverts over dark sections. Hero is pure white space — headline, subhead, button pair, no backdrop of any kind. Bands alternate surface modes down the page (white → coral card → white → cream callout → dark navy CTA → gray CTA strip → footer), each with 96px vertical padding. Content maxes at ~1280px. Demo grids run 3-4 columns with deliberately uneven card heights; a monochrome logo strip sits under the hero.

## Components
Primary button: #181d26 fill, white 16px/500 label, 12px radius, 16x24 padding; darkens to #0d1218 on press; one per viewport. Secondary: white with 1px hairline outline, same shape — stays white even on dark cards. Signature cards (coral #aa2d00, forest #0a2e0e, navy #181d26): 12px radius, 48px padding, white display type, flat — no shadows anywhere; depth comes from color contrast alone. Demo cards on peach/mint/yellow pastels frame product screenshots at 10px radius. Inputs: 44px tall, 6px radius, hairline border, blue #458fff focus ring. Pricing tiers: white cards, 10px radius; featured tier signaled only by a #f8fafc background shift, no badge or border. Links are #1b61c9 with no underline.

## Signature
- Full-bleed dark-coral and forest-green color-block cards punctuating an otherwise all-white long scroll
- Near-black primary CTA paired with a white hairline-outlined secondary — the recurring button duo
- Display type at weight 400-500 only; emphasis via size and surface color, never boldness
- A self-contained pricing dialect: Inter Display at weight 475 plus pill buttons, unique to that page

## Do
- Keep the primary button near-black (#181d26); the blue #1b61c9 is strictly for links despite its CSS variable name
- Leave heroes as bare white space — type and buttons only, no gradients or mesh
- Alternate band surfaces so no two consecutive sections share the same mode
- Vary demo-card heights within a grid to avoid a spec-sheet look
- Hold 96px vertical padding on every major band

## Don't
- Don't use blue as the CTA fill or push display weights to 600-700
- Don't use pill radii outside the pricing page — elsewhere buttons are 12px
- Don't add shadows or glows to cards; the system is flat, color-block-first
- Don't invert the nav to dark over signature sections — it stays light everywhere
- Don't invent accents beyond the documented coral/forest/cream/pastel set
