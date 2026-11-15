# X4 — Effort / proximity-to-failure: product and algorithm design spec

Agent X4 (product/algorithm design), 2026-11-03. **Design document only.** No firmware or hardware file was edited.
Inputs read: `BRIEF.md`; `CLAUDE.md` (hardware, firmware); `TENSR-SCIENCE-REPORT.md` §1, §5;
`TENSR-VALIDATION-PLAN.md` §4–5; `top5/F6-findings.md`; `top5/FA-audit.md`; the relevant rows of
`STUDY-EVIDENCE-TABLE.csv`. 22 WebSearches (`X4-searchlog.md`); studies in `X4-studies.csv` (37 rows).
**Access:** every web source was seen through search-engine summaries of abstracts or repository records. No full
text was read. WebFetch was not attempted; earlier rounds found it blocked. A number that came from one summary only
is marked UNVERIFIED.

**Evidence codes:** **D** direct (comparable hardware, dynamic lifting) · **I** indirect human · **M** mechanistic or
arithmetic · **H** product hypothesis. Nothing has run on a TENSR board, because none has been built. **Every
TENSR-specific performance statement is H.**

## Summary (10 lines)

1. **The product is a per-set effort readout: estimated RIR at set end as a range, plus a "hard set" flag.** Light
   loads need a tighter band (I: Lasevicius 2022, untrained). The live cue is secondary and gated. **Failure itself is
   not rewarded.**
2. **The estimator is a per-person, per-exercise Bayesian model of reps-to-failure (N).** The prior comes from the
   lifter's own load→reps history (I: Mitter 2023, multilevel R² 0.97–0.98 vs pooled 0.89–0.93). Within the set it
   is updated by slowdown features. RIR = N − reps done, and it is shown as an 80% interval, never a point.
3. **The strongest within-set features on the current board are timing features, not spectral ones.** Concentric
   duration grows: bar-lift time more than doubled from the first to the last bench rep (I: Duffey & Challis).
   Concentric duration also beat mean velocity in one preliminary study (adj R² 0.37 vs 0.14; I: Achermann 2024).
   EMG RMS/MDF are secondary, gated by quality, and must earn their place against an IMU-only baseline.
4. **ROM collapse is not a reliable failure marker in skilled lifters** (I: Brice, squat ROM unchanged to volition).
   Neither is a fixed "minimal velocity": last-rep velocity CV is >18% with ICC <0.60 (I: PeerJ 2020, n=96).
   **Stall detection** should therefore key on a failed concentric: motion stops and reverses before the rep's top.
5. **Static-segment exercises (curls with an upper-arm puck, pushdowns, leg extension, chest) leave the puck IMU nearly
   blind.** The fallback is EMG burst duration and envelope shape, with lower confidence. This is the main reason the
   **bar-clip second puck** is the upgrade path (I: individual velocity models <2 reps, squat only).
6. **The bar to beat is high.** Lifters underpredict by ~0.95 reps with between-person SD ~1.45 (Halperin 2022).
   Trained bench pressers may already be near 0.65 ± 0.78 reps intraset (Refalo 2024 JSCR, UNVERIFIED number).
   Reps-to-failure at a fixed load varies 0.7–1.1 reps (SEM) day to day (Mitter 2022). A history-only prior is
   therefore already a strong baseline.
7. **Fusion beats the lifter only if the sensor's error is comparable and not strongly correlated with theirs.** With
   bias-corrected self-report SD 1.0, sensor SD 1.5 and ρ 0.5, fusion gives SD 0.98: **no gain** (M). The sensor's
   realistic edge is where humans are worst: high-rep, light-load and isolation sets (I: Halperin; Murdoch 2020).
8. **Calibration needs no forced failure sessions.**
   - Use the lifter's own failure sets, which the stall detector confirms automatically.
   - Treat every non-failure set as **right-censored** (N ≥ reps done).
   - Take RIR tags as noisy observations.
   - Add an optional "button at 2-left, then continue" check set to learn each person's bias.
9. **Validation is staged:** bench → feasibility pilot → lab two-visit LOSO → gym field → decision-quality crossover.
   It has mandatory baselines: rep count with individual history, IMU-only, bias-corrected self-report, and an LPT
   individual model where one applies. Every acceptance number is an **ENGINEERING TARGET**.
10. **No respin is needed.** Per-rep features cost under 1 ms of ESP32-S3 CPU (a 1024-point FFT ≈ 98k cycles ≈ 0.4 ms
    at 240 MHz). Rep-end→haptic latency of ~0.2–0.4 s is achievable. BLE carries ~40-byte per-rep records; raw
    streaming (~11 kB/s) is for validation builds only.

---

## 0. Design stance — what "effort tracking" should mean for TENSR

**Kye's framing is adopted: proximity to failure is the core feature.** Two corrections from the evidence shape *how*
it is presented.

