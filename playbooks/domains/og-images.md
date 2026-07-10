# OG / Share Images Domain Playbook
> Coverage: 49 images from corpus

## When to use this corpus

- Designing an `og:image` / Twitter card / LinkedIn share image for a site, product, launch, or article.
- Choosing a composition pattern (headline + brand block, logo-centered, full-bleed art, split layout) before opening a canvas or writing generation code.
- Deciding how much text belongs on a share card, and where the wordmark goes.
- Picking a background treatment (flat brand field, gradient glow, texture/grain, blueprint grid, photo, 3D render) that matches the brand's register.
- Sanity-checking an existing card against what strong companies actually ship at 1200×630.

## Craft rules

1. **Design for the thumbnail, not the full frame.** Cards render as small as ~500×260 in feeds and ~150px in chat previews. Every reference that carries text keeps it huge relative to the frame: Mobbin and Attio set headlines at roughly 10-13% of image height per line. If a line of text is under ~48px at 1200×630, cut it or merge it.

2. **One message per card.** No reference in the corpus says two things. It is a headline (attio: "Customer Relationship Magic."), a value claim (mobbin: "Never run out of design inspiration again."), a brand statement (runner: "Runner does the work"), or a pure logo lockup (magma, dirt, ingamana). Body copy, feature lists, and secondary taglines do not survive thumbnail size — Lovable's single subtitle line is the maximum.

3. **Headline text-left, art-right is the workhorse layout.** The dominant pattern (attio, mobbin, lovi, chutes, fin, equals, twelvelabs, puck): text block anchored left third-to-half, visual object filling the right. Left-anchored text reads first at a glance and survives right-edge cropping in some feed layouts.

4. **Anchor the brand block in a corner, small and quiet.** Logos live bottom-left (cash-app, runner, popcorn, steno-ai, rre) or top-left (mobbin, handhold, equals), with wordmark bottom-right as a secondary spot (attio, contra). The logo is never the headline's size unless the logo IS the card (dia, magma, ribbit). Keep it 40-80px tall and give it corner breathing room — cropping algorithms shave edges.

5. **Contrast must survive compression and dark/light feed chrome.** WebP/JPEG compression at share size muddies mid-tone-on-mid-tone. The corpus almost always pairs near-black text (#111-#1a1a1a) with an off-white or light-gray field (attio #f7f8f9, mobbin #F7F5F2, equals #faf7f0), or pure white text on a dark/saturated field (lovable, framer, warp, cash-app green). Avoid gray-on-gray text; brightscout gets away with it only because the type is enormous and embossed.

6. **Off-white beats pure white.** Most light cards use warm off-whites (#f4f2ec, #f7f5f2, #faf7f0) rather than #ffffff, so the card reads as a designed object against the white page/feed background instead of dissolving into it. Dark cards (#0a0a0a-#121212) get the same edge-definition for free.

7. **Give backgrounds texture, not noise.** Flat fields are dressed with a quiet system: blueprint grids and dashed guides (attio, paper, cognition), grain gradients (handhold, lovable's noisy aurora), paper texture (runner, cognition), or a faint crop-mark grid (warp). The texture stays 5-15% contrast so text still dominates; full-strength texture appears only on no-text cards (norgram, p-cv, bakken-baeck).

8. **If you use product UI, use it as a prop, not a screenshot.** Screenshots appear cropped, rounded, tilted, or collaged — phone masonry (mobbin), floating glass panes (twelvelabs), a window card over collage (granola), an app peek along the bottom edge (notion, lovable's chat input bar). Never a legible full-app screenshot; UI at thumbnail size communicates "this is a product," not details.

9. **A logo-only card must earn it with craft.** The no-headline references (dia, dirt, magma, ingamana, ribbit, new-genre) work because the mark itself is treated as art: glass 3D, custom letterforms, surrounded characters, full-bleed render. A plain flat logo centered on a flat field is the weakest possible card — either art-direct the mark or add a headline.

10. **Color-block splits need a hard commitment.** Cash-app devotes a full half to flat brand green with only a tiny corner logo, and puck fills a flat blue field edge to edge. Half-hearted brand color (a thin stripe, a pale tint) reads as template; either the brand color owns 40%+ of the frame or it stays an accent.

11. **Two type sizes, maximum three.** References use one display size plus one small utility size (tagline, wordmark). Attio's two-tone weight shift (black "Customer" over gray "Relationship Magic.") shows how to add hierarchy without adding a size. Mixed serif-display-plus-sans-caption (runner, equals, sketch, infinite-machine) is the corpus's favorite way to signal editorial/premium.

12. **Respect a safe margin of ~60-80px on all sides.** Every text and logo element in the references sits well inside the frame; only deliberate full-bleed art (photos, textures, cropped giant type like flim) touches edges. Platforms crop 1200×630 to 1.91:1, 2:1, and square variants — keep the message inside the center 80%.

## How to navigate

- Catalog: `profiles/og.md` — one line per image with composition notes, `style:` tags, and a 2-3 color `palette:` in hex.
- Images: `media/og-images/<filename>` — filenames match the catalog entries (e.g. `media/og-images/attio.webp`).
- Workflow: grep `profiles/og.md` for style tags (`minimal`, `3d-render`, `photo-collage`, `editorial-serif`, `dark-tech`, etc.) to shortlist, then Read the actual images before committing to a direction.

## Best references

- **attio.webp** — the canonical B2B SaaS card: two-tone headline lower-left, blueprint motif upper-right, wordmark bottom-right; copy this structure when in doubt.
- **mobbin.webp** — text-left / screenshot-masonry-right split with a huge black headline on off-white; the cleanest "product gallery" card.
- **lovable.webp** — dark gradient-glow card with centered lockup, one subtitle, and a product-UI teaser bar; model for AI-product launches.
- **cash-app.webp** — brutal flat brand-color half plus one photo card and a tiny corner logo; proof that color commitment beats copy.
- **runner.webp** — serif statement bottom-left on paper texture with vintage collage right; the editorial/print-flavored template.
- **cosmos.webp** — centered mark orbited by tiny photo thumbnails on warm off-white; minimal centerpiece done with warmth.
- **equals.webp** — serif headline plus pastel spreadsheet-cell strips; shows how to encode the product's domain as a decorative motif.
- **dia.webp** — the logo-only card done right: gradient glyph, serif wordmark, generous whitespace on light gray.
- **shopify-editions.webp** — high-concept campaign card (classical painting remix, keyline-boxed headline); reference for one-off event/launch cards.
- **framer.webp** — dark dense screenshot grid with the logo dead center; the showcase/portfolio pattern at maximum density.
