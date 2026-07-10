---
name: cluely
kind: site
style: ML
category: ai-meeting-saas
website: https://cluely.com/
pages: [home, pricing, enterprise, careers]
palette:
  canvas: "#EDEFF6"
  ink: "#5A6472"
  primary: "#141414"
  accents: ["#4E9EFF", "#DDEAFE", "#F5C518"]
typography:
  display: "SF Pro / Inter-class neo-grotesque · medium-to-semibold · tight, near-default tracking"
  body: "Same neo-grotesque (Inter/SF Pro feel), regular weight, cool gray"
radius: "buttons medium 8-10px; cards large 16-20px; tags/toggles pill"
---
## Overview
Apple-adjacent minimal-light design: a soft periwinkle-gray canvas that gradients into white mid-page, near-black grotesque headlines, and muted gray body copy. Depth comes from soft ambient shadows and frosted, 3D "floating keycap" props rather than borders or hard lines. The overall read is calm, premium desktop-software marketing with one loud exception — the careers page injects sticker-collage playfulness (hand-painted yellow script, smiley and flame stickers) on the same quiet base.

## Layout
- Nav: slim top bar — logo left, four text links center-left, one solid dark pill/rounded CTA far right ("Get Started for Free" with Apple glyph). No nav border; it sits on the tinted canvas.
- Heroes: centered, large multi-line headline (often with an inline logo mark or gray de-emphasized words for contrast, e.g. "It's like Googling Mid-Sentence"), short gray subhead, one or two CTAs. Floating translucent 3D keyboard-key objects decorate hero and footer-CTA corners.
- Sections alternate: tinted-canvas bands and white bands, each introduced by a small blue eyebrow line ("Live meeting insights", "Open roles") above a black H2.
- Content patterns: big centered product screenshot in a rounded frame; 3-across card grids with caption text below; icon + title + description rows for use cases; accordion FAQ; wide feature-comparison table on pricing with the Enterprise column tinted blue.
- Footer: dark-on-light multi-column link grid, "All systems operational" green-dot status chip, and a row of circular compliance badges (SOC 2, ISO, GDPR, CCPA, HIPAA).

## Components
- Primary buttons: solid near-black (#141414) with subtle vertical gradient, white label, 8-10px radius, gentle drop shadow. Secondary/sales CTAs: light-to-mid blue gradient fill (#4E9EFF range) with soft glow, white text. Ghost/link actions are plain blue text.
- Cards: white or near-white fills, 16-20px radius, hairline-free — separation via soft diffuse shadows; pricing cards get a faint outer glow, the highlighted Enterprise card a blue-tinted halo.
- Tags: small light-blue pill chips ("Full time", "Coming soon") with blue text.
- Inputs/prompt bars: frosted translucent rounded search bar with sparkle icon, used decoratively in heroes.
- Tables: borderless rows with hairline dividers, blue checkmarks and gray x marks; highlighted plan column has a pale blue background panel.
- Toggle: pill-shaped Monthly/Annually switch with dark knob.

## Signature
- Periwinkle-gray canvas gradually fading to white and back — sections blend via gradients, almost never via hard edges.
- Translucent 3D keyboard keycaps (cmd, return, arrows) floating as ambient decoration around heroes and closing CTAs.
- Dark gradient primary buttons alongside glowing blue "Talk to sales" buttons — a two-CTA hierarchy repeated site-wide.
- Gray-on-black headline emphasis trick: de-emphasized words in light gray, the key word in black or with a blue scribble accent ("Interviews. Sales calls. Homework. **Meetings.**").
- Compliance-badge strip and status chip in the footer as a trust signature.

## Do / Don't
**Do**
- Build depth with soft shadows and background gradients; keep cards and sections borderless.
- Use one small blue eyebrow label above every black section heading to set rhythm.
- Keep body copy in muted cool gray (#5A6472) and reserve pure near-black for headings and button fills.
- Pair the dark primary CTA with a blue gradient secondary CTA; add the Apple glyph on download CTAs.
- Let big rounded product screenshots (macOS-style UI in 16-20px frames) carry the feature story.

**Don't**
- Don't add visible card borders, outlines, or hard section dividers — separation is tonal and shadow-based.
- Don't use saturated colors beyond the single blue family (plus the careers-page sticker art); no multi-color icon sets.
- Don't make headlines heavy display-black; weight stays medium/semibold with normal case.
- Don't use pill-shaped main buttons — pills are reserved for tags and toggles; buttons stay 8-10px.
- Don't put dense text over the decorative hero collages; heroes keep one headline, one subhead, one or two CTAs.
