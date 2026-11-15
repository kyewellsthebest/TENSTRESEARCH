# WA — Independent audit of the fat-loss round (W1–W6)

Agent WA, 2026-11-04. Adversarial audit. Every verdict comes from my own searches (`WA-searchlog.md`, 72 WebSearch
calls; budget ~60, overrun 12) or my own arithmetic (shown in section 2). Nothing is taken on an agent's word. Rows are in `WA-studies.csv`.

## Bottom line

- **No load-bearing citation is fabricated.** Every named study exists and its headline direction matches.
- **Four numbers are misread, and three of them matter for Kye.**
  1. **Huovinen 2015 does not show that a 300 kcal/day deficit "does nothing".** Energy intake fell significantly
     only in the 750 kcal group. The 300 kcal group's intake did not measurably fall. It shows a prescribed small
     deficit failing to happen, not a real small deficit failing to work. W5 and W1 both lean on it.
  2. **Garthe 2011's fast arm lost 1.0 %/week, not 1.4.** The 1.4 % was the target. Achieved rates were 0.7 % vs
     1.0 %. The lean-mass result is real; the contrast is smaller than W1/W5 state.
  3. **Nindl 1996 does not show that limb fat is "last to go".** The measured result is that Ranger candidates lost
     about half their fat from every region (arms, legs, trunk). The "fit fat" limb-persistence idea is the authors'
     interpretation. W3 built its arm explanation on that interpretation.
  4. **Tinsley 2017 is a feeding effect, not a carb effect, and it vanished after an overnight fast.** W6 says "a
     carb-heavy day can shift DXA regional lean up to ~3%". The abstract says the shift followed food "regardless of
     macronutrient content" and DXA returned to baseline after the next overnight fast. The right evidence for
     glycogen moving DXA is Bone 2017 (multi-day loading: +3.0 % lean, +3.1 % leg lean).
- **One omission matters:** in Redman 2009 (CALERIE), the metabolic adaptation W1 quotes (−431 / −240 kcal/day) was
  in the diet-only groups. In the **diet + exercise** group, body-composition-adjusted energy expenditure did not
  change. Kye exercises. The adaptation argument is weaker for him than W1 implies.
- **One inference is overstated:** W6's "almost certainly a ratio artefact" and W3's "most likely reason is that men
  hold limb fat last". In 852 young men on DXA, the arm was the **leanest** region by % in every ethnic group
  (Stults-Kolehmainen 2013, verified). Geometry alone would make arms read *fatter*. That they normally read *leaner*
  means men's trunk fat is normally much thicker than arm fat. If Kye's arms really read higher, the device is the
  first suspect, not biology.
- **Retractions:** Viana 2019 (BJSM) is retracted; W5 has it right. No other retraction surfaced. The Retraction Watch
  database was not queried directly, so this is not exhaustive.
- **Kye's model:** claim 1 right in kind, low on size. Claim 2 wrong as a mechanism. Claim 3 half right (carbs help
  hard, long sessions) and wrong on "flat burns fat". Claim 4: no spot reduction from limbs; the "arms fatter" reading
  is most likely a measurement or definition artefact.

---

## 0. Access

- **WebFetch re-test, 2026-11-04:** `https://pubmed.ncbi.nlm.nih.gov/24092765/` returned
  `getaddrinfo ENOTFOUND pubmed.ncbi.nlm.nih.gov`. Fetch is still blocked. pubmed.ncbi.nlm.nih.gov (and PMC) must be
  allowed in the session's network settings. Not retried.
- **Searches:** 72 WebSearch calls, standard mode. Budget was ~60; overrun of 12.
- **Access level:** every verdict is at the level of search-engine summaries of abstracts, repository records and
  publisher snippets. **No full text was read.** VERIFIED = bibliographic details plus headline numbers match an
  independent record. It does not mean methods were checked.
- **Seed for the random sample:** Python `random.seed(20261104)`, `random.sample(pool, 15)` over the 162 CSV rows
  not on the load-bearing list and not keyed UNVERIFIED. Kelly2009 was drawn twice (W4 and W6 rows), so 14 distinct
  papers were checked.

---

## 1. Citation verification

Verdicts: **V** verified · **P** partly (difference stated) · **U** unverifiable (reason stated) · **W** wrong.

### 1a. Energy balance and diet composition (W1, W2)

