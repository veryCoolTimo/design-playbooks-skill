---
name: reworkd
kind: site
style: ML
category: ai-infra-saas
website: https://www.reworkd.ai/
pages: [home]
palette:
  canvas: "#ffffff"
  ink: "#1b2028"
  primary: "#406fef"
  accents: ["#ebf2ff", "#8fb0f9", "#1a1c20", "#1f36b7"]
typography:
  display: "Inter-like neo-grotesque · bold-to-heavy · tight tracking"
  body: "Same grotesque family, regular weight, generous line-height"
radius: "medium 8-14px on buttons and pills; large 16px+ on cards, app-window mockups, and banner sections"
---
## Overview
Clean minimal-light SaaS page where near-white space carries almost everything and a single saturated blue does the work of brand, CTA, and data-visual accent. Heavy grotesque headlines get a blue gradient treatment on the key phrase ("data extraction"), and realistic product-UI mockups in browser-window chrome serve as hero art instead of illustration. The page flips to a near-black section for the proof/metrics block, giving one deliberate dark contrast beat before a blue-gradient closing CTA.

## Layout
Slim centered top nav: logo left, four text links center, one white pill "Get started" button right. Hero is fully centered: announcement pill ("Reworkd raises a $1.25M pre-seed") → two-line H1 (dark line over blue-gradient line) → one-sentence subhead → single blue CTA, all sitting on a soft blue-to-white vertical gradient, followed by a large browser-framed product screenshot. Sections alternate: centered social proof (investor avatars + logo strip in a bordered grid), a centered "problem" section with floating question-chip rows, a two-column feature block (text left, product UI right), a 3-up benefits row with small icons, then a 2x3-ish bento grid of feature cards mixing light and dark tiles. Whitespace is generous; content column stays narrow and centered; rhythm is roomy and evenly paced.

## Components
Buttons: solid #406fef fill with subtle top-light gradient and soft drop shadow, ~8-10px radius, bold white label; nav variant is white with hairline border, faint shadow, dark bold label. Pills: light announcement/status pills with hairline borders; status badges in the mockups are tinted pills (blue Active, green Succeeded, red Cancelled). Cards: very light gray (#f7f9fa-ish) fills with hairline borders and 16px+ radius; bento grid mixes light cards with near-black ones; the stats section uses a glowing blue gradient card for the hero metric flanked by metallic 3D numerals. Product mockups sit in macOS-style browser chrome with traffic-light dots and tab bars. Inputs appear only inside mockups: hairline-bordered, small radius, quiet placeholders.

## Signature
- One blue (#406fef) does everything: CTA fill, gradient headline word, chart rings, glowing stat card, closing banner.
- Real-looking product UI in browser-window chrome as the primary imagery — data tables, statuses, and a floating JSON snippet on dark.
- Single dark inversion: a near-black "Rely on Reworkd" metrics section with chrome-metallic 3D numbers (30k, 1M) and one radiant blue stat tile.
- Blue "aurora" gradient banner card as the final CTA, rounded and inset from the page edges.

## Do / Don't
Do:
- Keep the canvas white-to-pale-blue and let one saturated blue carry every emphasis moment.
- Set headlines in a heavy grotesque with tight tracking, and gradient-tint only the key phrase.
- Use browser-chrome product mockups with believable table data (IDs, statuses, dates, file links) as hero and section art.
- Reserve exactly one full-width dark section for metrics/testimonial proof, and make its numbers theatrical (metallic 3D, glowing card).
- Border cards with hairlines and light-gray fills; keep shadows soft and rare.

Don't:
- Don't introduce a second brand hue — greens/reds exist only as tiny status badges inside mockups.
- Don't use outline or ghost styles for the primary CTA; it is always a solid blue rounded button with bold white text.
- Don't fill the page with abstract illustration or stock imagery; imagery is product UI or typographic numerals.
- Don't crowd sections — each block is one idea, centered, with wide vertical breathing room.
- Don't go full-pill on buttons or sharp-cornered on cards; corners stay in the 8-16px+ rounded-rectangle range.
