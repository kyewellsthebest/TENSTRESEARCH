# A6 — Independent evidence audit

Agent A6, 2026-11-02. Adversarial audit of A1–A5. Every verdict below comes from my own searches (log: `A6-searchlog.md`) or my own recomputation (`A6-check-stats.py`, `A6-check-mdf.py`). Nothing is taken from another agent's notes. Corrected and new study rows: `A6-studies.csv`.

**Bottom line.**
- The citation base is sound. No load-bearing citation was fabricated. Two are numerically wrong: Kassiano 2023a and A4's description of the Colyer 2018 reference electrodes.
- Three citations are misapplied: Rodríguez-Rosell 2021 (A2), Orange 2022 (A5) and Zhao 2025 (A4).
- Six number-level details could not be confirmed. Each is listed in §1.
- The bigger problems are inferential:
  - A1, A2 and A5 read Halperin's 0.95-rep **bias** as an **error**.
  - A2's "MDF recovers faster than force" is contradicted by a primary study A2 did not find.
  - A5's MDF acceptance targets cannot be met even by a perfect device, by A3's own numbers.
  - A3's "500 SPS cannot measure MDF" is overstated, although its 2 kSPS recommendation stands.
  - A4 trusts within-set amplitude more than within-set MDF. The dry-electrode confound structure says the opposite.

---

## 0. Access

- **Re-test, 2026-11-02:**
  - WebFetch `https://doi.org/10.1016/S1050-6411(00)00027-4` returned `getaddrinfo ENOTFOUND doi.org`.
  - WebFetch `https://pmc.ncbi.nlm.nih.gov/` returned `ENOTFOUND`.
  - curl, run once each, to doi.org, pmc, api.crossref.org, eutils, Europe PMC, arxiv.org, api.openalex.org and api.semanticscholar.org: all returned no connection (HTTP 000).
  - **Fetch remains blocked. Only WebSearch works.** These hosts would have to be allowed in the session's network settings.
- **Searches used:** 84 WebSearch calls (standard mode), about 42% of the shared budget.
- **Access level:** every verification below is at the level of a search-engine summary of abstracts, repository records, publisher HTML snippets or the TI document-viewer. **Nothing was read in full text.** "VERIFIED" therefore means that bibliographic details and the headline result match an independent record. It does not mean the methods were checked.
- **Retractions:**
  - No retraction or correction was found for any load-bearing study. This is not exhaustive, because the Retraction Watch database itself was not queryable.
  - Barbalho: no agent relied on a Barbalho paper. A1 explicitly excluded them. Retraction Watch confirms these retractions:
    - Barbalho's IJSPP paper, April 2020;
    - a JSCR single-joint study in untrained women, December 2021;
    - a 2020 call to retract seven papers, including two single-joint-exercise trials. Some of the seven were still unretracted at last coverage.
  - Gentil 2013 (APNM 38(3):341–344) is Gentil-led, not Barbalho-led. No retraction found. Its result (no added elbow-flexor growth from single-joint work, n = 29 untrained) conflicts with later Barbalho-group trials that did find an effect. **Do not cite the Barbalho trials as counter-evidence.**

---

## 1. Citation verification

**Sampling.** The named list was checked in full. A random sample of 15 further rows was drawn with `random.seed(20261102)` over the 115 CSV rows not on the named list (A1–A5 pooled). Script inline in the search log.

Verdicts: **V** = verified; **P** = partly (the difference is stated); **U** = unverifiable (the reason is stated); **W** = wrong.

### 1a. Named list

