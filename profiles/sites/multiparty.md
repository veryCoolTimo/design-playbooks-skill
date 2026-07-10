---
name: multiparty
kind: site
style: ML
category: dev-infra-security
website: https://multiparty.ai/
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#111827"
  primary: "#2563EB"
  accents: ["#0B1130", "#3B82F6", "#F3F4F6"]
typography:
  display: "Inter/SF-style geometric grotesque · bold-heavy · tight tracking"
  body: "Inter/system sans, plus a workhorse monospace for code"
radius: "small 2-6px on buttons and code cards; nav CTA and tag chips are pill"
---
## Overview
A minimal-light developer-tool landing page: white canvas, near-black ink, one saturated blue doing all interactive work. The page reads like documentation with personality — real code snippets, policy diagrams, and permission-dialog mockups carry the visual load instead of illustration. One full-bleed dark navy section mid-page inverts the scheme for the "what is it" explainer.

## Layout
Floating rounded nav bar pinned top with logo left and three items plus a pill blue CTA right. Centered hero: oversized two-line bold headline, short gray subcopy with bolded product name, then an inline email input + blue button, then a row of gray capability chips. Below the hero, a full-width light diagram band (dotted background) showing chat bubbles, code nodes, and a permission dialog connected by lines. Sections alternate: centered heading, interactive step-through demo with labeled code panels; a big left-aligned bold statement block; the inverted dark navy section with bulleted feature copy and a code-comparison card; closing centered waitlist repeat of the hero form; tiny "BUILT BY Indent" footer. Generous vertical whitespace between sections, narrow centered text columns.

## Components
Buttons: solid blue (#2563EB) small-radius rectangles with white text ("Join Party", "Next →"); dialog mockup shows paired secondary (white, gray border) and primary blue buttons. Inputs: thin gray-bordered white fields with light gray placeholder, small radius, paired inline with the CTA. Cards: white panels with hairline gray borders and barely-there shadows containing monospace code with syntax coloring (blue/orange/green on light); labeled with tiny uppercase mono headers ("CHECKPOINT", "AVOID SHARING LOCATION"). Chips: light gray pill tags for capabilities; dark pill badge ("Still in private alpha", "OK, but what is it?"). Tab toggle (AI + ML / Finance / Security) as a dark segmented control inside the navy section.

## Signature
- UI-as-illustration: actual permission dialogs, chat bubbles, and syntax-highlighted code panels wired together with connector lines instead of abstract art
- Single blue (#2563EB) used for every CTA, link highlight, and chat bubble — no secondary brand color
- Big bold statement typography mid-page with a blue-highlighted phrase inside otherwise black text
- One dark navy inversion block breaking an otherwise all-white page
- Playful conversational copy ("Join Party", "Let's Party", "OK, but what is it?") against a strict technical layout

## Do
- Keep the canvas pure white with hairline gray borders; let real code and UI mockups be the imagery
- Use exactly one blue for all interactive elements and inline text highlights
- Set headlines huge, bold, near-black, tightly tracked, and center them in the hero
- Label diagram panels with tiny uppercase monospace captions
- Reserve the dark navy block for one explainer section and mirror the light structure inside it

## Don't
- Don't add gradients, photography, or decorative illustration — everything visual is functional UI
- Don't introduce a second accent color; even success/warning states stay inside code syntax coloring
- Don't use large border radii or heavy drop shadows on cards; borders are thin and shadows minimal
- Don't fill whitespace — sections are short, centered, and separated by large empty gaps
- Don't make the nav heavy; it stays a slim floating bar with a single pill CTA
