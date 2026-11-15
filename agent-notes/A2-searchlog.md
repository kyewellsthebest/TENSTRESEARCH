# A2 search log — surface EMG and fatigue

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