- **Effort is a threshold, not a score to maximise.** Failure vs 1–3 RIR adds little for trained lifters (Refalo
  2023/2024; Grgic 2022; FA-audit §3). Robinson 2024 shows hypertrophy improving closer to failure, so "closer is
  better" holds up to a point, but the marginal gain inside 0–3 RIR is small. **The readout must not turn into a
  "you reached failure!" reward loop** [I, moderate].
- **Load moderates it.** Failure mattered at 30% 1RM and not at 80% (Lasevicius 2022, untrained, knee extension)
  [I, limited]. So the target band shifts closer on light, high-rep sets. Light, high-rep sets are also where lifters
  guess worst: accuracy is better with heavier loads, fewer reps and closer to failure (Halperin 2022). In 21 trained
  men, 2-RIR estimates were most accurate at 85%, then 75%, then 65% 1RM (Murdoch 2020) [I, moderate]. **This is the
  niche where a sensor can most plausibly add value** [H].
- **FA-audit D1 still stands.** Effort is the *gate* on the unit of volume. The product's job is to make the
  **hard-set count** honest, not to make each set as hard as possible.

---

## 1. Outputs

### 1a. Per-set effort readout (primary)

**Shown after every set.**

| field | definition | display |
|---|---|---|
| `rir_est` | posterior median of RIR at the last completed rep | "~2 in reserve" |
| `rir_80` | 80% credible interval | "1–3" (a range is always shown; width is the honesty signal) |
| `hard_set` | P(RIR ≤ band upper) ≥ 0.7 | ✓ / ? / ✗ — "?" when the interval straddles the band |
| `band` | upper RIR counted as "hard": **3** by default; **1** when the set is high-rep or light (prior N > ~15, or load < ~60% of the lifter's e1RM for that exercise) | user-visible, user-editable |
| `basis` | which evidence dominated: history / sensor / your tag / failure observed | small text, for trust |
| `quality` | pass / degraded / withheld (SQI) | withheld → "no estimate; tag it yourself" |

- **Band thresholds are product rules [H] built on I evidence:** the 0–3 RIR consensus (Refalo 2023, Robinson 2024)
  and the light-load effect (Lasevicius 2022, untrained). The ~15-rep / ~60% cut-off is a design choice, not a
  finding.
- **Weekly roll-up:** hard sets per muscle (fractional counting per FA-audit), with the sets marked "?" shown
  separately. **"Stimulus" scores are not shown**, per the science report §2.
- **Wording rules:** "how close you got", never "how much you grew". No colour that rewards RIR 0 over RIR 2.

### 1b. Failure / stall detection (event)

**A failed rep** is a concentric attempt that did not reach the top of the range established by the set's earlier
reps, and that was followed by a descent or a rack.

**Detector, by exercise class:**

| class | primary evidence | secondary |
|---|---|---|
| Moving instrumented segment (squat/leg press/lunge thigh puck; delt raise/press upper-arm puck) | Segment angular velocity along the movement's principal axis falls to ~0 **before** the angle reaches ≥ 85% of the median top angle of reps 1–3. It then reverses, or holds for > ~1.5 s, then reverses. | EMG envelope stays high through the stall, which rules out a deliberate pause |
| Static instrumented segment (curl/biceps, pushdown/triceps, leg extension/quad, chest press/pec) | EMG burst much longer than the set's concentric median (> ~2× rep-1–3 median). The envelope plateaus, then decays without the normal inter-rep pattern. This is weaker evidence. | Small IMU signatures: belly-bulge tilt, whole-body sway (H) |
| Bar/stack clip (second puck) | Vertical velocity → 0 below the median top displacement, then reversal. This is the most direct case. An IMU bench sticking-point detector reached 2.8% detection error, with inter-subject variability the main limit (Rum 2022, Paralympic bench) [I, limited] | — |

- **Why not a "minimal velocity threshold".** Last-rep velocity in Smith bench had CV > 18.3% and ICC < 0.60
  (PeerJ 2020, n=96) [I, moderate]. Puck angular velocity is not bar velocity in any case (Banyard 2017; seven-device
  bench study; F6). The person's own minimal-velocity value is kept only as a **soft likelihood term**, never as the
  trigger.
- **Why not ROM collapse.** Skilled squatters kept joint ROM to volition while joints slowed (Brice 2019/20). Bench
  bar travel stayed nearly constant while lift time more than doubled (Duffey & Challis) [I, limited]. A shrinking ROM
  is a cue to "check form", not a failure flag.
- **Output.** `stall_prob`, timestamp and rep index. The app asks once: "Rep 9 looked like a miss — failure?
  ✓/✗". The answer becomes a label (§3). **False stalls are cheap. Missed stalls only cost labels.**

### 1c. Live cue (optional, gated)

**Purpose.** Tell the lifter when they **reach their own target band**. The cue never tells them to keep going.
"~2 left" is shown on the phone only when the interval is narrow. The haptic pulse means one thing only: **"you're
in your target zone now."**

**Why one-directional.** Feedback reliably raises acute effort (Weakley 2023: g 0.63; visual > verbal) [I,
moderate]. A cue biased toward "more left" pushes users past their intended stop: validation plan §5, the "sign of
the effect" risk. A cue that only ever says "you've arrived" cannot push a user past their intent. At worst it is
early or late.

**Conditions — all must hold [H, ENGINEERING TARGET thresholds]:**
1. The exercise has a **calibrated model**: ≥ 2 labelled anchor sets (failure observed, or a check set) for this
   person × exercise within the last ~6 weeks. **No population-only cue.**
2. The exercise is on the **validated list** from Stage C (§5). Exercise classes that failed validation never cue.
3. SQI passes on the current and previous rep: no lead-off on E1/E2/E3, no clipping, 50 Hz ratio and LF energy below
   bench thresholds (science report §5.4).
4. The posterior 80% interval width is **≤ 2 reps**, and P(RIR ≤ target) ≥ 0.7.
5. ≥ 3 reps completed, so the within-set baseline exists.
6. The user opted in for this exercise.
7. **Free-weight squat, bench and overhead press:** the cue is allowed only with the explicit "safeties set /
   spotter" toggle on. No failure-adjacent prompting is given otherwise.

**Haptic.** DRV2605L effect library: a single short "strong click" for target reached, and a double pulse for a
detected stall ("set over"). Nothing else. The motor is on the same puck as the electrodes, so EMG samples during a
haptic burst are blanked (~100 ms) to keep the motor's vibration artefact out of the features [H; measure on the
bench, S-A].

