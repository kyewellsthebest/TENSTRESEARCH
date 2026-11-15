# X3 — Do velocity and rep-duration methods for proximity to failure work beyond barbell squat and bench, and from a limb-worn sensor?

Agent X3, 2026-11-03. Research only. Studies: `X3-studies.csv` (38 rows). Searches: `X3-searchlog.md`.

**Access caveat.** WebFetch was refused for every host tried: PMC, PeerJ, Abertay and the sport-iat database.
So **no full text was read**. Every figure here is from an abstract excerpt seen through search (ABSTRACT) or
from a review or summary (SECONDARY), and is labelled that way. Prior work is not redone: F6 §3.1 and FA §4
(C2–C5) stand unless corrected below.

**Evidence codes** (SHARED-STANDARDS): D direct, I indirect, M mechanistic, H hypothesis.

## Summary (10 lines)

1. **Where it works:** barbell and Smith compounds, and pull-ups (squat, bench, prone row/bench pull, shoulder press). At
   the group level velocity loss (VL) tracks % of reps done very tightly (R² 0.88–0.97). Held-out prediction for one person is worse.
2. **Individual vs general models:** individual RIR–velocity models predict the next session to a **mean error under 2 reps**
   (Jukic 2024, n=46 trained, squat). General models do not reach that.
3. **VL % alone:** it predicts % reps with **more than 10% error** even when individualised (Jukic 2023 EJAP).
   In recreational lifters, set-1 velocities named the right RIR for **only 30.9%** of later reps (Mansfield 2023, BP + row).
4. **Velocity at failure is exercise-specific.** The minimal velocity threshold (MVT) runs from about 0.15–0.17 m/s
   (deadlift, bench) to about 0.40–0.47 m/s (seated row, lat pulldown). For one person, last-rep velocity is **unreliable**
   (CV over 18%, ICC under 0.60; García-Ramos 2020, n=96). A fixed per-person "failure velocity" is noisy.
5. **Machines:** the evidence is mostly load–velocity / 1RM work, not proximity to failure. The only machine VL→effort study
   found (leg press, older women) found VL **no better than traditional methods**.
6. **Isolation lifts, dumbbells and cables:** **no** VL→RIR validation found. Load–velocity was **inadequate** for 1RM on lower-limb
   single-joint lifts (Sport Sci Health 2025). Leg curl: r ≤ 0.22. Dumbbell IMU validity rests on n=5 with reps pooled (Sato 2015).
7. **Limb-worn IMUs:** forearm PUSH bands fail against LPTs (Banyard 2017; Orange 2019; Pérez-Castilla 2021). Wrist devices
   look good (Apple Watch r 0.95–0.97, SEE 0.064 m/s) **only because the wrist moves with the bar**. TENSR's puck sits on a muscle belly.
   **No** thigh- or upper-arm-worn validation exists.
8. **Rep duration:** at a constant range of motion (ROM), concentric duration is equivalent to mean velocity (M). It has **no**
   proximity-to-failure validation. It breaks when ROM shortens near failure. It is still the one signal available on every exercise,
   from the EMG burst, even where the worn segment does not move.
9. **Tempo:** every VBT study used maximal intended concentric velocity. Under a strict slow tempo, velocity is held down until the
   lifter can no longer hold the tempo. So expect a stall signal in the last ~1–2 reps, not a graded RIR (M/H; **no study found**).
10. **Achievable accuracy:** see the table in §6. Roughly 1–2 reps with a calibrated bar or stack clip on compounds. ≥2–3 reps,
    or only a "stall/failure" flag, with a limb puck or duration on isolation lifts. The lifter's own estimate is off by about 1 rep
    near failure (Halperin 2022), and that is the comparator to beat.

---

## 1. Velocity loss vs % reps completed, and RIR: what holds and for whom

