---
name: mintlify
kind: site
style: DT
category: developer-tools
website: https://mintlify.com/
pages: [home, pricing, careers, documentation, customers, lead-form, light-mode-home]
palette:
  canvas: "#0A0A0A"
  ink: "#A1A1AA"
  primary: "#FAFAFA"
  accents: ["#18E299", "#0D9373", "#F4F4F2"]
typography:
  display: "Inter-style neo-grotesque · medium-to-semibold · tight, near-default tracking"
  body: "Inter-style neo-grotesque"
radius: "pill on buttons; medium 8-14px on cards, inputs, and screenshot frames"
---
## Overview
Near-black, low-chroma marketing surface where mint green is rationed to the logo, tiny status dots, and docs-product accents rather than splashed across the page. Depth comes from full-bleed atmospheric imagery — aurora skies, watercolor coastlines, painterly cloudscapes — bleeding through darkness behind product screenshots. The whole site theme-flips cleanly: the light variant swaps #0A0A0A for warm off-white (#FAFAFA/#F4F4F2) while keeping identical layout, pill buttons, and hairline dividers.

## Layout
Floating pill-shaped nav bar (rounded container, subtle contrast against canvas) with logo left, five text links center, then Login / "Get a demo" (outline) / "Sign up" (solid pill) right. Heroes are center-aligned: small kicker label, 2-line headline, one-sentence subhead, two pill CTAs — followed by a large tabbed product screenshot. Long single-column rhythm: logo strip ("Powering experiences"), 3-up feature cards, alternating two-column feature blocks, case-study card grids. Careers and docs use narrow centered columns (~640px) with generous vertical whitespace; values and perks laid out as 2-column lists separated by 1px hairlines instead of boxes. Docs page is a classic 3-pane layout (sidebar / content / on-this-page) with a prominent top search bar.

## Components
Buttons: fully rounded pills, three tiers — solid high-contrast fill (white-on-dark or black-on-light), quiet outline/ghost with 1px border, and a green solid only inside the docs product ("Get Started"). Cards: 8-14px radius, 1px low-contrast borders, essentially shadowless, dark #111-ish fill on dark canvas / white on light; pricing "Popular" tier gets a slightly lighter fill and corner badge. Job listings are full-width bordered rows with chevron affordance. Inputs (request-preview form): white fields, 1px gray border, ~10px radius, leading icons, placeholder-only labels, stacked inside an elevated floating card over a ghosted docs screenshot. Info callouts in docs: pale tinted background with icon and inline links. Status pill "All systems normal" with green dot lives in the footer.

## Signature
- Painterly/atmospheric full-bleed backdrops (aurora, watercolor coastline, clouds) emerging from a near-black canvas behind tilted or framed product screenshots.
- Mint green used homeopathically: logo mark, status dot, docs accents — never as marketing CTA fill.
- Everything-is-a-pill chrome: nav container, buttons, badges — against squared-off, hairline-divided content lists.
- Perfectly mirrored dark/light themes with an explicit sun/moon toggle in the footer.

## Do / Don't
Do:
- Keep the marketing canvas near-black (#0A0A0A) with white pill CTAs; reserve green for the brand mark, status indicators, and in-product docs UI.
- Separate list content (values, perks, comparison tables) with 1px hairlines rather than boxed cards.
- Center heroes with kicker + short headline + one-line subhead + two pill CTAs, then a big framed screenshot.
- Use large scenic imagery that fades into the canvas at the edges instead of hard-edged hero photos.
- Ship a true light theme that reuses the exact same layout and component shapes.

Don't:
- Don't fill primary marketing CTAs with the brand green — the site's CTAs are neutral black/white pills.
- Don't add drop shadows or heavy elevation; hierarchy comes from fill lightness and 1px borders.
- Don't use square or 4px-radius buttons — every interactive pill is fully rounded.
- Don't saturate the palette; body text sits at muted gray (#A1A1AA on dark) with color only in imagery and small accents.
- Don't crowd sections — vertical spacing between blocks is very generous, with one idea per screen.