---

## 2. Signal design on the current board

### 2.1 Acquisition (firmware settings, no hardware change)

- **ADS1292R at 2 kSPS** (DR = 100, sinc3 −3 dB ≈ 524 Hz; science report §5.4).
  - CH1 only.
  - `RLDREF_INT = 1`, and respiration off (CLAUDE.md firmware requirements).
  - Lead-off detection on, feeding the SQI.
- **LSM6DSO**, accelerometer + gyro at **416 Hz**, FIFO-batched.
  - That rate is enough for kinematics, jerk and the 8–14 Hz tremor band.
  - A **research build** may run the accelerometer at 1.66–3.33 kHz for MMG (F6: the I2C budget rules out 6.67 kHz
    with gyro).
- **Common timebase.** The ADS1292R DRDY count and the IMU FIFO timestamp are both latched against the ESP32 µs timer.
  Rep-level alignment needs ~5 ms, which is easy.

### 2.2 Pre-processing (fixed before validation; applied identically to any reference)

1. EMG:
   - 20 Hz high-pass, 4th order;
   - 50 Hz (and 100/150 Hz) adaptive or IIR notch — test its MDF bias on the bench (science report §5.4);
   - ±full-scale clip detection.
2. Envelope: 50 ms moving RMS, used for burst detection only.
3. IMU: gyro bias re-estimated at every rest period (still > 2 s). Gravity direction comes from a complementary
   filter. The movement axis is the first principal component of gyro during reps 1–2.

### 2.3 Rep segmentation and phase-locking

- **Moving-segment exercises.** Rep = one cycle of the principal-axis angle.
  - The concentric phase is the monotonic segment whose sign is learned per exercise from rep 1, where the
    concentric is the higher-EMG half.
  - **Phase-locked EMG window** = the samples where the segment angle is between fixed angles θa and θb, set from
    reps 1–3 (central 60% of the ROM). The same joint-angle region every rep removes most of the angle and
    innervation-zone confound (science report §5.1).
- **Static-segment exercises.** Rep = one EMG envelope burst, with onset/offset at 15% of the set's rep-1–3 peak
  envelope.
  - **Phase-locked window** = a fixed 400 ms starting at burst onset. Equal length makes spectra comparable. Because
    no angle is available, the window is time-locked rather than angle-locked: weaker [H].
- **Fusion.** When both signals are present, IMU boundaries win and EMG confirms (artefact rejection). Rep counting
  is the most mature function here (RecoFit ±1 rep in 93% of sets, forearm IMU) [D, moderate for forearm; **H for
  upper-arm/thigh/belly placement**].

### 2.4 Per-rep features

All features are expressed **relative to the median of reps 1–3 of the same set**. Within-set normalisation sidesteps
the ~42% between-session amplitude CV of dry electrodes (Colyer 2018).

