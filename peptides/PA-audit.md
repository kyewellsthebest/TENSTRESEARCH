# PA — Independent audit of the peptide round (P1–P5)

Auditor PA, 2026-11-04. I read BRIEF.md, every P1–P5 findings, studies and scores file, and P2's final versions (re-checked after the coordinator's note). I verified claims myself through search, and I did not defer to the agents. There is no dosing, cycling, reconstitution or sourcing information anywhere in my files.

Outputs: `PA-rank-research.csv`, `PA-rank-benefit.csv`, `PA-rank-safety.csv` (48 substances each), `PA-studies.csv`, `PA-searchlog.md`.

## 1. Access

- WebFetch was re-tested once on `pubmed.ncbi.nlm.nih.gov` and failed with `ENOTFOUND`. The host is not allowed. Every agent hit the same wall on PMC.
- **No full text was read by anyone in this round.** Everything is ABSTRACT or SECONDARY.
- I used 55 WebSearches.
- Random sample: seed `20261104`, 15 rows drawn from the 103 rows the brief's named claims did not cover.

## 2. Citation verdicts (brief's named claims)

| claim | verdict | note |
|---|---|---|
| STEP-1 −14.9% | VERIFIED | Placebo −2.4% is from my recall of the abstract, not re-retrieved |
| STEP-1 extension: two-thirds regained | VERIFIED | 11.6 vs 1.9 points; n=327 |
| SELECT HR 0.80 (0.72–0.90) | VERIFIED | n=17,604; AE discontinuation 16.6 vs 8.2% |
| SURMOUNT-1 | VERIFIED | Placebo −3.1% not retrieved |
| SURMOUNT-5 −20.2 vs −13.7% | VERIFIED | GI-discontinuation direction conflicts between sources: PARTLY |
| Retatrutide phase 2 (Jastreboff 2023) | VERIFIED | −24.2% is a 48-wk secondary endpoint; the primary was at 24 wk |
| TRIUMPH status | VERIFIED (topline) | TRIUMPH-1 −28.3% in the top-dose arm, AE stops 11.3 vs 4.9%. Not peer reviewed. No submission found, so P1's "BLA Q1 2027" is UNVERIFIABLE |
| FDA Jan 2026 suicidality | VERIFIED | 91 trials, 107,910 people |
| NAION (EMA) | PARTLY | EMA says "up to 1 in 10,000 people". P1's "per 10,000 person-years" misstates it |
| Ashraf 2024 | VERIFIED | Only 3 vials delivered |
| AU GLP-1 compounding ban 1 Oct 2024 | VERIFIED | ~20,000 patients |
| Tesamorelin Falutz 2007 | VERIFIED | VAT −15.2 vs +5.0% |
| MK-677 Nass 2008 | **PARTLY** | FFM, glucose and insulin are right. **"Abdominal visceral fat fell" is WRONG**: no significant difference. Limb fat rose |
| MK-677 hip-fracture CHF | VERIFIED | Stopped early. Counts 4/62 vs 1/61 are secondary |
| CJC-1295 trial death | VERIFIED / PARTLY | Halted 17 Jul 2006. An FDAnews item on "findings of patient death investigation" exists and was not read, so "never established in any source" overstates |
| GH metas | VERIFIED | Elderly review = **Liu 2007** (146:104). Athletes review = Liu 2008 (148:747). The brief's "Liu 2008 ×2" is wrong; P2 is right |
| BPC-157 human studies | VERIFIED | n=16/12/2, uncontrolled, same clinic owner. Author initial for 2025 differs between P3 (K) and P5 (J): UNVERIFIABLE |
| Sikiric dominance | VERIFIED | >80% of >190 papers, from one critic's count on one date |
| TB-500 ≠ Tβ4 | VERIFIED / PARTLY | P3 labels the Ghent `dta.1402` paper "Ho2012". That paper is Esposito et al.; Ho 2012 is J Chromatogr A |
| ARISE-3 | VERIFIED | n=700, missed primary, announced Mar 2021 |
| TESTS (BMJ 2025) | PARTLY | Two figures circulate: HR 0.99 (0.77–1.27) and 0.97 (0.76–1.24). Both are null |
| LL-37 phase IIb | VERIFIED | 148 randomised (144 treated per sponsor) |
| Collagen meta (ES 0.48) | VERIFIED | 19 RCTs, 768 people |
| Kirmse 2019 | VERIFIED | fCSA rose equally in both arms |
| Cerebrolysin Cochrane 2023 | VERIFIED | 7 RCTs, 1,773. Total SAEs RR 1.16 (0.81–1.66) **and** a moderate-certainty possible rise in non-fatal SAEs |
| Elamipretide approval Sept 2025 | VERIFIED | 19 Sep 2025, after a May CRL |
| MMPOWER-3 | VERIFIED | −3.2 m (−18.7 to 12.3), p=0.69 |
| RECONNECT | VERIFIED | n=1,267; no rise in satisfying events; nausea 40 vs 1.3% |
| Afamelanotide approvals | VERIFIED | EC 2014, FDA 8 Oct 2019, TGA Oct 2020 (ARTG 18 Nov 2020). P4's summary line "FDA, EMA and TGA 2020" is WRONG |
| Melanotan II case reports | VERIFIED (case level) | Naevi, melanoma, priapism, renal injury. Causation not established |
| Breindahl 2015 | VERIFIED | Sample description conflicts (3 shops vs 73 vials from 4) |
| Janvier 2018 | VERIFIED | 5–75% applies to cysteine-containing peptides only |
| Delcourt 2023 | VERIFIED | |
| PCAC July 2026 | VERIFIED / UNVERIFIABLE | BPC-157 8–6–1, MOTS-c 7–5–2, epitalon 7–4–1 VERIFIED. Semax "yes" and DSIP "no" confirmed, counts not seen. Some outlets say "four peptides", which is probably day 1 only |
| April 2026 Category 2 removals | PARTLY | Announced 15 Apr, effective 7 days later (~22–23 Apr). The exact list differs between sources |
| WADA: BPC-157 S0 | VERIFIED | Named in S0 since the 2022 List, the first named S0 example |
| WADA: TB-500 | VERIFIED **S2** | "Thymosin-β4 and its derivatives e.g. TB-500". Any S0 claim is wrong |
| WADA: AOD-9604 | VERIFIED **S2** | GH fragments, 2026 text |
| WADA: MK-677, GHRPs | PARTLY | S2.2.4 per P2/P5 federation copies. Not opened by me |
| TGA: BPC-157 S4 + App D | VERIFIED | Sport Integrity Australia |
| TGA: CJC-1295, ipamorelin, MK-677 | UNVERIFIABLE (by PA) | P2/P5 cite TGA FOI docs; I did not reach them |
| TGA: melanotan II | PARTLY | Prescription-only, no ARTG product (TGA 2026). A TGA page says MT-II is "not specifically scheduled" (captured by S4) and notes a **Schedule 10** application. P5's "S4 since 1 June 2018" is UNVERIFIABLE |
| Victoria retatrutide liver | VERIFIED, now dated | 6 cases at 19 Jun 2026; **7 by late August** |
| Victoria anaphylaxis | VERIFIED + addition | 13 since Jul 2025; 12 were first episodes. **At least one death**, linked by a coroner (Medical Republic). P5 omitted it |
| Peptide Clinics [2019] FCA 1107 | VERIFIED / PARTLY | A$10M, nine contraventions; the company was in liquidation and did not appear. P5's "obstructive" and "no medical justification" wording was not seen |