| study | exercise | n / status | finding | evidence |
|---|---|---|---|---|
| SanchezMedina2011 | Smith squat, bench | trained | VL tracks lactate (r 0.97 squat, ~0.95 bench; **secondary**) | D group, moderate |
| GonzalezBadillo2017 | Smith bench | 22 + 28 men | VL–%reps "very close", similar across 50–70% 1RM; %reps for a given VL reliable | D group |
| RodriguezRosell2020 | Smith bench and squat | 20 men | R² 0.97 BP, 0.93 SQ. For the same VL, **bench has done fewer of its reps than squat**. RTF CV between people 15–22% BP, 26–34% SQ | D group |
| Izquierdo2006 | bench, squat | 36 | same relative pattern at every load; velocity falls faster in bench | D group |
| HernandezBelmonte2022 | full squat, shoulder press, prone bench pull | mixed | reps vs VL R² ≥ 0.97; within-subject SEM of RTF ≤ 1.9 reps | D group |
| SanchezMoreno2017 | pull-up | 52 | R² 0.88, stable after RTF rose 15% | D group |
| MoranNavarro2019 | four exercises | 30, novice to highly trained | velocity at 2/4/6/8 RIR similar across loads **and** training levels, reliable | D group (exercise list not captured) |
| Jukic2023EJAP | free-weight squat | trained | general **and** individual VL–%reps relationships predict the next session poorly (abs. error >10%) | D held-out, moderate |
| Jukic2023PB | squat | trained | fastest-rep velocity → RTF: **1.96 reps individual vs 2.81 general**, mean error, held-out | D held-out |
| Jukic2024 | free-weight squat | 46 (15F/31M) trained | individual RIR–velocity <2 reps mean error at 72 h; general not acceptable | D held-out, moderate |
| Qin2025 | Smith bench | 19 active men | general RIR–velocity bias −0.4 to +0.6 reps at 60/80%. %1RM and RTF–velocity approaches overestimated RIR by 3–6 reps at 60% | D, **bias not abs. error** |
| Mansfield2023 | free bench, prone row | recreational | 30.9% of later reps classified to the right RIR; velocity drifts across sets and loads | D held-out, negative |
| Paulsen2025 | squat, bench | 19 strength-trained, 2,972 obs | velocity vs *perceived* RIR, individual r² ≈ 0.3. Exercise, load, VL threshold and set number all shift it | D, negative-ish |
| MirasMoreno2023 | prone bench pull, Smith vs free | – | velocity for a given RTF is **higher on Smith** than free weight. Prediction error is similar | D |

**Reading.** The tight R² values are group fits across pooled sets. They say little about how many reps *this* lifter
has left in *this* set. What decides usefulness is held-out prediction:
- Jukic: about 2 reps with individual models.
- Mansfield: about 1 rep in 3 called correctly.
- Qin: small mean bias, absolute error not captured.

**Correction to F6.** F6 quoted "individual RSE ~1.0–1.2 reps vs general 3.4–3.7" for Jukic 2023 *Physiol Behav*. Those
are goodness-of-fit figures. The held-out mean prediction error in the abstract is **1.96 vs 2.81 reps**. Use the
held-out numbers.

**Upper vs lower body.** At the same VL the bench is further through its set than the squat, and velocity falls faster on
the bench (Izquierdo 2006; Rodríguez-Rosell 2020). Equations are therefore **exercise-specific**: a single VL cut-off
applied across lifts is wrong by construction (D, moderate). Lower-body sets also vary more in reps to failure (CV
26–34% vs 15–22%).

**Training status.** Morán-Navarro 2019 found velocity at a given RIR did not differ by training level. Jukic 2023
found that sex and training history did not change accuracy. So trained lifters are no harder, though no easier either (D, limited).

## 2. Minimal velocity threshold and last-rep velocity

- **MVT differs by exercise.** Values as surfaced from the NSCA VBT review table (SECONDARY):

  | exercise | approx. MVT |
  |---|---|
  | bench | 0.16–0.17 m/s |
  | deadlift | ~0.15 m/s |
  | leg press | ~0.21 m/s (15 athletes) |
  | seated row | ~0.40 m/s (n=23) |
  | lat pulldown | ~0.47 m/s (n=23) |

  - Machine pulls "fail" at roughly 3× the bench's velocity.
  - Any general failure-velocity default must be per exercise (I, limited).
