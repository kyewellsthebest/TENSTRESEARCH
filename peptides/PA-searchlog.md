# PA search log (independent audit, 2026-11-04)

Tool: WebSearch (standard). **55 searches, 1 fetch.** Budget ~60.

**WebFetch re-test:** `https://pubmed.ncbi.nlm.nih.gov/37952131/` failed with `ENOTFOUND`, so the host is not on the network allow-list. No further fetches were tried. To read full texts, `pubmed.ncbi.nlm.nih.gov` and `pmc.ncbi.nlm.nih.gov` have to be allowed in the session's network settings.

**Random-sample seed:** `random.seed(20261104)`, then 15 rows drawn from the 103 study rows (all P1-P5 `-studies.csv` files) that the brief's named claims did not already cover.

| # | Query (abridged) | Used for |
|---|---|---|
| 1 | SELECT Lincoff 17,604 HR 0.80 | SELECT |
| 2 | STEP 1 -14.9/-2.4; extension regain | STEP-1, extension |
| 3 | SURMOUNT-5 -20.2 vs -13.7 | SURMOUNT-5 |
| 4 | SURMOUNT-1 15.0/19.5/20.9 | SURMOUNT-1 |
| 5 | retatrutide phase 2 Jastreboff 2023 | retatrutide ph2 |
| 6 | TRIUMPH-1 topline 2026 | TRIUMPH status |
| 7 | FDA Jan 2026 suicidality removal | FDA decision |
| 8 | EMA PRAC NAION 1 in 10,000 | NAION |
| 9 | Ashraf JAMA Netw Open 2024 | Ashraf |
| 10 | Liu 2007 GH elderly | Liu 2007 |
| 11 | CJC-1295 ConjuChem death 2006 | CJC-1295 |
| 12 | Nass 2008 FFM | Nass |
| 13 | Adunsky 2011 CHF | Adunsky |
| 14 | Nass 2008 visceral fat / insulin | Nass VAT (P2 error found) |
| 15 | Liu 2008 athletes | Liu 2008 |
| 16 | Falutz 2007 tesamorelin | Falutz |
| 17 | BPC-157 Lee 2021 / Lee 2025 | BPC-157 humans |
| 18 | BPC-157 Sikiric >80% | Sikiric dominance |
| 19 | TB-500 Ac-LKKTETQ Ho 2012 | TB-500 identity (P3 citation mix-up found) |
| 20 | ARISE-3 RGN-259 | ARISE-3 |
| 21 | TESTS BMJ 2025 HR 0.99 | TESTS (two HRs) |
| 22 | HEAL LL-37 phase IIb | LL-37 |
| 23 | collagen meta Sports Med 2024 | collagen MA |
| 24 | Kirmse 2019 | Kirmse |
| 25 | Cochrane Cerebrolysin 2023 | Cochrane (SAE wording) |
| 26 | Cochrane Cerebrolysin seven RCTs 1773 | Cochrane (counts) |
| 27 | elamipretide approval + MMPOWER-3 | approval only |
| 28 | RECONNECT Kingsberg 2019 | bremelanotide |
| 29 | afamelanotide EMA/FDA/TGA dates | afamelanotide |
| 30 | PCAC July 2026 votes | PCAC |
| 31 | FDA April 2026 Category 2 removals | April removals |
| 32 | WADA 2026 BPC-157 / TB-500 / AOD-9604 | WADA classes |
| 33 | Victoria retatrutide liver alert | Vic liver |
| 34 | WADA 2022 BPC-157 added to S0 | BPC-157 S0 |
| 35 | Victoria anaphylaxis advisory | Vic anaphylaxis (fatality found) |
| 36 | Peptide Clinics [2019] FCA 1107 | court case |
| 37 | TGA Poisons Standard BPC-157/CJC/ipamorelin/MK-677 | TGA scheduling (BPC-157 only confirmed) |
| 38 | Breindahl 2015 melanotan II | Breindahl |
| 39 | Janvier 2018 Talanta | Janvier |
| 40 | Delcourt 2023 | Delcourt |
| 41 | AU GLP-1 compounding ban | AU ban |
| 42 | melanotan II case reports; TGA schedule | MT-II harms; TGA scheduling conflict |
| 43 | MMPOWER-3 Karaa 2023 | MMPOWER-3 |
| 44 | tirzepatide ADA 51.1% | sample |
| 45 | Beck 2014 ipamorelin | sample |
| 46 | SURMOUNT-1 DXA | sample |
| 47 | TESICO aviptadil | sample |
| 48 | TAZPOWER | sample |
| 49 | Krug 2018 | sample |
| 50 | TGA MT-II 27 notices | sample |
| 51 | Murphy 1998 MK-677 | sample |
| 52 | Athira LIFT-AD | sample |
| 53 | Scenesse TGA 2020 | afamelanotide TGA |
| 54 | STEP 1 DXA | sample |
| 55 | NL005 Tb4 phase I | sample |

**Not searched (owed):** sample rows Tb4_PU, Gusev2018 and MHRA_FOI24_274; the TGA scheduling of CJC-1295, ipamorelin, MK-677 and melanotan II against the current Poisons Standard; the dihexa retraction claim; the MOTS-c CB4211 "suspended 2018" claim. **Retractions:** none of the verified papers turned up as retracted in search. No dedicated retraction-database check was possible.
