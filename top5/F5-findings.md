# F5: Rest intervals, recovery between sessions, progression over time (nutrition and sleep as context)

Agent F5, 2026-11-02. Brief: `BRIEF.md`. Prior work: `../agent-notes/A1-findings.md` §12, `../agent-notes/A6-audit.md` C4.
Studies: `F5-studies.csv` (46 rows). Searches: `F5-searchlog.md` (29 WebSearch calls).

**Access, stated first.** WebFetch to `frontiersin.org` and `ncbi.nlm.nih.gov` failed DNS resolution. Those hosts would
have to be allowed in the session's network settings. **No full text was read.** Everything below comes from abstract or
summary text returned by WebSearch, so access is SECONDARY throughout. The included-study list of Singer 2024 was **not**
seen, so the overlap between its 9 studies and the primary trials listed here is inferred, not confirmed.

## Ten-line summary

1. **Rest interval is a real but small, mostly indirect lever.** Singer 2024 (Bayesian meta, 9 studies, 19 measurements):
   small benefit for rest >60 s, nothing appreciable beyond ~90 s. Pooled SMDs overlap heavily (short 0.48, CrI
   0.19–0.81; longer 0.56, 0.24–0.86). Most participants were untrained. (I, limited–moderate)
2. **The best mechanism evidence says short rest hurts because it costs reps (volume load), not because rest itself does
   anything.** In Longo 2022 (n = 28, within-subject legs), 1-min rest plus extra sets to match volume load grew as much
   as 3-min rest (~13% vs ~13%). Rest-matched but volume-short conditions grew ~7%. A 20 s vs 2 min volume-equated study
   in untrained men agrees. (I/M, limited)
3. **In trained lifters, the trials split cleanly at about 2 min.** 1 min < 3 min (Schoenfeld 2016, n = 21, sets-matched,
   so the 1-min group did less volume). 2 min = 5 min (Ahtiainen 2005, n = 13). Constant 2 min = decreasing
   2 min → 30 s (Souza-Junior 2011, n = 22). All are small and non-significance is not equivalence. (I, limited)
4. **"Progressive overload" is a necessity of logic but not a separable, testable factor.** No trial has a
   no-progression arm with effort held constant, and it could not have one, because a fixed load drifts away from failure
   as the lifter adapts. *How* you progress does not matter: load vs reps gave similar growth in trained lifters
   (Plotkin 2022, n = 43) and in untrained (Chaves 2024, n = 39). (I, moderate for "mode doesn't matter")
5. **Periodisation is a strength lever, not a growth lever.** Moesgaard 2022 (35 studies): hypertrophy ES 0.13
   (95% CI −0.10 to 0.36), 1RM ES 0.31 (0.04–0.57). Linear vs undulating made no difference (Grgic 2017, 13 studies). (I, moderate)
6. **Deloads have one trial, and it found no hypertrophy benefit and a strength cost** (Coleman 2024, n = 39, one week
   of complete cessation mid-way through 9 weeks). The rest of the deload literature is opinion and practice surveys
   (Bell 2023 Delphi; Rogerson 2024: deloads of ~6 days every ~5.6 weeks). (I, very limited)
7. **Recovery between sessions works through volume distribution, not frequency itself.** Frequency has no effect when
   volume is equated (Schoenfeld 2019, 25 studies, via A1). The MPS response is shorter in trained muscle (Tang 2008;
   Damas 2015 review). Early MPS goes to damage repair, not growth (Damas 2016, n = 10). (M, moderate; I, moderate)
8. **Breaks are cheap.** Size lost in a 3–10-week break comes back fast (Ogasawara 2013, Halonen 2024, both untrained).
   The *myonuclear* explanation for muscle memory is **not** supported in humans (Psilander 2019; a myonuclear-permanence
   meta-analysis: retained in rodents, not humans). (I, limited; M, limited)