Random sample (seed 20261104):
- VERIFIED (9): Tirzepatide ADA, TGA MT-II notices, Beck 2014, TAZPOWER, Athira, SURMOUNT-1 DXA, Murphy 1998, STEP-1 DXA, FDA 503A list (MT-II before Feb 2027).
- PARTLY (3):
  - Krug 2018: the 5/21 figure was not seen.
  - NL005: n is 84 (54 + 30), and results exist.
  - TESICO: 473 enrolled, and the OR attribution conflicts.
- UNVERIFIABLE (3): Tb4_PU, Gusev2018, MHRA FOI.
- No retractions found. No retraction database was reachable.

## 3. Conflicts reconciled

1. **MOTS-c PCAC vote.** 7–5–2 is correct (P1). P5 lists MOTS-c among the six recommended, which is consistent. **P4 is wrong** to say "outcome not found" and "category not verified". MOTS-c was on Category 2, came off it in April 2026, and the PCAC voted to recommend it.
2. **BPC-157 Category 2 removal date.** Announced **15 April 2026**, effective about 22–23 April. P3's "15 or 23 April" are the two ends of the same event.
3. **TB-500 under WADA: S2, not S0.** P3 and P5 are right. A "one site says S0" claim should be dropped.
4. **AOD-9604 under WADA: S2 (GH fragment).** This resolves P1's S2-vs-S0 conflict.
5. **Epitalon, semax and DSIP PCAC outcomes.** P4 said "not found". The panel voted for epitalon (7–4–1) and semax, and against DSIP.
6. **Melanotan II, TGA.** P5 "S4 since 2018" vs TGA's "not specifically scheduled; captured by S4". Treat it as prescription-only. The 2018 date is unproven.
7. **MOTS-c analogue.** P4 says the CB4211 trial was "suspended in 2018 over injection-site reactions"; P1 does not mention it. **UNVERIFIABLE**, and it should not be repeated until a source is shown.
8. **Thymosin alpha-1 HR.** 0.99 vs 0.97. Both are in circulation and both are null. Report both.
9. **Retatrutide AE discontinuation.** TRIUMPH-1 gives 4.1/6.9/11.3% vs 4.9%. P1's TRIUMPH-4 conflict (12.2/18.2 vs 9/12) remains unresolved.
10. **Lee & Burgess 2025 author initial.** P3 has "K", P5 has "J". Unresolved.

