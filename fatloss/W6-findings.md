# W6 — Measuring body fat and fat loss (whole-body and regional)

Agent W6, 2026-11-04. Studies: `W6-studies.csv` (40 rows). Searches: `W6-searchlog.md` (32).

**Access caveat, read first.** PMC, Cambridge Core and Frontiers are blocked in this session (WebFetch: ENOTFOUND). **No full
text was read.** Every number below comes from search-engine summaries of abstracts/landing pages (access = ABSTRACT or
SECONDARY in the CSV). Several author lists and years are marked UNVERIFIED. Treat specific numbers as "abstract-level".

## Plain-English summary (10 lines)

1. "My arms are a higher body-fat % than my belly" is almost certainly a **ratio artefact, not more fat**: a % is fat divided
   by everything else in that region, and an arm is a thin cylinder with little lean tissue under the skin.
2. Geometry alone (my calculation, below): the *same* 6 mm layer of fat is ~16% of a 40 cm arm but ~8% of an 85 cm trunk.
3. DXA makes it worse: the "trunk" region's lean mass includes organs, gut and blood (MRI muscle is only ~30% of DXA trunk
   lean), which dilutes trunk %fat; arm values are extrapolated over bone pixels and depend on where the arm cut line is drawn.
4. Segmental BIA (InBody, Tanita, hand-electrode scales) makes it different again: the arms dominate the impedance signal,
   segment estimates are poor at the individual level, and an upper-body pump or water/carbs shift arm values within hours.
5. The right comparison is **absolute fat thickness in mm** (skinfold or ultrasound) at triceps vs abdomen, or **regional fat
   mass in kg** on DXA — not regional %. In men, abdominal subcutaneous fat is usually the thickest site.
6. DXA is the best practical regional tool, but only standardised: overnight fast, no training that morning, voided, same
   scanner, same positioning. A carb-heavy day can shift DXA regional lean up to ~3% (individuals >9%).
7. Regional DXA fat precision is ~3–4% CV, so a real change needs ~9–11% of that region's fat mass (LSC = 2.77 × CV).
8. Smart scales track **weight** well (median error ≤0.3 kg) but miss fat mass by 2–4 kg (IQRs to 8 kg); never use them for regions.
9. A 250 kcal/day deficit is roughly 0.2 kg of fat a week — smaller than normal day-to-day water/glycogen swings, so track
   the **7-day average of morning weight** plus waist at the navel weekly, and judge over 3–4 weeks, not days.
10. Verdict on Kye's belief: the measurement is probably real but misread; verify with triceps vs abdominal skinfold (mm, same
    tester) and DXA regional fat **kg**, and expect the belly to carry more fat in absolute terms.

---

## 1. Why "arms have a higher %BF than my belly" is the expected artefact

