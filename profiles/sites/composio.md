---
name: composio
kind: site
style: DT
category: developer-tools
website: null
pages: [home]
palette:
  canvas: "#0f0f0f"
  ink: "#a8a8a8"
  primary: "#0007cd"
  accents: ["#1a26ff", "#00d4ff", "#7b3aed", "#33d17a", "#ff4d4d"]
typography:
  display: "abcDiatype (Inter substitute) · medium 500 · tight negative tracking (-2px at hero scale)"
  body: "abcDiatype (Inter substitute), 400; JetBrains Mono for code"
radius: "small-medium: buttons/inputs 8px, cards 12-16px, pill only on tiny badges"
---
## Overview
A monolithic near-black developer-infrastructure look where a single deep electric blue (#0007cd) does all the accent work: main CTAs, wordmark, and radial spotlight glows. One sans family (abcDiatype) at weight 500 handles every heading; body copy is soft gray on #0f0f0f. Depth comes from surfaces stepping up in brightness rather than shadows, and code surfaces sink to pure black.

## Layout
64px dark top nav (wordmark left, product menu center, GitHub stars + sign-in + blue "Get started" right; hamburger under 768px). Hero: centered 72px/500 headline with heavy negative tracking, two CTAs, and the signature 2x2 terminal-mockup grid lit from behind by a blue radial glow. Sections stack on the same #0f0f0f canvas at a 96px cadence inside a ~1200px container; toolkit cards run 4-up desktop down to 1-up mobile; a spotlight CTA band precedes a 5-column footer. Spacing stays fairly tight — the dark canvas supplies the breathing room.

## Components
Primary button: solid #0007cd fill, white 14px/500 label, 40px tall, 8px radius (never a full pill); pressed state darkens to #0005a3. Secondary buttons use a brighter surface (#222222) or a transparent 1px-outline variant at the same geometry. Cards sit on #181818 at 12-16px radius with no drop shadows — elevation is purely a brightness ladder (#0f0f0f -> #000000 recessed -> #181818 -> #222222). Code blocks and the terminal grid use pure-black backgrounds, JetBrains Mono at 13px, panes at 12px radius. Inputs are #181818 fills at 8px radius, 40-44px tall. Tiny uppercase badge pills (11px, +0.88px tracking) are the only pill shapes.

## Signature
- The 2x2 terminal-pane mockup with a central blue radial glow anchoring the hero.
- One scarce accent — deep electric blue #0007cd — reserved for CTAs, wordmark, and glows.
- Shadow-free brightness-step elevation on an unbroken near-black page.
- Single sans (abcDiatype/Inter) at weight 500 for all display sizes with strong negative tracking.

## Do / Don't
Do:
- Keep #0007cd scarce: primary CTAs, wordmark, and spotlight glows only.
- Build elevation by lightening surfaces (#181818, #222222); back heroes with a radial blue glow.
- Hold every CTA at 8px radius, 40px height, 14px/500 label.
- Set all code and CLI content in JetBrains Mono on pure-black blocks.
- Keep display type at weight 500 with tight negative letter-spacing.

Don't:
- Don't promote cyan (#00d4ff) or violet (#7b3aed) beyond illustrations — no second brand color.
- Don't round CTAs into full pills; pill shape belongs only to small badges.
- Don't add drop shadows anywhere.
- Don't use pure black (#000000) outside terminal/code surfaces.
- Don't thin display headings to weight 400.
