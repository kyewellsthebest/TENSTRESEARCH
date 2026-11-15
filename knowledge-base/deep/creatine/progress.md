# Creatine deep dive — progress (resume point)

**Active topic:** creatine monohydrate (deep-dive queue #1). **Tier B** (full primary review), per `protocol.md`.
**Current phase:** 1 complete (protocol + search + dedup + auto-filter). **Next: phase 2, title/abstract screening.**

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
| **Records left for title/abstract screening** | **4,587** |

New-after-dedup per search is in `searches.csv`.

## Session log

| date | phase | what was done | last record screened | next |
|---|---|---|---|---|
| 2026-11-15 | 1 | Protocol written (APPRAISAL.md §2 defaults: adults 18–50, hypertrophy ≥6 wk, strength ≥4 wk, thresholds, E01–E16). PubMed P1–P8, Europe PMC E1–E6, Semantic Scholar S1 run and logged. Merged into `records.csv` (5,553) with auto-filters. | none (screening not started) | Phase 2 batch 1 |

## Instructions for the next round (phase 2)

1. **Screen titles and abstracts** of records with an empty `ta_decision`, in `record_id` order. Use batches of about 200
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
