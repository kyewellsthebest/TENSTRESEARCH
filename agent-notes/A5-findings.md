# A5 — Validation and experimental design (draft of TENSR-VALIDATION-PLAN.md)

Agent A5, 2026-11-02. Answers RQ5 (how to validate accuracy, repeatability and decision benefit) and feeds RQ4/RQ6.
Evidence codes and strengths per `PROTOCOL.md` §5. Citation keys refer to `A5-studies.csv`.

**Search budget.** The shared web-search budget for this turn ran out before de Vet 2006, the Jukic papers and García-Ramos 2018 could be checked beyond the snippets already gathered; those are marked accordingly in the CSV.

**Access caveat, stated once.** In this session WebFetch could not resolve pubmed, PMC, springer or university
repositories (DNS refused; logged in `A5-searchlog.md`). Every source below was verified at the level of
bibliographic record + abstract/snippet via web search, not full text, unless marked otherwise. Formulas used in
the worked examples were checked numerically where possible: Bonett's (2002) formula reproduces his published
worked example (k = 4, ICC 0.85, width 0.2 → n = 19.2) exactly, which is the check that the formula below is
transcribed correctly.

**Labels used for every acceptance criterion.**
- **ENGINEERING TARGET (proposed)** — a number A5 proposes for TENSR. It is not from literature and must be argued
  for by Kye before data are collected, then pre-registered.
- **RESEARCH-ESTABLISHED** — a convention or threshold that is published, with citation. Note that most
  "established" thresholds here are *conventions* (e.g. how to label an ICC), not evidence that a value is
  adequate for a product decision.

---

## 0. What the programme has to establish, and the order it must go in

The product brief (CLAUDE.md) states the decisive test as "20–30 sets, half to true failure, half stopped 3 reps
short… the two groups must separate… about 9 times in 10". That test is a reasonable *Stage 4 pilot*, but on its
own it cannot establish the claim, for four reasons:

1. **It skips Stages 1–3.** If the device's median frequency (MDF) is wrong on the bench, or disagrees with a
   reference sEMG system on the same muscle, a separation result is uninterpretable. Validation is a chain:
   acquisition → repeatability → agreement with reference → prediction of a performance target → decision benefit.
   A link failing invalidates everything downstream.
2. **"9 times in 10" from one person's 20–30 sets is not an accuracy estimate.** Sets from one person are not
   independent, and the classifier/threshold would be tuned and tested on the same sets (leakage; Saeb2017).
   A 90% observed accuracy on 30 sets has a 95% Wilson CI of roughly 74–97%, before any clustering correction.
3. **"3 reps short" is not ground truth unless the set is then taken to failure** to confirm how many reps were
   actually left (see §4.2). Self-estimated RIR carries ~1 rep average error with very high heterogeneity
   (Halperin2022).
4. **Separation of two extreme groups (0 vs 3 RIR) is a classification at one easy threshold.** The product claims
   live RIR ("about 2 left"), which is a continuous prediction and needs MAE and calibration, not accuracy.

Internal inconsistency to resolve before Stage 1 (from PROTOCOL §1): bring-up uses **500 SPS** (Nyquist 250 Hz)
while the analysis brief says a **20–450 Hz** band-pass. A 450 Hz upper edge is impossible at 500 SPS; MDF
estimated at 500 SPS is computed on a spectrum truncated at 250 Hz and will be biased low relative to a 2 kHz
reference system. This is not a validation question, it is a design decision that Stage 1 must test against
(see S1.3). [H; engineering fact]

---

## 1. Stage 1 — Bench verification of acquisition and processing

**Purpose.** Show that the board + firmware + analysis pipeline returns known answers from known inputs, before any
human is involved. No literature can substitute for this; it is the product's own engineering record. Evidence
code throughout: H (product-specific), methods from I/M literature.

**Reference equipment.** Arbitrary waveform generator (≥16-bit, can play back a file); precision attenuator/divider
to µV levels (e.g. 1000:1 resistive divider with a known source impedance); RC network emulating skin–electrode
impedance (e.g. 250 kΩ ∥ few nF per arm, as modelled in `afe-sim-results.md`); a 50 Hz common-mode injection
fixture; oscilloscope; a BLE sniffer or second receiver; a lab sEMG amplifier for cross-check (optional).

