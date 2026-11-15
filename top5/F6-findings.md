# F6 — Sensing engineering: how TENSR could measure the top-5 hypertrophy factors

Agent F6, 2026-11-02. **Research only.** No hardware or firmware file was edited.

Board facts were read from `hardware/kicad/routed.kicad_pcb` (parsed), `BOM_JLCPCB.csv` and
`docs/AFE-DESIGN-REVIEW.md`. Literature was reached at search-snippet level only: WebFetch to PMC is blocked, see
`F6-searchlog.md`. Studies are in `F6-studies.csv` (46 rows).

**Evidence codes:**
- **D** — direct, on comparable hardware in lifting.
- **I** — indirect.
- **M** — mechanistic.
- **H** — product hypothesis, untested.

Nothing here has run on a TENSR board, because none has been built. So every TENSR-specific performance claim is
**H**.

## Summary

1. **Rest between sets** is the one factor the current board measures outright: set end to next set start, from EMG
   bursts and IMU motion. It needs firmware only.
   - **Recovery** is not measured; rest *duration* is.
2. **Weekly hard-set volume** is half-measurable with no hardware change.
   - Sets and reps are countable on the instrumented muscle (H; no upper-arm/thigh validation exists).
   - **"Hard"** depends on effort, so until effort is solved it rests on a user RIR tag (self-report error ~1 rep,
     Halperin 2022).
3. **Effort / proximity to failure** is not credibly measurable from one dry EMG channel plus a limb IMU.
   - EMG MDF is research-only (science report §5).
   - Arm-worn IMU velocity failed validation against bar transducers (Banyard 2017, PUSH; Orange 2019).
   - The credible route is **bar or implement velocity** with an **individual** RIR–velocity model: Jukic 2024, n=46
     trained, mean error <2 reps on squat. General models fail (RSE 3.4–3.7 reps).
4. **Load / tension progression.**
   - Load is a *log*: user entry, Tier 0/1.
   - Mechanical tension in the muscle is **not measurable** at any tier considered here. FMG needs four bands plus
     isometric calibration (Sakr et al.).
   - A puck clipped to a weight stack identified the load in 97.5% of trials (W8-Scope, n=50; a different device).
5. **Muscle length / ROM.**
   - The single puck sees **its own segment's** pitch/roll only.
     - That is enough for thigh-moving lifts (squat, lunge, RDL) and delt work.
     - It is also enough to classify the **proximal-joint** variant of biarticular exercises: seated vs prone leg curl
       (Maeo 2021), incline vs preacher curl.
   - It is blind on the exercises where the instrumented muscle sits on the *static* segment: curls with a biceps
     puck, leg extension, pushdowns.
   - A second segment fixes that:
     - two-IMU, magnetometer-free knee angle is ~3–5° RMSE (Seel 2014; Sensors 2020; Weygers pipeline 4.1°);
     - elbow is as low as ~2° (Fang 2023 review).
6. **The single most useful addition is a second TENSR puck. The board is unchanged; it needs new firmware modes.**
   - **Bar or dumbbell clip:** velocity, giving effort via an individual RIR–velocity model, load–velocity e1RM, and
     bar displacement as ROM. The precedent is Vmaxpro: ICC 0.91–0.96, LoA <0.12 m/s (Held 2021, n=19 trained).
   - **Weight-stack clip:** the load is identified.
   - **Adjacent-limb strap:** joint angle.
   - The $429 pair price already assumes two pucks.
7. **Phone-camera options:**
   - **Bar-velocity apps are viable.** Qwik VBT ≈ linear transducer; Metric and MyLift weaker and missed up to 30% of
     reps (PLOS ONE 2024).
   - **Pose-estimation ROM is biased at depth**: −5° to −14° knee, viewpoint-dependent. It is fine for full / partial /
     long-partial classes and not for degrees.
   - Propping a phone up for every set is real friction in a commercial gym.
