# Protocol: creatine supplementation + resistance training (deep dive)

- Topic slug: `creatine`. Written 2026-11-15, before any screening. Follows `knowledge-base/APPRAISAL.md` §2–§4.
- **Budget tier: B (full primary review).** This is a deep dive and Kye wants trained-lifter estimates. Existing
  meta-analyses mix trained and untrained samples and rarely use direct muscle imaging, so they can't answer the
  narrower trained-lifter question. Meta-analyses are kept as records for mapping and phase-3 citation chasing, and are
  appraised with AMSTAR 2.
- **Date floor: none. Language limit: none at the search stage.** Non-English records are counted and coded E12 at
  screening.
- **Not registered.** There is no PROSPERO entry. This file is the frozen protocol. Any change after searching starts
  is logged in the amendment log at the bottom, with its date and reason.

## 1. Review question

In healthy adults doing a resistance-training programme, does creatine supplementation, compared with placebo or no
creatine under the same training, change:
- lean / fat-free mass;
- direct muscle size;
- maximal strength;
- and, secondarily, body mass, muscular endurance, renal markers and adverse events?

How big is each effect in resistance-trained lifters specifically?

## 2. PICOS

| element | decision |
|---|---|
| **P**opulation | Healthy adults **18–50 y**, any sex, any training status. **Trained** (≥1 y of consistent RT, as defined by the study) is reported separately as the key subgroup. Untrained samples are included but flagged as *indirect* for Kye. At screening, samples that are mainly 16–17 y or >50 y are **E02**; so are samples defined by a clinical disease. Studies whose age range only partly overlaps 18–50 are kept to full text and decided on the reported mean and range. |
| **I**ntervention | Creatine supplementation in any form (monohydrate is primary; other forms are a subgroup), any dose, with or without loading, any timing, **combined with a structured RT programme**. Creatine taken with co-ingredients counts only if the comparator gets the same co-ingredients (otherwise E14). |
| **C**omparator | Placebo (preferred) or no creatine, with **the same RT programme**. Different training between arms is E14. No control arm, or single-arm pre/post, is E04. |
| **O**utcomes | Listed in §4. |
| **S**tudy design | RCTs, parallel or crossover (crossover needs an adequate washout, judged at full text). Randomised within-subject unilateral designs are kept and flagged. SR/MAs are kept as mapping records (tagged by publication type) and are not pooled. Non-randomised controlled trials are kept only for the safety outcomes (renal, adverse events), appraised with ROBINS-I, and excluded from efficacy estimates. |
| **Duration** | **Hypertrophy and lean-mass outcomes: ≥6 weeks** of training plus supplementation (≥8 weeks preferred, tested in sensitivity analysis). **Strength and endurance outcomes: ≥4 weeks.** Renal markers and adverse events: ≥4 weeks. Below these is E07, applied per outcome. Example: a 5-week trial can give strength data but not hypertrophy data. |

## 3. Eligibility and reason codes

These are APPRAISAL.md §4.3 codes, used exactly. Each exclusion gets one primary code at full text.

**Include if all of these hold:**
- humans aged 18–50, healthy;
- creatine arm plus RT;
- matched placebo or no-creatine arm with the same RT;
- randomised;
- duration at or above the threshold for the outcome;
- at least one eligible outcome measured by an eligible method;
- peer-reviewed primary report (or a thesis or preprint with enough data, flagged).

