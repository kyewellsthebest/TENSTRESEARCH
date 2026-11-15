# XA — Independent audit of the failure / effort-tracking round (X1–X4)

Agent XA, 2026-11-03. This is an adversarial audit of X1–X4, using the method of `../top5/FA-audit.md`. Every verdict
comes from my own searches (`XA-searchlog.md`, 59 WebSearch calls) or my own arithmetic. Corrected and new rows are
in `XA-studies.csv`.

Kye's framing is taken as given: tracking proximity to failure means tracking effort, and effort is the feature. My
job is to make sure that what gets built and claimed is true.

## Bottom line

- **No load-bearing citation is fabricated.** Every named study exists, and every headline direction matches.
- **Three Jukic papers are one dataset.** EJAP 2023, Physiol Behav 2023 and Physiol Rep 2024 all use the same 46
  lifters (15 F / 31 M), doing a 1RM test and two RTF tests 72 h apart, on the back squat. The round counts them as
  convergent evidence. They are one experiment analysed three ways. Velocity-RIR at the individual level has **one**
  free-weight replication (Janicijevic 2024, Smith squat, wrestlers), not three.
- **X4's light-load hard-set rule has no evidence at its precision.** The rule sets the band to 1 RIR when N > 15 or
  load < 60%. In Lasevicius 2022, the non-failure arms stopped at about 57% (low load) and 54% (high load) of
  failure reps. That is about 15 and 5–6 RIR, not 2–3. The study shows that far-from-failure is bad at light loads.
  It says nothing about 1 vs 3 RIR.
- **X4's safety argument has a hole.** X4 says a cue that only says "you've arrived" "cannot push a user past their
  intent". That is false once users learn to wait for the buzz. A late or withheld cue then means "keep going". X4's
  own targets allow 5% late cues and up to 20% withheld sets.
- **The round is too pessimistic in one place that matters.** "No sensor beats the lifter" is only established near
  failure on heavy sets. Far from failure, humans are bad:
  - Coaches watching video were off by **4.8 reps** at a third of the way into ~14-rep sets (Emanuel 2022).
  - Self-report error grows with reps per set at 5 and 3 RIR, but not at 1 RIR (Zourdos 2021).

  The useful boundary for effort tracking is "hard (≤ 3 RIR) vs not hard". That is where humans err most, and it
  is where the product should aim first.
- **The round is too optimistic in two places.**
  1. **Stall detection.** X4.C5 targets ≥ 90% sensitivity on moving-segment lifts and ≥ 75% on static ones. No
     published failed-rep detector exists for a limb- or muscle-worn sensor.
  2. **Auto-labelled failure sets.** If a set the lifter *stopped* gets labelled as failure, the model learns the
     very ~1-rep underprediction bias the device is meant to correct.
- **X4's arithmetic is correct**: the fusion maths, the FFT cycles, BLE bandwidth and ODRs. Its "0.7–1.1 reps
  day-to-day" figure is real (Mitter 2022 PLOS ONE). That figure is a lab floor, not gym variability.

---

## 0. Access

- **WebFetch re-test, 2026-11-03.** Five attempts, all `getaddrinfo ENOTFOUND`:
  - arxiv.org (King 2025 and Thomas 2025 abstract pages);
  - pmc.ncbi.nlm.nih.gov;
  - bytez.com (an arXiv mirror);
  - www.researchgate.net.

  Fetch is blocked at DNS. **arxiv.org and pmc.ncbi.nlm.nih.gov have to be allowed in the session's network settings**
  before anyone can read King 2025's or Thomas 2025's validation split. Nobody in this round, me included, has read
  either.
- **Access level.** Everything below is at abstract or search-summary level. VERIFIED means the bibliographic details
  and headline numbers match an independent record. It does not mean the methods were checked.

## 1. Citation verification

Verdicts: **V** verified · **P** partly (difference stated) · **U** unverifiable (reason) · **W** wrong.

### 1a. Velocity / bar-based

