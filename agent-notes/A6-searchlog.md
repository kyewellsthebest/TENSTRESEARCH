# A6 search log — 2026-11-02

**Fetch re-test (2026-11-02):** WebFetch https://doi.org/10.1016/S1050-6411(00)00027-4 -> `getaddrinfo ENOTFOUND doi.org`; WebFetch https://pmc.ncbi.nlm.nih.gov/ -> `ENOTFOUND`. curl (one attempt each, 15 s timeout) to doi.org, pmc.ncbi.nlm.nih.gov, api.crossref.org, eutils.ncbi.nlm.nih.gov, www.ebi.ac.uk (Europe PMC), arxiv.org, api.openalex.org, api.semanticscholar.org: all HTTP 000 (no connection). Fetch remains blocked; WebSearch only.

**Random-sample method:** pooled A1-A5 `*-studies.csv` rows (in file order A1..A5) excluding the 53 keys on the named list -> 115 rows; `random.seed(20261102); random.sample(rows, 15)` (Python 3). Sampled: GarminRepCount, Schoenfeld2020, Gerdle1992, Baek2025, SteeleRIR2017, Dankel2017, Schoenfeld2016, MartinezValdes2023, Pallares2021, BlandAltman1999, SanchezMedina2011, Saucier2021, Dimitrov2006, Lu2016, BicepsRecovery2008.

All searches: WebSearch, standard mode, 2026-11-02. Total 84.

