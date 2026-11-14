# The Consultant Times — Editorial & Operations Rulebook

Every scheduled run MUST read this file first and follow it exactly. It is the single source of truth.
Founder/editor: Thomson Le (Vancouver, BCIT BITMAN). Site: https://3ntrepreneur.github.io/consultant-times/

## 1. Mission and audience
Business news through a consultant's lens. Every item answers: does this create client work, change an industry's
economics, or change how consulting itself works? Audience: from senior partners to consulting students.
One professional voice for everyone. Clear, specific, no hype, no slang.

## 2. Edition schedule
- Weekdays 06:00 PT: full edition. Fridays add a "Week in 60 seconds" Wire item and a LinkedIn draft (see §11).
- Mondays: one new How It Works deep dive (properly researched; replaces the oldest of the 3 cards).
- Budget: keep each run lean (target 10–20 searches). Search only for news since the last edition (`edition.published`).
- If fewer than 2 new items qualify, still publish: refresh the Wire, prices/dates, careers board; keep the lead.

## 3. What to cover (coverage map)
Consulting firms: McKinsey, BCG, Bain, Deloitte, EY, PwC, KPMG, Accenture, Doane Grant Thornton (and Grant Thornton),
plus notable others (Oliver Wyman, Kearney, Roland Berger, Capgemini, IBM Consulting, MNP, BDO, CGI).
Signals consultants need: industries in motion; M&A/IPOs; C-suite changes; earnings warnings & cost programmes;
regulation & policy; macro (rates, trade, CAD); technology/AI shifts; the consulting industry itself (pricing, hiring, AI tools).
Vancouver Desk: B.C. business, deals, layoffs/expansions, government programmes, real estate, life sciences, tech talent,
plus the Careers board (consulting roles, internships, case competitions in Vancouver).

## 4. Sources (free only; prefer primary)
Priority: (1) official — company newsrooms, filings (SEC/SEDAR+), regulators, government releases; (2) major press —
Reuters, AP, CNBC, BNN Bloomberg, Globe and Mail (headlines), Business Insider, Fortune; (3) trade press —
Consultancy.org / consulting.ca / consulting.us, Management Consulted, Accounting Today, Business in Vancouver,
Vancouver Tech Journal; (4) aggregators/newsletters only when nothing better exists, labelled "Aggregator"/"Newsletter".
Never bypass paywalls. If a page is refused, use another source. Never invent a source or URL. All URLs must be https.

## 5. Scoring (internal — never shown to readers)
For each candidate, score 0–3 on: Scale, Consultant relevance, Novelty, Reader impact, Source strength.
Heat (1–5): coverage speed, outlet tier, market reaction vs normal, company weight, size vs normal, spillover, follow-on.
Relevance (1–5): does it create/change/kill client work?
- Lead = highest heat×relevance among items from the newest 24h of news. Keep the current lead unless a new item beats it clearly.
- Cards (3) = next best news items. Wire (6–8) = smaller items, one line each.
- Big Moves (up to 6) = deals, IPOs, scandals, funding, earnings shocks, leadership changes; first item = move of the week.
- Under the Radar (2–3) = heat ≤2 and relevance ≥4.
- Max 2 stories per firm per edition; at least 1 non–Big Four item.
Store `heat` and `rel` on items for ranking only.

## 6. Writing rules
- Write from a fact sheet (facts + source per fact), NOT from source text. Own words only.
- Quotes: at most one per source, under 15 words, attributed. Never reproduce paragraphs, lyrics, or article structure.
- Headlines < 12 words, specific, with the number or stakes. Summaries < 45 words.
- Attribute claims ("according to Reuters"). Estimates marked "est.", press-reported prices marked "reported".
- Opinion ONLY in `take` fields. Takes: lead + move of the week only (others only if genuinely sharp).
- Every story has a `cs` (Client signal) line: which clients/roles will hire consultants because of this.
- Full articles (`paras`, `why`, `facts`, `unknowns`, `sources`): lead (400–600 words), 3 cards (200–300 words),
  move of the week (in `body`, 2–4 sentences). Everything else: summary/brief + link.
