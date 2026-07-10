---
name: beeper
kind: site
style: DN
category: messaging-saas
website: https://www.beeper.com/
pages: [home]
palette:
  canvas: "#000000"
  ink: "#f5f5f7"
  primary: "#8748e1"
  accents: ["#e0559b", "#1273e6", "#8c30c3", "#25262e"]
typography:
  display: "Inter-like neo-grotesque · bold 700 · normal, slightly tight"
  body: "Inter-like neo-grotesque, regular"
radius: "buttons medium 8-12px; cards large 16-20px"
---
## Overview
Dark-neon consumer-software landing: a glowing magenta-to-violet hero haze over pure black, floating 3D chat-network app icons, and a centered iOS-style product mockup. Below the hero the page alternates between pure black and charcoal (#25262e) bands, with occasional white cards for contrast. Feels like an Apple-keynote-meets-Discord aesthetic — playful icon clutter up top, sober product storytelling below.

## Layout
Minimal top nav: logo left, only "Jobs" link plus one small "Get started →" button right. Hero is fully centered: two-line white headline, translucent CTA, then a tall phone mockup overlapping into the next black section. Section rhythm alternates black / charcoal full-bleed bands. Mid-page uses a large gradient feature card (purple-to-mauve) with a checklist and product screenshot; then a centered icon grid of 15+ chat-network logos; then a two-column masonry of feature cards mixing white, black, and one saturated iMessage-blue card. Final CTA section repeats the hero formula (logo + "Get Beeper" + gradient button) above large desktop/mobile screenshots bleeding off the bottom. Generous vertical whitespace, narrow centered text column (~600px) for prose.

## Components
- Buttons: rounded-rectangle (~10px, not pill), bold white label with trailing → arrow. Hero/nav version is frosted translucent white over the purple glow; the bottom CTA is a hard magenta→indigo gradient fill (#a13ee6 → #5b55e9). No visible borders or shadows.
- Cards: large-radius (16-20px) rounded rectangles, flat fills — white cards with dark ink, black cards with white ink, one solid #1273e6 blue card, one big purple-gradient "Chat Superpowers" panel. Colored headline per card (pink/magenta, blue, purple), no borders, no drop shadows.
- Product mockups: white app-UI screenshots with rounded corners, used as hero and section imagery.
- Icons: glossy 3D-rendered brand icons (WhatsApp, Instagram, Slack…) scattered with rotation in the hero; flat rounded-square brand tiles in the network grid.

## Signature
- Magenta/violet radial glow rising from black behind a centered phone mockup, ringed by floating tilted 3D chat-app icons.
- Pink→purple gradient text on section headings ("We're building the best chat app on Earth") against pure black.
- Masonry of flat feature cards that swap fill colors (white / black / brand blue) instead of using borders or shadows.
- Repeated "Get started →" arrow-button motif, translucent in the hero, gradient-filled at the footer CTA.

## Do / Don't
Do:
- Keep the canvas true black and reserve color for the hero glow, gradient headings, and card fills.
- Center everything in the hero and final CTA; use a narrow single column for long prose.
- Use brand-colored 3D or rounded-square network icons as decorative proof of integrations.
- Alternate black and #25262e charcoal bands to delimit sections instead of dividers.
- Give every feature card its own colored headline (pink, blue, purple) with neutral body text.

Don't:
- Don't add borders, outlines, or drop shadows to cards or buttons — contrast comes from fill color alone.
- Don't use pill-shaped buttons; corners stay at ~10px with a trailing arrow glyph.
- Don't spread the neon gradient across the whole page — below the hero, sections are flat black/charcoal.
- Don't crowd the nav; it carries only the logo, one link, and one small CTA.
- Don't set headings in a serif or condensed face — everything is one bold grotesque family at different weights.
