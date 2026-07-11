#!/usr/bin/env python3
"""Generate a self-contained visual preview.html from a profile's tokens.

Gives a visual reference (swatches, type scale, buttons, cards) with ZERO
dependency on the media layer — works from the profile frontmatter alone.

  python3 preview.py stripe            # -> previews/stripe.html
  python3 preview.py --all             # every profile
  python3 preview.py stripe --open     # print path to open
"""
import argparse, os, re, sys

LIB = os.path.expanduser("~/.claude/design-library")
OUT = os.path.join(LIB, "previews")

def parse(slug):
    p = os.path.join(LIB, "profiles", "sites", f"{slug}.md")
    if not os.path.exists(p):
        return None
    t = open(p, encoding="utf-8").read()
    fm = t.split("---", 2)[1] if t.startswith("---") else ""
    g = lambda pat: (re.search(pat, fm, re.M) or [None, None])[1]
    ac = re.search(r'accents:\s*\[([^\]]*)\]', fm)
    overview = re.search(r'## Overview\s*(.+?)(?:\n## |\Z)', t, re.S)
    return {
        "slug": slug,
        "style": g(r'^style:\s*(\S+)'),
        "category": (g(r'^category:\s*(.+)') or "").strip().strip('"'),
        "website": (g(r'^website:\s*(\S+)') or "").strip('"'),
        "canvas": g(r'canvas:\s*"(#[0-9a-fA-F]{3,8})"') or "#ffffff",
        "ink": g(r'ink:\s*"(#[0-9a-fA-F]{3,8})"') or "#111111",
        "primary": g(r'primary:\s*"(#[0-9a-fA-F]{3,8})"') or "#333333",
        "accents": re.findall(r'#[0-9a-fA-F]{3,8}', ac[1]) if ac else [],
        "display": (g(r'display:\s*"([^"]+)"') or "sans-serif"),
        "body": (g(r'body:\s*"([^"]+)"') or "sans-serif"),
        "radius": (g(r'^radius:\s*"?(.+?)"?\s*$') or "8px"),
        "overview": (overview[1].strip() if overview else "")[:400],
    }

def _lum(hexcol):
    h = hexcol.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    except (ValueError, IndexError):
        return 1
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255

def _on(hexcol):
    return "#ffffff" if _lum(hexcol) < 0.5 else "#111111"

def _radius_px(txt):
    m = re.search(r'(\d+)\s*px', txt or "")
    if "pill" in (txt or "").lower():
        return "9999px"
    return f"{m[1]}px" if m else "8px"

def swatch(hexcol, label):
    return (f'<div class="sw"><div class="chip" style="background:{hexcol}"></div>'
            f'<code>{hexcol}</code><span>{label}</span></div>')

def render(d):
    rad = _radius_px(d["radius"])
    # cards should never inherit pill radius — cap at a sane box radius
    card_rad = "16px" if rad == "9999px" else rad
    accents = "".join(swatch(a, f"accent {i+1}") for i, a in enumerate(d["accents"][:5]))
    on_primary = _on(d["primary"])
    disp_font = d["display"].split("·")[0].strip().strip('"')
    body_font = d["body"].split("·")[0].strip().strip('"')
    web = f'<a href="{d["website"]}" style="color:{d["primary"]}">{d["website"]}</a>' if d["website"] else ""
    return f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{d['slug']} — design preview</title>
