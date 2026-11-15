# Search log — TENSR science investigation

Searches run 2026-11-02 by six research agents (A1–A6), after the protocol was registered (`PROTOCOL.md`).
This file concatenates each agent's own log verbatim; the per-agent files in `agent-notes/` are the originals.

## Access conditions (apply to every entry)

- **Only WebSearch worked.** WebFetch, doi.org, Crossref, PubMed/eutils, PMC, Europe PMC, arXiv, OpenAlex,
  Semantic Scholar, ti.com and publisher hosts were all refused by this environment's network policy (proxy 403 or
  DNS failure). A6 re-tested on 2026-11-02 and recorded the failures.
- **Consequence: no paper was read in full text.** Every verification is at the level of a search-engine summary of
  an abstract, a repository record, a publisher HTML snippet or another paper's citation. The `access` column of
  `STUDY-EVIDENCE-TABLE.csv` records which, per study. Nothing is marked FULL.
- **Search budget:** WebSearch was limited to about 200 calls per coordinator turn, shared across agents. It was
  exhausted during batch 1; A1, A2, A3 and A5 each list searches they could not run. A6 ran in a later turn with a
  fresh budget (84 searches); the audit responses used a further ~23.
- Approximate totals: A1 64, A2 66, A3 37, A4 28, A5 29 (+3 not run), A6 84.

## How to re-run with full-text access

Allow `doi.org`, `pmc.ncbi.nlm.nih.gov`, `eutils.ncbi.nlm.nih.gov`, `api.crossref.org` and `www.ti.com` in the
environment's network settings, then re-verify every row in `STUDY-EVIDENCE-TABLE.csv` whose `access` is not FULL,
starting with the load-bearing rows named in `CLAIM-VERIFICATION.md` §3.

---

## A1

### A1 search log — 2026-11-02

Tool: WebSearch (standard mode) only. Blocked in this session, tried once each: `api.crossref.org` (curl: proxy CONNECT 403; WebFetch: DNS refusal), `sponet.de` (WebFetch: DNS refusal); curl to pubmed.ncbi.nlm.nih.gov, eutils.ncbi.nlm.nih.gov, www.ncbi.nlm.nih.gov, doi.org, europepmc.org, www.ebi.ac.uk all failed (no connection). After two WebFetch refusals, no further sites were tried, per the tool instruction. The shared WebSearch budget (200 per turn, all agents) was exhausted after A1's 53rd call; the last four calls returned no results.