| # | feature | source | rationale | evidence | used for |
|---|---|---|---|---|---|
| F1 | **Concentric duration** ratio | IMU (moving) / EMG burst (static) | At constant ROM, duration ∝ 1/mean velocity. Bench lift time > 2× first→last rep (Duffey & Challis). Duration beat MCV in one pilot (Achermann 2024: adj R² 0.37 vs 0.14) | I, limited; M | RIR likelihood, stall |
| F2 | Peak / mean concentric angular velocity ratio | IMU (moving only) | Segment velocity-loss analogue. VL→%reps completed R² 0.93–0.97 for **bar** velocity (bench/squat; Rodríguez-Rosell 2020). Segment ≠ bar | I for bar; H for segment | RIR likelihood |
| F3 | Eccentric duration | IMU (moving) | Strongest RPE predictor in wrist-IMU curls (Thomas & Wahlström 2025, preprint, 5 participants) | I, very limited | RIR likelihood |
| F4 | Inter-rep pause at lockout | IMU + EMG | Lifters breathe and rest between reps near failure (common observation; **no study found**) | H | RIR likelihood |
| F5 | Concentric ROM ratio | IMU (moving) | Not a failure marker in skilled lifters (Brice); kept for form / partial-rep flags | I, limited | form, stall secondary |
| F6 | Normalised jerk and the angular-velocity profile (time-to-peak, sticking dip depth) | IMU (moving) | A sticking region emerges near failure (Rum 2022; Duffey & Challis path change) | I, limited | RIR likelihood, stall |
| F7 | Tremor power 8–14 Hz during concentric, relative to rep 1–3 | accel/gyro | Fatigue raises 8–12 Hz physiological tremor; reported bands vary (8–10 to 9–20 Hz); small n | I, limited | RIR likelihood (research weight) |
| F8 | EMG RMS in the phase-locked window | EMG | Rises over the set, but **plateaus 3–5 reps before failure** (Sundstrup 2012), so it is weak near the end. Load-dependent (Jenkins 2015) | I, moderate (direction) | early-set prior adjust only |
| F9 | EMG MNF/MDF and Dimitrov FInsm5 in the window | EMG | Direction is robust (M). Per-rep estimator SD ~9 Hz at 0.5 s, so the slope is only visible late (science report §3 Q3). A spectral index crossing a set level relative to start predicted isotonic endurance time (Lee & Lee, n=10) | I/M; H on dry 25.4 mm | **slope over ≥ 5 reps only**, post-set weight |
| F10 | EMG burst duration and envelope area (static-segment) | EMG | The static-segment substitute for F1. The burst includes the eccentric's lower EMG, so its edges are soft | H | RIR likelihood (static) |
| F11 | Amplitude–spectrum joint state (JASA quadrant: RMS↑ and MDF↓ = fatigue) | EMG | Separates fatigue from load or effort changes (amp↑ with MDF flat) | M/I | quality and consistency check |
| F12 | SQI vector | EMG + IMU | lead-off, clip, 50 Hz ratio, LF energy, motion spikes | engineering | gate |

**Rejected as primary signals:** absolute EMG amplitude across sessions; any absolute MDF value ("90 Hz = cooked" in
CLAUDE.md has no support as a threshold, since MDF at failure is load-dependent per Jenkins 2015); fixed MVT.

### 2.5 State model (the core algorithm)

**Quantity estimated.** N, the total reps to failure for *this* set. RIR after rep k is N − k.

1. **Prior, set before rep 1.**
   - A load→N curve per person × exercise: a multilevel 2-parameter exponential, the form Mitter 2023 found best in a
     Bayesian comparison.
   - It is anchored by the lifter's logged load and their past sets.
   - Adjustments: set number within the session, and rest since the last set (the rest timer).
   - Prior SD floor ≈ the day-to-day reps-to-failure variability: SEM 0.7 reps at 90% 1RM and 1.1 at 70% (Mitter 2022,
     bench, trained) [I, moderate]. **No sensor is needed for this part; it is the "history" baseline.**
2. **Likelihood, from reps 1…k.**
   - Each feature's slowdown is modelled as fᵢ(k) = 1 + aᵢ·(k/N)^bᵢ + εᵢ. This is the fraction-of-set-completed shape
     that velocity loss follows at group level (Rodríguez-Rosell 2020; González-Badillo 2017).
   - aᵢ and bᵢ have population hyperpriors that shrink toward the person's estimates as labels accrue.
   - σᵢ is inflated when SQI is degraded.
   - Posterior over N is a **grid** (N = k…60; 60 cells × ≤ 6 features × k reps): microseconds of compute.
3. **Observations that update the posterior and the person parameters:**
   - **Stall/failure observed:** N = k (or k−1 if the failed rep is not counted), the strongest label.
   - **Set stopped at k, no failure, no tag:** N ≥ k, a censored observation. Weak, but there are a lot of them.
   - **User RIR tag r:** r = (N − k) + bᵤ + ε, ε ~ N(0, σᵤ²), with the bias bᵤ and spread σᵤ learned per user (§4).
   - **Check-set button press at rep j, then continued to failure:** gives the user's own "2-left" calibration point
     and N, which is the cleanest bias label.
4. **Drift.** Person × exercise parameters follow a random walk, with process noise tuned so that ~3–4 weeks without
   an anchor widens the prior noticeably. A failure set re-anchors. Detraining or a strength jump (a logged PR) inflates
   the variance.
5. **Output.** The posterior median and 80% interval of N − k, as in §1a.

