---
name: tryeraser
kind: site
style: ML
category: dev-tools
website: https://www.tryeraser.com/
pages: [home]
palette:
  canvas: "#FAFAFA"
  ink: "#090A13"
  primary: "#05060F"
  accents: ["#E8053B", "#0085FE", "#EC58AE", "#EF9D4E", "#CF76F8"]
typography:
  display: "editorial transitional serif (Tiempos/Freight-like) · regular weight, no bolding · tight, slightly condensed"
  body: "Inter-like grotesque sans, small sizes, mid-gray"
radius: "small 2-6px on buttons; medium 8-14px on product-screenshot cards"
---
## Overview
A near-monochrome, paper-quiet landing page: warm-white #FAFAFA canvas, ink-black serif headlines, and tiny gray sans body copy. Color is rationed to the two-shape red/blue logo and small candy-toned annotation chips (pink, orange, purple) that live inside product screenshots, mimicking the whiteboard tool itself. Large floating app screenshots with soft shadows do most of the storytelling; the chrome around them stays almost invisible.

## Layout
Slim top nav: centered-left text links in small sans, logo mark centered above the hero headline zone, "Sign In" far right — all on the bare canvas, no nav bar fill or border. Hero is fully centered: serif headline in two short lines, a single small outlined CTA, then a huge edge-to-edge product screenshot. Section rhythm alternates centered serif headlines ("Trusted by...", "A diagram is worth one-thousand words", "Get more done together") with left/right asymmetric feature blocks: a serif heading on one side, a screenshot card on the other, flanked by a vertical list of feature labels where the active item is dark and underlined and inactive items fade to light gray (tab-like progressive disclosure). Faint hairline guides and hand-drawn connector arrows float in the whitespace. Logo wall is desaturated gray. Testimonials sit in a 4-column masonry-ish grid of white cards. Generous vertical whitespace throughout; content column stays narrow (~55-60% width).

## Components
Buttons: compact rectangles with 2-4px radius; default is white fill + 1px near-black border + small sans label ("Try Eraser"), inverted near-black #05060F fill with white text for the emphasized mid-page CTA; footer CTA is white with an arrow glyph. Cards: white testimonial cards with hairline gray borders, small radius, avatar + name + Twitter/ProductHunt icon, no shadow; product screenshots are the heavy cards — medium radius, realistic app chrome, soft diffuse drop shadows. Feature-list "tabs": plain text items with underline on the active state, opacity fade on inactive. Small colored tag chips (pink/orange) with tiny white labels appear only inside product imagery. No visible form inputs on the page.

## Signature
- Serif display type for every headline on an otherwise utilitarian dev-tool page — an editorial voice over engineering content.
- One decorated word: "Keyboard first design" set with parts of the word as teal-outlined hollow letterforms next to filled black ones.
- Hand-drawn squiggly connector arrows and faint hairline frames scattered in the whitespace, echoing the whiteboard product.
- Color discipline: page is gray/black/white; saturated color (logo red #E8053B / blue #0085FE, chip pink/orange/purple) appears only in the logo and inside screenshots.

## Do / Don't
Do:
- Keep the canvas a single flat #FAFAFA end to end; let screenshots and whitespace create the sections, not background color bands.
- Set all headlines in the serif at modest sizes with tight leading; keep body text small, gray, and max ~40ch wide.
- Use outlined white buttons by default and reserve the solid near-black fill for one or two emphasis CTAs.
- Alternate left/right screenshot-plus-feature-list blocks, with inactive list items faded and the active one underlined.
- Add product color through the artifacts themselves (screenshots, chips, code-syntax colors), plus small hand-drawn arrows as decoration.

Don't:
- Don't introduce a brand-color filled CTA (no red or blue buttons) — the logo colors never touch the UI chrome.
- Don't use bold or oversized display type; the serif stays at regular weight and restrained scale.
- Don't add card shadows to text/testimonial cards — shadows belong only to floating product screenshots.
- Don't tint section backgrounds or add gradients; contrast comes from the one dark code-editor panel (#282F3D) inside a screenshot.
- Don't round buttons into pills; corners stay nearly square (2-6px).