### 1a. Geometry (calculation, not a study — evidence code: reasoning, strength n/a)
Model a limb or trunk as a cylinder with a uniform subcutaneous fat shell of thickness *t*. Fat area fraction =
1 − ((R − t)/R)². Mass fraction uses fat 0.90 g/cm³ and lean 1.06 g/cm³. (Script: arithmetic in this agent's run.)

| region (circumference) | fat layer | fat % by area | fat % by mass |
|---|---|---|---|
| upper arm 38 cm | 5 mm | 15.9 | 13.8 |
| upper arm 40 cm | 6 mm | 18.0 | 15.7 |
| upper arm 38 cm | 8 mm | 24.7 | 21.8 |
| trunk/waist 85 cm | 6 mm | 8.7 | 7.5 |
| trunk/waist 85 cm | 12 mm | 17.0 | 14.8 |
| trunk/waist 85 cm | 20 mm | 27.4 | 24.3 |

So an arm with **half** the subcutaneous fat thickness of the belly reads about the **same** regional %. This ignores visceral
fat (which adds to trunk %) and trunk organs (which dilute it, see 1b) — it is an illustration of scale, not a measurement.

### 1b. DXA-specific contributors
- **Trunk lean is mostly not muscle.** DXA-vs-MRI work found MRI muscle ≈ 0.30 of DXA trunk lean vs ≈ 0.70 in the legs
  [SciRep2023_DXAMRI, ABSTRACT]. Organs, gut contents and blood sit in the trunk denominator and lower trunk %fat.
- **Bone-pixel extrapolation.** ~40% of DXA pixels contain bone; soft-tissue composition there is extrapolated from
  neighbouring pixels, an assumption that fails when tissue over/under bone differs [BJN1997_DXAsoft, ABSTRACT]. Regions
  next to large bone areas (trunk, arms, head) have poorer precision (NCCOR guide, via search).
- **Arm cut lines and positioning.** Regional segmentation is drawn by software and adjusted by the technician; Nana 2015
  and Hind 2018 call for manual segmentation and foam positioning aids for limbs [Nana2015, Hind2018, ABSTRACT]. Broad
  shoulders/large arms touching the trunk or falling off the scan field move tissue between regions. Mechanism plausible;
  I found no study quantifying arm-%fat error from cut-line placement (gap).
- **Regional fat precision is the weakest DXA number.** Elite rugby league, GE iDXA, same-day repositioned: regional fat
  CV 3.1–4.1% (63–299 g) vs lean 2.0–2.4% [Barlow2015, ABSTRACT]. Arm-specific value not seen.
- **Hydration/glycogen.** A high-carb day raised DXA regional lean up to ~3% on average and >9% in individuals, and lowered
  DXA trunk fat up to ~3% [Tinsley2017]; glycogen depletion cut DXA leg lean 1.4% [Bone2017]. A depleted ("flat") day
  will also shift regional % — relevant because Kye wants to carb-cycle.
- DXA is fairly robust to an acute upper-body workout, unlike BIA [Rodriguez2023, ABSTRACT].

### 1c. Segmental BIA (InBody 770/570, Tanita, 8-electrode scales)
- **Limbs dominate the signal**: trunk ≈ half of body mass but ≈ 10% of whole-body impedance [Kyle2004, SECONDARY];
  5–12% of resistance (Dehghan & Merchant 2008, via search). Arm values are therefore the most signal-driven and the trunk
  the most equation-driven.
- **Individual segment error is large.** Wingo 2018 (n = 30): r > 0.87 in every segment, yet BIA over-read arm lean by
  0.97 kg and trunk lean by 5.58 kg, and under-read arm fat by 0.42 kg and leg fat by 1.94 kg [Wingo2018, ABSTRACT].
  InBody 770 trunk lean/fat only "moderate" agreement (CCC 0.90–0.95) [IranSegmental]; segmental BIA and DXA "not
  interchangeable" (n = 264) [MecherquesCarini2025]. Correlation ≠ individual accuracy.
- **Whole-body bias**: InBody 770 under-reads %BF and over-reads FFM vs DXA in trained adults [Antonio2019, McLester2020];
  MF-BIA %BF bias −4.0 ± 2.8 points, FM −2.9 ± 2.0 kg [MFBIA2024Military].
- **Acute state moves arm values.** Upper-body resistance exercise raised BIA TBW ~1 kg and FFM ~1.2 kg [Rodriguez2023]
  and segmental TBW/ICW/ECW [Florez_abstract]; muscle-damaging eccentric work changed the exercised segment's FM by −15.6%
  at 96 h with the other side unchanged [JPhysiolSci2019]. 2 L of water raised MF-BIA %BF 2–3 points — water read as fat
  [Jeong2023, SECONDARY]. Most BIA estimates did not return to baseline after an overnight fast following a diet change
  [Tinsley2017].
- Note: Wingo found BIA tends to *under*-read arm fat vs DXA, so segmental BIA is not consistently biased toward high arm
  %fat — but its regional output is noisy and the geometric ratio effect in 1a applies to any regional % from any device.

### 1d. Skinfolds
- Triceps is one of the most reliable skinfold sites; abdominal and iliac-crest folds are less reliable and novices exceed
  tolerable TEM there [Research Square preprint, search summary; not in CSV — preprint]. Biceps is the weakest site for both
  calipers and ultrasound [Muller2013].
- A large abdominal fold is hard to grip and calipers compress it — a source of *under*-reading the belly. If a gym used
  site-specific "%" outputs per site (some apps do), that is not a validated quantity.
- J-P 7- and 3-site equations were "not valid to detect" change in highly trained male athletes vs a 4C model
  [Silva_athletes_SKF, ABSTRACT]; equations tend to read low vs DXA (summaries; not in trained men).

## 2. Methods compared — what each is good for, and change needed to be real

| method | regional? | individual accuracy | precision / smallest real change | sensitivity to water/carbs/exercise | use for Kye |
|---|---|---|---|---|---|
| DXA (standardised) | yes (kg & %) | best practical; trunk % diluted by organs | regional fat CV 3.1–4.1% → LSC ≈ 9–11% of the region's fat [Barlow2015, Hind2018]; unstandardised scans double change-score noise [Nana2016] | carbs/food shift lean up to 3% regional [Tinsley2017, Bone2017]; robust to an acute workout [Rodriguez2023] | baseline + every 8–12 wk, fasted, same scanner |
| Segmental BIA / InBody | yes but poor | segments not interchangeable with DXA [Wingo2018, MecherquesCarini2025] | device-repeatability good, biology poor | large: water, upper-body training, diet [Jeong2023, Rodriguez2023, Tinsley2017] | trend only, same time/state; ignore segment % |
| Foot-to-foot smart scale | no | FM median error −2.2 to −4.4 kg, IQR to −8 kg [FrijaMasson2021] | weight excellent (≤0.3 kg) | large | weight only |
| Skinfold calipers (same trained tester) | site mm | equations biased in athletes | TEM sub-mm at good sites (ISAK thresholds not verified) | small (fluid trivial effect on surface anthropometry [Kerr2017]) | **best cheap regional check — use mm, not %** |
| B-mode ultrasound (Müller/ISAK) | site mm | 0.2 mm accuracy, 95% of observer differences within ±1 mm, ICC 0.998 [Muller2016] | ~1–2 mm per site | small | best regional check if available |
| A-mode (BodyMetrix) | site mm | SEE 2.6 %BF vs BOD POD in athletes [Wagner2016] | ICC ≥ 0.996 | small | acceptable tracker |
| Tape: waist | trunk only | n/a | self-measured TEM up to 0.76 in (~1.9 cm) in one study [WaistSelf2016]; measure 3× and average | small (bloating, food) | weekly, navel, morning, relaxed exhale |
| 3D optical scanner | shape + estimate | 3/4 scanners equivalent to 4C for groups, proportional bias [Tinsley2019_3DO] | %BF precision ~0.6% [Bennett_Styku] | moderate | ok for circumferences |
| 2D phone apps | no (whole body) | group-level OK, proportional bias [Graybeal2022]; one app over-read in youth [Minetto2023] | RMS-CV 0.5–3% | lighting/clothing | low priority |
| MRI/CT | yes, separates visceral | reference | n/a | n/a | research only |
| Progress photos | visual | none validated | not searched (budget) | lighting, pump, carbs | same light/time/state, monthly |

Ultrasound and DXA can disagree on *change*: in 20 resistance-trained men over 6 weeks, DXA fat-mass change correlated only
r = 0.49 (CCC 0.38) with total subcutaneous-thickness change, and not at all for the **arms** and lower body [Green2021,
ABSTRACT, small]. Arms are where every method is least consistent.

## 3. Tracking fat loss through water and glycogen swings

- Glycogen is stored with at least ~3 g water per g (up to ~17 g with ample fluid) [FernandezElias2015]. Kye's carb-cycling
  plan (high-carb training days, "flat" rest days) will therefore swing scale weight, BIA, DXA lean and even arm
  circumference day to day without any change in fat — the "flat" feeling is glycogen/water, not fat loss.
- Typical weekly weight cycle in free-living adults ≈ 0.35% (weekend up) [Turicchi2020].
- Arithmetic (rule of thumb, ~7,700 kcal/kg fat, which overstates real-world loss): 250 kcal/day ≈ 0.23 kg fat/week —
  below normal daily noise. Single weigh-ins cannot see it.

**Protocol:** weigh every morning after voiding, before food, same scale; use the 7-day rolling average and compare weeks.
Waist at the navel once a week (mean of 3). Triceps + abdominal (+ subscapular, thigh) skinfolds or ultrasound every 2–4
weeks by the same person, in mm. DXA at baseline and 8–12 weeks, under Nana's best-practice conditions, and make
regional decisions only on changes larger than the LSC. Never compare a scan or BIA reading from a high-carb day with one
from a low-carb day.

## 4. How Kye should verify the "fat arms" claim

1. Find out **which device** produced the number. If segmental BIA or a smart scale: discard the regional %; it is the
   least valid number on the list (sections 1c, 2).
2. If DXA: read the **fat mass in kg** per region and compare arms-to-trunk *kg* with typical male patterns, not region %.
   Remember trunk % is diluted by organs (section 1b) and arm % is inflated by geometry (1a).
3. Get **site thickness**: triceps and abdominal skinfolds (or B-mode ultrasound) by one trained tester, three readings each,
   same side, morning, no training beforehand. If the abdominal fold is thicker than triceps — the usual male pattern, with
   trunk sites rising faster than limb sites as men fatten (search summaries, centripetal-pattern studies) — the arms are
   not "fatter"; they just have less muscle under the same skin.
4. If triceps is genuinely thicker than abdomen in mm, that is an individual fat-patterning difference (largely genetic/
   hormonal), and still not something arm training will spot-reduce (other agents cover spot reduction).

## 5. Where the evidence is weak / gaps

- No full texts read; magnitudes are abstract-level.
- No study found that quantifies DXA arm-%fat error from cut-line placement or arm positioning in muscular men.
- No validated triceps:abdominal reference ratio for men.
- Smart-scale validation 2023–2026 in trained men: none found beyond blogs/vendor pages (excluded).
- ISAK TEM accreditation thresholds and progress-photo reliability: not verified/searched.
- Several samples are small (Bone n = 18, Green n = 20, Nana n = 21, Homer n = 4, Barakat n = 1) and some author groups
  (e.g. Antonio/ISSN) have supplement-industry ties — flagged in the CSV.