- **Last-rep velocity is a poor per-person constant.**
  - Smith bench, n=96: CV >18.3%, ICC <0.60 between sessions.
  - Correlation with 1RM velocity: r 0.18 paused, 0.37 touch-and-go (García-Ramos 2020).
  - For 1RM work, a general 0.17 m/s or a session-optimised MVT beat the person's own measured failure velocity:
    2.94 kg vs 4.02 kg error, n=126 (García-Ramos 2023; Janicijevic 2021).
  - **Implication for TENSR (M):** do not detect failure by "velocity fell below your stored V_fail". Use the *within-set
    trajectory*: slope and curvature of the decline relative to this set's fastest rep. Treat the last-rep velocity as noisy.
- **Inter-repetition pauses** change the RIR–velocity relationship (PMC11833798, details not captured). In a gym, lifters
  rest-pause near failure, which shifts velocity upward and makes RIR look larger than it is (M).

## 3. Beyond the barbell: machines, Smith, dumbbells, cables, isolation lifts

| class | proximity-to-failure evidence | velocity measurability | verdict |
|---|---|---|---|
| **Smith machine** (squat, bench, prone pull, shoulder press) | Most of the Spanish-group VL literature *is* Smith. Qin 2025 general RIR–velocity bias ≤0.6 reps | rail = 1-D motion, ideal for an IMU | **Best case** (D, moderate) |
| **Pin-loaded compound machines** (leg press, lat pulldown, seated row, chest press) | Leg press VL in older women: no better than traditional (D, limited, wrong population). Pulldown/row: L–V and MVT data only. Chest press: nothing found | weight stack moves vertically, 1-D, with natural zero-velocity points. Stack-tracked L–V fits well on leg extension (R² >0.93) | **Plausible, unvalidated** (I, limited). Pulley ratios mean stack velocity ≠ handle velocity, so it must be calibrated per machine. |
| **Dumbbells** | none found for VL→RIR | IMU validity rests on Sato 2015 (n=5, pooled reps, r 0.80–0.92). An unsourced 12.6% / 14.0% error was reported for PUSH on the DB press. Dumbbells rotate, so axis-agnostic integration is needed | **Unvalidated** (I, very limited) |
| **Cables** | none | handle path is 3-D and swings; the stack side is 1-D | **Unvalidated**. A stack clip is the only sane mount (H). |
| **Isolation lifts** (curl, triceps ext., lateral raise, leg ext., leg curl) | **none found for VL→RIR**. L–V "inadequate" for 1RM on lower-limb single-joint lifts (SSH2025). Leg curl r ≤ 0.22, SEE ≥ 42% (secondary). Leg extension individual fit good (R² >0.93) | low absolute loads, short ROM, small velocity range. Partial reps and body English near failure | **Not credible for graded RIR** today (I, limited). A stall/failure flag is plausible (H). |

**Why isolation lifts are hard (M):**
- MVT is high relative to the starting velocity, so there is a small dynamic range to resolve 5→0 RIR.
- Many hypertrophy lifters do not use maximal concentric intent on isolation work.
- Near failure, lifters shorten ROM or cheat (swing on curls, hip drive on raises). That *raises* bar velocity while the target
  muscle is failing.
- FA C4 already noted that self-reported RIR is also poor on the leg extension (ICC 0.18–0.66). The ground truth is shaky there too.

## 4. From a limb-worn sensor

**What has been validated is the wrist or forearm, and only because it rides with the bar.**

- **Forearm PUSH:**
  - Banyard 2017 (n=10): questionable for velocity at all loads.
  - Orange 2019: valid only for mean power at 40% bench.
  - Pérez-Castilla 2021: "reliable but not valid".
  - Callaghan 2022: acceptable only for back squat under ~1 m/s.