| key (agent) | verdict | what I found / what differs |
|---|---|---|
| Halperin2022 (A1, A2, A5) | **P** | Sports Med 52(2):377–390; 13 publications, 12 studies, 414 participants; 262 effects; underprediction 0.95 reps (95% CI 0.17–1.73); I² 97.9% — **all correct**. **Omitted by all three agents:** between-participant SD ≈ 1.45 reps; accuracy better with **heavier loads / fewer reps** and later sets. 0.95 is a **mean signed bias**, not a mean absolute error (see C1). |
| Refalo2023 (A1) | V | Sports Med; 15 studies. Set failure vs non-failure ES 0.19 (0.00–0.37); momentary-failure subgroup 0.12 (−0.13 to 0.37); "potential non-linear relationship". Matches A1. |
| Refalo2024 (A1) | V | J Sports Sci 42(1):85–101. Quadriceps thickness 0.181 cm (FAIL) vs 0.182 cm (1–2 RIR); Bayesian mixed models; more velocity/rep loss with FAIL. n not confirmed (secondary source says 26). |
| Robinson2024 (A1) | V | Sports Med 54(9):2209–2231; DOI 10.1007/s40279-024-02069-2. Hypertrophy improves closer to failure; strength little affected; exploratory. Also reported: **the heavier the load, the less proximity mattered** — A1 should state this. |
| Grgic2022 (A1) | V | JSHS 11(2):202–211; 15 studies; trained-subgroup hypertrophy ES 0.15 (0.03–0.26); non-failure favoured strength when volume was not equated. Note: only 2 of 7 hypertrophy studies were in trained subjects (secondary source). |
| Lasevicius2022 (A1) | V | JSCR 36(2):346–351; within-leg, 30% vs 80% 1RM, failure vs non-failure, volume-equated, 8 wk. Matches. |
| Plotkin2023 (A1) | V | Front Physiol 14:1279170; untrained; HT n = 18, SQ n = 16; 9 wk; MRI. Glute mCSA similar. Squat grew quads and adductors more. Higher HT glute sEMG did not consistently predict growth. Matches. |
| Vigotsky2018 (A1, A2) | V | Front Physiol 8:985 (2018). Matches. |
| Vigotsky2022 (A1) | V | Sports Med 52(2):193–199. Matches. |
| Schoenfeld2015 (A1) | V | Sports Med 45(4):577–585; 8 studies, 0.5–8 s similar; >10 s possibly inferior; load and failure not isolated (Lacerda 2021 critique). |
| Schoenfeld2017a (A1) | V | JSCR 31(12):3508–3523; 21 studies; ≤60% vs >60% 1RM to failure; hypertrophy similar, 1RM favours heavy. |
| Lopez2021 (A1) | V | MSSE 53(6):1206–1216; 28 studies, 747 adults; hypertrophy load-independent; strength favours high load. |
| Pelland2026 (A1) | **P** | Citation verified: Sports Med 2026;56(2):481–505; authors and conclusions match; fractional set counting. **DOI 10.1007/s40279-025-02344-w: UNVERIFIABLE** (exact-string search returned nothing). "67 studies / 2,058 participants" is from a blog only. |
| Singer2024 (A1) | V | Front Sports Act Living 6:1429789; 9 studies, 19 measurements; small benefit >60 s; none appreciable >90 s; mostly untrained. |
| Maeo2021 (A1) | V | MSSE 53(4):825–837; n = 20; whole hamstrings +14% vs +9%; short head of biceps femoris not different. |
| Maeo2023 (A1) | **P** | EJSS 23(7):1240–1250; n = 21; 12 wk. Long head +28.5% vs **+19.6%** (1.5×, d = 0.61); lateral+medial heads +14.6% vs +10.5% (1.4×). A1's whole-triceps "+19.9% vs +13.9%" **not confirmed**; A1 omitted the long-head comparator. |
| Pedrosa2022 (A1) | V | EJSS 22(8):1250–1260; 45 untrained women; initial-range partial gave the greatest regional quadriceps growth; 1RM similar. |
| Wolf2023 (A1) | **P** | IJSC 3(1). Lengthened partial vs full −0.28 (95% CI −0.81, 0.16) confirmed. **Sign convention disputed across sources**: a secondary source reports +0.28 favouring lengthened. Study count 23 vs 24 conflicting. |
| Wolf2025 (A1) | V | PeerJ 13:e18904; n = 30 trained, within-subject, 8 wk, upper-body; similar thickness and 10RM lat pulldown. |
| Schoenfeld2015 tempo | V | Same row as Schoenfeld2015 above. |
| Pareja-Blanco2017 (A1) | V | SJMSS 27(7):724–735; n = 22; VL40 more VL/VI hypertrophy; CMJ +9.5% (VL20) vs +3.5% (VL40); VL20 did 40% fewer reps. IIX-loss detail SECONDARY only. |
| Morton2016 (A1) | V | JAP 121(1):129–138; n = 49 trained; 30–50% vs 70–90% 1RM to failure; lean mass and fibre CSA similar; hormones unrelated. |
| Morton2019 (A2) | V | J Physiol 597(17):4601–4613. sEMG amplitude unrelated to glycogen depletion and anabolic signalling. Matches. |
| Haugen2023 (A1) | **P** | BMC SSMR 15:103; 13 studies, 1,016 participants; hypertrophy SMD −0.055 (−0.397, 0.287) correct. "Only 5 hypertrophy studies" **not confirmed**. |
| Augustin2025 (A1) | **P** | Int J Exerc Sci 18(3):329–342; DOI 10.70252/GDBL2230. **A1's author order is wrong**: Augustin, Piñero, Enes, … Nippard, Schoenfeld. Momentum neither helped nor hindered growth; more volume load. n = 30 not confirmed. |
| Jenkins2015 (A2) | V | EJAP 115:2335–2347. MPF last reps 71.6% (30%) vs 78.1% (80%) MVIC; amplitude +74% vs +147% across reps but higher at 80% throughout. n ≈ 18 not confirmed. |
| Sakamoto2012 (A2) | **P** | EJAP 112:1015–1025; 13 trained men; 40–80% × 4 speeds; pre-fatigue MDF similar; post-fatigue drop similar across speeds and larger at light loads. **DOI not confirmed** (A2 correctly flagged). |
| Yan2025 (A2, A4) | **P** | Front Physiol, DOI 10.3389/fphys.2025.1661217; Yan B, Li Z, Li C, Han C, Yao S, Ma D, Zhang W; n = 10 bodybuilders. MDF decline amplified by fast tempo; "high-load medium-tempo produced less fatigue". **A2's "largest decline at 80% + fast" not confirmed.** The load direction may conflict with Tsoukos2021 (light loads → larger MDF drop). |
| Nishihara2013 (A2) | V+ | Comput Math Methods Med 2013, **DOI 10.1155/2013/174342** (A2 had it unconfirmed). Innervation-zone shift 3.9 mm (acute angles) vs 16 mm (obtuse); 8-channel array, biceps. |
| Sundstrup2012 (A2) | V | JSCR 26(7); 15 untrained women; elastic lateral raise; normalised EMG curvilinear rise, **plateau 3–5 reps before failure**. |
| Keenan2005 (A2) | V | JAP 98:120–131; cancellation up to 62% at maximal activation (confirming Day & Hulliger). The 85% figure was not re-checked. |
| GonzálezIzal2010b (A2) | **P** | JEK 20(6):1097–1106; 15 trained, 5 × 10 leg press, vastus medialis; 46.6% (wavelet) and 49.8% (log FInsm5 + MAV). **The figures were seen in the 2009 working-paper abstract**, not confirmed in the journal version. |
| Burden2010 (A2) | V | JEK 20(6):1023–1035; DOI 10.1016/j.jelekin.2010.07.004. Endorses isometric MVC; task peak/mean reduces between-person variability. |
| Garofalo2026 (A2, A3) | **P** | JEK, DOI 10.1016/j.jelekin.2026.103111; 12 participants, 192 recordings, **isometric** biceps holds; MLP/Transformer/RNN on spectrograms vs **linear and SVR baselines**. Author list varies by source (Fiorilli). Validation scheme and MSE units unconfirmed; "87%" from an aggregator only. |
| RodríguezRosell2021 (A2) | V / **misapplied** | SJMSS 31:1621–1635; n = 33; VL10/30/45; no EMG change in any group. **That EMG was a training-adaptation measure, not a within-set fatigue measure** (C9). |
| Hermens2000 (A3, A4, A5) | V | JEK 10(5):361–374; DOI 10.1016/S1050-6411(00)00027-4 (PMID 11018445); 27 muscles. The 20 mm IED is confirmed by secondary sources. The ≤10 mm electrode size was not confirmed in-session (from memory: the size in the fibre direction is ≤10 mm). A3's "SENIAM does not cover pectoralis major": **UNVERIFIABLE** (muscle list not retrieved). |
| Besomi2019 (A3) | V | JEK 48:128–144; DOI 10.1016/j.jelekin.2019.07.008; covers IED and crosstalk. Cell values not seen. |
| Besomi2020 (A3) | **P** | JEK 53:102438; six approaches: task-matched MVC, standardised isometric MVC, **standardised submaximal task**, task peak/mean, non-normalised, M-wave. **A3's list omits the submaximal reference**, which is the one practical option for TENSR. |
| Lynn2018 (A3, A4, A5) | **P** | JSSM 17:205–215; **n = 12**; seven sessions on separate days; isokinetic; VL/VM/BF; no system effect on amplitude. **A3 wrongly says n "not retrieved" and "squat-type".** "Concurrent" placement (A5) is consistent. |
| Colyer2018 (A3, A4) | **P / W** | JSSM 17:101–109; 16 males; run/cycle/squat; within-session CV 13.8% vs 14.1%; **between-session ARV CV 42.6% (textile) vs 41.2% (surface)**; poorer agreement at high excitation; textile bursts longer. **A3 omits the 42% between-day figure. A4 says "even with gel electrodes" — WRONG**: the reference was Delsys Trigno dry silver-bar (A3 correct). |
| Nordander2003 (A3) | **P** | EJAP 89(6):514–519. 21% (MVC) to 33% (submax) of variance confirmed only second-hand, and **for trapezius**. A3 does not name the muscle. |
| Orange2019 (A3) | V | JSCR 33(9):2398–2408; 29 youth rugby players; PUSH vs GymAware; valid/reliable only at squat 20% (MP, PP) and bench 40% (MP r = 0.89, ICC 0.83). |
| Orange2022 (A5) | V / **misapplied** | J Sports Sci 40(11):1220–1234; 4 RCTs, 88 participants; strength SMD 0.06 (−0.51, 0.63). It compares **VBT prescription vs %1RM**, not feedback vs no feedback (C12). |
| Weakley2019a (A5) | V | JSCR 33(9):2420–2425; 15 adolescent rugby players; MCV 0.70 vs 0.65 m/s. |
| Weakley2019b (A5) | V | IJSPP 14(9):1205–1211; 28 players (16 vs 12); "possibly to likely" greater gains (MBI). |
| Weakley2020 (A5) | V | JSCR 34(11):3157–3163; 12 rugby players; four conditions. |
| Weakley2023 (A5) | **P** | Sports Med 53(9):1789–1803; 20 studies; +8.4% velocity, g 0.63 (0.36–0.90); visual 1.11 vs verbal 0.47. **The authors also concluded that chronic feedback produced greater adaptations; A5 omits this** (C12). |
| Bonett2002 (A5) | V | Stat Med 21:1331–1335. Worked example 19.2 reproduced: my code gives 19.15. A5's table recomputed exactly (C11). |
| KooLi2016 (A5) | V | J Chiropr Med 15(2):155–163. Cut-points 0.5/0.75/0.9 and the advice to judge the CI. |
| ADS1292R sinc3, −3 dB = 0.262·f_DR (A3, A4) | **V** | TI SBAS502C document-viewer: "the digital filter on each channel consists of a **third-order sinc filter**", notches at f_DR multiples; noise-table header "−3-dB bandwidth 0.262 f_DR"; 32.75 Hz at 125 SPS (TI E2E). **Independent check:** only order 3 gives 0.2615·f_DR (orders 1/2/4/5 give 0.442/0.318/0.227/0.204). |