| item | verdict | what I found / what differs |
|---|---|---|
| Rodríguez-Rosell 2020 | **V** | JSCR 34(9):2537–2547, DOI 10.1519/JSC.0000000000002881. n=20 men. VL vs % reps done: R² 0.97 (BP), 0.93 (SQ). **Do not mix it up with** the r 0.97 / 0.99 between VL and acute fatigue in the same abstract. That is a different relation. |
| Jukic 2023 EJAP | **V** | EJAP 123(6):1343–1357. 46 trained (15F/31M), free-weight back squat, 1RM + 2 RTF tests 72 h apart. Agreement unacceptable; errors >10%. **Same cohort as the next two.** |
| Jukic 2023 Physiol Behav | **V** | 265:114158. Held-out mean error **1.96 vs 2.81 reps** (individual vs general). Fit R² 0.98 vs 0.45–0.49. RSE 1.01–1.15 vs 3.44–3.66. X3's correction of F6 (use 1.96/2.81, not the RSE) is right. |
| Jukic 2024 Physiol Rep | **P** | e15955. 46 (15F/31M), free-weight back squat. **Same 1RM + 2×RTF-72 h design, so the same cohort.** The error is stated only as "mean error < 2 reps" for individual models; general models did not meet that. **"< 2" is a threshold, not a measured MAE.** X4.C7 benchmarks against it as if it were a number. The real value is unseen. |
| García-Ramos 2020 (n=96) | **V** | PeerJ 8:e8760. 96 "healthy men" (not stated as trained). Smith bench, paused and touch-and-go. Sets to failure at 75–90%. Vlast CV >18.3%, ICC <0.60. r(V1RM, Vlast) 0.18 / 0.37. |
| Mansfield 2023 | **V** | EJSS. Recreationally active (n=20 per one later summary). Bench and prone row at 60/80%, LPT. 30.9% of reps right; 69.1% wrong. Velocity drifts 0.019–0.027 m/s between sets. Exact-class criterion. |
| Qin 2025 | **V** | BMC SSMR 17:60. 19 men described as "physically active" but **with ≥2 y of RT**; X3's "active men" undersells them. Smith bench 60/80%. AE **1.3 ± 0.7** reps, deviation −0.4 to +0.6. **Design:** stop at an intended 2 or 4 RIR, then go to failure. That is a prescription test, not RIR estimation through a set. |
| Janicijevic 2024 | **V** | EJSS 24(3):364–371. 30 wrestlers, Smith squat. AE 1.1–1.7 (general) vs 1.2–1.8 (individual); r² 0.838 vs 0.957. Not worse under fatigue. |
| "Sports Engineering 2024" encoder | **P → resolved** | **Külkamp W, Kons R, de Souza J, Kunzler DH, Bishop C.** Sports Eng 27(1), DOI 10.1007/s12283-024-00450-y. 57 men. Lat pulldown, **knee extension**, bench, at **self-selected velocity**. ICC 0.88 (0.83–0.91). I did not see ">90% of sets within 2 reps"; it is X2/X4's secondary figure. X2 left this unresolved; X4 had it. |
| Morán-Navarro 2019 | **P** | JSCR 33(6):1496–1504. 30 men (novice, well trained, highly trained). Velocity CV 4.4–8.0%. No training-level difference. **Exercise list not confirmed** (one summary names bench, squat, prone pull, shoulder press). The authors' "substantial improvement over perceived exertion" was **not tested head-to-head** in anything I saw. Do not repeat it as a finding. |
| Miras-Moreno 2023 | **X3 V / X2 U** | Heliyon 9(9). 23 resistance-trained males, Smith vs free prone bench pull. Errors similar across methods. **All RTF–velocity relations overestimated RTF under fatigue**: in later sets they say more reps are left than really are. X2's "SEE ≈ 5.4 / 6.6 reps" is not in the abstract: UNVERIFIABLE. The fatigue overestimate matters for a multi-set gym product, and no agent flagged it. |
| Banyard 2017 | **V** | IJSPP 12(9):1170–1176. 10 strength-trained men, free-weight squat 20–100%. PUSH valid only for peak force; GymAware highly valid. |
| Orange 2019 | **P** | JSCR 33(9):2398–2408. **29 youth rugby league players (18 y).** PUSH valid and reliable only for squat MP and PP at **20%**, and bench MP at 40%. X3 gives only the bench 40% part. The conclusion is unchanged. |
| Apple Watch (Achermann 2023) | **V** | *Sports* (MDPI) 11(7), not Frontiers. n=22 recreational lifters with ≥3 y of squatting, vs Vicon. Wrist r 0.952–0.965, SEE 0.064 m/s; bar-mounted r 0.971–0.979, SEE 0.049. |

