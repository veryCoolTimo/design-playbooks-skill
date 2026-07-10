---
name: cursor
kind: site
style: EL
category: developer-tools
website: null
pages: [home, pricing, features, enterprise, blog]
palette:
  canvas: "#f7f7f4"
  ink: "#26251e"
  primary: "#f54e00"
  accents: ["#dfa88f", "#9fc9a2", "#9fbbe0", "#c0a8dd", "#c08532"]
typography:
  display: "CursorGothic (Inter as substitute) · regular 400, never bold · tight negative tracking (-0.11px to -2.16px)"
  body: "CursorGothic; JetBrains Mono on all code surfaces"
radius: "small-medium (buttons/inputs 8px, cards/IDE panes 12px, pills for badges)"
---
## Overview
A developer-tools site that trades the expected dark-IDE look for a cream editorial page (`#f7f7f4`) with warm near-black text. Headlines stay at weight 400 with negative tracking, so the tone feels like a print magazine rather than a loud tech launch page. One saturated orange (`#f54e00`) does all the CTA work, and a set of five pastel pills color-codes agent-action stages inside product mockups. Roughly half the visible content is monospaced code set in JetBrains Mono.

## Layout
64px top nav on the cream canvas: wordmark left, horizontal menu, sign-in plus orange download CTA right; collapses to a hamburger under 768px. Hero is a full-width 72px headline over body copy and two CTAs, with a centered white IDE-mockup card underneath. Sections repeat on an 80px vertical rhythm inside a ~1200px container over a 12-column grid; feature grids run 3-up (or 2-up for splits), footer is 5 columns. Whitespace is generous between bands while cards inside a band cluster tightly (16-24px gaps).

## Components
- Buttons: 40px tall, 8px radius, 14px/500 labels. Primary is orange with white text (pressed state darkens to `#d04200`); secondary is a white pill with a strong hairline border; the download CTA inverts to ink-on-cream at 44px; tertiary is a plain ink text link.
- Cards (feature, testimonial, pricing, code blocks): white surfaces on the cream floor, 12px radius, 1px `#e6e5e0` hairline, no shadows anywhere. The featured pricing tier flips to an ink background instead of using a colored ribbon.
- IDE mockup card: white shell with edge-to-edge internal panes in `#fafaf7`, code in 13px JetBrains Mono — the only element that reads as "elevated," purely via contrast and hairlines.
- Timeline pills: fully rounded, 11px uppercase 600 with 0.88px tracking; peach/mint/blue/lavender backgrounds with ink text, gold "Done" pill with white text.
- Inputs: white, 8px radius, 44px tall.

## Signature
- Cream canvas with warm ink instead of the dark-mode default every competitor uses.
- Display type at weight 400 with tight negative tracking — an editorial voice, never bold.
- A single orange as the only action color, used sparingly.
- Five pastel agent-stage pills (Thinking/Grepping/Reading/Editing/Done) confined to in-product timeline visuals.

## Do / Don't
Do:
- Keep orange exclusively for primary CTAs and the wordmark; everything else stays neutral.
- Set all headlines at weight 400 with negative letter-spacing.
- Build depth from 1px hairlines and white-on-cream contrast only.
- Use JetBrains Mono on every code surface, from inline snippets to full IDE panes.
- Hold the 80px section cadence and cap content at ~1200px.

Don't:
- Don't add a second action color or drop shadows of any kind.
- Don't push display type to 700+ — the magazine tone collapses.
- Don't swap the cream floor for pure white; white is reserved for card surfaces.
- Don't reuse the timeline pastels as status or system colors outside agent-timeline visuals.
- Don't grab CTA colors from third-party widgets like cookie banners.