**Why this structure.**
- Individual relationships are needed:
  - individual vs general reps–velocity R² 0.98 vs 0.45–0.49 (Jukic, Helms & McGuigan, fastest rep);
  - general RIR–velocity equations failed in bench (García-Ramos 2018);
  - individual load-specific > individual multi-load > general in prone bench pull (r 0.93 > 0.83 > 0.65/0.61).
- Sensor-only RIR models also fail in places:
  - velocity-based RIR estimates were inaccurate for 69.1% of reps in recreationally active people (Mansfield 2023);
  - velocity did not predict total reps in a 56-person back squat study (Haischer);
  - velocity was "compromised" in hex-bar deadlift at 65/85% (JSCR 2026).
  - **A prior from the lifter's own history plus a sensor likelihood degrades gracefully. A sensor-only regressor
    does not** [I, moderate for the need to individualise; H for the specific model].

### 2.6 Exercise coverage — what the single puck can see

| exercise (puck on target) | segment | usable features | expected confidence |
|---|---|---|---|
| Squat, leg press, lunge, split squat, hack squat (quad/glute on thigh) | moves | F1–F7, F9 | best single-puck case [H] |
| Lateral raise, OHP, front raise, rear-delt fly (delt on upper arm) | moves | F1–F7, F9 | good [H] |
| RDL, hip thrust (glute/ham on thigh) | moves (hip) | F1–F7 | moderate [H] |
| Seated/lying leg curl (hamstring on thigh) | static-ish | F7–F10, F11 | weak; second puck recommended |
| Biceps curl, preacher (biceps on upper arm) | **static** | F8–F11 | weak. Wrist/forearm or dumbbell clip recommended. Wrist-IMU near-failure (RIR ≤ 2) classifier F1 = 0.82 on preacher curls, n=13 (King 2025 preprint; validation split not seen) [I, very limited] |
| Pushdown, skull-crusher (triceps on upper arm) | static | F8–F11 | weak |
| Leg extension (quad on thigh) | static | F8–F11 | weak. Linear encoder on knee extension had a "slightly lower" ≤ 2-rep hit rate than lat pulldown/bench (>90%) (Külkamp 2024) |
| Calf raise (calf on shank) | moves little | F1 (small angles), F8–F11 | weak |
| Chest press / fly (pec on chest) | static | F8–F11 | weak; sternum-band artefact risk |

**Static-segment replacement, in order of preference:**
1. EMG burst duration (F10) as the duration proxy.
2. The EMG spectral slope over ≥ 5 reps (F9).
3. A second puck on the moving segment (forearm or shank), or on the implement.

Option 1 is **untested**. The eccentric's low EMG makes burst edges soft, and near failure lifters change cadence
voluntarily. The design rule is simple: **static-segment exercises start in "readout only, wide interval" mode** and
never cue until Stage C validates them.

### 2.7 With the second puck as a bar/stack/limb clip

| mode | adds | evidence | notes |
|---|---|---|---|
| **Bar/Smith/stack clip** | Vertical bar velocity by ZUPT integration. **Fastest-rep velocity and velocity loss** become the main likelihood terms (replacing F2), with an individual RIR–velocity model per exercise | I, moderate for LPTs. Bar IMUs are mixed (Vmaxpro ICC 0.55–0.96 across sources; IMUs "less reliable" in a seven-device bench study). TENSR's ZUPT is **H** until LPT-validated (FA C2) | Stall detection becomes direct. The posterior combines bar velocity (implement) with EMG of the target muscle |
| **Forearm/shank strap** | Moving-segment kinematics for curls, pushdowns, leg extension and leg curl: F1–F7 restored, plus the joint angle with puck 1 | Two-IMU angles lab-validated, not in lifting (FA C7) | Turns the static-segment exercises into moving-segment ones; the best fix for the arm and knee isolation lifts |
| **Dumbbell clip** | 3D velocity | **no validation found** (FA C3) | Lowest priority |

**Pair-price conflict (FA C6).** A second puck on the bar is not on a second muscle. Product copy must not promise
both at once.

---

## 3. Calibration UX for trained lifters

**Principle.** Never schedule a "calibration session". Learn from what trained lifters already do, and ask for at
most one small favour per exercise per block.

1. **Day 1 — history prior.** On first use of an exercise the app asks: "Last time you did ~this load, how many reps
   could you do?" Or it imports from a log. That sets the load→N prior with a wide SD.
2. **Natural failure sets — passive.** Many trained lifters take the last set of an isolation movement, or a
   machine set, to failure. The stall detector flags it, the app asks one-tap confirmation, and that set becomes an
   **anchor**. The first 2 anchors per exercise switch the model from "history only" to "calibrated".
3. **Censored sets — passive, every set.** A set stopped at k without failure still says N ≥ k. Across weeks this
   bounds the curve from below at no cost to the user.
4. **RIR tag — optional, post-set, one tap.** The app shows its estimate first only if the user has opted into "show
   then tag". The default is **tag first, then reveal**, so the tag stays independent of the device (§4).
