# X2 findings: what sensor-based failure / RIR / RPE estimation has achieved in dynamic lifting

Agent X2, 2026-11-03. Rows: `X2-studies.csv` (41). Searches: `X2-searchlog.md` (43 WebSearches, ~8 over budget).
**Access:** WebFetch could not reach arxiv.org, pmc.ncbi.nlm.nih.gov or www.ncbi.nlm.nih.gov (host blocked in
this session). **No full text was read.** Every number here comes from an abstract or a search-engine summary
(ABSTRACT or SECONDARY). Where summaries disagreed, I say so.

## Summary (10 lines)

1. **No study reports reps-in-reserve error in reps, from a body-worn sensor, under confirmed subject-independent validation, in dynamic lifting.** That is still true after this round. [I; strong as an absence across 43 searches]
2. **The best wearable result is King 2025 (ICMLA; arXiv 2512.11854).** A wrist IMU flagged "near-failure" reps (RIR ≤ 2, counted back from true failure) with **F1 ≈ 0.82**. It covers 13 people, one exercise (preacher curl) and 631 reps, and the split design was not retrieved. [ABSTRACT; limited]
3. **Wearable RPE models report "±1 accuracy", not error.** Thomas & Wahlström 2025 (dumbbell curl, IMU+EMG, reportedly 5 men, 69 sets): **41.4% exact, 85.9% within ±1 RPE**, with the label given verbally after every rep. EMG added only a little, and the top feature was **eccentric rep time**. Baek 2025 (load cell, 32 men / 64 limbs): >93% within ±1 RPE, with a limb-level leakage risk. Neither reports a trivial baseline. [ABSTRACT; limited]
4. **Isometric only:** Garofalo 2026 (sEMG, deep learning, 12 people) is the only EMG "proximity to failure" model. Its error is not in reps. [already in A3/A6]
5. **The best objective benchmark is still bar velocity**, with absolute errors of **about 1.1–2.0 reps**:
   - Janicijevic 2024: 1.1–1.8, elite wrestlers, Smith squat.
   - Qin 2025: 1.3 ± 0.7 general model, Smith bench.
   - Jukic 2023/2024: individual 1.96 vs general 2.81 reps to failure; individual RIR <2.
   - It fails in recreational lifters: Mansfield 2023 got RIR wrong on 69.1% of reps.
   - Velocity loss alone is poor (Jukic 2023b: >10% error). [I; moderate]
6. **Individual calibration helps less than its R² suggests.** In Janicijevic 2024, individual fits had r² 0.96 against 0.84, yet absolute error was *no better* (1.2–1.8 vs 1.1–1.7 reps).
7. **EMG spectral and amplitude features explain about half the variance of power loss** in a dynamic trained-lifter task (González-Izal 2010: R² 0.47–0.50). The same group found the models **may fail after a training block** (2011). Amplitude **plateaus over the last 3–5 reps** before failure (Sundstrup 2012), so on its own it cannot separate "3 left" from "failure".
8. **Consumer devices:** no published validation of an effort, RIR or failure feature was found for WHOOP, Apple Watch, Garmin, Inara, Vitruve, Enode, RepOne or Metric. WHOOP publishes only *repeatability* (r 0.97), which is not accuracy.
9. **The human benchmark:**
   - Lifters underpredict by **0.95 reps** (95% CI 0.17–1.73; between-person SD 1.45; Halperin 2022). Trained lifters underpredict by 2.02 reps (0.0–4.04) in the Armes preprint.
   - Humans are most accurate near failure and at heavy loads.
   - Derived: if errors were normal with mean 0.95 and SD 1.45, human MAE ≈ **1.4 reps**, or ≈ **1.16** after bias correction (M; lower bound, because 1.45 is the between-person SD, not the full error SD).
10. **Conclusion.** The achievable figures today are:
    - **"Reps left": about 1.2–2 reps MAE**, and only with *bar* velocity on compound lifts. That is **no better than a lifter's bias-corrected guess**.
    - **"Failure now / ≤2 left": F1 ~0.8** from one small, unreplicated wrist-IMU study.
    - **Nothing has replicated.** No EMG or EMG+IMU method has beaten an IMU-only or rep-time baseline by a meaningful margin.

---

## 1. Wearable / ML studies on dynamic lifting: what was found

