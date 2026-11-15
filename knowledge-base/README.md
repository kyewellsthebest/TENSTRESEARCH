# Muscle & training knowledge base — grows daily

A scheduled research task runs once a day. Each run:
1. Takes the next **1–2 open topics** from `TOPICS.md` (top of the queue first).
2. Sends **2 research agents** to the literature, then **1 independent auditor** to check them.
3. Appends verified studies to `STUDIES.csv`, writes a findings note to `notes/<date>-<topic>.md`, updates the
   topic's status and the plain-English verdict in `TOPICS.md`, logs the run in `LOG.md`, and builds a short PDF
   digest in `digests/`.
4. **Keeps the queue growing.** Each research note ends with 2–4 "New avenues": follow-up questions it uncovered.
   The best of these are added to `TOPICS.md` as new open topics. If fewer than 10 topics are open, the run does a
   topic-discovery step: it scans the last 12 months of meta-analyses and RCTs (PubMed / Europe PMC) and the main
   sports-science journals, plus popular lifting claims with no verdict yet, until at least 15 topics are open.
   Once a month it re-checks an older verdict for new studies.
5. Commits and pushes to `main` of this repo (kyewellsthebest/TENSTRESEARCH).

## Evidence rules (every run)

- **Sources.** Read full text where possible, from PubMed / PMC / Europe PMC / Crossref / DOIs, which are allowed
  in the `d1coder` environment. Google Scholar blocks automated access, so it is not used.
- **No fabrication.** Never invent studies, numbers or DOIs. Mark access FULL, ABSTRACT or SECONDARY.
- **Ranking.** Meta-analyses and RCTs first. Trained-lifter evidence is weighted above untrained, and longitudinal
  outcomes above acute signalling.
- **Interpreting results.** Report effect sizes and uncertainty. Fact-check striking claims. Check for
  retractions. Flag industry funding.
- **Safety.** No dosing or sourcing for unapproved or banned substances. Supplements are covered only where legal
  and evidence-based.
- **Audience.** Plain-English verdicts for Kye (87 kg, 13.6% body fat, trains heavy about 1.5 h a day,
  intermediate–advanced).

## Files

| file | what |
|---|---|
| `TOPICS.md` | The research queue with status and current verdict per topic |
| `STUDIES.csv` | Every study recorded, deduplicated, with audit verdicts |
| `notes/` | One findings note per topic per run |
| `digests/` | One PDF per run |
| `LOG.md` | Run history (date, topics, studies added, issues) |

Earlier rounds (TENSR, top-5 factors, failure tracking, fat loss, peptides, binges) live in the repo root folders and count as done
for their topics.
