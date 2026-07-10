# Blog Page Playbook
> Coverage: 61 examples from corpus (analyzed 20)

## Anatomy

Ordered skeleton, top to bottom. Percentages = share of the 20 analyzed screenshots showing the variant.

1. **Global nav** (100%) — standard marketing header; the Blog link is often marked active (cap, dimension, portrait).
2. **Page header** (95%) — three variants:
   - Plain title, usually just "Blog," centered (acctual, cap, outerbase, hellotime, starlight-money) or left-aligned (krepling, modal, raycast, scenery, trunk, paradigmai) — ~55%.
   - Title + one-line subtitle/mission ("The latest communications from ground control" — outerbase; "We write stuff from time to time that might be interesting" — raycast; "A rundown of the latest Index feature releases…" — index-app) — ~60% add a subtitle.
   - Oversized editorial hero with email capture built in (codex: giant uppercase headline + inline signup form) — ~5%.
3. **Category filter bar** (45%) — pill or tab row directly under the header: All Posts / Changelog / Announcement (dimension, index-app), topic pills (krepling, modal, trunk), tabs with color-coded categories (starlight-money), a horizontal category nav strip (goodnotes). Trunk adds the only search field in the sample.
4. **Featured post** (50%) — the newest/most important post gets 2–3x the footprint: full-width split card with big cover (scenery, starlight-money, krepling), hero-sized first card (cap, superhuman, outerbase), or a text-left/card-right hero with a "Read More" button (portrait, codex). Trunk pairs the featured card with a "Featured Posts" text sidebar.
5. **Post feed** (100%) —
   - 2-column card grid: ~35% (acctual, dimension, evervault, scenery, starlight-money, superhuman, portrait).
   - 3-column card grid: ~20% (hellotime, paradigmai, goodnotes at 3-up, modal's category rows, trunk's Latest Posts).
   - Single-column list/rows (thumbnail one side, text the other): ~35% (astro-build, cap, codex, genway, raycast, index-app, modal's top feed).
   - Text-only list rows, no thumbnails: ~10% (outerbase "Recent Posts", trunk "Valuable Tips" section).
6. **Card meta** — date (~95%), author name (~60%), author avatar (~45%: dimension, genway, index-app, portrait, starlight-money, cap byline), category pill (~45%), read time (~15%: genway, goodnotes).
7. **Load more / pagination** (25%) — numbered pages (astro-build), "Show more" / "See More…" / "Load more" buttons (modal, trunk, superhuman). Most sites simply list everything.
8. **Newsletter / subscribe capture** (30%) — inline hero form (codex), dedicated mid-page band (trunk "Stay in touch with us"), sidebar RSS block (astro-build), CTA with email field (scenery), footer form (superhuman).
9. **Pre-footer product CTA** (75%) — the blog almost always ends by selling the product: playful branded board (acctual "Love you, pay me"), gradient banner (genway, dimension), full-bleed brand-color block (scenery's yellow), dark block with serif headline (paradigmai, index-app), "Ship your first app in minutes." (modal). Superhuman uniquely inserts the CTA banner mid-feed.
10. **Footer** (100%) — full sitemap footer, same as the rest of the site.

## Patterns that work

- **Branded, systematized cover art instead of stock photos.** Every strong example generates covers from one template system: collage of product UI + stickers on brand colors (acctual), abstract 3D renders in one palette (modal's green glass, raycast's gradients), sky motif (cap), flat illustration set (krepling, hellotime), monochrome generative art (paradigmai). The feed reads as one brand even with 20+ posts.
- **Featured-post slot at the top.** cap, scenery, starlight-money, superhuman, trunk, portrait, and krepling all give the lead post a full-width or hero-scale card; the rest of the feed drops to a smaller grid. This creates hierarchy and a clear entry point.
- **Category pills that double as navigation.** modal's filter row (All Posts / Engineering / Customer Stories / Tutorials / News) plus per-category "Latest in …" sections with "View all" links turns a flat feed into a content hub. starlight-money color-codes each category pill (Product Releases = amber, Life at Starlight = red, Company News = blue) so the grid is scannable by type.
- **Compact meta line: avatar + name + role/date.** dimension (avatar, "Founder, CEO", date right-aligned), genway (avatar, date, read time), index-app and portrait do the same — it adds credibility at almost no layout cost.
- **Single-column rows for low-volume blogs.** cap (3 posts) and portrait (3 posts) make few posts feel intentional by using huge cards; outerbase shows the failure mode of the same volume with skinny text rows.
- **Mid-feed or end-of-feed conversion moment.** superhuman drops a gradient "Turn email into a competitive advantage" banner in the middle of the grid; trunk places a newsletter band between the featured area and Latest Posts. Blogs are top-of-funnel — the corpus consistently routes readers back to signup (75% have a pre-footer product CTA).
- **Human-voice subtitles beat SEO boilerplate.** raycast ("We write stuff from time to time that might be interesting ✌"), outerbase ("The latest communications from ground control"), index-app ("Our words") — one wry line sets tone cheaply.
- **Read-time labels for content-marketing-heavy blogs.** genway and goodnotes show "5 min read" / "7 min read" next to the date; useful when posts are long-form guides rather than announcements.
- **Editorial grid discipline.** paradigmai draws hairline rules between columns and rows and uses a serif display "Blog" — the strictly aligned 3-up grid with title + date + arrow icon feels premium with zero decoration.

## Variants by style

- **Light minimal** (acctual, cap, hellotime, index-app, goodnotes, portrait, genway, krepling): white/off-white ground, centered page title, cards with soft borders or subtle shadow, colorful illustrated thumbnails carry all the personality. Meta stays gray; category pills are outlined/neutral. Pre-footer CTA flips to a saturated brand block (acctual's green board, index-app's dark panel) for contrast.
- **Dark tech** (astro-build, modal, evervault, raycast, superhuman, starlight-money, scenery, dimension, outerbase, trunk): near-black background, thumbnails are gradient/3D/neon renders that glow against the dark. Accent color appears in the heading ("Modal *Blog*" in green) and category pills. Density is higher (evervault, superhuman run dense 2-col grids). CTA sections use gradients (dimension, superhuman) or a full-bleed brand-color slab (scenery's yellow).
- **Editorial / brutalist** (codex, paradigmai): oversized display type (uppercase grotesque at codex, serif at paradigmai), visible grid lines or hard section splits, monochrome art, very few posts per screen. codex splits the page into a light hero half and black CTA half; paradigmai closes with a serif manifesto headline. Works when the blog is sparse and each post is a statement.

## Anti-patterns

- **Text-only lists with dates as the sole meta** (outerbase "Recent Posts"): four bare rows with 11/3/2023-style dates on near-black — no thumbnails, no excerpts, low contrast. The page looks abandoned. If posts lack covers, at least add excerpts (astro-build's imageless rows survive because they keep title + excerpt + date).
- **Repeated identical cover art.** acctual shows the same "Guide to crypto accounting" collage on two different cards; templated covers must vary color/composition per post or the feed looks broken.
- **Clipped/truncated titles** ("A definitive guide on crypt businesses" — acctual). Card layouts need line-clamp with full titles that fit, not mid-word cuts.
- **Empty-feeling pages for young blogs.** index-app and dimension have 2–3 posts; index-app compensates with a strong hero and centered narrow column, but the gap between feed and footer CTA still yawns. If content is thin, use oversized single-column cards (cap, portrait) rather than a grid that exposes emptiness.
- **No pagination strategy on long feeds.** goodnotes and evervault render 40+ cards in one endless page with no "load more" or filters pulling weight; scan cost gets high. modal/trunk's capped feed + category sections handles volume better.
- **Meta contrast too low on dark themes.** starlight-money's and outerbase's thumbnails and gray meta text sit barely above the background; dark blogs need thumbnails that glow (modal, raycast) and meta at readable contrast.
- **Stock photography** — conspicuously absent across all 20 sites. Nothing in the corpus uses generic stock; every cover is branded product UI, illustration, or abstract render.

## Checklist

1. Title the page plainly ("Blog" or "[Brand] Blog") with a one-line human subtitle; skip generic "News & insights" phrasing unless it carries voice.
2. Design one cover-art template system (brand palette + product UI / illustration / abstract render) and generate every thumbnail from it; never mix in stock photos, never repeat identical art on two posts.
3. Give the newest or most important post a featured slot at 2–3x card size before the grid starts.
4. Pick feed density by volume: 3+ col grid for 15+ posts (goodnotes, hellotime), 2-col for 6–15 (starlight-money, scenery), oversized single-column for under 6 (cap, portrait).
5. Standardize the meta line: date always; author + avatar for credibility-driven products; category pill if you have 3+ content types; read time for long-form guides.
6. If you have 3+ content categories, add a filter pill/tab row under the header (modal, starlight-money, index-app) and consider color-coding pills.
7. Cap the initial feed and add "Show more" or per-category sections with "View all" links once past ~12 posts (modal, trunk).
8. End with a product CTA section in brand style (75% of corpus does) — headline + one button, optionally an email-capture variant.
9. Add a newsletter capture point (hero form, mid-page band, or footer) if the blog is a retention channel (codex, trunk, superhuman).
10. On dark themes, verify thumbnails and meta text hold contrast against near-black; on light themes, keep cards on subtle borders/shadows and let thumbnails carry the color.

## Best references

- **modal** — the most complete content hub: filter pills, capped top feed, per-category "Latest in …" rows, unified 3D cover art.
- **starlight-money** — featured split card + color-coded category pills on a dark grid; exemplary scannability.
- **trunk** — full-featured pattern: search, filters, featured + sidebar list, newsletter band, tiered sections (Latest Posts / Valuable Tips), big CTA.
- **cap** — the low-volume playbook: three posts made substantial with hero-scale cards, tags, and consistent sky-motif covers.
- **hellotime** — light playful grid; illustration/emoji thumbnails from one system, clean title + author + date meta.
- **paradigmai** — editorial minimalism: serif display title, hairline grid, monochrome art, arrow affordances.
- **superhuman** — dense dark grid with a featured hero and a mid-feed conversion banner; shows how to monetize scroll depth.
- **acctual** — light minimal with the strongest branded-collage cover system (minus its duplicate-art slip).