**Inputs.**
- *Synthetic EMG with known spectral parameters.* Band-limited Gaussian noise shaped by a standard sEMG spectral
  model, generated so that its MDF is known analytically, stepped down in controlled increments (e.g. 120 → 90 Hz,
  matching the brief's claimed fatigue range) with amplitude stepped independently. Farina & Merletti (Farina2000)
  established the practice of comparing spectral estimators on simulated signals with known MDF/MNF and showed the
  dependence of estimator variance on epoch length; a 2022 simulation study (Corvini2022, SECONDARY/ABSTRACT)
  examined factors influencing MNF/MDF during simulated fatigue. [I/M, moderate for the method]
- *Burst-modulated synthetic EMG* at rep-like timing (0.5–3 s bursts, variable duty cycle, tempo 1–6 s/rep) — to
  test rep segmentation and to check that MDF is **tempo-independent in the pipeline** (the brief's central claim
  depends on this; dynamic contractions shorten stationary epochs, González-Izal et al. 2012, J Electromyogr Kinesiol 22:501 — content not read, background only).
- *Recorded real sEMG* from an open dataset played back through the generator (keeps realistic non-stationarity).
- Sine sweeps, shorted input, and common-mode sine.

**Protocol and outcomes (each a bench test, repeated on all five boards).**

| # | test | outcome | acceptance |
|---|---|---|---|
| S1.1 | Shorted-input noise, 10 s, gain 6 | µVrms in analysis band; spectrum lines | **ENGINEERING TARGET** < 3 µVrms (already in `BRING-UP.md` §7); datasheet figure owed (BRING-UP §7) |
| S1.2 | Sine sweep 1–(fs/2) Hz at known amplitude | magnitude/phase response of full chain incl. decimation + firmware filters | **ENGINEERING TARGET** passband ripple < 0.5 dB across the analysis band; measured response must match the simulated one |
| S1.3 | Synthetic EMG, MDF known, at 500 SPS and at 1–2 kSPS | MDF bias and SD vs truth, per epoch length (0.25–1 s) | **ENGINEERING TARGET** bias < 2 Hz, SD < 3 Hz at the chosen epoch; *and* tracked MDF shift (120→90) recovered with slope error < 10%. If 500 SPS fails, the sampling rate decision is made here |
| S1.4 | Same, amplitude varied 20 µV–5 mV independently of MDF | MDF independence from amplitude; clipping onset | **ENGINEERING TARGET** MDF change < 2 Hz across amplitude range below clipping |
| S1.5 | Common-mode 50 Hz, with skin-impedance imbalance network (250 k vs 375 k) | CMRR at 50 Hz with RLD on/off | **ENGINEERING TARGET** report measured value against the 28/48 dB simulated figures; no threshold until datasheet items are in |
| S1.6 | Burst train at tempi 1–6 s/rep | rep-count error, burst onset/offset timing error | **ENGINEERING TARGET** 0 missed/extra reps on clean synthetic bursts at SNR ≥ 20 dB; onset error < 50 ms |
| S1.7 | Latency: generator step → on-phone timestamp | end-to-end latency distribution | **ENGINEERING TARGET** 95th percentile < 250 ms for "live" feedback (rep-level haptic cue) |
| S1.8 | BLE packet loss: 30 min stream, phone at 1, 3, 5 m, in pocket, in a gym with other BLE | % packets lost, longest gap | **ENGINEERING TARGET** < 0.1% lost and no gap > 100 ms at 1–3 m; losses must be *flagged* in the data, never silently interpolated |
| S1.9 | Haptic/BLE/IMU on vs off during S1.1 and S1.3 | change in noise and MDF | **ENGINEERING TARGET** no measurable MDF shift (< 1 Hz) with motor running |
| S1.10 | Determinism | same input file → identical outputs across boards and firmware builds | **ENGINEERING TARGET** bit-identical analysis outputs from the same raw file |

**Confounders.** Generator output impedance (an AWG's 50 Ω output does not emulate a 250 kΩ dry electrode — use the
impedance network); the divider's own noise; mains coupling through the bench; phone model and OS (BLE stacks
differ — test ≥ 2 phones). **Statistics.** Report every metric per board, mean and range across five boards.
Board-to-board spread is itself a result (BRING-UP: "one board differing from four siblings is a build fault").

**What Stage 1 cannot show.** Anything about skin, motion artefact, or physiology. Passing Stage 1 only licenses
moving to humans.

---

## 2. Stage 2 — Human measurement repeatability

**Purpose.** Quantify how much TENSR's outputs (RMS amplitude, MDF, rep count, the composite fatigue score) vary
when nothing physiological has changed. Without SEM/MDC, no change in a user's number can be interpreted.

**Distinguish reliability from agreement.** ICC is *relative* consistency (ranking people) and depends on the
between-subject spread of the sample; SEM/typical error is *absolute* consistency in the measurement's units and is
what an individual user needs (Weir2005; Hopkins2000; also de Vet et al. 2006, J Clin Epidemiol — UNVERIFIED, search budget exhausted before it could be checked). A homogeneous sample of trained lifters can give
a low ICC with a small SEM, and vice versa. Report both, always. [RESEARCH-ESTABLISHED methodology, strong]

**Reference equipment.** None needed for repeatability itself; standardise with an isometric dynamometer or a fixed
load + metronome so that the *task* is constant. Skin-prep protocol, a marked skin template (surgical marker / photo
with landmarks) for band position, and a band tension gauge.