## 4. Ranking method

- **Universe.** 48 substances: everything with its own section or scores row in P1–P4.
  - Orforglipron and MK-677 are included and labelled non-peptide.
  - Tesofensine and 5-amino-1MQ are excluded: non-peptides that P1 called out of scope.
- **(a) Research volume.** P5 rubric: approval +3, phase 3 +1, RCT volume up to +2. Ties broken by participants. Two auditor amendments, stated in each row:
  - An approval from a regulator other than FDA, EMA or TGA (Russia, China, Japan diagnostic, national EU) scores +1, not +3.
  - An approved drug gets the phase-3 point only for a phase-3 programme beyond the one that won approval (e.g. SELECT, MMPOWER-3).
  - Unpublished conference-abstract trials (BPC-157 enemas) score 0.
- **(b) Benefit.** P5 grades A–E on the best outcome, with the one-grade downgrades. Population and effect size are in every row. Within a grade, rows are ordered by effect size and certainty.
  - **Every A and B except collagen is in obesity or HIV, not lean lifters.**
  - Collagen is the only item with RCT evidence in resistance-trained people, and its effect may be connective tissue rather than muscle.
- **(c) Safety.** Sort by characterisation (C1 → C3 → CU), then severity S, then supply Q.
  - **Every CU ranks below every C1–C3**, whatever its apparent mildness.
  - Inside CU, substances with a mechanistic cancer flag (angiogenesis, telomerase, c-Met, IGF-1) rank lowest.
  - Gym-route substances whose only data are topical (LL-37, GHK-Cu) are ranked as injected, i.e. CU.
  - Retatrutide has C1 trial data, but every non-trial supply is grey market with a documented liver-injury cluster. So Q2 sets an S3 floor and it sits mid-table.

## 5. Caveats

- No full text was read. Every number is from abstracts or secondary summaries.
- Participant counts for CagriSema, survodutide, afamelanotide and orforglipron are estimates. The agents did not obtain them.
- The rubric rewards approvals in disease populations. hCG, oxytocin and sermorelin score high on volume while having nothing relevant to physique. Read volume and benefit together.
- The Q modifier assumes pharmaceutical-grade supply "exists somewhere". **In Australia, for every unapproved substance and for PT-141 and Tα1, the realistic route is grey market (Q2).**
- Theoretical S4 tags are mechanism-based, not observed harm.

## 6. Corrections each agent must accept

- **P1:**
  - NAION wording: "up to 1 in 10,000 users (EMA very-rare category)", not "per 10,000 person-years".
  - Mark "BLA Q1 2027" UNVERIFIED.
  - AOD-9604 is WADA **S2**.
  - Flag the conflicting SURMOUNT-5 GI-discontinuation direction.
- **P2:**
  - **Nass 2008 did not reduce visceral fat.** Fix the findings ("Abdominal visceral fat fell") and `P2-studies.csv` ("VAT decreased").
  - CJC-1295: say a company investigation report exists but was not read; do not say causality was "never established in any source".
- **P3:**
  - Re-key `Ho2012_TB500`. The dta.1402 paper is Esposito et al.; Ho 2012 is J Chromatogr A.
  - Drop the TB-500 "S0" aside.
  - BPC-157 Category 2 removal: announced 15 Apr 2026, effective ~22 Apr.
  - NL005: n is 84 and the results exist (mild AEs, no SAE).
  - TESTS: report both HRs.
- **P4:**
  - Afamelanotide dates: EC 2014, FDA 2019, TGA 2020.
  - PCAC outcomes exist: MOTS-c 7–5–2, epitalon 7–4–1, semax yes, DSIP no.
  - MOTS-c Category 2 status is known.
  - Retract or source the "CB4211 suspended 2018" claim.
  - Aviptadil: enrolment 473; check which endpoint OR 1.40 belongs to.
- **P5:**
  - Add the Victorian anaphylaxis **death** and the 7th liver case.
  - MT-II: "S4 since 2018" is unproven; a Schedule 10 application exists.
  - Remove "obstructive" and "no medical justification" from the FCA summary unless the judgment text is quoted.
  - The tirzepatide ADA data are from SURPASS (type 2 diabetes) trials.
- **Brief / coordinator:** the "Liu 2008 ×2" label is wrong. It is Liu 2007 (elderly) and Liu 2008 (athletes).