### 1b. Random sample (15 rows)

| key (agent) | verdict | note |
|---|---|---|
| GarminRepCount (A3) | V | IJES conference abstracts vol 14 iss 3 art 143; 20 participants; four Garmin devices; not accurate. Not peer reviewed (flagged correctly). |
| Schoenfeld2020 (A1) | V | Front Physiol 10:1571 (published Jan 2020); 27 trained; mid-thigh thickness benefit; possible leg-press detriment. |
| Gerdle1992 (A2) | **P** | Gerdle & Fugl-Meyer, Acta Physiol Scand 145(2):129–138; n = 10 women; plantar flexion. **Key finding omitted by A2:** the MPF shift is mainly sensitive to type II fibre biochemistry and **missed type I/hypoxic fatigue**. A2's row summary is not confirmed. |
| Baek2025 (A3) | **P** | Sensors 25(21):6588, DOI 10.3390/s25216588; force-time from a load cell; isokinetic bench. "93% within ±1 RPE" not confirmed. |
| SteeleRIR2017 (A3) = Steele2017b (A5) | V | Steele, Endres, Fisher, Gentil, Giessing. PeerJ 5:e4105; n = 141; underprediction; improves with experience. A3 had the authors unconfirmed; the same paper is duplicated across A3 and A5. |
| Dankel2017 (A1) | V | EJAP 117:2125–2135. |
| Schoenfeld2016 (A1) | V | JSCR 30(7); 21 trained men; 3 min > 1 min. |
| MartinezValdes2023 (A3) | **U** | ISEK confirms that a CEDE HD-sEMG matrix exists; journal, year and spacing not retrieved. |
| Pallares2021 (A1) | **P** | SJMSS 31(10):1866–1881; 16 studies; full ROM better for strength and lower-limb hypertrophy. ES 0.56/0.88 not confirmed. |
| BlandAltman1999 (A5) | V (method) | SE(LoA) ≈ √(3/n)·s recomputed; A5's half-widths match (4.8/3.2/2.2/1.7 Hz). |
| SanchezMedina2011 (A5) | **P** | MSSE 43(9):1725–1734. Lactate r = 0.97 (squat) / 0.95 (bench) and CMJ r ≈ 0.92 are SECONDARY. Ammonia appears as **R² = 0.85**, not r. |
| Saucier2021 (A4) | V | Sensors 21(16):5348; 15 players; Strive Sense3; positional differences only. |
| Dimitrov2006 (A2) | V | n = 7; **rectus femoris**; 10 × 15 knee extension at 50% 1RM; ΔFInsm5 ~8-fold vs ΔMDF 32%; ICC 0.75 vs 0.78. |
| Lu2016 (A5) | V | Int J Biostat 12(2); DOI 10.1515/ijb-2015-0039. |
| BicepsRecovery2008 (A2) | **P** | Oliveira & Gonçalves, Res Sports Med 16(4):244–256; n = 10; **one-minute bouts at 25–40% 1RM, not sets to failure**; EMG near reference by 1 min. It did not measure force recovery, so it **cannot** support "dissociation from force" (C4). |

