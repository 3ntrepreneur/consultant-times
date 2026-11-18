#!/usr/bin/env python3
"""Generate one static, crawlable page per article (s/<id>/index.html) plus sitemap.xml.
Run after every edition: python3 scripts/build_pages.py"""
import json, glob, os, re, html, shutil, datetime
BASE = "https://3ntrepreneur.github.io/consultant-times"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
def load(p, default):
    try: return json.load(open(p, encoding="utf-8"))
    except Exception: return default
ed = load("data/edition.json", {})
items = {}
def add(x, kind):
    i = x.get("id")
    if i and re.fullmatch(r"[a-z0-9-]{3,100}", str(i)) and i not in items: items[i] = (x, kind)
for k in ("stories", "policy", "bigMoves", "radar", "wire", "deskNews", "howItWorks"):
    for x in ed.get(k) or []: add(x, k)
for x in (ed.get("vancouver") or {}).get("stories") or []: add(x, "van")
for x in load("data/library.json", {}).get("items") or []: add(x, "howItWorks")
for f in sorted(glob.glob("data/archive/2*.json")):
    for x in load(f, {}).get("items") or []: add(x, x.get("kind") or "story")
e = lambda s: html.escape(str(s if s is not None else ""), quote=True)
def clip(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"
CSS = "body{margin:0;background:#F4EFE3;color:#1a1a1a;font:18px/1.7 Georgia,'Times New Roman',serif}.w{max-width:720px;margin:0 auto;padding:24px 20px 60px}.top{border-bottom:2px solid #1a1a1a;padding-bottom:10px;margin-bottom:24px}.top a{font-size:26px;font-weight:700;color:#1a1a1a;text-decoration:none}.k{font:600 12px/1 ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#7a1f1f}h1{font-size:36px;line-height:1.15;margin:10px 0}.cs{background:#EAE2D0;padding:12px 16px;margin:20px 0;font-size:16px}.btn{display:inline-block;background:#1a1a1a;color:#F4EFE3;padding:12px 20px;text-decoration:none;font:600 15px system-ui,sans-serif;margin:8px 0 20px}small,.m{font:14px/1.5 system-ui,sans-serif;color:#555}li{margin:6px 0;font:15px/1.5 system-ui,sans-serif}"
def body_of(x):
    out = []
    for p in x.get("paras") or []: out.append("<p>%s</p>" % e(p))
    for s in x.get("sections") or []:
        out.append("<h2>%s</h2>" % e(s.get("h")))
        for p in s.get("paras") or []: out.append("<p>%s</p>" % e(p))
    if not out and (x.get("summary") or x.get("body") or x.get("text")):
        out.append("<p>%s</p>" % e(x.get("summary") or x.get("body") or x.get("text")))
    return "".join(out)
def page(i, x, kind):
    title = x.get("title") or x.get("text") or i
    desc = clip(x.get("summary") or x.get("body") or x.get("why") or x.get("cs") or x.get("text") or title, 158)
    url = "%s/s/%s/" % (BASE, i)
    full = "%s/#story-%s" % (BASE, i)
    srcs = x.get("sources") or ([{"src": x.get("src") or "Source", "url": x.get("url")}] if x.get("url") else [])
    srcs = [s for s in srcs if str(s.get("url", "")).startswith("https://")]
    lis = "".join('<li><a href="%s" rel="noopener nofollow">%s</a></li>' % (e(s["url"]), e(s.get("src") or s["url"])) for s in srcs)
    date = e(x.get("date") or "") + (" " + e(x.get("year")) if x.get("year") else "")
    unk = "".join("<li>%s</li>" % e(u) for u in (x.get("unknowns") or []))
    ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": clip(title, 110), "description": desc, "mainEntityOfPage": url, "publisher": {"@type": "Organization", "name": "The Consultant Times", "url": BASE + "/"}}
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(clip(title, 90))} | The Consultant Times</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{e(url)}">
<meta property="og:type" content="article"><meta property="og:site_name" content="The Consultant Times"><meta property="og:title" content="{e(clip(title, 90))}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{e(url)}">
<script type="application/ld+json">{json.dumps(ld).replace("</", "<\\/")}</script><style>{CSS}</style></head><body><div class="w">
<div class="top"><a href="{BASE}/">The Consultant Times</a><br><small>Business news through a consultant's lens</small></div>
<div class="k">{e(x.get("kicker") or x.get("type") or x.get("lens") or kind)} · {date}</div><h1>{e(title)}</h1>
<p class="m">{e(x.get("confidence") or "")}{" · " + e(x.get("readTime")) if x.get("readTime") else ""}</p>
<a class="btn" href="{e(full)}">Open in the full site →</a>
{body_of(x)}
{('<div class="cs"><b>What it means:</b> ' + e(x["cs"]) + "</div>") if x.get("cs") else ""}
{("<h2>What we don't know yet</h2><ul>" + unk + "</ul>") if unk else ""}
{("<h2>Sources</h2><ul>" + lis + "</ul>") if lis else ""}
<p class="m">Written with AI under our <a href="{BASE}/#how-we-work">published editorial rules</a>. Not financial advice.</p></div></body></html>"""
shutil.rmtree("s", ignore_errors=True)
for i, (x, kind) in items.items():
    os.makedirs("s/" + i, exist_ok=True)
    open("s/%s/index.html" % i, "w", encoding="utf-8").write(page(i, x, kind))
today = datetime.date.today().isoformat()
urls = ['<url><loc>%s/</loc><lastmod>%s</lastmod><changefreq>daily</changefreq></url>' % (BASE, today)]
urls += ['<url><loc>%s/s/%s/</loc></url>' % (BASE, i) for i in items]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(urls) + "</urlset>\n")
print("pages:", len(items))