9. **Context only: protein and sleep are real but are not working-set factors.** Protein gives a modest added gain up to
   roughly 1.6 g/kg/d, with an imprecise breakpoint, CI ~1.0–2.2 (Morton 2018, 49 RCTs, 1863 people; Nunes 2022, 74 RCTs).
   One night without sleep cut MPS by 18% (Lamon 2021, n = 13). There is no longitudinal sleep-hypertrophy trial. (I/M, moderate / limited)
10. **Verdict for the top-5.** Neither "adequate rest" nor "progressive overload" earns an independent slot. Both are
    best expressed through the factors that already would: **rest preserves volume load** (a volume/effort modifier) and
    **progression preserves proximity to failure** (an effort modifier). If the coordinator wants one from this cluster,
    "rest ≥ ~2 min on heavy compounds so the next set keeps its reps" is the defensible one. It ranks below effort,
    volume and probably muscle length, and is a **rule with a floor, not a dial**.

## Scorecard (the five ranking criteria)

| Factor | 1. Effect size at realistic contrasts | 2. Certainty | 3. Trained-lifter evidence | 4. Controllable set to set | 5. Dose-response shape |
|---|---|---|---|---|---|
| Rest interval | Small. Pooled SMD difference ~0.08 (binary). Thigh pairwise ~0.17, CrI crosses 0 | Low–moderate: 9 studies, mostly untrained, heterogeneous | 3 small trials (n = 13–22), consistent with a ~2 min floor | **High** (fully under lifter control) | **Floor then plateau**: <60 s worse, >90 s–2 min flat; effect largely via volume load |
| Progressive overload (as a mode) | ~0 between load and rep progression | Moderate for "mode is irrelevant" (2 RCTs); **none** for "progression vs none" | 1 RCT (Plotkin 2022, n = 43) | Session to session, not set to set | Not testable as a dose; it is how effort and volume are kept constant |
| Periodisation | Hypertrophy ES 0.13 (CI −0.10 to 0.36) | Moderate (35 studies) | Mixed samples | Programme level | None for growth |
| Deload | ~0 hypertrophy, small strength cost | Very low (1 RCT) | 1 RCT | Programme level | Unknown |
| Inter-session recovery / frequency | ~0 when volume equated | Moderate (25 studies, via A1) | Mixed | Programme level | Only as volume distribution |
| Protein (context) | Modest. Small SMD for added FFM | Moderate (49 + 74 RCTs, overlapping) | Mixed | Daily, not per set | Plateau ~1.6 g/kg/d, imprecise |
| Sleep (context) | Unknown longitudinally | Very low for growth (acute MPS only) | None | No | Unknown |

---

## 1. Rest intervals

### 1.1 Meta-analyses (do not double count: Singer 2024 supersedes Grgic 2017 and overlaps it)

- **Singer 2024** (Front Sports Act Living 6:1429789). 9 RCTs (within- or between-group), 19 measurements: thigh 10, arm 6,
  whole body 3.
  - Binary model: short 0.48 (95% CrI 0.19–0.81) vs longer 0.56 (0.24–0.86).
  - By region: arm and thigh favour longer rest. Thigh pairwise 0.17 (CrI −0.13 to 0.43), from a secondary return. Whole
    body −0.08 (−0.45 to 0.29), slightly favouring short rest.
  - Conclusions: small benefit >60 s; "no appreciable differences" beyond 90 s; failure vs non-failure did not modify
    the result.
  - Authors' own caveats: substantial heterogeneity, and "caution … for highly-trained individuals" because most
    participants were untrained. The volume-load mediation is offered as "perhaps"; it is **not** a formal mediation model.
  - (I, limited–moderate)
- **Grgic 2017** (Eur J Sport Sci 17:983). Systematic review of 6 studies, no pooling. Both short (≤60 s) and long rest
  produce growth, with a possible advantage for long rest in trained participants measured sensitively. (I, limited)
- **Grgic 2018** (Sports Med 48:137), on strength. >2 min appears needed to maximise strength in trained lifters;
  60–120 s is enough in untrained. Study count not confirmed. (I, limited)

### 1.2 Primary trials

