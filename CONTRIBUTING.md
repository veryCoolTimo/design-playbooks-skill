# Contributing

Thanks for helping grow the corpus. Issues-first: open an issue before a large PR so we
can agree on scope.

## Add or update a site profile

1. Add screenshots under `media/<slug>/<page>/<page>.<ext>` (or run
   `python3 scripts/update_recent.py` to pull new recent.design items).
2. Generate the profile with the calibrated prompt in `scripts/profile-prompt.md`
   (read the screenshots, fill the schema — palette sampled from the real CTA/canvas,
   fonts inspected for headings vs body). Write it to `profiles/sites/<slug>.md`.
3. Rebuild + validate:
   ```
   python3 scripts/build_catalog.py
   python3 scripts/validate_library.py   # must print "0 errors"
   ```
4. Sanity-check the tokens visually: `python3 scripts/preview.py <slug>`.

## Add a playbook

- **Page playbook** — only when the corpus has ≥15 examples of that page type
  (`python3 scripts/build_coverage.py` to check). Fewer → extend `playbooks/pages/misc.md`.
- Every playbook needs a coverage badge (`> Coverage: N examples from corpus`) and must
  cite real slugs for each claim. The validator enforces the badge.

## Rules

- **Evidence, not opinion.** Every rule cites sites actually in the corpus.
- **Original analysis only.** Don't paste third-party design docs; write your own words.
  No proprietary assets in the repo (screenshots stay in the gitignored `media/`).
- **Keep the schema.** Profiles follow `scripts/profile-prompt.md`; generated DESIGN.md
  files follow `scripts/design-md-template.md` (Stitch-compatible sections).
- `validate_library.py` must stay green — it runs on every change.