### 1b. EMG / physiology

| item | verdict | what I found / what differs |
|---|---|---|
| Sundstrup 2012 | **V** | JSCR 26(7):1897–1903. 15 untrained women, elastic lateral raise, 3RM vs ~15RM to failure. Plateau 3–5 reps from failure. X1's grading (H for TENSR) stands. |
| Looney 2016 | **V, caveat** | JSCR 30(3):792–799. **10 trained men**, squat. **Design: a drop set, 90 → 70 → 50% to failure with no rest**, plus a 50% single set. Peak EMG at 90% > all others. The "light-load failure shows lower EMG" contrast is partly a drop-set artefact: the 50% set began already fatigued. |
| Benitez 2023 EJAP | **V** | 123(10):2145–2156. EMG amplitude rose at 30% and did not change at 80%. MPF fell at every load and action. **Contradiction X1 missed:** the companion JSCR 2023 paper from the same group found **final-rep EMG amplitude did not differ between 30 and 80%**. X1's "EMG amplitude at failure is load-dependent" is therefore mixed evidence, not settled. |
| Martinez-Valdes 2020 | **V** | J Neurophysiol, DOI 10.1152/jn.00447.2020. Isometric. Discharge rates fell to ~40% of endurance time, then rose. At failure they stayed below fresh 50% MVC rates. |
| Dideriksen 2011 | **V** | J Appl Physiol 111(2):485–494. Model. Cancellation ~40% and constant. Reduced synaptic input is the main constraint. |
| Allen 2008 | **P** | Physiol Rev 88:287–332. Pi and impaired SR Ca²⁺ release are favoured. The exact "limited importance" wording was not seen. **X1's "lactic acid claim not supported" is too strong for dynamic lifting.** Allen & Trajanovska 2012 say acidosis *does* reduce shortening velocity and power at body temperature, and the Fitts 2016 vs Westerblad 2016 exchange shows the debate is open. Velocity is what a set loses. |
| de Morree 2012 | **V, scope** | Psychophysiology 49(9):1242–1253. 16 recreationally active men, elbow flexion at **20% and 35% 1RM**, fresh vs fatigued arm. It shows RPE tracks motor command. It does **not** show that effort sense tracks proximity to failure. X1's "that is why the lifter's own effort sense tracks failure approach" is an inference. |
| Steele 2017 | **P** | Muscle Nerve 56(3):368–374, PMID 28044366. The MF wording was not seen. X1 already flags this. |
| González-Izal 2010 | **V** | JEK 20(6):1097–1106. 15 trained, 5×10 leg press, VM. R² 46.6% single index; 49.8% FInsm5 + MAV. Not to failure. |
| González-Izal 2011 | **V (content) / P (author)** | MSSE 43(2):303–311. 12 trained. After training, the sEMG–power-loss models "may fail"; metabolite models held. One summary lists Izquierdo as first author. Check the author order before citing. |

### 1c. Wearable / ML