- **Wrist:**
  - Beast wrist band r 0.94–0.98 vs LPT (Balsalobre 2017, n=10 powerlifters; correlations, not limits of agreement).
  - Apple Watch strapped tight: r 0.952–0.965, SEE 0.064 m/s on the squat vs Vicon (Achermann 2023).
  - A 0.064 m/s SEE is about 15–25% of a near-failure squat velocity of ~0.25–0.4 m/s (estimate). That is large next to the
    ~0.03–0.05 m/s step between adjacent RIR levels near failure. The step is *inferred* from Mansfield's 0.05 m/s load effect,
    not measured (H).
- **The muscle belly:** no study found validating a thigh-, upper-arm- or chest-worn IMU for bar velocity or proximity to failure.
  The 2021 IMU systematic review's valid models were all bar-mounted.

**Transfer to TENSR's puck (on the muscle belly):**

| puck on | exercise | does the worn segment move with the load? | what the puck can give |
|---|---|---|---|
| quad / glute (thigh) | squat, leg press, lunge, hip thrust | yes, rotates | thigh angular velocity. A within-set slowdown is plausible. Converting to bar m/s needs segment-length geometry (H) |
| delt (upper arm) | lateral raise, press, fly | yes | upper-arm angular velocity *is* the movement. A within-set slowdown is directly measurable (H) |
| lat / upper arm | pulldown, row | upper arm moves | as above (H) |
| biceps / triceps (upper arm) | curl, pushdown, skull-crusher | **no**, upper arm static | **no velocity**. Only EMG burst timing and tiny residual motion |
| quad / hamstring (thigh) | leg extension, leg curl | **no** (seated); thigh static | **no velocity**. EMG burst timing only |
| pec (chest) | bench, chest press, fly | **no**, torso static | **no velocity** |
| calf (shank) | calf raise | small shank tilt only | marginal |

Elshafei 2021 is the nearest thing to the delt-type case. A wrist IMU on concentration curls (20 gym-goers, ~3,000
reps) found angular velocity falls and completion time rises with fatigue. But the labels were RPE, and accuracy and
the subject split were not captured. The authors' 2022 follow-up personalises the model with crowd data, which
suggests cross-subject generalisation was weak (I, very limited).

## 5. Rep duration as the sensor-agnostic fallback

- **Mechanism (M, strong).** Mean concentric velocity = ROM / concentric time. If ROM is constant, %VL and %duration-increase
  carry identical information: a 30% VL is a 43% duration increase. All VL equations therefore transfer to duration *on
  condition* of constant ROM and maximal intent.
- **Validation:** **none found** for concentric duration as a proximity-to-failure predictor. The only adjacent data is
  Elshafei's "completion time rises" (I, very limited).
- **Where it breaks:**
  - ROM shortening near failure: duration can *fall* on a half rep while the muscle is failing.
  - Pauses at lockout or at the sticking point.
  - Sticking-region stalls lengthen duration abruptly. That is useful as a failure flag, not as a graded RIR.
  - Slow imposed tempo (§6a).
- **Why it still matters for TENSR:** it is available from the **EMG burst envelope** on every exercise, including the static-segment
  ones (curl with a biceps puck, leg extension, pushdown, chest press) where the IMU sees nothing.
  - Combining burst duration with IMU segment angle where available would give a ROM-normalised duration: an "angular
    velocity" substitute (H).
  - Burst onset/offset timing jitter on dry electrodes is unmeasured. At typical 1–2 s concentric phases, ±50 ms jitter is
    ±2.5–5% (estimate), comparable to the 5–10% per-rep VL increments near failure.

## 6. Tempo-controlled sets

**No study found** that tests velocity-based RIR under an imposed tempo.

Every study above instructed maximal intended concentric velocity, and Qin 2025 and the VL literature explicitly
require it.

**Mechanism (M):**
- With a 2–3 s concentric cadence the lifter throttles velocity below capacity.
- Measured velocity stays flat until the required force exceeds what the fatigued muscle can produce at that speed.
- It then drops abruptly, often on the last 1–2 reps.
- Velocity under a tempo is therefore a **late, binary stall signal**, not a graded proximity measure.
- The same applies to duration, which is fixed by the tempo until the stall.

