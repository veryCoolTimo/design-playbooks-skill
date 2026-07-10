# Use-Cases Page Playbook
> Coverage: 16 examples from corpus (analyzed 16)

## Anatomy

Two archetypes exist in the corpus. **Deep-dive** (one use case per page, ~69%: clay-com, clutch, default, equals, eraser, evervault, fable, liveblocks, modal, synthesia, listenup) and **index/hub** (all use cases listed on one page, ~25%: relayed, viewport, shareup, tome — tome is a hybrid: audience deep-dive that opens with a scenario index). One outlier (usedrop) serves unrelated content at the use-cases URL.

Ordered skeleton for the deep-dive archetype (dominant, build this by default):

1. **Nav with a "Use cases" item** — ~100%. Often a dropdown feeding sibling pages (clay-com, fable, modal, eraser, synthesia).
2. **Hero** — 100%. Eyebrow chip naming the use case or audience ("SALES ENABLEMENT" synthesia, "COLLABORATIVE FORMS" liveblocks, "FABLE FOR MARKETING TEAMS" fable, "Lead lists" clay-com) in ~60%; H1 states the job-to-be-done outcome; 1–2 sentence subhead; primary CTA (+ secondary "Book a demo"/"Browse examples" in ~44%: modal, liveblocks, tome, synthesia). Hero visual: real product UI performing the use case (~56%: clay-com, synthesia, eraser, evervault, default, listenup) vs. thematic illustration (~31%: clutch, fable, modal, relayed).
3. **Social-proof band** — ~44%. Logo row directly under hero (default, equals, liveblocks, synthesia) or testimonial cards (modal puts 3 customer quotes immediately below the fold); eraser places its logo wall mid-page.
4. **Problem framing** — ~25%. "Old way vs. new way" split (clay-com), "The Problem" 3-cell grid + "The Challenge" persona columns (clutch), pain statement with 3 pain cards (synthesia).
5. **Core body: scenario/feature rows** — ~69%. Alternating zig-zag rows, each = one sub-scenario with heading, 2–3 lines of copy, and a product screenshot or content mockup (clay-com ×6, fable ×4, synthesia, modal ×3, equals as numbered steps ×3, listenup as steps 1–6, shareup as stacked audience bands ×7). Per-row eyebrow category labels in fable (SOCIAL MEDIA / PRODUCT MARKETING / PAID ADS) and shareup (MARKETERS / VIDEO EDITORS / HIRING).
6. **Capability/feature grid** — ~50%. Icon grid of 4–7 supporting features after the narrative rows (liveblocks ×6, fable ×6, eraser 3 large + 4 small, clutch "Core Capabilities" ×4, evervault icon trios).
7. **Quantified proof / testimonials** — ~56%. ROI stat cards tied to the use case (synthesia: Xerox +50%, Zoom +90%), highlighted quotes + 4.9/5 rating + G2 badges (equals), full-bleed quote (liveblocks Microsoft, tome, clay-com), video testimonial (eraser).
8. **Examples/templates gallery** — ~31%. Runnable or copyable starting points: eraser diagram examples, modal "Try it out" carousel, liveblocks open-source examples, tome template grid.
9. **FAQ accordion** — ~13% (default, equals).
10. **Cross-links to sibling use cases** — ~38% in body (eraser's ~20-link "See Other Use Cases" index, equals' 3 use-case cards, tome "More use cases" ×3), plus footer use-case lists (modal, fable, liveblocks).
11. **Final CTA band** — ~94%. Usually a contrast flip: dark band on light pages (clay-com, evervault, relayed), giant wordmark footer (equals, default), oversized single button (listenup's full-width yellow "Get started").
12. **Footer**, often repeating the use-case taxonomy as links (modal, fable, liveblocks, equals).

Index archetype skeleton: hero naming the theme ("Make the most of Viewport", "A Space for everyone and any use case." shareup) → one card/row per use case with label chip + title + 1-sentence description + visual + arrow link (viewport, tome's Fundraising/Sales pitches/Microsites list) or illustration couplets (relayed) → final CTA.

## Patterns that work

- **H1 names the outcome or artifact, never the feature.** "Build the best lead lists using any data source you can imagine" (clay-com), "Create training videos your reps won't skip" (synthesia), "Fill out forms, together." (liveblocks), "Ship motion content the brand deserves" (fable). Compare relayed's generic "Use cases" H1 — the weakest hero in the corpus.
- **Show the product doing the use case in the hero.** clay-com embeds a full live-looking lead-list table with enrichment columns; eraser opens with an actual Netflix-style architecture diagram; synthesia embeds the video editor; evervault shows the payment form component. Illustration-only heroes (relayed, clutch) read slower.
- **Break the body into 3–6 sub-scenario zig-zag rows, each with its own screenshot.** clay-com dedicates one row per data source (CRM, Google Maps, SalesNavigator, Chrome Extension, CSV), each on a different pastel background to create rhythm; fable labels each row with an eyebrow channel (SOCIAL MEDIA, PAID ADS); modal alternates checklist + code/terminal/dashboard embeds.
- **Per-row micro-CTAs lower commitment.** clay-com puts "Try free" + "Use a template" under every scenario row instead of relying only on the final band.
- **Numbered walkthroughs fit workflow products.** listenup structures the whole page as Steps 1–6 with hand-annotated screenshots (arrows, handwritten labels pointing at UI); equals numbers its three pillars 1-2-3; synthesia uses a 4-step "see how it works" tabbed module.
- **Frame the problem before the solution.** clay-com's side-by-side "The old way: list building is expensive and disjointed / The new way" comparison; clutch's Problem → Solution → Challenge (per-persona: CISOs, Security Teams) → How We Solve It sequence reads like a sales narrative an SE would give.
- **Tie proof numbers to this use case, not the company.** synthesia's ROI cards (Xerox +50% cost savings, Zoom +90% time savings, each linking to a case study); default embeds a customer stat card inside each scenario chapter; equals highlights quote phrases with a yellow-marker effect and shows a 4.9/5 + G2 badges.
- **Cross-link the taxonomy so no page is a dead end.** eraser's "See Other Use Cases" block lists ~20 sibling pages as scannable links; equals ends with 3 sibling use-case cards; tome closes with "More use cases" cards for other audiences; modal/fable/liveblocks repeat the full use-case list in the footer.
- **Give a runnable starting point.** modal's "Try it out" example carousel (Deploy an OpenAI-compatible LLM service, RAG Chat with PDFs), tome's 8-template grid, liveblocks' open-source example cards, clay-com's "Use a template" buttons.
- **Index pages must be scannable in one pass.** viewport: chip + title + one sentence + screenshot + arrow, three cards, done. tome's index rows (title, 1-line description, thumbnail) let a founder self-select in seconds.

## Variants by style

- **Light minimal SaaS** (synthesia, evervault, clutch, viewport, equals): white ground, single accent (blue/indigo/green), real UI screenshots framed on soft cards, doc-like section headers, generous whitespace. Proof-heavy: badges, ratings, ROI stats live here. Dark contrast band reserved for one enterprise/developer section (evervault "Built for Developers", synthesia Enterprise) and the final CTA.
- **Dark tech** (eraser, modal, liveblocks, fable): near-black ground with one neon accent — lime (modal), yellow (fable), violet/pink (liveblocks). Product artifacts sit on bright white/light cards that pop against the dark ground (eraser's white diagram card, liveblocks' white form). Code snippets, terminals, and dashboards as body visuals (modal). Feature grids use thin-line icons and hairline dividers.
- **Colorful/playful** (default, shareup, clay-com): saturated pastel or gradient card backgrounds that change per scenario section (clay-com's lavender/pink/green/yellow row tints, default's yellow/pink/orange cards inside rounded purple-bordered chapters, shareup's purple-orange gradients and phone collages). 3D blobs/mascots (clay-com). Section = big rounded container acting as a chapter.
- **Editorial dark / gallery** (tome, usedrop): oversized display type, thumbnail-driven lists, magazine pacing, full-bleed imagery, yellow or lilac accent cards. usedrop adds serif marquee headlines and black-and-white photography (though its /use-cases URL actually serves a team page — style reference only).
- **Hand-drawn light** (relayed, listenup): line-doodle illustrations (relayed) or screenshot annotations with handwritten arrows and labels (listenup), conversational second-person copy ("You should do more user interviews. And you know it."). Works for approachable, human-centric tools; listenup pairs it with real UI, relayed doesn't and suffers for it.

## Anti-patterns

- **Generic "Use cases" as the H1** (relayed). Every strong page leads with the outcome; the index label belongs in the eyebrow (viewport does exactly this: eyebrow "USE CASES", H1 "Make the most of Viewport").
- **Illustration-only scenario rows with zero product evidence** (relayed: six doodle rows, no screenshots, no per-row CTAs, no social proof). The page describes concepts instead of demonstrating capability — nothing on it could not be claimed by a competitor.
- **Taxonomy drift: a /use-cases URL serving unrelated content** (usedrop's page is a "Meet the team" page). Breaks nav expectations and wastes the intent of a high-purchase-intent visitor.
- **No social proof anywhere on the page** (relayed, viewport, listenup carry no logos, quotes, or numbers) — conspicuously absent versus the 56% of the corpus that anchors the use case with named customers and stats.
- **Dead-end deep dives** (evervault, listenup end without any link to sibling use cases). Corpus leaders (eraser, equals, tome) always route sideways.
- **Text-only step lists with unbalanced whitespace** (evervault's "How it works": Store and Share steps are paragraphs with no visual, leaving a large empty column). Every step in stronger pages (listenup, equals) gets its own screenshot.
- **Burying the only product screenshot deep in the page** (clutch shows its UI once, ~60% down after five text sections). If the product has a UI, it belongs in or right after the hero.
- **Monotonous zig-zag walls.** Six identical alternating rows blur together; clay-com avoids this by rotating pastel background tints per row, default by wrapping each chapter in its own colored container — vary the ground, not just the side.

## Checklist

1. Decide archetype first: deep-dive (one use case, full narrative) or index (all use cases, scannable cards). Deep-dive is the default; index only when linking out to 3+ dedicated pages.
2. Hero: eyebrow chip = use-case/audience label matching the nav taxonomy; H1 = outcome in the user's words ("Create training videos your reps won't skip"); subhead ≤2 sentences; primary CTA + optional secondary (demo/examples).
3. Put a real product visual performing this exact use case in or directly under the hero — actual UI, not an abstract illustration.
4. Add a social-proof strip (customer logos or 2–3 short quotes) immediately after the hero.
5. Optionally frame the problem before features: old-way-vs-new-way split or Problem → Solution sequence (best for security/enterprise and category-creation products).
6. Body = 3–6 sub-scenario rows, alternating text/image sides; each row gets its own heading, ≤3 lines of copy, a dedicated screenshot, and ideally a micro-CTA; vary row background tints or wrap chapters in colored containers to keep rhythm. Use numbered steps instead if the use case is a sequential workflow.
7. Follow the narrative with a 4–7 item capability icon grid for supporting features you didn't give a full row.
8. Insert quantified, use-case-specific proof: ROI stat cards with customer names, ratings/badges, or a full-bleed quote from a recognizable customer.
9. Offer a concrete starting point: templates, runnable examples, or a demo gallery relevant to this use case.
10. Close with a contrast-flipped final CTA band, and cross-link 3+ sibling use cases (cards in body or a link index) plus the full taxonomy in the footer — never dead-end the page.

## Best references

- **clay-com** — canonical deep-dive: hero with live product table, old-vs-new problem split, six tinted zig-zag scenario rows each with dual micro-CTAs, dark closing band.
- **synthesia** — proof-heavy light SaaS: eyebrow-labeled hero, pain framing, step module, and the best ROI-stat cards in the corpus (named customers + percentages + case-study links).
- **eraser** — dark-tech deep dive that opens with a real artifact (actual architecture diagram) and models the ~20-link sibling use-case index.
- **modal** — dark-tech pattern for dev tools: testimonials above the fold, checklist + code/terminal embeds per section, runnable example carousel.
- **clutch** — enterprise-security narrative structure: Problem → Solution → per-persona Challenge → Capabilities → Benefits; the template for sales-led products.
- **viewport** — cleanest index page: three cards, chip + title + sentence + screenshot + arrow, zero noise.
- **tome** — editorial hybrid: audience page opening with a scannable scenario index (title/description/thumbnail rows), template grid, sibling cross-links.
- **fable** — dark creative-tool treatment: per-row channel eyebrows (SOCIAL MEDIA, PAID ADS) that map scenario rows to the customer's own vocabulary.
