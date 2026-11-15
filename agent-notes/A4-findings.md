# A4 — TENSR product translation: findings

**Agent:** A4 (product translation). **Date:** 2026-11-02. **Status:** batch-1 draft for the A6 audit.
**Inputs read:** `PROTOCOL.md`, `SHARED-STANDARDS.md`, `CLAUDE.md`, `docs/AFE-DESIGN-REVIEW.md`, `docs/BRING-UP.md`, `docs/afe-sim-results.md`, `BOM_JLCPCB.csv`, board placement via `fputil.py`.
**Access caveat:** WebFetch was refused for every host tried (ENOTFOUND under this session's network policy). Every external source below was seen only through search-engine summaries: access is SECONDARY or ABSTRACT, never FULL. A6 should treat every external number here as needing verification. Repo facts are measured and solid.

Evidence codes and strengths follow PROTOCOL §5. Study keys refer to `A4-studies.csv`.

---

## 0. What the repo says about the hardware, measured

Board placement read with `fputil.footprints(fputil.load('routed.kicad_pcb'))`:

| part | position (mm) | layer | note |
|---|---|---|---|
| E1 | (−12.7, −11.3) | B.Cu | detection electrode |
| E3 | (+12.7, −11.3) | B.Cu | detection electrode, 25.4 mm from E1 along the board's 44 mm axis |
| E2 | (0, +11.3) | B.Cu | driven RLD reference, 22.6 mm off the pair's axis |
| U6 LSM6DSO | (−2.5, +0.7) | F.Cu | 6-axis IMU, **no magnetometer**, near the electrode centroid |
| U1 ADS1292R | (−0.4, −8.0) | F.Cu | CH1 only; CH2 inputs tied to AVDD |

The band is 38 mm wide and the board is 44 × 40 mm, so the puck is wider than the band in both directions. Nothing in the repo records which board axis runs along the band. That decides whether the E1–E3 pair runs across or along the muscle fibres (section 4).

---

## 1. Measurement definition table (Task 1)

TENSR records one bipolar sEMG channel (E1–E3, 25.4 mm, dry 7 mm stainless studs), with the reference driven on the same muscle, plus a 6-axis IMU on the puck. It has no load input, no bar sensor, no second segment and no magnetometer.

**Joint angle from one puck IMU:** the IMU gives the orientation of the segment the band sits on. Pitch and roll come from gravity. Yaw drifts, because the board has no magnetometer. A joint angle is the relative orientation of two segments, so one IMU gives a joint angle only if the other segment's orientation is assumed. That works on a seated machine with a fixed segment. In free movement it does not. In many isolation exercises the band sits on the static segment: upper arm in a curl or pushdown, thigh in a leg extension, torso in a bench press for the chest. Then the IMU sees almost no rep motion at all. The puck rides on the muscle belly, so belly shape change will also tilt the puck slightly. That adds an artefact to segment orientation. [M; strength n/a, it is geometry]

| Construct | Physiological concept | Research-setting direct measure | What TENSR actually records | What could potentially be inferred | Assumptions & confounders | Required calibration | Confidence & validation needed |
|---|---|---|---|---|---|---|---|
| Muscle electrical activity | Summed motor-unit action potentials under the electrodes | Gel bipolar sEMG at SENIAM site, IED ≤20 mm, aligned to fibres; HD-EMG; intramuscular EMG | Differential voltage E1–E3 (24-bit, PGA), sampling rate TBD (500 SPS bring-up) | Burst timing; relative amplitude within a wear | Dry-contact impedance and drift; crosstalk (25.4 mm IED, 7 mm rings); orientation vs fibres unknown; reference on active muscle | Rest baseline per wear | **Measured**, quality unknown until bring-up §8. Validation: SNR and agreement vs gel reference |
| Muscle force & joint torque | Tension in the muscle; moment about the joint | Dynamometer, force plate, load cell, inverse dynamics | Nothing direct. EMG amplitude only | At best a within-wear, within-exercise, isometric-calibrated EMG–force curve | EMG–force is nonlinear, muscle-specific and velocity-dependent. Fatigue changes it (amplitude rises at constant force) | Per-wear multi-level contractions against a known load | **Not measured**. Inference: research-only [I; limited] |
| Mechanical tension | Active + passive force per fibre / per muscle | Not directly measurable in vivo. Estimated via force × moment arm models, shear-wave elastography | Nothing | Nothing beyond the force row | As above, plus passive tension at long lengths (no EMG at all) | n/a | **Not measurable** with this hardware [M] |
| Muscle length & stretch | Fascicle/MTU length, ROM at long lengths | Ultrasound fascicle imaging; motion capture + musculoskeletal model | Segment orientation of one segment (pitch/roll) | Rough "segment ROM" on exercises where the worn segment moves | Joint angle needs a second segment. Muscle length needs joint angles plus a model. Yaw drift | Per exercise, assumed static other segment | **Not measured**. A ROM proxy is research-only. A-mode sonomyography (v3) is the only path to direct thickness/length [M] |
| Contraction duration & rep tempo | Time per concentric/eccentric phase | Video, encoder, motion capture | EMG burst on/off times; IMU angular velocity | Rep duration (always); phase split (moving-segment exercises only) | Thresholds; static-segment exercises give no IMU phase; eccentric EMG is low | Per-exercise templates | **Inferable after validation** [I; moderate for rep duration] |
| Time under tension | Duration the muscle produces force under load | Force/position trace (encoder + load) | EMG-active duration; IMU motion duration | "Active time" or "set duration" | Electrical activity ≠ mechanical tension (lockout holds, eccentrics) | Per exercise | Inferable **as duration only**. "Tension" wording is unsupported |
| Local muscular fatigue | Reduced force/power capacity of this muscle (peripheral + central) | Pre/post MVC or twitch interpolation; power loss; sEMG spectral compression in isometric holds | Spectral content (MDF/MNF) + amplitude per rep window | Within-set **relative** spectral compression trend | MDF depends on joint angle, velocity, load, recruitment and temperature; electrode shift over the innervation zone; at 500 SPS the sinc3 filter is −3 dB at ~131 Hz (TI_SBAS502C) | Per user/muscle/exercise baseline reps; fixed angular window | **Inferable after substantial validation** [I/M; limited for dynamic gym use] |
| Whole-person fatigue | Systemic/central fatigue, readiness | Questionnaires, HRV, CMJ, MVC batteries, blood markers | Nothing relevant (one muscle, no HR) | Nothing | One peripheral channel cannot see systemic state | n/a | **Unsupported**. Do not imply it |
| Proximity to failure & RIR | Reps remaining before concentric failure at this load | Observed reps to failure; velocity-loss equations (individualised) | EMG features + limb IMU; no load, no bar velocity | Possibly an individual, per-exercise "nearer/further" class | Load and tempo alter the MDF trajectory (Yan2025; SJMSS2021bench); failure definitions vary; RIR self-report error | Several calibration sets to failure per exercise, likely per user | **Research-only** [H; very limited] |
| Contraction velocity & velocity loss | Bar/limb velocity per rep and its decline across a set | LPT (e.g. GymAware), optical, force plate | Limb-segment angular velocity (gyro) where the worn segment moves | Segment velocity loss on compound lifts with a moving worn segment | Segment ≠ bar. Accelerometer-type devices show weaker validity even when bar-mounted (Weakley2021); static-segment exercises give nothing | Per exercise | **Inferable after substantial validation**, restricted exercise list [I; limited] |
| Recovery between sets | Restoration of force/power capacity | Repeat-set performance; MVC/power probes | Elapsed time; EMG only if a probe contraction is made | Time since set end; MDF of a standard probe contraction | MDF recovers within ~1–10 min while amplitude/force may stay altered. MDF recovery ≠ performance readiness | Probe contraction per muscle | Timer: **measured**. "Recovery" estimate: **research-only** [I; limited] |
| Hypertrophy stimulus & long-term growth | Anabolic signalling → CSA/volume change over weeks | Ultrasound/MRI CSA over weeks; biopsies | Nothing about growth | Counts of sets and reps (and at most validated effort) per muscle the band was worn on | Acute EMG ≠ long-term growth (SHARED-STANDARDS rule 4) | n/a | **Unsupported** as a score. Set counts only. Grading of the drivers belongs to A1 |

---

## 2. Audit of the product brief (Task 2)

Classification key: **M** = measured by the hardware as designed. **V** = inferable after validation. **U** = unsupported or contradicted in its stated form.

### 2.1 "What the product is" and the core signal

| # | claim (CLAUDE.md) | class | reason |
|---|---|---|---|
| 1 | "Reads a single muscle" | M (with caveat) | One bipolar channel. Crosstalk from neighbours is likely at 25.4 mm IED with 7 mm studs, so "single" is aspirational |
| 2 | "scores how close a set came to failure" | V | No validated sEMG RIR or failure model was found (A4 search 21; preprints use IMU). Hypothesis H |
| 3 | "counts reps" | V | Plausible from EMG bursts. IMU help depends on the exercise (§1) |
| 4 | "times rest between sets" | M | Elapsed time between detected sets is trivial |
| 5 | "logs a whole training split automatically" | U | One band covers one muscle per session. Nothing identifies the exercise. A whole split needs moving the band plus user tagging, or several bands |
| 6 | "As a muscle fatigues, its fibres conduct more slowly, so the signal's median frequency drops" | V (mechanism M) | CV slowing is one cause of spectral compression. MU synchronisation, recruitment and action-potential shape also contribute. In dynamic exercise, angle, velocity and load shift MDF independently of fatigue [M/I] |
| 7 | "roughly 120 Hz fresh to 90 Hz cooked" | U as a general number | MDF values depend on muscle, IED, subcutaneous fat, electrode type and processing. At the 500 SPS bring-up rate TENSR cannot faithfully show 120 Hz: sinc3 −3 dB at ~131 Hz, Nyquist 250 Hz |
| 8 | "That drop is the fatigue measurement" | V | Within-set relative trend only, after validation |
| 9 | "it is tempo-independent" | **U, contradicted** | Load × tempo interaction on MDF decline at bench press (Yan2025, n=10, abstract). Larger MDF drop at lighter loads (SJMSS2021bench). MDF unrelated to velocity loss (Zhao2025). [I; limited-to-moderate against the claim] |
| 10 | "which is why this beats velocity-based training" | U | No head-to-head evidence. VBT has published RIR equations (GonzalezBadillo2017), though they need individualising (GarciaRamos2018). TENSR has no bar velocity at all |
| 11 | "Amplitude rises at the same time (more fibres recruited for the same load)" | V (mechanism M) | Holds for submaximal sets in the lab (SJMSS2021bench: amplitude higher mid/late set). Amplitude is also driven by contact, sweat, velocity and load, and between-day CV is ~40% even with gel electrodes (Colyer2018) |
| 12 | "the two together are the fatigue score" | V/H | The spectrum + amplitude joint idea exists in the occupational isometric literature (JASA. From memory, UNVERIFIED, for A2 to check). It is not validated for dynamic free-weight sets on dry electrodes |

### 2.2 Features list

| feature | class | reason |
|---|---|---|
| Rep counting | V | Suitable to prototype |
| Fatigue per rep | V | Relative trend only. Needs ≥1 kSPS and a fixed analysis window |
| Rep-of-failure | V | Detecting the failed rep (stall or incomplete ROM) is possible on IMU-moving segments. On static-segment exercises it is EMG-only and weak |
| Reps-in-reserve, live ("about 2 left") | U as stated, research-only | No validated sEMG RIR model was found. A live numeric RIR implies a precision nobody has shown |
| Set score — did this set reach failure | V | Post-hoc classification after substantial validation |
| Rest timer "driven by the muscle's own recovery, not a countdown" | U as stated | Resting muscle gives no spectrum. MDF recovers faster than force capacity (A4 search 17, SECONDARY). Needs a probe contraction and a trial showing benefit |
| Activation percentage — "is the target muscle doing the work" | U | One channel cannot apportion work among synergists. A % needs an MVC denominator per wear and posture |
| Eccentric vs concentric split | V (restricted) | Only where the worn segment moves |
| Weekly volume per muscle | V (counts, with tagging) | — |
| Stimulus per muscle | U | No measure of growth stimulus exists in this hardware or literature |

### 2.3 "Deliberately NOT claimed" and v3

The exclusion list is correct: mass, BP, injury, through-clothing. "Muscle mass tracking" via A-mode sonomyography (v3) is research-only. A single A-mode element measures thickness at one site, which is not muscle volume.

### 2.4 The validation test

"20–30 sets, half to true failure, half stopped 3 short, mixed tempos … separate ~9 times in 10."

- **Underpowered and confounded.** Failure sets are longer and contain more reps than 3-RIR sets at the same load. A classifier, or a human looking at a plot, can separate them on duration or rep count alone without any physiology. The test must compare against that baseline, and against IMU-only features (arXiv2510.03197 found eccentric rep time was its best RPE predictor; preprint).
- **Single person?** The brief does not say. One subject and one session is a feasibility demo, not validation. Use multiple subjects and multiple days, evaluate on held-out subjects, and report sensitivity and specificity with CIs (A5 to specify).
- **End-of-set classification ≠ live RIR.** Passing this test would support the *set score*, not "about 2 left".
- **"True failure" needs an operational definition** (concentric failure observed on video), and the tags must be fixed before the EMG is looked at.

### 2.5 The drop-set test: is "must not reset when the weight changes" expected?

**No — not as a pass criterion.** Four reasons [M/I; limited]:

1. **Amplitude will drop at the weight change.** Lower load recruits fewer and smaller motor units. The amplitude half of the stated composite will therefore make the "fatigue number" look better at each drop, by design.
2. **MDF depends on recruitment.** A lighter load recruits fewer high-threshold, higher-CV units, which by itself lowers MDF. A continued MDF fall after a drop is therefore not proof of tracking fatigue: it may be a load artefact in the direction the test hopes for. "Passes" is not diagnostic.
3. **MDF recovers fast.** Search summaries put recovery at under 1 min to about 10 min (A4 search 17; SECONDARY, UNVERIFIED). With ~10 s strip-time, partial recovery is plausible, which could produce an apparent "reset" in a muscle that is still fatigued.
4. **Load changes velocity and ROM profile**, and those shift MDF (claim 9).

A more informative design compares a probe contraction at a fixed load and posture before the set, after the top set, and after the drop set. The drop set then becomes a stress test of confounds rather than a pass/fail criterion. A5 to decide.

### 2.6 Business-context statements

- "Inara … A$169.99 pre-order, batch 3, trainer-focused" — **UNVERIFIED**. The site was unreachable from here. Search found only an App Store listing, "Inara: Ultimate Gym App" by Inara Technology Inc, with "No Sensor" subscription tiers. That hints a sensor tier exists but confirms nothing about its sensing method.
- Price, cost, break-even and subscription figures are outside the science scope and were not assessed.
- Regulatory language: see section 5.

---

## 3. Feature matrix (Task 3)

Written to `A4-feature-matrix.csv` (DRAFT, first row says so). Summary of recommendations:

| feature | recommendation |
|---|---|
| Rep counting & timing | Suitable to prototype |
| Electrical-activity duration | Suitable to prototype (descriptive) |
| Estimated TUT | Prototype only as "active time / set duration". "Tension" wording is misleading |
| Relative activation trend (within set) | Suitable to prototype |
| Activation % ("doing the work") | Unsupported/misleading in its proposed form |
| Eccentric/concentric split | Potentially useful after substantial validation (moving-segment exercises) |
| Within-set fatigue trend | Potentially useful after substantial validation |
| Proximity to failure / live RIR | Research-only |
| Set score (reached failure?) | Potentially useful after substantial validation |
| Rest timer | Elapsed-time timer: prototype. Recovery-driven: research-only |
| Left/right comparison | Research-only, and impossible with one band |
| Technique / contraction quality | Unsupported in proposed form (narrow IMU ROM-consistency items possible later) |
| Hypertrophy / set-effectiveness / stimulus score | Unsupported/misleading |
| Weekly volume (counts, tagged) | Suitable to prototype |

**Left/right with two bands needs:**
- a shared timebase: BLE timestamp sync to roughly 10 ms is enough to align reps, much tighter is not needed for amplitude or MDF;
- mirrored anatomical placement and orientation, recorded;
- per-side normalisation to a reference contraction;
- matched electrode condition.

Even then, an EMG asymmetry is not a strength or size asymmetry. Skinfold and impedance differ by side.

---

## 4. Hardware and firmware facts that constrain features (Task 4)

All are posed as **questions** for Kye. None is a decision.

**Q1. Sampling rate is internally inconsistent, and at 500 SPS the core feature is compromised.**
- Bring-up §7 uses 500 SPS, gain 6, because those are the datasheet noise conditions.
- The firmware brief says 1–2 kHz. The analysis brief says band-pass 20–450 Hz.
- At 500 SPS, Nyquist is 250 Hz, so a 450 Hz band edge is impossible.
- More importantly, the ADS1292R sinc3 decimation filter is −3 dB at 0.262 × f_DR (TI_SBAS502C, via search summary plus a TI E2E answer): ~131 Hz at 500 SPS, ~262 Hz at 1 kSPS, ~524 Hz at 2 kSPS.
- At 500 SPS the spectrum above ~130 Hz is attenuated, and MDF is biased low and compressed. The analog input filter's 0.042 dB tilt (AFE-DESIGN-REVIEW §3.1) is irrelevant next to this digital roll-off, which the review did not model.
- *Question:* which rate is the measurement rate? Does the noise floor at 2 kSPS (not the datasheet condition) still meet the bring-up step 7 thresholds? Does BLE carry ~48 kbit/s of raw EMG, or are features computed on the device?

**Q2. Which way do the electrodes point relative to the band, and so to the fibres?**
- E1–E3 runs along the 44 mm axis. Nothing records how the puck sits on the band.
- If the band wraps a limb and the pair runs circumferentially, it sits across the fibres of fusiform limb muscles (biceps, triceps, quads, calf). SENIAM places pairs along the fibre direction (Hermens2000, SECONDARY).
- Across-fibre placement changes amplitude, crosstalk and spectral content, and loses the conduction-velocity spatial-filter link MDF relies on.
- For pennate or fan-shaped muscles (deltoid, pec, glute) "fibre direction" differs by region anyway.

**Q3. Inter-electrode distance.**
- 25.4 mm exceeds SENIAM's 20 mm. Larger IED means more crosstalk and more sensitivity to innervation-zone position.
- For an aligned pair, the bipolar spatial filter has its first spectral zero near v/d: about 157 Hz at 4 m/s and 118 Hz at 3 m/s. That sits *inside* the 90–120 Hz band the brief uses. [M; to be confirmed by A3]
- MDF will therefore depend strongly on alignment, on CV and on band slip, not only on fatigue.

**Q4. Dry stainless studs.**
- Impedance is hundreds of kΩ and mismatched between studs, and it changes with sweat across a session. That directly confounds within-set amplitude and spectral trends.
- Mains rejection is the known failure mode (afe-sim-results §1b).
- *Question:* will the snap studs take snap-on gel electrodes for the validation phase? (PROTOCOL §1 lists this as undecided.)

**Q5. The reference electrode sits on the active muscle, 22.6 mm off-axis, driven by the RLD.**
- A driven reference on active muscle is workable for a differential channel.
- But SENIAM-style practice places the reference over electrically inactive tissue.
- *Question:* has its effect on common-mode pickup during contraction been considered, and is it covered in bring-up §8?

**Q6. The IMU is on the puck, so it measures the worn segment, not the bar or the joint.** See §1. *Question:* is the exercise list for IMU-dependent features (phase split, velocity loss, ROM) restricted to exercises where that segment moves?

**Q7. No magnetometer.** Yaw drifts, so heading-dependent segment orientation is unreliable beyond short windows.

**Q8. Possible extra IMU signal.** The LSM6DSO accelerometer can sample far above 100 Hz. Mechanomyography (muscle surface vibration) is a known research signal. *Question (research-only):* worth logging raw accelerometer at high rate during validation sessions?

**Q9. Documentation inconsistencies found while reading. Not edited; reported.**
- `afe-sim-results.md` §1/§1b still analyses C1/C2 = 1 nF.
- `BRING-UP.md` §8 still describes 100 pF as a pending "Kye's call", while §0/§9a and CLAUDE.md say 100 pF is fitted.
- `BRING-UP.md` §7a.3 still says U1.12 is 2.58 mm from its capacitor (now 1.15 mm).
- `BRING-UP.md` §9 repeats the drop-set "must not reset" criterion (see §2.5).

**Q10. Motion artefact.** No firmware exists yet. *Question:* what high-pass corner, and what IMU-gated artefact rejection, will separate band-slip transients from bursts?

---

## 5. Comparable products: claims and evidence (Task 5)

| product | sensing | claims (as found) | independent evidence found | grade |
|---|---|---|---|---|
| **Inara** (AU) | UNVERIFIED | App: AI workout logger and coaching. "No Sensor" tiers imply a sensor product exists | None. Site unreachable; nothing on sensing modality or validation | none |
| **Athos** (MAD Apparel, US) | textile EMG garments, multi-channel | muscle effort/activation, L/R balance | Lynn2018: n=12, isokinetic VL/VM/BF; no significant system effect on rep amplitude; variability 12% vs 10.7%. An undergraduate thesis found significant differences vs Noraxon (not peer-reviewed). Current company status unknown | I; limited (controlled lab, amplitude only) |
| **Myontec Mbody** (FI) | textile EMG shorts | quad/hamstring load, L/R balance | No product-specific validation found in this search. A 2020 review notes scarce independent validation and possible COI bias in supporting papers. Colyer2018 (textile shorts, brand not confirmed): agreement poorer at high amplitude, longer bursts, between-session ARV CV ~41–43% for both systems | I; limited |
| **Strive** (US) | EMG compression shorts + accelerometer | muscle load, fatigue, symmetry; "only platform proven …" (press release) | Saucier2021: 15 NCAA players; position differences only; no criterion validity | very limited |
| **MyoWare** (maker) | single-channel EMG module | not a consumer claim; "not for diagnosis" | Original MyoWare thesis (York U): curls, SNR 10–33 dB, RMS–force correlation. MyoWare 2.0: no validation found, SparkFun paused sales | very limited |
| **WHOOP Strength Trainer** | wrist IMU + biomechanical model | "muscular load"; "97% repeatability" | Company-internal only. Repeatability is not accuracy. "Passive MSK" not publicly validated | H (marketing) |
| **Fort** (YC) | motion + HR band | automatic strength tracking and fatigue | none found | none |
| **Innowearable Inno-X** | thigh EMG + accelerometer band | Eleiko collaboration | none found | none |
| **Delsys Trigno** etc. | research-grade wireless EMG | research instrument | It is the *reference* class TENSR would be validated against, not a competitor | n/a |
| **Vitruve / VBT** | LPT on the bar | velocity, RIR via velocity loss | RuizAlias2024: reliable, but validity criteria unmet for most variables vs GymAware. Weakley2021: LPTs beat accelerometers. VBT RIR equations need individualising (GarciaRamos2018) | I; moderate for LPT reliability |

**Pattern across the field:**
- No consumer EMG wearable found here has published criterion validity for fatigue, RIR or "set quality" during free-weight training. The best validation (Athos) covers amplitude in a dynamometer task.
- Companies publish repeatability (WHOOP) or between-group differences (Strive) and present them as validation.
- That is an opportunity for TENSR to be honest. It also means "beats VBT" would be the claim with the least support in the category.

**Australian regulatory language** (CLAUDE.md, supported by TGA2024 guidance, SECONDARY):
- Consumer fitness tracking is generally excluded from TGA software regulation when it is not intended to detect medical conditions. A tracker that issues health warnings is not excluded.
- Language to keep: fitness, training, effort, reps, sets.
- Language to avoid: injury (including "prevention"), rehab, diagnosis, clinical, "recovery" in a health sense, "readiness" framed as health, imbalance "risk".
- "Muscle recovery" on the rest timer should read as training timing, not tissue healing.
- CLAUDE.md's other items — ACMA/RCM mark, battery labelling, privacy policy, product liability insurance — are outside this agent's evidence scope. They are noted as stated, not verified.

---

## 6. Bottom line for the coordinator

1. **What is defensible to prototype now:** rep counting, set/rep duration, an elapsed-time rest timer, within-set relative amplitude trends, tagged set/rep counts per muscle. These are descriptions of what the device records.
2. **What needs substantial validation first:** a within-set spectral fatigue trend, a post-hoc "reached failure" set score, and phase split / segment velocity loss on a restricted exercise list.
3. **What is research-only:** live RIR, a recovery-driven rest timer, left/right comparison.
4. **What is unsupported or misleading as written:**
   - "tempo-independent";
   - "beats velocity-based training";
   - "activation % / is the target muscle doing the work";
   - "stimulus per muscle" / hypertrophy score;
   - "logs a whole training split automatically";
   - the fixed "120 → 90 Hz" numbers;
   - the drop-set "must not reset" criterion.
5. **Two hardware questions sit upstream of every spectral feature:** the measurement sample rate (Q1: 500 SPS defeats the core feature through the sinc3 roll-off at ~131 Hz) and the electrode orientation relative to the fibres (Q2/Q3). Until both are answered, no MDF number from TENSR can be compared with the literature.

**Confidence in this note:**
- High on repo-derived facts.
- Moderate on the direction of the evidence: external studies were seen only as summaries, and n is small throughout.
- Every external number needs A6 verification against the primary source.
