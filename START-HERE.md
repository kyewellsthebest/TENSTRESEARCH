# START HERE — what the research found

2026-11-02. A plain-English summary for Kye. The evidence and argument are in `TENSR-SCIENCE-REPORT.md`.

**How this was done.**
- Six research agents covered training science, EMG and fatigue, sensing and signal processing, product
  translation, validation design, and an independent audit.
- The protocol was saved before any searching.
- The auditor re-checked the load-bearing citations and the reasoning. The other agents answered it, and the open
  disagreements are kept, not smoothed over.
- **No firmware, hardware or product claim was changed.**

**One caveat on everything.** This environment could not open full papers. Only search summaries of abstracts and
records were reachable. No citation was found to be fabricated, but nothing was read in full. Re-check the key
studies with full-text access before anything goes on a website or in a pitch.

---

## The short version

**1. No "optimal" anything exists.**
- No study supports an optimal fatigue level, time under tension, contraction score or universal reps-in-reserve
  target.
- Every dose-response in the training literature is a shallow curve with wide uncertainty.
- A score against an optimum would be a number we invented.

**2. More EMG does not mean more growth.**
- The one direct test found more glute EMG in hip thrusts than squats, but no more glute growth (MRI).
- Heavy loads give more EMG than light loads, yet similar growth.
- Activation %, stimulus scores and "set effectiveness" are not just unproven — the evidence points against them.

**3. More fatigue does not mean more growth either.**
- Cluster sets, supersets, drop sets and failure vs 1–2 reps short all change fatigue without changing growth.
- Fatigue is a by-product, not a target.

**4. The spectral fatigue signal is real, but narrower than the brief says.**
- **Holds up:** the median frequency does fall during a hard set, typically by 20–30% *relative*. That is a peripheral
  muscle-fatigue marker.
- **Doesn't hold up:**
  - it isn't a "120 → 90 Hz" absolute scale;
  - tempo-independence is not established;
  - its value at failure depends on the load;
  - it is too noisy per rep to drive a live "2 left" cue (the trend only becomes visible around rep 8 of 10).
- **What's left:** it can describe a set **after** it ends, within one person, exercise and load.

**5. The hardware has three issues to settle before any fatigue claim.**
- **Data rate.**
  - At the planned 500 SPS, the ADS1292R's own digital filter is already 3 dB down at 131 Hz, and nothing above
    250 Hz exists.
  - The fatigue signal comes out biased low: a true 25% drop reads about 16%.
  - **Run at 2 kSPS.** Verified against the datasheet; the design review only checked the analogue filter.
- **Electrode orientation.**
  - The E1–E3 pair runs along the board's long axis.
  - Nothing records how the puck sits on the band. If that axis wraps around the limb, the electrodes sit across the
    muscle fibres.
- **One fixed geometry for seven muscles.**
  - 25.4 mm spacing, against 20 mm in the SENIAM standard.
  - Dry electrodes, with no study validating spectral fatigue on dry wearables.

**6. Reps-in-reserve from EMG has never been validated in real lifting.**
- The bar to beat is the lifter's own guess, which is off by about 1 rep on average with large spread.
- Even the best bar-velocity models only get under 2 reps.

**7. Your 20–30-set validation test is a pilot, not proof.**
- Failure sets have more reps by construction, so rep count alone separates the groups.
- One person's sets say nothing about other users.
- The drop-set "must not reset" test would pass or fail for reasons unrelated to fatigue.

---

## Answers to the six questions

**1. What can the band realistically measure?**
- One muscle region's electrical activity, and one limb segment's motion.
- From those: reps, sets, set duration, rest time, and weekly sets for that muscle.

**2. What can it estimate only after validation?**
- A post-set fatigue trend (spectral, one person, one exercise and load).
- Eccentric/concentric timing and range-of-motion shrinkage, on lifts where the band's segment moves.
- Possibly a within-set amplitude trend.

**3. Can we justify optimal fatigue, time-under-tension or contraction targets?**
- **No.** Use descriptions and labelled defaults instead.
- Defaults the evidence supports:
  - rest ≥ 90 s, or 2–3 min for heavy compound lifts;
  - a 0–3 reps-in-reserve effort range judged by the lifter, closer to failure with light loads.

**4. Strongest three features (useful and defensible)**
1. Automatic rep and set counting with set duration.
2. Weekly set count for the muscle wearing the band, with user-tagged effort.
3. Elapsed-time rest timer with evidence-based defaults.

Fourth candidate, and the only one that needs the EMG: the post-set fatigue trend. It has to prove it beats an
IMU-only model.

**5. Claims to avoid**
- Optimal fatigue or TUT, contraction rating, any percentage score, activation %.
- Hypertrophy, stimulus or set-effectiveness scores.
- Live "about 2 left".
- "Your muscle has recovered" or "ready".
- "Did you reach failure" as a score.
- 120 → 90 Hz, "tempo-independent", "beats velocity-based training".
- "Time under tension" (say set duration).
- Left/right imbalance from one band.
- "Logs your whole split".
- Anything about injury, rehab or health readiness (TGA).

**6. The experiments that matter most, in order**
1. A bench test of 500 SPS vs 2 kSPS with synthetic EMG of known frequency, plus signal-quality fault injection and
   an electrical-safety check.
2. TENSR beside a lab gel EMG pair in real lifts, testing both electrode orientations, per muscle.
3. Take the band off and put it back: does the same set give the same fatigue slope?
4. A reps-to-failure study, with every set taken to true failure and tested on people the model never saw, that must
   beat both the lifter's own bias-corrected guess and an IMU-only model.
5. Only then: does live feedback make people stop where they intended, without over-reaching?

---

## Feature verdicts at a glance

| Build now | After real validation | Research only | Don't build |
|---|---|---|---|
| Rep and set counting | Post-set fatigue trend | Live reps-in-reserve | Activation % |
| Set duration | Eccentric/concentric timing (some lifts) | "Reached failure" score | Contraction-quality score |
| Rest timer (elapsed) | | Recovery-driven rest timer | Hypertrophy / stimulus score |
| Weekly set count | | Amplitude trend (internal) | "Time under tension" |
| | | Left/right (needs two bands) | |

## Decisions only you can make

- The data rate (2 kSPS recommended).
- How the puck sits on the band.
- Dry vs gel electrodes for validation.
- Which muscles to name at launch.

Details: `OPEN-QUESTIONS.md`.

## The files

| File | What it is |
|---|---|
| `TENSR-SCIENCE-REPORT.md` | The full synthesis: measurement table, all target questions, training topics, sEMG, ML, final answers |
| `TENSR-FEATURE-EVIDENCE-MATRIX.csv` | 15 features × benefit, measurement, evidence, hardware fit, calibration, limits, validation, recommendation, audit status |
| `STUDY-EVIDENCE-TABLE.csv` | 169 studies with design, n, results, limits, access level and audit verdict |
| `CLAIM-VERIFICATION.md` | The brief's claims one by one, citation corrections, unresolved disagreements |
| `TENSR-VALIDATION-PLAN.md` | Five-stage programme with labelled acceptance criteria, sample-size examples, ethics |
| `SEARCH-LOG.md` | Every search, plus the access limits |
| `OPEN-QUESTIONS.md` | What is still unresolved, unverified or unsearched |
| `PROTOCOL.md` | The dated protocol and its change log |
| `agent-notes/` | Each agent's full findings, studies, searches, scripts, and responses to the audit |