| # | search string | useful hits |
|---|---|---|
| 1 | Pelland 2025 resistance training dose response meta-regressions weekly volume frequency hypertrophy strength Sports Medicine | Pelland Sports Med 2026 56(2) 481-505; SportRxiv 537 |
| 2 | Pelland Sports Medicine 2026 56 481 "resistance training dose response" doi 10.1007/s40279 | DOI 10.1007/s40279-025-02344-w (sponet record) |
| 3 | Robinson 2024 Sports Medicine proximity to failure meta-regressions ... 10.1007/s40279-024-02069-2 | Abertay record; FAU news |
| 4 | Refalo 2023 Sports Medicine "proximity-to-failure on skeletal muscle hypertrophy" ... | AUT repository; abstract |
| 5 | Halperin 2022 "Accuracy in Predicting Repetitions to Task Failure..." doi | PubMed 34542869; DOI; pooled 0.95 reps |
| 6 | Grgic 2022 J Sport Health Sci failure non-failure ... | DOAJ; ES values |
| 7 | Vieira 2021 JSCR "training performed to failure or not to failure" ... doi | citation/DOI only |
| 8 | Refalo 2024 J Sports Sci similar hypertrophy momentary muscular failure RIR ... | PubMed 38393985; AUT |
| 9 | Singer 2024 "Give it a rest" Bayesian meta-analysis ... | PMC11349676; DOI |
| 10 | Vieira Umpierre 2021 ... results effect size | none for results |
| 11 | Maeo 2021 hamstrings seated vs prone leg curl ... | PubMed 33009197 |
| 12 | Maeo 2023 triceps overhead vs neutral ... | DOI via secondary; Ritsumeikan release |
| 13 | Pedrosa 2022 partial ROM long muscle lengths knee extension ... | DOI; abstract |
| 14 | "10.1249/MSS.0000000000002523" | no exact hit |
| 15 | Kassiano 2023 gastrocnemius ... JSCR doi | PubMed 37015016; DOI |
| 16 | Wolf 2023 "Partial vs full range of motion resistance training" ... | IUSCA journal 182; DOI; SMDs |
| 17 | Pallares 2021 "Effects of range of motion on resistance training adaptations" ... | UGR repository; DOI; ESs |
| 18 | Maeo Huang Wu ... "Greater Hamstrings Muscle Hypertrophy" Med Sci Sports Exerc 2021 53(4) 825 doi | DOI confirmed |
| 19 | Wolf 2025 lengthened partial repetitions vs full ROM trained ... | PeerJ 18904 |
| 20 | Kassiano "Partial range of motion and muscle hypertrophy: not all ROMs lead to Rome" doi | letter SJMSS 2022; "Which ROMs lead to Rome" JSCR DOI |
| 21 | Schoenfeld Ogborn Krieger 2015 repetition duration meta ... | PubMed 25601394; DOI |
| 22 | PeerJ 10909 different repetition duration to failure ... | Lacerda 2021 |
| 23 | Wilk 2021 Sports Medicine movement tempo review doi | PMC8310485; DOI |
| 24 | Burd 2012 J Physiol muscle time under tension ... | PMC3285070; DOI |
| 25 | Schoenfeld Grgic Ogborn Krieger 2017 low- vs high-load ... | PubMed 28834797; DOI |
| 26 | Lopez 2021 load network meta-analysis MSSE doi | JYX; ECU; DOI |
| 27 | Schoenfeld 2021 Sports repetition continuum doi | PMC7927075; DOI |
| 28 | Schoenfeld Ogborn Krieger 2017 dose-response weekly volume ... | DOI; 10+ sets result |
| 29 | Schoenfeld Grgic Krieger 2019 frequency ... | DOI (VU repository) |
| 30 | Vigotsky ... 2022 "Longing for a longitudinal proxy" ... | DOI; polito post-print |
| 31 | Plotkin 2023 hip thrust vs back squat ... | Frontiers DOI; results |
| 32 | Wakahara 2013 "Nonuniform muscle hypertrophy..." | citation only; DOI not found |
| 33 | Vigotsky 2017 "Interpreting signal amplitudes..." | DOI; PMC5758546 |
| 34 | "10.1249/MSS.0b013e3182995349" | no exact hit (Wakahara DOI UNVERIFIED) |
| 35 | Schoenfeld 2016 longer interset rest ... | DOI; results |
| 36 | Schoenfeld ... 2017 concentric vs eccentric meta ... | PubMed 28486337; DOI; 10.0 vs 6.8% |
| 37 | Oranchuk 2019 isometric training review doi | PubMed 30580468; DOI |
| 38 | Haugen 2023 free-weight vs machine ... | DOAJ; DOI; SMDs |
| 39 | Coleman 2023 drop set meta ... | Coleman 2022 IJSC; Sodal 2023 DOI |
| 40 | superset vs traditional meta 2025 Sports Medicine Zhang ... | PMC12011898; DOI |
| 41 | Davies 2021 cluster sets meta ... | PubMed 33475986; DOI |
| 42 | Pareja-Blanco 2017 velocity loss 20 vs 40 ... | DOI; results |
| 43 | Lasevicius 2022 muscle failure low-load ... | PubMed 31895290; DOI |
| 44 | Morton 2016 J Appl Physiol neither load nor systemic hormones ... | PMC4967245; DOI |
| 45 | Zourdos 2016 RIR-based RPE scale ... | DOI; PMID 26049792 |
| 46 | cheating repetitions momentum ... | Augustin 2025 IJES |
| 47 | Gentil 2013 adding single-joint ... ; Barbalho retraction | Gentil citation; Barbalho abstract; retraction not checked |
| 48 | regional hypertrophy systematic review ... Zabaleta-Korta 2021 | indirect only; Varovic preprint |
| 49 | pause repetitions ... peak contraction ... | Schoenfeld 2020 flex/rest (fphys.2019.01571) |
| 50 | "Do Cheaters Prosper?" Augustin ... doi | DOI 10.70252/GDBL2230 |
| 51 | Dankel 2017 metabolites ... | DOI |
| 52 | Wackerhage 2019 stimuli and sensors ... | PubMed 30335577; DOI |
| 53 | Damas 2016 J Physiol MyoPS ... | PubMed 27219125; DOI |
| 54-57 | Morton 2019 J Physiol; Schoenfeld 2014 EJAP EMG; Lixandrao 2018 BFR; Kubo 2019 squat depth | **not run — shared search budget exhausted** |

