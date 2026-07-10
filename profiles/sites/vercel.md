---
name: vercel
kind: site
style: ML
category: developer-platform
website: null
pages: [home, ai-gateway, customers, pricing]
palette:
  canvas: "#fafafa"
  ink: "#171717"
  primary: "#171717"
  accents: ["#0070f3", "#7928ca", "#ff0080", "#50e3c2", "#f9cb28"]
typography:
  display: "Geist Sans (Inter substitute) · semibold 600 · very tight negative tracking (-2.4px at hero size)"
  body: "Geist Sans; Geist Mono for code and uppercase eyebrows"
radius: "bimodal — pill (100px) marketing CTAs vs small 6px nav/app buttons; cards medium 12-16px"
---
## Overview
A monochrome developer aesthetic: one near-black ink (#171717) does the work of headings, body hierarchy, CTA fills, and borders on a #fafafa sheet. Chroma is quarantined to a single soft mesh gradient (blue/cyan/violet/pink/amber) blooming in the hero; the rest of the page stays ink-on-white. The result feels like spec-sheet documentation that sells — precise, flat, quiet.

## Layout
Top nav on the canvas color with a bottom hairline: black wordmark left, gray ghost links, square Sign Up/Log In buttons right. Centered ~1200px container. Rhythm: gradient hero (128px vertical padding) → grayscale logo strip → 2/3/4-up grids of hairline-bordered white cards → code-editor band → template cards → display-type CTA band → gray footer. Whitespace and 1px lines separate everything; no heavy background blocks. 4px spacing base scaling to 96-128px between sections.

## Components
Two button families signal context: fully rounded black pills (white text, 0x14px padding) for marketing CTAs and their white-pill secondary twins; tight 6px-radius squares for nav and app chrome (black fill or white with hairline border). Category tabs are 64px pills; icon buttons are circles. Cards are pure white on the off-white canvas, defined by a 1px #ebebeb hairline at 12px radius (16px for pricing), shadowless by default; floating surfaces get a layered very-low-alpha shadow stack. Inputs match the small-button chrome: white, hairline, 6px radius. Code blocks are white with mono type inside a hairline frame.

## Signature
- Color exists in exactly one place: the multi-stop hero mesh gradient; every other pixel is the ink/gray/white ladder.
- Pill-vs-6px-square button split — the shape itself tells you marketing surface vs app chrome.
- Geist Mono uppercase eyebrows introducing sections like technical spec labels.
- Display type at 600 weight with aggressive negative tracking (-2.4px hero, -1.28px section headings).

## Do / Don't
Do:
- Build depth from 1px #ebebeb hairlines and the white-on-#fafafa surface step before reaching for any shadow.
- Keep weight binary: 600 headings, 500 buttons/labels, 400 everything else — no light, black, or italic.
- Step text grays deliberately: #171717 → #4d4d4d → #8f8f8f → #a1a1a1.
- Reserve #0070f3 for links, focus, and positive states only.
- Tighten letter-spacing as headings grow larger.

Don't:
- Don't use pure #000000 anywhere — ink is #171717 and body drops to #4d4d4d.
- Don't fill buttons, badges, or panels with the accent hues — violet/cyan/pink belong to the gradient and illustrations.
- Don't put a pill CTA in nav chrome or a square button in a marketing band; the shapes never mix contexts.
- Don't add a second decorative device (glows, photos, patterns) — the hero gradient is the only flourish.
- Don't stack heavy drop shadows; the strongest elevation is a finely layered low-alpha pair on menus/modals.