<style>
  :root {{ --canvas:{d['canvas']}; --ink:{d['ink']}; --primary:{d['primary']};
           --on-primary:{on_primary}; --rad:{rad}; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--canvas); color:var(--ink);
          font-family:{body_font!r},system-ui,sans-serif; padding:48px; }}
  .wrap {{ max-width:920px; margin:0 auto; }}
  h1 {{ font-family:{disp_font!r},system-ui,sans-serif; font-size:44px; margin:0 0 4px;
        letter-spacing:-0.02em; }}
  .meta {{ opacity:.6; font-size:13px; margin-bottom:8px; }}
  .over {{ opacity:.8; font-size:15px; line-height:1.5; max-width:640px; margin:0 0 40px; }}
  h2 {{ font-family:{disp_font!r},sans-serif; font-size:13px; text-transform:uppercase;
        letter-spacing:.1em; opacity:.5; margin:36px 0 14px; }}
  .row {{ display:flex; flex-wrap:wrap; gap:14px; }}
  .sw {{ display:flex; flex-direction:column; gap:4px; font-size:11px; }}
  .chip {{ width:96px; height:64px; border-radius:calc(var(--rad)/1.5);
           border:1px solid rgba(128,128,128,.25); }}
  .sw code {{ font-family:ui-monospace,monospace; opacity:.8; }}
  .sw span {{ opacity:.5; }}
  .type div {{ font-family:{disp_font!r},sans-serif; line-height:1.1; margin:6px 0;
               letter-spacing:-0.02em; }}
  .btn {{ display:inline-block; padding:11px 20px; border-radius:var(--rad);
          font-weight:600; font-size:14px; border:none; cursor:pointer; margin-right:12px; }}
  .btn-primary {{ background:var(--primary); color:var(--on-primary); }}
  .btn-ghost {{ background:transparent; color:var(--primary);
                border:1px solid var(--primary); }}
  .card {{ border-radius:{card_rad}; border:1px solid rgba(128,128,128,.2);
           padding:24px; max-width:320px; margin-top:8px;
           box-shadow:0 1px 3px rgba(0,0,0,.06); }}
  .card h3 {{ margin:0 0 8px; font-family:{disp_font!r},sans-serif; }}
  .card p {{ margin:0 0 16px; opacity:.7; font-size:14px; line-height:1.5; }}
  .foot {{ margin-top:48px; font-size:12px; opacity:.4; }}
</style></head><body><div class="wrap">
  <h1>{d['slug']}</h1>
  <div class="meta">{d['style']} · {d['category']} · {web}</div>
  <p class="over">{d['overview']}</p>

  <h2>Palette</h2>
  <div class="row">
    {swatch(d['canvas'],'canvas')}{swatch(d['ink'],'ink')}
    {swatch(d['primary'],'primary')}{accents}
  </div>

  <h2>Type scale — {disp_font}</h2>
  <div class="type">
    <div style="font-size:48px;font-weight:700">Display 48</div>
    <div style="font-size:32px;font-weight:600">Heading 32</div>
    <div style="font-size:20px;font-weight:500">Subhead 20</div>
    <div style="font-size:15px;font-weight:400;font-family:{body_font!r},sans-serif;opacity:.8">Body 15 — {body_font}</div>
  </div>

  <h2>Buttons — radius {rad}</h2>
  <button class="btn btn-primary">Primary action</button>
  <button class="btn btn-ghost">Secondary</button>

  <h2>Card</h2>
  <div class="card">
    <h3>Card title</h3>
    <p>A component styled with this system's canvas, ink, radius and hairline.</p>
    <button class="btn btn-primary">Get started</button>
  </div>

  <div class="foot">Generated from profiles/sites/{d['slug']}.md · design-playbooks · tokens only, no screenshot needed</div>
</div></body></html>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--open", action="store_true", help="print the output path")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    slugs = ([f[:-3] for f in os.listdir(os.path.join(LIB, "profiles", "sites")) if f.endswith(".md")]
             if a.all else [a.slug])
    if not slugs or slugs == [None]:
        print("usage: preview.py <slug> | --all", file=sys.stderr)
        return 2
    n = 0
    for slug in slugs:
        d = parse(slug)
        if not d:
            print(f"no profile: {slug}", file=sys.stderr)
            continue
        dest = os.path.join(OUT, f"{slug}.html")
        open(dest, "w", encoding="utf-8").write(render(d))
        n += 1
        if a.open or not a.all:
            print(dest)
    if a.all:
        print(f"generated {n} previews in {OUT}/")
    return 0

if __name__ == "__main__":
    sys.exit(main())
