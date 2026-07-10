---
name: getcoco
kind: site
style: CP
category: smb-finance-saas
website: https://getcoco.com/
pages: [home]
palette:
  canvas: "#F1F1F1"
  ink: "#6B6B6B"
  primary: "#2BC0F0"
  accents: ["#F5333F", "#1DCE7E", "#C93BF2", "#FFD121", "#111111"]
typography:
  display: "geometric grotesque (Circular/Graphik-like) · black/extrabold · tight"
  body: "same geometric grotesque · regular"
radius: "pill buttons; large 16px+ cards"
---
## Overview
A toy-box take on SMB finance: a flat light-gray page carrying huge white rounded cards, each paired with a full-bleed panel in one saturated primary color (magenta, red, green, cyan). Type does almost all the work — massive black headlines with muted gray continuation sentences — while playful confetti shapes and the multicolor CoCo logo supply the personality. Zero gradients, zero photography; everything is flat vector color.

## Layout
Minimal top nav: logo left, two pill ghost buttons plus one cyan pill CTA right — no link list. Page opens with a text-only headline ("What if taking control of your finances could earn you cash…") with the last word in coral red, before any card. Body is a strict vertical stack of full-width rounded cards: text column on the left (bold lead sentence in near-black, rest of sentence in gray, all inside one paragraph), and a color-block visual on the right showing an iPhone mockup or abstract shape composition. One idea per card, generous padding, wide gutters of gray canvas between cards. Closes with a big "Get yours. Join the waitlist." card echoing the hero, then a sparse one-line footer.

## Components
- Buttons: solid pill, cyan #2BC0F0 fill with white bold label ("Get the App", "Join Waitlist"); nav secondary buttons are light-gray pills with dark text. No borders, no visible shadows.
- Cards: white, large radius (~20-24px), effectively shadowless on the gray canvas — separation comes from the value contrast, not elevation. The colored visual panel is a child block sharing the card's rounded corners on its outer edge.
- Phone mockups: white iPhone frames sitting inside flat solid-color panels; UI inside uses the same 5-color accent system (category bars, bingo-card tiles).
- Headline device: two-tone sentences — bold ink phrase, then #9A9A9A/#6B6B6B gray continuation in the same size and weight zone.

## Signature
- One saturated flat color per section panel — magenta, red, green, cyan rotate down the page, never mixed within a panel.
- Logo as a design system: four letter-tiles in red/cyan/yellow/magenta reused as a giant app-icon card near the footer.
- Bold-ink + gray two-tone headlines instead of separate heading/subheading blocks.
- Confetti field of flat geometric shapes (circles, squares, capsules, triangles) in the brand palette as the hero illustration.

## Do / Don't
Do:
- Keep the canvas a flat light gray and let white pill-cornered cards float on it without shadows.
- Assign each section exactly one saturated accent color for its visual panel; cycle the palette down the page.
- Use one heavy geometric grotesque everywhere; make hierarchy with the ink-vs-gray two-tone sentence trick.
- Keep CTAs small cyan pills with short labels — the color blocks carry the loudness, not the buttons.
- Use flat vector shapes and in-palette phone UI mockups as the only imagery.
Don't:
- Add gradients, photography, drop shadows, or outlined buttons — everything on the page is flat fills.
- Cram multiple accent colors into one section panel; the confetti hero is the only place colors mix.
- Build a traditional multi-link navbar or dense footer; nav is three pills, footer is one line.
- Shrink the whitespace — cards rely on wide padding and tall panels to feel playful rather than busy.
- Use a serif or a light-weight display face; the voice is chunky black grotesque with tight tracking.