| Trial | n, status | Contrast | Hypertrophy result | Note |
|---|---|---|---|---|
| Schoenfeld 2016 | 21, trained men | 1 vs 3 min, sets matched | 3 min > 1 min for anterior thigh MT; triceps p = 0.06 | 1-min group did less volume load; 1RM also favoured 3 min |
| Ahtiainen 2005 | 13, trained men, crossover 2×3 mo | 2 vs 5 min | No difference (MRI quad CSA) | Both above the plateau |
| Souza-Junior 2011 | 22, trained men, all on creatine | constant 2 min vs 2 min→30 s | No difference (MRI) despite more volume in the constant group | Does not fit a pure volume account, or is under-powered |
| de Souza 2010 | ~20, trained | same design, no creatine | Not retrieved | UNVERIFIED |
| Longo 2022 | 28, within-subject (status UNVERIFIED) | 1 vs 3 min, with and without volume matching | ~13% when volume load high (either rest), ~7% when low | **The mediator test** |
| 20 s vs 2 min (Çukurova record) | untrained men | volume-equated | No difference | Authors and year UNVERIFIED |
| Fink 2017 | untrained ≥2 yr | 30 vs 150 s at 40% 1RM | Triceps +9.8 vs +10.6%; thigh +5.7 vs +8.3%; no significant difference | **Not trained**: the brief's "trained" label is wrong |
| Buresh 2009 | 12, untrained | 1 vs 2.5 min | 2.5 min > 1 min, arm CSA ~12 vs ~5% | Very small |
| Villanueva 2015 | older men | ~1 vs ~4 min, not to failure | Short > long (DXA lean mass, ~0.7 kg) | Opposite direction; DXA; irrelevant population |

**Hammarström 2020** (named in the brief as a rest trial) could not be found. The Hammarström 2020 paper I know of is
about training *volume*, not rest. Treat it as not a rest study.

### 1.3 Mechanism ("why it works")

- **Preserving reps → preserving volume load** (I, limited). This is the only mechanism with a direct causal test
  (Longo 2022, plus the 20 s / 2 min study). Short rest reduces the reps the next set can do at the same load. Add sets
  back and the deficit disappears. Every trained-lifter result in §1.2 fits this, except possibly Souza-Junior 2011.
- **Phosphocreatine resynthesis and metabolite clearance** (M, textbook; not re-verified here). These set how many reps
  the next set can do. That is the physiological route to the volume-load mechanism.
- **Acute hormone and metabolic-stress hypotheses: not supported.** Short rest raised acute GH, testosterone and
  cortisol without more growth (Buresh 2009, Fink 2017, Fink 2018). (I, limited, consistent)
- **The EMG spectral recovery rate is not readiness** (A6 C4). In Mills 1982, force recovered with a half-time of about
  30 s and EMG mean power frequency with a half-time of about 3 min, and other paradigms disagree on the direction.
  A spectral "recovered" signal has no validated link to next-set reps. (A, limited)

### 1.4 Striking claims fact-checked

- **"Science overturned decades of advice: 3 min grows more muscle"** (popular coverage of Schoenfeld 2016).
  - Supported: one significant site (anterior thigh) in 21 men over 8 weeks.
  - Triceps was a trend; elbow flexors were not reported as significant in what was seen.
  - The groups did not do the same volume load, and sessions in the 3-min group took about twice as long.
  - Ahtiainen 2005 and Souza-Junior 2011 found no difference at 2 min or more.
  - Verdict: **overstated**. The correct reading is "1 min with sets matched is worse", not "3 min beats 2 min".
- **"Rest beyond 90 s does nothing"** (Singer 2024).
  - This is "no appreciable difference" in pooled, mostly untrained data with wide CrIs.
  - Non-significance is not equivalence, and trained-lifter strength data (Grgic 2018) favour >2 min.
  - Verdict: correct as a hypertrophy floor, **not** evidence that 90 s is optimal for trained lifters on heavy compounds.
- **"Short rest is better for older adults"** (Villanueva 2015). One small DXA study, not to failure. Isolated, not
  replicated.

## 2. Recovery between sessions

