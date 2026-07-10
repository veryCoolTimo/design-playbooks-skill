# Websites Domain Playbook
> Coverage: 407 site profiles from corpus

## When to use this corpus

- Building any marketing or product website page — home, pricing, product, blog, about — where you want the structure and component grammar of real shipped sites instead of invented layouts.
- Choosing a visual direction before writing code: the nine style playbooks (minimal-light, dark-tech, dark-neon, colorful-playful, illustration, big-type, elegant-serif, photo-driven, gradient-mesh) each define a complete, internally consistent system with palette formulas and do/don't rules.
- Executing a brand-inspired brief ("make it feel like Stripe/Linear/Notion") — site profiles capture exact hex values, type weights, radius systems, and signature moves, so you borrow the system rather than the logo.
- Grounding concrete decisions — button radius, canvas hex, section rhythm, hero anatomy — in evidence from 407 analyzed sites rather than defaults.
- Sanity-checking a design in progress against documented anti-patterns (stock photos, carousel testimonials, multi-hue CTAs, shadow-heavy cards).

## Craft rules

1. **Commit to one canvas and hold it site-wide.** Every strong profile picks a single ground — pure white (notion #FFFFFF), off-white (vercel #fafafa), warm cream (clay-com #F3EFE7), near-black (linear.app #010102, mintlify #0A0A0A) — and never swaps temperature mid-page. Cream sites reserve pure white for cards; dark sites never use pure #000.
2. **Give exactly one color a monopoly on the primary CTA.** Either a single saturated hue (stripe indigo #533afd, supabase green #3ecf8e, linear lavender #5e6ad2) or deliberate no-color — black/white pills (figma, notion, clay-com, aave, mintlify). Never a second button hue, never gradient-filled buttons.
3. **Ink is never pure black.** Profiles tint it: deep navy #0d253d (stripe), warm #17170F, neutral #171717 (vercel), #191918 (notion). Body copy drops to a muted gray while headings hold full ink.
4. **Build depth with hairlines and surface steps, not shadows.** The corpus-wide elevation model is 1px low-contrast borders plus tint/lightness shifts (linear's charcoal ladder #0f1011→#141516, vercel's white-on-#fafafa). Soft shadows are permitted only under floating product mockups; glows, glassmorphism, and heavy drop shadows appear almost nowhere.
5. **The product is the imagery.** Real UI screenshots in browser/phone chrome, code panels, or crafted 3D/illustration — never stock photography. Dev products show syntax-highlighted code at section scale (supabase, vercel); SaaS shows a legible dashboard in the first viewport.
6. **Use a real type scale from one family.** One grotesque covers 80px display down to 12px microcopy, differentiated by size and weight. Pick a weight school and stay in it: bold-tight (700–800, negative tracking) or calm (300–600 with size doing the work — stripe's 300 display at -1.4px, linear's 600 at -3px). Track display sizes proportionally negative (~4% of size); monospace or italic-serif is a single seasoning, not a second base.
7. **Keep the radius system two-tier and consistent.** One radius for interactive elements, a larger one for cards/panels — pill buttons + 12–16px cards (stripe, figma, clay-com) or small 4–8px buttons + 8–14px cards (notion, supabase, linear). Never mix schools on one page (vercel's pill-vs-6px split is contextual, not random).
8. **Follow the page playbooks' anatomy before improvising.** A home page is nav → hero (H1 ≤9 words, 1–2 CTAs) → product visual → logo bar with kicker → feature bento or alternating rows → oversized proof (giant stat or pull-quote) → final CTA band repeating the hero promise → fat footer. Skipping the closing CTA band is the most common way pages end weakly.
9. **Pace long scrolls with surface alternation.** Sections shift white ↔ tint ↔ one dark or saturated band (figma's pastel bands, clay-com's jewel-tone bands, amplemarket's cream↔black); vertical padding runs 96px minimum, often 150–250px. Dark contrast bands work because they are singular — one or two per page.
10. **Quarantine accent color away from chrome.** Pastels and jewel tones live in section backgrounds, card fills, badges, headline highlight words, and illustration (figma, clay-com, notion's per-product theming) — never in body text, never in buttons, never scattered per-section without a system.
11. **Make numbers and quotes the proof, oversized.** One giant stat (aave's live $20.8B TVL numeral as the de facto hero) or one display-size attributed pull-quote beats ten claims; testimonials are stacked or gridded, never carousels.
12. **Keep the nav slim and quiet.** One row: logo left, ≤6 links, one filled CTA right; floating pill variants (mintlify, clay-com) are fine, mega-heroes and desktop hamburgers are not.

## How to navigate

- **Pages playbooks** — `/Users/timo/.claude/design-library/playbooks/pages/<type>.md` for the anatomy, patterns, and checklist of a page type: `home`, `pricing`, `product`, `features`, `blog`, `about`, `company`, `solutions`, `use-cases`, `resources`, `misc`. Start here when building a specific page.
- **Styles playbooks** — `/Users/timo/.claude/design-library/playbooks/styles/<style>.md` for the full system of a visual direction. Style codes in profile frontmatter map to files: ML → `minimal-light`, DT → `dark-tech`, DN → `dark-neon`, CP → `colorful-playful`, IL → `illustration`, BT → `big-type`, EL → `elegant-serif`, PH → `photo-driven`, GR → `gradient-mesh`. Start here when choosing or executing a style.
- **Site profiles** — `/Users/timo/.claude/design-library/profiles/sites/<slug>.md` for one brand's exact palette (hex), typography, radius, layout, components, signature moves, and do/don't rules. Frontmatter lists `style` (code above) and `pages` covered. Use for brand-inspired work or to see how a style playbook cashes out on a real site.
- **Screenshots** — `/Users/timo/.claude/design-library/media/<slug>/<page>/` holds the captured screenshots per site and page. Look at them when a profile description isn't enough to settle a layout question.
- **Workflow**: page playbook for structure → style playbook for the system → 2–3 site profiles of that style for concrete values → screenshots to verify.

## Best references

- **stripe** (GR) — gradient-mesh hero as the entire depth system over a white canvas; weight-300 display with negative tracking, tnum on every numeral; the fintech-polish benchmark.
- **linear.app** (DT) — the darkest, strictest system: #010102 canvas, five-step charcoal surface ladder, one lavender accent, product screenshots framing every section; how to do dark without glow.
- **supabase** (DT) — one green on grayscale, code panels as marketing, wireframe-diagram bento cards, monospace micro-labels; the dense developer-terminal aesthetic.
- **vercel** (ML) — monochrome discipline: #171717 does headings, CTAs, and borders; chroma exists only in the hero mesh; pill-vs-square button split signals marketing vs app chrome.
- **notion** (ML) — black-on-white with warm-gray #F6F5F4 flat cards, ink-doodle illustrations, per-product accent theming on a monochrome shell; the friendly-minimal SaaS baseline.
- **figma** (CP) — black pill buttons on white with full-bleed opaque pastel bands (lavender, lime, salmon) carrying all the color; restrained chrome, exuberant content.
- **clay-com** (IL) — warm cream canvas, jewel-tone full-bleed bands hosting real spreadsheet UI, 3D topiary-garden footer and squiggle ribbons; playful illustration without losing enterprise structure.
- **raycast** (DN) — near-black with rainbow-gradient panels and tinted headline words; neutral gray chrome so the glow owns every accent, including one halo'd climactic CTA per page.
- **aave** (DN) — dark navy with an aurora gradient hero and a giant live stat as the real hero; small white pill CTAs, matte flat cards; selling infrastructure with proof, not typography tricks.
- **mintlify** (DT) — atmospheric painterly backdrops fading into near-black, everything-is-a-pill chrome, brand green used homeopathically, perfectly mirrored dark/light themes.