5. **Check set — optional, ≤ 1 per exercise per 4–6 weeks.**
   - The app picks a set the user was already going to take hard.
   - The lifter **presses the puck button** (BUTTON_START_STOP, already on the board) when they believe 2 reps are
     left, then continues to failure.
   - That one set gives the person's self-report bias **at the RIR that matters**, plus N at that load. It is the
     two-visit validation-plan design compressed into a single set.
   - **Only offered on machines, Smith with safeties, or dumbbell/cable isolation work.** Never prompted on
     free-weight squat or bench without the safety toggle (FA C5).
   - Reaching the puck mid-set may be awkward on some placements; a phone tap or voice command is the alternative
     [H].
6. **Recalibration.**
   - Uncertainty grows with time since the last anchor (§2.5.4), so the interval widens visibly. The app nudges for
     an anchor only when the interval on that exercise exceeds ~3 reps.
   - A logged PR or a load jump > 10% inflates the variance.
   - A new band position is detected from the electrode-quality / RMS-baseline shift and resets the EMG-feature
     weights, but not the history prior.

**Acceptance risk.** There are **no user-acceptance data** for calibration-to-failure (FA C5). The passive design
above is the hedge, and Stage D measures how many anchors real users generate per exercise per month [H].

---

## 4. Beating the lifter's own guess

**Model the tag as a measurement, not as truth.** r = RIR_true + bᵤ + ε.
- Halperin 2022: mean underprediction 0.95 reps (95% CI 0.17–1.73), between-participant SD ~1.45 reps, I² 97.9%
  [I, moderate].
- **Within-person** residual SD after removing each person's bias is not reported anywhere I could find. That is the
  number that decides whether fusion helps. **Measure it in Stage C.**
- The trained-lifter error may be much smaller than the review average: Refalo 2024 JSCR (bench, 24 trained),
  0.65 ± 0.78 reps — **one summary, UNVERIFIED**.
- Bias direction shifts over weeks while absolute accuracy stays flat (FAU six-week bench study, abstract level).
- Errors grow with more reps per set (FAU squat/bench) and lighter loads (Murdoch 2020; Halperin).

**Fusion arithmetic** [M; Gaussian approximation, RIR treated as continuous; independent of TENSR's actual error,
which is unknown]. Fused SD = √(σs²σx²(1−ρ²) / (σs² + σx² − 2ρσsσx)); MAE ≈ 0.8 × SD.

| self-report SD σs (bias-corrected) | sensor SD σx | error correlation ρ | fused SD | fused MAE |
|---|---|---|---|---|
| 0.8 | 1.0 | 0 | 0.62 | 0.50 |
| 0.8 | 1.5 | 0.5 | 0.80 | 0.64 — **no gain** |
| 1.0 | 1.0 | 0.5 | 0.87 | 0.69 |
| 1.0 | 1.5 | 0.5 | 0.98 | 0.78 — **no gain** |
| 1.45 | 1.5 | 0 | 1.04 | 0.83 |
| 1.45 | 1.0 | 0 | 0.82 | 0.66 |

**Reading.**
- Fusion pays when the sensor's error is **within ~1.5× of the lifter's** and the two errors are **not strongly
  correlated**.
- ρ will be positive, because lifters also feel the slowdown. Features the lifter cannot perceive are worth more for
  fusion than features they can: EMG spectral compression and tremor band power (H).
- Against a well-calibrated trained bench presser (σ ~0.8) the sensor needs σx ≲ 1.0 to matter at all. Against a
  high-rep light-load leg extension (σ plausibly ≥ 1.5), it needs σx ≲ 2.

**Product consequences.**
1. **Learn bᵤ, σᵤ per user, and per exercise class where the data allow**, from anchors and check sets only. Never
   learn it from the device's own estimate; that would be circular.
2. Show **"your guess (corrected) / sensor / combined"** for the first weeks. Trust is earned by being visibly right on
   anchor sets.
3. **Default the fusion weight from validation, not from optimism.** If Stage C finds σx > 1.5σs for an exercise
   class, the sensor term is dropped there. The readout is then honestly "your tag, bias-corrected, plus history".
   That is still a better product than a raw tag.
4. **Place the sensor where humans are weakest:** high-rep, light-load and isolation sets, and early-set estimates.
   Note that the validation plan's R4.4 still demands a win inside RIR 0–3.

---

## 5. Staged validation plan for this feature

Builds on `TENSR-VALIDATION-PLAN.md` §4–5. It does not replace R4.1–R4.5 or S5.1. Every number below is an
**ENGINEERING TARGET** unless marked otherwise.

### Stage A — bench, no humans

