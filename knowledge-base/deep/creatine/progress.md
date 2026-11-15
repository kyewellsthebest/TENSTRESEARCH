# Creatine deep dive — progress (resume point)

**Active topic:** creatine monohydrate (deep-dive queue #1). **Tier B** (full primary review), per `protocol.md`.
**Current phase:** 2 in progress (title/abstract screening): 4,000 of 4,587 screened (batches 001–020). **Next: batches 021–023 (the last 587), then the consistency pass.**

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
| Screened so far (batches 001–020, verified) | 4,000 |
| → include (trials + SR/MA mapping records) | 144 |
| → maybe (to full text) | 41 |
| → exclude (E03 1413, E02 1219, E06 654, E01 250, E07 167, E04 28, E12 25, E14 24, E05 14, E08 11, E13 5, E16 5) | 3,815 |
| **Still to screen** | **587** (all Semantic Scholar records, SS1-0251 onward; few have PMIDs) |

New-after-dedup per search is in `searches.csv`.

## Session log

| date | phase | what was done | last record screened | next |
|---|---|---|---|---|
| 2026-11-15 19:40 | 2 | Third extra round at Kye's request. Batches 019 (SP8-0303…SS1-0050: last PubMed records, Europe PMC preprints/theses/abstracts, first Semantic Scholar) and 020 (SS1-0051…SS1-0250) screened and cross-verified (seeds 20261115019/20261115020; 80 records re-checked; no exclude overturned, no rescue). Changes: 5 maybes → exclude in batch 019 (SP8-0349, SE2-0014, SE2-0046, SS1-0029, SS1-0034); SS1-0110 include → maybe. SS1-0105 and SS1-0115 had been included from the screener's memory; the verifier confirmed both designs from OpenAlex abstracts and open reviews (Syrotuik is 37 days, not 8 weeks). SP1-1142 recoded E05→E08 (primary report is SE5-0001). Abstracts were unavailable for about half of the Semantic Scholar records. This round: 18 include, 16 maybe, 366 exclude. | SS1-0250 | Batches 021–023 |
| 2026-11-15 19:27 | 2 | Second extra round at Kye's request. Batches 017 (SP7-0045…SP8-0100) and 018 (SP8-0101…SP8-0302) screened and cross-verified (seeds 20261115017/20261115018; 69 records re-checked). Batch 018: one flagged exclude (SP8-0219, rowers) changed to maybe after full text showed 30% gym RT, which triggered the **rescue rule**; 160 remaining excludes re-screened, 0 changed. Other changes: SP8-0157 maybe→include (full text: supervised RT twice a week), SP8-0210 maybe→E02 (mean age 17.4), SP8-0168 include→maybe (training not described), SP8-0072 maybe→E03 (full text: no RT in analysed sample). SP1-0698 (batch 004, same rower trial) reopened as maybe. This round: 14 include, 8 maybe, 378 exclude (plus SP1-0698 moved from exclude to maybe). | SP8-0302 | Batches 019–020, then the consistency pass below |
| 2026-11-15 19:14 | 2 | Extra round at Kye's request ("continue"). Batches 015 (SP2-2540…SP2-2779) and 016 (SP2-2780…SP7-0044) screened and cross-verified (seeds 20261115015/20261115016; 59 records re-checked, no exclude overturned, no rescue). Batch 016 held the SP6/SP7 renal-safety records: 7 include (5 renal/safety SR/MAs, 1 heat-tolerance SR/MA, Kreider 2003), 4 maybe. One maybe changed to E06 (SP7-0013 Juhn 1998, narrative). This round: 7 include, 4 maybe, 389 exclude. | SP7-0044 | Batches 017–018 |
| 2026-11-15 18:28 | 2 | Batches 013 (SP2-2064…SP2-2301) and 014 (SP2-2304…SP2-2539), all P2-only noise. Screened and cross-verified (seeds 20261115013/20261115014; 47 records re-checked, 47/47 agree, no rescue). This round: 0 include, 0 maybe, 400 exclude. | SP2-2539 | Batches 015–016 |
| 2026-11-15 16:28 | 2 | Batches 011 (SP2-1542…SP2-1811) and 012 (SP2-1812…SP2-2062), all P2-only noise. Screened and cross-verified (seeds 20261115011/20261115012; 48 records re-checked, 48/48 agree, no rescue). This round: 0 include, 0 maybe, 400 exclude. | SP2-2062 | Batches 013–014 |
| 2026-11-15 14:28 | 2 | Batches 009 (SP2-0997…SP2-1279) and 010 (SP2-1280…SP2-1541), all P2-only noise. Screened and cross-verified (seeds 20261115009/20261115010; 47 records re-checked, 47/47 agree, no rescue). This round: 0 include, 0 maybe, 400 exclude. | SP2-1541 | Batches 011–012 |
| 2026-11-15 12:28 | 2 | Batches 007 (SP2-0417…SP2-0720) and 008 (SP2-0722…SP2-0996), almost all P2-only noise. Screened and cross-verified (seeds 20261115007/20261115008; 50 records re-checked, 50/50 agree, no rescue). This round: 1 include (SP2-0978, Kley 2008 muscle-disorder MA, a companion of Cochrane CD004760), 0 maybe, 399 exclude. SR/MA rule clarified (population doesn't count). | SP2-0996 | Batches 009–010 |
| 2026-11-15 10:29 | 2 | Batches 005 (SP1-0940…SP2-0014) and 006 (SP2-0015…SP2-0413) screened and cross-verified (seeds 20261115005/20261115006; 59 records re-checked, no rescue). One change: SP1-1142 maybe→E05 (a cognition-only report; chase its companion). A rule for SR/MAs was adopted (see conventions). Batch 006 was nearly all noise from P2 alone (1 include in 200). This round: 28 include, 3 maybe, 369 exclude. | SP2-0413 | Batches 007–008 |
| 2026-11-15 08:28 | 2 | Batches 003 (SP1-0469…SP1-0713) and 004 (SP1-0715…SP1-0938) screened by agents A and B, then cross-verified (seeds 20261115003/20261115004; 61 records re-checked). Batch 003: one flagged exclude (SP1-0660, age unreported) changed to maybe, which triggered the **rescue rule**. All 158 remaining excludes were re-screened and none changed. Batch 004: SP1-0917 (a multi-drug PED umbrella review) changed from include to E03, for consistency with SP1-0511/SP1-0655. Both maybes in batch 003 changed to include (SP1-0533 Galvan 2016, checked in full text; SP1-0637 renal review). This round: 30 include, 1 maybe, 369 exclude. | SP1-0938 | Batches 005–006 |
| 2026-11-15 06:28 | 2 | Batches 001 (SP1-0004…SP1-0229) and 002 (SP1-0230…SP1-0468) screened by agents A and B, each 200 records with PubMed abstracts. Cross-verification: A checked B's batch and B checked A's, re-screening all maybes, a seeded 10% of excludes (seeds 20261115001/20261115002) and the screener-flagged borderline excludes. 60 records re-checked; 0 excludes overturned (no rescue needed); 4 maybes resolved (1 include, 3 exclude). Merged into `records.csv`. | SP1-0468 | Batches 003–004 |
| 2026-11-15 04:28 | 1 | Protocol written (APPRAISAL.md §2 defaults: adults 18–50, hypertrophy ≥6 wk, strength ≥4 wk, thresholds, E01–E16). PubMed P1–P8, Europe PMC E1–E6, Semantic Scholar S1 run and logged. Merged into `records.csv` (5,553) with auto-filters. | none (screening not started) | Phase 2 batch 1 |

## Screening conventions agreed in batches 001–002 (keep them consistent)
- Acute, single-session or loading-only studies (shorter than the protocol minimum) with exercise: **E07**. Creatine with no structured RT programme at all: **E03**.
- Co-ingredient trials are **included** when the comparator gets the same co-ingredients (e.g. Cr+whey vs whey). A multi-ingredient product vs plain placebo is **E14**. Creatine in every arm (form or timing comparisons) is **E04**.
- Creatine-specific SR/MAs are included as mapping records even in clinical populations. Multi-treatment reviews of a disease are E02.
- Samples aged mainly >50 (e.g. 48–72, 55–70) are E02. If the age isn't reported in the abstract, mark maybe (decided at full text).
- **SR/MA rule (adopted 2026-11-15 10:29):** keep a creatine-specific SR/MA as a mapping record whenever its eligibility criteria could admit a trial meeting our PICOS (human creatine vs placebo/no creatine, RT co-intervention not excluded), whatever its outcomes or population. If its own criteria rule out any such trial, code it E05 (e.g. SP1-1040, cognition in people 55+ that excludes RT). Creatine plus a co-ingredient SR/MA (beta-alanine, HMB) counts as creatine-specific. **Clarified 12:28:** for this rule only the intervention, comparator and design parts of the PICOS count. A creatine-specific SR/MA restricted to a clinical or older population is still kept as a mapping record, as in batches 001–008 (e.g. SP1-0223/0340/0410, SP2-0978), because mapping records only feed citation chasing.
- A partial age overlap is decided at screening if the abstract reports both mean and range (e.g. SP1-1114, mean 54.5: E02). It goes to maybe only if age isn't reported.
- Multi-supplement or multi-drug SR/MAs that aren't creatine-specific are E03, but list them as citation-chasing sources (SP1-0511, SP1-0655, SP1-0917, SP1-1083, SP1-1066, SP1-1024, SP1-1034, SP1-1097, SP1-1130, SP1-0946, SP2-1280 Candow 2012, SP2-1059, SP2-1266, SP2-1677, SP2-1825, **SP2-2273** (SR/MA of nutrition + RT in older adults: creatine subgroup of 4 trials, LBM MD 2.61 kg, 95% CI 0.51 to 4.72; chase all 4), SP2-2075 (Cochrane SMA multi-drug review), SP2-2840 (EFSA 2016 opinion on creatine + RT in adults over 55), SP2-2656 (Bonilla 2024 opinion), SP6-0014 (Meuffels 2022), SP7-0013 (Juhn 1998 narrative side-effects review)).
- Plyometric-only training with no RT outcome is E05 (SP1-0521); E03 is also defensible.

## Links to resolve at full text / citation chasing
- SP1-0050 is probably a companion of SP1-0036 (Volek 1999/2000). Check for E08.
- SP1-0063 and SP1-0179 (excluded E05, signalling only) are Hespel-cohort companions of SP1-0082. Re-code as E08 if SP1-0082 is included.
- SP1-0118 and SP1-0131 (E05) are likely secondary reports of cohorts with muscle outcomes elsewhere. Chase them.
- SP1-0143 (maybe) and SP1-0235 (maybe) are the same rugby HMB+Cr cohort. Screen them together; one may be E08.
- SP1-0553 (E05; Hayward whey+omega-3+Cr, 4 wk) has a likely companion report with body composition. Chase it.
- SP1-0718 (E04; HMB+Cr vs Cr, rugby) may share a sample with SP1-0143/SP1-0235.
- The SP1-0757/SP1-0793 (Candow, older) and SP1-0575 (Bell, older) cohorts are excluded E02; their companion reports are excluded too.
- Wang creatine/PAP papers SP1-0532, SP1-0591 and SP1-0638 (included): check for sample overlap.
- SP1-0533 (Galvan 2016, creatine nitrate; included): check whether 1RM is reported or only bar power.
- SP1-1142 (E05; Baker 2026, perimenopausal women, Cr + 6 wk HIRT, cognition only): chase its body-composition/strength companion and recode as E08 if found.
- SP2-0336 (Earnest 1995; included with no abstract): confirm the 28-day duration and placebo at full text, and check overlap with SP7-0010 (Earnest 1996).
- SP2-0978 (Kley 2008, JNNP MA) is the journal companion of Cochrane CD004760 (SP1-0223/0340/0410). Link them and count as one review.
- Adverse-event context (excluded, for discussion only): SP2-0566 (stroke, MaHuang + creatine), SP2-0909 (rhabdomyolysis, creatine overuse), SP2-1770 (Jatoi 2017 cancer RCT, n=263, AEs similar), SP2-2039 (ALS, 30 g/d, more AEs and discontinuation).
- Measurement context: SP2-1762 (Bone 2017) shows creatine loading raises total body water by about 1.4% and shifts DXA lean mass. Use it for F-TIMING judgements at the risk-of-bias stage.
- SP2-1026, SP2-1235 and SP2-1265 are versions of one Cochrane SMA multi-drug review (E02; includes one creatine trial in children).
- Correction notices: SP1-1089 corrects SP1-1046; SP1-1101 corrects SP1-1090. Read both corrections at full text.
- **Renal block (batch 016).** SP6-0011, SP6-0018, SP6-0019 and SP6-0021 are four overlapping renal meta-analyses; do the overlap check at AMSTAR 2. SP6-0003 (Lopez 2009, heat/hydration SR/MA) is included on its abstract only; recode E05 if its full-text criteria restrict to acute exercise-in-heat trials. SP6-0020 (adolescent safety SR) is included for mapping only and is weak (PubMed only, 5 studies).
- SP7-0022 (Kreider 2003, included for safety outcomes only, ROBINS-I): confirm RT at full text. It is a different cohort from SP1-0116 (Mayhew 2002). Its likely companions are the Greenwood 2003 injury reports: PMID 12701814 (not in records.csv; add at citation chasing) and SP8-0047. Check all three for cohort overlap.
- Maybes needing full text that the proxy blocked (Europe PMC has no XML; PMC and publisher pages returned 403): SP7-0014 Poortmans 1999, SP7-0015 Robinson 2000, SP7-0041 Cancela 2008, SP7-0031 Shi 2005. Try again at phase 4 via other routes; if still unreachable, code E11 (awaiting).
- Renal-safety context, excluded E03 (no RT), not pooled: SP7-0038 Gualano 2008 (3-month RCT with aerobic training, cystatin C 0.82→0.71 mg/L creatine vs 0.88→0.75 placebo, n=18), SP7-0011 Poortmans 1997 (5-day loading), SP7-0029 (ALS, about 310 days), SP7-0042 (Parkinson's, 2 years), SP2-2705 (children with FSHD, creatinine +12.6 µmol/L).
- SP6-0001/0002/0004/0006 are four versions of one Cochrane McArdle review (E02). SP7-0028 and SP7-0037 are probably one haemodialysis trial (E02).
- **Batch 017–018 links.** SP7-0132 (Kreider 2025) and SP7-0145 (Gonzalez 2026) are one review family (same 685-trial dataset; AlzChem paid the publication fee: F-COI); count once, and use Kreider 2025 Supplemental File 1 for citation chasing. SP8-0047 (Greenwood 2003, included for safety only; full text confirms RT 4 d/wk) is a likely companion of SP7-0022 and PMID 12701814. SP7-0050 = SP8-0117 (Gualano 2011, type 2 diabetes, E02; measured GFR unchanged: renal context). SP8-0040 (E05) is the SP1-0143/SP1-0235 rugby cohort. SP8-0133 = SP8-0172; SP8-0141/0146/0175 one cohort (E07).
- SP7-0097 (Zajac 2020, included): magnesium creatine chelate, not monohydrate; S&C twice a week, content not described; creatinine 1.87 mg/dL at week 4 needs a careful read.
- SP8-0157 (Claudino 2014, included): body mass is the only eligible outcome. SP8-0255 (Wu 2022 scoping review, 16 RCTs on muscle growth) is the best citation-chasing source in batch 018.
- Maybes with no reachable full text: SP7-0095, SP8-0013, SP8-0091, SP8-0127 (try other routes at phase 4, else E11).
- **Batch 019–020 links.** SE5-0001 (Delbiondo 2026 preprint, included) is the primary report of the trial behind SP1-1142 (now E08); flags: preprint, the abstract's conclusion leans on a 0.38 kg difference with p=0.999 (F-SPIN), senior author advises creatine companies (F-COI). SE2-0011 (Krieger/Kerksick 2025 abstract, included) has a strength companion SS1-0419 in a later batch. SS1-0115 (Syrotuik 2000, included; 37 days, so strength only) has a thesis companion SS1-0136 (maybe; likely E08) and SS1-0475. SS1-0207 is probably a secondary report of SS1-0165. SS1-0220 (Cribb thesis, maybe) is probably the parent of SP1-0225/SP1-0250. SE2-0025 (E03) has a published version SS1-0479: give it the same code. SS1-0030 = SS1-0119; SS1-0072 = SS1-0036; SE6-0023 = SE6-0024.
- Included on thin evidence, to check first at full text: SE2-0005 (preprint, about 4 per arm, no placebo), SS1-0050 (conference-abstract SR; E13/E10 if no full paper), SS1-0162 and SS1-0165 (TLDR only), SS1-0080/SS1-0250/SS1-0160/SS1-0196 (check venue, F-PRED), SS1-0208 and SS1-0250 (randomisation not stated).
- SS1-0054 is the whole NSCA 2015 abstract book (E13): hand-search for creatine abstracts at citation chasing if wanted. SS1-0139 (Norwegian VKM safety opinion) and SS1-0217 (Forbes 2025 narrative review) are citation-chasing sources.
- SP1-0076 (include) has an electrical-stimulation co-stimulus and unsupervised voluntary training. Flag F-SUPERV.

## Open issue: "RT not stated" in athlete samples (found 2026-11-15 19:27)
Batches 001–005 excluded creatine-vs-placebo trials in athletes as **E03** when the abstract named no RT programme. From batch 016 on, such records were marked **maybe**. The SP8-0219 / SP1-0698 rower trial shows the abstract can hide a gym RT component. To make the screening consistent:
1. **Consistency pass (do after the last screening batch, before phase 3).** Re-screen every earlier E03 exclude whose reason is "creatine but no or unstated RT programme" in a healthy athlete or active sample with at least 4 weeks of creatine vs placebo. `screening/consistency-pass-candidates.json` holds a first keyword-based list (66 record ids) to start from; check each against Europe PMC full text where open, and move to maybe unless the abstract or full text positively rules RT out. Log it as a verification pass.
2. **Operational definition of "structured RT programme" (proposed; apply at full-text eligibility, phase 4).** The protocol requires creatine "combined with a structured RT programme" but does not say how much RT embedded in sport or occupational training counts. Proposed rule, written before any effect sizes were extracted: RT counts when the full text shows both arms performed resistance exercise (named exercises or a gym/strength session) at least once a week for the whole intervention, prescribed or supervised by the study or team. Flag F-SUPERV and F-EQUATE where the content is not described, and treat such trials as indirect for the trained-lifter subgroup. "Habitual training", sport practice only, or unspecified "conditioning" does not count (E03). This decides SP7-0097 (Zajac), SP8-0219/SP1-0698 (rowers), SP8-0168 (military police) and similar records. Record it in `protocol.md` as a dated clarification when phase 4 starts.

## Abstract retrieval for Semantic Scholar records (learned in batches 019–020)
- Semantic Scholar's batch API returns an abstract for only about a third of these records. **OpenAlex DOI lookups still work** even when its search budget is exhausted (`https://api.openalex.org/works/https://doi.org/<doi>`, field `abstract_inverted_index`); use that next, then Crossref, then Europe PMC.
- Semantic Scholar's one-line "TLDR" is machine-written and sometimes wrong. It may support a decision but must be named in `ta_reason`; never include a study on a TLDR or on memory alone without marking "design unverified".
- Publisher, J-STAGE and university-repository pages are blocked by the proxy. Thesis and conference-abstract maybes mostly cannot be resolved here; at phase 4 code them E11 (awaiting) if still unreachable.

## Non-English records that look eligible on content (E12, count only; report in the synthesis)
SS1-0124 (Korean, soldiers, 4 wk combined exercise + creatine vs placebo), SS1-0192 with companion SS1-0011 (Korean, football players, 5 wk strength training), SS1-0078 (Portuguese, creatine vs placebo, strength; design unverified). SS1-0097 (Portuguese SR) and SS1-0026 (Spanish SR in vegetarians; its three trials are already accounted for) would be mapping records if English.

## Efficiency note
(The P2-only records were finished in batch 016.) Records found only by P2 (no supplement term) are almost all noise (batch 006: 1 include in 200). They are still screened in full for recall, but a screener can decide most of them on the title alone.

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
