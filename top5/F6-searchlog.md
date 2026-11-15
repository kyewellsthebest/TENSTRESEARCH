# F6 — sensing engineering: search log

Agent F6, 2026-11-02. Budget ~30 WebSearch; used **27** plus **1 WebFetch** attempt.

## Access

- WebFetch on `www.ncbi.nlm.nih.gov/pmc/articles/PMC10886028/`: **blocked** (`getaddrinfo ENOTFOUND`, host not in
  the session's allowed domains). This matches the earlier rounds (`../SEARCH-LOG.md`), so I made no further fetch
  attempts.
- So every row is at **SECONDARY** level (search-engine snippet or abstract fragment), or is taken from
  `../STUDY-EVIDENCE-TABLE.csv` (marked "via prior table"). I read no full text.
- Board facts come from the repo itself: `hardware/kicad/routed.kicad_pcb` parsed with `hardware/scripts/sexp.py`,
  `hardware/kicad/BOM_JLCPCB.csv` and `docs/AFE-DESIGN-REVIEW.md`. I edited no hardware or firmware file.

## Repo checks (not web)

| check | result |
|---|---|
| U6 (LSM6DSOTR) pad nets | 1 GND, 2 GND, 3 GND, 4 IMU_INT1, 5 3V3, 6 GND, 7 GND, 8 3V3, 9 none, 10 none, 11 3V3, 12 3V3, 13 I2C_SCL, 14 I2C_SDA |
| J3 pad nets | 1 3V3, 2 GND, 3 I2C_SDA, 4 I2C_SCL, 5 EXP_GPIO2 (U2.6), 6 EXP_GPIO18 (U2.22) |
| I2C bus members | U5 DRV2605L, U6 LSM6DSO, J3; pull-ups R9/R10 = 2.2 k (BOM line 22) |
| U1 CH2 | IN2N/IN2P (pins 5, 6) tied to 3V3_A; PGA2N/P (7, 8) not connected; RESP_MODP/N (31, 32) tied to 3V3_A (AFE-DESIGN-REVIEW pin table) |
| U2 unused module pads | 26, 27, 30–41, 44 have no net: unrouted, so using them needs a respin |

## Queries

| # | query (abridged) | useful result |
|---|---|---|
| 1 | LSM6DSO pin description SDx SCx OCS_Aux SDO_Aux sensor hub | Mode 1: SDx/SCx tied to VDDIO or GND; Mode 2 = sensor-hub master I2C on SDx/SCx. **This board is in Mode 1 (both grounded).** |
| 2 | MediaPipe validity joint angle squat vs motion capture | Panni 2026 −13.9° knee bias; Yue (JMIR preprint) ICC 0.77, ~5° under; Cardiff 2024 CV <10% |
| 3 | systematic review IMU joint angle vs optical RMSE | Fang 2023 (52 studies; elbow ~2° best case); Poitras 2019 (42); 21-study review RMSE up to 12.1° |
| 4 | magnetometer-free joint angle, Seel joint axis | Seel 2014 ~3° knee; mag-free model 4.34°; Weygers pipeline 4.1° knee (via review); indoor magnetometer unreliable |
| 5 | wearable A-mode ultrasound muscle thickness vs B-mode | Bioengineering 2024 n=30, mean diff <0.91 mm, ICC >0.95; BodyMetrix JSCR 2022 |
| 6 | wearable ultrasound muscle thickness during exercise | AlMohimeed & Ono 2012 0.4 mm (5%); CMBES isometric 0.8 mm (3.4%); no dynamic resistance-exercise validation found |
| 7 | Weakley 2021 VBT device review findings | Linear transducers recommended; many devices not fully valid; apps "snapshot" only |
| 8 | NIRS SmO2 sets to failure | Miranda-Fuentes 2021 review (SmO2 68–78% → 10–46%); Acta Bioeng 2022 n=16; nothing links SmO2 to RIR |
| 9 | accelerometer MMG fatigue dynamic resistance | Beck 2005 review; UNL thesis: MMG amplitude ↑, frequency ↓ to failure; large individual variability |
| 10 | force myography FSR force estimation review | Xiao & Menon 2019 review; Sakr et al. R² 0.77–0.84 isometric (4 bands); FSR unit-to-unit curve differences |
| 11 | smartphone app barbell velocity validity | PLOS ONE 2024: Qwik ≈ LPT; Metric/MyLift weaker; 52/175 of 589 reps missed |
| 12 | Vmaxpro/Enode validity | Held 2021 n=19 trained, ICC 0.91–0.96, LoA <0.12 m/s squat; Olaya-Cuartero 2022 −0.021 m/s |
| 13 | Jukic RIR–velocity individual vs general | Jukic 2024 n=46: individual relationships <2 reps error at a later session (squat); general ones not acceptable |
| 14 | Skulpt Aim localized bioimpedance validity | No independent validation found; Longo 2021 EIM vs US exists, results not seen |
| 15 | ADS1292R temperature sensor and respiration | Mux routes the temperature sensor internally; respiration 2–10 kΩ at 30 µA, 32/64 kHz |
| 16 | LSM6DSO ODR 6667 Hz, current | 6667 Hz ODR exists (Zephyr); 0.55 mA is **combo** (accel + gyro) HP; accel-only figure not confirmed |
| 17 | upper-arm/thigh IMU rep counting free weights | No upper-arm/thigh validation found; RecoFit ±1 rep in 93% (arm-worn); Garmin wrist not valid |
| 18 | two IMUs elbow flexion vs mocap, curl | No curl-specific validation; errors <1° (linkage) to ~8° (task) |
| 19 | single thigh IMU squat depth validity | No direct validation; thigh best single site for knee flexion in cutting (R² 0.91, thesis) |
| 20 | Orange 2019 PUSH validity | Banyard 2017 (PUSH valid only for peak force); van den Tillaar 2019 (PUSH biased low on bench); Callaghan |
| 21 | ultrasound MT typical error vs hypertrophy | Soares et al. review: weighted relative error 6.5% < 16.6% training effect (the latter from a dissertation) |
| 22 | (follow-up of 21: authors) | Soares ALC, Carvalho, Mogami, Meirelles, Gomes (RBCDH); Lohmann 2024 Sports Med Open |
| 23 | markerless pose bench/deadlift ROM | No joint-ROM validation for barbell lifts; Taber 2023 bar-path app n=9; Puppyn & Brughelli review |
| 24 | Moxy/Train.Red NIRS validity | Feldmann 2019 Moxy validity; Skotzke 2024 MDC 14–18% SmO2; Train.Red: nothing |
| 25 | rest interval velocity recovery | 1 min too short to keep velocity; 3 min adequate in moderate-fatigue protocols (Smith machine, 2020) |
| 26 | camera weight-stack/plate recognition | Patents only for camera; W8-Scope (stack-mounted sensor) 97.5% weight ID, n=50 |
| 27 | sEMG rep counting sleeve | None found; LEAN Apple Watch 0.92% rep error; arXiv 2510.03197 EMG+IMU RPE 41.4% exact |

## What I searched for and did not find

- Any validation of **upper-arm or thigh-worn IMU rep counting** in free weights.
- A **thigh-only IMU squat-depth** validation against mocap under load.
- A **two-IMU elbow angle** validation during curls specifically.
- **Pose-estimation joint ROM in barbell lifts** (bench, deadlift).
- **Wearable A-mode** muscle thickness tracked **during dynamic resistance exercise**, or over a training block.
- Any **NIRS ↔ RIR / proximity-to-failure** relationship.
- Any independent validation of **Skulpt** (localized bioimpedance) or **Train.Red**.
