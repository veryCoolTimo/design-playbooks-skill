---
name: movingparts
kind: site
style: ML
category: developer-tools
website: https://movingparts.io/
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#101010"
  primary: "#2002FF"
  accents: ["#FCFD6F", "#F79EA1", "#DADBF1", "#41CF84", "#A25AFF", "#000000"]
typography:
  display: "Neue Haas Grotesk / Helvetica Now style grotesque · heavy (bold-black) · tight, near-touching"
  body: "same grotesque, regular weight; monospace (Söhne Mono-like) for eyebrows, captions, and testimonial attributions"
radius: "buttons none (sharp rectangles); site cards/panels large 16px+; phone-frame mockups extra-large device curves"
---
## Overview
A Swiss-leaning minimal-light page that sells a SwiftUI component library by showing the components themselves: oversized black phone-frame mockups running polished commerce UIs on electric ultramarine (#2002FF) fills. White canvas with a faint grid, heavy tight-set grotesque headlines, monospace metadata, and full-bleed section blocks that flip between white, pure black, pale lavender, and solid blue. Restraint in the chrome, saturation in the demos.

## Layout
Minimal header: abstract geometric logomark top-left, essentially no nav. Hero is centered — two-line black headline, short subhead, single sharp blue CTA — with product mockups and floating UI chips (keyboard keys, avatars, color wheel) bleeding off both edges over a subtle gray grid. Sections are full-width color slabs in strict alternation (white → black → lavender → black/collage → blue → white → black footer), each following the same lockup: left-aligned heavy headline, paragraph, "Book a demo →" button, then a large demo artifact. Three-column small-caps feature blurbs recur under demos. Annotated diagram section labels live app UI with monospace component-name chips (AggregateRating, ImagePager) connected by thin blue leader lines. Footer: articles grid in 3 columns, then black band with white logomark and mono link lists.

## Components
- Primary CTA: sharp-cornered rectangle, #2002FF fill, white bold label with "→", no border, no shadow; identical at every recurrence.
- Cards/panels: large-radius (~16-24px) rounded panels — dark code editor with toggle switch and syntax-highlighted SwiftUI, lavender rounded rectangles as backdrop shapes.
- Phone mockups: thick black device frames with extreme corner radii, containing fully-rendered app UIs (pill steppers, circular color swatches, square size selectors with 1px black selected border, pill "Add to Cart" buttons).
- Labels/chips: blue rectangles with white monospace text used as component callouts.
- Inputs (in demo): white rounded fields with leading icons and gray placeholder text on dark panels.
- Testimonials: quote-first, no card container, mono small-caps attribution with tiny circular avatar, set on solid blue.

## Signature
- Electric ultramarine #2002FF used everywhere — CTA fill, demo backgrounds, callout chips, full testimonial section — against pure white and pure black.
- Heavy grotesque headlines with very tight letter-spacing ("Supercharge your mobile team"), always 2 lines, sentence case.
- Product-as-hero: real component UIs inside chunky black phone frames replace all illustration and stock imagery.
- Monospace as a second voice for eyebrows, captions, component names, and attributions — a deliberate developer-culture cue.
- Full-bleed color-block sections (yellow/pink/black-texture app-screen collage) giving an editorial, poster-like rhythm.

## Do / Don't
Do:
- Keep exactly one CTA style: sharp blue rectangle, white bold text with arrow, repeated verbatim in every section.
- Alternate full-width section backgrounds (white, #000, #DADBF1, #2002FF) instead of using card containers on a single canvas.
- Set headlines in a heavy grotesque with tight tracking, left-aligned in sections, centered only in the hero.
- Use monospace for all metadata (eyebrows, dates, roles, component names) in small caps or all-caps.
- Let demo artifacts (phone frames, code panels) bleed off the viewport edges and overlap section boundaries.

Don't:
- Round the CTA buttons — sharp corners are the rule; large radii belong to panels and device frames only.
- Add drop shadows, gradients, or borders to buttons and cards; separation comes from flat color contrast.
- Introduce secondary link-style or ghost CTAs — the page uses a single button treatment throughout.
- Use stock photography or decorative illustration; every visual is product UI or packaging inside the demos.
- Mute the blue: #2002FF at full saturation is the identity — pastel or navy substitutes break the look.