- **MPS time course.**
  - Untrained, fasted: FSR above rest by +112% at 3 h, +65% at 24 h and +34% at 48 h (Phillips 1997; authorship from memory).
  - The response is **shorter and peaks earlier in trained muscle**: Damas 2015 review; Tang 2008 (n = 10, trained vs
    untrained leg). A companion thesis reports a return to baseline by about 28 h in the trained leg. That 28 h figure
    comes from the thesis, not the paper.
  - (M, moderate for direction; precise timing limited)
- **Muscle damage** (M, moderate).
  - In Damas 2016 (n = 10, untrained), integrated MyoPS did **not** correlate with hypertrophy in week 1, when damage
    was high. It did by weeks 3 and 10, once damage had attenuated.
  - Damas 2018 review: damage does not mediate or potentiate hypertrophy.
  - Practical consequence: soreness and damage are costs, not proxies for stimulus. Trained lifters, who show a
    repeated-bout effect, are past this stage for familiar exercises.
- **Frequency** (I, moderate, via A1).
  - Schoenfeld 2019 (25 studies): no effect when volume is equated.
  - Lopez 2021: more sessions helped those with a training background.
  - Read together: frequency matters only as a way of fitting in more good-quality volume.
- **Deloads** (I, very limited; opinion otherwise).
  - Coleman 2024 (PeerJ, n = 39): a one-week full stop at week 4.5 of 9 gave no hypertrophy difference and smaller
    lower-body strength gains. It did not support the "resensitisation" hypothesis.
  - Bell 2023 (Delphi; 34 → 29 → 21 coaches) gives a consensus definition only.
  - Rogerson 2024 (n = 246 athletes) describes practice: ~6.4 days every ~5.6 weeks.
  - A blog figure ("65% think they could progress without deloads") is UNVERIFIED.
  - No trial has tested a reduced-load deload (as opposed to cessation), or deloads in genuinely advanced lifters over
    longer blocks.

## 3. Progression over time

- **Progressive overload, mode** (I, moderate). Load vs rep progression gave similar hypertrophy in trained lifters
  (Plotkin 2022, PeerJ, n = 43, 8 wk; rectus femoris slightly favoured reps; 1RM favoured load by 2.0 kg, CI −2.4 to 7.8)
  and in untrained (Chaves 2024, IJSM, n = 39 within-subject, 10 wk). Plotkin's own lab caveats that reps cannot rise
  forever: very high reps eventually lose effectiveness.
- **Progressive overload, existence** (M, by inference; **no direct trial**). The mechanism is that as strength rises, a
  fixed load and fixed reps end further from failure. Fewer high-threshold motor units are then recruited near the end of
  the set, and fewer reps fall in the effective high-tension zone. Progression is how effort and volume stay constant in
  stimulus terms. That makes it a **consequence of the effort factor**, not an independent one.
- **Periodisation** (I, moderate). Moesgaard 2022 (35 studies): hypertrophy ES 0.13 (−0.10 to 0.36); strength ES 0.31.
  Grgic 2017 (13 studies, PeerJ, DOI unconfirmed): linear = undulating for growth. Overlapping studies; do not add them.
- **Training status and diminishing gains** (I, limited).
  - Lopez 2021: hypertrophy effects were larger in untrained participants (p = .033).
  - Mechanistically, this fits the shorter MPS response in trained muscle (Tang 2008, Damas 2015).
  - No study found quantifies a "genetic ceiling" or a per-year rate of decline in trained lifters. Any specific
    "x% per year" figure is UNVERIFIED and should not be used.
- **Detraining and retraining** (I, limited, untrained only).
  - Ogasawara 2013 (n = 14): 3-week breaks every 6 weeks matched continuous training at 24 weeks.
  - Halonen 2024: a 10-week break was regained rapidly.
  - **Myonuclear muscle memory in humans is not established.** In Psilander 2019 (n = 19), no myonuclear accretion
    occurred and the previously trained leg did not retrain better. The authors say their data do not allow a rigorous
    test. Snijders 2020 calls the question "largely ambiguous", and a myonuclear-permanence meta-analysis found myonuclei
    retained in rodents but not humans.
  - Epigenetic muscle memory (Seaborne 2018) was **not searched** and is UNVERIFIED here.