| item | verdict | what I found / what differs |
|---|---|---|
| King 2025 (arXiv 2512.11854) | **P** | Authors, ICMLA 2025, n=13, 631 reps, preacher curl, wrist 6-axis IMU, RIR ≤ 2 from momentary failure. **Segmentation F1 0.83, near-failure F1 0.82** at 1.6 Hz; that settles X2's "which is which". **The split design is still unknown** after 4 searches and a blocked fetch. **Every set went to failure**, so the model never saw a slow rep that was *not* near failure. No baseline seen. |
| Thomas & Wahlström 2025 (arXiv 2510.03197) | **P** | James Thomas & Johan Wahlström. **5 men** (confirmed), 18–25, ≥2 y RT. Delsys Trigno IMU 370 Hz + EMG 2148 Hz. Single-arm DB curl, verbal CR10 after every rep. 69 sets, >1000 reps. 41.4% exact, 85.9% ±1. **EMG role:** one summary says EMG was used **only in training**, compressed into label representations, with **IMU-only at test time**. Another says "adding EMG slightly improved accuracy". Both can be true: the gain may come from EMG-shaped labels. **Either way, there is no evidence that EMG at inference adds anything.** Split not found. |
| Baek 2025 | **P** | Sensors 25:6588. 32 men / 64 limbs, **7 sets at 7RM**, robotic isokinetic bench, load cell, RPE labels. ">93% within ±1" and the split were not seen. |
| Elshafei 2021 | **V** | Sensors 21(3):759. 98% subject-specific vs 88% cross-subject. 20 volunteers, ~3000 curls (from the companion paper). Borg labels. The protocol behind the 88% was not seen. |
| PERSIST (Albert 2022) | **V** | Data 8(1):9. 12 men with ≥1 y RT. IMU, ECG and Azure Kinect, flywheel squat, Borg 6–20. RPE, not RIR. |

### 1d. Human benchmark

| item | verdict | what I found / what differs |
|---|---|---|
| Halperin 2022 | **V** | **Sports Med** 52(2):377–390. 414 participants, 12 studies, 262 effects. Underprediction 0.95 (0.17–1.73). Between-participant SD 1.45 (0.99–2.12). I² 97.9%. Better closer to failure and with fewer reps. **Training status was not a meaningful moderator.** That cuts against X4's hope that trained lifters are much better. |
| Armes "preprint" (2.02) | **P** | It is published: Front Psychol 2020 (X1 has this right; X2 calls it a preprint). ≥1 y RT. **Knee extension**; experiment 2 at 70% of isometric MVC. 2.02 (95% CI **0.0**–4.04). X2's "trained lifters underpredict 2.02 reps" generalises one isolation machine and a load set from MVC to all trained lifting. Quote it as "knee extension, CI touching zero". |
| Refalo 2024 JSCR (0.65 ± 0.78) | **P** | The title is confirmed. 24 (12M/12F), bench at 75%. **0.65 ± 0.78 is still from one secondary source**: Marzagao 2026 (arXiv 2603.17495, Fitbod). If it is true, it is the **best case for humans**: heavy bench, trained, intraset, near failure. It must not be generalised to light or isolation sets. |

### 1e. Seeded random sample: 10 rows

The pool was rows from X1–X4 not named in the task (79 of 145). `random.seed(20261103)`, then `random.sample(pool, 10)`.

| row | verdict | note |
|---|---|---|
| X1 Gungor2024 | **V** | J Clin Med 13(8):2296. 16 trained men, 40/60/80% to failure. RMSSD lower after 80%. |
| X2 PLOS2022_TCN | **V** (exists) | Mu, PLOS ONE 2022, biceps, 20-min cycle. X2's "not retrieved" is honest. Irrelevant to lifting. |
| X2 Jin2025 | **P** | r 0.85 ± 0.15, n=8, but **only with electrical stimulation** on an isokinetic dynamometer (IEEE TNSRE 2025 version). X2 omitted the stimulation. TENSR cannot stimulate, so this does not transfer to v3 sonomyography as stated. |
| X4 Morris2014 | **V** | RecoFit, CHI 2014. ±1 rep 93% of the time, 114 participants, forearm. |
| X2 MirasMoreno2023 | **U** | X2's SEE 5.4/6.6 is not in the abstract. See 1a. |
| X2 Hwang2025 | **V** | Sensors 25:3309. Gait after step exercise, LOSO 87.94%. The abstract is ambiguous about which configuration. Not lifting, which X2 said. |
| X1 BenchPower2007 | **V, add n** | PMID 17530976, optical-encoder validation. **n=7**, 4×6 at 85–95% 6RM, so not strictly to failure. Peak power −55% in the final 2 reps. |
| X4 DuffeyChallis | **P** | JSCR 21(2):556–560 per Penn State (one citer gives J Hum Kinet). A citing paper reports mean concentric velocity **−40%** and peak −28%. With bar travel near constant, −40% velocity means lift time **×1.67**, not "more than doubled". X4's F1 rationale overstates it. |
| X2 AppleGarmin | **V** | Still no shipping RIR or failure estimate from Apple, Garmin or WHOOP as of today. New: WHOOP was reported (the5krunner, 2026-10-29, unconfirmed) to have bought Motra, an Apple Watch rep-counting app. That is rep counting, not effort. |
| X4 Tremor_fatigue | **P** | Glasgow 184542 is Aljihmani 2019: n=15, accelerometer, 8–14 Hz tremor more visible under fatigue. That is **not resistance sets**. "Training phase did not change the rise" was not found. |

