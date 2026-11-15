# BA — Independent audit of the binge round (B1, B2)

Agent BA, 2026-11-08. Adversarial audit. Every verdict below comes from my own searches (42 WebSearch calls, 7 over
the ~35 budget; `BA-searchlog.md`) or my own arithmetic (section 2, recomputed in a script). Nothing is taken on B1's or B2's word.
Rows: `BA-studies.csv`. No WebFetch was attempted; PMC is known to be blocked in this session. So every source is
ABSTRACT or SECONDARY, as in B1 and B2.

Verdicts: **VERIFIED** (exists, and the number or direction used matches what I reached), **PARTLY** (exists, but a
number, n or inference is off or unconfirmed), **UNVERIFIABLE** (exists, but I could not reach the specific result),
**WRONG** (contradicted).

## Bottom line

- **Nothing is fabricated.** All 38 sources I checked exist. Headline directions match.
- **No citation is WRONG.** Two *inferences* are wrong or overstated, and one matters:
  1. **B1's "protein-forward surplus stores less fat" row is not supported by Bray 2012.** Bray's headline result is
     that **fat gain was similar at 5 %, 15 % and 25 % protein**. Extra protein added lean mass and resting expenditure
     on top. It did not cut fat storage. The only support left is Antonio 2014/2015: small, free-living, one lab.
     Drop the row's lower fat figure, or mark it H.
  2. **da Luz 2015 is softer than B2 says.** In people without BED, **4 of 11** interventions showed a significant
     *increase* in binge eating, 2 no change, 5 a decrease. B2's "some lower-quality studies showed a transient rise"
     understates that. The authors' own conclusion ("does not necessarily trigger") stands.
- **Minor misstatements.** Jebb 1996's overfeeding arm was **n = 3**, not stated by B1. Kolaczynski's 12-h leptin rise
  was on **120 kcal/kg**, about 10,000 kcal for Kye, ten times his Sunday. McDevitt 2001: in **obese** women glucose did
  not raise DNL; only sucrose did. Orsama's 59 %/60 % figures are stated as fact in B1 but are from a press summary.
- **B2 under-claimed Turicchi 2020.** The **0.35 %** within-week swing is in the abstract itself. Upgrade to VERIFIED.
  The Monday-high/Friday-low framing is not in the abstract.
- **Retractions.** Orsama 2014 and Helander 2016 both have Wansink as co-author. No retraction, correction or concern
  notice was found for either. The Retraction Watch database was not queried directly, so this is not exhaustive.
- **The arithmetic is right in both files.** One small slip in B2 (64 %, not 60 %). The B1/B2 tables differ only
  because B1 subtracts the 5–25 % thermic loss and B2 does not. Both are internally correct.
- **The biggest problem is not in either file. It is the deficit they assumed.** Both tables use deficits of
  250–750 kcal/day. Kye's own numbers imply about **900–1,700 kcal/day**. At that size, the Sunday cancels only
  **12–22 %** of the week, not 40–80 %. If his numbers are right, the Sunday is a small cost. And if his numbers are
  right, he should be losing about **0.45–0.97 kg a week**. If his trend is flat, the numbers are not right. Section 4.

---

## 1. Verification table

### 1a. Load-bearing citations