### 1c. Other checks

- **Kassiano2023a (A1): numbers WRONG.**
  - The search returned final-range partial +6.2% and full +7.3%.
  - A1's "+15.2% vs +6.7% vs +3.4%" matches nothing. The 6.7% figure belongs to a different 2025 study.
  - The direction, lengthened partials largest, holds.
- **Zhao2025 (A4): selective.**
  - The PeerJ 2025 paper (DOI 10.7717/peerj.20426) found no MDF–velocity-loss relation.
  - The **same group's IJSM 2025;46(6):437–445** found a spectral fatigue index correlated with velocity loss at r = 0.603.
  - A4 cited only the null.
- **Tsoukos2021 = A4's "SJMSS2021bench".** A4 marks the authors UNVERIFIED; A2 has the row. Confirmed: n = 14; MDF drop and velocity loss larger at 40% and 60% than at 80%.
- **ThomasWahlström2025 (A2 "authors not retrieved").** Authors are Thomas J and Wahlström J; 69 sets, more than 1,000 reps; EMG "slightly improved" accuracy; eccentric rep time was the top predictor. Preprint.
- **Jukic2024 (A5).** Physiol Rep 2024; 46 trained participants; free-weight back squat. Individual RIR–velocity relationships gave mean error **<2 reps** next session; general equations did not.
- **Elfving 2002 EJAP** is A2's "MDFRecovery_Lumbar". The pH/force "dissociation" is **not** in what was retrieved.
- **Mills 1982 (J Physiol; new, primary).** Force recovery half-complete at about 30 s; **MPF half-complete at about 3 min**. This is the opposite direction to A2's claim (C4).
- **Vestergaard-Poulsen et al. (31P-MRS, new).** MDF fall correlated with pH, r = 0.82.

---

## 2. Causal-leap challenges

**C1 → A1, A2, A5. Halperin's 0.95 reps is a bias, not an accuracy.**
- 0.95 is a mean *signed* underprediction. The between-participant SD is about 1.45 reps.
- Self-report MAE is therefore probably above 1 rep. A constant bias is also correctable: a user told "you underestimate by about 1" gets better at once.
- A5's gate, "LOSO MAE ≤ 1.0 rep … better than self-report (~1 rep)", compares an MAE to a bias. Rebuild it against **measured self-report MAE in the same sessions**, raw and bias-corrected.
- Halperin also shows human accuracy is best near failure and at heavier loads. That is exactly the RIR 0–3 zone the product targets, so the bar is *higher* where it matters.
- **Benchmark nobody stated:** individualised bar-velocity RIR models, the best objective method available, achieve only "<2 reps" mean error (Jukic 2024). There is no precedent for any sensor beating a lifter's own bias-corrected guess.

**C2 → A3. "500 SPS cannot measure median frequency" is overstated; the recommendation survives.** I re-ran the model across five spectral shapes (`A6-check-mdf.py`).

| 500 SPS condition | measured fatigue drop (true −25%) | source of the loss |
|---|---|---|
| raw | −15.6% to −17.7% | droop plus truncation |
| inverse-sinc3 compensation | −21.4% to −24.2% | truncation only, about 3 points |
| ideal brick-wall at 250 Hz | −20.6% to −23.6% | — |

