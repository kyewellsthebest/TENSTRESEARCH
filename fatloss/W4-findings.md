# W4 — Why fat is distributed unevenly, and why a trained man's arms can read "fatter" than his belly or chest

Agent W4, 2026-11-04. Scope: regional fat distribution, regional lipolysis, the order fat comes off, and how regional
body-fat % is measured. Kye's model point 4b ("why do my arms carry a higher body-fat % than my belly or chest?") is
tested here; spot reduction (4a) is touched only where it bears on distribution.

**Access caveat, stated up front.** `pmc.ncbi.nlm.nih.gov` and `www.nature.com` do not resolve from this session
(both WebFetch attempts failed with ENOTFOUND), so no full text was read. Every source below is ABSTRACT (abstract or
abstract-level search summary) or SECONDARY (seen only through another paper or a summary). Numbers are quoted as the
abstract/summary gave them; anything I could not pin to a source is marked UNVERIFIED. To unblock full text, the
session's network settings would need `pmc.ncbi.nlm.nih.gov` and `www.nature.com` allowed.

---

## Plain-English summary (10 lines)

1. **The most likely explanation is the measuring device, not your arms.** If the number came from a smart scale or a segmental BIA machine (InBody, Tanita), regional fat % is *modelled*, not measured — and foot-only scales never pass current through your arms at all.
2. BIA measures electrical resistance, and the arms produce roughly half of whole-body resistance while holding about a tenth of lean mass; the trunk is the reverse (Bracco 1996). Small arm-water changes swing the arm estimate; the trunk estimate is barely measured.
3. Upper-body training and fluid shifts move BIA readings by around a kilogram of "lean mass" within an hour, while DXA barely moves (Rodriguez/Tinsley 2023). Hydration, glycogen and timing all change the answer.
4. **On DXA, young men's arms are normally their *leanest* region** (852 men, Stults-Kolehmainen 2013). A real DXA reading of arm % above trunk % would be unusual, so check before believing it.
5. **Belly fat in men is largely visceral (inside the abdomen).** It doesn't pinch and doesn't show on the mirror the way triceps fat does, so "my belly looks lean" and "my belly is lean" are different statements.
6. **Muscle changes the percentage.** A segment's fat % is fat ÷ (fat + lean). A thick chest or core under thin fat reads low; the same skin-fold thickness wrapped round a thin limb is a bigger share of it (simple geometry, worked below).
7. **Order of loss is real but modest:** men tend to lose trunk and visceral fat proportionally faster early in a diet, and the visceral advantage shrinks as total loss grows (Chaston & Dixon 2008; Hallgreen & Hall 2008). In very fit men, limb fat is described as the last to go (Nindl 1996, Army Rangers).
8. Where fat sits is strongly inherited (twin heritability of regional fat ~0.4–0.9; hundreds of waist-hip loci, most stronger in women) and shaped by sex hormones (in men, estradiol deficiency drove fat gain — Finkelstein 2013).
9. Depot biology differs (abdominal fat cells are far more beta-adrenergic/lipolytic than gluteal; alpha-2 "brake" differs by site and sex) — but **there is almost no human data on the upper-arm depot itself.** "Stubborn fat" is a reasonable mechanistic story with no outcome evidence that you can target it.
10. **You cannot spot-reduce arm fat** (13-study meta-analysis; 104-person MRI arm study). To find out which explanation is yours: one standardised DXA (or two, same day, to see its noise), plus ultrasound or skinfold *thickness in mm* at triceps vs abdomen vs chest, and a waist measurement.

**Verdict on Kye's point 4b:** the observation is *probably a measurement artefact or a definition artefact*; if it
survives a DXA, it is a *genuine but normal-variation fat pattern* (genetics + where he is in the order of loss), not a
sign that arm fat behaves differently in a way training or carb timing can target.

---

## 1. How regional "body-fat %" is defined — and why the arm number is fragile

**Definition.** A segmental % fat is fat mass ÷ total mass of that segment (DXA: fat ÷ (fat + lean soft tissue + bone)).
It is a ratio, so the denominator matters as much as the fat.

