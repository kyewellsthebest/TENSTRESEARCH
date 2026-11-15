# Search log: PubMed (agent 1, phase 1)

This is the human-readable copy. `searches.csv` is the authoritative log (PRISMA-S columns). The Europe PMC and
OpenAlex searches are logged by agent 2 in `search-log-europepmc-openalex.md`.

## Searches

All searches were run on **2026-11-15** against PubMed through the NCBI E-utilities:
- `esearch.fcgi`, by POST, with `retmax=10000` and `retmode=json`;
- metadata by `efetch` XML, in batches of 200 PMIDs, ≤3 requests/s, with retry on HTTP 429.

No date, language or species limits were used, except the `NOT (animals NOT humans)` written into P3, P7 and P8.

The PMID lists for every query are in `raw/pubmed-esearch-ids.json`.

| id | database | string (full text in searches.csv) | date | hits | records retrieved |
|---|---|---|---|---|---|
| P1 | PubMed | creatine block AND RT/outcome block AND supplement block (brief base string, unchanged) | 2026-11-15 | 1,145 | 1,145 |
| P2 | PubMed | P1 without the supplement block (sensitivity) | 2026-11-15 | 4,091 | 4,091 |
| P3 | PubMed | APPRAISAL §3.2 Cochrane highly sensitive RCT filter, exactly as written | 2026-11-15 | 567 | 567 |
| P4 | PubMed | §3.2 creatine + RT blocks AND SR/MA filter | 2026-11-15 | 73 | 73 |
| P5 | PubMed | P2 blocks AND SR/MA filter | 2026-11-15 | 171 | 171 |
| P6 | PubMed | creatine AND renal block AND supplement AND SR/MA filter (supplementary) | 2026-11-15 | 26 | 26 |
| P7 | PubMed | creatine AND renal block AND supplement AND Cochrane RCT filter (supplementary) | 2026-11-15 | 234 | 234 |
| P8 | PubMed | creatine AND athlete/training block AND supplement AND Cochrane RCT filter (supplementary) | 2026-11-15 | 839 | 839 |

**Union of the PubMed set: 4,617 unique PMIDs**, written to `raw/pubmed.csv`:
- P1–P5 give 4,091. P1, P3, P4 and P5 are all strict subsets of P2, so P2 alone gives the 4,091.
- P2 adds 2,946 records beyond P1.
- P6–P8 add 526 more: P6 adds 22 and P7 adds 165 beyond P1–P5; P8 adds 355 beyond P1–P7.

**Syntax notes:**
- No syntax changes were needed.
- PubMed reported no phrases ignored and no quoted phrases not found.
- PubMed mapped `"fat free mass"` to `"fat-free mass"` and `"meta-analy*"` to `"meta analy*"`. The full query
  translations are in `raw/pubmed-esearch-ids.json`.

**P3 count discrepancy:**
- APPRAISAL.md states that P3 gave 477 hits on 2026-11-15. Today it gave **567**. We could not reproduce 477:
  - without the `NOT` line, 602;
  - without the RT MeSH term, 521;
  - with `creatine[mh]` added, 571.
- The source of the 477 is unknown. It may have been run with a different string or interface.

## Profile of the 4,617 records (from PubMed metadata; not screening)

- **MeSH indexing:** Humans = yes 3,091, no 802, not yet indexed 724 (in-process or publisher-supplied records, mostly
  recent).
- **No DOI:** 345 records.
- **Language:** non-English 150 records (`language` field without `eng`).
- **Publication types** (a record can have several): RCT 851, Clinical Trial 319, Review 392, Systematic Review 168,
  Meta-Analysis 104, Case Reports 384.
- **Data problem:** one record, PMID 42896019, has an empty title. It is an NTP technical report on benzotriazoles in
  rats (a book record) and will be excluded at screening as E01.

## Recall check against the earlier survey (`notes/2026-11-15-creatine-studies.csv`, 22 keys)

The check matched on DOI against `raw/pubmed.csv`. For misses, the DOI was searched in PubMed (`<doi>[doi]`), or by
title, to confirm whether the paper is indexed.

| key | PMID | in P1–P5? | in final set? | queries |
|---|---|---|---|---|
| AshtaryLarky2025 | 41433021 | yes | yes | P1–P5 |
| Desai2024 | 39074168 | yes | yes | P1, P2, P4, P5 |
| Wang2026 | 42765482 | yes | yes | P1, P2, P4, P5 |
| Burke2023 | 37432300 | yes | yes | P1–P5 |
| Kazeminasab2025 | 40944139 | yes | yes | P1–P5 |
| Lanhers2017 | 27328852 | yes | yes | P1, P2, P5 |
| Lanhers2015 | 25946994 | yes | yes | P1, P2, P5 |
| Gu2026 | 42027564 | yes | yes | P1, P2, P4, P5 |
| vanderMerwe2009 | 19741313 | yes | yes | P1, P2 |
| Lak2025 | 40265319 | yes | yes | P1, P2, P3 |
| Lugaresi2013 | 23680457 | yes | yes | P1, P2, P3 |
| Antonio2013 | 23919405 | yes | yes | P1, P2, P3 |
| Dinan2022 | 36465581 | yes | yes | P1, P2, P3 |
| Forbes2021 | 34610729 | yes | yes | P1, P2, P3 |
| Syrotuik2004 | 15320650 | yes | yes | P1, P2 |
| Tsiaras2026 (renal MA) | 42035842 | **no** | yes | P6, P7 |
| deSouzaAlmeida2026 (renal MA) | 42507286 | **no** | yes | P6, P7 |
| Naeini2025 (renal MA) | 41199218 | **no** | yes | P6, P7 |
| Kreider2003 (athletes, safety; non-randomised) | 12701816 | **no** | yes | P7, P8 |
| Xu2024 (cognition MA) | 39070254 | no | no | — |
| Prokopidis2023 (cognition MA) | 35984306 | no | no | — |
| Hultman1996 (muscle loading kinetics, no RT) | 8828669 | no | no | — |

**Result:**
- All 15 efficacy papers in scope (the RT meta-analyses and RT trials) were captured by P1, including every paper named
  in the brief: Burke 2023, Kazeminasab 2025, Lanhers 2017, Desai 2024, Wang 2026 (indexed, PMID 42765482), Antonio
  2013 and Syrotuik 2004.
- **The misses, and why:**
  1. **The three renal meta-analyses** don't mention RT, strength or body composition in their title or abstract, so
     the RT/outcome block excludes them. Renal markers are a pre-specified secondary outcome, so we added P6 and P7.
     Both recover all three.
  2. **Kreider2003** describes "athletes" (college football players), not RT terms. P8 (athlete/training terms) and P7
     recover it. Its DOI isn't stored in PubMed, so a DOI search finds nothing; it was found by author, year and title.
  3. **Xu2024 and Prokopidis2023** (cognition) and **Hultman1996** (creatine loading kinetics, no RT) are out of scope
     by design (E05/E03). Missing them is expected, so no fix was added.

## Problems

- E-utilities returned occasional HTTP 429 (rate limit) responses. Each was retried and succeeded; all 4,617 PMIDs
  have metadata.
- The P3 hit count doesn't match APPRAISAL.md's stated 477 (see above).
- P6–P8 are an amendment made by agent 1 after the recall check and before any screening. The coordinator may drop
  them: rows found only by P6–P8 have `query_ids` made only of P6/P7/P8, and there are 526 of them.