**Participants.** Recreationally trained adults (≥ 1 yr resistance training), both sexes, a spread of
subcutaneous-fat thickness (measure it with ultrasound or skinfold; fat thickness is a known attenuator of sEMG
amplitude and spectrum — A2/A3 hold the evidence). Report BMI and skinfold as covariates.

**Protocol — three nested designs.**
1. *Within-session, band untouched:* 3 × submaximal isometric contractions at 40% and 70% MVC and 3 × reps at fixed
   load and metronome tempo, 3 min rest. Isolates instrument + physiological trial-to-trial noise.
2. *Within-session doff/don:* band removed and re-applied by the participant (not the researcher) between blocks —
   the real-world condition. Repeat with researcher application to separate user error from method error.
3. *Between-session:* 2–3 sessions 2–7 days apart, same time of day, no training of that muscle in the prior 48 h,
   user re-applies.

The forearm reapplication literature already warns that inter-day removal/replacement can drive ICC below 0.5 while
SEM stays similar, and between-day MDF-slope reliability in multi-joint quadriceps fatigue tasks has been reported
as mostly low (search snippets in `A5-searchlog.md`; primary studies not opened — UNVERIFIED as to exact values).
Treat doff/don as the most likely point of failure for a band product. [I, limited]

**Outcomes and statistics.**
- **ICC**: choose the form per Koo & Li (KooLi2016) and Weir (Weir2005). For test–retest with sessions as fixed
  occasions and the claim being about *a single measurement*: two-way mixed effects, absolute agreement, single
  measurement — ICC(A,1) in McGraw & Wong notation (≈ ICC(2,1)/(3,1) depending on convention). Absolute agreement,
  not consistency, because a systematic session shift (e.g. day-2 MDF 5 Hz lower) is exactly what a user would
  misread as fatigue. Report the software, model, type and definition (KooLi2016 reporting requirement).
  Interpret the **95% CI**, not the point: <0.5 poor, 0.5–0.75 moderate, 0.75–0.9 good, >0.9 excellent
  (KooLi2016 — RESEARCH-ESTABLISHED as a labelling convention, SECONDARY for the exact cut-points).
- **SEM** = SD × √(1 − ICC), or better, √(within-subject mean square) from the ANOVA (Weir2005). Typical error as CV%
  when error scales with magnitude, which is expected for EMG amplitude (Hopkins2000).
- **MDC95 / SDC** = 1.96 × √2 × SEM (Weir2005; the SDC terminology is de Vet's — UNVERIFIED here). This is the smallest change in one user's number that
  exceeds measurement noise at 95% confidence — the number that decides whether a per-set or week-to-week change
  shown in the app means anything.
- **Bland–Altman** on session 1 vs 2: bias, 95% LoA with their CIs, and a regression of difference on mean to test
  proportional bias; if present, use regression-based or log-transformed LoA (BlandAltman1999). With several reps
  per person, use the repeated-measures variant (Bland & Altman 2007, not opened — SECONDARY via BlandAltman1999
  record), never pool reps as if independent.
- **Systematic change in the mean** (learning, skin hydration) reported separately (Hopkins2000).

**Confounders.** Skin hydration/sweat (dry electrodes: impedance falls over minutes of wear — record wear time and
log pre-contraction baseline RMS); band position and rotation (photograph); band tension; fat thickness; time of day;
prior training; caffeine; ambient mains environment; contraction intensity drift (control with dynamometer feedback).

**Acceptance criteria.**
- ICC form and reporting — RESEARCH-ESTABLISHED (KooLi2016, Weir2005).
- **ENGINEERING TARGET** for MDF (isometric 70% MVC, doff/don between sessions): lower 95% CI of ICC(A,1) ≥ 0.75
  *and* MDC95 smaller than **half** the claimed fresh-to-failure MDF drop. If the brief's 120 → 90 Hz (30 Hz) drop
  is real, MDC95 must be < 15 Hz for a single set to be readable, and < ~10 Hz for "reps left" resolution. Note the
  30 Hz figure is itself a product hypothesis [H] that Stage 3 must measure.
- **ENGINEERING TARGET** for RMS amplitude: CV of normalised RMS (to a same-session reference contraction) < 15%
  between sessions. Raw µV amplitude is not expected to be comparable between sessions without normalisation.
- **ENGINEERING TARGET** rep count: ≥ 98% of reps detected, ≤ 1 false rep per 50, against video.

---

## 3. Stage 3 — Agreement with reference instruments during representative exercises

**Purpose.** Show that what TENSR reports from a dry 25.4 mm bipolar pair on a band agrees with a lab-grade
measurement of the same muscle during real lifts, and that its rep timing, ROM and velocity proxies (from the IMU)
agree with kinematic references.

**Reference equipment.**
- *sEMG:* research-grade wireless bipolar gel system (e.g. Delsys Trigno, Noraxon), placed per SENIAM
  (Hermens2000) for that muscle, **immediately adjacent** (proximal or distal along the fibre direction) to TENSR's
  pair, sampled ≥ 2 kHz, same analysis code applied to both. Concurrent recording is essential: Lynn et al. (Lynn2018)
  validated the Athos garment by placing research electrodes just distal on the same muscle, specifically because an
  earlier validation had not recorded concurrently. Adjacent ≠ identical: the two pairs see different motor-unit
  territories and innervation-zone distances, so some disagreement is physiological, which is why agreement limits
  must be judged against Stage 2's own between-placement variability of the *reference* system (place two reference
  pairs on a subsample to measure this).