**Geometry illustration (my arithmetic, not a study).** Treat a limb or torso as a cylinder with a uniform subcutaneous
fat shell of thickness *t* around radius *r*. The fat share of the cross-section is 1 − ((r − t)/r)².
- Upper arm, r ≈ 5 cm, t = 5 mm: 1 − (4.5/5)² = **19%** of the cross-section.
- Torso, effective r ≈ 15 cm, t = 5 mm: 1 − (14.5/15)² = **6.6%**.
The same pinch of fat is about three times the *percentage* on a thin segment. Real torsos also contain organs (lean)
and visceral fat, and arm shells are not uniform, so this is illustrative only — but it shows why "same fat everywhere"
need not read as "same % everywhere". Muscle growth in the chest/abdomen enlarges the denominator and pushes trunk %
down further. (Strength: arithmetic, not evidence.)

**What DXA populations actually show.** In 852 men aged 18–30, the arm was the region with the *lowest* % fat in every
ethnic group; trunk % fat was ~20.6% in non-Hispanic white men and 25.5% in Hispanic men (Stults-Kolehmainen 2013,
ABSTRACT/SECONDARY). So geometry alone does not normally make men's arms the fattest region — men's subcutaneous fat is
thicker on the trunk, and the trunk adds visceral fat. A true DXA arm-above-trunk pattern is atypical. (moderate, one
large DXA cohort; arm/trunk region boundaries are software-defined.)

**DXA precision for arms is the worst of any region.** Arm fat-mass CV 4.26% on a Lunar DPX-L versus ~2% total-body;
7.8% in wheelchair athletes (Keil 2016); least-significant-change varies by region, sex and tissue (Buehring 2014);
hand position alone shifts arm fat by ~0.05 kg (Thurlow 2017). On a lean arm holding ~1 kg of fat, a 5–8% CV is
±50–80 g per scan — small arm-vs-trunk differences on a single scan are within noise. (moderate)

## 2. Why smart-scale / segmental BIA limb readings are unreliable

- **BIA does not measure fat.** It measures impedance, converts it to body water and lean mass with proprietary
  equations, and fat is what is left over. Segment fat values inherit every assumption in that chain. Whether InBody's
  segmental fat is computed by subtraction is not stated in anything I could reach (UNVERIFIED).
- **Limbs dominate the signal.** In 51 women at 50 kHz, arms gave 47.6% and legs 43.0% of whole-body impedance while
  holding 10.6% and 34.8% of fat-free mass; the trunk gave ~10% of impedance and 48% of FFM (Bracco 1996, ABSTRACT).
  The arm is therefore *over*-weighted and the trunk *under*-measured; a trunk fat value is largely inferred.
