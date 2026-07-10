# Product Page Playbook
> Coverage: 48 examples from corpus (analyzed 20)

## Anatomy

Ordered skeleton observed across the sample. A "product" page is a feature-focused landing page for one product line or capability — deeper than the homepage, shallower than docs.

1. **Hero** — 100%. Eyebrow/category label ("MULTICHANNEL SEQUENCES" amplemarket, "PAYMENTS" outseta, "Rally for Product Updates" rally-space) + outcome-phrased H1 + 1–2 sentence subcopy + 1–2 CTAs.
   - Split hero with product visual right: ~60% (front, spellbook, brainfishai, monad, oysterhr, gitbook, amplemarket, clay-com)
   - Centered text-only hero: ~25% (cap, equals, rally-space, craft-do)
   - Hero with inline email-capture field instead of button: amplemarket
2. **Trust strip** directly after hero — ~60%. Logo bar (cap, clay-com, gitbook, oysterhr, brainfishai, default, spellbook has it inside the hero) or a single large customer quote with photo (amplemarket). Equals uses a "startups replacing Excel" logo row.
3. **Problem/context section** — ~25%. Pain-point cards ("Does this sound familiar?" front), before/after toggle ("without Brainfish" brainfishai), "From stoneage sales to multichannel mastery" (amplemarket).
4. **Core feature walkthrough** — ~85%. The body of the page. Two dominant shapes:
   - Alternating (zigzag) text + product-screenshot rows, 3–6 sections: amplemarket, front, craft-do, monad, oysterhr, penpot, hydra, outseta (~65%)
   - Numbered/stepped sequence: brainfishai (01–05 cards), prismic (steps 1–4), hydra (Data In → Transform → Data Out → Govern → Report pipeline chips), equals (Query/Analyze/Report tab-labeled sections) (~25%)
5. **Secondary feature grid / bento** — ~65%. 3–6 compact cards mopping up features that don't deserve a full section (penpot "Discover more features", prismic "Features that work for you", rally-space dark storytelling-kit cards, outseta 2×3 grids under each screenshot, save-day "But wait, there are more", spellbook "More spells to explore").
6. **Social proof block** — ~75%. Quote carousel (front), customer video cards (prismic, equals), photo-card team quotes (brainfishai), interleaved single quotes between feature rows (craft-do), full case-study band with metrics ("3x enrichment coverage" clay-com).
7. **FAQ accordion** — ~35% (amplemarket, common, default, equals, outseta, save-day).
8. **Final CTA band** — 100%. Full-width, visually distinct (sky-photo card cap, dark band amplemarket, giant yellow button listenup, illustrated landscape clay-com). Repeats the hero CTA verbatim.
9. **Mega-footer** — 100%. ~30% add a giant decorative wordmark above/inside the footer (brainfishai, common, default, spellbook, oysterhr, clay-com).

## Patterns that work

- **Outcome headline + category eyebrow.** Every strong hero names the job, not the feature list: "Route leads, meetings, and accounts to the right rep, every single time" (default), "Reduce Customer Effort with Built-In Contextual Help" (brainfishai), "Turn members into owners" (common). The eyebrow carries the product-taxonomy label so the H1 doesn't have to.
- **Real product UI in every feature section.** amplemarket, front, outseta, oysterhr, penpot, and hydra pair each claim with an actual (often simplified/redrawn) screenshot cropped to the one relevant panel. Simplified UI vignettes with fake data read better at small size than raw screenshots.
- **Per-feature proof.** brainfishai attaches a customer logo + case-study link + metric to each of its 5 numbered features ("92% of Smokeball users answered queries without escalation"). clay-com anchors the page with one deep case study (Anthropic, "3x enrichment coverage," "100+ users") using big stat typography.
- **Process-as-diagram.** hydra turns its pipeline into 5 clickable chips with an arrow plus a boxes-and-arrows dbt diagram on an orange band; prismic uses a 4-step numbered row with the active step highlighted. Works when the product is a workflow.
- **Interleaved testimonials as pacing.** craft-do drops a one-line italic serif quote with avatar between every two feature sections — social proof doubles as visual rest.
- **Capability index for a broad platform.** front ends with "Explore all of Front's capabilities": a dark band of 10 title+one-liner links to sub-pages. Keeps the page focused while exposing the full surface area.
- **Integration-first product pages get one card per integration.** listenup structures the entire page as full-width cards (Intercom, Slack, Zoom, Teams, API, Zapier), each with its own "Connect" button and a mini flow diagram, ending with "Request an integration."
- **CTA echo throughout.** amplemarket repeats the email-capture + "Get a demo" combo three times (hero, mid, final band); monad puts "Try Monad free" in nav, hero, mid-section, and footer. The final CTA always restates the free/no-credit-card promise (craft-do "Start for free. No credit card required.", save-day "Free to use. No credit card required.").
- **Personality moments in otherwise-corporate layouts.** save-day's mascot narrates ("Let's see how I actually do it"), cap's hand-script "you're in great company" over the logo bar, oysterhr's chunky yellow/teal color blocks. One or two moments, not the whole page.

## Variants by style