- *Bar/limb velocity:* linear position transducer (e.g. GymAware) for barbell lifts; LPTs show high validity for
  mean velocity against 3D motion capture in squat and bench but weaker in deadlift (Lorenzetti2017; Dorrell, SECONDARY
  via search snippet). Use 3D motion capture as criterion on a subsample.
- *Force/torque:* isokinetic dynamometer for single-joint isometric MVC and controlled-velocity work (biceps,
  quadriceps); force plate for multi-joint lifts.
- *Rep timing and ROM:* 3D motion capture or ≥ 120 fps synchronised video with manual annotation by two blinded
  raters (inter-rater ICC reported); electrogoniometer or a validated IMU pair for joint angle.
- *Synchronisation:* a shared hardware trigger (button press visible to all systems / LED in video / tap on the
  puck); report residual sync error.

**Participants.** Trained and less-trained lifters; both sexes; a range of limb circumferences and fat thickness;
include hairy skin and darker skin (no reason to expect EMG differences from skin tone, but pigmentation and hair
matter for any optical add-on and hair for dry contact — record it).

**Exercises.** For each muscle the product names, at least one single-joint and one multi-joint lift (e.g. biceps:
dumbbell curl, chin-up; quadriceps: knee extension, back squat), at ~60%, 75% and 85% 1RM, at slow and fast tempo,
and with free weight vs machine. Include an isometric MVC block for normalisation and an exercise-specific
reference contraction.

**Outcomes.** Per rep: RMS (normalised), MDF and MNF (same epoch rule on both systems), burst onset/offset, rep count,
concentric/eccentric split; IMU-derived ROM and peak/mean angular velocity vs goniometer/mocap; IMU-derived
velocity proxy vs LPT.

**Statistics.**
- Bland–Altman per outcome with LoA CIs; repeated-measures LoA (multiple reps per person); proportional bias;
  stratified by exercise and intensity. Also report **agreement of within-set slopes** (MDF change per rep), because
  the product claims a *change*, and two systems can disagree in level yet agree in slope.
- **Equivalence testing (TOST) against a pre-specified margin**, not "no significant difference". Lynn2018 concluded
  validity from no significant effect of system with n = 12 — a non-significant difference is not equivalence
  (SHARED-STANDARDS §6). [RESEARCH-ESTABLISHED principle]