- About half of A3's compression is the correctable droop, not lost information.
- A 500 SPS MDF is a *different, band-limited* index that still tracks fatigue at about 85–95% sensitivity.
- **Still recommend DR = 2 kSPS:** it is free in hardware, it keeps comparability with the literature, and 450 Hz becomes representable.
- **Change** "cannot measure" to "biased low; within-set trend compressed by about a third uncompensated, or by about 10% compensated".

**C3 → A3, A4. The 25.4 mm comb-filter dip is irrelevant to the *relative* fatigue trend.**
- With CV scaling 4 → 3 m/s and the spectrum scaling with it, the relative MDF drop is −25.4% at 25.4 mm against −25.0% at 20 mm (my run). The dip moves with conduction velocity, so it *is* the CV-tracking mechanism, not a confound.
- A3's "about 10 Hz lower" is absolute. It double-counts electrode filtering, because a Shwedyk-type spectrum is already fitted to recorded bipolar sEMG.
- A4's "MDF will depend strongly on … CV, not only on fatigue" mis-states this: CV *is* the fatigue signal.
- **A2 vs A3 disagree on the sign of the IED effect.** A2 cites a simulation in which a larger IED *raises* MDF; A3's idealisation *lowers* it. Unresolved, and it matters only for absolute Hz.

**C4 → A2 (also A4 §2.5). "MDF recovers faster than force, so a recovery timer ends early" is not established.**
- Mills 1982: force recovers fast (t½ ≈ 30 s) and MPF slowly (t½ ≈ 3 min). That is the opposite direction.
- Oliveira 2008 (light one-minute bouts, no force measure) cannot show a dissociation.
- The lumbar row (Elfving 2002) does not, in anything retrieved, contain the pH/force claim.
- **Correct verdict:** the direction and size of any MDF–performance recovery dissociation is inconsistent across paradigms; a spectral rest timer is **unvalidated**, not "contradicted". The product recommendation is unchanged (research-only), but the reason changes.

**C5 → A2, A4. "Tempo-independent: contradicted" is too strong.**
- Sakamoto 2012: the post-fatigue MDF drop was similar across four speeds. That *supports* partial tempo independence.
- Yan 2025 (n = 10): fast tempo amplified it.
- Correct verdict: **not established; mixed.**
- The brief's stronger claim, "therefore beats VBT", is unsupported regardless.

**C6 → A4. A4 ranks the confounds backwards.**
- A4 rates within-set *amplitude* trend "suitable to prototype" and *MDF* trend "after substantial validation".
- With dry studs, within-session sweat lowers electrode impedance over minutes. That moves **amplitude**: gain, CMRR and noise.
- It barely moves MDF. With C1/C2 = 100 pF, the input corner sits at about 3.5 kHz even at 250 kΩ (`afe-sim-results.md`), far above the band.
- Amplitude also rises with load, velocity and effort, plateaus 3–5 reps before failure (Sundstrup 2012), and drops at load changes. MDF is at least a specific peripheral marker (M, strong).
- Both need validation. Amplitude is **not** the safer feature.

**C7 → A3. "A reliable trend needs about 4–6 reps" is optimistic.** Using A3's own 0.5 s single-rep SD (9.3 Hz, which I reproduced) and a 30 Hz linear decline over 10 reps (3 Hz/rep):

| reps in regression | slope SE (Hz/rep) | t |
|---|---|---|
| 5 | 2.9 | 1.0 |
| 8 | 1.4 | 2.1 |
| 10 | 1.0 | 2.9 |

- In a 10-rep set the trend is first statistically visible at about rep 8, when the user already has about 2 reps left.
- In a 20-rep light set the slope per rep halves, so detection comes later still.
- **No live use of MDF slope is defensible.** A post-set summary is.

**C8 → A3 vs A4. Reference electrode on active muscle: A3 is right, A4 overstates.**
- E2 at (0, +11.3) is **equidistant** from E1 (−12.7, −11.3) and E3 (+12.7, −11.3). EMG generated under E2 therefore arrives at both detection electrodes nearly equally. It is common mode by geometry and rejected by the CMRR.
- RLD current is µA-scale; "current through contracting tissue" is not a measurement risk.
- **The real E2 risk is contact loss** on a moving belly under a band, which collapses the RLD and CMRR. That is an SQI or lead-off item, not a physiology one.
- A3's "about 1% contamination" is hand-waved: 48 dB is about 0.4%, and the CMRR loss from RC mismatch grows about 20 dB/decade above 50 Hz. Still low.

**C9 → A2, A4. Rodríguez-Rosell 2021 is misapplied.**
- Its "no EMG change" is pre/post-*training* neuromuscular EMG, not EMG tracking fatigue within a set.
- It says nothing about whether sEMG tracks proximity to failure as well as velocity does.
- Remove it from "why this beats VBT is unsupported". That verdict stands on the absence of any head-to-head trial alone.

**C10 → A4. Three factual errors.**
- (a) Colyer 2018's reference was dry silver-bar Trigno, not gel.
- (b) Zhao 2025 cited one-sidedly; the IJSM 2025 paper by the same group gives r = 0.60.
- (c) "SJMSS2021bench" is Tsoukos 2021, already verified by A2.

