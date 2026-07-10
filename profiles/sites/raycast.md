---
name: raycast
kind: site
style: DN
category: developer-tools
website: https://raycast.com
pages: [home, pricing, blog]
palette:
  canvas: "#07070a"
  ink: "#a6a6ad"
  primary: "#e8e8ec"
  accents: ["#ff6363", "#b968ff", "#56c2ff", "#59d499"]
typography:
  display: "Inter (geometric grotesque) · bold-to-extrabold · tight"
  body: "Inter"
radius: "medium 8-10px buttons, large 16px+ cards"
---
## Overview
Near-black canvas with luminous multi-hue gradients doing all the emotional work: headlines and feature cards glow in pink-purple-blue-orange while chrome stays quiet gray. The product (a macOS launcher) is rendered as glassy in-page app windows floating over gradient washes. Everything reads as a premium native-app aesthetic translated to the web: compact, precise, softly lit.

## Layout
Slim centered top nav: logo left, five text links center, Log in + a small filled Download button right; a "New" pill badge tags fresh nav items. Home hero is centered text over a faded, glowing screenshot of the app's command palette, with a gradient-tinted headline and a single CTA below. Sections alternate: one huge full-width gradient panel containing an app screenshot, then a row of 2-3 dark feature cards, then a centered H2 for the next chapter — a steady panel/cards/heading rhythm with generous vertical breathing room. Pricing is a left-aligned title over a spare 4-column comparison table drawn with thin hairline rules, no card boxes. Blog is a single centered column of horizontal post cards, each led by a full-bleed gradient artwork thumbnail. Both secondary pages end with the same centered "Ready for take-off?" download CTA plus a brew-install command in a code pill.

## Components
Buttons: soft-rectangle (8-10px radius) fills in near-white gray with dark text for primary actions ("Download for Mac", "Create Organization", "Subscribe"); the closing CTA gets a rainbow glow halo around its border. Secondary actions are plain text links or hairline-bordered ghosts. Cards: very dark panels (#121218-ish) with large 16px+ radii, no visible border, no drop shadow — separation comes from a slight lightness step over the black canvas; hero feature panels instead use full saturated gradient fills (magenta-to-purple, blue-to-cyan). Small square app-style icon tiles (rounded, colored fills) mark feature bullets and pricing rows. Inputs: dark filled field with subtle border and light placeholder, paired with a gray filled button. FAQ rows are hairline-divided accordions with chevrons. Checkmarks and em-dashes fill the pricing matrix; plan tiers carry tiny outlined pill badges ("Basic", "Paid").

## Signature
- Rainbow-gradient glow treatments: gradient-tinted headline words, gradient panel backdrops, and a literal multicolor halo around the final CTA button on pure black.
- The product UI itself as hero art — floating command-palette windows with glassy translucency embedded in gradient scenes.
- macOS-native vocabulary on the web: app-icon tiles, keyboard-shortcut chips, a brew install one-liner in a code pill.
- Neutral, almost colorless chrome (white/gray buttons, gray body text) so the neon gradients own every accent moment.

## Do / Don't
Do:
- Keep the canvas near-black and let color enter only through large gradient panels, artwork, and tinted headline words.
- Use near-white filled buttons with dark text as the primary CTA; reserve the rainbow glow for one climactic button per page.
- Separate cards from the background with a small lightness step and large radii instead of borders or shadows.
- Punctuate features with small rounded app-icon tiles in varied saturated colors.
- Hold section content to a narrow centered measure with big vertical gaps between chapters.

Don't:
- Don't use a saturated brand color as the button fill — the red logo mark never becomes a CTA color here.
- Don't box the pricing table into cards; it lives on hairline rules directly on the canvas.
- Don't add drop shadows or heavy borders to dark cards; the palette's glow does the depth work.
- Don't tint body copy — it stays neutral gray even when sitting next to full-spectrum gradients.
- Don't mix typefaces; the whole site runs on one grotesque at different weights and sizes.
