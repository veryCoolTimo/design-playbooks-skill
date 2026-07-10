# Minimal Light Style Playbook
> Coverage: 135 sites from corpus (analyzed 60)

## Essence
Minimal Light is a light-canvas system where near-black type and whitespace do almost all the work, and color is rationed to a single job — usually one CTA hue or one accent moment per viewport. The canvas is rarely a "background": it is the identity, ranging from pure white (aside, bento, cycleapp) through cool gray (aninix, cluely, miro) to warm cream/paper (amplemarket, replicate, index-app, stableaudio). Surfaces are flat: separation comes from hairline borders, tint shifts, and fill contrast rather than drop shadows or gradients on chrome. The product itself — real screenshots, browser/phone mockups, embedded UI fragments — is the imagery; illustration and photography are exceptions, not defaults. Contrast beats arrive as deliberate full-bleed dark or saturated bands (one or two per page), never as ambient darkness.

## Palette formula
- **Canvas** is one committed neutral, held across the whole page. Three families: pure/near white (#FFFFFF–#FCFDF8), cool light gray (#EFEFEF–#F4F6FA), and warm cream/ecru (#F1F0E9–#E8E5DA). Warm-canvas sites (amplemarket, replicate, index-app, gopano, stableaudio) explicitly forbid pure white; white becomes the *card* color that reads as elevated.
- **Ink** is near-black but almost never #000 — it is tinted toward the canvas temperature: warm charcoal (#17170F amplemarket, #25221E index-app), cool navy-charcoal (#191E2C cortexdao, #22274c fold-money), or neutral (#1A1A1A). Body copy frequently drops to a muted gray (#5A6472 cluely, #6B7280 june) while headings hold full ink.
- **Primary** is either (a) the ink itself — solid black/charcoal CTAs (amplemarket, aninix, ctrl nav, geniestudio, huddle-works, hellotime, podscan, shopify, minimax) — or (b) exactly one saturated hue with a monopoly on action: indigo #5755F4 (default), royal blue #2A44E8 (cycleapp), blue #0052ff (coinbase), green #17A672 (cortexdao), evergreen #17594F (lattice), orange-red #ef3701 (browserbase), mint #2EE5A8 (penpot), periwinkle #8F80F3 (aave-recent).
- **Accents** are quarantined: pastel card fills, headline highlight words, badges, and illustration — never buttons. Candy pastels (amplemarket, ctrl, equals-app, lottielab), one dark inversion band (#151515 miro, #0B0B33 june, #202020 default), or per-product color coding (minimax).
- Zero-hue is a legitimate pole: podscan, harry-atkins, becane-paris, cathy-dolle, orior-ai run pure grayscale and get "color" from value contrast and imagery alone.

Concrete example palettes:
1. **White + one blue** — canvas #FFFFFF, ink #17171A, primary #2A44E8, accents #FED230/#2BCB77/#FCB8FC decorative only (cycleapp; kin: june #5E5CE6, dock #4466FF, relate-so #2563EB).
2. **Cream + black CTA + pastels** — canvas #F1F0E9, ink #17170F, primary #121212, pastel accents #F5EC6E/#F6CCE8/#CDBFF7/#B9E7CF (amplemarket; kin: ctrl #F4F3EE with green #35C838).
3. **Warm paper duotone + one orange word** — canvas #F5F3EF, ink #25221E, primary charcoal #2B2723, accent #E8552B rationed to one moment per screen (index-app; kin: replicate #f9f7f3 with #ea2804).
4. **Cool gray + monochrome + delegated color** — canvas #F0F0F2, ink/primary #17171B, all saturation inside showcased work (aninix; kin: miro #EFEFEF with one purple word #9C33FA).
5. **Pale tinted canvas + single soft hue** — canvas #F2EFFB lavender, ink #1B1B1F, primary periwinkle #8F80F3 doing all accent work (aave-recent; kin: cluely #EDEFF6 with #4E9EFF).
6. **Grayscale absolute** — canvas #ffffff, ink #1a1a1a, primary #111111, grays #f4f4f5/#e4e4e7; "highlight" = inverting a card or section to black (podscan; kin: becane-paris #f4f4f4/#111111).

## Typography formula
- **One family does everything.** The dominant move is a single grotesque covering display, body, nav, and buttons, differentiated only by size and weight (amplemarket, default, fold-money, huddle-works, era-app, minimax "DM Sans covers 80px hero to 12px microcopy"). Adding a second family is a deliberate flourish, not a baseline.
- **The family is a grotesque**: geometric/neo-grotesque of the Inter / Aeonik / Neue Haas / Helvetica Now / Graphik class (june, cycleapp, ctrl, lattice, fabric-so, obviously). Friendlier products round it (fold-money Cera-like, gopano, lottielab, granola, dock, portrait).
- **Weight splits into two schools.** Bold-tight: 700–800 display with slightly negative tracking (cycleapp, planpoint "ultra-bold ~80-120px", hellotime, replicate 128px at line-height 1.0). Calm-institution: 400–500 display where size, not weight, is the hierarchy (coinbase weight-400 with -1 to -2px tracking, airtable "never heavier than 500", merlin, paper-design, shopify-design). Pick one; don't drift between them.
- **Body** is the same family at regular weight, small sizes (13–16px), generous line-height, often muted gray instead of full ink (cluely, june, seline, index-app).
- **Licensed accent voices**: monospace for labels/nav/code in developer-facing sites (browserbase, equals-app, multiparty, icebug, replicate JetBrains Mono); one italic-serif or script word inside a grotesque headline (aave-recent, portrait, privy, buymeacoffee); all-lowercase everywhere (paper-design). Each is a single seasoning, never the base.
- **Headline emphasis tricks** recur constantly: one phrase flipped to the brand hue (june, cycleapp, penpot, gopano), gray/ink two-tone (granola dark green vs silver gray, buymeacoffee second line gray), one italicized word (privy, podscan), inline badge/emoji embedded mid-headline (hellotime, ctrl, geniestudio, merlin).

## Layout & shape
- **Nav**: slim single row — logo left, few text links center, one filled CTA right (default, cycleapp, lattice, shopify). Variants: floating detached pill bar (miro, granola, portrait, multiparty) or near-empty nav of wordmark + one button (campsite-design, heyquin, fabric-so, ready-so).
- **Hero**: most often a centered stack — optional eyebrow/badge, 2-line headline, one-line gray subhead, 1–2 CTAs, then an oversized product mockup bleeding below (aave-recent, bento, cycleapp, rework d, podscan). Left-aligned heroes pair text with a mockup on the right (privy, cortexdao, era-app, shopify, sketch).
- **Section rhythm** = surface alternation, not dividers: white ↔ tint ↔ one dark band (airtable "no two consecutive sections share a mode", amplemarket cream↔black, june lavender panels, dock pastel panels, era-app stacked pastel bands). Vertical padding is huge — 96px minimum, often 150–250px (seline, aside); "one idea per screen" is the norm (fabric-so, orior-ai).
- **Containers**: content column ~1100–1280px max, text columns much narrower (~640–900px). Full-width rounded section shells at 24–40px radius are a recurring premium move (aave-recent, dock, index-app, huddle-works).
- **Radius system is two-tier**: interactive elements at one radius, containers at a bigger one. Pill buttons + 16–24px cards is the most common pairing (cycleapp, replicate, lattice, coinbase pill + 24px). A tighter school uses 4–10px buttons + 8–14px cards (amplemarket, june, hellotime, podscan, privy). A hard-edged minority uses zero radius everywhere (browserbase, becane-paris, harry-atkins, icebug). Never mix schools on one page.
- **Shadows are near-forbidden.** The default elevation model is: hairline 1px borders, flat fills, tint contrast. Soft diffuse shadows are permitted only under floating product mockups (aave-recent, june, fabric-so, ready-so). Hard shadows, glows, and glassmorphism appear in none of the 60 profiles as chrome.
- **Imagery**: real product UI in browser/phone/macOS chrome (aside, cluely, granola, reworkd, dock) or flat pastel mockup cards (huddle-works, era-app). Decorative garnish is small and hand-made: doodle arrows, script annotations, stickers, sparkles (merlin, sketch, amplemarket, geniestudio) — one touch per section.

## Do
1. Commit to one canvas neutral and hold it site-wide; if warm cream (amplemarket #F1F0E9, replicate #f9f7f3), reserve pure white strictly for cards and inputs.
2. Give exactly one color a monopoly on interaction — every CTA is the same fill (cycleapp blue, cortexdao green, lattice evergreen) or the same near-black (aninix, geniestudio, podscan repeat one identical button top-to-bottom).
3. Build depth with hairline 1px borders and tint shifts, not elevation (index-app, june, penpot, hellotime); allow soft diffuse shadow only under floating product mockups.
4. Alternate section surfaces (white/tint/dark) as the pacing device and keep 96px+ vertical padding per band (airtable, default, era-app, shopify).
5. Sell with real product UI — screenshots in browser or phone chrome with believable data — instead of stock art or abstract illustration (dock, reworkd, cluely, fold-money).
6. Use one headline emphasis trick per site and repeat it: brand-hue phrase (june), gray de-emphasis (granola, cluely), italic word (privy), or inline badge (hellotime).
7. Keep the radius system two-tier and consistent: pill or small buttons, one card radius, applied everywhere (minimax "pill everything interactive"; coinbase pill/24px; amplemarket 4-6px/8-14px).
8. Bookend pages with a recurring dark or brand-color closing band that reuses the hero CTA verbatim (amplemarket black band, cycleapp blue banner, lithic orange banner, dock repeats the hero headline).
9. Quarantine playful color to card fills, badges, and illustration — pastel sticky-notes (amplemarket), color-block feature tiles (default, obviously), widget chips (bento).
10. Set body copy small, regular weight, and muted gray, letting size — not boldness — carry hierarchy (coinbase, airtable, paper-design, cluely).

## Don't
1. Don't introduce a second saturated hue for buttons or links — the single-accent discipline is the style's spine (aave-recent, cycleapp, seline, multiparty all forbid it explicitly).
2. Don't add drop shadows, glows, gradients, or glassmorphism to cards and buttons; flat fills + hairlines only (ctrl, default, lithic, hellotime, penpot).
3. Don't mix radius schools — no pill CTA next to a square card system, no 16px button in a 4px system (obviously "no pill buttons"; cycleapp "don't square off buttons").
4. Don't set display type at heavy weight in a calm-weight system, or bold body copy for emphasis (coinbase "don't bold display copy", airtable "never 600-700", replicate "switch family, don't bold").
5. Don't fill whitespace — no extra feature grids, dividers, or decoration between sections; the empty gaps are the rhythm (bento, aninix, seline, ragged-edge "if a band feels empty, that is intended").
6. Don't paint whole sections in the accent color outside the one designated banner/band (default "accents are backgrounds only", dock "don't saturate the tints", lithic "orange is banner-only").
7. Don't use stock photography or generic illustration as hero art; imagery must be product UI or curated work (reworkd, obviously, replicate, shopify-design).
8. Don't stack multiple dark sections — the dark band works because it is singular, one or two per page (june "the navy block works because it is a single contrast moment", lottielab, merlin).
9. Don't color body text or scatter accents into paragraphs; emphasis in prose is underline or weight-neutral highlight, prose stays ink/gray (hellotime, lottielab, obviously).
10. Don't swap the canvas temperature mid-site — no pure-white sections on a cream site, no cream cards on a cool-gray site (replicate "don't swap cream for white — it flattens the identity"; gopano; miro "don't use pure white as the page background").

## Canonical examples
- **cycleapp** — the archetype: pure white, one royal blue with a total CTA monopoly, pill buttons, hairline flat cards, closing brand banner.
- **amplemarket** — warm-cream pole: ecru canvas, black small-radius CTAs, pastel stat tiles, cream↔black band alternation.
- **june** — screenshot-driven SaaS baseline: Inter, indigo highlight phrase, lavender panels, one navy contrast moment.
- **coinbase** — calm-institution typography: weight-400 display, pill-everything, one blue rationed per band.
- **airtable** — editorial-white pole: weight-capped display type, near-black CTA, color arrives only as full-bleed color-block cards.
- **aave-recent** — soft tinted-canvas variant: lavender canvas, single periwinkle, giant rounded section shells, italic-serif accent words.
- **podscan** — grayscale extreme: zero hue anywhere; emphasis achieved by inverting sections and cards to black.
- **replicate** — cream developer zine: hot orange as a "rubber stamp" one-per-viewport, 128px display at line-height 1.0, dark mono code wells.
- **miro** — gray-canvas product-as-background: dot-grid whiteboard metaphor, one purple accent word, hard light/dark alternation.
- **browserbase** — hard-edged engineering dialect: zero radius, mono labels, one orange-red CTA, flat isometric illustration.
- **granola** — friendly-rounded pole: pastel green pill CTA, two-tone green/gray headlines, ambient peach-lime washes, macOS mockups.
- **harry-atkins** — chrome-less minimum: no buttons at all, hairline rules and gray-value steps as the entire hierarchy system.
