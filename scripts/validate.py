#!/usr/bin/env python3
"""Validate an edition JSON before publishing. Exit 0 = OK, 1 = problems (printed)."""
import json, sys, re, datetime
p = sys.argv[1] if len(sys.argv) > 1 else "data/edition.json"
errs = []
def need(cond, msg):
    if not cond: errs.append(msg)
try:
    d = json.load(open(p, encoding="utf-8"))
except Exception as e:
    print("INVALID JSON:", e); sys.exit(1)
https = lambda u: isinstance(u, str) and u.startswith("https://")
need(isinstance(d.get("edition"), dict) and d["edition"].get("id") and d["edition"].get("label"), "edition.id/label missing")
S = d.get("stories") or []
need(len(S) >= 2, "need at least 2 stories")
ids = [s.get("id") for s in S]
need(len(ids) == len(set(ids)), "duplicate story ids")
need(d.get("lead") in ids, "lead must be one of the story ids")
for s in S:
    sid = s.get("id", "?")
    need(bool(re.fullmatch(r"[a-z0-9-]{3,80}", str(s.get("id", "")))), f"{sid}: bad id slug")
    for k in ("title", "summary", "cs", "firm", "kicker", "section", "date"):
        need(bool(s.get(k)), f"{sid}: missing {k}")
    need(len(str(s.get("title", "")).split()) <= 16, f"{sid}: headline too long")
    src = s.get("sources") or []
    need(len(src) >= 1, f"{sid}: no sources")
    for so in src: need(https(so.get("url")), f"{sid}: source url must be https")
    need(s.get("confidence") in (None, "Confirmed", "Reported", "Developing"), f"{sid}: bad confidence")
lead = next((s for s in S if s.get("id") == d.get("lead")), {})
need(len(lead.get("paras") or []) >= 2, "lead needs a full article (paras)")
for w in d.get("wire") or []:
    need(bool(w.get("text")) and https(w.get("url")), f"wire item bad: {str(w)[:60]}")
for m in d.get("bigMoves") or []:
    need(all(m.get(k) for k in ("type", "co", "title", "value", "cs")) and https(m.get("url")), f"bigMove bad: {m.get('title','?')}")
for r in d.get("radar") or []:
    need(all(r.get(k) for k in ("title", "cs")) and https(r.get("url")), f"radar bad: {r.get('title','?')}")
today = datetime.date.today().isoformat()
for j in (d.get("vancouver") or {}).get("jobs") or []:
    need(https(j.get("url")), f"job url bad: {j.get('role')}")
    if j.get("closes"): need(j["closes"] >= today, f"job expired: {j.get('role')}")
need(len(d.get("howItWorks") or []) >= 1, "howItWorks empty")
allitems = [("bigMove", m) for m in d.get("bigMoves") or []] + [("radar", r) for r in d.get("radar") or []] + [("vancouver", v) for v in (d.get("vancouver") or {}).get("stories") or []] + [("wire", w) for w in d.get("wire") or []] + [("howItWorks", h) for h in d.get("howItWorks") or []]
allids = ids + [x.get("id") for _, x in allitems]
for kind, x in allitems: need(bool(re.fullmatch(r"[a-z0-9-]{3,80}", str(x.get("id", "")))), f"{kind} item missing/bad id: {str(x.get('title') or x.get('text'))[:50]}")
need(len(allids) == len(set(allids)), "duplicate ids across sections")
for h in d.get("howItWorks") or []:
    if h.get("sections"): need(h.get("caseq") and h.get("caseAnswer") and len(h.get("sources") or []) >= 3, f"deep dive {h.get('id')} needs caseq, caseAnswer and 3+ sources")
txt = json.dumps(d)
need("<script" not in txt.lower(), "script tag found in data")
if errs:
    print("VALIDATION FAILED:"); [print(" -", e) for e in errs]; sys.exit(1)
print("OK:", len(S), "stories,", len(d.get("wire") or []), "wire,", len(d.get("bigMoves") or []), "big moves")