(Rows are numbered by call; some calls were issued in parallel batches. The count of calls that returned results is 53.)

## Audit-response searches (2026-11-02, later)

| # | search string | useful hits |
|---|---|---|
| R1 | Kassiano 2023 gastrocnemius partial ROM initial final full muscle thickness percent increase results abstract | MG +15.2/+6.7/+3.4 (fragment); LG +14.9/+6.2/+7.3 |
| R2 | Maeo 2023 triceps overhead vs neutral long head 28.5% 19.6% whole triceps volume abstract results | whole TB +19.9 vs +13.9 d=1.427; LH +28.5 vs +19.6; Lat+Med +14.6 vs +10.5 |
| R3 | Wolf 2023 partial vs full ROM meta-analysis lengthened partials hypertrophy -0.28 sign convention | abstract wording: benefit to lengthened partials (-0.28) |
| R4 | "10.1007/s40279-025-02344-w" | no hit; DOI unverified |
| R5 | Augustin Pinero Enes Nippard Schoenfeld "Do Cheaters Prosper" author list ... | no relevant hit |
| R6 | Pelland Remmert Robinson Hinson Zourdos "The Resistance Training Dose Response" Sports Medicine doi s40279-025 | citation confirmed; no DOI; SportRxiv 460 |
| R7 | Halperin 2022 predicting repetitions to failure SD 1.45 heavier loads ... | SD 1.45 (0.99-2.12); <=12 reps more accurate; heavier-load claim in preprint |

## A2

### A2 search log — surface EMG and fatigue

Agent: A2. Date of all searches: 2026-11-02.

## Access conditions (recorded honestly)

- `curl` to api.crossref.org, doi.org, pubmed.ncbi.nlm.nih.gov and eutils.ncbi.nlm.nih.gov: **refused by the egress proxy (HTTP 403 on CONNECT)**. No DOI could be resolved directly.
- `WebFetch` to paulogentil.com, pmc.ncbi.nlm.nih.gov and www.frontiersin.org: **DNS failure (host outside allowed domains)**. No full text could be opened.
- Only `WebSearch` worked. Everything below is therefore at the level of search-index abstracts/snippets, repository records and reference lists. **No study in A2's table was read in full text.** Access codes in the CSV are ABSTRACT (abstract or abstract-level summary seen) or SECONDARY (seen only via another paper's citation / a repository record).
- The shared WebSearch budget (200 calls per turn, all agents) ran out at the end of this agent's run; three final verification searches (Potvin/Sundstrup DOIs, Tsoukos 2024 DOI, a biceps-curl MDF Hz search) were **not performed**.

## Searches run (WebSearch, standard unless noted)

