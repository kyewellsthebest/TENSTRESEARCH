# A5 — Response to the A6 audit

Agent A5, 2026-11-02. Responds to C1, C11, C12, C17, C18 and §3 of `A6-audit.md`. `A5-findings.md` is unchanged and
stays as the record. Where a criterion below differs from it, this file supersedes it. Labels: **ENGINEERING TARGET
(proposed)** / **RESEARCH-ESTABLISHED**.

The 9.3 Hz (0.5 s) and 4.7 Hz (2 s) estimator floors are A3/A6 simulation outputs. I checked the arithmetic but did
not re-run the simulation.

---

## C1 — Halperin's 0.95 reps is a bias, not an error — **ACCEPT**

I wrote "average self-report error ~1 rep" and gated an MAE against it. That compares an MAE with a mean signed
bias. With a between-participant SD of about 1.45 reps, raw self-report MAE is likely above 1 rep. A constant bias is
also cheaply correctable: a device that only beats *uncorrected* self-report could lose to "add one to your guess".

I also accept the omitted benchmark: individualised bar-velocity models reach a mean error under 2 reps in the next
session (Jukic 2024, n = 46 per A6). That is the best objective precedent.

**Revised Stage 4 criteria**
- **R4.1 — ENGINEERING TARGET (primary gate).**
  - Self-report is collected in the same sessions, at the same rep, before the set is continued to failure.
  - The comparator is **bias-corrected** self-report, with each person's bias estimated only from their own *earlier*
    sessions.
  - Gate: the paired difference in MAE (TENSR minus bias-corrected self-report) under leave-one-subject-out
    validation has an upper 95% CI below 0. The CI is bootstrapped by participant.
  - Beating only raw self-report does not pass.
- **R4.2 — ENGINEERING TARGET.** TENSR beats an IMU-only baseline (rep-duration slowdown plus rep count) by at least
  0.3 reps of MAE, with the CI excluding 0. Unchanged.
- **R4.3 — reported, not a gate.** Absolute MAE for true RIR 0–3, set against the Jukic 2024 "<2 reps" benchmark
  (RESEARCH-ESTABLISHED as a benchmark, evidence code I). My original "≤ 1.0 rep" is demoted to an aspiration.
- **R4.4 — ENGINEERING TARGET.** R4.1 must hold within RIR 0–3 on its own. Humans are most accurate near failure, so
  winning on average at RIR 6–10 does not count.

## C11 — MDF targets infeasible — **ACCEPT** targets; **PARTLY** the fix

- **S1.3 "SD < 3 Hz" — ACCEPT.** A target the ideal estimator fails tests nothing about the board. My error in
  specifying the target.
- **Per-rep LoA ±10 Hz — ACCEPT.** The estimator floor between two electrode pairs is about ±20–26 Hz. My Example 1
  used s = 5 Hz on participant means while the criterion was per rep. That mismatch is mine; the example stands only
  for a means-based claim.
- **"Two-reference-pair floor as the *only* criterion" — PARTLY.** The floor is the right primary benchmark. Alone,
  though, it passes any device wherever two adjacent gel pairs themselves disagree badly, for example across an
  innervation zone. I keep an absolute usefulness ceiling tied to the effect size.
- **"MDC is the wrong noise term" — PARTLY.** Accepted for within-set claims, where slope precision is the right
  term (C7). MDC on absolute MDF still gates any between-session or week-to-week claim.
- **Bonett is a floor for ICC(A,1) — ACCEPT.** Size the n by simulation, or by Zou 2012 with assurance.
- **One participant's 30 sets — ACCEPT.** They say nothing about other users.

**Revised criteria (all ENGINEERING TARGET)**
- **S1.3.**
  - Bias under 2 Hz at each epoch length (0.25 / 0.5 / 1 / 2 s).
  - SD within 10% of the simulated ideal-estimator SD for the same spectrum and epoch.
  - Over a ≥ 10-rep synthetic 120→90 Hz decline, the regression slope is recovered with under 10% error.
  - Run at 500 SPS and at 2 kSPS; this comparison decides the sampling rate.
- **S2-a (between-session absolute MDF).** As before: lower 95% CI of ICC(A,1) ≥ 0.75, MDC95 reported. It gates
  between-session claims only.
