# Profile generation prompt (calibrated)

You are a design analyst. Read the screenshot files listed below with the Read tool,
then write a design profile for site "{{SLUG}}".

Screenshots (read ALL of them):
{{SCREENSHOT_PATHS}}

Known metadata (may be partial; trust the screenshots over it):
{{KNOWN_META}}

Return ONLY the profile markdown, exactly in this schema:

```markdown
---
name: {{SLUG}}
kind: site
style: <ML|DT|DN|CP|IL|BT|EL|PH|GR>
category: <industry slug>
website: <url or null>
pages: [<page types seen>]
palette:
  canvas: "#hex"
  ink: "#hex"
  primary: "#hex"
  accents: ["#hex"]
typography:
  display: "<family or closest guess> · <weight feel> · <letter-spacing feel>"
  body: "<family or closest guess>"
radius: "<none|small 2-6px|medium 8-14px|large 16px+|pill>"
---
## Overview
2-4 sentences: the visual language in essence.
## Layout
Nav pattern, hero structure, section rhythm, grid/whitespace character.
## Components
Buttons, cards, inputs: shape, borders, shadows, states seen.
## Signature
2-4 bullet points: what makes this site recognizable.
## Do / Don't
3-5 Do bullets, 3-5 Don't bullets grounded in what the screenshots show.
```

Rules:
- Hex colors: sample what you actually see. For `primary`, sample the MAIN CTA BUTTON
  fill specifically (not links, not logos). For `canvas`, sample the dominant page
  background; for `ink`, body text color. Check both hero and mid-page sections.
- Typography: inspect headings and body separately. Name the family if recognizable
  (Inter, Geist, GT America, Söhne, serif families...), otherwise describe the shape
  ("geometric grotesque", "humanist serif", "mono-spaced").
- radius: judge from buttons AND cards; if buttons are pills but cards are medium,
  write "pill buttons, medium cards".
- Do/Don't must be specific to THIS site's language, not generic design advice.
- American spelling. No marketing fluff. Output ONLY the markdown profile.