**C11 → A5. The sample-size arithmetic is correct. The MDF acceptance targets are not achievable.**
- **Rechecked, all correct** (`A6-check-stats.py`):
  - Bonett n: 30.6 / 22.0 / 53.6 / 74.5 / 56.5, matching A5's 31 / 22 / 54 / 75 / 57.
  - Wilson 95% CI for 27/30 = 0.744–0.965 (exact 0.735–0.979). A5's "about 74–97%" holds.
  - SEM χ² ratios 0.74–1.55 (n = 15), 0.80–1.34 (n = 30), 0.85–1.22 (n = 60).
  - The 11 Hz MDC example: upper bounds 17.0 / 14.7 Hz.
  - 100 positives; RCT 174 → 63 per group.
- **Caveat on Bonett:** the formula is a one-way/consistency approximation. A5 plans ICC(A,1), where systematic session bias widens the CI, so the Bonett n is a floor.
- **Caveat on the brief's test:** with **one** participant's 30 sets, the Wilson CI describes that person's sets only. It carries zero information about other users.
- **The targets:**
  - **S1.3 "MDF SD < 3 Hz":** the estimator floor for a stationary Gaussian signal is 9.3 Hz at 0.5 s and 4.7 Hz at 2 s. Below 3 Hz needs a window of about 5 s, longer than a rep. The physics of spectral estimation fails this target, not the board.
  - **Stage 3 "per-rep MDF LoA within ±10 Hz":** two pairs over different motor-unit territories each carry about 7–9 Hz estimator noise, so the difference SD is about 10–13 Hz and the LoA about ±20–26 Hz *with perfect hardware*. A5's own Example 1 uses s = 5 Hz on **participant means**, a different quantity from the acceptance criterion.
- **Fix:**
  - Set S1.3 against the theoretical estimator variance (bias < 2 Hz; SD within 10% of the simulated floor).
  - Set Stage 3 agreement on **per-set slope** and **multi-rep means**, benchmarked against two adjacent reference pairs (A5 already proposes this floor; make it the *only* criterion).
  - Stage 2 MDC (between-day absolute MDF) is the wrong noise term for a *within-set* trend. The relevant quantity is the within-set slope SE (C7).

**C12 → A5. The feedback evidence is mismatched and slightly too pessimistic.**
- Orange 2022 tests velocity-based *prescription* against %1RM, not feedback against none.
- Weakley 2023 (20 studies) concluded that feedback improved acute output **and chronic adaptations**. The certainty is low and the chronic studies are few, but A5's "no established long-term benefit" omits the authors' own conclusion.
- The relevant risk for TENSR is the **sign** of the effect, not its existence. Feedback reliably raises acute effort, so a mis-calibrated "2 left" cue will push users harder than intended.

**C13 → A4. "The IMU sees almost no rep motion" on static-segment exercises is untested and probably overstated.**
- A biceps or triceps belly bulges under a band each rep and tilts the puck. A4 calls this artefact.
- It is a rep-locked signal that may *help* counting. Free-weight curls also move the upper arm.
- No study found tests an upper-arm or belly-worn IMU; all rep-counting validation is forearm or wrist (RecoFit, ±1 rep 93%, verified).
- Phase split from the IMU on a static segment *is* unreliable; A4 is right there.

**C14 → A3. Electrode orientation is the unanswered hardware question; A3 skips it and A4 is right to raise it.**
- The pair runs along the board's 44 mm axis. Nothing records how the puck sits on the band. If the band wraps the limb, the pair probably runs **across** fusiform limb muscles.
- Evidence on the consequences is thin:
  - modelling: orientation changes power and selectivity more than spectral shape;
  - one vastus lateralis study: MPF fatigue slopes parallel −0.13 vs perpendicular −0.21, p = 0.09. Not equivalence.
- This must be measured in Stage 3, with both orientations against a reference pair, **before** any muscle is claimed.

**C15 → A2. "120 Hz is high for biceps" rests on a conference abstract.**
- The 77–79 Hz figure is isometric *mean* power frequency from a conference abstract.
- MNF normally exceeds MDF, so 120 Hz *median* is, if anything, even less likely.
- The direction is right; the evidence is weak (I, limited). Keep "absolute Hz is not transferable" as the robust statement.

**C16 → A1. Number-level errors.**
- Kassiano 2023a figures are wrong (§1c).
- Maeo 2023 whole-muscle numbers are unconfirmed and the long-head comparator is omitted.
- Augustin 2025 author order is wrong.
- Robinson 2024's load moderation (heavier load → proximity matters less) should be carried: it is the mirror of Lasevicius 2022 and directly relevant to RIR.

**C17 → all. Is a within-set MDF trend defensible at all?** My answer:
- **Yes, as a post-set descriptive physiological trend:**
  - multi-rep regression;
  - phase-locked concentric windows;
  - DR ≥ 1 kSPS, preferably 2 kSPS;
  - within one person, one exercise and one load.
  - Group-level direction: I, moderate (Jenkins, Tsoukos, Sakamoto, Dimitrov). On TENSR: H.
- **No, as a live number, a rep-of-failure detector, an RIR, or anything compared across loads.**
  - At-failure MDF is load-dependent (Jenkins, Tsoukos, Sakamoto).
  - Slope precision arrives too late (C7).
  - MPF is blind to type I fatigue (Gerdle 1992).

**C18 → A4, A5. The brief's 20–30-set test: agree with both, plus one point.**
- A failure set at a given load has more reps than a 3-RIR set *by construction*, so rep count alone separates them.
- The only informative version compares features **at a matched rep index** (e.g. reps 1…k of both set types) and predicts the outcome from data available before the stop decision.

---

## 3. Feature audit (eight questions)