8. **Minimum set for ≥3 of 5 factors measured by a sensor rather than typed in:**
   - (a) Firmware: set and rep detection plus a rest timer (rest, set counts).
   - (b) App: load entry plus exercise→muscle map (load log, volume).
   - (c) A second puck with a bar/stack-clip firmware mode, or a validated camera VBT (effort, load, coarse ROM).
   - **None of (a)–(c) needs a respin.**
9. **Things that need a respin, and none is in the minimum set:**
   - CH2 as a second EMG pair: IN2P/N are tied to 3V3_A and PGA2 is not connected.
   - Bioimpedance: RESP_MODP/N are tied to AVDD.
   - An external magnetometer behind the IMU's sensor hub: LSM6DSO SDx/SCx (U6.2/U6.3) are **grounded**.
   - On-board skin temperature, NIRS, A-mode ultrasound.
10. **J3 (I2C + GPIO2 + GPIO18 + 3V3/GND) takes a daughterboard without a respin.**
    - Candidates: an I2C magnetometer, an FSR on GPIO2's ADC (a band-contact signal-quality gate), or an I2C
      temperature sensor.
    - None of these measures a top-5 factor better than the second puck does. A magnetometer is actively worse near
      steel racks.
    - A-mode cannot measure "stretch under load" as CLAUDE.md claims. It measures **thickness** along one beam, and
      fascicle length needs B-mode imaging.

### Scorecard — best credible measurement per factor

| Factor | Tier 0 (as built) | Best tier that is credible | Evidence for that route | Respin? |
|---|---|---|---|---|
| 1 Effort / proximity to failure | User RIR tag. EMG MDF and concentric-duration slowdown are research-only. | **Tier 1/2: implement velocity + individual RIR–velocity model** | I, moderate (Jukic 2024; Held 2021; PLOS 2024). TENSR-as-bar-clip is H. | No |
| 2 Weekly hard-set volume | Set and rep counts on the instrumented muscle; hard set by user tag | Tier 0 counts + Tier 1/2 effort label | I, limited for on-muscle rep counting (RecoFit, wrist). No upper-arm/thigh study. | No |
| 3 Muscle length / ROM | Worn-segment angle; proximal-joint variant | **Tier 2: second puck on the adjacent segment** (3–5° knee) or Tier 1 camera classes | I, moderate for two-IMU angles (lab/gait); none in lifting | No |
| 4 Load / tension progression | Manual load log | Tier 1 log + Tier 2 stack/bar clip (load ID, e1RM). **Tension: not measurable.** | I, limited (W8-Scope; load–velocity) | No |
| 5 Rest / recovery | **Rest duration measured** (H until rep/set detection is validated) | Tier 0 for duration. Recovery probe = first-rep velocity next set (Tier 1/2). | M/I (velocity after 1 vs 3 min rest) | No |

---

## 1. What the board actually allows — pin-level facts

Read from the routed board, not from the briefs.