**For a strict-tempo lifter:**
- Graded proximity has to come from something not under voluntary control. EMG amplitude/MDF and tremor are the
  candidates, and they belong to the other agents' questions.
- An app that asks "max intent or tempo?" per exercise is needed so the velocity model is not applied where it cannot work (H).

## 7. Conclusion: achievable accuracy per exercise class

Rep errors are **mean absolute error in RIR on held-out sets**, where evidence exists. Otherwise they are marked as
estimates. "Stall flag" means detecting the failed or grinding rep, not predicting it.

| exercise class | (a) bar / implement / stack IMU | (b) limb-worn TENSR puck | (c) rep duration only (EMG burst or IMU) | calibration needed |
|---|---|---|---|---|
| Barbell squat, bench, row; Smith; pull-up | **~1–2 reps** individual (Jukic 2024, D moderate); general ~2–3 (Jukic 2023 PB). Smith BP general bias ≤0.6 reps (Qin 2025). **Requires an LPT-validated device**; TENSR's own clip is H | squat/lunge (thigh moves): relative slowdown, **est. ±2–3 reps, unvalidated** (H). Bench (pec puck): none | est. ±2–3 reps if ROM is stable; stall flag (H) | ≥1–2 sets to failure per exercise at working loads; recheck every ~4–6 weeks (H; Jukic tested only a 72 h gap) |
| Pin-loaded compound machines (leg press, pulldown, row, chest press) | stack clip: **est. 1.5–3 reps** individual (I limited: MVT data, L–V fits; one negative VL study in older women) | pulldown/row with a lat/delt puck: relative slowdown (H). Leg press with a thigh puck (H). Chest press: none | as above (H) | per machine (pulley ratio, MVT 0.2–0.47 m/s); sets to failure are safe here |
| Dumbbell compounds (DB press, DB row) | **unvalidated**; est. ≥2–3 reps (I very limited). A clip on a rotating DB needs orientation-robust integration | delt/lat puck where the upper arm moves (H) | (H) | as above, plus device validation vs LPT/mocap first |
| Cables | stack clip only (H) | as machines | (H) | per station |
| Isolation lifts | **graded RIR not credible** (no VL→RIR study; L–V inadequate on lower-limb single-joint). Stall flag (H) | lateral raise / fly (upper arm moves): relative slowdown + stall flag (H). Curl, pushdown, leg ext., leg curl: **no velocity at all** | **the only motion-timing signal** on static-segment lifts, via EMG burst. Stall flag at best; graded RIR est. no better than ±3 reps (H) | sets to failure per exercise; maximal-intent instruction |
| Any lift under strict slow tempo | stall flag only, last ~1–2 reps (M) | stall flag (M) | stall flag (M) | — |

**What this means for the product:**
1. A velocity-derived RIR can be claimed only for exercises where something rides with the load: a bar clip, a Smith bar
   or a weight stack. It needs an **individual** calibration to failure and maximal concentric intent. Even then it is
   about 1–2 reps, which is roughly the lifter's own bias-corrected guess near failure. So the device's value is
   **consistency and the no-effort log**, not superior accuracy.
2. On isolation lifts, and wherever the puck's segment is static, velocity cannot carry effort tracking. The defensible
   features there are:
   - a **failure/stall flag**: the burst-duration jump, or a partial rep from the IMU angle where the segment moves;
   - a **per-set "how far did duration/slowdown progress"** relative to that lifter's own calibrated failure sets.
   Graded RIR there has to come from EMG (other agents) or the lifter.
3. **Validation TENSR must run itself:**
   - (i) puck-as-clip velocity vs an LPT on Smith, barbell, stack and dumbbell;
   - (ii) limb-puck angular-velocity loss vs bar VL on squat, lateral raise and pulldown;
   - (iii) EMG-burst duration vs LPT concentric time;
   - (iv) held-out RIR error vs the lifter's own call, in the same sets.
   None of (i)–(iv) has any published precedent for a muscle-belly-worn device.