Sample result: 5 V, 4 P, 1 U, 0 W. No fabrication. The P rows all lose a qualifier (stimulation, n, design or a number)
in the direction that flatters the signal.

## 2. X4: arithmetic and design claims

| claim | check | verdict |
|---|---|---|
| Fusion: σs 1.0, σx 1.5, ρ 0.5 → 0.98 | Min-variance fusion of two correlated unbiased estimates. Recomputed all six rows: 0.625, 0.799, 0.866, 0.982, 1.043, 0.823; MAE = 0.798 × SD. | **Correct.** Add three facts. (1) At σs = 1.0 and σx = 1.5 the sensor's weight hits **zero at ρ = 0.67**; with ρ = 0.5 its weight is 0.14. (2) Weights estimated from small calibration sets lose more than this ideal. (3) **Fusion needs the lifter's tag on every set.** That contradicts "logging without typing". With no tag, the sensor competes only with history (B1). |
| 1024-pt FFT ≈ 98k cycles ≈ 0.4 ms | ESP-DSP table: `dsps_fft2r_fc32` 1024 complex, **97,847 cycles on ESP32-S3**, i.e. 0.408 ms at 240 MHz. An ESP-DSP example README shows 140,472 cycles in another configuration (0.59 ms). Bit reversal and windowing are extra. | **Correct.** Still ≪ 1 ms per rep. ESP32-S3 dual-core LX7 at 240 MHz: correct. |
| BLE research stream ≈ 11 kB/s | 2000 × 3 B + 416 × 12 B = 10,992 B/s ≈ 88 kbit/s | **Correct.** "Needs 2M PHY" is over-cautious: 1M PHY with DLE carries it. The phone's connection interval is the real limit, and A4 tests it. The ~40 B per-rep record budget adds up (~35 B by field). |
| Latency 0.2–0.4 s | Rep-end detection dominates; compute < 5 ms; ERM start tens of ms | **Plausible.** Note: at 2 s/rep the lifter is starting the next rep when the buzz arrives. |
| ADS1292R 2 kSPS, −3 dB ≈ 524 Hz | DR[2:0] = 100b → 2 kSPS; sinc3 −3 dB ≈ 0.262 × f_DR | **Correct.** |
| LSM6DSO 416 Hz; MMG at 1.66–3.33 kHz | The ODR ladder is 12.5 … 416(417), 833, 1666, 3333, 6666 Hz for accel and gyro | **Valid ODRs.** F6's I2C budget was not re-checked. |
| "Day-to-day reps-to-failure 0.7–1.1 reps" | **Source found: Mitter et al. 2022, PLOS ONE (e0268074).** 24 trained, free-weight bench, two sessions 1 week apart. SEM **0.7** reps at 90% (0.5–0.9), **1.1** at 70% (0.8–1.4). | **Verified, scope narrow.** These are fresh first sets in a lab, on bench only. In a gym, with prior sets, variable rest and sleep, the spread is larger (Miras-Moreno: velocity relations overestimate RTF under fatigue). It is a **floor**. It also means a perfect history model is already about **0.55–0.9 reps MAE on a fresh first set**. X4.C2 (sensor beats history by ≥ 0.3) may fail on first sets and pass only on later ones. **Report X4.C2 by set number.** |
| Hard-set band: 3 default, 1 if N > 15 or < 60% | Lasevicius 2022 (JSCR 36(2):346–351, untrained knee extension): reps/set at failure vs non-failure were 34.4 vs 19.6 (low load) and 12.4 vs 6.7 (high load). The non-failure arms stopped about 15 and about 5–6 reps short. | **Band 3: a defensible product rule.** **Band 1: not supported.** The evidence says "far from failure is bad at light loads", not "3 RIR is not enough". Ship band 3 everywhere. Show a light-load *note*, not a different threshold, until there are data. |
| "A one-directional cue cannot push a user past intent" | Logic | **Wrong.** If users wait for the buzz, a late or withheld cue is a "keep going" signal. X4.C6 allows ≤ 5% late cues. Stage B allows ≤ 20% withheld sets, so up to 1 set in 5 has no cue at all. **Fixes:** (a) the UI must say "no buzz ≠ keep going"; (b) Stage E must measure overshoot on sets where the cue is withheld or late; (c) the "safeties set" toggle is a self-declaration, so call it that. |
| Haptic blanking 100 ms | No source found on DRV2605L/ERM coupling into dry EMG. Mechanism (M): an ERM coin motor's vibration sits inside the 20–450 Hz EMG band (frequency is my estimate, not sourced), so a notch cannot remove it. The puck carries electrodes and motor together. Motor current transients share rails with the AFE, and U5.1's REG cap sits 5.36 mm away (an accepted deviation in CLAUDE.md). | **Plausible risk, correctly sent to bench test A2.** Two changes. (1) Blank from the DRV2605L GO bit until the effect ends **plus braking plus settle**, not a fixed 100 ms; a double pulse likely runs past 100 ms. (2) **Blank the IMU features too.** The motor shakes the gyro and accelerometer on the same puck. X4 blanks only EMG. Cost is near zero, because the cue fires at rep end. |
| "Stall sensitivity ≥ 90% (moving), ≥ 75% (static)" | No published failed-rep detector for a limb- or muscle-worn sensor was found (search 55). Rum 2022 is a bar IMU detecting sticking points, not failures. | **These are targets with no precedent.** The static class rests on EMG burst length alone. Label them guesses. |