| item | verdict | what I found / what differs |
|---|---|---|
| Hall 2015 Cell Metab 22:427 | **V** | n = 19 obese, ward; 6 days at −30 % by cutting carbs or fat; fat loss 53 ± 6 vs 89 ± 6 g/day; carb cut raised fat oxidation, fat cut did not. |
| Hall 2016 AJCN (vol. 104 per W2; pages not seen by WA) | **P** | n = 17 overweight/obese men; 4 wk high-carb then 4 wk KD 15:5:80; order not randomised; chamber EE +57 kcal/d transient; body-fat loss slowed. **W1 attributes the 151 kcal/d DLW figure to the Friedman & Appel reanalysis.** My search output was garbled on this point; my recollection is that 151 ± 63 appears in Hall's own abstract. Unresolved. Do not quote the attribution. |
| Hall & Guo 2017 Gastroenterology 152:1718 | **V** | +26 kcal/d EE and +16 g/d fat loss on lower-fat isocaloric diets, P < .0001; ~32 controlled-feeding studies per one summary. Study count stays soft (20 vs 32). |
| DIETFITS, Gardner 2018 JAMA 319:667 | **V** | n = 609; −5.3 vs −6.0 kg; difference 0.7 kg (−0.2 to 1.6); genotype P = .20, insulin-30 P = .47. One press piece (TCTMD) wrongly reported a significant insulin interaction. |
| Ebbeling 2018 BMJ 363:k4583 | **V** | n = 164 randomised after ~12 % loss; TEE +209 kcal/d (91 to 326) low- vs high-carb, 20 wk maintenance. The dispute over the analysis plan is real (W1 states it fairly). |
| Romijn 1993 AJP 265:E380 | **V** | n = 5 trained; 25/65/85 % VO2max; peripheral lipolysis highest at 25 %; muscle TG lipolysis only at higher intensity; plasma-derived oxidation rises over 2 h at 65 %. "Plasma FFA supply most of the fuel at 25 and 65 %" is stronger than the abstract text I saw; at 65 % fat vs carbohydrate was roughly 50/50 per a GSSI summary. **P on that one phrase.** |
| Achten 2002 MSSE 34:92 | **V** | n = 18 **moderately** trained cyclists; FATmax 64 ± 4 % VO2max, 74 ± 3 % HRmax; zone 55–72 %. W1 says "trained". Minor. One summary attaches 56/64/58 % figures to a protocol comparison; not the headline. |
| Melanson 2009 J Appl Physiol 107:1847 | **V** | DOI 10.1152/japplphysiol.00958.2009; lean sedentary 10, lean trained 10, obese 7; 1 h at 55 %; 24-h fat oxidation unchanged when energy balance held; fat balance more positive on the exercise day (P < .01). W2's "citation only" can be upgraded. |
| Iwayama 2015 EBioMedicine 2:2003 | **V** | n = 10 non-obese men, chamber, energy-balanced; 24-h fat oxidation 456 control, 717 before breakfast, 446 afternoon, 432 evening kcal/d. |
| Schoenfeld 2014 JISSN 11:54 | **V** | n = 20 women (10/10), 4 wk hypocaloric, 1 h steady cardio 3×/wk; no between-group difference in any outcome. |
| Vieira 2016 BJN 116:1153 | **V** | −3.08 g (95 % CI −5.38 to −0.79) more fat oxidised fasted. 27 studies / 273 participants only in secondary write-ups. W1 had it SECONDARY/UNVERIFIED; W2 had it right. |
| Hackett & Hagstrom 2017 JFMK 2:43 | **P** | 5 studies, 96 participants; between-group effect on body mass trivial. **W2 says the between-group effects on %BF and lean mass were also trivial.** The abstract text I found gives *within-group* effects for those (small for %BF, trivial for lean mass, in females). Say "trivial for body mass; too few data for the rest". |
| Redman 2009 PLoS ONE 4:e4377 | **P** | −431 ± 51 (3 mo) and −240 ± 83 (6 mo) kcal/d, body-composition-adjusted, are for the **pooled CR + LCD groups**. **Adjusted TDEE was unchanged in the CR + exercise group.** W1 omits this. n not confirmed. |
| Glycogen-depletion MA 2025 Physiol Rep (doi 10.14814/phy2.70683) | **P** | Exists; 20 studies, 168 men + 12 women; depletion depends on intensity, duration, sets, training status. **"Higher intensity depletes less" and the set estimate (−11.2) not confirmed** in what I saw. Authors not retrieved. |

### 1b. Fasted training, refeeds, carbs, protein, TRE (W2, W5)