| key | used by | claim checked | verdict | what I found |
|---|---|---|---|---|
| Horton 1995 | B1 | fat 90–95 % stored, carb 75–85 % | **VERIFIED** | AJCN 62:19–29. 9 lean + 7 obese men, 14 d at +50 %. Fat 90–95 % in abstract; carb 75–85 % in full-text extract. Difference largest early. |
| Thearle 2013 | B1 | 24-h EE +10.7 % on 200 % overfeeding | **VERIFIED** | JCEM 98:2791. n = 20. 10.7 ± 5.7 % (2.9–18.8 %) on 20 %-protein diets. Attenuated at 3 % protein. r = −0.53 with fat. |
| Dallosso 1984 | B1 | +5.6/6.4 % EE = 9/11 % of surplus | **VERIFIED** | BJN 52:49–64. 8 men, 1 wk at +50 % fat. "Substantial fat deposition". |
| Jebb 1996 | B1 | fat balance 74 % of surplus | **PARTLY** | 74.1 % verified. CHO balance by ~day 5 verified. But only **3** men were overfed (6 in total, +33 %). B1 omits n. 540/551 g not seen. |
| Acheson 1988 | B1 | 15 g/kg; ~500 g before net DNL; 150 g/d | **PARTLY** | n = 3. 15 g/kg and 150 g lipid/d verified. The ~500 g figure is OCR-garbled in the abstract; one secondary gives ~800 g positive balance before RQ > 1. Point stands: one day cannot saturate glycogen. |
| McDevitt 2001 | B1 | DNL 2–3× "in lean and obese women" | **PARTLY** | AJCN 74:737. 8 lean, 5 obese, 96 h at +50 %. 2–3× in **lean** with both sugars. In **obese**, sucrose doubled DNL and glucose did not change it. "Does not contribute greatly to total fat balance" verified. |
| Bussau 2002 | B1 | glycogen max within 24 h | **VERIFIED** | EJAP 87:290–295. n = 8 trained men, 10 g/kg/d at rest. 95 → 180 mmol/kg wet mass in 1 day. **Needs rest**: Kye trains daily. |
| Dirlewanger 2000 | B1 | CHO overfeeding leptin +28 %, EE +7 %; fat neither | **VERIFIED** | IJO 24:1413. 10 lean women, 3 d per arm. Leptin change unrelated to EE change. |
| Kolaczynski 1996 | B1 | 12 h overfeeding, leptin +40 %, next morning | **VERIFIED** citation, **transfer weak** | JCEM 81:4162. n = 8 at **120 kcal/kg** in 12 h. That is ~10,400 kcal for 87 kg. Says nothing about +1,000. |
| Halliday 2020 | B1 | intake fell in OR (P = 0.03), not OP (P = 0.33) | **VERIFIED** | Obesity 28:259. 22 OP + 30 OR, 3 d at 140 %. PYY rose in OR only. Follow-up 4.0 ± 1.3 y; r = 0.35 not seen. |
| Bray 2012 | B1 | 3.16/6.05/6.51 kg; protein stores less fat | **PARTLY** | JAMA 307:47. n = 25, +954 kcal/d, 8 wk. Weights verified. **Fat gain similar in all three groups.** Low protein stored > 90 % of excess as fat; normal/high ~50 % fat + ~50 % lean. REE +160/+227 kcal/d. B1's "protein-forward retains less as fat" is not what Bray shows. |
| Schroor 2024 | B2 | 28 RCTs; FFM −0.20 kg | **VERIFIED** | Adv Nutr. TRE 7, ADF 10, 5:2 11. WMD −0.20 kg (−0.39 to −0.01, P = 0.044). Combined IER not superior. |
| Racette 2008 | B2 | weekend +0.06 kg/d; CR stopped losing; EX +0.08 | **VERIFIED** | Obesity 16:1826. n = 48, aged 50–60, 1 y. |
| Haines 2003 | B2 | +82 kcal/d (all), +115 (19–50 y) | **VERIFIED** | Obes Res 11:945. CSFII 1994–96, 2 recall days. Fri–Sun vs Mon–Thu. Activity not measured. |
| Orsama 2014 | B1, B2 | Sun/Mon peak; 59 %/60 %; Wansink | **PARTLY** | Obes Facts 7:36. n = 80. Co-author Wansink confirmed. No retraction found (not exhaustive). 59 %/60 % not confirmed by me. B1 states them as fact; B2 correctly flags them. |
| Turicchi 2020 | B2 | 0.35 % within-week; Mon high, Fri low | **PARTLY → upgrade** | PLoS One 15:e0232152. n = 1,421 weekly. **0.35 % is in the abstract.** Mon/Fri turning points not in abstract. Christmas +1.35 %. |
| Herman & Mack 1975 | B2 | restrained eat more after preload | **VERIFIED** | J Pers 43(4):647–660, doi 10.1111/j.1467-6494.1975.tb00727.x. B2 had DOI UNVERIFIED. Design via secondary accounts. |
| Westenhoefer 1999 | B2 | rigid → more binges; flexible → fewer | **VERIFIED** | IJED 26:53–64. Rigid: higher disinhibition, BMI, more and more severe binges. Distinct dimensions. |
| Stewart 2002 | B2 | rigid → ED symptoms; n = 188 | **VERIFIED** | Appetite 38:39–44, doi 10.1006/appe.2001.0445. Cross-sectional, nonobese women. |
| Linardon & Mitchell 2017 | B2 | intuitive eating most consistent | **VERIFIED** | Eat Behav 26:16–22. n = 372. Flexible benefit only after rigid controlled. |
| da Luz 2015 | B2 | no consistent link in non-BED | **PARTLY** | Obes Rev 16:652. Non-BED: **4 increased, 2 unchanged, 5 decreased** of 11. BED: decreased in all 4. B2 understates the increases. |
| Ganson 2022 | B2 | 60.9 % men, 53.7 % women; modal 1,000–1,499 kcal | **VERIFIED** | J Eat Disord 10:113, doi 10.1186/s40337-022-00642-6. n = 2,717. Cross-sectional. |
| Murray 2018 | B2 | 89 %; men: ED symptoms P = 0.04, OBE P = 0.03 | **VERIFIED** | Appetite 130:274, doi 10.1016/j.appet.2018.08.026. 89.1 % verified; association in men verified; no link to distress. n = 248 not seen by me. |
| Coelho do Vale 2016 | B2 | planned deviations help | **VERIFIED** | J Consum Psychol 26(1):17–28. Two experiments (simulated and real dieting) plus a third study. DOI not confirmed. |
| Andersen 1995 | B2 | 46 % binge after shows; 85 % regain | **VERIFIED** | IJED 18:49–57. n = 45 drug-free men, competition morning. 6.8 kg lost, 6.2 regained. |
| Goldfield 2006 | B2 | high binge/BN, esp. competitors | **VERIFIED** (direction) | Can J Psychiatry 51:160. "Especially competitors" share eating features with BN. Percentages and group n not seen by me either. |
| Mathisen 2019 | B2 | DE fell at show, worse 1 month after | **UNVERIFIABLE** | Sports 7:236 exists, aims match. The specific time-course results were not in what I reached. |
| DSM-5 BED | B1, B2 | criteria; ≥ 1/wk × 3 mo; severity bands | **VERIFIED** | InsideOut DSM-5/-TR sheets. Severity 1–3 / 4–7 / 8–13 / 14+. Sub-threshold "low frequency/limited duration" exists. |
| Butterfly helpline | B1, B2 | 1800 33 4673; 8 am–midnight, 7 days | **VERIFIED** | butterfly.org.au and healthdirect. 8 am–midnight AEST/AEDT, 7 days, **closed national public holidays**. Hours date from a Feb 2018 expansion. ReachOut still lists 8 am–9 pm weekdays: stale. Not a crisis line. |
| Lifeline | B1, B2 | 13 11 14 | **VERIFIED** | 24/7 phone. Text 0477 13 11 14. 000 if life in danger. |

