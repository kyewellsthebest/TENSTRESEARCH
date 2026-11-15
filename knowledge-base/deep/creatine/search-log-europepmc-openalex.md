# Search log: Europe PMC, OpenAlex, Semantic Scholar (creatine deep dive, phase 1)

Run 2026-11-15 by search agent 2. Machine-readable rows are in `searches-epmc-oa.csv` (to merge into `searches.csv`). Raw records: `raw/europepmc.csv` (1,303 unique Europe PMC records from E2-E6), `raw/semanticscholar.csv` (1,832 records from S1). `raw/openalex.csv` was **not created** because OpenAlex was blocked (see O1). Nothing screened.

| id | database | exact string / URL | date | hits | records retrieved | notes |
|---|---|---|---|---|---|---|
| E1 | Europe PMC | `(creatine) AND ("resistance training" OR "resistance exercise" OR "strength training" OR "weight training" OR weightlifting OR "weight lifting" OR bodybuilding OR "lean mass" OR "fat-free mass" OR "muscle mass" OR hypertrophy OR "muscle thickness" OR "cross-sectional area" OR "muscle strength" OR "one repetition maximum" OR "body composition") AND (supplement OR supplementation OR supplemented)` | 2026-11-15 | 31701 | 0 (count only) | COUNT ONLY, not retrieved: unrestricted fields include OA full text, inflating hits. Exact task query. |
| E2 | Europe PMC | `TITLE_ABS:creatine AND (TITLE_ABS:"resistance training" OR TITLE_ABS:"resistance exercise" OR TITLE_ABS:"strength training" OR TITLE_ABS:"weight training" OR TITLE_ABS:weightlifting OR TITLE_ABS:"weight lifting" OR TITLE_ABS:bodybuilding OR TITLE_ABS:"lean mass" OR TITLE_ABS:"fat-free mass" OR TITLE_ABS:"muscle mass" OR TITLE_ABS:hypertrophy OR TITLE_ABS:"muscle thickness" OR TITLE_ABS:"cross-sectional area" OR TITLE_ABS:"muscle strength" OR TITLE_ABS:"one repetition maximum" OR TITLE_ABS:"body composition") AND (TITLE_ABS:supplement OR TITLE_ABS:supplementation OR TITLE_ABS:supplemented)` | 2026-11-15 | 943 | 943 | Primary Europe PMC record set (task query restricted to title/abstract with TITLE_ABS:). All records retrieved. No 500s/retries. new_after_dedup = records not already returned by earlier E queries (key id+source); not deduplicated against PubMed. |
| E3 | Europe PMC | `TITLE_ABS:creatine AND (TITLE_ABS:"resistance training" OR TITLE_ABS:"resistance exercise" OR TITLE_ABS:"strength training" OR TITLE_ABS:"weight training" OR TITLE_ABS:weightlifting OR TITLE_ABS:"weight lifting" OR TITLE_ABS:bodybuilding OR TITLE_ABS:"lean mass" OR TITLE_ABS:"fat-free mass" OR TITLE_ABS:"muscle mass" OR TITLE_ABS:hypertrophy OR TITLE_ABS:"muscle thickness" OR TITLE_ABS:"cross-sectional area" OR TITLE_ABS:"muscle strength" OR TITLE_ABS:"one repetition maximum" OR TITLE_ABS:"body composition") AND TITLE_ABS:supplement*` | 2026-11-15 | 1015 | 1015 | Sensitivity variant: supplement* truncation catches supplements/supplementing. Superset of E2; 72 extra records kept, tagged E3. new_after_dedup = records not already returned by earlier E queries (key id+source); not deduplicated against PubMed. |
| E4 | Europe PMC | `TITLE_ABS:"creatine" AND (TITLE_ABS:"resistance training" OR TITLE_ABS:"strength training") AND PUB_TYPE:"randomized controlled trial"` | 2026-11-15 | 177 | 177 | APPRAISAL.md 3.2 Europe PMC string (RCT pub-type filter). new_after_dedup = records not already returned by earlier E queries (key id+source); not deduplicated against PubMed. |
| E5 | Europe PMC | `TITLE_ABS:"creatine" AND (TITLE_ABS:"resistance training" OR TITLE_ABS:"strength training")` | 2026-11-15 | 578 | 578 | APPRAISAL.md 3.2 string without PUB_TYPE (indexing incomplete). E4 is a subset. new_after_dedup = records not already returned by earlier E queries (key id+source); not deduplicated against PubMed. |
| E6 | Europe PMC | `SRC:PPR AND TITLE_ABS:creatine AND (TITLE_ABS:"resistance training" OR TITLE_ABS:"resistance exercise" OR TITLE_ABS:"strength training" OR TITLE_ABS:"weight training" OR TITLE_ABS:weightlifting OR TITLE_ABS:"weight lifting" OR TITLE_ABS:bodybuilding OR TITLE_ABS:"lean mass" OR TITLE_ABS:"fat-free mass" OR TITLE_ABS:"muscle mass" OR TITLE_ABS:hypertrophy OR TITLE_ABS:"muscle thickness" OR TITLE_ABS:"cross-sectional area" OR TITLE_ABS:"muscle strength" OR TITLE_ABS:"one repetition maximum" OR TITLE_ABS:"body composition")` | 2026-11-15 | 86 | 86 | Preprint check (SRC:PPR); no supplement block for sensitivity. 46 preprints not found by E2-E5. new_after_dedup = records not already returned by earlier E queries (key id+source); not deduplicated against PubMed. |
| O1 | OpenAlex | `https://api.openalex.org/works?filter=title_and_abstract.search:creatine%20AND%20(%22resistance%20training%22%20OR%20...)&per-page=200&cursor=*` | 2026-11-15 | n/a | 0 | BLOCKED: HTTP 429 "Rate limit exceeded / Insufficient budget" - free daily budget shared by this IP used up ($0 remaining, retryAfter ~70143 s, resets midnight UTC). Retried once; stopped per APPRAISAL 3.1. No API key used (would need user email - privacy). Not run; no records. Semantic Scholar used instead (S1). |
| S1 | Semantic Scholar | `creatine + ("resistance training" | "resistance exercise" | "strength training" | "weight training" | weightlifting | "weight lifting" | bodybuilding | "lean mass" | "fat-free mass" | "muscle mass" | hypertrophy | "muscle thickness" | "cross-sectional area" | "muscle strength" | "one repetition maximum" | "body composition") + (supplement | supplementation | supplemented)` | 2026-11-15 | 1832 | 1832 | All 1832 retrieved. One HTTP 429 retried after backoff, then succeeded. new_after_dedup = records with no DOI/PMID match to the Europe PMC set (952 matched); approximate, title-only matches not checked; not deduped vs PubMed. No language field in S2. |

