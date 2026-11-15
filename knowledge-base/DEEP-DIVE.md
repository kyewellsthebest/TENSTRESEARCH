# Deep-dive mode: one topic, every study, rigorously filtered (from 2026-11-15)

Kye wants depth, not quick skims. Each topic is therefore researched **exhaustively over many rounds**, the way a
systematic review is done, before the worker moves to the next topic. The screening and quality rules are in
**`APPRAISAL.md`**, and every phase follows it.

## Folder per topic: `knowledge-base/deep/<topic-slug>/`

| file | what |
|---|---|
| `protocol.md` | The question (PICO), eligibility rules, outcomes, and the exact search strings per database. Written before searching. |
| `search-log.md` | Every search run: database, string, date, number of hits. |
| `records.csv` | **Every record found**, deduplicated (often thousands). Columns: id (PMID/DOI), title, year, journal, pub_type, source_db, screen_stage, decision, exclusion_reason. |
| `included.csv` | Studies that passed full-text eligibility, with the extraction fields from `APPRAISAL.md`. These cover participants (n, sex, age, body mass, height, BMI/body fat, training status and years, baseline strength), diet (energy, protein g/kg, whether intake was controlled, recorded or matched), drug use, supplements, adherence, supervision, training equated, duration, outcome measures and method, results with effect size and CI, funding and conflicts of interest. |
| `rob.csv` | Risk of bias per included study (RoB 2 domains for RCTs, ROBINS-I for non-randomised, plus TESTEX score). Overall: low, some concerns or high. |
| `meta-analyses.csv` | Existing meta-analyses appraised with AMSTAR 2, and how much their included studies overlap. |
| `synthesis.md` | Results per outcome; sensitivity analyses (low-risk-of-bias only, trained only, diet-controlled only); moderators (training status, sex, age, body mass, protein intake, dose, duration); GRADE certainty per outcome; plain-English verdict; what's still unknown. |
| `progress.md` | Which phase the topic is in, the counts at each funnel stage, and what the next round should do. |

## Phases (a topic usually takes several rounds)

1. **Protocol and search.**
   - Write `protocol.md`.
   - Run the full search in PubMed (E-utilities: esearch/efetch, retrieving all PMIDs, not just the first page), Europe
     PMC and OpenAlex.
   - Deduplicate into `records.csv`.
   - Log counts in `search-log.md`.
2. **Screening.**
   - Apply automated filters first: humans, publication type, language. Record the reason for every exclusion.
   - Then screen titles and abstracts **in batches**, one batch per agent per round.
   - Check a random 10% of each batch's exclusions again. Keep going until all records are screened.
3. **Citation chasing.**
   - Search the reference lists of the included studies and of the key meta-analyses (backward).
   - Search the papers that cite them (forward), using OpenAlex or Semantic Scholar.
   - Screen any new hits.
4. **Full text, extraction and risk of bias**, in batches of about 15–25 studies per agent per round.
   - Read the full text from PMC or the publisher where it is open.
   - Fill in `included.csv` and `rob.csv`.
   - Run the data-integrity checks from `APPRAISAL.md`: retractions, registration versus reported outcomes, and
     implausible numbers.
5. **Synthesis and verdict.**
   - Write `synthesis.md` with GRADE certainty.
   - Pool effect sizes with Python only where the studies are similar enough.
   - Update the topic's **living page in `library/`**, `LATEST.md` and `TOPICS.md` (marked "deep-dive done").
   - Build the topic's PDF report in `reports/` or the deep folder.
6. **Audit.** An independent auditor agent re-checks a random sample of the screening decisions, extractions and
   risk-of-bias calls, plus every number in the verdict.

## Each round (2 agents)

- Read `progress.md` for the active topic, run the next phase, or the next batch of a phase, with the 2 agents,
  update every file, and push.
- When a topic reaches "deep-dive done", start the next one from the deep-dive queue below.
- Update the `library/` page with an interim "Draft — deep dive in progress (phase N)" verdict whenever the evidence
  changes.

## Access notes (tested 2026-11-15)
- **PMC full text:** `pmc.ncbi.nlm.nih.gov` may not resolve. Use Europe PMC instead:
  `https://www.ebi.ac.uk/europepmc/webservices/rest/{PMCID}/fullTextXML`.
- **Retraction checks:** use Crossref's `updated-by` / `update-to` fields, which carry Retraction Watch data. The
  retractionwatch.com site itself is blocked.
- **Citation chasing:** OpenAlex has a free daily limit. When it runs out, fall back to Semantic Scholar or the
  Europe PMC citations and references endpoints.
- **Blocked:** cochrane.org. Use the published RoB 2 and GRADE papers instead.

## Honest limits, to be stated in every synthesis

- Participant factors (weight, height, diet and so on) can only be accounted for **when studies report them**.
  Individual-level adjustment needs individual participant data, which is rarely available, so moderator analysis is
  done at study level. It shows associations, not individual causes.
- Screening is done by AI agents with spot checks, not by two independent humans. The audit samples the decisions
  to catch systematic errors.
- Full text is only available when it is open access. Studies read from the abstract alone are marked as such and
  tested in a sensitivity analysis.

## Deep-dive queue (in order)

1. Creatine monohydrate (already surveyed in round 1; now go exhaustive)
2. Protein intake: total daily dose and per-meal dose for muscle growth
3. Training volume (weekly sets) in trained lifters
4. Proximity to failure (effort)
5. Caffeine
6. Lengthened-position training / range of motion
7. Rest intervals
8. Energy deficit size and lean-mass retention in trained lifters
Further topics come from `TOPICS.md`; Kye can reorder this list at any time.
