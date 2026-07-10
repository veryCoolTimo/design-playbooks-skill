---
name: clickhouse
kind: site
style: DT
category: database
website: null
pages: [home, pricing, events]
palette:
  canvas: "#0a0a0a"
  ink: "#cccccc"
  primary: "#faff69"
  accents: ["#ffffff", "#1a1a1a", "#22c55e", "#3b82f6", "#ef4444"]
typography:
  display: "Inter · bold 700 · tight negative tracking (-1 to -2.5px)"
  body: "Inter (JetBrains Mono for code)"
radius: "small 6-8px buttons/inputs · medium 12px cards"
---
## Overview
A two-color system: near-black canvas with a single electric yellow doing all brand work. White Inter headlines at 700 with aggressively negative tracking give an engineered, precision feel; there is no serif or second typeface for contrast. Cards sit barely lighter than the page (#1a1a1a on #0a0a0a) with hairline borders and zero drop shadows — depth is implied, not rendered. Real SQL code windows and product UI screenshots serve as the imagery in place of illustration.

## Layout
Fixed 64px black top nav: logo left, horizontal menu, "Sign in" text link plus yellow CTA at right; collapses to hamburger under 768px. Hero splits roughly 7/5 — headline stack left, code window or product mockup right. Content maxes at ~1280px on a 12-column grid; feature cards run 3-up on desktop, pricing 3-4-up. Major bands breathe at 96px vertical rhythm with 32px card padding — dense enough to read developer-grade, not marketing-airy. Surface modes alternate band to band (black canvas, dark card cluster, full-yellow CTA band) so no two consecutive sections look the same.

## Components
- Buttons: yellow fill with black label, Inter 14/600, 40px tall, 8px radius; secondary is the same shape in #1a1a1a with white text. Active state darkens the yellow to #e6eb52; disabled goes murky olive (#3a3a1f).
- Cards: 12px radius, #1a1a1a fill, optional 1px #2a2a2a hairline, no shadow. Variants include code windows (JetBrains Mono, syntax colors, internal chrome like line numbers), product mockups, event cards, and pricing tiers — the featured tier simply flips to full yellow.
- Inputs: 40px dark fields, 8px radius, focus signaled by a yellow border.
- Badges are the only pills: dark ones for labels, yellow uppercase ones for "NEW". Tabs use transparent/muted inactive vs. surface-card active.
- Stat callouts: huge (56px/700) yellow numbers set directly on the canvas, no container.

## Signature
- One accent only — electric yellow #faff69 paired with black; rare per-element, generous as full-bleed CTA bands and featured pricing tiers.
- Giant yellow stat numbers ("47k+", "2.8k+") as bare text on black, carrying the credibility beats.
- Actual syntax-highlighted SQL windows as hero and section artifacts instead of abstract graphics.
- Shadowless depth: elevation comes solely from #1a1a1a-on-#0a0a0a tonal steps and hairlines.

## Do / Don't
Do:
- Keep every surface in the black-to-#242424 range or full yellow; nothing in between.
- Set all display type in Inter 700 with negative tracking; build hierarchy through size, not weight steps.
- Put yellow only on primary CTAs, stat numbers, focus borders, and intentional yellow bands.
- Embed real code in dark card windows with mono type and syntax colors — the query is the visual.
- Alternate band treatments (canvas / card grid / yellow band) to create rhythm without decoration.

Don't:
- Add a second brand hue or gradients; green/blue/red exist only as semantic status colors.
- Cast drop shadows — separation is tonal and hairline-based.
- Use pill shapes beyond small badges; buttons stay at 8px, cards at 12px.
- Set headlines lighter than 700 or push weight past it.
- Swap code mockups for illustration, or spill yellow into body text and incidental fills.