Q1 measures the claimed construct? · Q2 directly validated in dynamic lifting? · Q3 could electrode movement, technique or muscle length explain the result? · Q4 threshold evidence-based? · Q5 generalises? · Q6 user can act on it beneficially? · Q7 risk of unnecessary fatigue, poor technique or false confidence? · Q8 what would falsify it?

**Rep counting & timing.**
- Q1: yes (event count).
- Q2: IMU yes, forearm/wrist: ±1 rep in 93% of sets (RecoFit), 91% (Soro). EMG-burst counting on a belly band: no.
- Q3: partials, pauses, rest-pause and co-contraction create or merge bursts.
- Q4: per-exercise thresholds, not evidence-based.
- Q5: unknown for belly-worn placement.
- Q6: yes, logging.
- Q7: low.
- Q8: video count disagreement above 2% of reps, or >1 false rep per 50, on held-out users.
- **A6: prototype.** Agree with A4.

**Electrical-activity duration.**
- Q1: yes, but threshold-defined.
- Q2: no on dry studs; textile bursts systematically longer than reference (Colyer 2018).
- Q3: yes; noise floor and contact change on/off times.
- Q4: no.
- Q5: values are not comparable across devices.
- Q6: no outcome use; TUT is not a lever (Schoenfeld 2015).
- Q7: low.
- Q8: onset/offset bias against a gel reference above about 50 ms, varying with contact.
- **A6: log only, not displayed as a metric.** Stricter than A4.

**Estimated TUT.**
- Q1: no; it is electrical or kinematic duration, not tension.
- Q2: no.
- Q3: yes.
- Q4: no target exists.
- Q5: n/a.
- Q6: no (0.5–8 s/rep equivalent).
- Q7: a "TUT score" invites slow reps with no benefit.
- Q8: n/a (no claim to falsify once renamed).
- **A6: show "set duration" only; drop the word "tension".** Agree with A4, and go further.

**Relative activation trend (amplitude within a set).**
- Q1: partly; amplitude is net drive minus cancellation (Keenan 2005).
- Q2: lab gel, yes (Jenkins, Sundstrup); dry studs, no.
- Q3: **yes, strongly**: sweat and impedance, band shift, velocity, load, plateau near failure.
- Q4: none.
- Q5: within-wear only.
- Q6: unclear.
- Q7: **yes**: users will chase a rising line, by squeezing or going slower, with no outcome evidence.
- Q8: within-set amplitude slope from TENSR vs adjacent gel pair, CCC < 0.8, or driven by impedance drift (baseline-noise trend).
- **A6: internal/research view only until Stage 3.** **Disagree with A4's "suitable to prototype" as a user feature** (C6).

**Within-set fatigue trend (MDF).**
- Q1: a peripheral electrophysiological marker (M, strong). Not capacity loss, not proximity to failure.
- Q2: lab wired gel, dynamic, group level, yes. TENSR, no.
- Q3: joint angle and IZ shift (16 mm), load, tempo (mixed); orientation unknown.
- Q4: no threshold; at-failure MDF is load-dependent.
- Q5: within person, exercise and load only.
- Q6: weakly; it describes the set after the fact.
- Q7: moderate; a falling line reads as "good set" and invites grinding.
- Q8: TENSR slope disagrees with an adjacent gel pair; or it adds nothing over IMU rep-duration slowdown in predicting reps to failure; or between-placement slope variance swamps the effect.
- **A6: post-set summary only, at DR ≥ 1–2 kSPS, gated by SQI. Drop it if it does not beat the IMU-only baseline.** Agree with A4's tier; stricter wording.

**Between-set recovery estimate / spectral rest timer.**
- Q1: no; spectral recovery ≠ readiness, and the direction of the dissociation is inconsistent (C4).
- Q2: no.
- Q3: yes; a probe contraction adds fatigue.
- Q4: no.
- Q5: no.
- Q6: the outcome literature already gives the answer: a ≥60–90 s floor, nothing gained beyond about 90 s for growth (Singer 2024). Longer for strength (Schoenfeld 2016).
- Q7: false precision.
- Q8: a randomised within-subject trial in which spectral-guided rest does not beat a fixed 2–3 min for next-set reps.
- **A6: research-only.** Agree with A4; different reason.

**Rest timer (elapsed time).**
- Q1: yes.
- Q2–Q5: trivial.
- Q6: yes, with an evidence-based default (≥ 90 s; 2–3 min for heavy compound work).
- Q7: low, if no "recovered" language is used.
- Q8: n/a.
- **A6: ship.** Agree with A4.

**Proximity to failure / live RIR.**
- Q1: no direct construct.
- Q2: **none** in dynamic free-weight lifting. Garofalo 2026 is isometric; Thomas & Wahlström is a preprint in which EMG added little to the IMU.
- Q3: yes, entirely.
- Q4: no.
- Q5: no; load-dependent (Robinson 2024, Lasevicius 2022, Jenkins 2015).
- Q6: only if better than the user's own bias-corrected guess. Even velocity reaches only <2 reps (Jukic 2024).
- Q7: **high**; feedback raises acute effort (Weakley 2023), so a biased cue drives extra fatigue.
- Q8: LOSO MAE not below *measured* self-report MAE (C1), or no gain over IMU-only.
- **A6: research-only, never displayed as a number in v1.** Agree with A4.

