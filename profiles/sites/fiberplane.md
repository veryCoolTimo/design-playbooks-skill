---
name: fiberplane
kind: site
style: BT
category: devops-saas
website: https://fiberplane.com/
pages: [home]
palette:
  canvas: "#F4F4F4"
  ink: "#18181B"
  primary: "#141414"
  accents: ["#8B7CFF", "#F97434", "#EC3E8F", "#2BB35A"]
typography:
  display: "high-contrast transitional serif (Tiempos/Freight feel) · regular-to-medium weight at very large sizes · tight, near-default tracking"
  body: "compact neo-grotesque sans (Inter-like) · small sizes, muted gray"
radius: "pill on buttons; large 16px+ on cards, app screenshots, and full-width gradient section blocks"
---
## Overview
A big-type editorial landing page for a devops notebook tool: enormous serif headlines set against a quiet light-gray canvas, punctuated by full-bleed rounded sections filled with soft aurora gradients (violet, orange, magenta) or near-black. Product truth is carried by large, realistic app screenshots floating over the gradients. Color lives almost entirely in the gradient panels and tiny UI chips; chrome (nav, buttons) stays strictly black and white.

## Layout
- Slim dark pill-shaped nav bar floating at top: logo left, text links center, "Log in" plus black "Try for free" pill right.
- Hero is nearly all typography: a 4-line serif headline with staggered/indented line breaks ("Hackable / runbooks / for effective / workflows"), decorated with small avatar cursors and colored collaboration carets woven between the words; one word inverted with a black highlight box. Sub-copy is tiny and gray, CTAs are modest pills below.
- Section rhythm alternates: light-gray canvas with centered serif headline → full-width rounded rectangle section (purple/orange gradient or black) containing an app screenshot → back to light canvas. Generous vertical whitespace between bands.
- Mid-page "Your team, literally on the same page" uses horizontally scrolling rows of colored avatar+name pills bleeding off both edges.
- Closing CTA is another large gradient rounded band with left-aligned serif headline and a black button; multi-column footer on light gray.

## Components
- Buttons: solid near-black pills with white text and a "›" chevron ("Try for free ›", "Get started for free ›"); secondary actions are white/light pills with subtle borders ("Watch video", Product Hunt badge). No visible gradients or shadows on buttons.
- Cards/screenshots: white app-UI mockups with large rounded corners (~12-16px) and soft drop shadows, floating over gradient or black backgrounds; terminal mockup is a dark rounded card with monospace green-on-black-ish log text.
- Chips/labels: small rounded tag pills in pastel colors inside the notebook UI; avatar pills with thin colored outlines; a green "Open discussion" pill.
- Text highlight: solid black rectangle behind a word with white text ("effective", "fp.new" in monospace) — used as an inline emphasis device.
- Template cards: stacked white sheets with checkbox list items, slight rotation for a paper-pile effect.

## Signature
- Giant serif headline broken across staggered lines, invaded by live-collaboration cursors, carets, and avatar bubbles.
- Full-width heavily-rounded gradient blocks (violet/orange/magenta aurora blur) alternating with flat light-gray bands.
- Black highlight-box inversion on a single word inside headlines, including monospace command names (fp.new).
- Strict black-pill CTA against otherwise colorful gradients — color never touches the buttons.

## Do / Don't
**Do**
- Set headlines in a large high-contrast serif with deliberate, uneven line breaks; keep body copy tiny, gray, and sans-serif.
- Contain every gradient inside a large-radius full-width block; keep the page canvas itself flat light gray.
- Use solid black pills with a trailing chevron for all primary CTAs, in the nav, hero, and closing band alike.
- Show the product as real, detailed app screenshots (notebook UI, terminal, browser chrome) floating with soft shadows over the gradient panels.
- Emphasize single words with an inverted black highlight box; render commands/CLI terms in monospace inside that box.

**Don't**
- Don't color the buttons or links with the gradient hues — brand color stays in backgrounds, chips, and avatars only.
- Don't use sans-serif or all-caps for section headlines; every big heading on the page is the serif in sentence case.
- Don't fill the light sections with decoration — between gradient bands the canvas is empty except for centered type.
- Don't use sharp corners anywhere prominent; nav, buttons, screenshots, and section blocks are all pill or 16px+ rounded.
- Don't write long paragraphs — supporting copy is one or two tiny gray lines per section.
