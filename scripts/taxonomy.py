#!/usr/bin/env python3
"""Canonical category taxonomy + keyword normalizer.

Maps any freeform category string (266 seen in the corpus, plus future ones)
into one of ~14 canonical buckets. Rules are ordered — first match wins — so
more specific signals (crypto, fintech) are checked before generic ones (saas).
The original string is preserved as `subcategory` by the catalog builder.
"""
import re

# Canonical buckets, checked top-to-bottom. Each: (canon, [keyword regexes]).
# Order matters: specific domains before generic "saas/software".
RULES = [
    ("crypto-web3",   [r"crypto", r"web3", r"defi", r"blockchain", r"dao", r"wallet", r"token"]),
    ("fintech",       [r"fintech", r"finance", r"payment", r"banking", r"invest", r"wealth",
                       r"bnpl", r"lending", r"insurtech", r"insurance"]),
    ("ai-ml",         [r"\bai\b", r"ai-", r"-ai\b", r"\bml\b", r"machine-learning",
                       r"foundation-model", r"llm"]),
    ("developer-tools",[r"dev-?tool", r"developer", r"dev-?platform", r"dev-?infra", r"dev-?data",
                       r"dev-?collab", r"dev-?monitoring", r"dev-?resources", r"devtools",
                       r"devops", r"observability", r"api\b", r"cli", r"sdk", r"cms", r"database",
                       r"cloud-infra", r"cloud-platform", r"cloud-cost", r"low-code", r"no-code",
                       r"website-builder", r"web-builder", r"site-builder", r"backend",
                       r"browser", r"file-sharing", r"infrastructure"]),
    ("security",      [r"security", r"cyber", r"privacy", r"compliance", r"identity"]),
    ("design-creative",[r"design", r"creative", r"portfolio", r"agency", r"studio", r"motion",
                       r"branding", r"illustration", r"3d", r"font", r"typograph"]),
    ("productivity",  [r"productivity", r"collaborat", r"project-management", r"scheduling",
                       r"workflow", r"knowledge", r"note", r"docs?\b", r"calendar", r"meeting",
                       r"internal-tools", r"feedback", r"personal-software", r"product-management",
                       r"product-comms", r"content-creation", r"content-platform", r"messaging"]),
    ("marketing-sales",[r"marketing", r"sales", r"crm", r"seo", r"advertis", r"gtm",
                       r"lead", r"outbound", r"email-market", r"sms-market",
                       r"customer-s(?:ervice|upport|uccess)", r"support"]),
    ("data-analytics",[r"analytics", r"\bbi\b", r"data-", r"-data\b", r"data-platform",
                       r"data-tooling", r"b2b-data"]),
    ("hr-people",     [r"\bhr\b", r"hr-", r"recruit", r"hiring", r"talent", r"people"]),
    ("ecommerce-retail",[r"ecommerce", r"e-commerce", r"retail", r"shop", r"fashion",
                       r"footwear", r"sportswear", r"food", r"beverage"]),
    ("media-consumer",[r"media", r"entertainment", r"music", r"video", r"podcast", r"social",
                       r"streaming", r"reading", r"creator", r"community", r"membership",
                       r"link-in-bio", r"gaming"]),
    ("hardware",      [r"hardware", r"electronics", r"semiconductor", r"wearable", r"automotive",
                       r"aerospace", r"transportation", r"telecom", r"consumer-hardware",
                       r"enterprise-tech"]),
    ("health",        [r"health", r"medical", r"climate", r"sustainab", r"govtech", r"nonprofit",
                       r"legaltech", r"ed-tech", r"education", r"real-estate", r"venture", r"travel",
                       r"accessibility"]),
    ("productivity",  [r"utility", r"utilities", r"form-builder", r"writing", r"freelance"]),
    ("developer-tools",[r"web-platform", r"web-builder"]),  # webflow etc.
    ("media-consumer",[r"webinar", r"audiovisual"]),
]

CANON = [c for c, _ in RULES]

def normalize(raw):
    """Return (canonical, subcategory). subcategory is the original string (or None)."""
    if not raw:
        return "other", None
    s = raw.lower().strip()
    for canon, pats in RULES:
        for p in pats:
            if re.search(p, s):
                return canon, raw
    return "other", raw

if __name__ == "__main__":
    import json, os, collections
    LIB = os.path.expanduser("~/.claude/design-library")
    cat = json.load(open(f"{LIB}/catalog.json"))
    c = collections.Counter(normalize(v["category"])[0] for v in cat["sites"].values())
    total = sum(c.values())
    print(f"{len(cat['sites'])} sites -> {len(c)} canonical buckets:")
    for k, v in c.most_common():
        print(f"  {v:4d} {k}")
    other = [s for s, v in cat["sites"].items() if normalize(v["category"])[0] == "other"]
    print(f"\nunmapped ('other'): {len(other)}")
    for s in other[:20]:
        print(f"  {s}: {cat['sites'][s]['category']}")
