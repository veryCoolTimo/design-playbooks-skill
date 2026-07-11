# DESIGN.md generator template

Fill this for the USER'S project. Copy hex/font FACTS from the closest reference
profile; write all prose in your own words for the user's brand. Apply requested
hue shifts. Substitute proprietary fonts with a close free alternative and say so.

```markdown
---
project: <Brand>
kind: design-system
style: <ML|DT|DN|CP|IL|BT|EL|PH|GR>
reference: <slug it was derived from>
colors:
  canvas: "#hex"          # page background
  surface-1: "#hex"       # raised cards
  surface-2: "#hex"       # nested / hover
  ink: "#hex"             # primary text
  ink-muted: "#hex"       # secondary text
  hairline: "#hex"        # borders
  primary: "#hex"         # main CTA / brand
  primary-hover: "#hex"
  accents: ["#hex"]       # 0-3 supporting
  success: "#hex"
  danger: "#hex"
typography:
  display: "<font> · <weights> · <tracking>"
  body: "<font> · <size range>"
  mono: "<font, if used>"
rounded: { sm: "Npx", md: "Npx", lg: "Npx", pill: "9999px" }
spacing: { section: "Npx", block: "Npx", inline: "Npx" }
container: "NNNNpx"
---

## Overview
2-4 sentences: the visual language for THIS brand.

## Colors
Role → hex table; when to use each; contrast notes.

## Typography
Display/body/mono roles, scale, tracking, casing rules.

## Layout
Nav pattern, container width, section rhythm, grid, whitespace.

## Components
Buttons (states), cards, inputs, badges — shape/border/shadow with token refs.

## Do's and Don'ts
5 Do / 5 Don't specific to this brand's language.

## Responsive Behavior
Breakpoints, how the grid collapses, touch targets, image behavior.

## Agent Prompt Guide
A ready-to-paste block for an AI agent: 1-line palette summary (canvas/ink/primary hex),
the two font names, radius scale, and 2-3 imperative rules ("use <primary> for one CTA
per section; headings weight X; cards Npx radius"). This makes the file drop-in usable.
```

**Ecosystem note:** the section names above are compatible with the widely-used Google
Stitch / awesome-design-md 9-section format (Visual Theme, Color Palette & Roles,
Typography Rules, Component Stylings, Layout Principles, Depth & Elevation, Do's and
Don'ts, Responsive Behavior, Agent Prompt Guide). Keep them so generated files work in
any tool that expects that format.