## 3. Challenging the headline conclusions

### 3a. Where the round is too pessimistic

1. **"No sensor beats a bias-corrected lifter" holds only near failure.** Evidence that humans are much worse far from
   failure:
   - Emanuel 2022: 259 coaches, video. Absolute error **4.8 / 2.0 / 1.2 reps** at 33 / 66 / 90% of a set averaging
     13.9 reps. They **underestimate early** and slightly overestimate late.
   - Zourdos 2021 (JSCR 35 Suppl 1:S158, 70% squat): error grows with total reps at a called 5 RIR (r 0.65) and
     3 RIR (r 0.56). It does not at 1 RIR. Training age did not help.
   - Halperin 2022: worse further from failure and above ~12 reps. Training status not a moderator.
   - Casanova 2025: 1 RIR is more accurate than 3 RIR; 75% is more accurate than lighter loads.

   The commonest real-gym effort error is a set ended at 4–6 RIR that the lifter believed was 1–2. **Calling that set
   "not hard" is an easier problem than RIR estimation.** It is binary, and the true margin is large. Humans are
   worst exactly there. No study has tested a sensor on it head-to-head (search 58 found none). So it is **open, not
   lost**. The round should say "unknown", not "no better than the lifter".
2. **"Every VBT study used maximal intended velocity" (X3 §6) is wrong.** Külkamp 2024 used **self-selected velocity**
   and got ICC 0.88 for maximum reps.
3. **"No VL→RIR validation on isolation lifts" (X3 summary 6) is too strong.** Külkamp 2024 included **knee
   extension**, slightly worse than bench and pulldown. The WKU thesis (in X2) has curl and leg-extension data. Thin,
   but not none. X3 and X2 contradict each other here.