| Resource | As built | What it permits without a respin | What needs a respin |
|---|---|---|---|
| **ADS1292R CH1** | E1–E3 differential, E2 = RLD reference | EMG at up to 2 kSPS (DR=100 recommended by the science report) | — |
| **ADS1292R CH2** | IN2N/IN2P (pins 5, 6) → 3V3_A; PGA2N/P (7, 8) not connected | The internal mux can still select the **die-temperature sensor**, test signal or supply check (TI SBAS502C). This is board temperature, not muscle temperature. | A second EMG pair: input network, protection, electrodes and re-done analog layout |
| **ADS1292R respiration** | RESP_MODP/N (31, 32) → AVDD; firmware must never enable it | Nothing | Bioimpedance: excitation 32/64 kHz, 2–10 kΩ range at 30 µA (datasheet) |
| **LSM6DSO (U6)** | I2C at SA0=GND (pin 1). **SDx (2) and SCx (3) to GND**: Mode 1 per datasheet. INT1 → U2.7; INT2 (9) and OCS_Aux (10) unconnected; SDO_Aux (11) and CS (12) → 3V3. | Accel/gyro to 6667 Hz ODR (high-rate accelerometer MMG); FIFO; embedded pedometer/tilt functions | **Sensor-hub Mode 2** (external magnetometer read by the IMU itself). SDx/SCx must become a master I2C bus. |
| **I2C bus** | U2 ↔ U5 DRV2605L, U6 LSM6DSO, J3. Pull-ups R9/R10 = 2.2 kΩ. | Any extra I2C device on J3 (magnetometer, temperature, FSR ADC) whose address does not clash with DRV2605L (0x5A per TI) or LSM6DSO (0x6A with SA0 low) | — |
| **J3** | 1 3V3, 2 GND, 3 SDA, 4 SCL, 5 EXP_GPIO2 (U2.6), 6 EXP_GPIO18 (U2.22); 1.27 mm SMD, top side, 5.8 mm tall | Daughterboard or flex to the band: I2C sensors, an analog FSR divider on GPIO2. GPIO2 should be ESP32-S3 ADC1; **verify against Espressif's table.** GPIO18 is on ADC2. | Anything that must touch skin on the **underside** (NIRS optics, a skin thermistor, ultrasound): J3 is on the top face |
| **ESP32-S3** | BLE 5; module pads 26, 27, 30–41 and 44 unrouted | BLE link to a second puck or to the phone; a BLE-central role is possible (H) | Using the unrouted GPIOs |
| **Electrodes** | 3 dry studs, 25.4 mm IED, fixed triangle | — | More electrodes |

**One consequence matters for factor 3.** CLAUDE.md lists "eccentric vs concentric split" as a feature. That split
needs either the worn segment to move (IMU) or EMG burst shape. EMG is weakest on eccentrics (science report §2).

---

## 2. Tier × factor matrix

Each cell gives:
- what is **measured**, then what is **inferred** from it;
- the **validation** (`F6-studies.csv` key) and evidence code;
- the **feasibility** grade: cost / power / size / firmware effort / gym fit.

The **respin flag** is **R** for "needs a respin" and **—** for "no respin".

