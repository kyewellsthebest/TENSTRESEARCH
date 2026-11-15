# TENSR validation plan

2026-11-02. This is a **proposal**. No human testing and no device changes were made in this investigation.

It is built from A5's design (`agent-notes/A5-findings.md`), corrected by the audit (`agent-notes/A6-audit.md`
C1, C7, C11, C12, C17, C18) and by A5's response (`agent-notes/A5-response.md`), which supersedes the original where
they differ.

**Labels used on every criterion:**
- **[RESEARCH-ESTABLISHED]** — a method or convention with a citation.
- **[ENGINEERING TARGET]** — a number we propose. It is not a published threshold and can be changed with a reason.

**The chain.** Each stage licenses the next. A failure invalidates everything downstream.
acquisition → repeatability → agreement with reference → prediction of a performance target → decision benefit.

---

## 0. Decisions needed before Stage 1

1. **Data rate.** Every agent recommends **2 kSPS (DR = 100)** for any spectral feature. At 500 SPS the ADS1292R's
   sinc3 filter is −3 dB at 131 Hz, and a true −25% MDF drop reads about −16% uncorrected. S1.3 compares the two rates
   on the bench and records the decision. The bring-up noise test at 500 SPS stays valid as a datasheet-condition check.
2. **Electrode orientation.** Record how the puck sits on the band relative to the E1–E3 axis. If the 44 mm axis
   runs around the limb, the pair is **across** the fibres of the fusiform limb muscles. Stage 3 tests both orientations.
3. **Electrodes for validation.** Decide whether snap-on gel electrodes will be used in any arm. They are the
   largest signal-quality lever without a respin. The product claim must be validated on what ships.
4. **Raw-data path.** Validation needs the raw EMG stream logged at full rate, not only on-device features.

---

## 1. Stage 1 — Bench verification (no humans)

**Question.** Does the board + firmware + analysis return known answers from known inputs?

**Reference equipment.**
- Arbitrary waveform generator, ≥16-bit.
- µV-level divider.
- An **RC network emulating dry-electrode impedance**, e.g. 250 kΩ vs 375 kΩ arms per `afe-sim-results.md`. An AWG's
  50 Ω output does not emulate skin.
- 50 Hz common-mode injection fixture, oscilloscope, BLE sniffer, at least two phone models.

**Inputs.**
- Synthetic EMG with analytically known MDF, stepped 120 → 90 Hz independently of amplitude.
- Burst trains at 1–6 s/rep.
- Recorded open-dataset sEMG played back.
- Sine sweeps, shorted input, common-mode sine.

| # | Test | Acceptance |
|---|---|---|
| S1.1 | Shorted-input noise, 10 s, gain 6 | < 3 µVrms in band [ENGINEERING TARGET, from BRING-UP §7]. The datasheet figure is still owed. |
| S1.2 | Sine sweep to fs/2 through the full chain (analogue + sinc3 + firmware filters) | Passband ripple < 0.5 dB across the chosen analysis band, and the measured response matches the model [ENGINEERING TARGET] |
| S1.3 (revised) | Synthetic EMG with known MDF, at **500 SPS and 2 kSPS**, epochs 0.25/0.5/1/2 s | Bias < 2 Hz per epoch length. SD within 10% of the simulated ideal-estimator SD for the same spectrum and epoch. Over a ≥10-rep synthetic 120→90 Hz decline, slope recovered within 10%. **This test decides the data rate.** [ENGINEERING TARGET]. The original "SD < 3 Hz" is dropped: the ideal estimator itself gives ~9.3 Hz at 0.5 s and ~4.7 Hz at 2 s. |
| S1.4 | Amplitude 20 µV–5 mV at fixed MDF | MDF change < 2 Hz below clipping; clipping onset recorded [ENGINEERING TARGET] |
| S1.5 | 50 Hz common mode with an imbalanced skin network, RLD on/off | Report against the simulated 28/48 dB. No threshold until the datasheet items are in. |
| S1.6 | Burst trains at 1–6 s/rep | No missed or extra reps at SNR ≥ 20 dB; onset error < 50 ms [ENGINEERING TARGET] |
| S1.7 | Step → phone timestamp latency | 95th percentile < 250 ms for a rep-level cue [ENGINEERING TARGET]. A per-rep record sent 0.3–0.6 s after the rep is realistic (A3). |
| S1.8 | BLE loss over 30 min at 1/3/5 m, in pocket, busy gym | < 0.1% lost, no gap > 100 ms at 1–3 m. Losses **flagged, never interpolated** [ENGINEERING TARGET] |
| S1.9 | Haptic motor, BLE and IMU on vs off | MDF shift < 1 Hz [ENGINEERING TARGET] |
| S1.10 | Determinism | Same raw file → bit-identical outputs across boards and builds |
| S1.11 | **Signal-quality index (SQI)** | Lead-off (including E2 contact loss), clipping, 50 Hz ratio, low-frequency motion energy and baseline-noise trend each trip the "no reading" state on injected faults. Zero silent outputs under fault [ENGINEERING TARGET] |
| S1.12 | **Electrical safety** before first human contact | DC and AC current through each electrode in normal and single-fault conditions (shorted RLD output, failed series resistor) within IEC 60601-1 type BF patient-auxiliary-current limits, used as internal limits. The device cannot be worn while charging from mains [ENGINEERING TARGET; standard used as a yardstick, not a legal requirement] |

