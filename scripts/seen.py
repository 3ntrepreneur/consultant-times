#!/usr/bin/env python3
"""Check candidate URLs/titles against everything already published, before fetching.
Usage: python3 scripts/seen.py URL [URL ...]   (prints SEEN <id> <where> or NEW)"""
import json, glob, sys, re, os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def norm(u): return re.sub(r"^https?://(www\.)?|[?#].*$|/+$", "", u.strip().lower())
idx = {}
def walk(o, where, cur=None):
    if isinstance(o, dict):
        i = o.get("id", cur)
        for k, v in o.items():
            if k == "url" and isinstance(v, str): idx.setdefault(norm(v), (i, where))
            elif k == "sources" and isinstance(v, list):
                for s in v:
                    if isinstance(s, dict) and isinstance(s.get("url"), str): idx.setdefault(norm(s["url"]), (i, where))
            else: walk(v, where, i)
    elif isinstance(o, list):
        for x in o: walk(x, where, cur)
for f in ["data/edition.json", "data/library.json"] + sorted(glob.glob("data/archive/*.json")):
    p = os.path.join(root, f)
    if os.path.exists(p) and not f.endswith("months.json"):
        walk(json.load(open(p)), f)
for u in sys.argv[1:]:
    h = idx.get(norm(u))
    print(("SEEN %s %s" % h if h else "NEW") + "  " + u)
