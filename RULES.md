# The Consultant Times — Editorial & Operations Rulebook

Every scheduled run MUST read this file first and follow it exactly. It is the single source of truth.
Founder/editor: Thomson Le (Vancouver, BCIT BITMAN). Site: https://theconsultanttimes.com/

> Precedence (cleanup 26 Nov 2026): later sections override earlier ones. In particular §16 (one credible source is enough) overrides every "2+ sources" line, §15e (How It Works weekly, Monday 10:00 run only) overrides any daily wording, and §17 (feeds, full stories, low-news days) overrides §15 where they differ.

## 1. Mission and audience
Business news through a consultant's lens. Every item answers: does this create client work, change an industry's
economics, or change how consulting itself works? Audience: from senior partners to consulting students.
One professional voice for everyone. Clear, specific, no hype, no slang.

## 2. Edition schedule
- Once a day at 10:00 PT. The 22:00 edition was dropped by the owner on 26 Nov 2026 (usage cost); §17d is retired. Fridays add a "Week in 60 seconds" Wire item and a LinkedIn draft (see §11).
- Once a week (Monday 10:00 run only; owner's rule, 18 Nov 2026): THREE new How It Works deep dives (see §6). They replace last week's three, which move to data/library.json. On all other runs, carry the current three forward unchanged and do not research or write new deep dives.
- Budget: build-up phase (until every page reaches its target, see §6f) 30–40 searches per run, otherwise 15–25. Keep runs lean either way. Search only for news since the last edition (`edition.published`).
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
- Big Moves = deals, IPOs, funding, earnings shocks, leadership changes, restructurings, partnerships, legal and governance matters; first item = move of the week. `type` must be exactly one of: M&A | Funding | IPO | Earnings | Leadership | Restructuring | Partnerships | Legal & Governance | Divestiture | Distress | Market Entry | Canada. A Canadian move keeps its event type and also sets `"canada": true` (so it shows under the Canada filter). Use "Legal & Governance" for investigations, lawsuits, fines and board probes (allegations stay allegations).
- Under the Radar (2–3) = heat ≤2 and relevance ≥4.
- Max 2 stories per firm per edition; at least 1 non–Big Four item.
Store `heat` and `rel` on items for ranking only.

## 6. Writing rules
- Write from a fact sheet (facts + source per fact), NOT from source text. Own words only.
- Quotes: at most one per source, under 15 words, attributed. Never reproduce paragraphs, lyrics, or article structure.
- Headlines < 12 words, specific, with the number or stakes. Summaries < 45 words.
- Attribute claims ("according to Reuters"). Estimates marked "est.", press-reported prices marked "reported".
- Opinion ONLY in `take` fields. Takes: lead + move of the week only (others only if genuinely sharp).
- Every story has a `cs` (shown as "What it means") line: which clients/roles will hire consultants because of this.
- EVERY item on the page (stories, Big Moves, Under the Radar, Vancouver Desk, Wire, How It Works) has an `id` and opens
  its own article page. Write in a Guardian-style feature voice: specific, well-structured, context-rich, never padded.
  Article depth is set by tier AND by how many verified facts exist. Never pad thin news with speculation; if facts run out,
  stop and say what is unknown.
  * Tier 1 (lead, 3 cards, move of the week): 800–1,200 words in `paras` (or `sections` [{h, paras}]), plus facts, why,
    unknowns, cs, sources (aim for 3+ sources, at least one primary). Lead and move of the week also get a `take`.
  * Tier 2 (other Big Moves, Under the Radar, Vancouver Desk stories): 300–600 words in `paras`, plus cs and 2+ sources.
  * Tier 3 (Wire items): 120–250 words in `paras` explaining the item and its context, plus the source link.
  * How It Works (ONCE A WEEK on the Monday 10:00 run, exactly 3 new deep dives, 1,400–2,400 words each (about double the launch length; validator minimum 1,300)). Each week has ONE of each `type`:
      - "Industry": how an industry works (economics, players, cost drivers, cycles), e.g. trucking, airlines, banking.
      - "Business": how one specific company works. It does NOT have to be big; any real business with enough public data
        (filings, annual reports, credible trade press) works, including small, local or Canadian ones.
      - "Strategy": a business-strategy, marketing or analysis framework (SWOT, Porter's Five Forces, market sizing, 4Ps, unit
        economics, etc.) explained clearly AND applied to a real company or industry with sourced numbers.
    Pick topics from data/backlog.json ({"industry":[],"business":[],"strategy":[]} lists of {topic,hook}); prefer reader suggestions
    from the form; at least one Canadian or B.C.-relevant topic per week; remove used topics and top each list up to 15+. These
    categories are internal guidance: the site just shows the `type` label (Industry / Business / Strategy).
    Research from primary sources first (annual report, 10-K/earnings release, regulator or industry-body data), then trade press.
    Fields: `id`, `type`, `sector`, `title`, `body` (2 sentences), `summary`, `ai`, `kicker` "How It Works", `firm`, `date`, `year`,
    `confidence`, `readTime`, `facts` (4 key numbers), `sections` [{h, paras}] (5+), then `caseq`, a structured MECE `caseAnswer`,
    `cheat` (6–8 one-line facts), and 4+ sources (at least one primary).
      Industry and Business headings in order: The short version; How it makes money; The economics; The number that runs the
      business; Where AI and automation hit; Who wins and why.
      Strategy headings: The short version; How to do it properly; A worked example (real company, sourced numbers); From
      analysis to choices; Common mistakes; Where AI and automation hit.
    Every number must come from a source; label our own arithmetic "computed". Never invent figures.
  * Library: before writing the new three, move last week's three full objects from edition.howItWorks into the FRONT of
    data/library.json ({"items":[...]}, newest first). Never delete library items. Ids must be unique across edition + library.
- Usage guard: if the run is running long, finish Tier 1 fully, then Tier 2, then Tier 3; a Tier 3 item may ship as a
  summary-only brief rather than delaying the edition. Carry over unchanged articles from the previous edition by id
  (do not rewrite them).
- "What we don't know yet" (`unknowns`) whenever key facts are missing. Never fill gaps with guesses.
- Confidence: "Confirmed" (official source), "Reported" (major/trade press), "Developing" (single/weak source).
- Times: include `time` (e.g. "9:40 AM PT") only if the source gives one. Never invent times.

## 6b. Category pages (each section has its own layout, filled automatically)
The site builds every category page from ALL items in the edition, so each page needs enough material. Every item (stories,
bigMoves, radar, wire, vancouver.stories) should carry `desk` (one of the 9 industry desks) and `firm` where relevant; stories
also carry `section`. Aim per edition: AI & Tools 8+ items, Big Moves 6 moves + 3 wire deals, Vancouver Desk 5–8 items
(at least 4 genuinely local B.C. items), firm pages: any firm named in an item is matched automatically, so name firms
precisely in titles/summaries. Industry desks: spread items across desks; avoid leaving a desk empty for a whole week.

## 6d. Industry desks and the consultant's lens (`deskNews[]`; `data/desks.json`)
Purpose: every desk page should read like a newspaper section and answer what a consultant would ask about an industry or company.
- Each run, every desk in DESKS gets fresh coverage. Target 4–6 `deskNews[]` items per desk, and no desk empty for more than a week. Search each desk by its own metrics (see `data/desks.json` `desks.<desk>.metrics`) and by the nine lenses.
- Lenses (field `lens`, exactly one of): Market size & growth | Profit pools & margins | Structure & competition | Demand & customers | Talent & operations | Regulation & policy | Technology & disruption | Capital & M&A | Risks & unknowns. Aim to cover several different lenses per desk, not five deals.
- Fields per item: `id` (slug), `kicker` "Industry desk", `firm` (company name if the story is about one company, else "Industry"), `desk`, `date` ("Nov 9"), `year`, `confidence`, `readTime`, `lens`, `title`, `summary`, `cs` (client signal), `paras` (2–3, 120–250 words total, own words), `facts[]` ({k,v}; 3+; only figures a source states, with the as-of date or "estimate"), `questions[]` (2+, what a client would ask), `unknowns[]` (1+), `dates[]` ({iso,label}, for upcoming events), `sources[]` (2+ https).
- Company stories answer the company checklist in `data/desks.json` (strategy, growth and margin, cash and debt, customers, cost base, leadership changes, deals, exposure, where consultants get hired) where sources allow. Never invent a number to fill a checklist item; put it in `unknowns`.
- Items older than 60 days are archived with kind "desk" (see archive procedure). Standing items with future `dates` stay until the last date passes.
- Government or company claims (for example a White House release) are labelled as claims in the text.

## 6e. Method guide (`data/guide.md`)
Read `data/guide.md` before drafting any How It Works piece or desk story. It holds the owner's business-acumen method: one master question per piece, the 60-second business-model test, the moat checklist, what every Industry piece must include, and number discipline. It is method only. Never publish unsourced "industry-typical" figures; cite a real source for every number.

## 6f. Volume targets and retention (owner's decision, 14 Nov 2026)
Every section page should look like a full newspaper section. Phase 1 targets (reach within about two weeks, then hold): each industry desk 10 items; AI & Tools 10 (new and updated software consultants use: Alteryx, Celonis, KNIME, Power BI, Tableau, process-mining and analytics tools, AI assistants, their releases and updates); Policy 10; Big Moves 10; Vancouver 10; each firm page 3. Phase 2 (only when the owner says so, after checking usage): 20 each, 5 per firm.
- Build-up: while a page is below target, add enough new items each run to close the gap (about 2–4 per page per day), prioritising pages that are empty. Never pad with stale or weak items; a short page with real items beats a full page of filler.
- Retention: items do NOT leave the edition just because a new day started. Keep each item on its page for 30 days (policy and desk items with a future `dates` entry stay until that date passes), then archive it. Front-page `stories[]` still turns over daily. When a page has more than 2x its target, archive the oldest first.
- Carry-forward: new runs start from the previous edition's arrays and add, update or archive items; they do not rebuild them from scratch.
- `data/status.json` records per-page counts each run so the next run knows where the gaps are.

## 6c. Policy & Regulation (own tab; `policy[]` in edition.json)
Purpose: government rules, funding and deadlines that create client work. AI policy first, then trade, tax, competition, privacy,
procurement and sector regulation that move business. 3–5 new items a day when there is news; never pad.
Jurisdictions to watch: Canada (federal and B.C.), United States (federal and states), EU and UK, plus major others (China, Australia).
Sources: official first (government releases, Canada Gazette, regulators, legislation sites, Federal Register), then major press, then law-firm
analysis (label stype "Research"). Cheap and free only.
Fields per item in `policy[]`: `id`, `kicker` "Regulation", `firm` "Industry", `desk` "Public sector", `juris` (Canada | B.C. | US | EU | UK | Global |
Rest of world | Other), `date`, `year`, `confidence`, `readTime`, `title`, `summary` (<45 words), `cs`, `paras` (200–450 words, 3–5 paragraphs), `unknowns`,
`sources` (2+, https), and `dates` [{iso:"YYYY-MM-DD", label}] for every FUTURE deadline, start date or consultation close (feeds the "On the calendar" box).
Neutrality: report what a law or agency says and who supports or opposes it; no opinion on parties or politicians; contested claims need two sources;
say what is not yet known. Check status before repeating a date from an earlier edition.
Standing items (laws not yet in force, open consultations) stay in `policy[]` until their last date passes, then are archived (kind "pol").
Other items (bigMoves, radar, wire) that are really policy should carry `juris` (and `dates`) so they appear on the Policy page too.
Run budget: 2–4 policy searches per run.

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
- Add Wire item tagged "Week in 60 seconds" linking to the five top stories (internal #story- links allowed as url "https://theconsultanttimes.com/#story-ID").
- Write a ~120-word LinkedIn post in Thomson's professional voice about the week's top story, with the article link,
  and save it as a Gmail DRAFT addressed to Thomson himself (Gmail create_draft only), subject
  "LinkedIn draft — The Consultant Times, week of YYYY-MM-DD". NEVER send it, never post anything anywhere,
  and never commit drafts to this public repository.

## 12. Data contract (data/edition.json) — see scripts/validate.py
Top-level: schema, edition{id,label,published,next}, lead (story id), stories[], wire[], caseOfDay{q,basedOn},
policy[], bigMoves[], radar[], deskNews[], vancouver{stories[],jobs[]}, howItWorks[3 — exactly: one Industry, one Business, one Strategy], archive[], corrections[].
Also data/library.json ({"items":[]}, past How It Works deep dives) and data/backlog.json ({"industry":[],"business":[],"strategy":[]}, each a list of {topic,hook}).
Story ids: lowercase-hyphen slugs, unique, stable across editions (articles keep their links).
ARCHIVE (nothing is ever deleted; old links must keep working): at the start of every run, compare the previous edition.json with
the new draft. Every item whose id is NOT in the new edition (stories, policy, deskNews, bigMoves, radar, wire, vancouver.stories) is copied in full
into data/archive/YYYY-MM.json (month of today; {"items":[...]}, newest first) with `kind` (story|pol|move|radar|wire|van|desk) and
`archivedOn` (YYYY-MM-DD) added. Add the month to data/archive/months.json if new. Items that stay on the page are not archived.
Use the same ids as before. Archive ids must be unique and must not overlap the live edition (validate.py checks this).
Leave edition.archive[] empty. How It Works items go to data/library.json instead (§6).

## 13. Run procedure (crash-safe)
1. Read RULES.md, data/guide.md, data/edition.json, data/status.json, data/backlog.json (if any).
2. Research (including each desk per §6d) → fact sheets → score → draft new edition into `data/edition.next.json`.
3. Independent check pass: re-open sources and verify every number, name, date, and URL in new/changed items. Fix or cut.
4. Run `python3 scripts/validate.py data/edition.next.json`. If it fails: fix and re-run once. If it still fails: do NOT
   publish; keep the current edition; write status {result:"failed", reason}; send a push notification "Edition failed".
5. On pass: copy current edition.json (and library.json) → last-good.json / keep a copy of library.json as library.prev.json, then move edition.next.json → edition.json, update status.json
   {last_run, result:"ok", edition}, commit with message "Edition YYYY-MM-DD" and push to main.
6. Send a push notification ONLY if items were held or the run failed.


## 14. Keep every page at 10 or more items (carry-forward)
- Every industry desk, Policy, Big Moves, AI & Tools and Vancouver page must hold at least 10 items after each run. Firm pages should hold 3 or more where possible.
- Never rebuild arrays from scratch. Start from the previous edition, add the new items, and when a page would drop below 10, keep the best older items (highest heat x relevance, newest first) until it is back at 10. Move only the items beyond the best 20 per page to the archive.
- Count items per desk across stories, policy, bigMoves, radar, wire and deskNews, using each item's `desk` value. Check counts before publishing and report any page under 10.
- Every article needs 2+ real https sources, in-prose attribution, and at most one quote under 15 words per source. Do not invent URLs; a page may stay short rather than publish an unsourced item.
- Site display: the `cs` field shows as "What it means". The first entry in `questions` shows as the "For your next interview" prompt, so write it as a question an interviewer could ask. The `facts` field is stored but no longer shown on article pages.
- Set `edition.next` to the next run time (e.g. "MON 10:00 AM PT" or "TODAY 10:00 PM PT").

## 15. Front page freshness (owner's rule, 18 Nov 2026)
- Every run (10:00 daily) must replace or recycle the front page. The lead and the three cards (the first four `stories`) must be news from the last 24 hours. Nothing older than 48 hours may stay in the lead or card slots.
- Before finishing, check the date of each of those four items. If any is stale, replace it with the best fresh item (highest heat x relevance, newest first) and move the stale item down the `stories` list (it keeps its id and page; do not archive it early).
- A new item that clearly beats the lead (see §5) becomes the lead in the same run. Do not wait for the next edition.
- Spend research effort on this first: look for fresh candidates (Big Four/MBB firms, Nvidia/AI, big M&A, CEO changes, earnings, policy) before refilling category pages. Fresh items still need 2+ real https sources and must pass the §7 hold rules.
- If fewer than four fresh, verifiable items exist, fill the slots with the freshest available and list in the final message which slots are stale and why.

### 15b. Many fresh items on the front page; older items live on category pages (owner's rule, 18 Nov 2026)
- The front page (`stories[]`, in addition to the lead and three cards) should carry as many fresh items as the run can verify: aim for 8-12 items from the last 24 hours, ordered newest and hottest first. Each run, add every fresh verified story, not just two or three.
- Front-page items older than 48 hours leave the front page (they drop out of the front `stories` order, or are moved out of `stories[]` into the array that matches their section: bigMoves, policy, deskNews, radar or wire). They keep their id and link and stay on their category page, which is built from all items by `desk`. Nothing is deleted; archive rules in §6f and §12 still apply.
- Every category page (the 9 industry desks, Policy, Big Moves, AI & Tools, Vancouver) must be refreshed each run with news from the last 24 hours, shown first. Search each desk for fresh items each run (use `data/desks.json` metrics) and add at least 1-3 new verified items per desk per run where they exist. Items older than 48 hours stay below the fresh ones, still at 10+ per page (§14).
- Fresh items need 2+ real https sources and must pass the §7 hold rules. If a desk has no fresh verifiable item, leave its older items in place and name the desk in the final message; never pad with weak or single-sourced items.
- Budget: this overrides the lean-search budget for the 10:00 run. Use up to 40 searches/fetches, spent first on the front page, then on each desk.

### 15c. Big Moves: what consultants care about (owner's request, 18 Nov 2026)
Big Moves is not just earnings. Each run, search every type below for news from the last 24 hours and add every verified item (aim for 10+ fresh Big Moves per run, newest first, each with 2+ sources):
- M&A, take-privates, mergers of equals, and hostile or contested bids (due diligence, integration, synergy work).
- Divestiture: carve-outs, spin-offs, asset sales, break-ups, business exits.
- Distress: bankruptcy and insolvency filings, creditor protection (CCAA/Chapter 11), restructuring support agreements, dissolutions and wind-downs, going-concern warnings, delistings, major debt exchanges.
- IPO / listings, SPACs, direct listings, secondary offerings, and Funding rounds of $100M+.
- Market Entry: entry into a new country, segment or category; large new plants, data centres and product lines; JV launches.
- Restructuring: layoffs, cost programmes, reorganisations, closures.
- Leadership: CEO/CFO/chair changes and activist campaigns.
- Partnerships: large alliances and supply or technology deals.
- Legal & Governance: regulatory actions, fines, major lawsuits, investigations (allegations stay allegations; §7 applies).
- Earnings only when there is a shock, a guidance change or a read-across to client work.
For each, `cs` must say what work it creates (for example, bankruptcy: turnaround, restructuring advisory, supply-chain contingency; divestiture: separation, TSA design; market entry: market sizing, go-to-market).

### 15d. Search returns headlines only: read the pages (owner's rule, 18 Nov 2026)
- WebSearch often returns titles and URLs without page text or dates. That is NOT a reason to carry the edition forward unchanged. Open the pages: use the `web-fetch` agent (or WebFetch) to read candidate articles and primary releases (company newsrooms, SEC filings, regulators) and build fact sheets from what was actually read.
- Pick candidates from search headlines, listing pages (consultancy.org, American Banker, company newsrooms) and wire-style roundups, then fetch each in batches (several URLs per agent call) to save time.
- If a page cannot be fetched, try a primary source or another outlet. Only if two sources cannot be read does the item stay out; say so in the final message.
- A run that publishes no new front-page item must state exactly why (which fetches failed) in `data/status.json` and the final message. "Search returned headlines only" is not an accepted reason by itself.

### 15e. How It Works cadence (owner's rule, 18 Nov 2026)
How It Works is weekly, not daily. New deep dives are written only on the Monday 10:00 run (if Monday is a holiday, the next weekday 10:00 run). Every other run keeps the three current deep dives in `howItWorks` and writes nothing new for them, which frees search budget for the front page, Big Moves and category pages (§15-15d). Keep backlog topics topped up to 15+ per list.

### 15f. Per-article pages for Google (owner's request, 18 Nov 2026)
After validation passes and before committing, run `python3 scripts/build_pages.py`. It writes one crawlable page per item to `s/<id>/index.html` and rebuilds `sitemap.xml`. Commit `s/` and `sitemap.xml` together with the edition files (include them in every "Edition" commit). Never hand-edit files under `s/`. The front page (`index.html`) is not touched by runs.

## 16. One credible source is enough (owner's decision, 18 Nov 2026)
This overrides every "2+ sources" requirement above (§6, §6c, §6d, §14, §15, §15c, §15d). An item may publish with ONE real https source if that source is credible: an official primary source (company newsroom, filing, regulator, government release) or a major or established trade outlet (Reuters, AP, Bloomberg, CNBC, BNN Bloomberg, Globe and Mail, FT, WSJ, NYT, CBC, Consultancy.org network, Business in Vancouver, etc.). Aggregators, blogs and listing-page excerpts alone do not count. A single-source item must be attributed in the text ("according to ...") and set `confidence` to "Reported" (or "Developing" if the source is a trade outlet reporting without confirmation). Not changed: the §7 HOLD rules (personal-conduct stories still need two major outlets; breaking scandals still start on the Wire), and How It Works still needs 4+ sources. Still read the page before writing; never write from a headline or excerpt alone.

### 15h. Big Moves tabs: five per type (owner's rule, 22 Nov 2026)
The Big Moves filter has no "All" tab; it opens on M&A. Every type tab (M&A, Funding, IPO, Earnings, Leadership, Restructuring, Partnerships, Legal & Governance, Divestiture, Distress, Market Entry, Canada) must always hold at least 5 items: one lead (highest `heat`, shown as the big card) and four smaller ones. Carry older verified items forward to keep each tab at 5; add fresh ones first. Canada counts items with `"canada": true`. Report any tab under 5.

### 15g. Headlines as leads; fetch permission (owner's rule, 25 Nov 2026)
- A headline or listing summary may be used as a lead and, when pages cannot be read, as a source for a short item. Never stop a run for "headlines only": first search for more sources on each headline and try to read them (use the `web-fetch` agent or WebFetch).
- An item built from a headline or summary alone must say so in its text, stay Tier 2/3 length, set `confidence` to "Reported" or "Developing", list what is unknown, and invent no facts beyond what the headline/summary states. Prefer a second source when one exists.
- §7 HOLD rules still override this: personal-conduct and allegation stories are never published from headlines alone.
- WebFetch on the consultancy.org network (consultancy.org/.uk/.eu/.asia, consulting.us/.ca) is permitted by the owner. If a fetch fails with PROVENANCE_REQUIRED, say so in status.json and use the headline route above rather than carrying the edition forward unchanged.

## 17. Feeds, full stories, low-news days (owner's rules, 26 Nov 2026)
### 17a. Feeds first
- Start every run from `data/feeds.json`: fetch each working feed (web-fetch agent or WebFetch; the shell cannot reach the web), keep items newer than `edition.published`, and use WebSearch only to fill gaps. Update `feeds.json` when a feed breaks or a new one is found and tested (say what was tested).
- Run `python3 scripts/seen.py <url> ...` on every candidate URL before fetching it. SEEN means it is already published; skip it unless it is a real update.
### 17b. A full story for every new headline
- Every new headline gets its source page opened and read, then written at its tier (§6): feed or listing text alone is not a story. Fetch in batches (several URLs per agent call).
- Headline-only items (§15g) are the exception, allowed only when the page cannot be fetched after trying a second outlet. Cap: at most 3 headline-only items per edition. If more candidates remain unread, leave them out rather than ship thin items.
### 17c. Low-news days and the front page
- If no item from the last 24 hours can be verified for a lead or card slot, the best verified item from the last 72 hours may take it, with `confidence` "Developing" if the facts are thin. Say in status.json which slots used this and why. This replaces the "freshest available, stale" fallback in §15.
### 17d. Retired
The 22:00 run no longer exists (owner's decision, 26 Nov 2026). If a run finds fewer than 2 verified new items, it still publishes per §2 (refresh Wire, careers board, dates).