### 1b. Seeded random sample (seed 20261108, from 36 unchecked unique keys)

| key | file | verdict | note |
|---|---|---|---|
| Davis 2016 | B2 | **VERIFIED** | EJCN 70:292, doi 10.1038/ejcn.2015.195. 8 studies. Comparable loss when restriction matched. B2 marked it SECONDARY; abstract is reachable. |
| Smith 1999 | B2 | **VERIFIED** | Appetite 32:295–305, doi 10.1006/appe.1998.0204. n = 223. r = 0.65 and 0.59 verified. |
| Mars105 sodium | B1 | **PARTLY** | It is Rakova et al. 2013, Cell Metab 17:125–131. Na stores cycle independent of intake. "No weight change" comes from a separate Mars500 abstract. |
| Headland 2016 | B2 | **VERIFIED** | Nutrients 8:354. 9 studies, 981 randomised, p = 0.458. |
| Byrne 2018 (MATADOR) | B2 | **VERIFIED** | Via WA-audit (prior round, own searches). 12.3 vs 8.0 kg fat, completers. Not re-searched. |
| Campbell 2020 | B1 | **VERIFIED** | Via WA-audit. n = 27; only dry FFM differed on reanalysis. Not re-searched. |
| Minehira 2004 | B1 | **PARTLY** | IJO 28:1291. 11 lean, 8 overweight. Lower DNL, higher glycogen synthesis in overweight: verified. B1's "175 % of needs, 71 % CHO" not seen by me. |
| Stice 2002 | B2 | **PARTLY** | Health Psychol 21(2):131–138 exists. Dieting as a predictor is how later papers cite it. Full predictor list not reached. |