- **Foot-to-foot scales** pass current leg to leg; any arm or trunk figure they print is extrapolated, not measured
  (follows from the electrode path; no validation study for arm values from foot-only scales found — UNVERIFIED as to
  any specific brand's algorithm).
- **Agreement with DXA.** Whole-body InBody vs DXA: −3.3% BF bias, LoA ±5.6% (Esco 2015); LoA under ±4.94% with
  proportional bias in obese adults (Nickerson 2020); BF% LoA about −6.0 to +4.2 points (Hurt & Ebbert 2021); systematic
  under-estimation of BF% across InBody models (J Clin Densitom 2018 reliability/agreement study; first author not
  confirmed, recalled as McLester — UNVERIFIED). Arm *lean* tissue agreed to LoA ±0.79 kg in female
  athletes (Esco 2015). One small study (n = 30) found BIA overestimated arm lean mass by ~0.97 kg and underestimated
  arm fat (SECONDARY, authors not verified). **I found no study giving arm *fat* % limits of agreement vs DXA** —
  the exact metric Kye is reading has no validation I could locate.
- **Acute exercise.** After upper-extremity resistance exercise, BIA total body water and FFM were ~1 and ~1.2 kg
  higher than rest; DXA changes were negligible (Rodriguez/Tinsley 2023, n = 32). An InBody 770 crossover in 32
  resistance-trained adults showed arm FM falling 0.15–0.22 kg after exercise (conference abstract, SECONDARY). A lean
  arm holds maybe ~1 kg of fat, so that is a 15–20% swing in arm fat from timing alone.
- **Hydration/food.** Hypohydration moved BIA BF% from 14.4% to 12.3% while hydrostatic weighing stayed put (1998,
  endurance-trained); a 30-min aerobic bout lowered measured fat %, water intake raised it (2021 segmental-BIA study).
  Glycogen holds water (vendor figure ~3 g per g, SECONDARY), so carb-cycling days will shift readings. One 2021 paper
  reported *no* BF% change after violating pre-test rules (abstract only) — the evidence is not unanimous, but the
  direction of risk is clear: unstandardised readings are not comparable.

**Bottom line:** a segmental BIA arm-fat % is the least trustworthy number such a device produces. (moderate)

## 3. Visceral versus subcutaneous — why the belly can "look" lean

Men preferentially store fat centrally, and a large share of male abdominal fat is visceral (inside the abdominal wall),
which a pinch, a mirror or a tape at the skin does not see as subcutaneous thickness. DXA trunk/android regions and
MRI/CT do see it. So a trained man with thin abdominal skin-fold, visible abs and a thick triceps pinch can genuinely
carry more total trunk fat than arm fat. Visceral fat is also driven by local cortisol generation in omental fat
(11β-HSD1 higher in omental than subcutaneous fat; "Cushing's disease of the omentum" hypothesis — Bujalska 1997;
fat-specific 11β-HSD1 overexpression produces visceral obesity in mice — Masuzaki 2001), and is more variable with
ethnicity (higher VAT for a given BMI in several Asian groups; South Asian male data inconsistent). (moderate for the
storage pattern; limited for the cortisol mechanism in ordinary men)

## 4. Why distribution differs between people: genes and hormones

- **Heritability.** DXA twin study: regional fat % heritability ~0.82–0.85 for trunk, ~0.81–0.83 lower body (Malis
  2005, Danish twins). Reviews put total/regional fat heritability at 0.40–0.90; twin designs can inflate it;
  subscapular skinfold heritability fell from 0.77 to 0.40 after adjusting for total fatness. (moderate)
- **GWAS.** Shungin 2015 (Nature, up to 224,459 people): 49 WHR-adj-BMI loci, ~20 sexually dimorphic, 19 of those
  stronger in women; loci enriched for adipose expression, adipogenesis, angiogenesis, insulin resistance. Pulit 2019
  (694,649): 346 loci; 266 in women vs 91 in men; 97 of 105 dimorphic signals stronger in women. Distribution genetics
  are mostly characterised by waist-hip ratio — **there is no arm-fat GWAS in what I found.** (strong for "it is
  heritable"; none for "arm-specific")
- **Sex hormones.** In men with gonadal steroids suppressed (Finkelstein 2013, NEJM), androgen deficiency cost lean
  mass and strength, while **estrogen deficiency primarily accounted for increases in body fat**. TRT trials in
  hypogonadal men are inconsistent for visceral fat (small waist reduction in one crossover n = 24; no VAT change in a
  24-week RCT where subcutaneous fat fell). (moderate; regional detail mostly not reported in abstracts)
- **Age** shifts fat centrally in men; I did not verify a specific source this session (UNVERIFIED — flagged, not
  relied on).

## 5. Depot biology: adrenergic balance, lipolysis, LPL

- **Beta vs alpha-2.** Abdominal subcutaneous fat cells were 10–20× more beta-adrenergically sensitive than gluteal
  cells in both sexes, with ~2× beta-receptor density; in women, abdominal cells had ~40× less alpha-2 antilipolytic
  sensitivity than gluteal ones; post-receptor lipolysis did not differ (Wahrenberg, Lönnqvist & Arner 1989, JCI).
  Obese subjects' abdominal cells had a stronger alpha-2 (brake) response than lean subjects'; men with a high
  abdominal alpha-2 response were fatter (Mauriège 1991). Children's abdominal cells were more alpha-2 responsive than
  adults' (puberty paper, 1991, SECONDARY).
- **In-vivo FFA release (Jensen lab).** Men's upper-body subcutaneous fat resists the antilipolytic effect of a meal
  more than women's (Jensen 1995); epinephrine doubled leg palmitate release in men (n = 8) but not women (n = 7)
  (Jensen 1996); upper-body subcutaneous fat is the dominant, more lipolytically active source of systemic FFA.
  Note "upper-body subcutaneous" in these studies is estimated by subtraction and includes arms and trunk together —
  **the arm depot has not been isolated.**
- **Storage.** 24-h meal-fat storage did not predict where fat went during 8 weeks of overfeeding (Votruba & Jensen
  2012, n = 28, 15 men); gluteal LPL and storage patterns differ by sex (Votruba 2007; Santosa 2008; Fried & Kral 1987;
  Fried 1993 — glucocorticoid effects on LPL stronger in omental fat, especially in men).
- **Arm depot specifically:** I found **no human biopsy or microdialysis study of triceps/upper-arm adipose lipolysis**.
  Any claim that "arm fat is stubborn because of alpha-2 receptors" is extrapolation from abdominal/gluteal data,
  mostly in women. (limited → none for arms)

**"Stubborn fat" fact-check:** *partly right as mechanism, unsupported as an actionable claim.* Regional differences in
adrenergic balance are real and measured; that they make one region reliably last to go in a given man, or that any
protocol (fasted cardio, yohimbine, carb timing) re-orders regional loss, was not shown in anything I found.

## 6. The order fat comes off

- **Visceral first, proportionally, early.** Chaston & Dixon 2008 (systematic review of imaging studies): % weight loss
  was the only predictor of the visceral-vs-subcutaneous ratio (r = −0.29) — modest losses show preferential VAT loss,
  larger losses shrink that preference; VLCDs gave exceptional VAT loss only under ~4 weeks, gone by 12–14 weeks.
  Hallgreen & Hall 2008 (37 studies, 1,407 people): VAT change is predicted by fat-mass change plus the starting
  VAT/fat ratio, allometrically (exponent reported as k ≈ 1.3 ± 0.1 in a follow-up letter, SECONDARY), regardless of
  method. (moderate)
- **Trunk before limbs, especially in men.** 22-week program, 180 overweight adults: trunk lost most, then legs, then
  arms; men lost the highest percentage from the trunk. 12-month diet trial: men started with 7.0 ± 0.9% more of their
  fat in the trunk and lost more trunk fat than women. (moderate, overweight samples)
- **Lean, fit men (closest to Kye).** Nindl 1996: 165 Army Ranger candidates (~14.7% fat), 13% weight loss over 8
  weeks at −1000 kcal/d: about half the fat lost from **every** region (arms, legs, trunk); the fattest quintile carried
  a larger share of fat in the arms and lost a larger share from the arms; authors describe a "fit fat" pattern in which
  limb fat persists until extreme loss. (moderate, single cohort, abstract only)

**Fact-check, "the last place fat goes is X":** there is no single universal last depot. Population data say early
loss is weighted to visceral/trunk in men, then roughly proportional; in lean fit men limbs may *appear* to hold on
because trunk fat has already gone. That fits Kye's observation if he is lean: arm % looks relatively high because the
trunk has already dropped.

## 7. Spot reduction (brief, as it bears on arm fat)

Localized training does not reduce local fat: Ramírez-Campillo 2022 meta-analysis (13 studies, 1,158 participants, 37
comparisons, 17 favoured the trained limb, 20 the untrained; ES −1.21 to 1.07). Kostek 2007 (n = 104, 12 weeks training
one arm): MRI showed generalized subcutaneous fat loss with **no** difference between trained and untrained arm; only
calipers in men showed a trained-arm drop — technique-dependent. Stallknecht 2007 showed higher blood flow and
lipolysis in fat next to contracting muscle ("spot lipolysis") acutely — an acute substrate effect that has not
translated into regional fat-mass change in training trials. (strong for "no meaningful spot reduction")

---

## 8. Ranked explanations for "my arms have more body-fat % than my belly or chest"

| # | Explanation | Likelihood | Why | How Kye checks it |
|---|---|---|---|---|
| 1 | **Device/method artefact** (segmental BIA or foot-only scale) | Highest, if the number came from a scale/InBody | Arm values are model outputs; arms dominate impedance; trunk is barely measured; no arm-fat-% validation vs DXA found; hydration, glycogen and recent upper-body training move the arm estimate by a large fraction of its fat | Check whether the device has hand electrodes. Re-test under standard conditions (morning, fasted, voided, no training for ≥12–24 h, never after an arm/push day) on 3 days and look at the spread. If arm % jumps around by several points, it is noise. |
| 2 | **Definition/denominator effect** | High | Segment % = fat ÷ segment mass; a thick chest/core under thin fat reads low; the same fat thickness on a thinner limb is a larger % (geometry example in §1) | Compare **thickness in mm**, not %: skinfold (same trained tester) or B-mode ultrasound (Müller 2016 sites: distal triceps, upper and lower abdomen) at triceps vs abdomen vs chest. |
| 3 | **Belly fat is visceral, not pinchable** | Moderate–high for "belly looks lean" | Men store abdominal fat viscerally; mirror and pinch miss it | Waist circumference at the navel; DXA android/VAT estimate. A waist that hasn't come down tells you the belly still holds fat. |
| 4 | **Where he is in the order of loss** | Moderate, if he has been dieting and is lean | Men lose trunk/visceral fat proportionally faster early; in fit men limb fat is described as last to go (Nindl 1996) | Track the trend, not one reading: arm vs trunk fat mass on repeated DXA (6–12 weeks apart) during the cut. |
| 5 | **Genuine individual fat pattern (genes, hormones)** | Low–moderate as the *main* reason; real as a contributor | Regional fat is strongly heritable; estradiol matters for fat in men | Only meaningful after DXA confirms it. If DXA shows arm % > trunk % (atypical for young men) **and** he has symptoms, a GP blood panel (total/free testosterone, estradiol, SHBG) is reasonable; do not self-diagnose. |
| 6 | **Arm-specific depot biology ("stubborn" alpha-2 fat)** | Low as an explanation he can act on | Real regional adrenergic differences, but no human data on the upper-arm depot | Nothing to test; no protocol targets it. Total fat loss is the only lever. |

**The single most informative check:** one DXA scan under standard conditions, ideally two on the same day with
repositioning, so he sees the scanner's own arm-fat noise. If the DXA arm % is not above trunk %, explanation 1 or 2 was
the answer. If it is, explanations 4 and 5 are in play.

## 9. Kye's model, point 4 — verdict

- **4a "can fat be lost from specific limbs?"** — **Wrong.** No meaningful spot reduction (meta-analysis + MRI trial).
  Acute local lipolysis exists but does not change local fat mass in practice.
- **4b "why do my arms carry a higher BF%?"** — the premise is **probably a measurement/definition artefact**. If real,
  it is a normal-variation pattern (heritable distribution, trunk/visceral fat lost first in men), not evidence that
  arm fat needs special treatment. Carb cycling or fasted training is not shown to re-order which region loses fat.

## Gaps and what I could not verify

- No full text read (PMC and nature.com blocked). All figures are abstract/summary-level.
- No study found that validates segmental-BIA **arm fat %** against DXA with limits of agreement.
- No human study of upper-arm/triceps adipocyte lipolysis or adrenergic receptors.
- No arm-specific fat-distribution GWAS.
- Age effect on male fat distribution not sourced this session (UNVERIFIED).
- Several primary authors for the order-of-loss studies (22-week PRONAF-style program; 12-month protein trial; n = 30
  BIA arm study) were seen only as titles/summaries and are marked SECONDARY with incomplete citations.