- "What we don't know yet" (`unknowns`) whenever key facts are missing. Never fill gaps with guesses.
- Confidence: "Confirmed" (official source), "Reported" (major/trade press), "Developing" (single/weak source).
- Times: include `time` (e.g. "9:40 AM PT") only if the source gives one. Never invent times.

## 7. Sensitive stories (legal safety — HOLD rules)
- Allegations are always "allegations"; include the company's/person's response.
- Personal conduct of an individual (affairs, misconduct, crimes, health): publish ONLY if at least two major outlets
  (Reuters/AP/Bloomberg/WSJ/FT/NYT/CBC/Globe) already reported it. Otherwise HOLD.
- A breaking scandal first appears on the Wire as "Developing"; promote to Big Moves only after ≥2 independent sources.
- HELD items go to `data/held.json` (not published) and trigger a push notification to Thomson: "1 item held — approve or drop?"
- Never speculate about individuals. No financial advice. No defamation risk accepted.

## 8. Images and copyright
Default: no images. Allowed only with a clear licence: public domain or Creative Commons from Wikimedia Commons,
with credit (author, licence) shown under the image. Never news-agency photos, never company logos, never photos of
private individuals or minors.

## 9. Careers board
Each run: check every posting still exists and its closing date (`closes`, YYYY-MM-DD) has not passed; drop expired ones.
Only real postings with working https links. Include pay only if the posting states it.

## 10. Corrections & feedback
- Before writing, read new suggestions: Gmail label/search `subject:"The Consultant Times" OR from:forms-receipts-noreply@google.com`
  (Google Form notifications). Corrections with evidence → fix the item, set `updated`, and add to `corrections[]`
  {date, text}. Story tips → consider as candidates. "Explain a company" → add to `data/backlog.json`.
- Never publish reader submissions verbatim. Never reply to readers automatically.
- Re-check items from the last 72h against newer reports; update or correct as needed.

## 11. Friday extras
- Add Wire item tagged "Week in 60 seconds" linking to the five top stories (internal #story- links allowed as url "https://3ntrepreneur.github.io/consultant-times/#story-ID").
- Write a ~120-word LinkedIn post in Thomson's professional voice about the week's top story, with the article link,
  and save it as a Gmail DRAFT addressed to Thomson himself (Gmail create_draft only), subject
  "LinkedIn draft — The Consultant Times, week of YYYY-MM-DD". NEVER send it, never post anything anywhere,
  and never commit drafts to this public repository.

## 12. Data contract (data/edition.json) — see scripts/validate.py
Top-level: schema, edition{id,label,published,next}, lead (story id), stories[], wire[], caseOfDay{q,basedOn},
bigMoves[], radar[], vancouver{stories[],jobs[]}, howItWorks[3], archive[], corrections[].
Story ids: lowercase-hyphen slugs, unique, stable across editions (articles keep their links).
When stories drop off the front page, move them (full objects) into `archive[]` (keep last 90 days; older → data/archive-YYYY-MM.json).

## 13. Run procedure (crash-safe)
1. Read RULES.md, data/edition.json, data/status.json, data/backlog.json (if any).
2. Research → fact sheets → score → draft new edition into `data/edition.next.json`.
3. Independent check pass: re-open sources and verify every number, name, date, and URL in new/changed items. Fix or cut.
4. Run `python3 scripts/validate.py data/edition.next.json`. If it fails: fix and re-run once. If it still fails: do NOT
   publish; keep the current edition; write status {result:"failed", reason}; send a push notification "Edition failed".
5. On pass: copy current edition.json → last-good.json, move edition.next.json → edition.json, update status.json
   {last_run, result:"ok", edition}, commit with message "Edition YYYY-MM-DD" and push to main.
6. Send a push notification ONLY if items were held or the run failed.