- Concordance (Lin's CCC) as a secondary summary; Pearson r is not agreement.

**Confounders.** Motion artefact (cable-free on TENSR but band slides on contraction), crosstalk from neighbouring
muscles (one channel cannot reject it), innervation zone position, electrode–skin impedance change with sweat,
muscle shortening under a fixed electrode in dynamic work (González-Izal et al. 2012, J Electromyogr Kinesiol 22:501 — content not read, background only discusses non-stationarity), load and
joint angle effects on MDF independent of fatigue.

**Acceptance criteria.**
- Placement and reference methodology — RESEARCH-ESTABLISHED (Hermens2000; BlandAltman1999).
- **ENGINEERING TARGET**: MDF per-rep LoA within ±10 Hz *and* within-set MDF slope agreement CCC ≥ 0.8 vs adjacent gel
  reference, at 75% 1RM, for each muscle claimed. Muscles that fail are dropped from the claim, not averaged in.
- **ENGINEERING TARGET**: rep count agreement with video ≥ 98% per set across all exercises; ROM LoA within ±10°.
- **ENGINEERING TARGET**: disagreement between TENSR and reference no larger than disagreement between two adjacent
  reference pairs (the physiological floor).

---

## 4. Stage 4 — Validation of fatigue, proximity-to-failure and performance estimates

### 4.1 Reference targets (what "truth" is)

| target | how measured | strength as truth |
|---|---|---|
| **Reps to momentary failure (RTF) / actual RIR** | set taken to momentary failure under standardised definition; RIR at rep *i* = total reps − *i* | best available, but failure itself is noisy and motivation-dependent (Steele2017a) |
| **Velocity loss %** | LPT, first vs fastest rep vs current rep | well-characterised fatigue index for barbell lifts (SanchezMedina2011) [I, moderate]; not available for TENSR's users, so a reference only |
| **Isometric MVC drop pre/post set** | dynamometer, MVC within 30 s of set end | direct neuromuscular fatigue measure; logistically heavy |
| **Self-reported RIR** | after each rep or set | **not** ground truth: average under-prediction ~0.95 reps, I² ≈ 98% (Halperin2022); trainees underpredict reps to failure (Steele2017b) |

**Labelling failure.** Use Steele et al.'s set end-point terminology (Steele2017a): *momentary failure* = unable to
complete the concentric phase of the next rep despite maximal effort, with standardised technique criteria agreed in
advance (ROM threshold from the goniometer/IMU, no pausing beyond X s). Two raters label failure from video blind to
TENSR output; report inter-rater agreement. Record *why* the set ended (failure, technique breakdown, pain, refusal).
Sets ended for pain/refusal are not failure and are not RIR-labelled.

**RIR ground-truth design.** Every set used for RIR validation must be **continued to failure**. "Stop 3 short"
sets cannot be labelled RIR = 3 without that; use a two-visit design instead: visit A establishes RTF at a load;
visit B repeats the load and stops early at a prescribed rep, then (after the TENSR prediction is recorded) the
participant continues to failure, giving true RIR at the stop point. Day-to-day RTF variability at fixed load sets a
floor on how accurate any predictor can be — measure it (Stage 2 design) and report it.

### 4.2 Validation structure and leakage

- **Subject-independent evaluation.** Leave-one-subject-out (LOSO) or grouped k-fold by participant for any model or
  threshold learned from data. Record-wise (rep-wise or set-wise) splitting lets the model learn the person rather
  than the fatigue state and "often massively overestimates" accuracy (Saeb2017; counter-view in the companion
  commentary, Little et al. 2017 GigaScience gix020, that subject-wise CV is not always sufficient). [RESEARCH-ESTABLISHED, strong for the
  principle]
- **Additional held-out axes**, each reported separately: new session (train day 1, test day 2 — includes doff/don),
  new exercise (train curls, test chin-ups), new load, new tempo, new muscle. A model that only works within an
  exercise it has seen must be marketed that way.
- **Calibration-required vs calibration-free.** The velocity literature is the closest precedent: individual
  RIR-velocity relationships outperform general equations, and only individual relationships from a prior session
  gave mean error < 2 reps in the next session (Jukic2024); velocity-loss-to-%reps models had poor predictive ability
  for free-weight squat (Jukic2023; Pérez-Castilla 2024, SECONDARY); general equations failed across subjects
  (GarciaRamos2018). [I, moderate] Expect TENSR to need a per-user, per-exercise calibration set; test both a
  population model and a model with *k* calibration sets (k = 1, 2, 3) and report the learning curve.
- **Leakage checklist:** normalisation constants (MVC, baseline MDF) computed only from training data or from the
  test subject's *own* pre-set data available in real use; feature selection, filter tuning, epoch length and
  thresholds chosen inside the training folds only; no use of the set's total rep count (unknown in real time) in
  features; the 20–30-set pilot data cannot be reused as the test set for the thresholds it inspired.
- **Simpler baselines must be beaten** (PROTOCOL §5 checks): (a) rep count alone with population average RTF at that
  %1RM; (b) IMU-only rep-duration slowdown (a velocity-loss proxy from the puck); (c) the user's own self-reported
  RIR. If EMG adds nothing over (b), the EMG claim falls.

### 4.3 Metrics

- **Continuous RIR:** MAE in reps (with participant-clustered bootstrap CI), bias, proportion within ±1 rep, by true-
  RIR bin (accuracy near failure matters more than at RIR 8). **Calibration plot** (predicted vs observed RIR) with
  calibration slope and intercept (VanCalster2019: poor calibration can make a model less useful than a
  better-calibrated one with lower discrimination). [RESEARCH-ESTABLISHED]
- **Decision thresholds** ("stop now", "≤ 2 left"): sensitivity, specificity, PPV/NPV at the operating threshold,
  each with a 95% CI accounting for clustering; ROC AUC only as a secondary summary. Accuracy alone is not reported
  without class balance.
- **Set score ("did this set reach failure")**: same, but sets ended for non-failure reasons excluded.
- **Drop-set test** from the brief: pre-specify the expected shape (monotonic fatigue index across drops, no reset at
  load change) and test it against MVC drop and velocity loss as references, not by eye.
- Sample-size for model development and external validation should follow Riley's criteria (Riley2020; Riley2024),
  which explicitly reject rules of thumb and show n = 100 gives unstable calibration estimates.

**Acceptance criteria.**
- Subject-wise validation, calibration reporting — RESEARCH-ESTABLISHED (Saeb2017; VanCalster2019; Riley2024).
- **ENGINEERING TARGET**: LOSO MAE ≤ 1.0 rep for true RIR 0–3, upper 95% CI ≤ 1.5, and **better than the user's own
  self-report** (the population average self-report error is ~1 rep, Halperin2022 — a device no better than asking
  the lifter has no RIR claim). Calibration slope 0.8–1.2.
- **ENGINEERING TARGET**: "≤ 1 RIR" flag sensitivity ≥ 0.80 with lower CI ≥ 0.70, specificity ≥ 0.80.
- **ENGINEERING TARGET**: EMG model improves on IMU-only baseline by ≥ 0.3 reps MAE with CI excluding zero.

---

## 5. Stage 5 — Does feedback improve decisions or outcomes?

**Why it is a separate question.** A valid measurement does not imply benefit. Velocity-based training is the
nearest precedent and is instructive:
- *Acute performance:* visual velocity feedback raised mean concentric velocity in a 10-rep back squat set vs no
  feedback in 15 adolescent athletes (Weakley2019a); verbal kinematic, visual kinematic and verbal encouragement all
  improved bar velocity in 12 rugby players with trivial differences between them (Weakley2020); a 2023 meta-analysis
  of 20 studies found feedback improved velocity by ~8.4% (g ≈ 0.63), visual > verbal (Weakley2023, ABSTRACT).
  Jiménez-Alonso et al. 2022 (JSCR 36(6):1511–17) studied augmented feedback in strength- vs power-oriented sessions;
  the abstract could not be retrieved — **its result is UNVERIFIED here**; the 2023 review reports the authors
  suggested verbal velocity feedback may matter more in strength-oriented than ballistic training (SECONDARY).
- *Training adaptations:* a 4-week trial in 28 semi-professional rugby players found "possibly to likely" greater
  improvements in sprint, CMJ and 3RM squat with feedback (Weakley2019b) — small n, magnitude-based inference.
  Orange et al. 2022 pooled 4 RCTs (88 participants) of VBT vs traditional training and found trivial differences
  with wide CIs (strength SMD 0.06, 95% CI −0.51 to 0.63), low-to-very-low certainty (Orange2022).
  [I, limited for any long-term outcome benefit of feedback]

So: feedback reliably changes *acute* effort; there is no established long-term outcome benefit of velocity
feedback, let alone EMG-based feedback. TENSR's Stage 5 claim is [H].

**Designs.**
1. *Acute decision-quality crossover* (cheapest, do first): within-participant, randomised order, sessions ≥ 72 h
   apart: (a) TENSR live RIR feedback vs (b) self-report RIR vs (c) TENSR worn but blinded. Target: stop sets at
   RIR 2. Primary outcome: absolute error between intended and *actual* RIR at stop (each set continued to failure
   after the stop decision, or failure confirmed in a subsequent set at the same load). Secondary: set-to-set
   consistency, total volume, session RPE.
2. *Parallel-group RCT* (8–12 weeks): TENSR feedback vs same programme with self-reported RIR, both arms wearing the
   device (blinded logging in control to equalise novelty and data capture). Primary outcome chosen in advance from
   one of: ultrasound muscle thickness of the instrumented muscle (sonographer blinded to group, fixed sites marked,
   duplicate images); 1RM or isokinetic peak torque (tester blinded). Secondary: adherence (sessions completed,
   device wear time), adverse events, perceived usefulness (validated usability scale), training volume.
   Analyse by ANCOVA on post with baseline covariate, ITT.
3. *N-of-1 / crossover by block* is not suitable for hypertrophy (carry-over), only for acute decision outcomes.

**Blinding limits.** Participants cannot be blinded to receiving feedback; use outcome-assessor blinding, a
"device worn, display off" control, and expectation questionnaires. Pre-register; report per CONSORT.

**Minimal important differences.** No established MID exists for muscle thickness or 1RM in trained populations
that A5 could verify. Use the instrument's SDC (Stage 2-style reliability of the ultrasound measure in the
researchers' own hands) as a floor, and justify a *smallest effect worth detecting* against the Orange2022 estimate
— note its CI includes both zero and moderate effects. **ENGINEERING TARGET (proposed)**: a Stage 5 benefit claim
requires the 95% CI of the between-group difference to exclude zero *and* the point estimate to exceed the outcome's
SDC; otherwise market only measurement features.

**Confounders.** Novelty/Hawthorne effects, coach attention, differential adherence, programme differences that
the feedback causes (more volume in one arm — decide in advance whether volume is an outcome or must be matched),
diet/protein, sleep, baseline training status.

---

## 6. Sample size — precision-based planning with worked examples

Principle: plan for the **width of the confidence interval of the quantity the claim is about**, not for a p-value,
and not for a generic "n = 30". All three examples below are conditional on stated assumptions; change an assumption
and the n changes. **No universal adequate n is implied.** The unit of sample size is the *participant*; reps and
sets within a participant are not independent and add less information than their count suggests.

### Example 1 — Claim: "TENSR's per-rep MDF agrees with a lab sEMG system within ±10 Hz" (Stage 3)

Assumptions: SD of between-system differences s = 5 Hz (to be replaced with the pilot value); bias ≈ 0; one
summary difference per participant per condition (mean over reps) so the classic formula applies.
Approximate SE of each 95% LoA ≈ √(3/n)·s (Bland & Altman 1986/1999, BlandAltman1999).
95% CI half-width of each LoA ≈ t(0.975, n−1) · √(3/n) · s:

| n participants | LoA = ±9.8 Hz, CI half-width |
|---|---|
| 15 | ±4.8 Hz |
| 30 | ±3.2 Hz |
| 60 | ±2.2 Hz |
| 100 | ±1.7 Hz |

With s = 5 Hz, the LoA (±9.8 Hz) sits right at the ±10 Hz margin, so *no* n proves agreement — the upper CI will
always exceed 10 Hz. That is the useful output of the calculation: the claim is only testable if s is
substantially below 5 Hz. Lu et al. (Lu2016) give a power-based method for the n needed so that the LoA CI falls
inside a predefined clinical margin with stated α and β, implemented in MedCalc and the R package blandPower — use
it once the pilot gives s and the bias. With repeated reps per person, use the repeated-measures LoA, which widens
the interval.

### Example 2 — Claim: "MDF test–retest reliability is good" (Stage 2)

Bonett (Bonett2002): n ≈ 8z²(1−ρ)²[1+(k−1)ρ]² / [k(k−1)w²] + 1, with planning ICC ρ, k sessions, target CI width w.
Check: reproduces Bonett's example (k = 4, ρ = 0.85, w = 0.2 → 19.2).

| planning ICC | sessions k | CI width w | n |
|---|---|---|---|
| 0.85 | 2 | 0.20 (≈0.75–0.95) | 31 |
| 0.85 | 3 | 0.20 | 22 |
| 0.85 | 2 | 0.15 | 54 |
| 0.75 | 2 | 0.20 | 75 |
| 0.90 | 2 | 0.10 | 57 |

Bonett's formula targets the *expected* width; Zou (Zou2012) adds **assurance** (probability that the achieved width
is no wider than the target), which increases n — use the ICC.Sample.Size R package. Note the circularity: a planning
ICC is needed to plan; take it from the Stage 2 pilot, not from literature on gel electrodes. Because the CI on ICC
depends on between-subject spread, recruit a heterogeneous sample deliberately, and report SEM (Example 2b).

