# Daily run procedure

Follow this every time you are asked to "do today's research run". Work autonomously and don't ask questions.

## Continuous mode (from 2026-11-15)
The worker is woken **every 2 hours** and runs until Kye says stop. (Changed 2026-11-15 from hourly with 4 agents to every 2 hours with 2 agents, to stay within Kye's Pro usage.)
- **Stop switch.** If the file `knowledge-base/STOP` exists, do nothing: reply "Stopped (STOP file present)" and end
  the turn. Kye can create that file on GitHub to stop the research without talking to Claude.
- **Overlap.** If a run is somehow still in progress (uncommitted notes from this hour), finish and commit that
  first; never run two rounds at once.
- **Usage limit.** If a run fails because the usage limit is reached, write nothing more. The next hourly wake
  continues once the limit resets.

## 0. Sync and re-read
- `git pull origin main`.
- Read `CLAUDE.md`, `knowledge-base/README.md`, `knowledge-base/TOPICS.md`, the last 10 rows of
  `knowledge-base/LOG.md`, and `agent-notes/SHARED-STANDARDS.md`.
- Never rely on memory from earlier runs; the repo is the source of truth.

## 1. Pick topics
- Take the first **two** topics marked "open" in `TOPICS.md`. Topics Kye added at the top come first.

## 2. Research (two background research agents in parallel, one per topic)
Brief each agent to:
- find the meta-analyses, RCTs and key trials, preferring trained lifters and longitudinal outcomes;
- use full text via PubMed E-utilities (eutils.ncbi.nlm.nih.gov), PMC (pmc.ncbi.nlm.nih.gov), Europe PMC REST
  (www.ebi.ac.uk/europepmc/webservices/rest), Crossref (api.crossref.org), doi.org, OpenAlex and Semantic Scholar,
  plus WebSearch;
- never invent studies, numbers or DOIs, and mark access FULL/ABSTRACT/SECONDARY;
- report effect sizes with uncertainty, fact-check striking claims and retraction status, and flag industry
  funding;
- give a plain-English verdict and a practical recommendation for Kye (87 kg, 13.6% body fat, trains heavy about
  1.5 h a day);
- give no dosing or sourcing for banned or unapproved substances.

Each agent writes `knowledge-base/notes/<YYYY-MM-DD>-<topic-slug>.md`, ending with a **"New avenues"** section of
2–4 researchable follow-up questions. It also writes a CSV of studies with this header (all fields quoted):

`key,topic,citation,doi_or_link,design,n,population,duration,intervention_comparison,outcome_measure,result_effect_uncertainty,limitations_coi,access,verification`

Budget: about 30 searches per agent.

## 3. Audit
- When both agents finish, launch one independent auditor agent.
- It verifies the load-bearing citations and numbers in both notes, plus a seeded random sample of 8 more rows.
- It appends an "Audit" section with corrections to each note.

## 4. Keep the queue growing
- Add the best "New avenues" to `TOPICS.md` under **Discovered**, tagged with the run date, skipping duplicates.
- If fewer than 12 topics are open, run **topic discovery** until at least 20 are open:
  - recent (last 12 months) meta-analyses and RCTs on resistance training, hypertrophy, strength, sports
    nutrition, body composition, supplements and recovery, found via PubMed or Europe PMC date-filtered searches;
  - the latest issues of Sports Medicine, MSSE, JISSN, JSCR, EJAP and Nutrients;
  - popular lifting claims that have no verdict here yet.
- Monthly (if `LOG.md` shows no "refresh" in 30 days): re-check one done topic older than 3 months for studies that
  would change its verdict.

## 5. Write up
1. Append the verified rows, adding a `run_date` column, to `knowledge-base/STUDIES.csv`. Deduplicate by DOI or key.
2. In `TOPICS.md`, mark each topic "done (<date>)" and add a 1–2 line plain-English verdict.
3. Add a `LOG.md` row: date, topics, studies added, new topics queued (and how many are open), issues.
4. Build a 3–8 page PDF digest at `knowledge-base/digests/<YYYY-MM-DD>-digest.pdf`. It contains the verdicts, key
   numbers, practical takeaways, the new avenues added and the study table. Use Python reportlab with DejaVu fonts;
   adapt `binge/make_binge_pdf.py`. Never use Unicode subscript characters.
5. Commit with a clear message and push to `main`. Retry up to 4 times on network errors.

## 5b. Update the library (Kye reads this, so it matters as much as the notes)
For each topic researched this round:
- Choose its category folder under `library/`: training, exercises, diet, fat-loss, supplements,
  peptides-and-drugs, recovery, body-measurement or tensr-product. Add a new category folder only if none fits.
- Create or update **one living page** `library/<category>/<topic-slug>.md`. It contains, in this order:
  - a **Verdict** line (confidence Strong / Moderate / Limited / Very limited, last-updated date, and "Draft" if not
    yet audited);
  - **What to do** — 2–5 practical bullets for Kye;
  - **Key numbers** — effect sizes with confidence intervals;
  - **Caveats**;
  - links to the dated note(s), the studies CSV and the digest PDF.

  If the page already exists, update the verdict and add the new evidence. Never delete earlier findings without
  saying why.
- Update that category's `README.md` index table: Topic | Verdict | Confidence | Page.
- Add an entry at the **top** of `LATEST.md`: date, topics, one-line verdict each, links to the pages and digest.
  Replace any "in progress" placeholder for the same round.

## 6. Finish
End with a 5–10 line summary:
- the topics researched;
- the headline verdicts;
- studies added;
- new topics queued and how many are open;
- anything that failed.
