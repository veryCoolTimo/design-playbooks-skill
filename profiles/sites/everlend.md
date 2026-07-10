---
name: everlend
kind: site
style: DT
category: defi-lending
website: https://everlend.finance/
pages: [home]
palette:
  canvas: "#030507"
  ink: "#B4B6B8"
  primary: "#1CD272"
  accents: ["#7CF0B4", "#161A1E", "#0E9F52"]
typography:
  display: "geometric grotesque (Aeonik/Graphik feel) · medium-semibold · tight, near-zero tracking"
  body: "same grotesque family, regular weight; monospace used for bracketed technical labels"
radius: "pill buttons · medium 12-16px cards"
---
## Overview
Near-black dark-tech landing with a single neon-green signal color doing all the work: CTA fills, glowing wireframe isometric graphics, timeline markers, and monospace annotations. Everything else sits in a narrow band of charcoal grays (#14181D-#1A1F24) so the green reads as energy against a void. The tone is engineered and quiet rather than loud crypto-maximalist.

## Layout
Slim top nav: small logo left, three centered text links, pill "Launch App" button right. Hero is a left-right split — glowing 3D isometric stack of layered plates on the left, heading + paragraph + dual CTAs on the right. Sections alternate: big left-aligned two-line headings ("Our community / is worldwide.") paired with content on the right, then full-width dark panels. A vertical green-line roadmap timeline with dot markers runs down the page. Generous vertical whitespace between sections; content sits in a centered ~1200px column.

## Components
- Primary button: solid green (#1CD272) pill with dark text and a trailing arrow; secondary button: dark charcoal pill (#14181D) with white text and a small icon.
- Stat cards: charcoal (#161A1E) rounded rectangles with a circular icon chip left, large white number, gray caption, and a diagonal-arrow glyph bottom-right.
- Feature/blog cards: same charcoal fill, ~14px radius, image or icon on top, white title, gray body — no visible borders, no drop shadows; separation comes purely from the slightly lighter fill.
- Product screenshot framed in a green-glow outline card, tilted slightly for depth.

## Signature
- One neon green (#1CD272) against true near-black; no second brand hue anywhere in the UI chrome.
- Glowing wireframe/isometric 3D graphics (layered hex plates, radar arcs) with green edge light.
- Monospace green bracketed labels — "[END OF FEBRUARY]", "(The highest APY on your deposit)" — as a code-flavored annotation layer.
- Vertical roadmap timeline: thin green rule, dot nodes, date tags in mono caps.

## Do / Don't
Do:
- Keep the background near-black (#030507) and build surfaces from barely-lighter charcoals — contrast between layers stays subtle.
- Reserve solid green fills for the primary CTA and small markers; use green as glow/edge-light on illustrations elsewhere.
- Pair pill buttons with medium-radius (12-16px) borderless cards.
- Use monospace bracketed captions in green for dates, parameters, and technical asides.
- Left-align section headings and break them over two short lines.

Don't:
- Don't add borders or drop shadows to cards — flat fill differences carry the hierarchy here.
- Don't introduce a second accent hue for UI; the multicolor dots exist only inside the product-dashboard data, not in page chrome.
- Don't use pure white body copy — body text sits at muted gray (#B4B6B8); white is reserved for headings and big numbers.
- Don't use sharp-cornered or small-radius buttons; every button on the page is a full pill.
- Don't brighten the canvas toward navy or gray-blue — the palette depends on a true-black void.