| | 1 Effort / proximity to failure | 2 Weekly hard-set volume | 3 Muscle length / ROM | 4 Load / tension progression | 5 Rest / recovery |
|---|---|---|---|---|---|
| **T0 — board + firmware/app + user input** | **Measured:** EMG MDF/amplitude per rep; puck angular velocity; concentric duration per rep. **Inferred:** relative within-set fatigue trend; slowdown. **Validation:** MDF direction I/M, no dry dynamic validation; limb IMU not a bar sensor (Banyard2017, Orange2019); user RIR off by ~1 rep (Halperin2022). **Feasibility:** $0 / existing / existing / high (2 kSPS, phase-locking, SQI) / fair. **—** | **Measured:** reps (EMG bursts + IMU), set boundaries. **Inferred:** sets per instrumented muscle; hard set if user tags RIR ≤ ~3. **Validation:** RecoFit ±1 rep 93% (arm); LEAN 0.92% (wrist); Garmin wrist invalid. Nothing for upper-arm/thigh: H. **Feasibility:** $0 / – / – / medium / good for one muscle; other muscles only if the puck moves or sets are logged. **—** | **Measured:** worn-segment pitch/roll vs gravity. **Inferred:** squat/lunge depth from thigh angle; delt raise arc; proximal-joint variant (seated vs prone curl, incline vs preacher). **Validation:** thigh is the best single site for knee flexion in cutting (R² 0.91, thesis); nothing in lifting: H. **Blind** when the worn segment is static. **Feasibility:** $0 / – / – / medium / good where it applies. **—** | **Measured:** nothing. **Inferred:** nothing. **User-logged:** load, reps → e1RM by formula. **Feasibility:** $0 / – / – / low / fine; typing friction. **—** | **Measured:** time from set end to next set start. **Inferred:** rest duration; prompt via haptic. Recovery: EMG probe contraction (research; spectral and force recovery dissociate). **Validation:** set detection H; rest-duration effect evidence belongs to the factor agents. **Feasibility:** $0 / – / – / low / very good. **—** |
| **T1 — phone camera, manual entry, QR/NFC, VBT integration** | **Measured:** bar velocity (camera VBT) or third-party VBT over BLE/API. **Inferred:** velocity loss; RIR via **individual** RIR–velocity model. **Validation:** Qwik ≈ LPT, Metric/MyLift RMSE up to 0.14 m/s, 9–30% reps missed (PLOS2024_apps); Weakley2021; Jukic2024 (<2 reps, squat); Jukic2023_EJAP (VL% alone >10% error). **I, moderate.** **Feasibility:** $0 HW / phone / – / high (CV) or medium (integration; most VBT protocols closed: H) / poor-fair (phone placement every set). **—** | **Measured:** exercise identity via QR/NFC on the machine (phone reads it). **Inferred:** sets credited to *all* target muscles via an exercise→muscle map, including muscles the puck is not on. **Validation:** none needed for tagging; the map itself is a convention. **Feasibility:** cents per tag / – / – / low / gym must accept tags. **—** | **Measured:** 2D keypoints (MediaPipe/BlazePose); bar displacement. **Inferred:** knee/hip angle at the bottom; full vs partial vs long-partial classes. **Validation:** squat knee bias −13.9° (Panni2026, vs IMU), ICC 0.77 and −5° (Yue_JMIR), CV <10% (Cardiff2024); bar displacement good (Taber2023, n=9). No joint-ROM validation in bench/deadlift. **I, limited.** **Feasibility:** $0 / phone battery / – / high / fair. **—** | **Measured:** entered or QR-defaulted load; plate/pin recognition by camera (patents only; no accuracy data). **Inferred:** load progression; e1RM from load–velocity if VBT is integrated. **Validation:** Weakley2021 for devices; camera plate ID unvalidated. **Feasibility:** $0 / – / – / low (entry) to high (vision) / good for entry. **—** | **Measured:** HR from a paired strap/watch (BLE HRS is a standard profile); next-set first-rep velocity. **Inferred:** systemic recovery (HR); local readiness (velocity). **Validation:** velocity lower after 1 min vs 3–5 min rest (RestSmith2020). HR recovery ↔ local muscle recovery not reviewed. **Feasibility:** $0 / – / – / medium / good if the user owns a strap. **—** |
| **T2 — additions on or around the current product** | **Second puck as bar/dumbbell clip (no respin):** bar velocity by IMU integration with zero-velocity updates. **Validation precedent:** Vmaxpro ICC 0.91–0.96, bias 0.01 m/s (Held2021); −0.021 m/s (OlayaCuartero2022). TENSR's own algorithm: **H** and must be validated against an LPT. **Accel MMG (firmware only):** MMG amplitude ↑ and frequency ↓ to failure (Beck2005; UNL_MMG2016), individual variability large; limb motion swamps MMG: H. **CH2 second EMG pair (R):** orientation redundancy, so a better MDF signal, not a new construct. **Feasibility:** clip ~$45 BOM/puck (CLAUDE.md cost) / one more battery / puck-size / high / good (VBT users already clip). | Second puck on a second muscle doubles the instrumented muscles per session (—). FSR in band via J3/GPIO2 as a contact-quality gate, so fewer junk sets get counted (—; FSR curves vary per unit, per-unit calibration needed). | **Second puck on the adjacent segment (—):** two-segment joint angle, magnetometer-free. **Validation:** knee ~3° (Seel2014), 4.34° (MagFree2020), 4.1° (Weygers_viaReview); elbow ~2° best case, 6–8° in tasks (Fang2023); upper-limb reviews RMSE up to 12.1°. Lab/gait, **not lifting**: I, moderate. **Magnetometer via J3 (—)** or the IMU sensor hub (**R**): indoor and near-steel distortion makes it worse than mag-free methods (MagFree2020; review). Not recommended. **Feasibility:** ~$45 / – / strap / high (joint-axis calibration, BLE time sync) / good. | **Puck on weight stack (—):** load ID 97.5% (W8Scope2020, a different device). **Puck on bar:** load–velocity profile gives e1RM over weeks. **FSR band / FMG:** radial pressure gives isometric force only with four bands + calibration, R² 0.77–0.84 (Sakr_FMG). Not tension, not in lifting. **Bioimpedance (R):** acute swelling; Skulpt has no independent validation found. **Feasibility:** clip ~$45 / – / – / medium-high / good on pin-loaded machines. | Second puck changes nothing new. **Skin temperature (J3 or R):** helps interpret MDF recovery, which is temperature-sensitive (M; not reviewed). |
| **T3 — new sensing** | **NIRS (R; skin side):** SmO2 falls to ~10–46% post-set (MirandaFuentes2021). No SmO2↔RIR link found; SmO2 at failure did not differ by load (ActaBio2022, n=16). Moxy MDC 14–18% SmO2 (Skotzke2024). **I, limited**; fat thickness confounds. **Bar-mounted IMU (commercial):** see T2 precedent. **Load cell:** force directly on cables/machines, giving force-velocity. **Feasibility:** NIRS optics + AFE on the underside, extra mA (est.) / puck redesign / medium / sweat and fat issues. | — | **A-mode ultrasound (R, v3):** muscle **thickness** along one beam. It does not give fascicle length or "stretch": thickness is an indirect, untested proxy for length (H). **Validation:** static A vs B mode, mean diff <0.91 mm, ICC >0.95 (Lee2024_Amode, n=30); wearable prototypes see 0.4–0.8 mm contraction changes, isometric/isotonic only (AlMohimeed2012; CMBES_US). **Feasibility:** 50–100 V pulser, MHz-rate ADC, gel coupling / high power during bursts (est.) / puck redesign / very high / **poor** (gel every session). | **Load cell (inline on a cable or handle):** true external force over time, i.e. impulse/"tension" of the implement, not the muscle. **A-mode thickness** as a slow growth readout: needs ≤~6% error (Soares_RBCDH: B-mode 6.5% vs a 16.6% training effect) and fixed timing to dodge swelling (Lohmann2024). **I, limited; H** for a worn device. | NIRS reoxygenation half-time between sets: a local recovery construct (M); reliability modest (Skotzke2024). |