- **S2-b (new).** Same load and rep count, band re-applied between sessions. The between-session SD of per-set MDF
  slope must be under half the mean slope at that load.
- **S3.**
  - Gated outcomes: per-set slope, and the mean of reps 1–3 vs the last 3.
  - (a) The TENSR-vs-reference LoA is no wider than 1.25 × the LoA between two adjacent gel pairs.
  - (b) The half-width of the slope LoA is below the mean group slope at that load.
  - Per-rep LoA is reported only, with no gate.
  - Both pair orientations relative to the fibres are tested before any muscle is claimed (C14).

## C12 — Feedback evidence — **ACCEPT** (Orange), **PARTLY** (pessimism)

- **Orange 2022 — ACCEPT, misapplied.** It compares VBT prescription with %1RM prescription, not feedback with none.
  It is retired as a feedback precedent. My RCT-size illustration survives only as arithmetic.
- **Weakley 2023 — ACCEPT that I omitted it.** The authors concluded feedback improved acute output *and* chronic
  adaptations. That will be reported.
- **"No established long-term benefit" — PARTLY, disagreement preserved.**
  - We agree on the facts: low certainty, few chronic studies, and the main one (Weakley 2019b, n = 28) used
    magnitude-based inference.
  - I still read that as "not established".
  - Either way, none of it transfers to EMG-derived feedback (code H).
- **The risk is the sign of the effect — ACCEPT.** A biased "2 left" cue will push users past their intended stop.
  - **S5.1 — ENGINEERING TARGET (acute crossover gate).**
    - Mean signed error between achieved and intended RIR is within ±0.5 rep (95% CI).
    - The share of sets ending at least one rep nearer failure than intended is non-inferior to bias-corrected
      self-report, with a 10-percentage-point margin.
  - **S5.2 — ENGINEERING TARGET.** Fatigue cost is recorded per arm: velocity loss where measured, next-set reps at the
    same load, and 24/48 h soreness. Extra volume bought at disproportionate fatigue is not a benefit.
  - The outcome RCT runs only after S5.1 passes and live RIR has passed Stage 4.

## C17 — Within-set MDF trend only as a post-set descriptive — **ACCEPT**, one reservation

- I accept the conditions: multi-rep regression, phase-locked concentric windows, ≥ 1–2 kSPS, and one person,
  exercise and load.
- I accept C7: at about 9 Hz per-rep SD, t ≈ 2 arrives near rep 8 of 10. **Live** MDF output therefore has no
  validation target, and cross-load MDF comparisons are excluded from every gate.
- **Reservation (PARTLY).** Stage 4 keeps a pre-registered *research* test of whether rep-level MDF features add to an
  IMU-plus-rep-count model under leave-one-subject-out validation. The prior is low, but a documented null is the
  cleanest way to retire the brief's central claim. It is not a product gate.

## C18 — The brief's test separates by construction — **ACCEPT**

**S4.matched — ENGINEERING TARGET (design rule).**
- Features come only from reps 1…k, where k is the shorter set's stop rep, at matched load.
- Predictions use only data available before the stop decision.
- Rep count and duration at rep k are mandatory baselines.
- The brief's test passes only if TENSR beats them under leave-one-subject-out validation, across multiple
  participants.

## §3 — Feature tiers — **ACCEPT** as they bear on validation

- **Live RIR is research-only in v1.** Stage 5's RIR arms are research protocols under HREC until R4.1 passes.
- **Set score is research-only.** I defer to A1/A6 on the outcome evidence. Failure classification stays in Stage 4
  only as a labelling check.
- **MDF trend is post-set, gated by a signal-quality index, and dropped if it fails R4.2.**
- The rep-count thresholds (2% of reps; 1 false rep per 50) match mine.

---

## Disagreements preserved

| # | A6 | A5 |
|---|---|---|
| P1 | The two-reference-pair floor is the **only** Stage 3 criterion | The floor is primary; keep an absolute usefulness ceiling (S3 b) |
| P2 | A5 is "slightly too pessimistic" on chronic feedback benefit | Low certainty from few trials that used magnitude-based inference is "not established"; report the authors' conclusion, do not adopt it |
| P3 | No live use of MDF is defensible | Agree for the product; still run a pre-registered research test against IMU baselines |