| ID | test | target |
|---|---|---|
| A1 | Feature pipeline on synthetic EMG with an imposed MDF ramp (−25% over 12 "reps"), plus 50 Hz and motion artefact injection | MDF slope recovered within ±10% of truth at 2 kSPS, 400 ms windows, ≥ 5 reps; notch bias < 2 Hz |
| A2 | Haptic artefact: DRV2605L effects firing while the electrodes are on a skin phantom | Artefact energy in 20–450 Hz below the noise floor after the 100 ms blanking |
| A3 | Latency: rep end → haptic start, with the IMU and EMG pipeline running | ≤ 300 ms median, ≤ 500 ms p95 |
| A4 | BLE: per-rep records and raw research stream at 2 kSPS EMG + 416 Hz IMU for 60 s sets | 0 lost per-rep records (buffered); raw-mode loss < 0.1% |

### Stage B — feasibility pilot (internal, n ≈ 8–12 trained, pre-registered as exploratory)

- **Exercises:** one moving-segment (leg press or Smith squat, thigh puck), one moving upper-limb (lateral raise or
  machine shoulder press, delt puck), one static (biceps curl, upper-arm puck).
- **Loads:** ~65 / 75 / 85% e1RM, sets to failure. LPT on the implement, plus video.
- **Questions:**
  - Do F1/F2/F10 rise monotonically within a set in ≥ 80% of sets?
  - How often does SQI withhold a set?
  - Stall-detector sensitivity and specificity against two blinded video raters.
- **Go/no-go:**
  - **monotonic-slowdown rate ≥ 80% (moving), ≥ 60% (static);**
  - **withheld ≤ 20%;**
  - **stall sensitivity ≥ 85%.**
  - Failing on the static class moves it to "readout only" and makes the forearm puck the plan.
- **Leakage rule:** the pilot's thresholds are never tested on pilot data again (validation plan §4).

### Stage C — lab validation of RIR (n by Riley 2020/2024; plan ~30–40 trained)

**Design.** The two-visit RIR protocol from validation plan §4.
- Visit A: calibration sets to failure. Visit B: stop at a prescribed rep, record the lifter's tag and the device
  estimate, then continue to failure for true RIR.
- **Add one check-set** (button at "2 left") per exercise to measure bᵤ and σᵤ directly.
- Exercises: the Stage B three plus one static isolation (leg extension). Bar clip arms on Smith squat and stack
  machines.

**Splits.**
- Leave-one-subject-out for population hyperparameters.
- **Within-subject new-session tests** for personalised models.
- New-load, new-exercise and new-tempo tests reported separately.
- Never record-wise (Saeb 2017).
- The total set length is never a feature (validation plan §4).

**Matched-rep analysis (S4.matched).** Features from reps 1…k only, where k is the stop rep.

**Baselines (all mandatory):**

| baseline | definition |
|---|---|
| B0 | rep count + **population** load→N |
| **B1** | rep count + **individual** load→N history prior (the §2.5 prior with no sensor term). **This is the baseline that matters**; it is new versus the validation plan |
| B2 | IMU-only likelihood (F1–F7) |
| B3 | self-report, raw |
| B4 | self-report, bias-corrected from the person's earlier anchors only |
| B5 | individual RIR–LPT-velocity model (Jukic method), on the exercises where an LPT applies — the "ceiling" reference, not a product baseline |

**Metrics.**
- MAE in reps, overall and **within true RIR 0–3**.
- Signed bias.
- 80%-interval coverage.
- Calibration slope and intercept.
- Stall-detector sensitivity, PPV and false-alarm rate per 100 non-failure reps.
- Cue precision (below).
- Every metric with participant-bootstrapped 95% CIs.

**Acceptance — all ENGINEERING TARGET:**

| ID | criterion |
|---|---|
| X4.C1 | Fused estimate beats **B4** (bias-corrected self-report) in RIR 0–3: paired MAE difference, upper 95% CI < 0 (= R4.1 / R4.4) |
| X4.C2 | Sensor term beats **B1** (history-only prior) by ≥ 0.3 reps MAE, CI excluding 0. **Otherwise the sensor is not doing the estimating; history is.** |
| X4.C3 | EMG features beat **B2** (IMU-only) by ≥ 0.2 reps MAE, or EMG is dropped from the RIR model and kept for SQI and rep timing only (= R4.2/R4.5 spirit) |
| X4.C4 | 80%-interval empirical coverage 0.75–0.85 per exercise class |
| X4.C5 | Stall detector: sensitivity ≥ 90% on moving-segment exercises, ≥ 75% static; ≤ 1 false stall per 200 non-failure reps |
| X4.C6 | Live-cue precision: when the cue fires for target T, true RIR ∈ [T−1, T+1] in ≥ 80% of cues; true RIR < T−1 (cue late, lifter nearer failure than intended) in ≤ 5% |
| X4.C7 | Absolute MAE in RIR 0–3 reported against Jukic 2024's "<2 reps" (squat, individual LPT) [benchmark: I]. "≤ 1 rep" is the aspiration, not a gate |

### Stage D — gym field study (consented, free-living, 6–8 weeks)

