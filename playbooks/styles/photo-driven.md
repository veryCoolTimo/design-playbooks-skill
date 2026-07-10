# Photography-Driven Style Playbook
> Coverage: 16 sites from corpus (analyzed 16)

## Essence
Photography carries all the emotion and nearly all the color; the interface deliberately recedes into ink, white, and at most one rationed accent hue. Pages are stacks of full-bleed bands — cinematic photo sections alternating with quiet white (or cream, or near-black) reading bands — and the surface flip itself is the section divider, not borders or rules. Depth is almost outlawed: cards are flat, shadows are rare-to-forbidden, and elevation comes from band polarity (white/black inversion at renault, vodafone, apple) or hairlines. The style splits into two typographic moods sharing one skin: the "shout" camp burns enormous uppercase display type straight onto imagery (spacex, nike, vodafone), while the "whisper" camp keeps headlines modest so listing/product photos own the hierarchy (airbnb, tesla, pinterest). Either way, the UI is chrome for a photo gallery, and every pixel of decorative work belongs to the image.

## Palette formula
Canvas is white (12 of 16) or a warm cream (superhuman #F5F3EE, usedrop #F4EFE6) — spacex alone inverts to pure black. Ink is near-black but rarely pure: #222222 (airbnb), #1d1d1f (apple), #111111 (nike, tedy), #33332e (pinterest), #25282b (vodafone), #393C41 (tesla). The primary is either exactly one saturated brand hue spent almost exclusively on CTAs and logo (roughly one accent moment per viewport), or black itself when the brand refuses color (nike, runwayml, createanything, usedrop, spacex). Accents are neutrals (#f5f5f5-family grays for photo backdrops and secondary buttons) plus, in the "candy" sub-branch, pastel band fills that never touch buttons (tedy, goodnotes, usedrop). Semantic color is confined to meaning: nike's red exists only as sale-price text; pinterest bans blue links.

Example palettes:
- **airbnb** — canvas #ffffff · ink #222222 · primary #ff385c · neutrals #f7f7f7 / #dddddd / #6a6a6a (one hot red on a 90%-white page)
- **apple** — canvas #ffffff · ink #1d1d1f · primary #0066cc · surfaces #f5f5f7 / #272729 / #000000 (blue is the only interactive signal; tiles flip light/dark)
- **spacex** — canvas #000000 · ink #ffffff · no accent · #f0f0fa fill only on shop cards (all other color comes from photographs)
- **vodafone** — canvas #ffffff · ink #25282b · primary #e60000 · grays #f2f2f2 / #7e7e7e / #bebebe (red spent only on CTA pills and the logo orb)
- **tesla** — canvas #FFFFFF · ink #393C41 · primary #3E6AE1 · neutrals #171A20 / #F4F4F4 / #EEEEEE (one blue in the entire system)
- **tedy** — canvas #FFFFFF · ink #111111 · primary #F5117B · pastel bands #FBD9E6 / #DCC8F5 / #CDEAF0 / #FBF0D0 (hot magenta cuts through pastels; the candy sub-branch)

## Typography formula
One family does nearly everything — a proprietary or neutral grotesque (Airbnb Cereal, SF Pro at apple, NouvelR at renault, Universal Sans at tesla, Pin Sans at pinterest, D-DIN at spacex, abcNormal at runwayml), with the weight ladder kept short and disciplined: 400/700 only (renault), 400/500 with 500 max (tesla), 300/400/600/700 with 500 banned (apple), or a single 400 across the whole hierarchy (runwayml). Two display registers recur:

1. **The shout**: massive uppercase over photography — 96px Futura at 0.9 leading (nike), 80px D-DIN-Bold with wide positive tracking (spacex), 126–144px weight-800 with -1px tracking (vodafone). Line-height crushes to 0.9–0.95; tracking is either tight-negative or deliberately wide-positive, never default.
2. **The whisper**: modest mid-weight heads that defer to imagery — 28px max at 500–700 (airbnb), 40px/500 cap (tesla), semibold 600 with -0.28 to -0.37px tracking, never 700 (apple), regular-weight 36–48px at -0.9 to -1.2px (runwayml).

The editorial sub-branch adds one high-contrast display serif for hero/marquee moments only, always paired with a grotesque for everything else: italic-serif wordmark collision (createanything), edge-bleeding serif mastheads with italic connector words (usedrop), serif/grotesque headline duet (tedy). Body is always the grotesque: 14–17px, 1.47–1.7 leading (apple's 17px/1.47; spacex's 16px/1.5–1.7). Pinterest jumps 70px display straight to 16px body with no middle tier — extreme size contrast replaces weight games.

## Layout & shape
- **Full-bleed band stacking** is the master grid: each section is an edge-to-edge surface (photo, white, near-black, or pastel), stacked with zero gap so the color change is the divider — apple, renault, vodafone, spacex, runwayml, superhuman, tedy, goodnotes, usedrop, ecosia. Spacex and tesla push bands to 100vh, one message per screen.
- **Content caps** at ~1280–1440px; prose narrows further (~980px at apple). Section verticals run 48–96px (nike 48px rhythm, apple ~80px, runwayml 64–96px).
- **Photo grids** collapse gutters where marketing sections breathe: 8px masonry gutters at pinterest, 8px product gutters at nike, 16px at airbnb — dense inventory under airy editorial.
- **The image is the card**: zero padding, zero border, zero resting shadow; meta text stacks below in a few small lines (nike, pinterest, airbnb) or the label floats as a white corner pill on the image (pinterest, nike, airbnb badges).
- **Radius splits by brand temperature**: pill buttons dominate (apple, nike, spacex, vodafone 60px, ecosia, runwayml, tedy, goodnotes, createanything, usedrop), while the engineered camp stays tight — tesla 4px, renault 2px, synthesia 4–6px, superhuman 4–8px. Cards run 0px (nike, renault) to 8–16px (airbnb ~14px, pinterest 16px, goodnotes 16–24px); pinterest enforces a strict 16 / 32 / pill vocabulary.
- **Shadows are a scarcity budget**: zero anywhere (spacex, nike, tesla, renault, vodafone, ecosia, usedrop), or exactly one recipe — airbnb's single soft lift on hover/search/dropdowns, apple's lone drop-shadow under product renders, pinterest's modal-only shadow, synthesia's soft frame under hero screenshots.

## Do
- Spend the accent on one moment per viewport: the primary CTA, the logo, maybe a saved-state icon — nothing else (airbnb's Rausch, pinterest's #e60023, vodafone's red, tesla's blue, renault's one yellow element per viewport).
- Divide sections by flipping the full-bleed surface (white → gray → near-black, or photo → white), never by decorative rules or tinted strips (apple, renault, vodafone, runwayml).
- Let the photo be the card: clip the image to the card radius, keep zero padding and no border, stack 2–5 short meta lines below or float a white pill label on the image (nike, pinterest, airbnb).
- Keep one type family across the whole hierarchy and build contrast with size and a two-to-four-step weight ladder (renault 400/700, tesla 400/500, runwayml all-400).
- If headlines sit on photography, commit: uppercase, heavy or condensed, crushed 0.9–0.95 leading, and grade the photo darker for contrast instead of adding a scrim (spacex, nike, vodafone).
- Stage products on a consistent neutral studio backdrop so grids read as one system (nike's #f5f5f5 squares, tesla's transparent PNGs on white).
- Ration elevation to at most one shadow recipe with a named job — product render (apple), hover lift (airbnb), modal (pinterest) — and keep everything else flat on hairlines.
- Use pills as the "this is actionable" cue when the brand is consumer-warm (apple, nike, vodafone, spacex, tedy); use 2–6px corners when it is engineered-precise (tesla, renault, synthesia).
- Anchor secondary structure with 1px hairlines: #dddddd section splits (airbnb), #e7eaf0 grid dividers (runwayml), #f2f2f2 catalogue rows (renault).
- For the editorial sub-branch, let one serif display moment collide with grotesque everything-else, and desaturate people photography to black-and-white (usedrop, createanything, tedy).

## Don't
- Don't introduce a second accent hue — no blue links next to a red brand, no green checks beside a yellow CTA; even semantic color must earn a narrow job (renault, runwayml, pinterest, spacex all ban it outright).
- Don't put shadows, glows, or gradient scrims on cards, buttons, or text; depth belongs to the photograph and to band inversion (tesla, spacex, nike, superhuman, usedrop).
- Don't add gradients as atmosphere — if a section needs mood, use an image (apple: "atmosphere must come from the imagery itself"; goodnotes, ecosia, usedrop all flat-fill).
- Don't pad or frame photos inside cards, force aspect ratios on marketing imagery, or stack chrome between image and viewer (spacex, nike, pinterest).
- Don't inflate quiet-camp headlines with weight or size — airbnb breaks past ~28px/800, apple breaks at 700, tesla breaks past 40px/500; typographic muscle reads wrong when photos carry hierarchy.
- Don't mix radius grammars: pick pill-for-actions + one card radius and hold it; no in-between values (pinterest's 16/32/pill rule, apple's pill/18px/8px split, renault's 2px/0px).
- Don't tint the footer or swap canvas mid-page arbitrarily — band changes are deliberate rhythm, and airbnb's footer stays page-white while renault always closes black.
- Don't replace photography with illustration or abstract 3D — this style's proof layer is real photos, product renders, or genuine screenshots (synthesia, vodafone, createanything).
- Don't run body or supporting copy in the display serif where one exists; serifs are display-only garnish (usedrop, tedy).
- Don't double primary CTAs in one band — one filled (or one ghost) pill per fold, extras demoted to outline/text (spacex's single ghost pill, nike's one black pill per viewport, runwayml's demote-to-ghost rule).