| item | verdict | what I found / what differs |
|---|---|---|
| Henselmans 2022 Nutrients 14:856 | **P** | 49 studies; carbs unlikely to matter in a fed state up to ~10 sets/muscle; long-term no effect in 15 (one each way). **Acute tally differs:** W2 says "none in 13, benefit in 6"; the author's own summary says 11 of 19 acute studies found no effect. Do not quote W2's split. |
| Campbell 2020 JFMK 5:19 | **V** | n = 27 RT men and women; 2-day carb refeed vs continuous, 7 wk; authors' claim of preserved FFM/RMR; Sainsbury reanalysis: only dry FFM differed. W2 has the journal right. |
| Peos 2021 ICECAP MSSE | **V** | n = 61 RT adults; 4 × 3-wk restriction with 1-wk breaks vs continuous, 12 wk; similar fat loss and FFM (56.7 kg both); less appetite with breaks. |
| Byrne 2018 MATADOR Int J Obes 42 (online 2017) | **V** | n = 51 obese men; fat loss 12.3 ± 4.8 vs 8.0 ± 4.2 kg; FFM loss similar; completer analysis (19 + 17). |
| Ho 2024 Nutrients 16:3066 | **V** | 7 RCTs, n = 164; fat mass WMD −1.52 (−2.30 to −0.75); no change in muscle or strength. **Energy intake was also lower with TRF** — confirms W2's "they ate less". |
| Morton 2018 BJSM 52:376 | **V** | 49 RCTs, n = 1,863; breakpoint 1.62 g/kg/d (95 % CI 1.03–2.20); mostly energy balance. |
| Helms 2014 IJSNEM 24:127 (protein) | **V** | 6 studies; 2.3–3.1 g/kg **FFM**, scaled with deficit and leanness; no study above 2.7 g/kg FFM tested. |
| Helms 2014 JISSN 11:20 (contest prep) | **V** | 0.5–1 %/wk confirmed by summary; protein and fat ranges appear in its table (row mapping not seen). Note: two different "Helms 2014" papers are cited under the same key in different files. |
| Longland 2016 AJCN 103:738 | **V** | n = 40 men, ~40 % deficit, RT + HIIT 6 d/wk, 4 wk; fat −4.8 vs −3.5 kg; LBM +1.2 vs +0.1 kg (from lead-author summary). **COI omitted by W2/W5:** Phillips reports dairy-industry funding. |
| Garthe 2011 IJSNEM 21:97 | **P** | n = 24 (13 slow, 11 fast), both sexes; LBM +2.1 % vs −0.2 %, p < .01; fat −31 % vs −21 %. **Achieved weekly loss was 0.7 % vs 1.0 %, not 1.4 %.** 12-month follow-up: no difference (verified). |
| Huovinen 2015 JSCR 29:29 | **P** | n = 15 (8 / 7) jumpers and sprinters, 4 wk; 750 group −2.2 kg mass, −1.7 kg fat, FFM held. **Energy intake fell significantly only in the 750 group.** The "300 kcal deficit produced nothing" reading is wrong: the 300 group did not demonstrably create a deficit. Diet was also lower-carb, so carb and energy are confounded. |
| Murphy & Koehler 2022 SJMSS 32:125 | **P** | ES −0.57 (lean), −0.31 (strength, NS); ~500 kcal/d meta-regression; mostly untrained. Study count disputed: W5's "59 studies, 1,495 people" vs a summary giving 7 RCTs (282) for the direct comparison plus a matched-study analysis. |
| Roth 2023 SJMSS 33(1) | **V** | n = 38 RT men, 3 vs 5 sets/exercise, intake 30 kcal/kg, wk 2–7; no difference in lean mass or muscle thickness. Upper-body training unsupervised; subjects not very lean; deficit modest. |

### 1c. Spot reduction and regional fat (W3, W4)

| item | verdict | what I found / what differs |
|---|---|---|
| Ramírez-Campillo 2022 Human Movement 23(3) | **V** | doi 10.5114/hm.2022.110373 (online Dec 2021); 13 studies, 1,158 participants, 14–71 y; 37 comparisons, 17 favour trained limb, 20 untrained. Pooled g −0.03 (−0.10 to 0.05) seen in a secondary summary only. **Scope caveat no agent states:** it pooled *trained vs contralateral limb* designs. Abdominal RCTs such as Brobakken are outside it. |
| Kostek 2007 MSSE 39:1177 | **V** | n = 104 (45 M, 59 F), 12 wk non-dominant arm; skinfold fell in trained arm in men (P < .01); MRI: no between-arm difference. |
| Ramírez-Campillo 2013 JSCR 27:2219 | **V** | 7 M + 4 F; one leg, 960–1,200 reps; total fat −5.1 %; trained leg n.s.; arms −10.2 %, trunk −6.9 %. Arm/trunk loss exceeded the trained leg's but **not the control leg's**. |
| Katch 1984 RQES | **V** | 13 experimental + 6 control men; 5,004 sit-ups in 27 days; fat-cell diameter fell at all three sites equally. W3 calls the 13 "trained"; they were the training group. Trivial. |
| Vispute 2011 JSCR 25:2559 | **V** | n = 24 sedentary; 6 wk ab training; no change in any fat measure; curl-ups improved. |
| Brobakken 2023 Physiol Rep (phy2.15853) | **V** | n = 16 overweight men, 10 wk, abdominal endurance work + treadmill vs treadmill; DXA trunk fat −1,170 g (7 %) vs no change; **net difference 697 g** (W3 had this UNVERIFIED; now verified); total fat loss similar. |
| Paoli 2021 IJERPH 18:3845 | **P** | Exists; SR circuit reduced body mass and abdominal SC thickness (ultrasound). **Sample inconsistent: abstract n = 14, full text 18 (9 M, 9 F).** Group × time contrast not seen. |
| Scotto di Palumbo 2017 JSMPF 57:794 | **V** | n = 16 inactive women, 8 wk; upper-body RT group lost −12.1 % arm vs −4.0 % leg fat (P = .02); reverse in the lower-body group. DXA + skinfold. |
| Stallknecht 2007 AJP-Endo 292:E394 | **V** | Blood flow and lipolysis higher in SCAT next to contracting muscle at all intensities; "spot lipolysis". Year listed 2006 online. n = 10 not confirmed. |
| Heinonen 2012 J Appl Physiol | **V** | n = 6 women, PET; adipose blood flow rose only next to active muscle (rest 1.0 ± 0.3 ml/100 g/min). |
| Heinonen 2014 Circ J 78(6) | **V** | n = 9 men; 1.3 ± 0.6 → 8.0 ± 3.0 ml/100 g/min with exercise; 10.5 with adenosine. |
| Porcari 2005 JSSM 4:66 | **V** | 24 in stimulation group, 8 wk; strength +58 %, endurance +100 % vs +28 %; waist −3.5 cm; no change in weight or SC fat. The device maker cites it in marketing; funding still not seen. |
| Hernandez 2011 Obesity (doi 10.1038/oby.2011.64) | **V** | n = 32 non-obese women (14 lipo, 18 control); fat restored by 1 y, redistributed to the abdomen; treated thighs stayed reduced. "Upper abdomen" and "arms" are press wording. |
| Nindl 1996 MSSE 28:786 | **P** | n = 165 Ranger candidates, 14.7 % fat; −1,000 kcal/d, 13 % weight loss, 8 wk; **~half of fat lost from every region**; fattest quintile carried and lost a larger arm share. W4 reports this correctly. **W3 reports the authors' "limbs hold on" interpretation as the result.** It is not the measured result. |
| Chaston & Dixon 2008 IJO 32:619 | **V** | 61 studies; % weight loss the only predictor of VAT/SAT ratio (r = −0.29); VLCD edge gone by 12–14 wk. |
| Hallgreen & Hall 2008 IJO 32:845 | **V** | 37 studies, 1,407 people; VAT change set by fat-mass change and initial VAT/FM ratio; k = 1.3 ± 0.1, R² = 0.73. k is in the paper itself, not only the letter (W4 had it SECONDARY). |
| Stults-Kolehmainen 2013 Nutr Diabetes 3:e64 | **V** | n = 852 men 18–30; **arm the lowest fat % in all ethnicities.** This is the strongest single fact on Kye's question 4b. |