Measure the following:
- anchors generated per exercise per month;
- withheld-set rate;
- drift of the person parameters;
- disagreement rate between the tag and the device;
- MAE on naturally occurring failure sets, comparing the prediction made at rep k−2 with the observed N.

**Targets:**
- ≥ 1 anchor per exercise per 4 weeks for ≥ 60% of users' regular exercises, or the passive calibration plan is
  revised;
- withheld ≤ 15%.

### Stage E — decision quality (validation plan §5)

The acute crossover runs as written: TENSR cue vs self-report vs blinded device, with target RIR 2. **S5.1 is the
safety gate for shipping the live cue.** The parallel-group RCT runs only after X4.C1 and S5.1 pass.

---

## 6. Firmware, compute and BLE implications

| item | design | basis |
|---|---|---|
| ADS1292R data path | 2 kSPS DRDY interrupt → SPI read of 9 bytes (status + 2 ch) → ring buffer. The ESP32-S3 SPI with DMA handles this easily | datasheet DR; science report §5.4 |
| IMU | LSM6DSO 416 Hz accel + gyro, FIFO watermark ~32 samples, I2C batched reads | F6 I2C budget |
| Per-rep compute | 20 Hz HP + notch (IIR, per sample); RMS; one 1024-point float FFT per rep window (or 3 × 256-point Welch). ESP-DSP lists `dsps_fft2r_fc32` 1024-point at **97,847 cycles on ESP32-S3 ≈ 0.41 ms at 240 MHz** (my conversion). Moments, MDF, FInsm5, kinematics, grid posterior (60 × 6 × k): ≪ 1 ms | Espressif ESP-DSP benchmark [vendor doc] |
| Where the model runs | **Posterior and cue on the puck**, so a BLE dropout cannot delay or fabricate a cue. **Person parameters fitted on the phone** and pushed to the puck before each exercise (~200 bytes) | design |
| Latency budget | Rep-end detection 100–200 ms (needs the start of the eccentric, or burst offset + hysteresis); compute < 5 ms; DRV2605L trigger over I2C ~1 ms plus motor spin-up tens of ms → **~0.2–0.4 s** | science report §5.4 (0.3–0.6 s); A3 measures it |
| BLE product mode | One record per rep (~40 B: rep index, timestamps, 10 features as int16, SQI bits, posterior median and interval), one per set (~32 B). Negligible bandwidth | design |
| BLE research mode | Raw EMG 2 kSPS × 3 B = 6 kB/s plus IMU 416 Hz × 12 B ≈ 5 kB/s ≈ **11 kB/s**. Needs 2M PHY / DLE, which the ESP32-S3 supports; confirm the throughput on the bench (A4) | arithmetic [M] |
| Two-puck sync | Time offset from BLE connection events or a periodic sync message. Rep-level features need ~5–10 ms, not µs | design [H] |
| Button | The existing BUTTON_START_STOP serves as the check-set marker and the "this was failure" confirmation | board |
| Firmware prerequisites | `RLDREF_INT = 1` before RLD use; respiration never enabled (CLAUDE.md) | CLAUDE.md |

**Respin needed: none.**
- Nice-to-have for v2, none required:
  - an orthogonal CH2 electrode pair, so that fibre orientation stops being unknown (F6, needs a respin);
  - an easier-to-reach button position.
- A magnetometer is **not** needed for any part of this feature.

---

## 7. What would make this fail — and the honest fallback

1. **The history prior (B1) is as good as the sensor (X4.C2 fails).** Then TENSR's effort feature is "your history,
   your tags bias-corrected, failure auto-detected, hard sets counted". That is still useful and still automatic,
   but the sensor is a rep/stall detector, not an RIR meter. Say so in marketing.
2. **Static-segment exercises stay weak.** Ship them as readout-only with wide intervals, and sell the forearm/shank
   strap mode.
3. **Dry-electrode quality withholds too many sets.** Snap-on gel electrodes are the largest lever (science report
   §5.3). The IMU features carry on regardless.
4. **The trained-lifter tag is already ~0.6–0.8 reps MAE** (if Refalo 2024 holds). On heavy compounds the device
   cannot beat it. Its value there is **objectivity and logging without typing**, not accuracy. Do not claim "more
   accurate than you" until X4.C1 passes for that exercise class.

---

## 8. Open items

- Within-person residual SD of bias-corrected RIR tags in trained lifters. Not found; decisive for §4.
- Refalo 2024 JSCR intraset bench numbers (24 trained; 0.65 ± 0.78): UNVERIFIED, one summary.
- The King 2025 preprint's validation split (LOSO or not) and its participant split: not seen.
- The Achermann 2024 ISBS sample and exercise: not seen.
- Upper-arm/thigh rep counting and EMG-burst duration as a velocity proxy: no study found. Stage B answers it.
- Tremor 8–14 Hz vs reps to failure: no direct study found.
- Haptic artefact coupling from the DRV2605L motor into the dry electrodes: bench test A2.