---

## 3. Factor by factor — what is credible, and why

### 3.1 Effort / proximity to failure

**What is credible.**
- **Implement velocity**, modelled **per person and per exercise**.
  - Individual RIR–velocity fits held to <2 reps at a later session in 46 trained lifters (squat).
  - General equations did not hold (Jukic 2024; Jukic 2023 Physiol Behav: individual RSE ~1.0–1.2 reps vs general
    3.4–3.7).
  - A single velocity-loss % threshold carries >10% error in %reps completed (Jukic 2023 EJAP).
  - The product therefore needs **calibration sets taken to failure**. Intermediate and advanced lifters can do this;
    beginners cannot do it reliably.
- **Bar velocity sources that have been validated:**
  - linear transducers (gold standard, Weakley 2021);
  - Vmaxpro-type bar IMUs (Held 2021);
  - one camera app (Qwik VBT; PLOS ONE 2024).

**What is not credible today.**
- **The puck's own angular velocity.**
  - Arm-worn PUSH was valid only for peak force in squat (Banyard 2017) and biased low on bench (van den Tillaar 2019).
  - A *within-set relative* slowdown of the worn segment on exercises where it moves (squat thigh, raise upper arm) is
    plausible but untested: H.
- **Concentric-phase duration** (EMG burst or IMU).
  - At constant ROM, duration is inversely proportional to mean velocity. So duration growth over a set is a free
    velocity-loss proxy (M).
  - It breaks exactly when lifters shorten ROM near failure.
  - It is worth testing in Stage 2 because it costs nothing.
- **EMG MDF.** Research-only (science report §5). One fusion study (wrist IMU + sEMG, curls) reached 41.4% exact and
  85.9% within ±1 RPE. EMG added only slightly.