**Tally (38 rows):** VERIFIED 27, PARTLY 10, UNVERIFIABLE 1, WRONG 0. The Kye-specific sources in section 4
(ten Haaf 2014, Lichtman 1992, Champagne 2002, training-cost and PAL sources) are extra rows in `BA-studies.csv`.

---

## 2. Arithmetic

Recomputed in a script. Constants: 9.4 kcal/g pure fat; 7,700 kcal/kg adipose tissue.

**Fat from +1,000 kcal.**
- B1: 750–950 kcal retained → 80–101 g pure fat → 97–123 g adipose. **Correct.**
- B2: all 1,000 retained → 0.106 kg pure fat ("≈ 0.11 kg"). **Correct.** As adipose tissue it is 0.13 kg. B2's "at most about 0.1 kg" is the pure-fat figure, not tissue. Trivial.
- B1 table rows (fat-heavy 96–101 g / 117–123 g, and so on): all **correct** to ±1 g.
- B1 "protein-forward 600–800 kcal retained": arithmetic correct, premise not supported (section 1).

**Glycogen, water, gut.**
- 100–300 g glycogen × 4 (1 g + 3 g water) = 0.4–1.2 kg. **Correct.** The 3 g/g is a floor (Fernández-Elías), not a constant.
- 3 g sodium = 130 mmol → 0.93 L isotonic. **Correct.**
- 100 g adipose ≈ 111 mL. **Correct.**
- Gut contents 0.5–1.5 kg: **estimate, no source.** B1 says so. Fine.
- Total +0.5–2.5 kg: sum of ranges, not measured. Note the tension with B2: daily-weigh studies show the *average* weekend swing is only 0.3–0.35 % (≈ 0.3 kg for Kye). The 2.5 kg top end is an upper bound for a very salty, high-carb, high-volume day, not the expectation.

**B1 weekly table** (5 × D deficit, Sunday retains 750–950):

| D | 5-day | with Sunday | share given back | days to cancel |
|---|---|---|---|---|
| 250 | 1,250 (162 g) | 300–500 (39–65 g) | 60–76 % | 3.0–3.8 |
| 385 | 1,925 (250 g) | 975–1,175 (127–153 g) | 39–49 % | 1.9–2.5 |
| 500 | 2,500 (325 g) | 1,550–1,750 (201–227 g) | 30–38 % | 1.5–1.9 |

All **correct**. B1's break-even "1,300–2,600 kcal depending on deficit" is right at the low end (1,316 at D = 250). At D = 500 it is 2,632–3,333.

**B2 weekly table** (Sunday counted in full):

| D | net | share cancelled | kg/week | without Sunday |
|---|---|---|---|---|
| 250 | −250 | 80 % | 0.032 | 0.162 |
| 500 | −1,500 | 40 % | 0.195 | 0.325 |
| 750 | −2,750 | 27 % | 0.357 | 0.487 |

All **correct**. One slip: with Fri/Sat at +300 each, the D = 500 week is −900, which is **64 %** cancelled, not 60 %.

**Reconciling B1 and B2.** They agree once you line them up.
- B1 subtracts the thermic loss (5–25 % of the surplus). B2 counts all 1,000 kcal. That is 50–250 kcal a week, or 6–32 g of tissue. Immaterial.
- They use different D grids. At D = 500 they give 30–38 % (B1) and 40 % (B2). Same answer.
- B1 anchors its headline (40–50 %) to a 0.25 kg/week target from the fat-loss round. B2 anchors to D = 250–750.
- **Reconciled rule:** Sunday cost ≈ (750 to 1,000) ÷ (5 × D). Use the B2 figure as the conservative one.

---

## 3. Reconciled verdict on Kye's three questions

1. **Does the Sunday add fat?** Yes: about 100–130 g of adipose tissue, or less if part of it is carbohydrate sitting as glycogen. It is not a separate lump. It is netted against the week. Over the week it adds fat only if the week is in surplus. *(I/M, moderate)*
2. **Monday "fatter", scale the same?** Glycogen water, gut contents and sodium. Typical weekend swing ≈ 0.3 kg; one big day can add more. Fat cannot be seen at 100 g. *(I, moderate for the rhythm; M for the cause)*
3. **Is it alright?** Physiologically, yes. The risk is behavioural: loss of control, escalation, compensation. Both files handle this well, and the help contacts are correct.

