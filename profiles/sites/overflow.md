---
name: overflow
kind: site
style: GR
category: design-tools-saas
website: https://overflow.io/
pages: [home]
palette:
  canvas: "#fafafc"
  ink: "#000000"
  primary: "#000000"
  accents: ["#169afb", "#fdc023", "#6b61f2", "#8788f3", "#fec466"]
typography:
  display: "Inter-like geometric grotesque · medium-to-semibold · neutral, slightly tight tracking"
  body: "Same grotesque family (Inter-like), regular weight, generous line-height"
radius: "buttons medium 8-12px; cards large 16-24px"
---
## Overview
A near-white, airy SaaS landing page whose single dramatic moment is the hero: a soft blue-violet-orange gradient mesh that bleeds off all edges behind white display type. Below the fold the page snaps back to disciplined monochrome — black text on #fafafc — and lets product screenshots and small saturated accents (sky blue, amber, indigo) carry all the color. Buttons are pure black, giving CTAs unambiguous weight against the pale canvas.

## Layout
Sticky-style top nav on the page background (no bar fill): logo left, center link row with two dropdowns, Sign In plus a black pill-ish CTA right. Hero is center-aligned: two-line display headline, two-line subhead, primary black CTA paired with a light gray secondary button, then a huge browser-chrome screenshot overlapping the gradient mesh. Section rhythm alternates: (1) two-column feature blocks — text column with heading, paragraph, black CTA beside a large product mock; (2) a centered heading with a stacked list of screenshot cards, each framed by a thick colored rounded border (blue, yellow, indigo) with a text-and-testimonial column at right; (3) 3-column card grids for feature summaries; (4) one full-width #f2f2f4 gray band to break the white. Whitespace is very generous; content sits in a wide centered container.

## Components
Primary buttons: solid black, white label with a small right-arrow glyph, ~10px corner radius. Secondary button: light gray (#f0eff2) fill, black label, same radius, no border. Feature cards: #f5f5f7-ish tiles with large radius (16-24px), no visible border or shadow, containing small illustrative UI vignettes. Screenshot showcases: white browser/mac chrome (traffic-light dots) inside thick colored rounded frames. Testimonial: circular grayscale or color avatar, bold quote, name and title in gray. Logo strip of client marks (Amazon, Netflix, Spotify, Microsoft, Facebook, Yahoo) in black monochrome. Footer: white, multi-column link lists, dark rounded newsletter card at right.

## Signature
- One-scene gradient mesh: blue → violet → orange aurora confined to the hero (and echoed in small blobs later); the rest of the page is monochrome.
- Thick colored rounded frames (sky blue #169afb, amber #fdc023, indigo #6b61f2) wrapping product screenshots like oversized borders.
- All-black CTA buttons with trailing arrow, repeated identically in nav, hero, and every section.
- Playful inline highlight: a blue cursor-flag "wow" chip inside a headline, mimicking the product's own annotation UI.

## Do / Don't
Do:
- Reserve the gradient mesh for the hero backdrop and let white display type sit directly on it.
- Use solid black buttons with an arrow glyph as the only high-emphasis element on white sections.
- Frame product screenshots in thick single-color rounded borders, rotating through blue, yellow, and indigo per card.
- Keep sections on #fafafc and insert at most one #f2f2f4 gray band for rhythm.
- Use one saturated accent per component (a blue bar, a yellow frame), never mixed within it.

Don't:
- Don't run gradients behind body copy or mid-page sections; color below the hero lives only in accents and screenshots.
- Don't add borders or drop shadows to feature cards — flat light-gray fills with big radii only.
- Don't introduce a colored (blue/purple) CTA; primary actions are black here, and links stay plain text.
- Don't tint the near-black text; ink is true black with #646464 for secondary copy.
- Don't crowd sections — every block gets a full screen's worth of whitespace and a single focal screenshot.