### 1d. Measurement (W4, W6)

| item | verdict | what I found / what differs |
|---|---|---|
| Bracco 1996 J Appl Physiol 81:2580 | **V** | n = 51 **women**; arms 47.6 % / legs 43.0 % of impedance vs 10.6 % / 34.8 % of FFM; trunk 10.0 % of impedance, 48.2 % of FFM. Women only: transfer to men is assumed. |
| Kyle 2004 Clin Nutr 23:1226 | **P** | Citation verified (ESPEN part I). The "trunk ≈ 10 % of impedance" figure was not in what I saw; Bracco carries it anyway. |
| Wingo 2018 Clin Nutr ESPEN 28:141 | **V** | n = 30; r > .87 every segment; arm lean +0.97 kg, trunk lean +5.58 kg, arm fat −0.42 kg, leg fat −1.94 kg. |
| Rodriguez / Tinsley 2023 JSCR 37:1042 | **V** | 14 M + 18 F **recreationally active**; upper-body RE raised BIA TBW ~1 kg, FFM ~1.2 kg; DXA changes negligible. |
| Tinsley 2017 MSSE 49:823 (DXA/BIA) | **P** | Feeding raised DXA lean up to 1.7 % total, 3 % regional; trunk fat down up to 3 %; **"regardless of macronutrient content"; DXA back to baseline after the second overnight fast**; BIA not. W6 frames it as a carb-day effect on DXA. That is wrong for fasted scans. The ">9 % in individuals" figure not seen. |
| Bone 2017 MSSE 49:1029 | **V** | 18 trained male cyclists; glycogen loading +3.0 % lean, +3.1 % leg lean; depletion −1.4 % leg lean; TBW +2.3 %. |
| Barlow 2015 J Clin Densitom 18:546 | **V** | 45 elite rugby league men, iDXA, repositioned; regional fat CV 3.1–4.1 % (63–299 g); total FM 2.3 %. |
| Frija-Masson 2021 JMIR mHealth 9:e22487 | **V** | Weight error ≤ 0.3 kg; fat-mass median error −2.2 / −4.4 / −3.7 kg; ~50 **hospital patients** per scale, not athletes. |
| Müller 2016 BJSM 50:45 | **P** | 0.2 mm accuracy (18 MHz); **ICC 0.998 and "95 % within ±1 mm" apply to sums of 8 sites (10–50 mm), not single sites.** W6 table presents them as site precision. |

### 1e. Exercise strategy (W5)

