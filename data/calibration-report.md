# Calibration Report — profile-prompt.md vs ground truth

**Round 1 (2026-07-10)** — prompt: `scripts/profile-prompt.md` (v1, with CTA-specific
color sampling + separate heading/body font inspection baked in from the start).

Ground truth: authoritative `DESIGN.md` files (getdesign.md) for the 3 sites that
have BOTH screenshots and an etalon.

| Site | Check | Etalon | Generated | Verdict |
|---|---|---|---|---|
| figma | palette.primary | #000000 | #0D0D0D (black family) | PASS |
| figma | typography | figmaSans | "Figma Sans (neo-grotesque)" | PASS |
| figma | radius | pill 50px buttons / 2-32px scale | "pill buttons, small 2-6px cards" | PASS |
| supabase | palette.primary | #3ecf8e | #3ecf8e (exact) | PASS |
| supabase | typography | Circular | "geometric grotesque (Circular-like)" | PASS |
| supabase | radius | sm 6 / md 8 / lg 12 | "small 4-6px buttons, medium 8-12px cards" | PASS |
| raycast | palette.primary | #ffffff (white CTA) | #e8e8ec (near-white) | PASS |
| raycast | typography | Inter | Inter (exact) | PASS |
| raycast | radius | md 8 / lg 10 | "medium 8-10px buttons" | PASS |

**Result: 9/9 PASS in round 1. Prompt frozen as calibrated. No further rounds needed.**

Notes:
- The CTA-fill sampling rule ("sample the MAIN CTA BUTTON fill specifically") is what
  nailed raycast (white CTA on dark) and figma (black CTA) — keep it verbatim.
- Agents also correctly identified dual-polarity systems (supabase launch-week white
  mode, figma dark blog) — the "check both hero and mid-page sections" rule works.
