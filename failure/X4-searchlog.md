# X4 — search log

Agent X4, 2026-11-03. Budget ~25 WebSearch; used **22**, all standard mode. No WebFetch (earlier rounds found PMC/DOI
fetch blocked). Every result was seen as a search-engine summary of abstracts or repository records; nothing was read in full text.

## Repo reads (not web)
`failure/BRIEF.md`; `CLAUDE.md` (hardware, firmware); `TENSR-SCIENCE-REPORT.md` §1–5; `TENSR-VALIDATION-PLAN.md` §4–5;
`top5/F6-findings.md`; `top5/FA-audit.md`; `STUDY-EVIDENCE-TABLE.csv` rows for Halperin2022, Jukic2024, Garofalo2026,
ThomasWahlstrom2025, Sundstrup2012, Jenkins2015, Lasevicius2022, Weakley2023, Morris2014, Saeb2017, SanchezMedina2011.

## Queries

| # | query (abridged) | useful result |
|---|---|---|
| 1 | minimal velocity threshold last repetition velocity reliability individual squat bench failure | PeerJ 2020 (n=96 Smith bench): Vlast CV >18.3%, ICC <0.60; Banyard 2017 back-squat V1RM CV 22.5% (cited) |
| 2 | velocity-based RIR prediction dumbbell/machine/single-joint individual accuracy | García-Ramos 2018 individual r² .984; prone bench pull 4-model ranking (n=15); Külkamp 2024 pointer |
| 3 | linear encoder RIR lat pulldown knee extension bench 57 men | Külkamp 2024 Sports Eng: ICC 0.88; ≤2-rep error >90% LP/BP, KE lower |
| 4 | wearable IMU wrist RIR estimation ML LOSO | King 2025 arXiv 2512.11854; Thomas & Wahlström 2025 (5 participants); RIR patent; no LOSO result found |
| 5 | "Rep Smarter, Not Harder" details | 13 participants, 631 reps, preacher curl; seg F1 0.83, near-failure F1 0.82; split not seen |
| 6 | RIR accuracy improves with practice / Refalo 2024 bench | Refalo 2024 JSCR intraset bench (24 trained, 0.65 ± 0.78 — one summary); FAU 6-week bias shift; familiarisation study |
| 7 | Refalo intraset RIR bench 75% 0.65 (verification) | Citation confirmed via an arXiv reference list; **numbers NOT confirmed**; summary's DOI malformed — not used |
| 8 | biceps curl / lateral raise velocity loss reps to failure | No single-joint study; Rodríguez-Rosell 2020 VL→%reps R² 0.97/0.93; prone pull VL negative |
| 9 | sEMG RIR prediction dynamic 2025 MDF amplitude | No dynamic EMG-RIR study found; spectral endurance prediction "limited" (2011 biceps) |
| 10 | endurance time prediction biceps Dimitrov index | Lee & Lee (n=10) incremental-time predictor; MDPI 2021 follow-up; errors not seen |
| 11 | physiological tremor fatigue resistance exercise 8–12 Hz | Review: 8–12 Hz peak rises with fatigue; small studies (n 9–11); no reps-to-failure tracking |
| 12 | ROM decreases final reps set to failure kinematics | Duffey & Challis bench (time >2×, distance constant); Brice squat (ROM unchanged, skilled) |
| 13 | Bayesian hierarchical reps-to-failure velocity individual | Mitter 2023 multilevel R² 0.97–0.98 vs 0.89–0.93; Jukic fastest-rep R² 0.98 vs 0.45–0.49; Haischer squat negative |
| 14 | test-retest reps to failure fixed load CV | Mitter 2022 PLOS ONE: ICC 0.86/0.65, SEM 1.1/0.7 reps at 70/90% |
| 15 | sEMG armband repetition counting validation | Nothing direct; Garmin rep counts invalid; band-exercise IMU MAE 0.88–3.21 |
| 16 | concentric duration predicts RIR without velocity device | Achermann 2024 ISBS adj R² 0.37 vs 0.14; Mansfield 2023 69.1%; Haischer |
| 17 | "The velocity of resistance exercise does not" 69.1% | Mansfield 2023 EJSS: bench + prone row, 60/80%, recreational; González-Badillo 2017 counterpoint |
| 18 | thigh/arm-mounted IMU velocity loss vs LPT | PUSH (youth rugby) not valid; seven-device bench: IMUs less reliable; no thigh/arm VL study |
| 19 | automatic failed rep / sticking point IMU | Rum 2022 Sensors: 2.8% detection error, 0.50 s max timing error, Paralympic bench |
| 20 | esp-dsp ESP32-S3 FFT benchmark | dsps_fft2r_fc32 1024-pt 97,847 cycles (ESP32-S3, optimised) |
| 21 | vibrotactile haptic feedback during resistance training | Only wrist-posture curl study (thesis, n=30); no rep-level effort-cue study found |
| 22 | RIR accuracy light load / high reps worse | Murdoch 2020 (21 trained: 85% > 75% > 65%); FAU reps-per-set; hex-bar deadlift 2026 VBT compromised |

## Not found (searched, nothing usable)
- Any validated sEMG RIR model in dynamic lifting.
- Velocity-loss → RIR on dumbbell or isolation exercises from a limb-worn sensor.
- Within-person residual SD of bias-corrected RIR self-report.
- Upper-arm / thigh rep counting validation.
- User acceptance of calibration-to-failure.