| # | query (abridged) | useful hits |
|---|---|---|
| 1 | Cifrek 2009 surface EMG based muscle fatigue evaluation in biomechanics Clin Biomech doi | CROSBI record, DOI 10.1016/j.clinbiomech.2009.01.010 |
| 2 | González-Izal 2012 electromyographic models to assess muscle fatigue review JEK | UNAV repository, DOI 10.1016/j.jelekin.2012.02.019 |
| 3 | Vigotsky 2018 interpreting signal amplitudes sEMG Frontiers | DOI 10.3389/fphys.2017.00985, PMC5758546 |
| 4 | González-Izal 2010 wavelet indices leg press power loss | JEK 20(6):1097, DOI 10.1016/j.jelekin.2010.05.010; abstract (n=15, 5x10 leg press, R² 46.6%/49.8%) |
| 5 | "EMG spectral indices and muscle power fatigue during dynamic contractions" | JEK 20(2):233, DOI 10.1016/j.jelekin.2009.03.011 |
| 6 | Dimitrov 2006 FInsm5 MSSE dynamic | abstract: n=7, 10x15 knee ext 50% 1RM; ΔFInsm5 ~8-fold vs ΔFmed 32% |
| 7 | Sakamoto Sinclair 2012 bench press speeds intensities EMG | abstract: n=13, 5 loads x 4 speeds; MDF drop similar across speeds, larger at light loads |
| 8 | Potvin 1997 muscle kinematics EMG amplitude frequency dynamic | J Appl Physiol 82(1):144; n=15; abstract fragments |
| 9 | (WebFetch Potvin PDF, Vigotsky PMC, Vigotsky Frontiers) | all blocked |
| 10 | Dimitrova & Dimitrov 2003 facts pitfalls fallacies | citation only, JEK 13:13-36 |
| 11 | Farina 2006 interpretation sEMG dynamic ESSR | ESSR 34(3):121-127, abstract-level |
| 12 | Bonato 2001 time-frequency cyclic dynamic | citation only, IEEE TBME 48(7):745-753 |
| 13 | MacIsaac 2001 dynamic factors myoelectric | IEEE EMBS 2001 conference paper (DTIC PDF); CV more resilient than MNF to angle/force |
| 14 | Farina/Merletti 2001 joint angle EMG variables | IEEE EMB Mag 20:62-71, citation only |
| 15 | Doud & Walsh 1995 muscle length fatigue EMG frequency | citation via later paper; MNF/MDF decrease with increasing muscle length (secondary) |
| 16 | Farina Merletti Enoka 2004 neural strategies | J Appl Physiol 96:1486-95, abstract |
| 17 | Keenan 2005 amplitude cancellation | DOI 10.1152/japplphysiol.00894.2004; cancellation up to 62% at max, up to 85% with fatigue-like MUAP changes |
| 18 | Enoka & Duchateau 2008 muscle fatigue J Physiol | 586(1):11-23 |
| 19 | Walker 2012 neuromuscular fatigue max vs hypertrophic loadings | abstract: n=13 untrained, 15x1RM vs 5x10RM leg press |
| 20 | Sundstrup 2012 heavy vs failure EMG | abstract: n=15 untrained women; EMG plateau last 3-5 reps; MPF fell |
| 21 | sEMG predict RIR wearable (extended) | no direct study; arXiv 2510.03197 RPE; Halperin context |
| 22 | arXiv 2510.03197 details | 69 sets/1003 reps; EMG added little over IMU; no accuracy figures in snippet |
| 23 | velocity loss vs EMG MDF (extended) | Tsoukos 2021; Rodríguez-Rosell 2021; Yan 2025; Tsoukos 2024 |
| 24 | ML sEMG predict failure LOSO (extended) | Garofalo 2026 JEK (isometric, n=12); LOSO basketball pilot; Halperin 2022 |
| 25 | Tsoukos 2021 EMG + velocity to failure (extended) | n=14, 40/60/80% 1RM; MDF drop larger at 40/60% |
| 26 | "Estimating proximity to muscular failure using surface EMG and deep learning" | DOI 10.1016/j.jelekin.2026.103111; LSTM MSE 49.44±18.34 |
| 27 | MDF recovery vs force recovery (extended) | lumbar MDF 1-6 min, dissociated from pH and force; elbow flexor plateau 2-5 min |
| 28 | Morton 2019 J Physiol | DOI 10.1113/jp278056; sEMG amplitude unrelated to fibre glycogen depletion |
| 29 | velocity effect on MDF (extended) | no direct isolation study found; Gerdle 1992 |
| 30 | Yan 2025 bench tempo load MDF | Frontiers 10.3389/fphys.2025.1661217; n=10; 80%+fast tempo largest MDF decline |
| 31-32 | Sakamoto 2012 DOI | not confirmed |
| 33 | Rodríguez-Rosell 2021 | DOI 10.1111/sms.13967; no significant EMG changes |
| 34 | Izquierdo 2009 power + MDF repeated sets | not found; MSS DOI fragment unresolvable |
| 35 | biceps MDF typical values (extended) | conference abstract MPF ~77-79 Hz; fat r=-0.362 |
| 36 | "10.1249/MSS.0b013e3181edfa96" | no match |
| 37 | EMG amplitude rise at constant force | recruitment mechanism, mixed rate-coding evidence |
| 38 | Burden 2010 normalisation | JEK 20(6):1023-1035; MVC endorsed but "neither … guaranteed" |
| 39 | Burden 2010 DOI | 10.1016/j.jelekin.2010.07.004 via reference list |
| 40 | Dimitrov 2006 DOI | 10.1249/01.mss.0000233794.31659.6d via third-party page |
| 41 | Enoka 2008 DOI | 10.1113/jphysiol.2007.139477 confirmed |
| 42 | Martin & MacIsaac 2006 IZ shift | JEK 16(2):144-148; Nishihara 2013: IZ shift 3.9 mm acute vs 16 mm obtuse |
| 43 | Enoka & Duchateau 2016 | DOI 10.1249/mss.0000000000000929 |
| 44 | Brody 1991 pH MDF CV | citation only, J Appl Physiol 71:1878-1885 |
| 45 | IED effect on spectrum | simulation: IED ↑ raises ARV and MDF; EJAP 2014 IED 10-50 mm study |
| 46 | Disselhorst-Klug 2009 | abstract-level; DOI not confirmed |
| 47 | Halperin 2022 | DOI 10.1007/s40279-021-01559-x; underprediction 0.95 reps (95% CI 0.17-1.73), I²=97.9% |
| 48 | Sánchez-Medina 2011 | DOI 10.1249/MSS.0b013e318213f880 |
| 49 | Disselhorst-Klug 2009 DOI | not confirmed |
| 50 | MMG vs EMG dynamic fatigue | Beck 2005 BioMed Eng Online 4:67 |
| 51 | Farina 2014 update DOI | 10.1152/japplphysiol.00162.2014 |
| 52 | NIRS resistance exercise review | Miranda-Fuentes 2021 IJERPH (PMC8074101), 4 studies |
| 53 | Jenkins 2015 80 vs 30% | DOI 10.1007/s00421-015-3214-9; MPF final reps 71.6 vs 78.1% of MVIC |
| 54 | Walker 2012 DOI | not found |
| 55 | González-Izal 2010 J Biomech | DOI 10.1016/j.jbiomech.2010.05.009 |
| 56 | Schoenfeld 2014 | DOI 10.1007/s00421-014-2976-9 |
| 57 | MDF recovery between resistance sets (extended) | biceps: MF back near reference by 1 min (Res Sports Med 2008); no direct dissociation study |
| 58 | reliability MDF slope | elbow flexor 75% 1RM MF ICC 0.90-0.98; slopes less reliable than initial/final values |
| 59-61 | (biceps-curl MDF Hz; Potvin/Sundstrup DOIs; Tsoukos 2024 DOI) | **not run — search budget exhausted** |