| study | target (label) | n | exercise | sensor | validation | result | leakage / design risk |
|---|---|---|---|---|---|---|---|
| King 2025 (ICMLA; arXiv 2512.11854) | per-rep RIR ≤ 2 (from **true failure**) | 13; 631 reps | preacher curl | wrist IMU | **not retrieved** | F1 0.82 (classifier) / 0.83 (segmentation); summaries disagree on which is which | single exercise; never sees sets stopped short; baseline unknown |
| Thomas & Wahlström 2025 (arXiv 2510.03197) | RPE per rep (verbal) | 5 men (one summary); 69 sets, >1000 reps | 1-arm DB curl | IMU + sEMG | **not retrieved** | 41.4% exact, 85.9% ±1 | n=5 with 1000 reps: a rep-wise split leaks by construction unless LOSO was used |
| Elshafei & Shihab 2021 (Sensors 21:759) | fatigue (Borg) | dataset of 20 | concentration curl | wrist IMU | subject-specific vs cross-subject | 98% vs **88%** | the 10-point drop moving to new users is the honest number |
| Elshafei 2022 (Sensors 22:1454) | same | same | same | wrist IMU | crowd-similarity personalisation | +5.9 points over cross-subject | relative gains only |
| Al-Mulla 2015 (A3) | fatigue/non-fatigue segments | 13 | DB curl | sEMG | 70/30 trial split | 87.9% | within-subject leakage; label = time-on-task |
| Albert 2021 (IEEE BIBM) | RPE per set | 16 | flywheel squat | 6 IMUs + ECG | not retrieved | MAPE 7.71%, r 0.85, **R² 0.48** | HRV/TRIMP most informative, so needs a chest strap |
| Baek 2025 (Sensors 25:6588) | RPE per set | 32 men / 64 limbs | robotic isokinetic bench | load cell | not retrieved | >93% ±1 RPE | limbs of one person may be split across train and test |
| Wang 2022 (Healthcare 10:2292) | 4 subjective fatigue states | n/r | isokinetic knee | sEMG | not retrieved | CNN 91.4% | machine; subjective classes |
| ICRA 2026 (arXiv 2602.15684, A3) | time-fraction to failure | 10 | robot-guided arm | sEMG | not retrieved | RMSE CNN 20.8% vs **linear 26.9%** | simple baseline nearly as good |
| Garofalo 2026 (JEK) | continuous proximity to failure | 12 | **isometric** curl | sEMG | leave-one-out (level unconfirmed) | MSE 49.4 ± 18.3 (units unclear) | isometric |
| González-Izal 2010 (JEK) | % power loss | 15 trained | leg press 5×10 | sEMG VM | in-sample | R² 0.47–0.50 | not to failure; group fit |

Context only (not lifting): Hwang 2025 sEMG+IMU fusion, gait, **LOSO 87.9%** (n=35); adding IMU to EMG improved it.
A PolyU goniometer curl model claims 95% accuracy and AUC 0.99. Its split is unknown, and near-perfect numbers on a
small dataset usually mean window-level splits, so it is UNVERIFIED and not used.

### Fact-checks on the striking numbers

- **"85.9% within ±1 RPE" (Thomas 2025) and ">93% within ±1 RPE" (Baek 2025).** A ±1 window on a scale whose labels
  cluster in a 3–4 point band is easy to hit. A constant "predict the median" model can score high ±1 accuracy. Neither
  abstract reports such a baseline, so these figures **cannot be read as skill** until compared with one. The exact-class
  figure (41.4%) is the informative one. [M]
- **Thomas 2025's EMG claim.** One secondary source says EMG was compressed into label representations used only in
  training, with test-time inference on IMU alone. If so, "IMU+EMG" means *EMG-informed labels plus an IMU model*. That
  supports the reading that **kinematics carry most of the usable signal**. UNVERIFIED.
- **Within-subject results drop on new people.** Elshafei 98% → 88%, and Hwang's LOSO is lower than typical
  within-subject figures. Every fatigue paper with >90% accuracy and no stated subject-independent split should be
  read as an upper bound. [I; moderate]
- **Janicijevic 2024.** r² of 0.96 for individual fits sounds like a big win over 0.84. In absolute error it is a tie.
  **R² is the wrong yardstick for RIR**; error in reps is the right one. [I; moderate]
- **Mansfield 2023, "69.1% wrong".** This uses an exact-RIR criterion, which is stricter than the ±1-rep or MAE used
  elsewhere. It is not directly comparable, but it does show that velocity-RIR breaks down in recreational lifters on
  bench and row. [I; moderate]

## 2. Bar-velocity RIR / reps-to-failure: the best objective method

| study | n / sample | exercise | model | prediction error |
|---|---|---|---|---|
| Janicijevic 2024 EJSS | 30 elite wrestlers | Smith back squat | general vs individual RTF–velocity | AE 1.1–1.7 (general), 1.2–1.8 (individual); not worse under fatigue |
| Qin 2025 BMC SSMR | 19 trained men | Smith bench, 60/80% | general RIR–velocity | **AE 1.3 ± 0.7**; %1RM-based methods overshot RIR by 2.8–5.8 reps at 60% |
| unresolved citation (via Qin search) | n/r | Smith + free bench | individual vs general | individual 0.64–1.36 vs general 1.25–2.00 at RIR 5; similar at RIR 2 and 0 |
| Jukic 2023a | 46 trained | squat (fastest rep) | individual vs general | mean error 1.96 vs 2.81 reps (total RTF) |
| Jukic 2024 Physiol Rep | (46) trained | free-weight squat | individual vs general RIR–velocity | individual <2 reps at all loads; general did not reach it |
| Jukic 2023b EJAP | trained | squat | velocity loss → % reps | >10% error, both models |
| Mansfield 2023 EJSS | recreational | bench, prone row | velocity at each RIR | wrong for 69.1% of reps |
| Sports Eng 2024 (device unnamed) | 57 men | lat pulldown, knee extension, bench | device estimate | ≤2-rep error in >90% of sets (pulldown, bench); knee extension worse; ICC 0.88 |
| Miras-Moreno 2023 Heliyon | n/r | prone bench pull | general | SEE ≈ 5.4 (Smith) / 6.6 (free) reps |