## Counts

- Europe PMC, all fields (full text included): **31,701** hits (E1, count only).
- Europe PMC, same query restricted to title/abstract: **943** hits, all retrieved (E2). This is the Europe PMC record set; E3-E6 add 360 more, total 1,303 unique (by id+source).
- Europe PMC sources in the file: MED 1,171; PPR (preprints) 86; PMC 18; PAT (patents) 12; AGR 9; ETH (theses) 7. Languages: eng 1,202; blank 86 (preprints); a handful rus/spa/por/jpn and others.
- OpenAlex: not run (budget exhausted for this IP).
- Semantic Scholar bulk: **1,832** hits, all retrieved; 952 match a Europe PMC record by DOI or PMID.

## Recall check (known key papers)

| paper | DOI | Europe PMC | Semantic Scholar |
|---|---|---|---|
| Burke 2023, regional hypertrophy MA (Nutrients) | 10.3390/nu15092116 | found (E2, E3, E5) | found |
| Lanhers 2017, upper-limb strength MA (Sports Med) | 10.1007/s40279-016-0571-4 | **MISS** | **MISS** |
| Lanhers 2015, lower-limb strength MA (extra check) | 10.1007/s40279-015-0337-4 | **MISS** | **MISS** |
| Antonio 2013, pre vs post workout creatine (JISSN) | 10.1186/1550-2783-10-36 | found (E2, E3) | found |
| Syrotuik 2004, responders vs nonresponders (JSCR) | 10.1519/12392.1 | found (E2, E3) | found |
| Desai 2024, strength gains in adults <50 y (Nutrients) | 10.3390/nu16213665 | found (E2, E3, E5) | found |

**Why Lanhers is missed:** both Lanhers papers are indexed in Europe PMC (PMIDs 27328852, 25946994) but their title/abstract say "strength performance" and do not contain any concept-block phrase ("muscle strength", "strength training", "resistance training", etc.). The concept block has no bare `strength` term. Suggest adding `strength` (or `"strength performance"`) / `"1RM"` / `power` to the concept block in a later round, or relying on citation chasing; check whether the PubMed search catches them.

## Problems

- OpenAlex blocked by shared-IP daily budget (HTTP 429). Not retried further; needs a run after midnight UTC or an API key (which needs the user's email, so not requested).
- Europe PMC: no 500 errors this run; no retries needed.
- Semantic Scholar: one 429, succeeded on retry.
- `TITLE_ABS:creatine` also matches "creatine kinase" papers, so expect many off-topic records at screening.
- The exact task query uses `supplement` without truncation; E3 shows truncation adds 72 records.
