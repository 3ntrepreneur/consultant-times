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
BMT = ["M&A","Funding","IPO","Earnings","Leadership","Restructuring","Partnerships","Legal & Governance","Divestiture","Distress","Market Entry","Canada"]
for m in d.get("bigMoves") or []:
    need(m.get("type") in BMT, f"bigMove {m.get('id')} has invalid type {m.get('type')}")
    need(all(m.get(k) for k in ("type", "co", "title", "value", "cs")) and https(m.get("url")), f"bigMove bad: {m.get('title','?')}")
for r in d.get("radar") or []:
    need(all(r.get(k) for k in ("title", "cs")) and https(r.get("url")), f"radar bad: {r.get('title','?')}")
today = datetime.date.today().isoformat()
for j in (d.get("vancouver") or {}).get("jobs") or []:
    need(https(j.get("url")), f"job url bad: {j.get('role')}")
    if j.get("closes"): need(j["closes"] >= today, f"job expired: {j.get('role')}")
need(len(d.get("howItWorks") or []) == 3, "howItWorks must contain exactly 3 deep dives")
need(sorted(h.get("type") for h in d.get("howItWorks") or []) == ["Business", "Industry", "Strategy"], "howItWorks must be exactly one Industry, one Business and one Strategy deep dive (field `type`)")
for p_ in d.get("policy") or []:
    need(bool(re.fullmatch(r"[a-z0-9-]{3,80}", str(p_.get("id", "")))), "policy item bad id")
    need(p_.get("juris") in ("Canada", "B.C.", "US", "EU", "UK", "Global", "Rest of world", "Other"), f"policy {p_.get('id')} needs a valid juris")
    need(len(p_.get("paras") or []) >= 2 and p_.get("summary") and p_.get("cs"), f"policy {p_.get('id')} needs paras, summary and cs")
    need(len(p_.get("sources") or []) >= 2 and all(str(s_.get("url", "")).startswith("https://") for s_ in p_.get("sources") or []), f"policy {p_.get('id')} needs 2+ https sources")
    for e_ in p_.get("dates") or []: need(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(e_.get("iso", "")))), f"policy {p_.get('id')} bad date iso")
DESKS = ["Tech & AI","Financial services","Energy & resources","Consumer & retail","Health","Industrials & logistics","Media & telecom","Public sector","Consulting industry"]
LENSES = ["Market size & growth","Profit pools & margins","Structure & competition","Demand & customers","Talent & operations","Regulation & policy","Technology & disruption","Capital & M&A","Risks & unknowns"]
for n_ in d.get("deskNews") or []:
    i_ = n_.get("id")
    need(bool(re.fullmatch(r"[a-z0-9-]{3,80}", str(i_ or ""))), "deskNews item bad id")
    need(n_.get("desk") in DESKS, f"deskNews {i_} needs a valid desk")
    need(n_.get("lens") in LENSES, f"deskNews {i_} needs a valid lens")
    need(len(n_.get("paras") or []) >= 2 and n_.get("summary") and n_.get("cs"), f"deskNews {i_} needs paras, summary and cs")
    need(len(n_.get("facts") or []) >= 3 and len(n_.get("questions") or []) >= 2 and len(n_.get("unknowns") or []) >= 1, f"deskNews {i_} needs 3+ facts, 2+ questions and 1+ unknowns")
    need(len(n_.get("sources") or []) >= 2 and all(str(s_.get("url", "")).startswith("https://") for s_ in n_.get("sources") or []), f"deskNews {i_} needs 2+ https sources")
    for e_ in n_.get("dates") or []: need(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(e_.get("iso", "")))), f"deskNews {i_} bad date iso")
    need(sum(len(x.split()) for x in n_.get("paras") or []) <= 400, f"deskNews {i_} is too long (keep under 400 words)")
allitems = [("policy", q) for q in d.get("policy") or []] + [("bigMove", m) for m in d.get("bigMoves") or []] + [("radar", r) for r in d.get("radar") or []] + [("vancouver", v) for v in (d.get("vancouver") or {}).get("stories") or []] + [("wire", w) for w in d.get("wire") or []] + [("howItWorks", h) for h in d.get("howItWorks") or []] + [("deskNews", n) for n in d.get("deskNews") or []]
allids = ids + [x.get("id") for _, x in allitems]
for kind, x in allitems: need(bool(re.fullmatch(r"[a-z0-9-]{3,80}", str(x.get("id", "")))), f"{kind} item missing/bad id: {str(x.get('title') or x.get('text'))[:50]}")
need(len(allids) == len(set(allids)), "duplicate ids across sections")
for h in d.get("howItWorks") or []:
    need(len(h.get("sections") or []) >= 5, f"deep dive {h.get('id')} needs 5+ sections")
    need(h.get("caseq") and h.get("caseAnswer") and len(h.get("cheat") or []) >= 5 and len(h.get("facts") or []) >= 3 and len(h.get("sources") or []) >= 4, f"deep dive {h.get('id')} needs caseq, caseAnswer, cheat (5+), facts (3+) and 4+ sources")
    need(sum(len(p.split()) for s_ in h.get("sections") or [] for p in s_.get("paras") or []) >= (650 if "launch" in str(d.get("edition", {}).get("id", "")) else 1300), f"deep dive {h.get('id')} is under the minimum length (1,300 words; launch edition 650)")
import os
lib = os.path.join(os.path.dirname(os.path.abspath(p)), "library.json")
if os.path.exists(lib):
    L = json.load(open(lib)).get("items", [])
    lids = [x.get("id") for x in L]
    need(len(lids) == len(set(lids)), "duplicate ids in library.json")
    need(not (set(lids) & set(allids)), "library.json ids overlap with the edition")
txt = json.dumps(d)
need("<script" not in txt.lower(), "script tag found in data")
if errs:
    print("VALIDATION FAILED:"); [print(" -", e) for e in errs]; sys.exit(1)
print("OK:", len(S), "stories,", len(d.get("wire") or []), "wire,", len(d.get("bigMoves") or []), "big moves")

# archive integrity (non-fatal files may not exist yet)
adir = os.path.join(os.path.dirname(os.path.abspath(p)), "archive")
if os.path.isdir(adir):
    aids = []
    for f in sorted(os.listdir(adir)):
        if f.endswith(".json") and f != "months.json":
            aids += [x.get("id") for x in json.load(open(os.path.join(adir, f))).get("items", [])]
    if len(aids) != len(set(aids)): errs.append("duplicate ids in data/archive")
    if set(aids) & set(allids): errs.append("archive ids overlap with the live edition")
    if errs:
        print("VALIDATION FAILED:"); [print(" -", e) for e in errs]; sys.exit(1)