**Set score ("did this set reach failure").**
- Q1: a binary label the user already knows; the IMU sees a stalled rep.
- Q2: no.
- Q3: rep count and duration explain separation by construction (C18).
- Q4: no.
- Q5: no.
- Q6: **no**. The outcome evidence says failure adds trivial or no hypertrophy over 0–3 RIR (Refalo 2023/2024, Grgic 2022), and it costs more fatigue (Refalo 2024; Pareja-Blanco 2017).
- Q7: **high**; a "did you reach failure?" score rewards failure.
- Q8: n/a.
- **A6: research-only; do not ship as a score.** **Disagree with A4's "potentially useful after substantial validation".**

**Left/right comparison.** Not deliverable on one band; EMG asymmetry ≠ strength asymmetry. **A6: research-only.** Agree with A4.

**Technique / contraction quality.**
- Q1: undefined construct.
- Q2: no.
- Q3: yes.
- Q4: no.
- Q5: no.
- Q6: no.
- Q7: rewards amplitude.
- Q8: the construct must be defined first.
- **A6: unsupported.** Narrow IMU ROM-shrinkage within a set on moving-segment lifts is a later candidate (H). Agree with A4.

**Hypertrophy / set-effectiveness / stimulus score.**
- Q1: no.
- Q2: **contradicted**. Plotkin 2023 (higher glute EMG, no more growth); heavy loads give more EMG, not more growth (Schoenfeld 2017a, Lopez 2021, Morton 2016); amplitude unrelated to fibre-level signalling (Morton 2019).
- Q3–Q8: moot.
- **A6: do not build.** Agree; A6 rates it **contradicted**, not merely unsupported.

**Activation % ("is the target muscle doing the work").**
- Q1: no; one channel cannot apportion work, and crosstalk at 25.4 mm IED is unknown.
- Q2: no.
- Q3: yes.
- Q4: needs an MVC or submaximal reference each wear (Besomi 2020).
- Q5: no.
- Q6: no outcome link.
- Q7: mind-muscle chasing.
- Q8: n/a.
- **A6: unsupported/misleading.** Agree with A4.

**Eccentric/concentric split.**
- IMU on a moving segment only.
- No outcome reason to coach phase timing (Schoenfeld 2017c; tempo literature).
- **A6: log only, restricted list.** Agree with A4.

**Weekly volume (sets per instrumented muscle).**
- Q1: yes for counts.
- Q2: depends on rep and set detection.
- Q5: one muscle per band; compound lifts feed other muscles fractionally (Pelland 2026).
- Q6: yes; weekly sets is the best-supported dose variable.
- Q7: a "hard set" filter needs RIR. Use user-tagged effort instead.
- **A6: prototype counts with user tags. "Stimulus per muscle": do not build.** Agree with A4.

---

## 4. Disagreements with the draft recommendations

| # | agent | draft | A6 position | basis |
|---|---|---|---|---|
| D1 | A4 | Relative amplitude trend: suitable to prototype (user-facing) | Internal only until Stage 3 | C6; Colyer between-day CV 42%; Sundstrup plateau |
| D2 | A4 | Set score: potentially useful after validation | Research-only; rewards failure, which outcomes do not support | Refalo 2023/2024, Grgic 2022; C18 |
| D3 | A4 | Tempo-independent: "U, contradicted"; Zhao2025 against MDF–VL | "Not established, mixed"; Zhao is contradicted by its own group's IJSM 2025 | C5, C10 |
| D4 | A4 | 25.4 mm dip makes MDF depend "strongly on CV" | Irrelevant to the relative trend; absolute-only | C3 |
| D5 | A2 | Rest timer "contradicted" because MDF recovers faster than force | Unvalidated; dissociation direction inconsistent (Mills 1982) | C4 |
| D6 | A2 | Rodríguez-Rosell 2021 shows EMG insensitive where velocity is sensitive | Misapplied (training-adaptation EMG) | C9 |
| D7 | A3 | 500 SPS "cannot measure" MDF | Biased and compressed, partly correctable; still choose 2 kSPS | C2 |
| D8 | A3 | MDF trend estimable after about 4–6 reps | About 8 of 10 reps for t ≈ 2; no live use | C7 |
| D9 | A5 | S1.3 SD < 3 Hz; Stage 3 per-rep LoA ±10 Hz; MDC as the gate for within-set claims | Physically unattainable; gate on slope agreement against a two-reference-pair floor | C11 |
| D10 | A5 | RIR gate: MAE ≤ 1 rep, "better than self-report ~1 rep" | Compare with measured self-report MAE, raw and bias-corrected, same sessions | C1 |
| D11 | A5 | No long-term benefit of feedback (Orange 2022) | Orange is the wrong comparator; Weakley 2023 claims chronic benefit (low certainty); the risk is the sign of the effect | C12 |
| D12 | A1, A2, A5 | Halperin = "~1 rep accuracy" | ~1 rep bias, SD ≈ 1.45; better near failure and at heavy loads | C1 |
| D13 | A3 | Orientation not addressed; E2 "low concern" | Agree on E2 (equidistant geometry); orientation is the top unanswered hardware item | C8, C14 |
| D14 | A4 | IMU sees "almost no rep motion" on static segments | Untested; belly-tilt may help counting; phase split still unreliable | C13 |
| D15 | A4 | Electrical-activity duration: prototype as a descriptive number | Log, do not display | Colyer timing bias; no outcome relevance |

**Unchanged by the audit:**
- No optimal fatigue level, TUT or universal RIR target exists (A1).
- Amplitude is not a growth-stimulus measure (A1, A2).
- No validated sEMG RIR method exists for dynamic lifting (A2, A3, A4).
- Subject-wise validation against simple baselines is mandatory (A3, A5).
- The sample rate must be fixed before any spectral claim (A3, A4).