- **Accelerometer MMG.**
  - The fatigue direction matches EMG (frequency ↓, amplitude ↑; Beck 2005).
  - It is free in hardware: LSM6DSO up to 6667 Hz ODR.
  - Gross limb acceleration during a rep dwarfs MMG, and inter-individual variability is large. Research arm only.
  - **I2C budget:** 6 B × 6.67 kHz ≈ 40 kB/s, above the ~35–40 kB/s ceiling of 400 kHz I2C once overhead is counted.
    Use 3.33 kHz or the FIFO with batched reads (estimate; check the datasheet).

**Gym fit.** A bar clip is normal kit for intermediate and advanced lifters who already use VBT. A phone on a tripod
every set is not.

### 3.2 Weekly hard-set volume

- **Two parts:**
  - **counting sets** — Tier 0 can, on the instrumented muscle;
  - deciding **which sets are "hard"** — needs factor 1.
- **Whole-split volume needs logging.** One puck sees one muscle. Volume across a split needs either:
  - the app's exercise→muscle map plus logging (QR/NFC on machines lowers friction), or
  - the user moving the puck.
  - The product claim "logs a whole training split automatically" is only true for the muscle being worn.
- **Rep-count validation.**
  - It exists for wrist/forearm: RecoFit ±1 rep in 93% of sets, n=114; Apple Watch app 0.92% error; Garmin wrist not
    valid.
  - **No search found an upper-arm or thigh validation.** Belly-worn counting on static-segment exercises depends on
    EMG bursts alone (O7 in OPEN-QUESTIONS). Stage 2 bench testing has to answer this.
- **Counting junk sets.** Lead-off, sweat and contact loss create false sets. An FSR band-pressure channel on J3/GPIO2
  would be a cheap contact gate (H).

### 3.3 Muscle length / ROM (training at long lengths)

**The structural insight.** Where the puck sits decides what it can see.

| exercise (puck on target muscle) | worn segment | single-puck ROM? |
|---|---|---|
| Squat, lunge, split squat, RDL (quad/glute/hamstring puck on thigh) | thigh moves | **Yes** — thigh pitch is the squat-depth proxy (H; no lifting validation found) |
| Lateral raise, overhead press, fly (delt puck) | upper arm moves | **Yes** — shoulder abduction/flexion arc vs gravity |
| Seated vs prone/lying leg curl (hamstring puck) | thigh static, but its pitch differs between variants | **Variant only** — hip angle tells long vs short (Maeo 2021: seated +14% vs prone +9% volume, untrained, n=20) |
| Incline vs preacher curl (biceps puck) | upper arm static, pitch differs | **Variant only** — shoulder angle; elbow ROM unseen |
| Biceps curl, triceps pushdown, leg extension, calf raise | worn segment static | **No** — needs a second segment |
| Chest press / fly (pec puck) | torso static | **No** |

**Upgrades.**
- **Second puck on the adjacent segment:**
  - magnetometer-free knee 3–5°, elbow ~2–8° in lab work;
  - not validated in loaded lifting;
  - needs a joint-axis calibration motion and BLE time sync between pucks (H; firmware heavy).
- **Phone pose.** Biased at deep flexion — the exact range that matters for "long lengths" — by −5° to −14°. Use it
  for classes, not degrees.
- **Bar displacement.**
  - It comes from the same video, or the same bar clip, as velocity.
  - Vmaxpro displacement bias is 2–3.4 cm, LoA 7.8–10.7 cm.
  - It catches half-reps on barbell lifts.

**Magnetometer.** Not recommended. Mag-free constraint methods match magnetometer pipelines, and magnetometers are
unreliable indoors and near steel (Sensors 2020; review).
- Available without a respin as an I2C part on J3. The IMU sensor-hub route needs a respin because SDx/SCx are
  grounded.

**A-mode.** Measures thickness, not length, so it is not a ROM sensor. The CLAUDE.md phrase "true stretch-under-load"
should read "thickness change under load (an untested proxy)".

### 3.4 Load / mechanical tension and its progression

- **Mechanical tension in the muscle is not measurable** with anything in Tiers 0–3 as scoped:
  - EMG ≠ force (science report §2);
  - FMG needs multi-band isometric calibration;
  - A-mode thickness ≠ force.
