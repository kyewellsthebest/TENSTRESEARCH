# A3 search log (2026-11-02)

Environment: WebSearch only. WebFetch / curl to ti.com, doi.org, api.crossref.org, pubmed.ncbi.nlm.nih.gov,
robertomerletti.it were refused (proxy 403 / DNS not resolvable - outside allowed domains). The shared
per-turn WebSearch budget (200, all agents) was exhausted after A3's 37th query; two further queries
("Rep Smarter" details; LOSO vs subject-dependent leakage in sEMG fatigue ML) were not executed.

| # | source | query | useful hits |
|---|---|---|---|
| 1 | WebSearch ext | ADS1292R digital decimation filter sinc3 -3 dB bandwidth data rate 125...8k SPS | Mouser/Hackaday mirrors: sinc3; -3 dB 32.75/65.5/131 Hz at 125/250/500 SPS |
| 2 | WebFetch | ti.com/lit/ds/symlink/ads1292r.pdf | BLOCKED |
| 3 | WebFetch | pubmed 11018445 | BLOCKED |
| 4 | WebSearch ext | ADS1292R CONFIG1 DR[2:0] fMOD/1024 fMOD/16 | DR table endpoints; fMOD = fCLK/4 or /16 |
| 5 | WebSearch ext | ADS1292 noise table 1 kSPS 2 kSPS -3-dB bandwidth 262 524 | 0.262 fDR relation; family noise rows |
| 6 | WebSearch | LSM6DSO ODR / FIFO | 6.66 kHz max, 9 KB FIFO (secondary) |
| 7 | WebSearch ext | Hermens 2000 SENIAM IED 20 mm electrode 10 mm | JEK 10(5):361-374; 20 mm, <=1/4 fibre length, <=10 mm |
| 8 | WebSearch | SENIAM skin prep reference electrode biceps landmark | skin prep secondary; landmarks NOT found |
| 9 | WebSearch ext | Besomi 2019 CEDE electrode selection matrix | DOI 10.1016/j.jelekin.2019.07.008 |
| 10 | WebFetch | robertomerletti.it CEDE tutorial | BLOCKED |
| 11 | WebSearch ext | CEDE electrode matrix IED innervation zone crosstalk | detection volume / crosstalk statements (secondary) |
| 12 | WebSearch ext | Besomi 2020 CEDE amplitude normalization matrix | DOI 10.1016/j.jelekin.2020.102438; six approaches |
| 13 | WebSearch | De Luca 2010 filtering sEMG movement artifact | DOI 10.1016/j.jbiomech.2010.01.027 |
| 14 | WebSearch | Ives & Wigglesworth 2003 sampling rate | Henn/Hillstrom 1340 Hz; Ives not found |
| 15 | WebSearch | Ives Wigglesworth Clin Biomech 18 543 | bibliographic only |
| 16 | WebSearch | Nordander 2003 subcutaneous fat EMG amplitude | DOI 10.1007/s00421-003-0819-1; Baars 2006 |
| 17 | WebSearch | Lynn 2018 Athos validity | JSSM 17:205-215 abstract |
| 18 | WebSearch | textile/dry EMG garment vs gel during squat | Colyer & McGuigan 2018; textile materials PMC8811440 |
| 19 | WebSearch | dry stainless electrode impedance sweat over time vs Ag/AgCl | sweat lowers impedance over time; Ag/AgCl ~3x stainless (source unclear) |
| 20 | WebSearch | Searle & Kirkup 2000 | Physiol Meas 21:271-283; buffered+shielded caveat |
| 21 | WebSearch ext | test-retest MDF slope dynamic resistance reapplication | Mathur 2005, Larsson 2003, lifting 2002, back ext 2008; slope CV 14-27% |
| 22 | WebSearch | Fauth 2010 / between-day sEMG squat | Fauth 2010 abstract; Frampton 2026 |
| 23 | WebSearch | repetitive lifting reliability; Mathur quadriceps | PubMed 15642658; two-site PMC5427161 |
| 24 | WebSearch | Larsson 2003 knee extension reliability | bibliographic only |
| 25 | WebSearch | Farina & Merletti 2000 estimator comparison | DOI 10.1016/S1050-6411(00)00025-0 |
| 26 | WebSearch | Bonato 2001 TF parameters cyclic dynamic | IEEE TBME 48(7):745-753 |
| 27 | WebSearch | Morris 2014 RecoFit | +/-1 rep 93%, n=114/146 sessions |
| 28 | WebSearch | IMU rep counting validity free weights smartwatch | Garmin IJESAB abstract (no device valid); Soro 2019 |
| 29 | WebSearch | Soro 2019 Sensors CrossFit DL counting | 19(3):714; 91% within +/-1 |
| 30 | WebSearch | PUSH band validity vs LPT | Orange 2019, Lake 2019, van den Tillaar 2019 |
| 31 | WebSearch ext | ML sEMG predict RIR / proximity to failure LOSO | Garofalo 2026 JEK; arXiv 2512.11854; arXiv 2510.03197; Steele-type RIR accuracy PMC5712461 |
| 32 | WebSearch ext | systematic review ML sEMG fatigue dynamic subject-independent | inter-subject CCR 0.68 (unattributed); small-n, subjective labels |
| 33 | WebSearch | Garofalo 2026 details | DOI 10.1016/j.jelekin.2026.103111; n=12, 192 recs, LOO, LSTM MSE 49.44 |
| 34 | WebSearch | ML fatigue resistance training assistive robotics | Baek 2025 Sensors (load cell, RPE); arXiv 2602.15684 RMSE CNN 20.8 vs linear 26.9 |
| 35 | WebSearch | Karthick 2018 | details not found (UNVERIFIED) |
| 36 | WebSearch | Al-Mulla pseudo-wavelet dynamic biceps | 2015 J Med Syst n=13, 87.9%, 70/30; 2011 MEP n=10 88.41% |
| 37 | WebSearch | arXiv 2510.03197 details | Thomas & Wahlstrom; curls; Trigno; eccentric time top predictor |
| 38 | WebSearch | Moniri 2021 trunk fatigue forecasting | subjects not found |
| 39 | WebSearch | Rep Smarter arXiv details | NOT RUN - budget exhausted |
| 40 | WebSearch | LOSO vs subject-dependent leakage sEMG | NOT RUN - budget exhausted |

Derived analyses (no search): A3-sim-sampling.py (sinc3 + aliasing + MDF bias), A3-sim-mdf-window.py (Welch MDF variance Monte Carlo).