**2b. SEM / MDC precision.** With n participants and 2 sessions, SEM is estimated with ≈ n degrees of freedom. The
95% CI for an SD from χ² gives SEM bounds of ×0.74–1.55 at n = 15, ×0.80–1.34 at n = 30, ×0.85–1.22 at n = 60.
MDC inherits the same ratio. If the claim is "MDC95 < 15 Hz" and the point estimate is 11 Hz, n = 15 gives an upper
bound of ~17 Hz (claim not supported), n = 30 gives ~14.7 Hz (just supported).

### Example 3 — Claim: "TENSR flags ≤ 1 RIR with sensitivity ≥ 0.80" (Stage 4)

Assumptions: true sensitivity 0.85; required 95% CI half-width 0.07 (so the lower bound clears ~0.78). Independent
positives needed ≈ z²p(1−p)/d² = 100 positive (≤ 1 RIR) rep-states. But positives are clustered within
participants: with m = 5 positive sets per person and an intra-participant correlation of 0.2, the design effect is
1 + (m−1)·0.2 = 1.8 → ~180 positive sets ≈ 36 participants, before allowing for drop-out and for the LOSO
procedure (which estimates the performance of the *development process*, not a frozen model; a frozen model then
needs a fresh external validation set per Riley2024). Specificity needs its own count of negatives.