Takeaways:

- With the bar measured directly, on Smith-machine or free-weight compound lifts in trained people, velocity gets
  **about 1.1–2 reps of absolute error**. Errors are larger at light loads and far from failure.
- Isolation and machine evidence is one study, the unnamed Sports Engineering 2024 encoder device. It shows a
  **≤2-rep** tolerance met in >90% of sets, which is a looser criterion than MAE.
- None of this was done with a limb-worn IMU. FA and F6 already established that a limb IMU is not a bar sensor.

## 3. How the sensors compare with the lifter

| method | typical error | evidence |
|---|---|---|
| Lifter's own guess (Halperin 2022) | bias +0.95 (underpredicts); between-person SD 1.45; derived MAE ≈ 1.4 raw, ≈ 1.2 bias-corrected (lower bounds) | I, moderate (meta, I² 98%) |
| Trained lifters (Armes preprint) | underpredict 2.02 (0.0–4.04) | I, limited |
| Coaches from video (Emanuel 2022, n=259) | depends on exercise, load and proximity; experience negligible | I, moderate |
| Bar velocity, general or individual | AE ≈ 1.1–2.0 reps; fails in recreational (Mansfield) | I, moderate |
| Wrist IMU, near-failure flag | F1 ≈ 0.82, n=13, split unknown | I, very limited |
| Wearable IMU+EMG RPE | 41% exact, 86% ±1 RPE, n≈5 | I, very limited |
| sEMG alone, dynamic | no error-in-reps result exists; R² ≈ 0.5 for power loss | none / limited |

**Bottom line.**

- On the published evidence, **no sensor yet beats a bias-corrected lifter**. The best objective method, bar velocity,
  is at best on par. Humans are also most accurate exactly where TENSR wants to work: near failure, on heavy sets.
- A sensor's realistic edge is **not a lower MAE**. It is three things:
  - removing the lifter's systematic underprediction bias (about 1 rep, more in trained lifters);
  - consistency from set to set and day to day;
  - an objective **after-the-fact** readout: the slope in the final reps, and whether the last rep was a grind or a stall.

## 4. What this means for TENSR (feeds Q4)

- **Target the strongest claim the evidence allows: a binary/ordinal post-set "how close you got" (0 / 1–2 / 3+ RIR),**
  not a live rep count. King 2025 shows that RIR ≤ 2 detection at F1 ~0.8 from a wrist IMU is plausible. TENSR's IMU
  sits on the working segment, which is a better position. [H]
- **The IMU-only baseline comes first.** Every dynamic result points to **rep time (especially eccentric/concentric
  duration) and angular velocity** as the main signals: Thomas 2025's top feature, Elshafei's angular-velocity
  slowdown, and the bar-velocity literature. EMG has to earn its place **over** that baseline under LOSO. [I; limited]
- **EMG's plausible role** is the MDF slope across the set, as a second, tempo-independent channel. Amplitude cannot
  do this job because of the plateau. The calibration may drift with training (González-Izal 2011), so recalibrate
  periodically. [I; limited]
- **Validation design**, which A6's D10 already specifies:
  - leave-one-subject-out, *and* a separate session with the band re-applied;
  - labels from true sets to failure, with some sets stopped short and disguised as such;
  - report MAE in reps with CI, against both the **raw and bias-corrected self-report from the same sets**, plus a
    rep-number-only baseline and an IMU-only baseline;
  - include **isolation lifts**, because the bar-velocity evidence does not cover them.
- **Ready-made data to start on:** PERSIST (Albert 2022, Data 8:9; 12 trained men, flywheel squat, IMU+ECG, RPE per
  set) is public. It can test an IMU feature pipeline offline, though its labels are RPE, not RIR.

## 5. Not verified / open

- The validation splits of King 2025 and Thomas 2025: both arXiv full texts were unreachable. These two are the most
  product-relevant papers, so someone with arxiv access should read them before they are cited as more than "promising".
- The Smith vs free-weight bench individual/general RIR study: citation not resolved.
- The device and authors in Sports Engineering 2024 (s12283-024-00450-y).
- Jukic 2024's n (46 is shared with the 2023 fastest-rep paper and probably the same cohort, but this is not confirmed).
- Inara: no validation document found after one targeted search. That is an absence of evidence only.
