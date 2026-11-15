# W3 — Spot reduction: can fat be lost from one region by training it (or by anything else)?

Agent W3, 2026-11-04. Brief: `BRIEF.md` (Kye's question 4). Studies: `W3-studies.csv`. Searches: `W3-searchlog.md`.

**Access caveat that applies to everything below.** WebFetch could not reach any host from this session
(`pmc.ncbi.nlm.nih.gov`, `pubmed.ncbi.nlm.nih.gov` and `doaj.org` all failed DNS - those hosts have to be allowed
in the session's network settings before anyone can open full texts). Every number here comes from abstracts
quoted in search results, or from secondary write-ups, and each is marked as such. **No full text was read.**
Where a number is from a blog or press release rather than an abstract it is marked SECONDARY and should not be
quoted without checking.

## Plain-English summary (10 lines)

1. **Training a muscle does not meaningfully take the fat off that muscle.** The best synthesis (Ramirez-Campillo et al. 2022, 13 studies, 1,158 people) finds a pooled local effect of essentially zero: g = -0.03 (95% CI -0.10 to 0.05).
2. **The best single arm study agrees.** 104 people trained one arm for 12 weeks; MRI showed fat loss in *both* arms, no different between trained and untrained (Kostek 2007).
3. **Leg study, same answer, sharper.** 12 weeks of 960-1,200 leg-press reps per session on one leg: the trained leg lost nothing significant; the *arms* (-10%) and trunk (-7%) lost fat (Ramirez-Campillo 2013, n = 11).
4. **Sit-ups don't shrink belly fat** (Katch 1984: 5,004 sit-ups in 27 days, abdominal fat cells shrank no more than buttock or upper-back cells; Vispute 2011: 6 weeks of ab work, no change in abdominal fat).
5. **There is a real local effect in the fat, but it is acute and small.** Fat next to a working muscle gets more blood flow and releases more fatty acids during the session (Stallknecht 2007; Heinonen 2012). That released fat enters the bloodstream and is burned anywhere; the depot is refilled at the next meals. Across weeks it does not show up as local loss.
6. **A few small trials claim spot reduction** (Scotto di Palumbo 2017, n = 16; Paoli 2021, n = 14; Brobakken 2023, n = 16). They are small, use skinfold/ultrasound or regional DXA, and are outweighed by the null trials and the meta-analysis. Best honest reading: if any local effect exists it is a few hundred grams at most, hard to tell from measurement error.
7. **Skinfold results flatter spot reduction; MRI does not.** Skinfolds and ultrasound at one site are compressed and thinned by a growing muscle underneath; MRI of the whole limb is the better test, and MRI says no.
8. **Gadgets:** ab EMS belts strengthen muscle and can shave a little off a tape measure but did not reduce subcutaneous fat (Porcari 2005); sauna suits/wraps lose water; aminophylline creams have small, weak, mostly 1990s trials of thigh girth.
9. **Only things that physically destroy or remove fat cells reduce one spot**: cryolipolysis (~10-25% local fat-layer reduction in uncontrolled series) and liposuction - and after liposuction the fat comes back within a year, to the abdomen (Hernandez 2011).
10. **For Kye:** you cannot choose where fat comes off. Men lose it preferentially from the trunk first and hold it on the limbs until late - which is the most likely reason your arms read fatter than your belly or chest. The fix is total fat loss and time, not arm work. Train arms for muscle; muscle under the fat changes how the arm looks, not how much fat is on it.

**Verdict on Kye's question 4 ("can fat be lost from specific limbs?"): WRONG** if it means by training or by any non-surgical method that is practical for him. Evidence: moderate-to-strong (one meta-analysis with low heterogeneity, plus the best-designed within-subject MRI trial), with a small, inconsistent minority of positive trials.

---

## 1. The direct evidence - training a region and measuring fat there

### 1.1 Meta-analysis

**Ramirez-Campillo, Andrade, Clemente, Afonso, Perez-Castilla, Gentil (2022), Human Movement 23(3):1-14,
doi:10.5114/hm.2022.110373.** (The author list was verified; it is *not* Calatayud.) 13 studies, 1,158 participants
aged 14-71, comparing a trained segment with an untrained one. Pooled Hedges' g = **-0.03 (95% CI -0.10 to 0.05),
p = 0.508**, I² = 24.3%, Egger p = 0.133. Authors: no spot reduction "regardless of the characteristics of the
population and of the exercise program." [ABSTRACT via search snippet]

- What this means: the CI excludes anything larger than a trivial effect (|g| > 0.1) in either direction, so this
  is closer to *evidence of absence* than mere non-significance. Moderate-to-strong.
- Caveats: same lead author as one included trial (2013); several included studies are old, skinfold-based and in
  untrained people; one secondary source mentions durations of 2-20 weeks (not verified); the figure of "37
  comparisons" appears in a search summary but was not confirmed.
- A 2022 meta-analysis of the opposite hypothesis does not exist in what I found; nothing in 2024-2026 overturns it
  (searched; no new trials surfaced - see search log - but PubMed itself could not be opened, so a 2025-26 trial
  could have been missed).

### 1.2 Within-subject unilateral trials (the strongest design: the other limb is the control)

| study | n | what was trained | measure | result |
|---|---|---|---|---|
| Kostek 2007 MSSE | 104 (45 M, 59 F) | non-dominant arm, 12 wk RT | **MRI** + skinfold | MRI: SC fat fell in **both** arms, trained = untrained. Skinfold: trained arm fell in **men only** (p < 0.01). Authors: no spot reduction by MRI. |
| Ramirez-Campillo 2013 JSCR | 11 (7 M, 4 F) | non-dominant leg, leg press 960-1,200 reps, 10-30% 1RM, 3x/wk, 12 wk | **DXA** | Total fat 13.5 → 12.8 kg (-5.1%). Trained leg: no significant change. Arms **-10.2%**, trunk **-6.9%**. Energy intake unchanged. |
| Krotkiewski 1979 EJAP | 10 F (per secondary summary) | one leg, isokinetic, ~5 wk | ultrasound + skinfold + biopsy | SC thickness fell in the trained leg only, **but fat-cell size did not change**; muscle thickened. Authors: strength training "can hardly be used" for local fat loss. |
| Walts 2008 (PMC2991130) | 181 aged 50-85 | one leg, knee extension, ~10 wk | thigh imaging (CT/MRI, not verified) | SC and intermuscular fat **unchanged** in either leg; untrained leg as control. |
| one-legged aerobic cycling (author UNVERIFIED) | 8 F | one leg, 12 wk | regional | no body-composition change in the trained thigh |

The Krotkiewski result is the key to reading the positive skinfold/ultrasound studies: **the fat layer over a
muscle that grows gets thinner without losing fat**, because the same volume of fat is stretched over a larger
circumference and compressed against a firmer muscle. A single-site caliper or ultrasound reading then shows "local
fat loss" that a whole-limb MRI or fat-cell biopsy does not. That is exactly the Kostek split (skinfold yes, MRI no).

### 1.3 Abdomen

| study | n | design | result |
|---|---|---|---|
| Katch 1984 RQES | 13 trained + 6 controls, men | 27 days of sit-ups, 5,004 total | Fat cells biopsied at abdomen, subscapular and gluteal sites: abdominal cells did **not** shrink more than the other sites. Skinfold, girth and body composition did not change. |
| Vispute 2011 JSCR 25(9):2559-64 | 24 sedentary (14 M, 10 F), RCT | 7 ab exercises, 2x10, 5 d/wk, 6 wk | No change in weight, %fat, android fat (DXA), waist, or abdominal skinfold. Curl-up endurance improved (47 ± 13 vs 32 ± 9). |
| Kordi 2015 JMPT 38(3):203-9 | 40 overweight/obese women, RCT | diet vs diet + 12 wk ab resistance training | Ab training added **nothing** to abdominal SC fat thickness beyond diet. The only null trial where fat *was* being lost overall - so it is the most informative null. |
| Brobakken 2023 Physiol Rep (PMC10680576) | 16 overweight men, RCT | treadmill vs treadmill + torso rotation & crunches, 4 d/wk, 10 wk | DXA: authors report more trunk fat used in the abdominal group - "spot reduction exists". Secondary blog: trunk fat **-697 g more** with similar total fat loss (**UNVERIFIED**). |
| Paoli 2021 IJERPH 18:3845 | 14, RCT | 8 wk "spot reduction" circuit vs traditional RT | ultrasound + skinfold + BIA: SR group reduced body mass and abdominal SC fat (p < 0.05). Group-by-time contrast and effect sizes not seen. |

The two positive abdominal trials have a combined n of 30; they used ultrasound/skinfold (Paoli) or regional DXA
(Brobakken), whose trunk region cannot separate subcutaneous from visceral fat and moves with gut contents and
hydration. Brobakken's group also did extra work, so a slightly larger total deficit is a competing explanation.
Kordi (n = 40, diet-matched) and Vispute are negative. **Weight of evidence: no meaningful abdominal spot reduction;
a small effect cannot be excluded and would be at most a few hundred grams over months.**

### 1.4 Arms

Kostek (n = 104, MRI) is the decisive study and is null. Ramirez-Campillo 2013 lost the most fat from the arms
while training the leg. Scotto di Palumbo 2017 (n = 16 women, RCT, DXA) is the main positive one:
upper-body RT group lost more arm fat than leg fat (**-12.1% vs -4.0%, p = 0.02**) and the lower-body group the
reverse (legs **-11.5%** vs arms -2.3%). Note the design: each group's *cardio* was on the opposite limbs (upper-body
RT + cycling; lower-body RT + arm ergometer), so the authors' reading is "local RT mobilises the fat, cardio burns it".
Problems: n = 16, inactive women, 8 weeks, and DXA arm fat is a small number (of the order of 1 kg per arm in lean
people - not verified for this sample) so a 10% change is ~100 g, close to the precision of regional DXA. One
secondary source says the trunk showed no difference. [ABSTRACT + SECONDARY]

Gwinup, Chelvam & Steinberg 1971 (Ann Intern Med, "Thickness of subcutaneous fat and activity of underlying
muscles") is the classic tennis-arm citation: commonly summarised as dominant and non-dominant arms of tennis
players having the same fat thickness despite larger dominant-arm girth. **I could not find its abstract; its
results are UNVERIFIED** from this session. The same idea is confirmed independently and with better methods by
**Sanchis-Moysi 2019** (Front Pediatr, volumetric MRI, 7 child tennis players vs 7 controls): subcutaneous fat
volume was **similar in the dominant and non-dominant arm** in both groups, even though the racket arm does an
"enormous" amount more work. Tennis players had 48% less abdominal SC fat than controls (p = 0.001) but only
17-18% less (n.s.) in the arms - i.e. playing sport took fat off the trunk more than off the arms that were doing
the work. Tiny cross-sectional sample; consistent with everything else.

### 1.5 Thighs

Ramirez-Campillo 2013 (trained leg: no change), Walts 2008 (n = 181, no change), Krotkiewski 1979 (thickness yes,
fat cells no), one-legged cycling (no change). Scotto di Palumbo's lower-body group is the only positive.
**No meaningful thigh spot reduction.**

---

## 2. Mechanism: why there is a local signal at all, and why it doesn't add up

**The local effect is real, acutely.** Stallknecht, Dela & Helge (Am J Physiol Endocrinol Metab 2007; 292:E394,
online 2006): 10 fasted men did one-legged knee extension at 25%, 55% and 85% Wmax; femoral subcutaneous fat
next to the *working* leg had higher blood flow (133Xe washout) and higher lipolysis (microdialysis glycerol) than
next to the resting leg at every intensity. The authors' own phrase: exercise can induce "spot lipolysis".
Heinonen et al. (J Appl Physiol 2012, n = 6 women; PET) found the same: adipose blood flow rose with intensity
**only next to working muscle**; and (Circ J 2014, n = 9 men) adipose flow next to working quadriceps went from
**1.3 ± 0.6 to ~8.0 ml/100 g/min**. [ABSTRACT]

**Why it does not become local fat loss:**

1. **Released fat is not burned locally.** Fatty acids leaving adipose tissue go into the blood and are taken up by
   whichever muscle (or liver) is using them. Spot lipolysis changes where fat *leaves*, not where it is burned.
2. **Depots refill from what you eat.** Between sessions the meal fat and the fatty acids recycled by the body are
   stored again, and *where* they are stored is set by the depot's uptake, hormones (sex steroids, cortisol,
   insulin) and genetics, not by which muscle was trained yesterday. One review in the search set notes that
   regional differences in lipolysis do not explain fat distribution and that fatty-acid *uptake* matters more.
   Net change in a depot = what left minus what came back; training shifts only the first term, briefly.
3. **The size of the flux.** A rough arithmetic illustration (**mine, not from a paper**): if whole-body fat
   oxidation in moderate exercise is about 0.5 g/min drawn from ~15 kg of adipose tissue, that is ~0.03 g/min per
   kg. Even tripling that for ~250 g of fat over a working biceps gives ~1-2 g per hour of training. Over a block of
   training that is not nothing on paper - which is why the trials are needed - and the trials show it is refilled:
   MRI in Kostek, DXA in Ramirez-Campillo and the meta-analysis find no net local loss.
4. **Energy balance sets total fat loss; sex, age and genetics set the order.** Small direct-training session
   energy costs (Vispute: ~75 min/week of ab work) make no dent in a deficit either.

**Plain answer to "why":** the working muscle does pull a bit more fat out of the fat right next to it during the
session, but that fat is burned everywhere and the spot is topped up again from food, so after weeks the map of
where your fat is stored is unchanged.

---

## 3. Measurement - why the literature looks contradictory

| method | what it measures | bias for spot reduction |
|---|---|---|
| Skinfold at one site | compressed double fold of skin + fat at one point | **Flattered.** Thinner when muscle underneath grows/firms (Krotkiewski 1979, Kostek 2007 men). Poor agreement with DXA/MRI (cited in Brobakken 2023). |
| Ultrasound at one site | fat-layer thickness at one point | Same geometric problem; better than calipers but still one point. |
| Girth/tape | everything under the tape | Moves with muscle tone, posture, gut contents, water (see EMS, sauna suits). |
| Regional DXA | fat mass in a segment defined by cut lines | Whole segment, good; but arm segments are small (precision limited), cut-line placement varies, trunk can't separate visceral/subcutaneous. |
| MRI/CT volumetric | actual subcutaneous fat volume along the limb | **Best.** Kostek 2007, Walts 2008, Sanchis-Moysi 2019 - all null for local loss. |
| Fat-cell biopsy | adipocyte size at a site | Direct; Katch 1984 and Krotkiewski 1979 - null. |

Rule for Kye's own data: a caliper or tape change on a trained arm while you are also gaining muscle there is not
evidence of local fat loss.

---

## 4. Non-exercise "local" methods

| method | evidence | verdict |
|---|---|---|
| **Ab EMS belt** - Porcari 2005, J Sports Sci Med 4(1):66-75 | 8 wk, 5x/wk: ab strength +58%, endurance +100% (control +28%), waist -3.5 cm, **no change in body weight or subcutaneous fat**. Funding not verified - device-maker funding is plausible for this literature and should be checked before citing. Porcari 2002 JSCR (EMS on body comp): reportedly no differences (UNVERIFIED, forum source). | Muscle effect, no fat effect. Girth change is tone/posture. |
| **Sauna suit / neoprene wrap / waist trainer** - ACE-sponsored 2017 trial | 45 overweight adults, 8 wk exercise ± neoprene suit: body fat -13.8% vs -8.3% *relative* change, small absolute difference; **industry-sponsored, SECONDARY**. No waist-trainer RCT found. | Sweat is water, regained with the next drink. No credible local fat effect. |
| **Topical aminophylline / xanthine creams** - Greenway, Bray & Heber 1995 (Obes Res) review of their trials; Abdi Dezfouli 2023 (Front Endocrinol) systematic review | Small thigh trials (5-30 women), treated thigh lost more **girth** than untreated thigh; 0.5% five times weekly for five weeks called "most potent". Reviewers: more high-quality trials needed. | Girth, not fat mass by imaging; small, old, mostly one group's trials. Not worth money. |
| **Local heating** | No trial found in this search. Heating raises adipose blood flow (Heinonen 2014 shows adipose vessels can dilate well beyond exercise levels) but blood flow is not fat loss - the same argument as §2. | No evidence. |
| **"Targeted" diets** ("belly-fat foods", carb cycling for the abdomen) | None found that test a regional claim. Diet changes total fat; men lose trunk fat first whatever the diet (see §5). | No such thing as a regional diet. |
| **Cryolipolysis** | Ingargiola 2015 SR (19 studies): caliper -14.7 to -28.5%, ultrasound -10.3 to -25.5% local fat-layer reduction. A 2025 MA (30 studies, 3,158 participants; first author reported as Ravindran, UNVERIFIED) pooled suprailiac thickness ~-5.2 mm at 12 wk (95% CI ~-9.0 to -1.4). **Paradoxical adipose hyperplasia** (the treated area *grows*): rare but under-reported, 0.0005% to ~1% across reports (Ho & Jagdeo 2017 found 16 published cases). Mostly uncontrolled, many device-sponsored. | **Works locally, modestly** - it kills fat cells. Cosmetic, a few mm. Not fat loss in any metabolic sense. |
| **Liposuction** - Hernandez 2011, Obesity, doi:10.1038/oby.2011.64 | RCT, 32 women (14 lipo, 18 control), small-volume lipo of lower abdomen/hips/thighs. At 1 year total fat had **returned**, redistributed to the **upper abdomen**; treated thighs stayed reduced. [press + abstract] | Removes local fat; the body defends total fat and puts it back elsewhere - often somewhere worse. |

---

## 5. Why Kye's arms may carry more fat than his belly or chest

This is the second half of question 4. I could not open DXA reference tables for arm-versus-trunk %fat in men
(search returned an Italian reference set showing limb values only: young men's arm %fat ~9-15%), so the
following is mechanism and the one relevant cohort, not a reference-range comparison.

1. **Men mobilise trunk fat first and limb fat last.** In fit young men (US Army Ranger course, Nindl et al. 1996
   per the title confirmed; author/year from memory, so mark UNVERIFIED), fat stayed on the arms and legs until
   extreme weight loss, when abdominal fat was nearly depleted. In a 12-month weight-loss trial men lost more
   trunk fat and less leg fat than women (-5.0 vs -3.9 kg trunk; -1.7 vs -2.1 kg legs) [SECONDARY, citation not
   pinned]. So a lean-ish, dieting man ends up with a belly that has caught up and limbs that lag: exactly Kye's
   pattern. The abdomen is the "first in, first out" depot in men; limbs are slow.
2. **DXA arithmetic.** Regional %fat = fat / (fat + lean + bone) in that segment. The trunk segment contains
   organs, spine and a lot of lean mass, which dilutes its %fat; the arm segment is a thin limb with a skin + fat
   sleeve around relatively little muscle, so a few hundred grams of arm fat is a big percentage. Where the DXA
   operator places the shoulder cut line (how much axilla/shoulder fat lands in "arm") moves arm %fat too.
3. **Skinfold/ultrasound site choice** - triceps is one of the thickest folds on many lean men; the chest
   (pectoral) fold is one of the thinnest. Comparisons across sites are not like-for-like.
4. **What it is not:** it is not evidence that arms need "more arm work" or less carbohydrate. Kostek's 104 trained
   arms did not lose more fat than the untrained ones.

**Implication:** the arm fat comes off last, with continued total fat loss. Bigger arm muscles do change the look
(a larger muscle under the same fat looks leaner and stretches the layer thinner - the Krotkiewski effect), which
is a real, legitimate reason to keep training arms hard - for muscle, not for fat.

---

## 6. Verdicts by region (effect sizes as honest as the sources allow)

| region | verdict | best estimate | strength |
|---|---|---|---|
| **Arms** | No spot reduction | Kostek MRI: trained vs untrained difference ≈ 0 (n = 104). One positive DXA RCT: ~8 percentage points more relative loss (n = 16). | moderate-strong against |
| **Abdomen** | No meaningful spot reduction | Katch, Vispute, Kordi null; Brobakken + Paoli positive (n = 30 combined, measurement-limited). Upper bound if real: hundreds of grams over 8-10 weeks. | moderate against |
| **Thighs** | No spot reduction | Ramirez-Campillo 2013, Walts 2008 (n = 181) null. | moderate-strong against |
| **All regions pooled** | No | g = -0.03 (95% CI -0.10 to 0.05), I² 24% | strong-moderate against |
| **Non-surgical gadgets** (EMS, wraps, creams, heat) | No fat effect | girth/water only | limited (poor-quality trials), all against |
| **Cryolipolysis** | Yes, locally, small | ~10-25% of the layer, ~5 mm | moderate for local effect; mostly uncontrolled |
| **Liposuction** | Yes locally, but total fat returns within ~1 yr, elsewhere | n = 32 RCT | limited-moderate |

## 7. What would change this verdict

A within-subject trial in resistance-trained men, unilateral arm training for ≥12 weeks under a controlled
deficit, outcome by volumetric MRI of both arms, with energy intake measured. None exists in what I found. Until
then the honest position is the meta-analysis: no effect large enough to matter.

## 8. Unverified / owed

- Full texts of every paper (session network blocks PubMed/PMC/DOAJ).
- Gwinup 1971 results; Olson & Edelstein 1968 results; the 1965 "Mohr" study's author name; the one-legged cycling
  study's authors; Porcari 2002 result; Brobakken 2023's -697 g; the cryolipolysis 2025 MA first author.
- Funding of Porcari 2005 and the cryolipolysis studies.
- DXA reference ranges for arm vs trunk %fat in men.
