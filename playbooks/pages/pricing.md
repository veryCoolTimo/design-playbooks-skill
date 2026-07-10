# Pricing Page Playbook
> Coverage: 123 examples from corpus (analyzed 20)

## Anatomy

Ordered skeleton, top to bottom. Percentages = share of the 20 analyzed screenshots.

1. **Slim nav** with a "Pricing" item marked active + primary CTA button top-right — 100%.
2. **Hero: short H1 + one-line subhead** — 100%. Two headline modes: plain label ("Pricing" — evervault, raycast, metaview, titan, herokit) or value claim ("Simple and transparent" — cycleapp; "Reassuringly expensive" — betterstack; "Predictable pricing, designed to scale" — supabase; "How much do you value your time?" — listenup). No imagery in the hero except colorful brands (gamma clouds, cohere gradient, goodnotes product shots).
3. **Billing/plan toggle** directly under the hero — 40% (gamma, cycleapp, herokit, listenup, pirsch, specifyapp; obviously uses a segmented control to switch plan *types*; pirsch adds a usage slider that recalculates prices live).
4. **Plan cards row** — 80%. Dominant variant: **3 cards** (60%: cap, cycleapp, evervault, gamma, herokit, listenup, metaview, obviously, pirsch, saybriefly, specifyapp, tedy). 4 cards: june, supabase. 2 plans: betterstack. Table-as-cards: raycast. No cards at all: ada (lead-gen form), titan (editorial fee schedule), cohere (usage-rate rows + calculator).
5. **Enterprise/custom tier** — 85%. Either the last card ("Let's Talk" — specifyapp, supabase, june, tedy) or a separate full-width strip below the cards (saybriefly, cohere, gamma's "Contact sales@" bar).
6. **Feature comparison table** — 40% (cycleapp, evervault, pirsch, raycast, specifyapp, supabase, betterstack), grouped by category (Usage / Collaboration / Support etc.). cap instead runs a **competitor** comparison table (Cap vs Loom vs CleanShot X).
7. **Social proof**: logo bar (cap, cohere, june, listenup, obviously, pirsch, specifyapp — 40%) and/or testimonial quotes (cohere, june, specifyapp).
8. **FAQ accordion** — 75% (betterstack, cohere, gamma, goodnotes, herokit, june, listenup, metaview, obviously, pirsch, raycast, specifyapp, supabase, tedy, titan). Typically 5–12 questions, single column, plus/chevron toggles.
9. **Final CTA banner** — 85%. Full-width block restating the free entry point ("Try Cycle today", "Downtime ends today" — betterstack, "Ready to Level up Your Analytics?" — pirsch, giant yellow button — listenup, email-capture bar — metaview).
10. **Footer**, often with an oversized brand wordmark (ada, gamma, cohere, saybriefly) — a corpus-wide signature move.

## Patterns that work

- **Highlight exactly one recommended plan** with a badge and stronger visual weight: filled color card (cap's blue Pro, herokit's yellow Pro, saybriefly's yellow Solopreneurs), tinted background (listenup's lilac Pro), elevated/outlined center card (gamma "Most popular", cycleapp "Most picked", specifyapp, evervault "Popular", pirsch "Best Value", supabase). The badge sits on the card's top edge, centered.
- **"Everything in X, plus…" inheritance** instead of repeating the full list per tier: gamma ("Includes everything in Free, and…"), june ("Everything in Growth plus"), cycleapp, metaview ("← All features in Free +"), evervault. Keeps cards scannable and makes the upgrade delta obvious.
- **Toggle with an explicit savings callout**: gamma pairs the yearly pill with a green "Save up to 25% with a yearly plan" chip; cycleapp puts "Save 25%" inside the toggle; herokit adds a "20% OFF" pill. Never make the user compute the discount.
- **Anchor pricing with strikethrough**: listenup shows "$29 → $25/month" on yearly billing — the discount is visible at the price itself, not only at the toggle.
- **Usage-based pricing needs an interactive calculator, not prose**: cohere embeds a per-embedding price slider ("50k embeddings ≈ $50.00"); pirsch drives all three card prices from a page-view slider; ada links a "Calculate your savings" tool. betterstack prints per-unit rates inline in its tables.
- **Put logos where the doubt is**: metaview attaches "Chosen by: AngelList, Tally…" strips directly beneath each paid card; cap places "Used by employees at Tesla, Microsoft…" between the hero and the cards. Proof adjacent to the decision beats a generic logo wall.
- **Group long comparison tables by category with repeated plan CTAs**: cycleapp (Usage/Collaboration/Features/Admin/Support), supabase (per-product icons: Database, Auth, Storage…), evervault repeats Get Started buttons in the table header so users convert without scrolling back up.
- **De-risk the free tier at the point of click**: gamma badges Free with "No credit card required"; listenup captions its giant CTA "Start for free. No card required."; raycast answers "Why is Raycast free?" first in its FAQ.
- **Sectioned feature lists with honest ✕ marks**: obviously splits each card into Service / Support / Technology / Deliverables with both checks and dimmed crosses; titan lists what every customer gets ("What you get — no matter what") before fee details. Transparency reads as confidence.
- **One-time vs subscription side by side**: goodnotes shows Yearly $9.99 and One-Time $29.99 as columns of the same card — a clean pattern when both models exist.

## Variants by style

- **Light minimal** (cap, cycleapp, june, metaview, obviously): white/cream page, gray hairline card borders, one accent color reserved for the highlighted plan and CTAs. Density is low in cards, high in the comparison table below. FAQ on white or a softly tinted panel (metaview's blush block).
- **Dark tech** (betterstack, evervault, pirsch, raycast, specifyapp, supabase): near-black background, cards as slightly lighter panels with 1px borders, accent color only on the "popular" badge/CTA (supabase green, specifyapp violet/pink, pirsch yellow). This style carries the longest comparison tables in the corpus (betterstack, supabase run thousands of pixels of grouped tables) — depth is the selling point. herokit is the hybrid: dark canvas + one loud neon-yellow recommended card.
- **Colorful / playful** (gamma, tedy, saybriefly, listenup, goodnotes, cohere): each card or band gets its own background color (saybriefly's yellow/dark-green cards, tedy's pink/lavender/green sections), illustrated or gradient heroes (gamma's clouds, cohere's aurora), hand-drawn annotations and jokes (listenup's "We eat our own dog food" arrow, "Your logo" placeholder in the logo bar). Cards stay simple; personality lives in the surroundings and the final CTA (listenup's oversized pill button, tedy's glowing dark demo banner).
- **Editorial serif** (titan): no cards at all — a fee schedule laid out as ruled horizontal rows (product name + serif rate "0.25%/year"), tiered rates by deposit size, a human contact card with a photo, and dense legal disclosures in the footer. Fits regulated/finance products where card grids would feel flippant.
- **Enterprise lead-gen** (ada): no listed prices — hero contains the qualification form ("Get pricing"), followed by "what's included" capability lists, ROI stat cards (60K hours, $2.7M, 6.7x), a savings calculator, and a demo CTA. Use only when pricing is genuinely custom; you're trading self-serve conversion for lead quality.

## Anti-patterns

- **Endless undifferentiated tables**: betterstack's comparison section runs ~8000px of small-text tables with no sticky plan header — by mid-scroll you can't tell which column is which. If the table is that long, keep plan names/CTAs pinned (evervault and supabase mitigate by repeating headers/CTAs).
- **Triple-repeating near-identical lists**: obviously prints the same ~20 rows in all three cards with only 2–3 cells differing — the diff is what matters; inheritance ("Everything in X, plus") or a table encodes it better.
- **No recommended plan**: raycast's flat table and june's four equal cards (Pro only gets a thin outline) leave choice-paralysis on the user; 60% of the corpus explicitly badges one plan — do it.
- **Hiding prices behind a form** (ada) without any numeric anchor at all — acceptable only for high-ACV enterprise sales; every self-serve product in the corpus shows at least one real number above the fold.
- **Burying the plans**: goodnotes leads with a brand hero and product shots, pushing plan cards below the fold; pricing pages in the corpus otherwise get to numbers within one viewport.
- **Toggle without stating the delta**: nothing in the corpus ships a bare Monthly/Yearly switch — every toggle carries "Save 25%" or shows the struck-through monthly price. A silent toggle is a corpus-wide avoidance.
- **Mixed pricing bases without a legend**: tedy sells per-employee tiers ($6/$5/$4 by headcount) inside one card plus a "+5% claim processing fee" — that fee footnote in small type is the weakest part of an otherwise clear page. Surcharges belong at the price, not in fine print.
- **FAQ as open text walls**: everyone uses collapsed accordions; only the first item is ever pre-expanded (june, metaview).

## Checklist

1. Hero = short H1 + one clarifying subhead; no hero imagery unless the brand is colorful/playful. Nav has active "Pricing" state and a primary CTA.
2. Show 3 tiers (max 4): free/entry → recommended mid → enterprise "Let's talk". Equal-height cards; each card = name, one-line audience descriptor, price with unit ("/mo, per seat, billed annually"), CTA, feature list.
3. Badge and visually elevate exactly one plan (fill, tint, or outline + "Most popular").
4. Use "Everything in [previous tier], plus…" for tiers 2+; list only the delta.
5. If monthly/annual both exist: toggle above the cards with explicit "Save N%" and/or strikethrough anchor price. Default to yearly.
6. Usage-based component? Add a live slider/calculator that outputs a dollar figure (cohere, pirsch), never a rate table alone.
7. Below cards: grouped comparison table with category headers; repeat plan names + CTA buttons at the top of the table (and sticky if >2 screens tall).
8. Add proof near the decision: logo bar under the cards or per-card "Chosen by" strips (metaview); one or two testimonials optional.
9. FAQ accordion (6–12 items) answering billing mechanics: trial, cancellation, payment methods, what counts toward limits, upgrade/downgrade.
10. Close with a full-width CTA banner restating the free/no-credit-card entry point; footer may carry the oversized wordmark for brand punch.

## Best references

- **gamma** — canonical colorful 3-card layout: toggle + savings chip, badge trio ("No credit card" / "Most popular" / "Most powerful"), elevated center card, inheritance lists, FAQ, giant wordmark footer.
- **cycleapp** — cleanest light-minimal execution: toggle with "Save 25%", "Most picked" badge, exemplary grouped comparison table, playful CTA banner.
- **supabase** — dark-tech depth done right: 4 cards, cost-control section, product-grouped mega table, compliance badges; the template for infra pricing.
- **evervault** — compact dark 3-card + comparison table with in-header CTAs + compliance cross-sell cards.
- **listenup** — playful persuasion: strikethrough anchor pricing, credits + pay-as-you-go explained, joke logo bar, oversized final CTA.
- **cohere** — the usage-based reference: rate card + interactive price calculator + free/enterprise strips sandwiching it.
- **titan** — editorial serif fee schedule for finance/regulated products; rows instead of cards, human contact block, disclosure-heavy footer.
- **metaview** — per-card "Chosen by" logo strips and a tidy cream aesthetic; smallest page in the corpus that still covers cards + FAQ + CTA.
