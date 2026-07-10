---
name: lazy-so
kind: site
style: DT
category: productivity-software
website: https://lazy.so/
pages: [home]
palette:
  canvas: "#0d0e10"
  ink: "#a1a3a7"
  primary: "#1e1f23"
  accents: ["#fafafc", "#c8c9cd"]
typography:
  display: "Inter-style grotesque paired with an elegant transitional serif (Signifier/Freight feel) · regular-to-medium, oversized · tight tracking on sans, normal on serif"
  body: "Inter-style neo-grotesque"
radius: "small 4-6px on buttons; medium 8-14px on cards and the capture widget"
---
## Overview
Near-monochrome dark-tech minimalism built around light itself: a black canvas (#0a0a0a to #1a1c20) with a giant eclipse/planet radial gradient and a horizontal lens-flare beam slicing through the hero. Color is almost entirely absent -- hierarchy comes from grayscale value steps, soft glows, and a sans/serif type duet. The product (a capture command bar) sits dead-center as the hero object, rendered as a real UI widget rather than a screenshot mockup.

## Layout
Ultra-sparse nav: logo mark + wordmark left, a single "Get Lazy" button with a keyboard-shortcut chip (L) right, no menu links. Hero is fully centered: mixed sans/serif headline, one-line gray subtitle, then the interactive capture-bar widget framed by the eclipse glow. Sections alternate between charcoal panels and pitch-black starfield backdrops, each opening with a small uppercase letterspaced eyebrow ("UNIVERSAL CLIPPER"), a white sans headline, and a gray serif or gray sans echo line. Rhythm is long and cinematic -- generous vertical dead space (sometimes 500px+ of pure black with tiny star specks) between content blocks. Content sits in a centered ~1200px column; feature grids use 2-3 column card rows with thin 1px dividers. Page closes symmetrically with the eclipse motif rising from the bottom edge behind the final CTA.

## Components
Buttons: dark charcoal fill (#1e1f23) with a subtle 1px lighter border and white/near-white label, 4-6px radius -- the main CTA is barely lighter than the page, glow and placement carry the emphasis. Keyboard-shortcut chips (small bordered squares with a letter) accompany CTAs. Email input: slightly lighter charcoal fill (#323337 focus ring feel), inline @ icon, paired side-by-side with its button. Cards: #1c1d21 panels, 1px low-contrast borders, 8-14px radius, faint top-edge highlight suggesting embossed glass; no drop shadows, elevation implied by glow. The hero capture widget is a functional-looking command bar with placeholder text, a link-preview pill, an Inbox row, and a Capture button -- product-as-hero-component.

## Signature
- Eclipse motif: enormous dark circle with rim-light glow plus a horizontal lens-flare beam through the hero; the motif returns inverted at the page bottom.
- Sans/serif headline pairing in one line: "Capture" in white grotesque, "at the speed of thought" in lighter gray serif.
- Grayscale-only palette; not a single saturated brand color anywhere -- emphasis via luminance, glow, and starfield texture.
- Keyboard-first cues everywhere: shortcut chips on buttons, slash-command placeholder text, command-bar hero.

## Do / Don't
Do:
- Keep everything grayscale; separate layers with 2-4% luminance steps (#0a0a0a page, #1c1d21 card, #323337 input) and 1px borders.
- Pair a neutral grotesque with an elegant serif inside the same headline, using the serif for the softer, evocative half of the phrase.
- Center the hero and make a live-looking product widget the focal object, lit by a radial glow.
- Use uppercase letterspaced gray eyebrows above section headlines, and let sections breathe with very tall black gaps dotted with faint stars.
- Attach keyboard-shortcut chips to CTAs to reinforce the keyboard-first positioning.

Don't:
- Introduce accent colors, gradients with hue, or colored links -- the system is strictly value-based.
- Use drop shadows for elevation; this site uses rim glows and border highlights instead.
- Make the primary button bright or filled-white; CTAs here are dark charcoal with a border, distinguished by context not contrast.
- Crowd the nav with links -- the pattern is logo plus a single action button.
- Use large radii or pill buttons; corners stay tight (4-6px) even on large widgets.