| code | reason, as applied to this topic |
|---|---|
| E01 | Not human / in vitro / animal |
| E02 | Wrong population. Covers clinical disease (e.g. muscular dystrophy, CKD, cancer, sarcopenia clinics), mean age or range mainly <18 or >50 (including 16–17 y), and children. |
| E03 | Wrong intervention. Covers no creatine arm, creatine without an RT programme (including endurance or sport-only training with no RT), a creatine precursor only (e.g. GAA), and dietary creatine only. |
| E04 | Wrong or no comparator. Covers single-arm studies and comparisons only between creatine forms or doses with no placebo or no-creatine arm. |
| E05 | No eligible outcome, or an outcome not measured by an eligible method. Examples: cognition-only, acute performance-only, signalling-only. |
| E06 | Wrong design. Covers narrative reviews, editorials, case reports, cross-sectional studies, and acute single-session studies. |
| E07 | Duration below the minimum for that outcome (§2) |
| E08 | Duplicate or secondary report of an included study (link it to the primary report) |
| E09 | Retracted (Crossref `updated-by`, with PubMed's Retracted Publication as backup) |
| E10 | Insufficient data to extract, and the authors' data can't be obtained |
| E11 | Full text not accessible (record what was tried; keep it as "awaiting") |
| E12 | Non-English (count only) |
| E13 | Conference abstract or protocol only, with no results |
| E14 | Co-intervention confounds the comparison. Examples: creatine plus protein or carbohydrate versus a placebo without them, or different training between arms. |
| E15 | Predatory or non-peer-reviewed venue with no verifiable methods |
| E16 | Other (write it out) |

The following topics are excluded **at screening, not in the search**:
- cognition-only (E05);
- disease-only populations without RT (E02 or E03);
- acute single-session studies (E06 or E07);
- animal and in-vitro work (E01).

## 4. Outcomes and measurement hierarchy (APPRAISAL §2.2)

**Primary outcomes:**
1. **Lean / fat-free mass** (kg).
   - Hierarchy: DXA (rank 4) > BIA/BIS, air displacement, hydrostatic (rank 5). Skinfold-derived FFM is recorded but
     not pooled with DXA.
   - It is a **surrogate**: creatine raises intracellular water, so lean mass is downgraded for indirectness relative
     to tissue.
2. **Direct muscle size.**
   - Hierarchy: MRI/CT CSA or volume (rank 1) > ultrasound muscle thickness or CSA (rank 2) > biopsy fibre CSA
     (rank 3).
   - Pooled by method, never mixed with lean mass.
3. **Maximal strength.**
   - Hierarchy: 1RM in a trained lift > 1RM in an untrained lift > isometric or isokinetic torque.
   - Upper and lower body are analysed separately.

**Secondary outcomes:**
- body mass (kg; rank 6 measure, not a hypertrophy measure);
- fat mass or body-fat % (recorded);
- muscular endurance: reps to failure at a fixed load (effort-sensitive);
- renal markers: serum creatinine, eGFR, measured GFR (e.g. ⁵¹Cr-EDTA, iohexol), cystatin C, urea, urinary albumin or
  protein;
- adverse events: any reported event, GI, cramping, dropouts due to AEs.

The preferred effect is the between-group difference in change, with its 95% CI. Timing standardisation (fasting,
hydration, time since the last session, and DXA after creatine loading) is recorded as flag F-TIMING.

### Pre-specified thresholds (for GRADE imprecision and for the wording of verdicts)

These are our judgements, written before seeing the results, and they won't be moved afterwards.

| outcome | trivial | small | moderate | large | basis |
|---|---|---|---|---|---|
| Lean / fat-free mass, MD | <0.3 kg | 0.3–<1.0 kg | 1.0–<2.0 kg | ≥2.0 kg | APPRAISAL §2 example (0.3 kg). 0.3 kg is about 0.4% of a ~70 kg FFM, smaller than plausible DXA day-to-day noise. Upper cut-offs are our judgement. |
| Muscle thickness (ultrasound), MD | <0.1 cm, or <2% of baseline | 0.1–<0.2 cm (2–<5%) | 0.2–<0.4 cm (5–<10%) | ≥0.4 cm (≥10%) | Our judgement. 0.1 cm is about 2–3% of a typical 3–5 cm elbow-flexor or quadriceps MT, and at or below the between-session error usually reported for ultrasound MT. Each study's own TE/MDC is checked when reported. |
| CSA or volume (MRI/CT/US), relative MD | <2% | 2–<5% | 5–<10% | ≥10% | Our judgement. It matches the MT bands in relative terms. 2% is below the ~2.7% early swelling-related CSA rise reported at week 3 [Damas2016, via APPRAISAL]. |
| 1RM, MD as % of baseline | <2% | 2–<5% | 5–<10% | ≥10% | APPRAISAL §2 example (2%). For Kye a 2% change is about 2–4 kg on main lifts. Upper cut-offs are our judgement. |
| Any outcome, SMD | <0.2 | 0.2–<0.5 | 0.5–<0.8 | ≥0.8 | Cohen's conventional bands, used only when natural units can't be pooled |
| Serum creatinine, MD | <0.3 mg/dL (26.5 µmol/L) is not clinically meaningful in itself | — | — | — | 0.3 mg/dL is the KDIGO AKI creatinine-rise criterion. Creatine raises creatinine without injury, so creatinine is a surrogate; **measured GFR or cystatin C decides any renal verdict**. |
| Measured GFR / eGFR(cystatin), MD | decline <10 mL/min/1.73 m² | — | — | — | Our judgement; flagged as a judgement in synthesis |

## 5. Pre-specified subgroups and moderators (study level; observational; ~10 studies per covariate needed)

Each moderator is tested by subgroup interaction or meta-regression only when there are enough studies. Results are
hypotheses, not findings (ecological fallacy; APPRAISAL §7.2).

1. **Training status:** trained (≥1 y RT) versus untrained or not stated. This is the primary moderator.
2. **Sex:** male, female, or mixed (by proportion female).
3. **Age:** mean age, continuous, within 18–50.
4. **Body mass:** baseline body mass (continuous) and dose relative to body mass (g/kg/d).
5. **Protein intake:** mean g/kg/d (continuous), plus whether protein was matched between arms.
6. **Dose and loading:** loading phase versus maintenance only; maintenance dose (g/d); total cumulative dose.
7. **Duration:** weeks, continuous; 6–8 versus >8 weeks for the hypertrophy outcomes.
8. **Diet control level:** APPRAISAL §7.2 levels 1–4; ≥3 versus ≤2.
9. **Creatine form:** monohydrate versus other forms.
10. **Measurement method** for lean mass: DXA versus other.

**Sensitivity analyses:**
- low risk of bias only;
- excluding high risk of bias;
- trained only;
- diet-controlled only (level ≥3);
- FULL-text-only (excluding ABSTRACT-only studies);
- double-blind only;
- excluding preprints and theses;
- ≥8 weeks only for the hypertrophy outcomes.

## 6. Appraisal and synthesis tools (APPRAISAL §6, §9)

- **RoB 2** for RCTs (parallel and crossover variants), judged per outcome.
- **ROBINS-I** for non-randomised studies kept for the safety outcomes.
- **TESTEX** (0–15) as an add-on for every training trial.
- **AMSTAR 2** for SR/MAs, plus an overlap check of their included studies.
- APPRAISAL §6.2 flags (F-BLIND, F-DIET, F-DRUGS, F-TIMING, F-COI and the others).
- §6.3 integrity checks: retraction, registration versus reported outcomes, GRIM/statcheck, baseline plausibility.
- **Pooling:**
  - random-effects MD in natural units, with the 95% CI, I² and a 95% prediction interval;
  - pooled by measurement method;
  - crossover and unilateral designs use paired SEs or are narrated;
  - funnel plot and Egger's test only with ≥10 studies.
- **GRADE** per outcome, against the thresholds above. Lean mass is downgraded for indirectness (water) unless
  direct-imaging data agree. Untrained-only evidence is downgraded for indirectness when applied to Kye.

## 7. Search strategy (run 2026-11-15; no date or language limits)

There's no access to Embase, Web of Science, SPORTDiscus or Google Scholar, so expect lower recall than a formal
review (APPRAISAL §3.1). We compensate with three databases plus phase-3 citation chasing.

### 7.1 PubMed (E-utilities `esearch.fcgi`, POST, retmax 10000; all PMIDs retrieved)

**P1 (base):**
```
(creatine[tiab] OR creatine[mh] OR "creatine monohydrate"[tiab]) AND ("resistance training"[mh] OR "resistance training"[tiab] OR "resistance exercise"[tiab] OR "strength training"[tiab] OR "weight training"[tiab] OR "weight lifting"[mh] OR "weight lifting"[tiab] OR weightlifting[tiab] OR bodybuild*[tiab] OR "lean mass"[tiab] OR "fat-free mass"[tiab] OR "fat free mass"[tiab] OR "muscle mass"[tiab] OR hypertroph*[tiab] OR "muscle thickness"[tiab] OR "cross-sectional area"[tiab] OR "muscle strength"[mh] OR "muscle strength"[tiab] OR "1RM"[tiab] OR "one repetition maximum"[tiab] OR "body composition"[mh] OR "body composition"[tiab]) AND (supplement*[tiab] OR "dietary supplements"[mh])
```

**P2 (sensitivity):** P1 with the final `AND (supplement*[tiab] OR "dietary supplements"[mh])` block removed.

**P3 (APPRAISAL §3.2 Cochrane highly sensitive RCT filter, exactly as written):**
```
creatine[tiab] AND ("Resistance Training"[MeSH] OR "resistance training"[tiab] OR "strength training"[tiab] OR "weight training"[tiab] OR "weight lifting"[tiab] OR "resistance exercise"[tiab]) AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomized[tiab] OR placebo[tiab] OR drug therapy[sh] OR randomly[tiab] OR trial[tiab] OR groups[tiab]) NOT (animals[mh] NOT humans[mh])
```

**P4 (§3.2 blocks with the SR/MA filter):**
```
creatine[tiab] AND ("Resistance Training"[MeSH] OR "resistance training"[tiab] OR "strength training"[tiab] OR "weight training"[tiab] OR "weight lifting"[tiab] OR "resistance exercise"[tiab]) AND (systematic review[pt] OR meta-analysis[pt] OR "systematic review"[tiab] OR "meta-analy*"[tiab])
```

**P5:** P2 `AND (systematic review[pt] OR meta-analysis[pt] OR "systematic review"[tiab] OR "meta-analy*"[tiab])`.

**P6–P8:** supplementary recall-fix strings, added before screening. See the amendment log. Their exact strings are in
`searches.csv`.

The PubMed set is the union P1 ∪ … ∪ P8. `raw/pubmed.csv` holds one row per PMID, and `query_ids` lists every query
that returned it.

### 7.2 Europe PMC (REST `search`; run by agent 2, whose log has the exact calls)

```
(creatine) AND ("resistance training" OR "resistance exercise" OR "strength training" OR "weight training" OR weightlifting OR "weight lifting" OR bodybuilding OR "lean mass" OR "fat-free mass" OR "muscle mass" OR hypertrophy OR "muscle thickness" OR "cross-sectional area" OR "muscle strength" OR "one repetition maximum" OR "body composition") AND (supplement OR supplementation OR supplemented)
```

This includes preprints (SRC:PPR is flagged, not excluded). APPRAISAL §3.2 also asks for a PUB_TYPE-filtered run and
an unfiltered run; agent 2 documents these.

### 7.3 OpenAlex (`/works`; run by agent 2)

A `title_and_abstract.search` filter for `creatine`, combined (AND) with the same concept list as 7.2:
- resistance training, resistance exercise, strength training, weight training, weightlifting, weight lifting,
  bodybuilding;
- lean mass, fat-free mass, muscle mass, hypertrophy, muscle thickness, cross-sectional area, muscle strength;
- one repetition maximum, body composition;
- supplement, supplementation, supplemented.

The exact API calls are in `search-log-europepmc-openalex.md`.

### 7.4 Later phases

- Phase 3: backward and forward citation chasing from the included trials and the key SR/MAs (OpenAlex, Semantic
  Scholar, Europe PMC citations).
- Trial-registry check (ClinicalTrials.gov, ANZCTR via WebSearch) for registered but unpublished trials.

## 8. Amendment log

| date | change | reason |
|---|---|---|
| 2026-11-15 | Population narrowed from the brief's "≥16 y adults" to 18–50 y. Duration split by outcome (hypertrophy ≥6 wk, strength ≥4 wk). Reason codes switched to APPRAISAL E01–E16. | APPRAISAL.md arrived mid-task; the coordinator said it overrides the brief. Done before screening. |
| 2026-11-15 | Added PubMed P3 (Cochrane RCT filter), P4 and P5 (SR/MA filter). | Coordinator instruction / APPRAISAL §3.2 |
| 2026-11-15 | Added supplementary PubMed P6 (renal SR/MA), P7 (renal-marker RCTs) and P8 (athlete/training RCTs). | Recall check: P1–P5 missed 3 renal meta-analyses (Tsiaras2026, deSouzaAlmeida2026, Naeini2025) and Kreider2003 (athletes; no RT terms in the abstract). Renal markers are a pre-specified secondary outcome. Added after searching but **before any screening**. Records found only by P6–P8 can be identified (and dropped) via `query_ids`. |
