---
name: portalgaming
kind: site
style: GR
category: web3-gaming-platform
website: https://portalgaming.com/
pages: [home, build, ecosystem]
palette:
  canvas: "#FFFFFF"
  ink: "#111111"
  primary: "#0A0A0A"
  accents: ["#A793F6", "#EE6352", "#5B4FD8", "#8FB4C4", "#F4F4F2"]
typography:
  display: "Neue Haas Grotesk / Helvetica Now style neo-grotesque · medium weight · tight, near-neutral tracking"
  body: "Same neo-grotesque, regular weight; uppercase monospace for eyebrow labels and footer links"
radius: "pill buttons; large 16px+ cards (roughly 20-24px)"
---
## Overview
A bright, near-white canvas that saves color for illustration: soft lavender gradient meshes, glassy 3D hexagons, and rainbow ribbon streams sit inside large rounded cards while all chrome (nav, buttons, text) stays strictly black on white. Headings are plain sentence-case grotesque at generous sizes; tiny uppercase monospace labels give it a technical, spec-sheet undertone. The result reads as a calm Swiss layout hosting vivid Web3 artwork.

## Layout
Sticky-top slim nav: logo left, a white pill segmented control for Solutions/Build/Ecosystem in the center-left, and two black pill CTAs ("Launch App", "Start Building") on the right. Heroes come in two flavors: a full-bleed lavender gradient-mesh banner with centered headline (home), or a split pair of rounded cards — gray text card left, illustration card right (build, ecosystem). Section rhythm alternates white and #F4F4F2 gray bands; big centered statement paragraphs (2-4 lines of large grotesque) act as dividers between feature blocks. Two-column pattern repeats: narrow left column with heading + small body + pill buttons, wide right card with illustration. Bento grids appear mid-page (2x2 mixed-size cards) and every page ends with the same "$PORTAL is your key" block: one large violet card plus a 2x2 grid of small gray product cards, then a mono-labeled 4-column footer.

## Components
Buttons: solid black pills with white text and a small circled arrow-northeast icon at the right end; inverse white-on-dark pills appear over colored cards. No visible outline or ghost variants — everything is the same pill with arrow. Cards: large-radius (20px+) flat fills — light gray #F4F4F2, white with hairline border, or saturated violet/coral — no drop shadows anywhere. Product identity chips are 3D beveled hexagons (gradient steel-blue Hub, coral Pay, violet Wallet). Logo/partner cards: small gray tiles with a circular logo mark, mono name label top-left, and a tiny "Visit" pill bottom-left. Eyebrow labels ("PORTAL HYPERWAY", "DISTRIBUTION", "LIQUIDITY") are small uppercase monospace in muted gray. No inputs seen.

## Signature
- Black pill buttons ending in a circled diagonal-arrow glyph, identical across nav, heroes, and cards
- Glassy 3D hexagon product badges (Hub / Pay / Wallet) and rainbow ribbon "liquidity streams" fanning across white cards
- Soft lavender gradient-mesh fields (#C9BDF8 to white) used for hero banners and the big violet $PORTAL card
- Uppercase monospace micro-labels over otherwise plain sentence-case grotesque type
- Everything lives inside large rounded rectangles; the page itself stays white and shadowless

## Do / Don't
Do:
- Keep all UI chrome monochrome (black on white) and let color live only inside illustration cards
- Use the pill + circled-arrow button for every CTA, black fill by default, white fill on colored surfaces
- Alternate white and #F4F4F2 section bands and insert large centered statement paragraphs between feature sections
- Pair a narrow text column (heading, small gray body, pill CTAs) with a wide rounded illustration card
- Reuse the mono uppercase eyebrow label pattern for section and card metadata

Don't:
- Add drop shadows, borders heavier than a hairline, or glassmorphism to cards — fills are flat
- Set headings in uppercase or with heavy tracking; display type stays sentence case and quiet
- Use the violet or coral as button fills or link colors — the CTA color is black
- Introduce sharp corners; nothing on these pages is squarer than ~16px except the page edge
- Crowd sections — each block gets a full band of whitespace and one idea
