---
name: tesla
kind: site
style: PH
category: automotive
website: null
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#393C41"
  primary: "#3E6AE1"
  accents: ["#171A20", "#5C5E62", "#F4F4F4", "#EEEEEE"]
typography:
  display: "Universal Sans Display · medium (500), never heavier · normal tracking"
  body: "Universal Sans Text"
radius: "small 2-6px (buttons 4px); category cards ~12px"
---
## Overview
A digital showroom built on extreme subtraction: full-screen cinematic car photography carries all the emotion while the interface nearly disappears. The palette is white plus grays plus exactly one blue, reserved for the primary CTA. No shadows, no gradients, no borders — separation comes from whitespace and the hard cut between imagery and clean white surfaces.

## Layout
Chromeless top nav (wordmark left, five 14px category buttons centered, icon trio right) floats transparently over the hero and gains a frosted white background on scroll. Every major section is 100vh — one vehicle, one title, one CTA pair per screen, giving scrolling a gallery-slide cadence. Hero imagery runs edge-to-edge with a carousel (dots plus edge arrows); a mega-dropdown opens as a full-width white panel with a 3-column vehicle grid and a text-link sidebar. A persistent "Ask a Question" chat bar sits pinned to the viewport bottom.

## Components
Buttons: 4px radius, 40px min height, roughly 200px wide, 14px/500 label; primary is solid #3E6AE1 with white text, secondary is white with #393C41 text. All state changes animate via color/border at 0.33s — never scale or translate. Cards are borderless and shadowless: nav-panel vehicle cards are transparent PNGs on white with text links below; homepage category cards are full-bleed photos clipped to ~12px radius with a white label top-left and no overlay gradient. Inputs stay near browser-default: transparent background, #8E8E8E placeholders, minimal borders.

## Signature
- Viewport-height photo sections where the car is the entire composition and UI is a whisper on top
- One chromatic color in the whole system: #3E6AE1, used only on primary action buttons and promo text
- Two font weights total (400/500), most UI text locked at 14px, default letter-spacing, no uppercase
- Zero elevation: layering via frosted-glass opacity and z-index, never box-shadow

## Do / Don't
Do:
- Give each message a full viewport — car photo, model name, subtitle, then a centered pair of CTAs
- Keep #3E6AE1 strictly for the primary button; secondary actions get white fill with graphite text
- Hold every transition at 0.33s color-only easing across nav, buttons, and links
- Use transparent-PNG studio renders on pure white for product grids
- Cap headline size at 40px/500 in the Display cut; run all other text in the Text cut

Don't:
- Add box-shadows, gradients, or borders anywhere — depth belongs to the photography
- Introduce a second accent color, bold (700) weight, or uppercase transforms
- Round buttons past 4px or reach for pill shapes; only large photo cards earn ~12px
- Animate hovers with scale/translate — state feedback is background and border color only
- Stack more than two CTAs on a screen or fill whitespace with extra content
