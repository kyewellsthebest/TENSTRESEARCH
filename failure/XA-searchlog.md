# XA search log — independent audit of X1–X4

Agent XA, 2026-11-03. 59 WebSearch calls (budget ~60). 5 WebFetch attempts, all failed.

## WebFetch re-test (2026-11-03)

| URL | result |
|---|---|
| https://arxiv.org/abs/2512.11854 | `getaddrinfo ENOTFOUND arxiv.org` |
| https://arxiv.org/abs/2510.03197 | `getaddrinfo ENOTFOUND arxiv.org` |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC10907223/ | `getaddrinfo ENOTFOUND pmc.ncbi.nlm.nih.gov` |
| https://bytez.com/docs/arxiv/2510.03197/paper (arXiv mirror) | `getaddrinfo ENOTFOUND bytez.com` |
| https://www.researchgate.net/publication/398720702_... | `getaddrinfo ENOTFOUND www.researchgate.net` |

Fetch is still blocked at DNS for every host tried. arxiv.org and pmc.ncbi.nlm.nih.gov would have to be added to
the session's allowed network domains. No full text was read. Every verdict below is at abstract or search-summary
level.

## Searches

| # | query (abridged) | used for | outcome |
|---|---|---|---|
| 1 | "Rep Smarter, Not Harder" King Azeem Valafar ... leave-one-subject-out | King 2025 | n=13, 631 reps, F1 0.83 seg / 0.82 near-failure; split NOT found |
| 2 | Thomas Wahlström 2025 RPE inertial EMG LOSO | Thomas 2025 | authors James Thomas & Johan Wahlström; 69 sets; ≥2 y trained; split not found |
| 3 | arxiv 2512.11854 participants train test split held-out | King split | split not found |
| 4 | arxiv 2510.03197 leave-one / cross-validation EMG training only | Thomas EMG role | one summary: EMG used only in training to build labels, IMU-only at test |
| 5 | Rodríguez-Rosell 2020 VL and RIR bench squat R2 | RR2020 | JSCR 34(9):2537–2547; R² 0.97/0.93; n=20 |
| 6 | Jukic 2023 "Velocity loss is a flawed method" EJAP | Jukic EJAP | EJAP 123(6):1343–1357; 46 (15F/31M); 1RM + 2 RTF tests 72 h apart |
| 7 | Jukic Helms McGuigan fastest repetition Physiol Behav | Jukic PB | Physiol Behav 265:114158 confirmed; numbers not in this summary |
| 8 | Jukic 2024 Physiol Rep e15955 | Jukic 2024 | 46 (15F/31M), same 1RM + 2 RTF 72 h design; individual mean error "<2 reps" |
| 9 | "fastest repetition" Jukic 1.96 2.81 | Jukic PB numbers | 1.96 vs 2.81 confirmed; R² 0.98 vs 0.45–0.49 |
| 10 | García-Ramos 2020 PeerJ last repetition 96 | GR2020 | PeerJ 8:e8760; 96 healthy men; CV >18.3%, ICC <0.60; r 0.18/0.37 |
| 11 | Mansfield Peiffer Galna Scott 2023 30.9% | Mansfield | EJSS; recreationally active; 30.9% / 69.1%; bench + prone row 60/80% |
| 12 | Qin Liu García-Ramos 2025 gauging proximity | Qin 2025 | BMC SSMR 17:60; 19 men, ≥2 y RT; AE 1.3 ± 0.7; deviation −0.4 to 0.6 |
| 13 | Janicijevic ... 2024 wrestlers | Janicijevic | EJSS 24(3):364–371; 30 wrestlers; AE 1.1–1.7 / 1.2–1.8 |
| 14 | Sports Engineering 2024 s12283-024-00450-y authors | Sports Eng encoder | Külkamp, Kons, de Souza, Kunzler, Bishop; 57 men; 3 exercises; ICC 0.88 |
| 15 | Morán-Navarro 2019 movement velocity level of effort | Morán-Navarro | JSCR 33(6):1496–1504; 30 men in 3 strength groups; CV 4.4–8.0%; exercise list not confirmed |
| 16 | Sundstrup 2012 muscle activation strategies | Sundstrup | JSCR 26(7):1897–1903; 15 untrained women; elastic lateral raise; plateau 3–5 reps |
| 17 | Looney 2016 EMG perceptual squat | Looney | JSCR 30(3):792–799; 10 trained men; drop-set design |
| 18 | Benitez Bergstrom 2023 EJAP biceps EMG MMG | Benitez | EJAP 123(10):2145–2156 confirmed; companion JSCR: final-rep EMG no load difference |
| 19 | Martinez-Valdes ... 2020 J Neurophysiol | Martinez-Valdes | verified |
| 20 | Dideriksen Enoka Farina 2011 | Dideriksen | J Appl Physiol 111(2):485–494; ~40% cancellation; verified |
| 21 | de Morree Klein Marcora 2012 | de Morree | Psychophysiology 49(9):1242–1253; 16 recreationally active men; 20/35% 1RM elbow flexion |
| 22 | Allen Lamb Westerblad 2008 limited importance | Allen | bibliographic only; exact quote not seen; acidosis debate open (Fitts 2016 vs Westerblad 2016; Allen & Trajanovska 2012) |
| 23 | Steele ... 2017 Clarity in reporting terminology | Steele | Muscle Nerve 56(3):368–374; PMID 28044366; MF wording not seen |
| 24 | Baek Kwon Khan Lee 2025 Sensors | Baek | Sensors 25:6588; 32 men / 64 limbs; 7 sets at 7RM; isokinetic bench load cell; split not seen |
| 25 | Elshafei Shihab 2021 Sensors 21 759 | Elshafei | 98% / 88%; 20 volunteers, ~3000 curls; split protocol not seen |
| 26 | González-Izal 2010 JEK; 2011 MSSE | G-I 2010 | JEK 20(6):1097–1106; 15 trained; 5×10 leg press; 46.6% / 49.8% |
| 27 | "Effects of strength training on muscle fatigue mapping..." | G-I 2011 | MSSE 43(2):303–311; 12 trained; sEMG tracking "may fail" after training; verified |
| 28 | Halperin 2022 accuracy predicting repetitions to task failure | Halperin | Sports Med 52(2):377–390; 414; 0.95 (0.17–1.73); SD 1.45; training status not a moderator |
| 29 | Armes "Just one more rep" 2.02 | Armes | Front Psychol 2020; knee extension; ≥1 y trained; 2.02 (0.0–4.04) |
| 30 | Refalo ... 2024 intraset RIR bench | Refalo 2024 | title confirmed; 0.65 ± 0.78 only via Marzagao 2026 arXiv summary |
| 31 | intraset RIR bench 75% Refalo abstract | Refalo 2024 | still secondary only; Casanova 2025 1 RIR > 3 RIR accuracy |
| 32 | Banyard ... 2017 IJSPP PUSH GymAware | Banyard | IJSPP 12(9):1170–1176; 10 strength-trained men; verified |
| 33 | Orange 2019 PUSH rugby | Orange | JSCR 33(9):2398–2408; 29 youth rugby; valid only squat MP/PP 20%, bench MP 40% |
| 34 | Achermann 2023 Apple Watch | Achermann | Sports 11(7); 22 recreational; wrist r 0.952–0.965, SEE 0.064 |
| 35 | Mitter 2022 reproducibility strength-endurance | Mitter 2022 | PLOS ONE; 24 trained; bench; 1 wk apart; SEM 0.7 (90%), 1.1 (70%) |
| 36 | Albert 2022 PERSIST | PERSIST | Data 8(1):9; 12 men ≥1 y; IMU + ECG + Kinect; flywheel squat; Borg 6–20 |
| 37 | Miras-Moreno 2023 Heliyon prone bench pull | Miras-Moreno | 23 trained men; errors similar; all RTF–MV relations overestimate RTF under fatigue |
| 38 | RecoFit 2014 93% ±1 | Morris 2014 | verified, 114 participants |
| 39 | Duffey Challis fatigue bar kinematics | Duffey & Challis | JSCR 21(2):556–560 per PSU; a citing paper gives mean concentric velocity −40% |
| 40 | PMID 17530976 bench peak power | BenchPower2007 | optical encoder validation; n=7; 4×6 at 85–95% 6RM; −55% peak power |
| 41 | Hwang 2025 sEMG IMU CNN-LSTM 87.94% | Hwang | Sensors 25:3309; gait after step exercise; LOSO |
| 42 | Güngör 2024 failure BP HRV | Gungor | J Clin Med 13(8):2296; 16 trained men; 40/60/80% |
| 43 | Jin 2025 Harvard A-mode ultrasound | Jin | r 0.85, n=8, electrically stimulated, dynamometer |
| 44 | PLOS ONE 2022 sEMG ECG TCN | PLOS2022 | exists (Mu, PLOS ONE 2022); biceps; results garbled |
| 45 | Apple Garmin WHOOP 2025 2026 RIR feature | consumer | no RIR feature found; WHOOP–Motra acquisition reported Oct 2026, unconfirmed |
| 46 | tremor fatigue 8–12 Hz Glasgow | tremor row | Glasgow 184542 = Aljihmani 2019, n=15, accelerometer, 8–14 Hz; not a lifting study |
| 47 | RIR accuracy far from failure high reps 2024 2025 | task 3 | Zourdos 2021; Casanova 2025; Emanuel 2022 numbers |
| 48 | 2025 2026 wearable RIR LOSO MAE reps | task 3 | nothing new found |
| 49 | Zourdos "Proximity to Failure and Total Repetitions..." | task 3 | JSCR 35(Suppl 1):S158–S165; PMID 30747900; 70% squat; error vs total reps r 0.65 / 0.56 |
| 50 | "4.8" "2.0" "1.2" RIR 33% 66% 90% | task 3 | Emanuel 2022, 259 coaches, mean set 13.9 reps |
| 51 | esp-dsp dsps_fft2r_fc32 1024 ESP32-S3 | X4 compute | 97,847 cycles verified |
| 52 | LSM6DSO ODR options | X4 IMU | 12.5 Hz … 6.66 kHz ladder; 416/417 Hz valid |
| 53 | DRV2605L ERM EMG artifact | X4 haptic | no direct source |
| 54 | Lasevicius 2022 design | X4 band | non-failure reps 19.6 vs 34.4 (low), 6.7 vs 12.4 (high) |
| 55 | IMU failed-rep / sticking detection sens spec | X4.C5 | none found |
| 56 | "Rep Smarter" emergentmind split | King split | nothing |
| 57 | Thomas 2025 five participants Delsys | Thomas n | 5 men confirmed; Delsys Trigno; EMG 2148 Hz, IMU 370 Hz |
| 58 | velocity vs self-report RIR head-to-head | task 3 | no same-set head-to-head found; Paulsen 2025 PeerJ |
| 59 | arXiv 2603.17495 303,494 near-failure sets | task 3 | Marzagao (Fitbod) 2026; 14,966 users, 388 exercises |
