---
name: together.ai
kind: site
style: DT
category: ai-infrastructure
website: null
pages: [home, pricing, research, docs]
palette:
  canvas: "#ffffff"
  ink: "#000000"
  primary: "#000000"
  accents: ["#fc4c02", "#ef2cc1", "#bdbbff", "#c8f6f9", "#010120"]
typography:
  display: "The Future (custom geometric sans; Inter closest) · medium 500, never bold · tight negative tracking (-1.92px at 64px)"
  body: "The Future / Inter, 400-500; uppercase PP Neue Montreal Mono for eyebrows and button labels"
radius: "small 2-6px (4px canonical on buttons and cards; 8px feature tabs; pill only for the chat orb)"
---
## Overview
An AI cloud platform whose pages swing between near-black navy (#010120) hero and research bands and clean white product/pricing bands, with zero mid-tone grays in between. All decoration is carried by one asset: a three-stop orange-magenta-periwinkle gradient ribbon in the hero. The voice comes from a two-font split — a tight custom geometric sans for narrative, and an uppercase mono for every technical label.

## Layout
Sticky nav sits dark over the hero (logo left, centered links, black sign-in pill right) and flips to white on scroll; collapses to a hamburger with full-overlay drawer on mobile. Hero is a 50/50 split: sentence-case 64px headline plus CTA cluster left, gradient-ribbon SVG right. Sections alternate dark/white full-bleed bands with ~80px vertical padding; content caps at ~1280px. Grids run 3-up for research/testimonial/stat cards, 2-up for articles; pricing pages use dense full-width data tables with 12px row rhythm. Every long page ends with a giant faint-gray "together.ai" wordmark stretched edge to edge above the footer.

## Components
Buttons are compact 4px-radius rectangles (never full pills) with uppercase mono labels: black fill with white text for the primary CTA everywhere; mint (#c8f6f9) and plain-white variants only inside heroes; a #313641 ghost fill on dark bands; a hairline-outlined white variant with a slightly tighter 3.25px radius on pricing pages. Cards are flat, 4px-radius, separated by 1px hairline borders (#ebebeb on white, #313641-ish on dark) — no drop shadows except a faint navy-tinted one on the floating circular chat orb. Stat tiles carry pastel mint/periwinkle fills. Inputs are white with hairline borders at 4px radius. Table headers sit on light-gray rails with 11px uppercase mono labels; segmented toggles use a gray rail with white/black pill segments.

## Signature
- One gradient does all decoration: orange → magenta → periwinkle, hero-scale only, never cropped, reordered, or shrunk to an icon.
- Strict two-font contrast: sentence-case display sans for headlines, uppercase mono (positive tracking) for eyebrows, buttons, and table headers — never swapped.
- Hard dark/white band alternation with hairline-bordered flat cards; contrast replaces shadow as the elevation system.
- The oversized stencil-tinted "together.ai" wordmark banner closing every page.

## Do / Don't
**Do**
- Use the black pill as the single primary CTA on every surface — pricing, footer, nav alike.
- Set all eyebrows, button labels, and table headers in uppercase mono with slight positive tracking (JetBrains Mono / Geist Mono 500 as substitutes).
- Keep the three-stop gradient as one large hero ribbon and let it carry all brand color.
- Alternate #010120 and #ffffff bands with 80px section padding; lean on hairline borders for card edges.
- Hold cards and buttons at the 4px radius, weights capped at 500, and negative tracking on display sizes.

**Don't**
- Add a fifth accent or use the gradient legs (orange/magenta) as standalone UI fills.
- Set paragraphs in the mono face or headlines in all caps — each role belongs to exactly one font.
- Put soft shadows on light-surface cards; only the floating chat orb floats.
- Turn CTAs into full pills; the round shape is reserved for the single circular icon button.
- Introduce mid-gray surfaces between the dark navy and white bands — #ebebeb exists only for table headers, rails, and dividers.