| item | verdict | what I found / what differs |
|---|---|---|
| Steele 2021 Sports 9:155 | **V** | Fat mass −0.016 (−0.07 to 0.04), FFM −0.0004; GRADE high. |
| Viana 2019 BJSM 53:655 | **V retracted** | Retraction Watch, Dec 2020; expression of concern June 2019. W5 correct. |
| Wewege 2017 Obes Rev | **V** | 13 trials; HIIT −1.7 kg, MICT −2.1 kg fat, no difference; ~40 % less time. **Omitted by W5:** running reduced fat mass; cycling had no significant effect. That sits awkwardly with W5's "prefer cycling" (which is about interference, not fat). |
| Nedeltcheva 2010 Ann Intern Med 153:435 | **V** | n = 10 (3 F, 7 M), 14 d each; fat 1.4 vs 0.6 kg, FFM 1.5 vs 2.4 kg. "55 %" is the cut in the *share* of weight lost as fat. |
| Careau 2021 Curr Biol 31:4659 | **V** | n = 1,754 (IAEA DLW database); compensation ~28 %, via lower BEE; higher with more fat. |
| Pontzer 2016 Curr Biol 26:410 | **V** | n = 332, five populations; TEE plateaus in the upper activity range. |
| Vissers 2013 PLoS ONE 8:e56415 | **V** | 15 studies, 852 subjects, no caloric restriction; g −0.497 (−0.655 to −0.340); ~30 cm² women, ~40 cm² men at 12 wk. |
| Schumann 2022 Sports Med (PMID 34757594) | **V** | 43 studies; max strength −0.06, hypertrophy −0.01 (n.s.), explosive −0.28; same-session worse (p = .043) than ≥ 3 h apart. |
| Wilson 2012 JSCR (PMID 22002517) | **V** | 21 studies; hypertrophy ES 1.23 (RT) vs 0.85 (concurrent); running, not cycling, impaired hypertrophy and strength. |
| Eddens 2018 Sports Med 48:177 | **V** | 10 studies; RT first +6.91 % (1.96–11.87) lower-body dynamic strength; no effect on hypertrophy, VO2max, body fat. |
| GLP-1 lean-mass MA, PMID 41877354 | **V (abstract) / P (numbers)** | Diabetes Obes Metab 2026;28(6):4818, doi 10.1111/dom.70666; lean share similar for drugs and lifestyle; RT + protein preserve muscle. Per-drug %s (35.2 / 25.4 / 26.8; lifestyle 26.2; lifestyle + RT 17.5) and "20 RCTs, 15,782" seen only in secondary summaries. Lifestyle + RT vs drug is a cross-trial comparison. |

### 1f. Seeded random sample (14 distinct papers)

| row | verdict | note |
|---|---|---|
| W6 Homer2024 | **V** | n = 4 men, crossover; CHO: mass +0.3 %, MT +2.1 %; placebo all down; authors say within measurement error. |
| W2 Escobar2016 | **V** | BJN; 3–7 g/kg/d borrowed from endurance; CHO restriction may not hurt acute RT. |
| W4 FriedKral1987 | **P** | Int J Obes 11:129; 26 F, 14 M severely obese. "Men larger internal fat cells" is loose: men's omental cells were as large as subcutaneous; women's were smallest. |
| W4 / W6 Kelly2009 (drawn twice) | **P** | PLoS ONE 4:e7038. Abstract: **adult values are total-body only**. W4's "adult trunk/limb fat-mass ratios given" not supported by what I saw; W6's "trunk:leg ratio" also not seen. |
| W5 SURMOUNT1DXA | **V** | n = 160 DXA substudy; ~75 % fat / ~25 % lean of weight lost, both arms. |
| W6 VBC2022 | **U** | Not searched; budget. Authors unknown. Do not cite. |
| W1 Hansen2005 | **U** | Only a reference-list entry found (Sports Med 35:363). Findings not seen. |
| W3 SanchisMoysi2019 | **V** | 7 + 7 children; abdominal SAT −48 % (P = .001), arms −17–18 % (n.s.); dominant = non-dominant arm. |
| W4 Looney2024 | **V** | Front Nutr 2024;11:1491931; **n = 14 (11 M, 3 F)**; InBody 770 FM −2.9 kg, %BF −4.0, FFM +2.8 kg. **Same paper as W6's MFBIA2024Military** (W6 marks authors UNVERIFIED). Merge the rows. |
| W1 Achten2003 | **V** | Achten & Jeukendrup, IJSM 24:603; 55 endurance-trained men; MFO 0.52 ± 0.15 g/min at 62.5 ± 9.8 % VO2max. |
| W6 MFBIA2024Military | **V** | = Looney 2024 above. |
| W6 Minetto2023 | **V** | Sci Rep; 124 M + 69 F youth players; app overestimated %BF by +3.7 / +4.6 points. |
| W1 Rosenbaum2008 | **V** | AJCN 88:906; 7 matched trios; adaptive thermogenesis persists > 1 y at ≥ 10 % reduced weight. |
| W5 Barakat2020 | **V** | SCJ 42(5):7–21; recomposition documented in RT individuals. Content beyond abstract not seen. |

Sample result: 10 V, 2 P, 2 U. No W. The rows are in better shape than the load-bearing interpretations.

### 1g. Book-keeping faults

- **Key collisions:** `Tinsley2017` is a TRF trial in W2 and a DXA/BIA feeding study in W6. `Helms2014` is the JISSN
  contest-prep review in W1/W5 and the IJSNEM protein review in W2. `Looney2024` (W4) and `MFBIA2024Military` (W6) are
  the same paper. `Kelly2009` appears in W4 and W6 with different readings.
- **Internal inconsistency in W1:** summary line 2 says 200–300 kcal/day is "0.25–0.35 % of body weight a week"; its
  own section 5 (and my arithmetic) gives 0.21–0.32 %.
- **W3's UNVERIFIED list can shrink:** Brobakken's 697 g and Nindl's citation (MSSE 28(7):786–793, n = 165) are now
  verified.

---

## 2. Arithmetic

All computed in this session (Python). Assumed man: 85 kg, ~15 % fat (12.75 kg fat, 72 kg FFM).

**2a. Deficit → weekly fat loss.**

| deficit | adipose @ 7,700 kcal/kg | pure lipid @ 9,400 kcal/kg | % body weight / wk (85 kg) |
|---|---|---|---|
| 200 kcal/d | 0.18 kg/wk | 0.15 | 0.21 % |
| 300 kcal/d | 0.27 | 0.22 | 0.32 % |
| 500 kcal/d | 0.45 | 0.37 | 0.54 % |
| 650 kcal/d | 0.59 | 0.48 | 0.70 % |

