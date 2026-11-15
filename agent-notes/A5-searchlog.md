# A5 search log (validation and experimental design)

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