---

## 4. Kye-specific numbers

**Inputs (from chat, unverified):** 87 kg; 13.6 % body fat, device unknown; 1,800–2,000 kcal/day on 5 days; heavy
weights ~1.5 h/day; 2 × 20 min steady cardio (~200 kcal each) per week.

### 4a. Resting expenditure

- Lean mass = 87 × 0.864 = **75.2 kg**. Correct.
- Katch-McArdle: 370 + 21.6 × 75.2 = **1,994 kcal**. Correct.
- Cunningham: 500 + 22 × 75.2 = **2,154 kcal**. Correct.
- **Cunningham is the better of the two for him.** ten Haaf & Weijs 2014 (n = 90 recreational athletes, ~9 h/week,
  calorimetry) found Cunningham predicted RMR accurately. Harris-Benedict, WHO, Schofield, Mifflin and Owen were under
  50 % accurate. *(I, moderate; Dutch athletes 18–35)*
- **The body-fat figure barely matters.** At 10 % fat Cunningham gives 2,223; at 18 % it gives 2,069. Device error
  moves RMR by under ±80 kcal.

### 4b. Activity multiplier

- Coordinator: 1.5–1.6 × RMR. With its own inputs that gives **2,990–3,190** (Katch-McArdle) and **3,231–3,446**
  (Cunningham). The stated **2,900–3,300** is a little low at both ends of its own arithmetic. Small error.
- Is 1.5–1.6 plausible? It is on the low side for this load, not the high side.
  - DLW in 7 Japanese bodybuilders: TEE 3,432 ± 634 kcal, **PAL 2.00 ± 0.21**. *(ABSTRACT, Japanese; tiny n)*
  - Westerterp: DLW PAL tops out at about 2.0–2.4 in vigorously active people. *(ABSTRACT)*
- **Factorial check** (my build-up, M):
  - RMR (Cunningham) 2,150.
  - Thermic effect of food at ~1,900 intake: ~190.
  - Lifting: measured sessions are ~200–300 kcal per ~45–60 min. One review range is 64–534 kcal; volume drives it.
    For 90 min of heavy lifting with long rests, gross ~300–500, so **net ~170–370** after the 135 kcal of RMR that
    would be spent anyway. EPOC adds a median of ~40 (range 6–114). *(SECONDARY via reviews)*
  - Cardio: 400 kcal/week ≈ 57/day.
  - Everyday movement (NEAT): unknown. 300–900 kcal is a wide but normal range. This is the biggest unknown.
  - Total: **~2,900–3,700**. Dieting usually lowers NEAT and some adaptive thermogenesis, so the top end is unlikely.
- **Audit estimate of maintenance: ~2,900–3,500 kcal/day, central ~3,150.** The coordinator's range is defensible.
  The honest uncertainty is ±300 kcal, and it is mostly NEAT. Only weeks of weight-and-intake tracking will narrow it.

### 4c. Is 1,800–2,000 a ~1,000–1,300 kcal deficit?

- **On paper, yes, and possibly more.** Against 2,900–3,500, it is a **900–1,700 kcal** deficit. Central ~1,250.
- 1,800–2,000 is **below his own estimated RMR** (2,150). For an 87 kg lifter that is an aggressive cut.
- Energy left after exercise is about (1,900 − 300 to 450) ÷ 75 ≈ **19–21 kcal per kg lean mass per day**. That is low.
  (The common 30 kcal/kg threshold is mostly from women; it was not searched here. Treat it as a flag, not a verdict.)
- Protein at 1.6–2.2 g/kg is 140–190 g, or 560–770 kcal. That leaves little room for carbs to fuel 1.5 h of lifting.

### 4d. The under-reporting caveat. This is the important part.

- **Lichtman 1992** (NEJM 327:1893): 10 "diet-resistant" obese people under-reported intake by **47 ± 16 %** and
  over-reported activity by 51 %. Their expenditure was normal (within 5 % of predicted). Extreme, small sample.
  *(ABSTRACT)*
- **Champagne et al. 2002** (J Am Diet Assoc 102:1428): 7-day records against doubly labelled water. Non-dietitian
  women under-reported by **429 kcal/day** (significant). Even registered dietitians were 223 kcal/day under.
  n = 10 + 10. *(ABSTRACT; one index lists Monteiro first, so author order is PARTLY)*
