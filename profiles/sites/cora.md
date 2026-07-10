---
name: cora
kind: site
style: IL
category: ai-assistant-saas
website: https://cora.computer/
pages: [home]
palette:
  canvas: "#1a89c0"
  ink: "#fdfaf2"
  primary: "#ffffff"
  accents: ["#0e7dc4", "#df9721", "#101010", "#f16156"]
typography:
  display: "old-style serif (Lyon/Freight-like) · regular weight, high contrast · normal tracking"
  body: "modern grotesque sans (Graphik/Inter-like)"
radius: "pill (buttons); large 16-24px (cards, product frames)"
---
## Overview
One continuous painterly landscape mural is the entire page: the scroll travels from a bright blue sky with cumulus clouds down through golden California hills to a dusk-brown foreground, and every section floats on top of it. Crisp white product UI cards (inbox lists, draft composer, daily brief) sit like paper cutouts against the painting. Serif display headlines in cream white plus a plain grotesque for body copy give it a calm, literary, anti-SaaS tone. A solid flat-blue frame (#0e7dc4) borders the whole viewport like a postcard, echoing the postage-stamp logo.

## Layout
Minimal nav: stamp-style logo left, "Log in" + blue pill "Start free trial" grouped inside a single white pill capsule right. Hero is centered serif headline, one-line subhead, single white pill CTA, then a large rounded product screenshot that overlaps into the illustration. Sections alternate: left-aligned text block (serif H2 + sans paragraph + pill CTA) paired with a floating white UI card on the right; then full-width centered moments (envelope illustrations, "Today's Brief" card stack). Section rhythm is extremely airy — hundreds of pixels of pure painting between sections, with the mural's color shift (sky → hills → dusk) acting as the section divider. Pricing is two white cards on the ochre field; FAQ is a stack of dark translucent accordion pills; footer is one large dark-brown rounded panel.

## Components
Buttons: pills throughout. Primary = solid white pill with near-black label and trailing arrow (hero, footer); secondary = 1px white-outlined transparent pill on the painting ("Start your free trial", "Get Started" mid-page); nav CTA = solid blue (#0e7dc4) pill; pricing CTAs = solid black (#101010) pills on white cards. Cards: white, large radius (~16-24px), soft diffuse shadow, thin light borders; product-shot frames get a thick off-white bezel. Translucent panels: dark brown/blackish glass with lighter 1px border (security grid, FAQ accordions, plan toggle). Small accents inside UI mocks: red calendar chip (#f16156), orange folder, checkmark lists.

## Signature
- A single top-to-bottom painted landscape (sky → golden hills → dusk) as the page background, with scroll position mapped to time-of-day and color temperature.
- Postage/mail metaphor: stamp-shaped logo, painted envelope illustrations mid-page, "MADE BY EVERY" postmark in the footer.
- Cream serif display type over the painting vs. black grotesque UI type inside white cards — two distinct text worlds.
- Flat blue postcard border framing the entire viewport.

## Do / Don't
- Do run one continuous illustrated environment behind all sections and let its color shifts (blue → ochre → brown) replace visible section boundaries.
- Do keep real product UI in crisp white large-radius cards so it reads as artifact-on-painting, not screenshot-in-template.
- Do use white or white-outlined pill buttons over the illustration and reserve solid black pills for CTAs sitting on white cards.
- Do set headlines in a warm old-style serif in cream (#fdfaf2) and switch to a plain grotesque for all UI and body copy.
- Don't place long body text directly on busy painted areas — keep paragraphs short or move them onto cards/translucent panels.
- Don't introduce gradients, neon, or glassy tech styling; the palette must stay within the mural's natural sky/earth tones plus white and near-black.
- Don't use sharp corners anywhere — every interactive element is a pill and every container is heavily rounded.
- Don't crowd sections; the empty stretches of painting between blocks are structural, not wasted space.