4. **History priors have industrial-scale precedent.** Marzagao 2026 (arXiv, Fitbod) fitted load × reps on **303,494
   near-failure sets from 14,966 users across 388 exercises**, with user-level CV. A population load→N prior (X4's B0)
   for most gym exercises is therefore buildable from logs. The author also warns that "near failure" is often
   violated in unsupervised logs.

### 3b. Where the round is too optimistic

1. **Jukic ×3 = one cohort.** See the bottom line. Treat individual velocity-RIR as "one squat cohort plus one Smith
   cohort".
2. **The "< 2 reps" yardstick is a bound, not a value.** X4.C7 benchmarks against a number nobody in this round has
   seen.
3. **Auto-anchors inherit the human bias.** X4's calibration uses "natural failure sets" confirmed by one tap.
   - Steele 2017 and Halperin separate volitional from momentary failure.
   - Lifters underpredict by about 1 rep. A set the lifter *racked* believing it was failure is often 1–2 reps short.
   - Labelled N = k, it teaches the model the bias the device exists to remove.

   **Rule: only a detected failed concentric is an anchor. A racked set with every rep completed is censored
   (N ≥ k), even if the user taps "failure".** Measure how accurate the one-tap confirmations are in Stage B.
4. **King 2025's F1 0.82 is not "plausible RIR ≤ 2 detection" yet.**
   - The split is unknown.
   - Every set went to failure, so "slow rep" and "near failure" were never separated.
   - No rep-number baseline was reported.

   In a 10-rep set to failure, 3 of 10 reps are positive. A rule like "the last reps slow down" may score similarly.
   TENSR's own Stage C must include sets stopped short at a heavier load, where reps are slow but not near failure.
5. **EMG in RIR models: zero dynamic evidence at inference.**
   - Thomas 2025 may have used EMG only to shape training labels.
   - González-Izal 2011: sEMG–power models may fail after a training block.
   - Benitez/JSCR 2023: final-rep amplitude is the same at 30 and 80%.

   X4.C3 (EMG must beat IMU-only by ≥ 0.2 reps or be dropped) is the right gate. **Expect it to fail.** Plan the
   product so EMG's job is rep timing on static-segment lifts, signal quality and activation, not RIR.
6. **Multi-set drift.** Miras-Moreno 2023 found velocity relations **overestimate** reps left under fatigue, and
   Mansfield found 0.02–0.03 m/s drift between sets. A "set-3 RIR" from a set-1 model will read too high. That
   bias is in the unsafe direction: it tells the lifter there is more left. X4's prior adjusts for set number, which is
   right; validate it separately per set number.
7. **CLAUDE.md's validation test leaks.** The brief's "20–30 sets, half to failure, half 3 short, must separate 9/10"
   can be passed trivially, because the failure sets *contain the failed rep*. Features must come from reps before the
   stop point (X4's matched-rep rule). It is also one person, so it says nothing about generalisation.

### 3c. Is the coarse grade (0 / 1–2 / 3+) the right first product?

**Nearly. The cut is in the wrong place.**
- **The 0 vs 1–2 split is the hardest and least useful.**
  - It is hardest because humans are already best there (Halperin, Zourdos 1 RIR, Refalo's 0.65 if true).
  - It is least useful because failure vs 1–2 RIR adds little to growth (FA §1a).
  - "0" is claimable only when a failed concentric is actually detected. Then it is an event, not an estimate.
- **The boundary that matters is "hard (≤ 3 RIR)" vs "not hard (≥ 4)".** It decides whether a set counts toward
  weekly hard sets (FA D1). Human error is largest there, the error has a known direction (early underestimation by
  coaches), and the true margin is wide.

**Recommended first product:** after each set, one of
- **Failure** (stall detected),
- **Hard** (≤ 3),
- **Not hard** (≥ 4),
- **Unsure**.

No numeric RIR until X4.C1 and X4.C2 pass for that exercise class. Keep X4's posterior engine underneath; just do not
show the number yet.

## 4. What TENSR can honestly claim, by stage

| stage | can claim | cannot claim |
|---|---|---|
| **Now (no board built)** | "Designed to count reps, flag sets you take to failure, and track hard sets per muscle." "Built on the published science of effort and velocity loss." | Any accuracy. "Knows how many reps you have left." "Detects failure before it happens." "Tempo-independent fatigue score." CLAUDE.md's "that drop is the fatigue measurement, and it is tempo-independent, which is why this beats velocity-based training" has **no dynamic-lifting support**. The MDF fall is load-dependent and has no knee near failure (X1). "90 Hz = cooked" has no support. |
| **After Stage A (bench)** | Engineering facts only: latency, battery, BLE, haptic artefact suppressed. | Anything about people. |
| **After Stage B (pilot, n ≈ 8–12)** | Only measured numbers on named exercises, labelled exploratory: "counted reps within ±1 on X% of sets on [exercises]"; "flagged N of M failed reps". | RIR accuracy. Any comparison with the lifter. |
| **After Stage C (lab, LOSO + new session)** | Per exercise class, only where the gate passed: "calls hard vs not-hard sets correctly X% of the time (CI)"; "estimates RIR within X reps (MAE, CI) on [class]". **"More accurate than your own guess" only where X4.C1 passed. "The sensor adds to your training history" only where X4.C2 passed.** | Claims on classes that failed (likely the static-segment lifts). EMG as the RIR source if X4.C3 failed. |
| **After Stage D (field)** | "Works in a real gym": withheld-set rate, anchors per month, agreement with the lifter. | Lab accuracy restated as field accuracy. |
| **After Stage E (crossover / RCT)** | "Helps lifters finish sets closer to their target", with the effect size. Only after S5.1 shows no unsafe overshoot. | Hypertrophy or growth outcomes, ever, without an RCT. Injury, rehab or clinical language, ever (CLAUDE.md regulatory). |

**Claims that are true today and worth making:** the device needs no typing to log; it timestamps every rep; it
detects a failed rep, once Stage B measures this; and it counts hard sets the same way every time. Consistency and
automatic logging are real value. They are not accuracy, and copy must not blur the two.

## 5. Corrections each agent must accept or rebut

- **X1.**
  - The Looney contrast comes from a drop set. Add the JSCR 2023 counter-finding (final-rep EMG equal at 30/80%).
  - Soften "lactic acid not supported" for dynamic, velocity-limited sets (Allen & Trajanovska 2012).
  - de Morree supports RPE ≈ motor command, not RPE ≈ proximity.
  - Jukic 2023/2024 are one cohort.
- **X2.**
  - Armes is published, knee extension, CI 0.0–4.04.
  - The Miras-Moreno SEE is unverifiable; add the overestimation-under-fatigue result.
  - Resolve "Sports Eng 2024" → Külkamp et al.
  - Jin 2025 needs electrical stimulation.
  - King: segmentation 0.83, near-failure 0.82.
  - Thomas: n = 5 confirmed; EMG possibly training-only.
  - "No sensor beats the lifter" holds near failure only.
- **X3.**
  - Remove "every VBT study used maximal intent" and "no isolation VL→RIR study" (Külkamp: self-selected velocity,
    knee extension).
  - Qin's sample had ≥2 y RT.
  - Orange also validated squat MP/PP at 20%.
  - The Jukic rows are one cohort.
  - Achermann: n = 22, *Sports* (MDPI).
- **X4.**
  - Drop the band-1 light-load rule, or label it H with "no evidence at this precision".
  - Rewrite the cue-safety argument; add withheld/late-cue overshoot to Stage E.
  - Blank the IMU as well as EMG, keyed to the effect's end.
  - Anchors only from detected failed concentrics.
  - Report X4.C2 by set number.
  - X4.C7's "< 2" is a bound.
  - Duffey & Challis supports ×1.67, not ">2×".
  - Mitter 2022 is a lab floor.
  - Fusion needs a tag on every set.
