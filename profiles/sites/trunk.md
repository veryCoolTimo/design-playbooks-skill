---
name: trunk
kind: site
style: IL
category: dev-tools
website: https://trunk.io/
pages: [about, blog, customers, product-check, product-ci-analytics, product-ci-debugger, solution-bazel, solution-clang-tidy]
palette:
  canvas: "#0F0F0E"
  ink: "#A9A9A6"
  primary: "#F5F5F3"
  accents: ["#4ADE80", "#9B5CF6", "#3B82F6", "#F5A31B"]
typography:
  display: "neo-grotesque sans (Inter/Suisse-like) · semibold · tight, near-zero tracking"
  body: "same neo-grotesque sans, regular, muted gray"
radius: "pill buttons/nav; large 16px+ cards"
---
## Overview
An all-dark "night railway" world: near-black warm charcoal canvas covered in faint hand-sketched white line illustrations — mountain ridges at the top and bottom of every page, train tracks that snake down the entire scroll as a continuous pipeline metaphor, and wireframe 3D boxes/machines as hero objects. Headlines are big white grotesque type with one or two words tinted in the product's accent color; each product line owns a hue (Merge/Bazel green, Check/clang-tidy purple, CI Analytics blue, CI Debugger amber) while the chrome stays monochrome. The single strong solid element on any page is the white pill CTA.

## Layout
Floating pill navbar: dark capsule with a thin light outline, logo left, dropdown links center, "Log in" text + white-outlined "Sign Up" pill right. Heroes are left-aligned or centered H1 (2-3 lines, accent-colored keyword) + one-line subhead + "Get Started" white pill and "Schedule A Demo" ghost text link, with a sketched illustration to the right or behind. Below: grayscale customer logo strip, then alternating full-width dark cards and 2-3 column feature-card grids; the sketched track illustration threads between sections and generous black space separates them. Every page ends the same way: centered "Try it yourself or request a demo" block, CTA pair, a sketched cylindrical tree-trunk illustration, then a footer with newsletter pill input, 5-column link lists, and a green "All systems operational" status dot.

## Components
- Buttons: primary = solid off-white pill with near-black label; secondary = plain white text link or thin-outlined pill; no shadows, no gradients.
- Cards: very dark gray (#1A1A19-ish) panels with 16-20px radius and a hairline lighter border; interiors mix short copy with small sketch illustrations; two-tone card titles (white word + gray word).
- Inputs: pill-shaped email field with dark fill and thin border, "Subscribe" pill sitting inside/adjacent.
- Product UI mockups shown as dark terminal/dashboard panels with mono type and accent-colored data (green checks, blue charts, syntax-highlighted code).
- Team/blog imagery is grayscale; blog thumbnails are illustrations in framed dark cards.

## Signature
- Continuous hand-drawn white train-track/pipeline illustration winding down the full page, plus sketched mountain silhouettes framing top and bottom.
- One accent hue per product (green, purple, blue, amber) applied only to a keyword in the headline, small icons, and illustration highlights — never to the CTA, which stays white.
- Wireframe/sketch 3D objects (crates, cylinders, machines) instead of photos or flat vector art; everything else grayscale.
- Pill-everything chrome: capsule navbar, pill buttons, pill inputs, pill filter chips on the blog.

## Do
- Keep the canvas near-black and let sketched white line art carry the illustration load; reserve solid fills for the CTA and tiny accent dots.
- Color exactly one or two headline words in the section's accent; keep surrounding text white.
- Use the white pill "Get Started" + plain-text "Schedule A Demo" pairing consistently at hero and page end.
- Give cards a hairline border and 16px+ radius on a slightly lighter dark fill so they read against the black without shadows.
- Use monospace type for code-flavored moments (printf(), terminal panels) with accent-colored tokens.

## Don't
- Don't introduce light/white page sections — every page here is dark edge to edge.
- Don't color the primary CTA with the product accent; the button is always off-white.
- Don't use photography or glossy 3D renders; imagery is grayscale portraits and pencil-style line sketches only.
- Don't mix multiple accent hues within one product page (blog/customers aside, each page commits to a single accent).
- Don't add drop shadows, gradients, or heavy borders; depth comes from fill-value steps and hairlines.