Report every metric for all five boards. Board-to-board spread is itself a result.

---

## 2. Stage 2 — Human measurement repeatability

**Question.** How much do TENSR's outputs vary when nothing physiological has changed? Without this, no change in a
user's number can be interpreted.

**Methods [RESEARCH-ESTABLISHED].**
- ICC(A,1): two-way, absolute agreement, single measurement. Report the CI, not just the point (Koo & Li 2016;
  Weir 2005).
- SEM, and typical error as CV% for amplitude (Hopkins 2000).
- MDC95 = 1.96 × √2 × SEM (Weir 2005).
- Repeated-measures Bland–Altman with proportional-bias check (Bland & Altman 1999/2007).
- ICC is relative and sample-dependent; SEM/MDC is what an individual user needs. Report both.

**Participants.**
- Recreationally trained adults, both sexes.
- Measured spread of subcutaneous fat (ultrasound or skinfold).
- Hair and skin condition recorded.

**Protocol — three nested designs.**
1. **Within session, band untouched:** isometric 40% and 70% MVC, and fixed-load metronome sets.
2. **Within session, doff/don:**
   - the participant re-applies the band, which is the real-world condition;
   - then the researcher re-applies it, to separate user error from method error.
3. **Between session:** 2–3 visits 2–7 days apart, same time of day, no training of that muscle in the prior 48 h.

**Outcomes and acceptance.**

| ID | Outcome | Acceptance |
|---|---|---|
| S2-a | Absolute MDF, between sessions, isometric 70% MVC | Lower 95% CI of ICC(A,1) ≥ 0.75; MDC95 reported. **Gates between-session claims only** [ENGINEERING TARGET] |
| S2-b (new) | Per-set MDF **slope**, same load and rep count, band re-applied | Between-session SD of slope < ½ the mean slope at that load [ENGINEERING TARGET]. This is the right noise term for a within-set claim. |
| S2-c | Amplitude normalised to a same-session reference contraction | Between-session CV < 15% [ENGINEERING TARGET]. Context: raw amplitude CV was ~41–43% between sessions even on a reference system (Colyer 2018). Raw µV is **not expected** to be comparable. |
| S2-d | Rep count | ≥ 98% detected, ≤ 1 false rep per 50, vs video [ENGINEERING TARGET] |

**Confounders to record.** Wear time and sweat; logged baseline noise; band position (photo and skin marks) and
tension; fat thickness; time of day; prior training; caffeine; mains environment.

---

## 3. Stage 3 — Agreement with reference instruments during real lifts

**Question.** Does what TENSR reports agree with lab measurement of the same muscle during representative exercise?

**Reference equipment.**
- **sEMG:** research-grade wireless bipolar gel system at ≥ 2 kHz, placed per SENIAM (Hermens 2000)
  **immediately adjacent** to TENSR's pair along the fibres. Same analysis code on both. Concurrent recording, as in
  Lynn 2018.
- **Reference-pair floor:** on a subsample, **two adjacent reference pairs**, to measure how much two good pairs
  disagree. Adjacent pairs see different motor-unit territories.