## Audit-response searches (2026-11-02)


1. Mills 1982 J Physiol spectrum recovery: citation confirmed.
2. "clear dissociation between the recovery of intracellular pH": phrase not found; Béliveau 1992 and isolated-fibre work found.
3. Yan 2025 abstract: confirmed 80% + fast → greatest MDF decline, interaction p < 0.05.
4. Mills 1982 abstract: force t½ 30 s, MPF t½ 3 min.
5. Elfving 2002: EJAP 88(1-2):85-93 confirmed; abstract not retrieved.
6. González-Izal 2010b "46.6%": working paper only.

## A3

### A3 search log (2026-11-02)

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

## A4

### A4 search log (product translation)

All searches 2026-11-02 via the WebSearch tool (summaries only). **WebFetch failed for every host tried** (inara.technology, pmc.ncbi.nlm.nih.gov: ENOTFOUND in this session's network policy), so no full text was opened; access is SECONDARY/ABSTRACT throughout.

| # | string | source | useful hits |
|---|---|---|---|
| 1 | Inara wearable EMG muscle sensor inara.technology claims | WebSearch | none (patents only) |
| 2 | Athos EMG compression apparel validation study | WebSearch | Lynn2018 (JSSM 17:205); USC senior thesis (negative, not peer-reviewed) |
| 3 | Whoop strength trainer muscular load accuracy validation | WebSearch | WHOOP R&D blog; the5krunner 2026 article (Passive MSK) |
| 4 | (fetch) https://inara.technology | WebFetch | FAILED - host not allowed |
| 5 | (fetch) PMC5950737 | WebFetch | FAILED - host not allowed |
| 6 | Inara strength training wearable Australia muscle activation sensor pre-order | WebSearch | App Store "Inara: Ultimate Gym App" (Inara Technology Inc; "No Sensor" tiers); Fort (YC, IMU+HR); Innowearable Inno-X (thigh EMG band) |
| 7 | Lynn 2018 JSSM Athos wearable sEMG validity reliability | WebSearch | Lynn2018 details |
| 8 | mbody Myontec EMG shorts validation study | WebSearch | Colyer2018; Hermann & Senner 2020 (COI note) |
| 9 | Colyer McGuigan 2018 textile electrode EMG shorts | WebSearch | Colyer2018 details incl. CV 41-43% |
| 10 | Vitruve linear encoder validity reliability | WebSearch | RuizAlias2024 PLoS One |
| 11 | Strive smart compression EMG sports wearable claims | WebSearch | Saucier2021 Sensors |
| 12 | ADS1292R sinc3 digital filter -3 dB bandwidth 0.262 data rate | WebSearch | TI SBAS502C 0.262 x fDR; TI E2E 125 SPS example |
| 13 | sEMG median frequency repetitions to failure dynamic resistance predict RIR | WebSearch | Zhao2025 (PMC12667690); load-dependent MDF bench study |
| 14 | TGA excluded goods fitness wearable software | WebSearch | TGA excluded software guidance; Allens 2021/2022 |
| 15 | Gonzalez-Izal 2012 electromyographic models muscle fatigue | WebSearch | record + DOI only |
| 16 | drop set electromyography amplitude median frequency | WebSearch | IJSC 2023 leg-press drop-set RMS (not opened); no drop-set MDF study found |
| 17 | median frequency recovery time course after fatiguing contraction | WebSearch | handgrip 1980 (recovery <1 min, UNVERIFIED authors); 2015 MU study (MPF recovered by 10 min, RMS elevated) |
| 18 | "Changes in EMG and movement velocity during a set to failure..." | WebSearch | SJMSS 2021 abstract; Tsoukos & Bogdanis 2023 JHK |
| 19 | bench press 65% 1RM RPE velocity loss MDF 2025 | WebSearch | Zhao2025; Rodiles-Guerrero 2022 |
| 20 | Weakley 2021 VBT devices review | WebSearch | Weakley2021 Sports Med; Wannouch 2025 PLoS One |
| 21 | wearable sEMG machine learning RIR proximity to failure | WebSearch | arXiv 2512.11854, 2510.03197 (preprints); a USPTO patent "Reserve estimates during resistance training" (modality unknown) |
| 22 | SENIAM IED 20 mm orientation Hermens 2000 | WebSearch | secondary citations only |
| 23 | Athos MAD Apparel shut down status | WebSearch | no current status found |
| 24 | MyoWare 2.0 validity research grade | WebSearch | York U thesis (original MyoWare, curls, SNR 10-33 dB); SparkFun paused sales of MyoWare 2.0 |
| 25 | SJMSS 2021 bench 40/60/80% authors | WebSearch | authors not found |
| 26 | PMC12667690 details | WebSearch | Zhao et al. author list |
| 27 | Yan 2025 Front Physiol load and tempo bench EMG | WebSearch | Yan2025 details |
| 28 | Gonzalez-Badillo 2017 velocity RIR equations | WebSearch | IJSM 2017 DOI; Garcia-Ramos 2018 IJSPP (individualisation) |

## A5

### A5 search log (validation and experimental design)

Date for all searches: 2026-11-02. Tool: WebSearch (standard). WebFetch was attempted on e-space.mmu.ac.uk,
pubmed.ncbi.nlm.nih.gov and link.springer.com and failed with DNS resolution errors (host outside the session's
allowed network domains); no full texts were read. The shared web-search budget for the turn was exhausted before
three final verification searches (de Vet 2006; Jukic 2023/2024 details; García-Ramos 2018 details) could run.

| # | search string | source | useful hits |
|---|---|---|---|
| 1 | Weakley 2019 visual feedback velocity bench press squat "augmented feedback" resistance training adaptations | web | Weakley2019a (JSCR 33(9), n=15); pointer to 4-week rugby study |
| 2 | Jiménez-Alonso 2022 velocity feedback resistance training performance randomized | web | Bibliographic record JSCR 36(6):1511-17, DOI 10.1519/JSC.0000000000003705; Orange2022 mention; no abstract |
| 3 | Lu 2016 sample size Bland-Altman agreement International Journal of Biostatistics | web | Lu2016 DOI 10.1515/ijb-2015-0039; MedCalc + blandPower implementations |
| 4 | Bonett 2002 sample size requirements estimating intraclass correlations desired precision Statistics in Medicine | web | Bonett2002 DOI 10.1002/sim.1108; worked example n=19.2 (reproduced by A5) |
| 5 | Zou 2012 sample size formulas estimating intraclass correlation coefficients precision assurance | web | Stat Med 31(29):3972-81; ICC.Sample.Size R package |
| 6 | Halperin 2022 accuracy in predicting repetitions to task failure ... Sports Medicine | web | Halperin2022: -0.95 reps, I2 97.9% |
| 7 | Saeb 2017 need to approach machine learning record-wise subject-wise cross-validation GigaScience | web | Saeb2017 gix019; commentary gix020 |
| 8 | wearable EMG garment validity reliability compared research-grade sEMG Athos Lynn 2018 | web | Lynn2018 JSSM 17:205-215, n=12 |
| 9 | Koo Li 2016 guideline selecting reporting intraclass correlation coefficients | web | KooLi2016 DOI 10.1016/j.jcm.2016.02.012 |
| 10 | Weir 2005 quantifying test-retest reliability ICC and SEM | web | Weir2005 DOI 10.1519/15184.1 |
| 11 | Weakley "Show me, tell me, encourage me" feedback 2020 | web | Weakley2020 JSCR 34(11); Weakley2023 meta-analysis g values |
| 12 | 2022 J Sports Sci meta-analysis VBT vs traditional ... four trials | web | Orange2022, 4 RCTs, 88 participants, SMDs with CIs |
| 13 | "Effect of Augmented Feedback on Velocity Performance During Strength-Oriented and Power-Oriented..." abstract | web | record only; SECONDARY summary via Weakley2023 |
| 14 | Weakley 2023 Sports Medicine "effect of feedback on resistance training performance and adaptations" | web | Sports Med 53(9):1789-1803, 20 studies |
| 15 | Weakley 2019 augmented feedback 4-week rugby union IJSPP | web | Weakley2019b IJSPP 14(9):1205-11, n=28 |
| 16 | National Statement 2023 NHMRC effective 1 January 2024 risk levels | web | NS2023; lower/higher risk; 2025 edition status unclear |
| 17 | TGA wellness exclusion fitness software consumer health 2021 | web | TGA2021 guidance; every function must qualify |
| 18 | Riley 2020 BMJ sample size prediction model; Van Calster 2019 calibration | web | Riley2020 BMJ 368:m441; VanCalster2019 BMC Med 17:230 |
| 19 | Sánchez-Medina González-Badillo 2011 velocity loss MSSE | web | DOI 10.1249/MSS.0b013e318213f880; correlations SECONDARY |
| 20 | Hermens 2000 recommendations SEMG sensors placement SENIAM | web | Hermens2000 DOI 10.1016/S1050-6411(00)00027-4 |
| 21 | Bland Altman 1999 measuring agreement ... repeated measures LoA CI | web | BlandAltman1999 DOI 10.1177/096228029900800204 |
| 22 | validity linear position transducer GymAware ... 3D motion capture | web | Lorenzetti2017 (n=9); Dorrell (deadlift weaker), Mitter |
| 23 | Farina Merletti 2000 comparison of algorithms ... simulated signals median frequency | web | Farina2000 DOI 10.1016/S1050-6411(00)00025-0; Corvini 2022 simulation |
| 24 | Steele 2017 clarity in reporting terminology set endpoints | web | Steele2017a Muscle Nerve 56(3):368-74; Steele2017b PeerJ |
| 25 | Hopkins 2000 measures of reliability sports medicine | web | Hopkins2000 DOI 10.2165/00007256-200030010-00001 |
| 26 | González-Izal 2012 electromyographic models muscle fatigue review | web | record only, DOI 10.1016/j.jelekin.2012.02.019 |
| 27 | Riley 2024 BMJ evaluation of clinical prediction models part 3 external validation | web | Riley2024 BMJ 384:e074821; n=100 too small for calibration |
| 28 | between-day reliability surface EMG median frequency dynamic resistance ICC electrode reapplication | web | snippets only: biceps MF ICC 0.90-0.98 n=10 same site; quadriceps MF-slope low between days; forearm reapplication ICC<0.5 - primary studies UNVERIFIED |
| 29 | predicting RIR from velocity loss individual vs general equations Jukic / Morán-Navarro | web | Jukic2024 (Physiol Rep, PMC10901726), Jukic2023 (EJAP), García-Ramos 2018, Pérez-Castilla 2024 |
| 30 | de Vet Terwee 2006 agreement vs reliability | web | NOT RUN - budget exhausted |
| 31 | Jukic 2024/2023 author/DOI verification | web | NOT RUN - budget exhausted |
| 32 | García-Ramos 2018 IJSPP verification | web | NOT RUN - budget exhausted |

Fetch attempts (all failed, DNS): e-space.mmu.ac.uk (Weakley2023 PDF), pubmed.ncbi.nlm.nih.gov (Jiménez-Alonso
abstract), link.springer.com (Weakley2023).

Computation: sample-size worked examples computed in python3 (no scipy; t and chi-square quantiles hard-coded from
standard tables). Bonett formula validated against his published example.

## A6

### A6 search log — 2026-11-02

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