## 4. Individual variability: what it means for any universal target

- **Hubal 2005** (n = 585 per citing papers, untrained, 12 weeks, MRI): size change from roughly −2/3% to +59%; ~6%
  with practically no gain; strength 0 to ~250%.
- **Ahtiainen 2016** (pooled cohort, n not confirmed): size +4.8 ± 6.1% (range −11 to 30%); 29% "low responders"
  against the control CI.
- **Fact-check of "non-responders exist".**
  - Much of the observed spread is measurement error and day-to-day biology. When control-group variance is subtracted,
    Dankel & Loenneke (2020) detected **no true individual-response variance for hypertrophy**.
  - Chaves 2025 counters that the control-group method cannot capture within-person variation and proposes
    within-subject unilateral designs.
  - Net: true heterogeneity probably exists but is smaller than raw ranges suggest. "Non-responder" is mostly a
    measurement artefact for hypertrophy. (M/I, limited)
- **Implication.** Every "optimum" in §1–3 is a group-mean floor with wide CIs. A product cannot honestly prescribe
  "rest 127 s" or flag someone as a "non-responder". What a single user can defensibly see is their own next-set reps
  after different rest lengths, and their own logged progression over weeks.

## 5. Nutrition and sleep (context only, outside the working-set question)

- **Protein.**
  - Morton 2018 (BJSM, 49 RCTs, 1863 participants): modest added FFM; breakpoint ~1.62 g/kg/d. Its CI (~1.03–2.20) was
    seen only in secondary sources, which call the breakpoint imprecise.
  - Nunes 2022 (74 RCTs, overlaps Morton): small extra LBM gains; significant for under-65s at ≥1.6 g/kg/d.
  - (I, moderate)
- **Sleep.**
  - Lamon 2021 (n = 13, crossover): one night of total deprivation gave MPS −18%, cortisol +21% and testosterone −24%.
  - That is acute, extreme and has no growth outcome. Dattilo 2011 is a hypothesis paper whose content was not retrieved.
  - (M, limited; no longitudinal I evidence found)
- Neither is a set-level factor, and neither belongs in a working-set top-5.

## 6. Recommendation to the coordinator (ranking)

| Candidate | Belongs in top-5? | Why |
|---|---|---|
| Rest interval | **Borderline: #5–#7, as a floor rule** | Real, small, controllable. Its effect is mostly mediated by volume load, so it partly double counts volume. State it as "≥ ~2 min on heavy multi-joint lifts, ≥ ~90 s otherwise, or add sets". |
| Progressive overload | **No, as a separate factor**; mention it as part of effort | No testable independent effect, and the mode doesn't matter. Its job is to keep sets near failure as strength rises. |
| Periodisation, deload, frequency | No | Null or near-null for growth when volume is equated. |
| Protein, sleep | No (outside scope) | Not working-set factors; protein is a modest real effect. |

**TENSR relevance (brief, H).**
- Elapsed rest is trivially trackable: EMG burst offset → next onset, plus IMU. Reps per set are already counted. So
  **"rest" and "next-set rep retention" are both measurable with the current board**, and that is the mechanism that
  matters.
- A spectral "you're recovered" timer remains unvalidated (A6 C4). Use elapsed time, not "recovered" language.
- Progression needs load, which only the user can enter. With it, reps × load per exercise per week is loggable.
  Without it, rep trends at a fixed load can be logged.

## 7. Open disputes

- **Is the rest effect fully mediated by volume load?** Longo 2022 says yes. Souza-Junior 2011 found more volume
  without more growth. Singer 2024 only says "perhaps". No formal mediation meta-analysis exists.
- **Do trained lifters need longer rest than untrained?** Grgic 2017/2018 and Singer 2024 suggest so. There are only
  ~3 trained hypertrophy trials, all small.
- **Deloads for advanced lifters, and reduced-volume (not cessation) deloads:** untested.
- **True inter-individual response variance in hypertrophy:** contested on method (Dankel vs Chaves).