- **Light minimal / neutral SaaS** (amplemarket, front, cap, outseta, listenup, default): white or bone background, one accent color, generous whitespace, zigzag screenshot sections. Proof is logos + quotes. default and outseta punch up an otherwise plain layout with heavily saturated screenshot backdrops (green/orange/pink/blue cards framing gray UI). cap goes almost monochrome with soft 3D renders — the weakest at communicating actual product.
- **Dark tech** (equals, gitbook, hydra, prismic, spellbook): near-black canvas, one hot accent (terminal green equals, orange hydra, orange-red spellbook), aurora/gradient glows behind screenshots (gitbook). Screenshots render as light cards popping off the dark field or as dark UI with accent highlights. Feature grids use hairline-bordered cells. Dark pages skip playful illustration; hydra substitutes a single monochrome line-art hero illustration (elephant) as its one flourish.
- **Colorful / playful** (brainfishai, clay-com, oysterhr, penpot, save-day, rally-space): full-bleed color blocks per section (pink→white→salmon→mint brainfishai; yellow/teal oysterhr; yellow/brown save-day), mascots or 3D scenes (clay-com's landscape final CTA), rounded cards with visible borders. Color changes are the section separators — no hairlines needed.
- **Editorial / serif** (monad, craft-do, common, equals headline): serif display headlines with mono or small-caps supporting text (monad pairs serif H1s with monospace body and button labels), abstract line-drawn diagrams instead of screenshots, hairline horizontal rules between sections, big whitespace. common goes full Swiss-brutalist: mono labels, gradient blobs, giant footer wordmark. This style trades screenshot density for atmosphere — works only when paired with at least one concrete UI shot (monad's connect-form vignette).

## Anti-patterns

- **Abstract renders instead of product.** cap's feature cards show 3D shields, clouds, and orbs where every competitor shows UI; after reading you still don't know what the app looks like. common has the same issue — gradient blobs where screenshots should be. If the visual could belong to any product, replace it.
- **No pricing tables.** 19 of 20 pages defer pricing to a dedicated page; only craft-do embeds a simple 2-card Free/Plus block. Don't build a full pricing matrix on a product page.
- **No orphan heroes.** Zero pages have a hero without an immediate CTA, and none use "Learn more" as the sole hero CTA — primary is always try/demo/start.
- **Uniform section rhythm without breaks.** The weaker stretches (default's very long mid-page) survive only because colored cards alternate hues; pages that alternate background color or insert a quote/stat band every 2–3 sections (craft-do, brainfishai, amplemarket) read far better than an unbroken white scroll.
- **Feature sections with paragraph walls.** Corpus body copy is 1–3 sentences plus optional bolded lead-in (front bolds the claim, then explains). Nothing longer appears anywhere in the sample.
- **Skipping the final CTA band.** Never happens in the corpus — every page closes the loop before the footer, usually with a visual change-up (photo, illustration, dark band).
- **Generic stock photography.** Absent from all 20 pages. People appear only as real customers (brainfishai's team photo cards, prismic's developer videos) or inside product screenshots.

## Checklist

1. Write the hero as eyebrow (product/category label) + outcome H1 (job-to-be-done, not feature name) + 1–2 sentence subcopy + primary CTA ("Try/Start free" or "Book demo") with optional secondary; put a cropped product visual beside or under it.
2. Place a trust element within one viewport of the hero: logo bar (5–10 grayscale logos) or one big customer quote with name/photo/company.
3. Build 3–6 core feature sections, each = short claim headline + 1–3 sentences + real UI vignette (simplified screenshot with believable data, cropped to the relevant panel). Alternate text left/right, or number the steps if the product is a sequential workflow.
4. Attach proof to features where you have it: a metric, a customer logo, or a case-study link per section (brainfishai pattern), or one deep case-study band with oversized stats (clay-com pattern).
5. Sweep remaining features into a compact 3–6 card grid with icon + title + two lines each; link out ("Full features list") instead of expanding the page.
6. Break the scroll rhythm every 2–3 sections: alternate background colors, insert a one-line testimonial, or drop a stat/quote band.
7. Add a FAQ accordion (4–7 questions) if the product needs objection-handling (pricing model, data privacy, migration); otherwise skip.
8. Close with a full-width CTA band that visually breaks from the page (dark, photographic, or illustrated), restates the hero CTA, and adds the friction-remover line ("Free. No credit card required.").
9. Keep global nav; no pricing table on the page; no stock photos; every visual must be product UI, a diagram of the workflow, or a real customer.
10. If the page is integration-centric, use one full-width card per integration with its own connect CTA and a "Request an integration" escape hatch (listenup pattern).

## Best references

- **front** — canonical B2B structure: pain cards → bold value restatement → 3 zigzag feature sections → app-icon integration cloud → capability link index → quote carousel.
- **brainfishai** — numbered feature cards each carrying a customer logo, metric, and case-study link; masterclass in per-feature proof and color-blocked pacing.
- **clay-com** — bright color-blocked screenshots, one deep case study with giant stats, illustrated final CTA scene; playful without losing density.
- **monad** — editorial serif + mono system proving a product page can be quiet: three sections, hairline rules, one UI vignette, gradient accents.
- **hydra** — workflow-as-diagram: pipeline chips, boxes-and-arrows dbt flow on an orange band, strict black/orange monochrome.
- **spellbook** — dark-tech hero with annotated product card, alternating orange/dark bands, 3-card feature row, giant footer wordmark.
- **rally-space** — chunky display type, mono eyebrow labels, video-first visuals, dark bento for the long tail of features.
- **craft-do** — interleaved serif testimonials as pacing, warm color-blocked hero and CTA, the one tasteful embedded pricing block in the corpus.