## Canonical examples
- **spacex** — the purest reduction: black canvas, zero accent, one ghost pill per full-viewport photo band, uppercase DIN burned onto ungraded imagery.
- **apple** — light/dark tile stacking as section grammar; one blue, one shadow (under renders), pill = actionable.
- **nike** — 96px uppercase display over campaign photos while product cards are radius-zero, shadow-zero photos on a shared #f5f5f5 studio square.
- **airbnb** — the whisper camp benchmark: 28px-max headlines, one hot red on an all-white page, photo-first cards with a single hover-shadow recipe.
- **tesla** — 100vh gallery-slide sections, two font weights, one blue button, zero elevation; the most subtractive light-canvas example.
- **pinterest** — dense masonry counterpoint: image-is-the-card at 8px gutters, strict 16/32/pill shape law, one exact red.
- **vodafone** — campaign-poster typography: 144px weight-800 uppercase over editorial photos, 300-weight sub-heads, red rationed to pills and the logo orb.
- **renault** — engineered flatness: 2px-corner buttons, square photo tiles, one yellow element per viewport, white/black band inversion as the only depth.
- **runwayml** — monochrome editorial: every CTA the same black pill, all-400 type, gray ladder instead of accents, photo interludes as pacing breaks.
- **superhuman** — the warm-canvas variant: cream base, jewel-tone bands, UI chips composited over dusk photography, hairline-only separation.
- **usedrop** — the editorial sub-branch: edge-bleeding serif mastheads, B&W portraits, cream/black/lavender/chartreuse band stack, bullet-prefixed black pills.
- **tedy** — the candy sub-branch: pastel rounded slabs holding lifestyle photos, one hot-magenta pill against pastels and black, serif/grotesque headline duet.