| # | query (abridged) | useful result |
|---|---|---|
| 1 | Halperin 2022 ... 0.95 repetitions | verified 12 clusters/262 effects, I2 97.9% |
| 2 | Halperin "Accuracy in predicting repetitions to task failure" ... 414 | 13 pubs/12 studies/414; heavier loads more accurate |
| 3 | Refalo 2023 Sports Medicine proximity-to-failure ... | ES 0.19 (0.00-0.37); momentary 0.12 (-0.13,0.37) |
| 4 | Refalo 2024 J Sports Sci ... 1-2 RIR quadriceps | 0.181 vs 0.182 cm; 42(1):85-101 |
| 5 | Robinson 2024 Sports Medicine estimated proximity to failure ... | 54(9):2209-2231; load moderates |
| 6 | Grgic Schoenfeld Orazem Sabol 2022 JSHS ... | 11(2):202-211; trained ES 0.15 (0.03-0.26) |
| 7 | Lasevicius 2022 JSCR ... | 36(2):346-351 confirmed |
| 8 | Plotkin 2023 Front Physiol hip thrust ... | HT 18 / SQ 16 untrained, MRI, EMG not predictive |
| 9 | Vigotsky 2022 Sports Med Longing for a longitudinal proxy | 52(2):193-199 |
| 10 | Schoenfeld Ogborn Krieger 2015 repetition duration ... | 45(4):577-585; 0.5-8 s |
| 11 | Lopez 2021 MSSE ... 28 studies 747 | 53(6):1206-1216 |
| 12 | Pelland ... Sports Medicine 2026 56 481 | citation confirmed; DOI not seen |
| 13 | "10.1007/s40279-025-02344-w" | no hit - DOI UNVERIFIABLE |
| 14 | Singer ... Give it a rest ... | 9 studies/19 measurements; >60 s, none >90 s |
| 15 | Maeo 2023 EJSS triceps overhead ... | long head 28.5 vs 19.6% |
| 16 | Maeo 2021 MSSE seated vs prone leg curl ... | 14 vs 9% confirmed |
| 17 | Wolf 2023 IJSC partial vs full ROM ... -0.28 | CI confirmed; sign convention disputed |
| 18 | Wolf 2025 PeerJ lengthened partials trained ... | n=30 trained, similar |
| 19 | Pedrosa 2022 EJSS partial ROM long lengths ... | 45 untrained women |
| 20 | Pareja-Blanco 2017 SJMSS VL20 VL40 ... | 27(7):724-735; CMJ 9.5 vs 3.5% |
| 21 | Morton 2019 J Physiol fibre activation ... | sEMG unrelated to glycogen/signalling |
| 22 | Morton 2016 JAP neither load nor hormones ... | n=49 trained; 121(1):129-138 |
| 23 | Haugen 2023 BMC free-weight vs machine ... | 13 studies 1016; SMD -0.055 |
| 24 | Augustin ... Do cheaters prosper ... | 18(3):329-342; author order differs from A1 |
| 25 | Jenkins 2015 EJAP three sets to failure 80 vs 30% ... | MPF 71.6 vs 78.1% MVIC |
| 26 | Sakamoto Sinclair 2012 bench press speeds ... | 112:1015-1025; MDF drop similar across speeds |
| 27 | Yan 2025 Front Physiol bench press loads tempos ... | authors; fast tempo amplified MDF drop |
| 28 | Nishihara 2013 IZ shift 3.9 mm 16 mm | DOI 10.1155/2013/174342 |
| 29 | Sundstrup 2012 lateral raise elastic ... | plateau 3-5 reps before failure |
| 30 | Keenan ... 2005 amplitude cancellation 62% | 98:120-131 |
| 31 | Gonzalez-Izal 2010 wavelet indices power loss ... | JEK 20(6):1097-1106; 46.6/49.8% from 2009 WP |
| 32 | Burden 2010 How should we normalize ... | JEK 20(6):1023-1035 |
| 33 | Garofalo 2026 JEK proximity to failure EMG deep learning | 12 ppl/192 rec isometric; linear+SVR baselines |
| 34 | Rodriguez-Rosell 2021 SJMSS VL 10/30/45 EMG | no EMG change - training EMG |
| 35 | Hermens ... SENIAM ... 20 mm 10 mm ... | JEK 10(5):361-374; PMID 11018445 |
| 36 | Besomi 2019 CEDE electrode selection matrix ... | 48:128-144 |
| 37 | Lynn 2018 JSSM Athos ... | n=12, 7 sessions, isokinetic |
| 38 | Colyer McGuigan 2018 textile ... | between-session CV 42.6/41.2% |
| 39 | Nordander 2003 EJAP subcutaneous fat ... | 21-33% trapezius (second-hand) |
| 40 | Besomi 2020 CEDE normalization matrix ... | six approaches incl. submaximal task |
| 41 | Orange 2019 JSCR PUSH ... | 33(9):2398-2408; 29 youth rugby |
| 42 | Orange 2022 VBT vs traditional SMD 0.06 ... | J Sports Sci 40(11):1220-1234 |
| 43 | Weakley 2023 Sports Med feedback meta-analysis 8.4% | 20 studies; chronic benefit concluded |
| 44 | Weakley 2020 Show me tell me; Weakley 2019 visual feedback adolescent | JSCR 34(11); JSCR 33(9):2420-2425 |
| 45 | Bonett 2002 Stat Med ICC sample size k=4 0.85 0.2 | 19.2 example via presize docs |
| 46 | Koo Li 2016 ICC guideline cut-offs | 15(2):155-163 |
| 47 | ADS1292R datasheet "0.262" ... | 0.262 fDR; 32.75 Hz at 125 SPS |
| 48 | Barbalho retracted resistance training ... | RW: IJSPP 2020, JSCR Dec 2021, 7-paper call |
| 49 | Garmin wrist-worn devices repetition counting IJESAB | 20 ppl, 4 devices, not accurate |
| 50 | Schoenfeld To flex or rest ... | Front Physiol 10:1571; n=27 |
| 51 | Gerdle 1992 Acta Physiol Scand MPF selective ... | 145(2):129-138; type II selective |
| 52 | Baek 2025 Sensors ML fatigue assistive robotics ... | 25(21):6588; 93% not confirmed |
| 53 | Steele Endres Fisher Gentil Giessing 2017 PeerJ ... | e4105; n=141 |
| 54 | Dankel 2017 EJAP metabolites ... | 117:2125-2135 |
| 55 | Schoenfeld 2016 JSCR longer interset rest ... | n=21 trained |
| 56 | Martinez-Valdes 2023 CEDE HD matrix ... | not found |
| 57 | Pallares 2021 SJMSS ROM meta ... | 31(10):1866-1881; 16 studies; ES not seen |
| 58 | Sanchez-Medina 2011 VL lactate ammonia ... | r 0.97/0.95 secondary; ammonia R2 |
| 59 | Dimitrov 2006 MSSE FInsm5 ... | n=7 rectus femoris; ICC 0.75/0.78 |
| 60 | "Neuromuscular recovery of the biceps brachii ..." 2008 | Oliveira & Goncalves; 1-min light bouts |
| 61 | Saucier 2021 Sensors Strive basketball | 21(16):5348; 15 players |
| 62 | Lu ... 2016 Int J Biostat Bland-Altman sample size | 12(2) |
| 63 | Tsoukos 2021 SJMSS bench EMG velocity 40/60/80 | n=14 confirmed |
| 64 | Zhao Kurokawa Tajima Liu Okada 2025 ... | PeerJ null vs IJSM 2025 r=0.603 |
| 65 | SENIAM sensor locations pectoralis major 27 muscles | list not retrieved |
| 66 | Schoenfeld Grgic Ogborn Krieger 2017 low vs high load ... | 31(12):3508-3523; 21 studies |
| 67 | Gentil 2013 APNM single-joint retraction | found 2015 AJSM instead |
| 68 | "Effect of adding single-joint exercises ... untrained subjects" | Gentil 2013 n=29 confirmed; no retraction seen |
| 69 | upper arm worn IMU repetition counting biceps curl ... | no upper-arm study found |
| 70 | ADS1292R datasheet decimation "third-order" sinc ... | TI: third-order sinc confirmed |
| 71 | Weakley 2019 IJSPP augmented feedback 4 weeks ... | 14(9):1205-1211; 16 vs 12 |
| 72 | Jukic 2024 RIR-velocity relationship ... | Physiol Rep; n=46; <2 reps individual |
| 73 | Thomas Wahlstrom arXiv 2510.03197 ... | authors; 69 sets; ecc rep time top predictor |
| 74 | recovery of EMG median frequency lumbar exponential ... | Elfving 2002 EJAP; no pH/force |
| 75 | De Luca Gilmore Kuznetsov Roy 2010 filtering 20 Hz | 43(8):1573-1579; >=20 Hz second-hand |
| 76 | Searle Kirkup 2000 Physiol Meas wet dry insulating | 21:271-283; buffered+shielded |
| 77 | EMG median frequency recovery faster than force ... 31P pH | Mills 1982 MPF t1/2 3 min vs force 30 s; V-Poulsen r=0.82 pH |
| 78 | Morris Saponas Guillory Kelner RecoFit CHI 2014 ... | 93% within +/-1; arm-worn |
| 79 | Mathur Eng MacIntyre 2005 reliability quadriceps MDF slope | n=22; slope less reliable |
| 80 | Saeb ... 2017 GigaScience record-wise subject-wise | no hit (search returned journal pages) |
| 81 | Kassiano 2023 gastrocnemius partial ROM 15.2 6.7 3.4 | final +6.2, full +7.3; A1 numbers unsupported |
| 82 | Sodal 2023 Sports Med Open drop-set meta title | title confirmed; 9(1):66 |
| 83 | Wakahara ... 2013 nonuniform hypertrophy MSSE DOI | 45(11):2158-2165; DOI not seen |
| 84 | electrode orientation relative to muscle fibres ... MDF | VL study slopes -0.13 vs -0.21 p=0.09; modelling: power not spectrum |

Derived (no search): `A6-check-stats.py` (sinc order vs 0.262 fDR; Bonett; Wilson; LoA CI; SEM chi-square; A5 sample sizes), `A6-check-mdf.py` (spectral-shape sensitivity of A3's 500 SPS bias; truncation vs droop vs compensation; bipolar dip on relative change). A3-sim-sampling.py re-run in full and A3-sim-mdf-window.py re-run at 300 trials: both reproduce A3's numbers.