- **Kinematics:**
  - linear position transducer for barbell lifts;
  - 3D motion capture on a subsample;
  - ≥ 120 fps video annotated by two blinded raters, with inter-rater ICC;
  - electrogoniometer or validated IMU pair for joint angle.
- **Force:** isokinetic dynamometer for MVC and controlled-velocity work.
- **Synchronisation:** a shared hardware trigger.

**Participants.**
- Trained and less-trained lifters, both sexes.
- A range of limb circumference and fat thickness.

**Exercises.**
- For each muscle the product will name: one single-joint and one multi-joint lift.
- ~60/75/85% 1RM, slow and fast tempo, free weight and machine.
- **Both pair orientations relative to the fibres** (C14).

**Statistics.**
- Repeated-measures Bland–Altman per outcome, stratified by exercise and intensity.
- **TOST equivalence** against pre-specified margins. Non-significance is not equivalence: Lynn 2018 concluded
  validity from a non-significant system effect with n = 12.
- Lin's CCC secondary. Pearson r is not agreement [RESEARCH-ESTABLISHED].

**Acceptance (revised).**

| ID | Outcome | Acceptance |
|---|---|---|
| S3-a | Per-set MDF slope, and mean of reps 1–3 vs last 3 | TENSR-vs-reference LoA ≤ 1.25 × the LoA between two adjacent reference pairs (**primary**) [ENGINEERING TARGET] |
| S3-b | Same | Half-width of the slope LoA < the mean group slope at that load (**usefulness ceiling**, kept by A5 against A6's objection; see CLAIM-VERIFICATION O5) [ENGINEERING TARGET] |
| S3-c | Per-rep MDF | **Reported only, no gate.** The estimator floor between two pairs is ~±20–26 Hz with perfect hardware. The original ±10 Hz target was physically unattainable. |
| S3-d | Within-set amplitude slope | Agreement with the reference, **and** shown not to track the baseline-noise or impedance trend. Required before any amplitude trend reaches a user. |
| S3-e | Rep count vs video | ≥ 98% per set across all exercises [ENGINEERING TARGET] |
| S3-f | IMU ROM and phase, moving-segment exercises only | ROM LoA within ±10° [ENGINEERING TARGET]. Static-segment exercises tested separately; no claim until shown. |
| S3-g | Orientation | If the across-fibre orientation fails S3-a, that orientation is excluded from the product and the band design must enforce alignment. |

**Muscles that fail are dropped from the claim, not averaged in.**

---

## 4. Stage 4 — Validation of fatigue and proximity-to-failure estimates

**Reference targets.**
- **Actual reps to failure.** Every RIR-labelled set is continued to momentary failure, defined per Steele 2017 with
  technique criteria fixed in advance. Two raters label failure blind to TENSR; why each set ended is recorded.
- **Velocity loss** from a linear position transducer.
- **Isometric MVC drop**, pre/post set.
- **Self-reported RIR is a comparator, not truth** (Halperin 2022: bias ~0.95 reps, SD ~1.45).
- **Day-to-day variability in reps to failure** at fixed load sets the floor for any predictor. Measure it.

**Two-visit RIR design.**
1. Visit A establishes reps to failure at a load.
2. Visit B repeats the load and stops at a prescribed rep.
3. TENSR's prediction and the lifter's own estimate are recorded.
4. The set then continues to failure, giving true RIR at the stop point.

**Validation structure [RESEARCH-ESTABLISHED].**
- **Leave-one-subject-out**, or grouped k-fold by participant. Record-wise splits overestimate accuracy (Saeb 2017).
- New-session, new-exercise, new-load and new-tempo held-out tests are reported separately.
- Leakage controls:
  - normalisation, feature selection, epoch length and thresholds are chosen inside training folds only;
  - the total rep count of the set is never a feature;
  - the brief's pilot sets are never reused as the test set for the thresholds they inspired.
- Calibration plots with slope and intercept (Van Calster 2019).
- Model sample size by Riley 2020/2024 criteria, not rules of thumb.
- **Population model vs k = 1/2/3 calibration sets**, with the learning curve reported. The velocity precedent
  (Jukic 2024) predicts per-user calibration will be needed.

**Mandatory baselines.** Any EMG feature that does not beat these is dropped:
- (a) rep count plus population average reps-to-failure at that load;
- (b) IMU-only rep-duration slowdown;
- (c) the lifter's own estimate, raw and **bias-corrected** using only their earlier sessions.

**S4.matched — design rule (C18).**
- Features come only from reps 1…k, where k is the shorter set's stop rep, at matched load.
- Predictions use only data available before the stop decision.
- Rep count and duration at rep k are mandatory baselines.

**Acceptance (revised).**

| ID | Criterion |
|---|---|
| R4.1 (primary gate) | Same sessions, same rep. Paired difference in MAE (TENSR − bias-corrected self-report) under leave-one-subject-out validation, with a participant-bootstrapped upper 95% CI < 0. **Beating only raw self-report does not pass.** [ENGINEERING TARGET] |
| R4.2 | Beats the IMU-only baseline by ≥ 0.3 reps MAE, CI excluding 0 [ENGINEERING TARGET] |
| R4.3 | Absolute MAE for true RIR 0–3 **reported**, against the Jukic 2024 "<2 reps" benchmark for individualised velocity models [benchmark: RESEARCH-ESTABLISHED, I]. "≤ 1 rep" is an aspiration, not a gate. |
| R4.4 | R4.1 holds within RIR 0–3 on its own. Humans are most accurate near failure, so winning at RIR 6–10 does not count [ENGINEERING TARGET] |
| R4.5 | Post-set MDF trend: must add predictive value over (a) and (b) or it is removed from the product [ENGINEERING TARGET] |
| R4.research | Pre-registered research test of rep-level MDF features against IMU baselines. **Not a product gate.** A documented null retires the brief's central claim. |

---

## 5. Stage 5 — Does feedback improve decisions or outcomes?

**Why separate.** A valid measurement does not imply benefit.
- Velocity-feedback precedent: feedback reliably raises **acute** effort (Weakley 2019a, 2020; Weakley 2023
  meta-analysis of 20 studies, g ≈ 0.63, visual > verbal).
- Weakley 2023's authors also concluded chronic adaptations improved. The certainty is low, the chronic trials are few,
  and the main one (n = 28) used magnitude-based inference.
- None of it transfers to EMG-derived feedback [H].
- **The key risk is the sign of the effect.** A biased "2 left" cue will push users past their intended stop.

**Designs, in order.**
1. **Acute decision-quality crossover** (cheapest, first).
   - Arms, randomised order, ≥ 72 h apart: TENSR cue vs self-report vs device worn but blinded.
   - Target: stop at RIR 2. Each stop is continued to failure to obtain actual RIR.
   - **S5.1 safety gate [ENGINEERING TARGET]:**
     - mean (achieved − intended RIR) within ±0.5 rep, 95% CI;
     - the share of sets ending ≥ 1 rep nearer failure than intended is non-inferior to bias-corrected self-report,
       with a 10-percentage-point margin.
   - **S5.2 [ENGINEERING TARGET]:** record fatigue cost per arm — velocity loss, next-set reps at the same load,
     24/48 h soreness. Extra volume bought at disproportionate fatigue is not a benefit.
2. **Parallel-group RCT, 8–12 weeks.** Runs **only after R4.1 and S5.1 pass.**
   - TENSR feedback vs the same programme with self-report; both arms wear the device.
   - Primary outcome (choose one in advance):
     - ultrasound thickness of the instrumented muscle, blinded sonographer, marked sites;
     - 1RM or isokinetic torque, blinded tester.
   - ANCOVA on post with a baseline covariate, ITT, CONSORT, pre-registered.
   - **Claim rule [ENGINEERING TARGET]:** the 95% CI excludes zero **and** the point estimate exceeds the outcome's
     smallest detectable change. Otherwise market measurement features only.
3. N-of-1 designs are unsuitable for hypertrophy (carry-over) and are used only for acute decision outcomes.

**Blinding limits.** Participants cannot be blinded to feedback. Use assessor blinding, a display-off arm and
expectation questionnaires.

---

## 6. Sample-size planning (precision-based; no universal n)

Plan from the claim and the precision needed. A5's worked examples were all recomputed by A6
(`agent-notes/A6-check-stats.py`).

| Claim | Assumptions | Result |
|---|---|---|
| Test–retest ICC good | ICC 0.85, 2 sessions, 95% CI width 0.2 (Bonett 2002) | ~31 participants. **A floor for ICC(A,1)**, because systematic session bias widens the CI. Size by simulation or Zou 2012 with assurance. |
| SEM precision | χ² CI on SEM | ×0.74–1.55 at n = 15; ×0.80–1.34 at n = 30; ×0.85–1.22 at n = 60 |
| Agreement LoA | SE(LoA) ≈ √(3/n)·s (Bland–Altman) | If the true difference SD is 5 Hz, LoA = ±9.8 Hz. A "±10 Hz" claim **cannot be shown at any n.** Applies to multi-rep means, not single reps. |
| "Flags ≤ 1 RIR" sensitivity | Sensitivity 0.85 ± 0.07 | ~100 positive sets; ~180 sets / ~36 people allowing for clustering (assumption-dependent) |
| Outcome RCT | SMD 0.3 | ~175 per group; ~63 with ANCOVA at pre/post r = 0.8 |
| The brief's pilot | 27/30 correct | Wilson 95% CI 74–97% — **for one person's sets only**, carrying no information about other users |

---

## 7. Safety, consent and ethics (for later testing)

- **HREC.**
  - Review under the NHMRC National Statement on Ethical Conduct in Human Research. The 2023 edition is in force from
    1 Jan 2024; NHMRC refers to a 2025 edition, so **check which edition applies on the application date.**
  - Training to failure, MVC testing and a novel electrical device on skin plausibly make Stages 2–5 **higher risk**,
    needing full HREC review.
  - Stage 1 needs none. Use a university partner or a registered independent HREC.
- **Consent.** Plain-language statement covering:
  - the device is an unvalidated prototype;
  - risks of failure training (DOMS, strain, rare exertional rhabdomyolysis);
  - skin reactions;
  - that body data is collected;
  - the right to withdraw;
  - what happens to the data.
- **Screening.**
  - Australian adult pre-exercise screening.
  - Exclude: implanted electronic devices (the RLD injects current), uncontrolled cardiovascular disease, recent
    musculoskeletal injury, and pregnancy for maximal tests.
  - Spotters and safety bars on every failure set; first-aid-trained staff; graded familiarisation.
- **Skin.**
  - Nickel release from stainless studs: screen for nickel allergy or patch-test.
  - Photograph the skin before and after; grade reactions on a pre-defined scale.
  - Consider ISO 10993-5/-10 evidence for skin-contact materials.
- **Electrical safety.** S1.12 must pass before first contact. No wearing while mains-charging. LiPo handling rules.
- **Privacy.**
  - Body data falls under the Privacy Act 1988 (Cth) and the APPs.
  - Collect the minimum; de-identify at source; set retention periods.
  - Use research data for model training only with explicit consent.
- **Adverse events.** Pre-defined categories (skin, musculoskeletal, cardiovascular, device malfunction or heat),
  severity, causality, HREC reporting timelines and a stopping rule. Report zero counts too.
- **TGA boundary.** The wellness exclusion applies only if **every** function qualifies. No injury, rehab, diagnosis
  or "imbalance risk" language in study or product material. Do not run patient or rehab studies under the product's
  name.
- **Conflict of interest.**
  - Kye owns the product. Pre-register on OSF and share the analysis code.
  - The Stage 4 test-set analysis must be run by someone not involved in model development.
  - Publish negative results.

---

## 8. Summary

| Stage | Question | Gate to proceed |
|---|---|---|
| 1 Bench | Does the chain return known answers? | S1.1–S1.12; **data rate decided at S1.3**; SQI and electrical safety pass |
| 2 Repeatability | How big is noise when nothing changes? | S2-b slope reproducibility after re-application; S2-a for any between-day claim |
| 3 Agreement | Does TENSR agree with lab sEMG and kinematics in real lifts? | S3-a/b per muscle and orientation; failed muscles dropped |
| 4 Prediction | Does it predict reps to failure better than the lifter and the IMU? | R4.1, R4.2, R4.4 under leave-one-subject-out |
| 5 Benefit | Does feedback improve decisions, then outcomes? | S5.1 acute safety gate, then RCT claim rule |
