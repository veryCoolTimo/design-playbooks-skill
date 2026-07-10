---
name: madewithgsap
kind: site
style: DN
category: dev-resources
website: https://madewithgsap.com/
pages: [home, collection, faq, pricing]
palette:
  canvas: "#0D0D0D"
  ink: "#F2F0EA"
  primary: "#CDF546"
  accents: ["#F2542D", "#F5B821", "#8FE0B4"]
typography:
  display: "Helvetica Now / Neue Haas Grotesk style neo-grotesque · medium weight · tight, near-default tracking with custom ligatures (crossed 'th' in the wordmark)"
  body: "Same neo-grotesque for prose; uppercase monospace (JetBrains Mono feel) for labels, buttons, and metadata"
radius: "small 2-6px on buttons; medium 8-14px on large cards and FAQ rows"
---
## Overview
A near-black, editorial-brutalist showcase where a single neon-lime accent does all the color work at the chrome level, while the demo content itself supplies bursts of orange, yellow, red, and mint. Massive neo-grotesque headlines sit against tiny uppercase monospace metadata, creating an extreme type-scale contrast. The mood is "print poster meets code editor": playful in content, disciplined in structure.

## Layout
Sticky-feeling top nav: wordmark left, three center links (Collection with superscript count, Pricing, FAQ), Sign In plus a lime pill-adjacent CTA right. Home opens light-on-cream with a fanned deck of colorful effect cards, then inverts to the black canvas for the rest of the page — sections are separated by a scalloped (half-circle) edge divider rather than straight seams. Long numbered sections (1 Effects, 2 Learning, 3 Our goal) use a two-column split: index + label left, right-aligned paragraph and media right. Collection page is a dense 3-column masonry of dark demo tiles, each with its own mono metadata header and PLAY chip. Recurring marquee band ("Get ready to animate ✛ Get ready to animate") with lime plus-sign separators precedes the footer. Footer: newsletter field left, three mono link columns right, and a giant full-bleed wordmark bleeding off the bottom edge.

## Components
- Primary CTA: neon-lime (#CDF546) rectangle with black uppercase monospace label and a "↳" return-arrow prefix, small 2-4px radius, no shadow.
- Secondary buttons: solid off-white rectangles or 1px-outlined dark rectangles, same mono uppercase treatment ("LICENSING PAGE", "FAQ PAGE").
- FAQ items: full-width rows with 1px low-contrast borders, ~8px radius, mono uppercase question text prefixed by "↳".
- Pricing card: single dark panel with hairline border, mono "UNIQUE PRICE" tag chip, oversized grotesque "85€", stacked mono feature list, lime CTA.
- Feature mini-cards: black tiles with lime pixel-glyph icons, lime title bar text, tiny justified body copy.
- Newsletter input: borderless field with bottom hairline, placeholder in grotesque, mono "↳ SUBMIT" affordance.

## Signature
- One neon: lime #CDF546 reserved for CTAs, plus-sign glyphs, and icon accents — nothing else in the chrome is colored.
- Dual type system: huge tight neo-grotesque display (often 100px+) against 10-12px uppercase monospace labels with wide tracking.
- "↳" arrow prefix on nearly every interactive element (buttons, FAQ rows, submit links).
- Scalloped half-circle section dividers between cream and black bands, and a footer wordmark so large it crops off the viewport.
- Fanned/stacked colorful effect cards (orange, red, yellow, mint) as the hero object on an otherwise monochrome stage.

## Do / Don't
**Do**
- Keep the canvas near-black (#0D0D0D) and let colorful demo thumbnails be the only saturated areas besides the lime CTA.
- Prefix CTAs and list rows with the "↳" glyph and set all button/label text in uppercase monospace.
- Use extreme scale jumps: 6-10x between display headlines and their mono eyebrow labels.
- Separate major sections with the scalloped-edge divider or a marquee strip instead of plain padding.
- Right-align long body paragraphs against left-anchored numbered section labels in the two-column editorial layout.

**Don't**
- Don't introduce a second accent color in UI chrome — orange/yellow/red belong only inside content cards.
- Don't round buttons past ~6px or use pills; shapes stay rectangular and flat with zero drop shadows.
- Don't use serif or handwritten faces anywhere; the system is strictly grotesque + monospace.
- Don't put the lime fill on anything that isn't a primary action — secondary actions are white or outlined.
- Don't center body copy in editorial sections; centering is reserved for short display statements and the pricing intro.
