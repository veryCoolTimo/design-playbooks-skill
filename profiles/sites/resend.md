---
name: resend
kind: site
style: DT
category: email-api-saas
website: https://resend.com/
pages: [home, features, pricing, enterprise, contact, handbook]
palette:
  canvas: "#000000"
  ink: "#a1a1aa"
  primary: "#f5f5f5"
  accents: ["#2ebd85", "#0d3d3a"]
typography:
  display: "high-contrast editorial serif (Didone/Newsreader-like) for hero words · light-to-regular · tight; geometric grotesque (Inter-like) · medium · normal for section heads"
  body: "Inter-like geometric grotesque"
radius: "buttons pill; cards/inputs medium 8-14px"
---
## Overview
Near-total black canvas with a strictly monochrome grayscale system: white display type, gray body text, hairline dark-gray borders. The single chromatic voice is a functional green (status dots, pricing checkmarks) plus a faint teal light-beam glow behind the home hero. The defining move is typographic tension — enormous editorial serif hero words ("HandBook", "Get in touch", "Pricing") set against clean grotesque UI text everywhere else.

## Layout
Slim top nav: wordmark left, center dropdown links (Features, Company, Resources, Help, Docs, Pricing), right "Sign in" + white pill "Get Started". Heroes are centered (home, features) or left-aligned two-column (enterprise pairs headline with an inline contact form). Long single-column pages with generous vertical padding; sections alternate centered serif-or-grotesque headings, 2-3 column feature grids divided by thin vertical rules rather than boxed cards, logo walls in grayscale, and full-width dark product-UI screenshots. Massive footer sitemap (6 columns) with address, YC badge, social icons, and a green "All systems operational" status pill.

## Components
Buttons: white pill with dark text (primary), dark charcoal pill with light text (secondary/table CTAs), some with trailing chevron. Cards: very dark gray (#111-ish) fills, 8-14px radius, hairline #27272a borders, no visible shadows — separation by tone, not elevation. Inputs: dark fills, subtle 1px border, ~8px radius, muted gray placeholders. FAQ rows as slim dark rounded bars with chevron toggles. Pricing tiers as bordered dark cards with green check bullets; comparison tables use hairline row rules and green check icons. Testimonial cards with small circular avatars in a horizontal strip.

## Signature
- True-black background with grayscale-only imagery (logo walls, generative-art book covers) and one functional green accent
- Giant high-contrast editorial serif reserved for a few hero words, colliding with an otherwise all-grotesque interface
- Thin vertical/horizontal hairlines dividing feature grids instead of card boxes
- Embedded dark-mode product screenshots (dashboard, code editors with syntax highlighting) as the main visual proof
- Green "All systems operational" pill and green checkmarks as recurring trust markers

## Do
- Keep the canvas true black and build hierarchy from grays (#111 cards, #27272a hairlines, #a1a1aa body, #fff headings)
- Reserve the display serif for one or two short hero phrases per page; use the grotesque for all section headings and UI
- Use white pill buttons for the primary CTA and charcoal pills for secondary actions
- Let green appear only as semantic signal (checks, status, live dots), never decorative
- Show the product via dark UI screenshots and real code blocks with syntax color

## Don't
- Don't introduce brand colors into buttons, links, or backgrounds — CTAs stay white/charcoal
- Don't add drop shadows or gradients on cards; separation comes from fill tone and 1px borders
- Don't use colored or photographic imagery — illustrations and logos stay grayscale
- Don't box every feature into cards; prefer hairline-divided columns for feature grids
- Don't set body copy in the serif or at high contrast — the serif is a display-only accent