### Illustration — Stage 5 RCT scale

For a standardised difference of 0.3 (larger than Orange2022's pooled 0.06), 80% power, α = 0.05: ~175 per group with
a post-only comparison; ANCOVA with a baseline–post correlation of 0.8 reduces it by (1 − 0.8²) to ~63 per group.
This is shown to make the scale of an outcome trial visible, not as a recommended n.

---

## 7. Ethics and safety for human testing (Australia)

- **HREC review.** Human research in Australia is reviewed under the NHMRC *National Statement on Ethical Conduct in
  Human Research 2023* (in effect from 1 January 2024; NHMRC pages indicate a 2025 edition with a delayed/changed
  effective date — **check which edition applies on the application date**) (NS2023). The 2023 revision replaced the
  three-tier risk scheme with *lower risk* vs *higher risk*; research carrying risk of harm beyond discomfort is
  higher risk and requires full HREC review. Training to momentary failure, MVC testing and a novel electrical
  device on skin plausibly put Stages 2–5 in the **higher-risk** category; Stage 1 (bench) needs none. A company
  without its own HREC can use a university partner or a registered independent HREC.
- **Informed consent.** Plain-language statement covering: the device is an unvalidated prototype; failure training
  risks (DOMS, acute muscle strain, rare exertional rhabdomyolysis — especially in untrained participants with high
  eccentric volume); skin reactions; that data are body data; right to withdraw without penalty; what happens to data.
- **Screening and exercise safety.** Pre-exercise screening (e.g. the Australian adult pre-exercise screening system);
  exclusion of uncontrolled cardiovascular, recent musculoskeletal injury, pregnancy for maximal testing, implanted
  electronic devices (pacemakers — the RLD drives current into the body); spotter and safety bars for every
  failure set; first-aid-trained staff; graded familiarisation before 1RM and failure sets; stop rules.
- **Skin.** Dry stainless-steel studs pressed by an elastic band for long sessions: risk of contact dermatitis (nickel
  release from some stainless grades), pressure marks and maceration with sweat. Record electrode material and grade;
  inspect and photograph skin before/after; exclude known nickel allergy or provide a patch test; grade reactions on a
  pre-defined scale. Consider ISO 10993-5/-10 biocompatibility evidence for skin-contact materials (standard not
  opened here — UNVERIFIED as to scope details).
- **Electrical safety.** A battery-only device worn on skin is not legally required to meet IEC 60601-1 if it is not a
  medical device, but its patient-leakage and auxiliary-current concepts are the right engineering yardstick for an
  RLD circuit that injects current through the reference electrode. Verify on the bench: DC and AC current through
  each electrode under normal and single-fault conditions (shorted RLD output, failed series resistor); ensure the
  device **cannot be worn while USB-charging from a mains adapter** during trials (BRING-UP already notes USB ground as
  a noise path); LiPo safety (protection, no charging on body, damaged-cell handling). **ENGINEERING TARGET**: apply
  IEC 60601-1 body-floating (BF) patient-auxiliary-current limits as internal acceptance limits, measured, before
  first human contact.
- **Data privacy.** EMG, IMU, body measurements and training logs are health-adjacent personal information under the
  Privacy Act 1988 (Cth) and the APPs; collect the minimum, de-identify at source with a key held separately, store
  in Australia or document cross-border disclosure, set retention periods, and keep research data separate from any
  commercial dataset unless consent explicitly covers reuse for model training.
- **Adverse events.** Pre-defined AE categories (skin, musculoskeletal, cardiovascular, device malfunction/heat),
  severity grading, causality judgement, reporting timelines to the HREC, and a stopping rule. Report AEs in every
  publication, including zero counts.
- **TGA boundary.** The TGA's general health and wellness exclusion (in force since 25 Feb 2021) covers consumer
  products that non-invasively monitor a physical parameter for general health or wellness; **every function must
  qualify** — one function framed as detecting injury, diagnosing, or rehabilitating takes the product outside the
  exclusion (TGA2021). Study documents, recruitment material and outcome names must use training/performance
  language (fatigue, effort, reps) and avoid injury-prevention, rehabilitation or diagnostic claims — consistent with
  CLAUDE.md. A research protocol that recruits patients or measures rehabilitation outcomes would itself pull the
  device toward medical-device territory and should not be run under the product's name.
- **Conflict of interest.** Kye owns the product; validation analysed by the developer is at high risk of bias.
  Pre-register (OSF), share analysis code, and have Stage 4 test-set analysis run by someone not involved in model
  development; publish negative results.

---

## 8. Summary of the programme

| stage | question | gate to proceed | criterion type |
|---|---|---|---|
| 1 Bench | does the pipeline return known MDF/amplitude/reps from known signals? | S1.1–S1.10 pass on ≥ 4 of 5 boards | ENGINEERING TARGETS |
| 2 Repeatability | how much does a reading move when nothing changes, incl. doff/don? | MDC95 < ½ claimed fatigue shift; ICC CI reported | ICC form RESEARCH-ESTABLISHED; thresholds ENGINEERING |
| 3 Agreement | does it match lab sEMG and kinematic references on real lifts? | LoA/TOST within margin per muscle; no worse than two reference pairs | method RESEARCH-ESTABLISHED; margins ENGINEERING |
| 4 Prediction | does it predict actual RIR / failure in new people, sessions, exercises? | LOSO MAE ≤ 1 rep, better than self-report and IMU-only baselines; calibrated | method RESEARCH-ESTABLISHED; thresholds ENGINEERING |
| 5 Benefit | does feedback improve decisions or outcomes? | acute crossover first; outcome RCT only if acute benefit is shown | ENGINEERING; precedent [I, limited] |

**Direct answers for the coordinator.**
- RQ5: the brief's 20–30-set test is a Stage 4 pilot at one easy threshold; it cannot validate RIR, it has no
  ground truth for the "3 short" sets unless they are continued to failure, and it is at high risk of leakage and
  self-evaluation bias. [H; methodological principles strong]
- The single biggest methodological risk for a band product is **doff/don repeatability** of MDF and amplitude; it
  is untested for dry 7 mm studs at 25.4 mm and the gel-electrode literature already shows reapplication degrades
  between-day reliability. [I, limited]
- The velocity-feedback precedent supports acute effort changes but **not** long-term outcome superiority
  (Orange2022, low certainty). Any TENSR claim of better training outcomes is [H] with no supporting evidence. [I, limited]
- The 500 SPS vs 20–450 Hz inconsistency must be resolved in Stage 1 because MDF agreement with a 2 kHz reference
  depends on it.