- **What can be tracked is the external load and its trend:**
  - **logged load** — Tier 0/1; QR/NFC can pre-fill the machine;
  - **load identification on pin-loaded stacks** with a clipped IMU — W8-Scope 97.5%, n=50, a different device, so H
    for TENSR;
  - **e1RM over weeks** from a load–velocity profile (bar clip or camera VBT) — this is the honest "progression"
    metric;
  - **inline load cell** — Tier 3; force on cables/handles; useful mostly for cable work.
- **Gym fit.** Manual entry is what serious lifters already do in apps. Automatic load ID only pays where entry is the
  friction.

### 3.5 Rest between sets / recovery

- **Rest duration**
  - Tier 0, measured directly once set detection is validated; firmware only.
  - A haptic cue at a chosen rest length is trivial (DRV2605L is on board).
  - This is the most defensible factor TENSR can track.
- **Recovery** is a different construct:
  - **local:** next-set first-rep velocity — 1-min rest left velocity lower than 3–5 min, Smith machine, non-failure;
  - **systemic:** HR from a paired strap (BLE Heart Rate Profile; Tier 1).
  - The current "rest timer driven by the muscle's own recovery" claim (CLAUDE.md) is research-only: spectral and
    force recovery dissociate (science report §2).

---

## 4. Minimum set of additions to credibly track ≥3 of the 5 factors

**Level A — "tracked", no hardware at all (firmware + app):**
1. Firmware set and rep detection from EMG bursts + IMU; rest timer with a haptic cue.
2. App: exercise picker with exercise→muscle map (QR/NFC optional), load entry, end-of-set RIR tag.

This gives:
- **Rest (5)** — measured;
- **Volume (2)** — counted on the worn muscle, logged for the others; "hard" by self-report;
- **Load (4)** — logged.

That is 3 of 5, but only rest is *sensed*. Honestly, this is a logging app with automatic rep, set and rest detection.

**Level B — 3+ factors *sensed* — recommended minimum. No respin.**

3. **A second TENSR puck plus a clip/strap accessory, with firmware modes:**
   - **bar/dumbbell mode** — velocity, rep, displacement;
   - **stack mode** — load ID;
   - **segment mode** — joint angle with the first puck.
4. **App: individual RIR–velocity calibration** — a few sets to failure per exercise, Jukic 2024 method.

This adds:
- **Effort (1)** — sensed via velocity; the precedent is validated; TENSR's own algorithm is H;
- **Load progression (4)** — sensed via e1RM or stack ID;
- **ROM (3)** — sensed via bar displacement or joint angle;
- **Volume (2)** — becomes "hard-set" volume.

The result is **4–5 factors sensed**, one exercise at a time, depending on where the second puck goes.

**Alternative to item 3, zero hardware:** a camera VBT feature, or integration with an existing VBT app/device.
- Validity varies by app (only Qwik matched an LPT in one study, and versions change).
- Highest friction in a real gym.

**What would make Level B fail:**
- no in-house validation of TENSR's bar-velocity algorithm against an LPT. Weakley 2021 shows many commercial IMUs fail
  this.
- users who will not do calibration sets to failure;
- BLE sync between two pucks and the phone.

**Respin is not needed for Level A or B.** It is only worth considering for:
- CH2 orientation redundancy, which addresses K2 (orientation unknown) and improves EMG quality, not factor coverage;
- v3 A-mode thickness as a growth readout.

### Respin vs no-respin, item by item

