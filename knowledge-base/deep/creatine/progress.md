# Creatine deep dive — progress (resume point)

**Active topic:** creatine monohydrate (deep-dive queue #1). **Tier B** (full primary review), per `protocol.md`.
**Current phase:** 2 in progress (title/abstract screening): 400 of 4,587 screened (batches 001–002). **Next: batches 003–004.**

## Funnel so far (PRISMA counts)

| stage | count |
|---|---|
| Records identified: PubMed (P1–P8 union) | 4,617 |
| Records identified: Europe PMC (E2–E6, title/abstract set) | 1,303 |
| Records identified: Semantic Scholar bulk (S1) | 1,832 |
| Records identified: OpenAlex (O1) | not run (HTTP 429 – IP daily budget exhausted) |
| **Total source rows** | **7,752** |
| Duplicates removed (DOI 2,028; PMID 125; title+year+first author 46) | 2,199 |
| **Unique records (`records.csv`)** | **5,553** |
| Auto-filter E01 animal-only (MeSH animals without humans) | 787 |
| Auto-filter E12 non-English (count only) | 148 |
| Auto-filter E06 editorial/comment/letter/erratum only | 19 |
| Auto-filter E09 retracted (PubMed "Retracted Publication") — all off-topic | 7 |
| Auto-filter E16 patent records | 5 |
| **Records for title/abstract screening** | **4,587** |
| Screened so far (batches 001–002, verified) | 400 |
| → include (trials + SR/MA mapping records) | 46 |
| → maybe (to full text) | 10 |
| → exclude (E06 112, E03 84, E02 72, E07 46, E01 11, E14 9, E04 6, E05 4) | 344 |
| **Still to screen** | **4,187** |

New-after-dedup per search is in `searches.csv`.

## Session log

| date | phase | what was done | last record screened | next |
|---|---|---|---|---|
| 2026-11-15 06:28 | 2 | Batches 001 (SP1-0004…SP1-0229) and 002 (SP1-0230…SP1-0468) screened by agents A and B, each 200 records with PubMed abstracts. Cross-verification: A checked B's batch and B checked A's, re-screening all maybes, a seeded 10% of excludes (seeds 20261115001/20261115002) and the screener-flagged borderline excludes. 60 records re-checked; 0 excludes overturned (no rescue needed); 4 maybes resolved (1 include, 3 exclude). Merged into `records.csv`. | SP1-0468 | Batches 003–004 |
| 2026-11-15 04:28 | 1 | Protocol written (APPRAISAL.md §2 defaults: adults 18–50, hypertrophy ≥6 wk, strength ≥4 wk, thresholds, E01–E16). PubMed P1–P8, Europe PMC E1–E6, Semantic Scholar S1 run and logged. Merged into `records.csv` (5,553) with auto-filters. | none (screening not started) | Phase 2 batch 1 |

## Screening conventions agreed in batches 001–002 (keep them consistent)
- Acute, single-session or loading-only studies (shorter than the protocol minimum) with exercise: **E07**. Creatine with no structured RT programme at all: **E03**.
- Co-ingredient trials are **included** when the comparator gets the same co-ingredients (e.g. Cr+whey vs whey). A multi-ingredient product vs plain placebo is **E14**. Creatine in every arm (form or timing comparisons) is **E04**.
- Creatine-specific SR/MAs are included as mapping records even in clinical populations. Multi-treatment reviews of a disease are E02.
- Samples aged mainly >50 (e.g. 48–72, 55–70) are E02.

## Links to resolve at full text / citation chasing
- SP1-0050 is probably a companion of SP1-0036 (Volek 1999/2000). Check for E08.
- SP1-0063 and SP1-0179 (excluded E05, signalling only) are Hespel-cohort companions of SP1-0082. Re-code as E08 if SP1-0082 is included.
- SP1-0118 and SP1-0131 (E05) are likely secondary reports of cohorts with muscle outcomes elsewhere. Chase them.
- SP1-0143 (maybe) and SP1-0235 (maybe) are the same rugby HMB+Cr cohort. Screen them together; one may be E08.
- SP1-0076 (include) has an electrical-stimulation co-stimulus and unsupervised voluntary training. Flag F-SUPERV.

## Instructions for the next round (phase 2)

1. **Screen titles and abstracts** of records with an empty `ta_decision`, in file order (next unscreened is the first empty row after SP1-0468). Use the workflow from batches 001–002: write `screening/batch-NNN-input.csv`, have each agent write `batch-NNN-decisions.csv`, cross-verify into `batch-NNN-verify.csv`, then merge into `records.csv`. Use batches of about 200
   per agent, with two agents per round (for example, agent A takes the first 200 unscreened and agent B the next 200).
   - Fetch abstracts via PubMed efetch (by PMID), or via Europe PMC or Semantic Scholar for records without a PMID.
   - Write `ta_decision` (include/exclude/maybe), `ta_reason` (E-code plus a few words) and `screened_by`
     (agent/round id) after **every** batch.
   - Be generous: if unsure, mark maybe.
   - Expect a lot of creatine-kinase and animal noise, plus clinical populations (E02).
2. **Verification pass** (APPRAISAL §4.2):
   - In a separate agent, re-screen all maybes plus a seeded random 10% of each batch's excludes. Record the seed
     and fill `verified_by`.
   - If that pass rescues any eligible record, re-screen all of that batch's excludes.
3. **Still owed from phase 1:**
   - Run **OpenAlex (O1)** once the IP budget resets (after 00:00 UTC). Merge any new records with
     `merge_records.py` (run as `python3 merge_records.py .` from this folder; extend it to read `raw/openalex.csv`): the dedup order is DOI, then PMID, then title+year+author.
     Give new records ids `SO1-xxxx`.
   - **Optional fix-up search** with a bare `strength` / `"strength performance"` term in Europe PMC. The Lanhers
     2015 and 2017 meta-analyses were missed by Europe PMC and Semantic Scholar, but PubMed found both.
4. **Retraction check:** Crossref `updated-by` is deferred to full-text stage (included studies only). Only the
   PubMed retracted pub-type filter has been applied so far.
5. **Grey literature:** search ClinicalTrials.gov and ANZCTR for registered creatine + RT trials, via WebSearch,
   at phase 3.

## Known gaps (state in the synthesis)
- No Embase, Web of Science, SPORTDiscus or Google Scholar access, and OpenAlex is still pending.
- 724 PubMed records have no MeSH tags yet, so the animal auto-filter could not apply to them. They are screened
  manually.
- Single-AI-reviewer screening, with a 10% verification sample.