- **The test is the scale trend, not the food log.** If Kye's numbers are right, he should lose about
  **0.45–0.97 kg a week**, central ~0.7 (table below). Part of that is water and lean tissue, so scale loss could even
  be larger early on.
  - **If his 4-week trend really is falling ~0.5–1 kg/week**, the numbers are roughly right. Then the Sunday is a minor
    cost and the bigger worries are lean-mass loss and the binge pressure of a hard cut (B2 §3e).
  - **If his trend is flat or slow**, then either intake is under-reported or maintenance is lower than estimated.
    Unlogged weekend eating is the usual culprit. One example: true weekday intake 25 % higher (~2,375), Sunday really
    +1,500, Fri/Sat each +300 over maintenance. That week nets only **~−1,775 kcal ≈ 0.23 kg**.
- "The scale reads the same on Monday" is not evidence of anything on its own. Compare 7-day averages, 4 weeks apart.

### 4e. Weekly maths for HIS pattern

Mon–Thu plus one more day at 1,800–2,000. Fri/Sat at maintenance (M). Sunday at M + 1,000. Sunday counted in full
(B2 convention). 7,700 kcal/kg.

| case | M | intake | daily D | 5-day deficit | net week | ≈ kg/week | Sunday share | without Sunday |
|---|---|---|---|---|---|---|---|---|
| low | 2,900 | 2,000 | 900 | 4,500 | −3,500 | 0.45 | 22 % | 0.58 |
| coordinator low | ~2,900–3,000 | ~1,900–2,000 | 1,000 | 5,000 | −4,000 | 0.52 | 20 % | 0.65 |
| **central** | **3,150** | **1,900** | **1,250** | **6,250** | **−5,250** | **0.68** | **16 %** | **0.81** |
| coordinator high | — | — | 1,300 | 6,500 | −5,500 | 0.71 | 15 % | 0.84 |
| high | 3,500 | 1,800 | 1,700 | 8,500 | −7,500 | 0.97 | 12 % | 1.10 |
| under-reported example | 3,150 | ~2,375 true | 775 | 3,875 | −1,775* | 0.23 | — | — |

\*Sunday +1,500 and Fri/Sat +300 each in that row.

Subtracting the thermic loss (B1 convention) adds 50–250 kcal to each net week. It changes nothing.

**Read for Kye.** On his own numbers, the Sunday costs **12–22 %** of the week's fat loss. That is far less than the
40–80 % in B1/B2's tables, which assumed much smaller deficits. Break-even would need a Sunday of about 4,500–8,500 kcal
over maintenance. The Sunday is not his problem. If anything is, it is either (a) a cut that is harder than it needs
to be, or (b) intake that is higher than he thinks. His weight trend tells him which.

---

## 5. Caveats

- **No full text.** All 38 rows are ABSTRACT or SECONDARY. Same limit as B1 and B2.
- **Kye's inputs are self-report from chat.** The body-fat device is unknown. Height, age, job and step count are
  unknown; NEAT dominates the uncertainty.
- **Training cost** comes from studies of shorter sessions, often in women. 90 min of heavy lifting is mostly rest
  between sets. I scaled; nobody measured him.
- **ten Haaf 2014** validates Cunningham in Dutch recreational athletes aged 18–35. Transfer to Kye is reasonable,
  not proven.
- **The bodybuilder PAL (2.00)** is from 7 people, read via a Japanese-language abstract record. Author not seen.
- **Retraction check** for Orsama/Helander used search, not the Retraction Watch database.
- **Bussau 2002** refilled glycogen at rest. Kye trains daily, so refill on a Sunday is plausible but not identical.
- **Not checked by me:** Schutz 1989, Flatt 1985, Levine 1999, Bouchard 1990/1996, Leaf & Antonio 2017, Antonio
  2014/2015, Heer 2000/2009, Helander 2016, Müller 2015, Harvie 2011, Cioffi 2018, Davoodi 2014, ICECAP, Hall 2008,
  Polivy 2010, Polivy & Herman 1985, Hoddy 2015, Pila 2017, Buechel 2026, Suffolk 2015, Alwan 2024, Chappell 2018,
  Schlögl 2015, Olsson & Saltin 1970, Fernández-Elías 2015. They are outside the sample.
- **Medicare eating-disorder plan details** remain unchecked, as both agents said.