- 7,700 kcal/kg is adipose *tissue* (≈ 85 % lipid). DXA "fat mass" is closer to lipid (~9,400 kcal/kg). Measured
  on DXA, a 250 kcal/d deficit is ~0.19 kg fat/week at best, not 0.23.
- Reality is lower still. Part of each kg lost is lean tissue and glycogen water, and expenditure drifts down (Hall
  2011 dynamic model; Careau 2021 compensation ~28 % of activity energy). All agents state the static rule
  overstates loss. Correct.

**2b. 0.5–0.7 %/week at 85 kg** = 0.43–0.60 kg/wk = **468–654 kcal/d** at 7,700 kcal/kg. W5's "450–650 kcal/day" is
right. 1 %/wk = 935 kcal/d.

**2c. Cylinder geometry** (uniform shell; fat 0.90, lean 1.06 g/cm³).

| case | fat % by area | by mass | agent's figure |
|---|---|---|---|
| 40 cm arm, 6 mm | 18.0 | 15.7 | W6: 18.0 / 15.7 — correct |
| 85 cm waist, 6 mm | 8.7 | 7.5 | W6: 8.7 / 7.5 — correct |
| 85 cm waist, 12 mm | 17.0 | 14.8 | W6 correct |
| r = 5 cm, 5 mm | 19.0 | 16.6 | W4: 19 — correct |
| r = 15 cm, 5 mm | 6.6 | 5.6 | W4: 6.6 — correct |
| 40 cm arm, 5 mm | 15.1 | 13.1 | (realistic trained arm) |

The sums are right. The **inference** is overstated. W4's r = 5 cm arm is a 31 cm arm; a trained man is nearer
38–42 cm, which lowers the effect. And the geometry predicts arms read *higher* than trunk at equal thickness. The
852-man DXA cohort says arms normally read *lowest*. So in real men the trunk shell is far more than twice the arm
shell, plus visceral fat. Geometry explains why the gap is smaller than the thickness gap. It does not explain a
reversal on its own.

**2d. DXA LSC = 2.77 × CV.** 2.77 = 1.96 × √2 (95 % confidence on the difference of two scans). Correct.

| CV | LSC |
|---|---|
| 3.1 % (Barlow regional FM, low end) | 8.6 % |
| 4.1 % (Barlow high end) | 11.4 % |
| 4.26 % (DPX-L arm FM) | 11.8 % |
| 7.8 % (Keil, wheelchair athletes) | 21.6 % |

- W6's "~9–11 %" is right (8.6 rounds to 9).
- **W4's "±50–80 g per scan" on a 1 kg arm is 1 SD for one scan, not the change needed.** The change needed is
  2.77 × that: ~140–220 g.
- Worked case: per-arm fat ~0.7 kg (assumed), LSC 9–11 % = 63–77 g. If arm fat falls in proportion to total fat
  (Nindl), a 0.25 kg/wk cut removes ~14 g/wk per arm. **About 5 weeks before one arm's change can be told from scan
  noise; about 10 weeks at the 7.8 % CV.** A single re-scan inside a month cannot answer Kye's arm question.

**2e. Glycogen and water.** 400–600 g glycogen × (1 + 3–4 g water) = **1.6–3.0 kg**. W1's "1.5–3 kg" is right. A
daily carb-cycling swing of ~1 kg equals 3.7–4.4 weeks of fat loss at 0.23–0.27 kg/wk. W1's "3–5 weeks" is right.

**2f. Upper bounds worth stating (new).**
- Fasted cardio: 3.08 g extra fat oxidised per session ≈ 28 kcal. Three sessions a week for a year = **0.48 kg**,
  and only if none of it is compensated. Melanson 2009 says it is compensated.
- Iwayama's before-breakfast effect: 717 − 456 = 261 kcal/d ≈ 28 g fat oxidised, at energy balance. Not fat lost.
- Hall 2015 gap: 89 − 53 = 36 g/d, the opposite direction to Kye's model.

---

## 3. Conflicts between agents, reconciled

**3a. Deficit size: Kye's 200–300 vs W1/W5's 0.5–0.7 %/week (~450–650 kcal/day at 85 kg).**
- Neither side has a trial in trained men that tests 250 kcal/day directly. Huovinen's 300 arm did not achieve a
  deficit. Garthe compared 0.7 % with 1.0 %, not with 0.25 %.
- What is solid: Garthe (0.7 % beat 1.0 % for lean mass, n = 24); Murphy & Koehler (lean gains fall toward zero near
  −500 kcal/d, mostly untrained); Roth 2023 (trained men lost some lean mass even at a moderate deficit).
- **Ruling:** W1/W5's range is better supported as a *default* for a man with fat to lose. 200–300 is not wrong; it is
  the slow end, and it is the same size as intake-logging error. **Define the deficit by outcome:** aim for 0.5 %/wk
  of body weight on the 7-day average (~0.4 kg/wk at 85 kg). Drop toward 0.3–0.5 % when lean or when main lifts fall
  for 2–3 sessions in a row. If Kye insists on 250 kcal, he must verify it on the trend, or it may be zero.

