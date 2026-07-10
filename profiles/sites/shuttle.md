---
name: shuttle
kind: site
style: DT
category: file-sharing-saas
website: https://shuttle.zip/
pages: [home, pricing, updates]
palette:
  canvas: "#000000"
  ink: "#9C9C9E"
  primary: "#FFFFFF"
  accents: ["#2E62F0", "#F5A623", "#E8332E"]
typography:
  display: "geometric grotesque (Aeonik/Neue Haas feel) · extrabold · tight"
  body: "same grotesque family · regular · normal"
radius: "pill buttons; medium 8-14px cards (app mockups ~16px)"
---
## Overview
Near-pure black canvas with heavy white display type and muted gray body copy; the product itself supplies the color. Realistic dark-mode app mockups (file browsers, share dialogs, activity feeds) float on the void as the sole imagery, dotted with emoji-style blue folder icons, warm photo thumbnails, and colored multiplayer cursors. A hand-drawn orange arrow doodle and cursor name-tags add a playful counterweight to the otherwise austere layout. Punctuated two-line taglines ("Your files. Your rules.") anchor both the hero and the footer.

## Layout
Slim top nav: bold wordmark left, three small text links right (Updates, Pricing, Sign up), separated from content by a hairline rule. Content is left-aligned in a narrow center column (~40% of viewport width) — even the hero headline sits left-of-center rather than centered. Home page alternates rhythm: short copy block + white pill CTA + "Currently in beta" microcopy, then a full-width dark app-mockup composition, repeated four times. Pricing uses a classic 3-card row where the middle and right cards are outlined in blue and orange respectively. Updates page is a changelog: each entry pairs a large rounded image card (light/lavender/blue gradient backgrounds framing app screenshots) with dim gray prose below. Generous black whitespace between every section; no visible grid lines or section dividers.

## Components
Buttons: white pill with black label for primary ("Get started for free"), dark-gray pill with white label for secondary ("Follow us"); pricing cards use small rounded-rect buttons tinted per plan (gray, blue #2E62F0, orange #F5A623). Cards: pricing cards are ~12px rounded rects on near-black fill with 1px borders — neutral gray for Free, blue for Individual, orange for Team — with matching colored plan names and checkmarks. FAQ rows are full-width dark-gray rounded bars with chevron toggles. App mockups: dark #161618-ish panels with subtle 1px borders, sidebar + content-pane structure, floating modal dialogs (Share, Invite, Customize) with soft shadows. Multiplayer cursor badges: saturated pill labels (blue, red, orange) with pointer triangles. No glassmorphism, no gradients on the marketing chrome itself.

## Signature
- Punchy two-sentence headline pattern with terminal periods ("Your files. Your rules.") in extrabold tight-set grotesque, repeated hero-to-footer.
- Left-aligned narrow content column on a pure black field — deliberate asymmetry instead of centered-hero convention.
- Color-coded pricing tiers: card border, plan name, checkmarks, and CTA all inherit the tier hue (gray / blue / orange).
- Playful artifacts on austere ground: hand-drawn orange arrow squiggles, emoji-blue folder icons, and named multiplayer cursors scattered around sections.

## Do / Don't
**Do**
- Keep the canvas true black and let dark app mockups sit borderline-invisible on it, defined only by faint 1px borders.
- Reserve saturated blue and orange for meaning (tier identity, in-app actions, cursors), never for page chrome.
- End every headline sentence with a period and split it across two short lines.
- Repeat the CTA pattern verbatim after each feature section: white pill + tiny gray "Currently in beta" note beside it.
- Dim long-form prose (updates page) to mid-gray so imagery stays dominant.

**Don't**
- Don't center the hero or widen body copy beyond the narrow left column.
- Don't add gradients, glows, or glass effects to marketing surfaces — gradients belong only inside the changelog image-card backgrounds.
- Don't color the primary CTA; it is white-on-black everywhere, with colored buttons confined to pricing cards.
- Don't use stock photography or illustration — the only imagery is the product UI itself.
- Don't introduce heavy card shadows or thick borders; separation comes from hairlines and spacing.