| Addition | Factors helped | Respin? | Why |
|---|---|---|---|
| 2 kSPS EMG, set/rep detection, rest timer, concentric-duration slowdown | 1 (research), 2, 5 | **No** | firmware |
| ADS1292R die temperature via CH2 mux | MDF interpretation only | **No** | internal mux; but it reads board, not muscle, temperature |
| High-ODR accelerometer MMG | 1 (research) | **No** | LSM6DSO 6667 Hz; I2C budget limits the rate |
| Second puck: bar / stack / segment modes | 1, 3, 4 (+2) | **No** | same board; new firmware + accessory |
| Phone camera VBT / pose; QR/NFC; BLE HR strap | 1, 3, 4, 2, 5 | **No** | app |
| I2C magnetometer on J3 | 3 (marginal, likely negative) | **No** | J3 has SDA/SCL/3V3/GND; check address clash with 0x5A/0x6A |
| Magnetometer behind LSM6DSO sensor hub | 3 | **Yes** | U6.2 SDx / U6.3 SCx are grounded (Mode 1) |
| FSR band-pressure via J3 GPIO2 (ADC) | SQI for 2; FMG weak for 4 | **No** | divider on a daughterboard; verify GPIO2 = ADC1 |
| Skin temperature | MDF context | **J3: no** (top side; flex to skin); **on-board near a stud: yes** | — |
| CH2 second EMG pair / orthogonal pair | 1 robustness | **Yes** | IN2P/N → 3V3_A, PGA2 NC, electrodes fixed; analog layout redo |
| Bioimpedance (ADS1292R respiration or AD5940-class) | none of the 5 directly | **Yes** | RESP_MODP/N tied to AVDD |
| NIRS | 1, 5 (weak) | **Yes** | skin-side optics on the underside |
| A-mode ultrasound | growth readout; not ROM | **Yes (v3)** | pulser, ADC, transducer, gel |
| Inline load cell | 4 | separate device | — |

---

## 5. Striking claims, fact-checked

| Claim | Check | Verdict |
|---|---|---|
| "A-mode sonomyography is the only non-imaging way to get true stretch-under-load" (CLAUDE.md v3) | A-mode returns echo depth along one beam: thickness. Fascicle length needs B-mode imaging or a model. Wearable A-mode is shown only in isometric/isotonic bench tests (0.4–0.8 mm changes). | **Overstated.** Thickness is plausible; "stretch" is H. |
| Two IMUs give accurate joint angles | Knee 3–5° mag-free in lab/gait; elbow ~2° best case, up to 12° across reviews | **Supported in the lab; untested in loaded lifting** |
| Phone pose estimation is accurate for ROM | Bias −5° to −14° at deep knee flexion, viewpoint-dependent; no bench/deadlift joint-ROM validation | **Coarse classes only** |
| Wearable IMUs measure bar velocity | Bar-mounted Vmaxpro valid (n=19 trained); arm-worn PUSH not | **Only if mounted on the implement** |
| Velocity loss tells you RIR | Group level yes (Sánchez-Medina 2011); individual models <2 reps; general models and single VL% thresholds poor | **Individual calibration required** |
| NIRS shows proximity to failure | SmO2 drops in sets; no RIR link; MDC 14–18% | **Unsupported for RIR** |
| Camera recognises plates/pins | Patents only; one hobby project reports frequent failure | **Unvalidated** |
| Skulpt-type local bioimpedance measures muscle quality | No independent validation found (Longo 2021 exists, results unseen) | **Unverified** |

---

## 6. Open questions this agent could not close

- LSM6DSO full ODR/bandwidth/current table (DS12140). Was 0.55 mA the combo HP figure? Accelerometer current at
  6667 Hz?
- ESP32-S3: GPIO2 = ADC1_CH1 and GPIO18 = ADC2_CH7 is from memory of Espressif's table. Verify. Also ADC2 co-existence
  with BLE on the S3.
- DRV2605L I2C address 0x5A, from memory of TI. Check before choosing a J3 sensor.
- No validation exists for upper-arm/thigh rep counting, thigh-only squat depth, two-IMU curl elbow angle, or pose ROM
  in barbell lifts. Each is a Stage 2/3 bench test, not a literature question.
- Whether TENSR's LSM6DSO range settings are enough for a bar clip (±16 g, ±2000 dps are the LSM6DSO maxima per its
  family spec; confirm). Whether the clip mass and attachment add error.
- Exact authors and years for several search-only rows (marked in `F6-studies.csv`).