**3b. Protein: 1.6 g/kg (Morton) vs 2.3–3.1 g/kg FFM (Helms).**
- They answer different questions. Morton: mostly energy balance; breakpoint 1.62 g/kg BW with an upper CI of 2.2.
  Helms: lean, trained, in a deficit; 6 studies; no arm above 2.7 g/kg FFM.
- In Kye's units (85 kg, 72 kg FFM): Morton 136 g (to 187 g at the upper CI); Helms 166–224 g = **1.95–2.63 g/kg BW**.
- **Ruling:** 1.6 g/kg BW is the floor, not the target, in a deficit. **~2.0–2.4 g/kg BW (170–205 g/d at 85 kg)**
  covers both bodies of evidence. Above ~2.6 g/kg BW there is no tested benefit. Longland's 2.4 g/kg result was in a
  40 % deficit in non-lifters, with dairy-industry funding on the author side.

**3c. Does fasted cardio have any small benefit?**
- Acute: yes, ~3 g more fat oxidised per session (Vieira). 24-h: yes, only on energy-balanced chamber days (Iwayama).
  When food matches the exercise, 24-h fat oxidation is unchanged and fat balance is, if anything, more positive
  (Melanson).
- Weeks: no detectable difference (Hackett, 5 trials, 96 people; Schoenfeld 2014). None in trained men.
- **Ruling:** no fat-loss benefit has been shown. The acute effect's ceiling is ~0.5 kg/year with zero compensation.
  It is too small to be worth a worse session. A metabolic-health effect (Edinburgh 2020, insulin sensitivity) is a
  different outcome and not relevant to Kye's goal.

**3d. A small abdominal spot effect?**
- Positives: Brobakken (n = 16 men, −697 g trunk DXA net, total fat equal); Paoli (n = 14 or 18, ultrasound);
  Scotto di Palumbo (n = 16 women, limbs, DXA, opposite-limb cardio).
- Negatives: Katch, Vispute, Kordi (abdomen); Kostek (MRI, n = 104, arms); the 2022 meta-analysis (g −0.03,
  37 comparisons, limb-vs-limb).
- The meta-analysis **does not cover abdominal designs** (no contralateral control exists for the trunk). Brobakken's
  trunk DXA includes visceral fat, which falls with aerobic and trunk work regardless of "spot" (Vissers).
- **Ruling:** limb spot reduction — strong evidence against. Abdomen — **unresolved, low certainty**. If an effect
  exists, it is hundreds of grams over 10 weeks, measured by methods that cannot separate it from visceral change.
  W3's verdict stands; its "moderate against" for the abdomen is one grade too strong.

**3e. Are arms "last to go" in men?**
- Nindl (n = 165 fit men, DXA): **about half of fat lost from every region.** Not limb-last. The fattest men lost a
  *larger* share from the arms.
- Stults-Kolehmainen (n = 852): arms are the leanest region by %.
- Chaston & Dixon; Hallgreen & Hall: visceral leads early, proportionally, and the lead shrinks with more loss.
- The 22-week PRONAF ordering (trunk > legs > arms) is SECONDARY in W4 and was not re-checked.
- **Ruling:** "arm fat is last to go in men" is **weakly supported** — an author interpretation, not a measured
  result. W3's "most likely reason your arms read fatter" is not supported. W4's ranking (device artefact first,
  definition second, biology last) is the better-founded one.

---

## 4. Verdict on Kye's model

| # | claim | verdict | why (mechanism) | evidence strength |
|---|---|---|---|---|
| 1 | Fat loss = a 200–300 kcal/day deficit | **Right in kind; low in size; fragile in practice** | Fat mass follows energy balance (Hall 2015; Hall & Guo 2017; DIETFITS). 250 kcal/d ≈ 0.19–0.23 kg fat/wk, ~0.25 % BW/wk at 85 kg: below the 0.5–0.7 % range where the athlete data sit, and the same size as logging error. Protects muscle; may not exist unless checked on the trend. | strong (energy balance); limited (optimal size in trained men) |
| 2 | Glucose is #1 fuel; fat burns only once glycogen is "flattened"; hence fasted cardio | **Wrong as a mechanism. Right only that carbs and insulin shift the fuel mix acutely.** | Fat is oxidised all the time; peak fat use at ~60–65 % VO2max with full glycogen (Romijn; Achten 2002/2003). Intensity sets the mix. More fat burned ≠ more fat lost (Hall 2015: 53 vs 89 g/d). Fasted cardio: +3 g/session, no difference over weeks. | strong (mechanism, wards); limited (fasted-cardio trials, small, none in trained men) |
| 3a | Lifters need carbs to fuel sessions | **Partly right** | Little effect fed at ≤ 10 sets/muscle; benefit mainly vs fasted training and high volume; benefits confounded with extra energy (Henselmans). | moderate |
| 3b | Few carbs on rest days to be "flat" burns more fat (carb cycling) | **Wrong as a mechanism; no supporting trial** | "Flat" = less glycogen and water (Bone 2017; Fernández-Elías 2015). Weekly fat balance follows the weekly deficit. Refeed/diet-break RCTs in trained people show no added fat loss (Campbell 2020; ICECAP). Harmless as a scheduling tactic if weekly calories hold. | moderate (mechanism); limited (no direct carb-cycling RCT) |
| 4a | Can fat be lost from specific limbs? | **No** | Spot lipolysis is real and acute (Stallknecht; Heinonen); released fat is burned anywhere and the depot refills. MRI (Kostek) and the meta-analysis (g −0.03) are null. Abdomen: unresolved, small at most. Only liposuction or cryolipolysis remove local fat, and liposuction fat returns elsewhere (Hernandez). | strong (limbs); low (abdomen) |
| 4b | Why do his arms read higher % than belly or chest? | **Most likely a measurement or definition artefact** | Segmental BIA over-weights the arms (47.6 % of impedance, 10.6 % of FFM — Bracco) and moves ~1 kg after upper-body training (Rodriguez 2023). A ratio on a thin cylinder inflates arm % (section 2c). On DXA, men's arms are normally the *leanest* region (852 men). Belly fat in men is partly visceral, invisible to pinch and mirror. "Arms are last to go" is weak (Nindl: proportional loss). | moderate (device and definition); weak (biological order-of-loss) |

