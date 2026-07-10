---
name: prototyper-for-figma
kind: site
style: DT
category: design-tools
website: https://prototyper.design/
pages: [home]
palette:
  canvas: "#383838"
  ink: "#9B9B9B"
  primary: "#0A8DE7"
  accents: ["#39425F", "#6B79A3", "#7B4DFF", "#2C2C2C"]
typography:
  display: "Geometric grotesque (Inter/SF-like) · bold · normal tracking"
  body: "Same grotesque family · regular · muted gray"
radius: "pill buttons; large 16px+ cards"
---
## Overview
A dark charcoal plugin landing page that borrows Figma's own visual grammar: soft dark-gray canvas (not black), bright Figma-blue pill CTAs, and app-window mockups with syntax-highlighted code as the hero imagery. Sections alternate between two shades of charcoal, then break into a single slate-indigo pricing block for contrast. Everything is centered, compact, and calm — the color lives in the product screenshots, not the chrome.

## Layout
Slim top nav: small logo left ("Prototyper for Figma"), four plain text links right (Features, Pricing, Install, Docs) — no nav CTA button. Every section is center-aligned: emoji/icon + bold heading, one or two lines of muted subtext, then a large media card. Section rhythm alternates background shades (#383838 / #2C2C2C) and drops one saturated slate-blue (#39425F) band for pricing. Content column is narrow (~640px media cards) with generous vertical padding. Social proof appears twice: like/install stat pills under the hero, and a 2x2 grid of Twitter-style testimonial cards near the end. Page closes with a mirrored hero CTA and a minimal one-row footer.

## Components
- Buttons: pill-shaped, Figma blue (#0A8DE7) fill with white label and small leading icon; secondary actions are plain text links. Pricing card uses a darker slate pill ("Buy now") plus outlined pill ("Get a quote").
- Toggle pills: white pill for the active state, ghost/outlined gray pills for inactive tabs (Draggable/Reactions/Keypad, Simple/Complex) — used as section content switchers.
- Media cards: large-radius (16-20px) faux app windows with traffic-light dots, dark code panels with colorful syntax highlighting; one gets a vivid purple-to-blue gradient border/glow.
- Pricing cards: nested rounded cards in lightened slate (#6B79A3-ish) on the indigo band; strikethrough old price, checkmark feature lists, small "Save 20%" chip.
- Testimonials: rounded dark-gray cards styled as tweets — avatar, name/role, body text with blue inline links, faded reply/retweet/like icons.
- Stat chips: small dark pills with emoji (heart + likes, arrow + installs).

## Signature
- Figma-native feel: the exact Figma blue on pill CTAs, plugin-window mockups, "Works with Figma" credit line.
- Warm dark-gray canvas (#383838) instead of near-black, with subtle two-tone section banding.
- Emoji/glyph prefixes on every section heading (code brackets, lightning bolt, tag, bird).
- One deliberate color break: the slate-indigo pricing section amid an otherwise monochrome page.
- Interactive-feeling white/ghost pill toggles that switch the demo content.

## Do / Don't
Do:
- Keep the canvas a soft charcoal (#383838) and reserve saturation for CTAs, code syntax colors, and one accent section.
- Center every section: icon + bold white heading, 1-2 lines of #9B9B9B subtext, then a large rounded media card.
- Use pill-shaped buttons everywhere, with the Figma blue fill only on the main "Try for free" CTA.
- Present the product as realistic app windows with syntax-highlighted code panels; a gradient glow border is allowed on one showcase.
- Style social proof as native artifacts (tweet cards, like/install stat pills) rather than plain quote blocks.

Don't:
- Don't use pure black backgrounds or high-contrast white sections — the page never leaves dark mode.
- Don't add borders or drop shadows to separate sections; rely on background-shade shifts alone.
- Don't left-align hero copy or widen the content column — everything sits in a narrow centered stack.
- Don't introduce a second brand hue in the chrome; the purple gradient belongs to media frames only, and indigo only to pricing.
- Don't square off corners — no element on the page has sharp or small-radius corners.
