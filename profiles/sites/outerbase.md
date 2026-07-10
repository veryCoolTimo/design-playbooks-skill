---
name: outerbase
kind: site
style: DT
category: dev-data-tools
website: https://www.outerbase.com/
pages: [home, pricing, blog]
palette:
  canvas: "#0e0e0e"
  ink: "#c9c9c9"
  primary: "#e8e8e8"
  accents: ["#8b5cf6", "#34d399", "#f5a623"]
typography:
  display: "Inter-like geometric grotesque · bold/semibold · tight; serif wordmark (soft chunky serif) reserved for the logo"
  body: "Inter-like grotesque; JetBrains Mono-style monospace for pricing-table values and SQL snippets"
radius: "pill on buttons; medium 8-14px on cards and app-screenshot frames"
---
## Overview
Near-black "outer space" dark theme: an almost flat #0e0e0e canvas dusted with faint star specks and constellation line-art, with content rendered in shades of gray. Color is rationed to tiny doses — purple chart bars, a green terminal icon, amber SQL syntax — while every CTA is a light pill that glows against the dark. The mood is quiet, monochrome, and telescope-like: soft radial glows behind the hero product shot act as the main light source.

## Layout
Top nav is minimal: serif wordmark left, three text links (Pricing, Blog, Docs) plus two pill buttons (dark "Log in", white "Sign up") right. Home hero is centered: eyebrow pill badge, large three-word headline, one-line subhead, single CTA pill, then a floating product screenshot lit from behind by a planet-horizon glow, followed by a grayscale logo strip. Sections alternate centered headlines with bento-style feature card grids (2-col asymmetric clusters of dark rounded cards). Pricing uses three side-by-side plan cards over a long monospace comparison table with hairline row dividers. Blog is a single centered column: hero post card with constellation image, then a hairline-divided list of recent posts. Generous vertical whitespace between sections; constellation doodles fill empty regions.

## Components
Buttons: pills in two tones — off-white fill (#e8e8e8) with dark text for primary actions, dark gray (#2a2a2a-ish) with light text for secondary; no visible drop shadows, just contrast. Cards: dark charcoal (#1a1a1a range) panels, 8-14px radius, barely-there 1px borders, slightly lighter than the canvas; plan cards get a subtle top-lit gradient. Inputs shown in product mockups: dark fields with rounded corners and placeholder gray text. Checkmarks in pricing lists are thin, dim gray glyphs. Toggle switch (Monthly/Annual, light/dark theme) is a pill with a white knob. Tables use monospace values and 1px hairline dividers instead of zebra striping.

## Signature
- Space metaphor carried literally: star-speck background, constellation line drawings, planet-horizon glow behind the hero, copy like "communications from ground control."
- Serif display wordmark against an otherwise all-grotesque, all-gray interface.
- Nearly monochrome grayscale system where purple/green/amber appear only inside product mockups and charts, never in page chrome.
- White pill CTAs as the brightest objects on the page — light-on-dark inversion instead of a brand-color button.

## Do
- Keep the canvas near-black and flat; create depth with soft radial glows and slightly-lighter charcoal cards, not shadows.
- Make primary CTAs off-white pills with dark text; pair with a dark-gray secondary pill.
- Use monospace for data: pricing values, feature-table cells, SQL/code snippets.
- Scatter faint star dots and thin constellation line-art in empty regions and section transitions.
- Ration accent color (purple, green) to product screenshots, charts, and icons inside cards.

## Don't
- Don't introduce a saturated brand-color button — CTAs here are white/gray pills, never purple or blue fills.
- Don't use heavy borders, drop shadows, or elevation stacks; separation comes from 1px hairlines and tonal steps.
- Don't set headings in the serif — the serif is logo-only; page headings stay grotesque sans.
- Don't brighten the background or add light-mode sections; every page section sits on the same near-black canvas.
- Don't zebra-stripe or box the comparison table — thin dividers and monospace alignment carry it.