---

## 5. Fact-checked plan: trained man, fat loss, keep muscle

Each line carries its evidence grade. Numbers assume 85 kg; scale to body weight.

1. **Deficit by outcome, not by calculator.** Target ~0.5 % of body weight per week on the 7-day average of morning
   weight (~0.4 kg/wk; ~450–500 kcal/d nominal). Range 0.3–0.7 %. Go slower when lean or when strength drops.
   *Moderate* (Garthe; Helms JISSN; Murphy & Koehler).
2. **Adjust every 2–3 weeks** by ~100–200 kcal/d if the trend misses. Never from a single weigh-in. *Inference from
   measurement noise* (section 2e; Turicchi 2020).
3. **Protein 2.0–2.4 g/kg body weight per day (170–205 g).** Floor 1.6 g/kg. *Moderate* (Morton; Helms IJSNEM).
4. **Keep lifting heavy and progressively.** Same lifts and loads, 0–3 reps in reserve. Volume can drop from 5 to 3
   sets per exercise without extra lean loss (Roth 2023). Expect some DXA "lean" loss anyway; part is glycogen and
   water. *Strong* in untrained (Hunter; Geliebter); *limited–moderate* in trained (Roth, n = 38).
5. **Carbs where they help training.** Put most of the day's carbs before and after hard or high-volume sessions.
   Fewer on rest days is fine **only if weekly calories do not change**. It burns no extra fat. *Moderate*
   (Henselmans; mechanism).
6. **Do not train fasted to "burn fat".** Do cardio when it fits. Lifting fasted is where carbs most clearly help
   performance. *Limited* (Hackett; Schoenfeld 2014; Henselmans).
7. **Cardio as an energy lever, not a fat-burning zone.** 2–4 × 20–40 min, low-impact (cycling, incline walking,
   rowing). Interval and steady give the same fat loss (Steele 2021, GRADE high). Running costs more hypertrophy and
   strength than cycling (Wilson 2012). Lift first or separate by ≥ 3 h to protect strength (Eddens; Schumann).
   *Strong* (HIIT = MICT for fat); *moderate* (interference).
8. **Do not eat back exercise calories.** ~28 % of activity energy is compensated (Careau); TEE plateaus at high
   activity (Pontzer). Hold a fixed daily step floor. *Moderate* (compensation); *limited* (steps — no trial in
   dieting lifters).
9. **Sleep 7–9 h.** Short sleep shifted loss from fat to lean in a 10-person, 2-week crossover (Nedeltcheva).
   *Limited*, large effect.
10. **Diet breaks optional.** They reduce hunger but add no fat loss in trained people (ICECAP). Use them for adherence.
    *Moderate*.
11. **Measure the arm question properly, once.** Discard any smart-scale or segmental-BIA arm %. Get one DXA after an
    overnight fast, no training that day, ideally two same-day scans with repositioning to see the scanner's own
    noise. Read regional fat in **kg**, not %. Add triceps and abdominal skinfold or B-mode ultrasound in **mm** by
    one tester. Re-scan no sooner than 8–12 weeks (section 2d). Do not compare a scan after multi-day carb loading with
    one after depletion (Bone 2017: ±3 % lean). *Moderate*.
12. **Ignore:** spot work for fat, sauna suits, EMS belts, fat-burning creams, "stubborn fat" protocols. Train arms
    for muscle. A bigger muscle under the same fat looks leaner. *Strong (against the gadgets)*.

---

## 6. What remains owed

- Full texts: none read (PubMed/PMC blocked).
- Hall 2016: who reported the 151 kcal/d DLW figure.
- Henselmans 2022: the acute-study tally.
- Ramírez-Campillo 2022: the pooled g from the paper itself, not a summary.
- Glycogen MA 2025: "higher intensity depletes less" and the authors.
- Kelly 2009: whether adult regional ratios exist in the supplement.
- PMID 41877354: per-drug percentages from the abstract itself.
- A trial of carb cycling at matched weekly energy in trained men; a fasted-vs-fed body-composition trial in trained
  men; a unilateral arm trial under a controlled deficit measured by MRI. None exists in what any agent or I found.
