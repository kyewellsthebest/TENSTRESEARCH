# Exercise selection, upper body — which exercise grows more muscle and builds more strength?

Run date: 2026-11-16 · Topic status: audited 2026-11-16 · Studies file:
`2026-11-16-exercise-selection-upper-body-studies.csv` (57 rows)

**Evidence tags:** strength of evidence is given as strong / moderate / limited / very limited, followed by the citation
key from the CSV. Access is marked FULL (full text read), ABSTRACT or SECONDARY. "Training study" means people trained
for weeks and muscle size or strength was measured before and after. "EMG" means electrodes measured muscle activity in
one session. **An EMG difference is never proof of more growth.** I report EMG only where no training study exists, and
I label it every time.

**Read this first: the evidence is thin.**

- Head-to-head training studies that measured muscle size exist for only a handful of upper-body comparisons: free
  weights vs machines, flat vs incline bench, push-ups vs bench, curl variants, triceps extensions overhead vs arm at
  the side, dumbbell vs cable lateral raises, and compound-only vs compound-plus-isolation for the arms.
- For **lats, mid-back, traps, rear delts and forearms I found no head-to-head training study that measured muscle
  size.** Not one. Everything said about "the best lat exercise" comes from EMG.
- Most trials last 8–12 weeks, have 10–40 people, and use beginners. Only a few size studies used trained lifters:
  HernandezBelmonte2023, Larsen2025, Wolf2025, deFranca2015, and ZabaletaKorta2023 (recreationally trained women).
- "No significant difference" in a 20-person study does not prove two exercises are equal. It usually means the study
  was too small to tell.

**A word on the Barbalho papers.** One research group (first author Barbalho) published five trials on compound vs
isolation exercises, mostly concluding that isolation work adds nothing (corrected at audit: the draft said four).

- Two are **retracted**: Barbalho2020 (recreational bodybuilders, Eur J Sport Sci; retracted August 2022) and a
  trial in untrained young women that is not a CSV row (J Strength Cond Res 2020;34(8):2214-2219, PMID 29781936;
  retracted January 2022).
- One has a 2026 **Expression of Concern** about the validity of its data (Barbalho2018a).
- Barbalho2021 has no retraction or expression of concern. PubMed links it to an erratum whose record is mislabelled,
  so I could not read what was corrected.
- Barbalho2018b carries no notice.

I give all of them no weight. The four that are CSV rows are there only so nobody cites them by mistake. Older reviews
that lean on them (for example Gentil 2017, doi 10.1007/s40279-016-0627-5, not a CSV row; ABSTRACT) should be read
with that in mind.

**Key clash with the lower-body note.** "Barbalho2020" in this file is the retracted bodybuilder trial (doi
10.1080/17461391.2019.1611932). "Barbalho2020" in the lower-body file is a different paper: the squat vs hip thrust
trial (doi 10.1055/a-1082-1126), which has no notice. "Nunes2020" is also two different papers (preacher curls here,
calf raises there). Give them separate keys before merging into `STUDIES.csv`.

---

## 1. Chest

- **Barbell, machine and Smith-machine pressing grow the pecs equally.** Strength: **moderate**.
  - HernandezBelmonte2023 (ABSTRACT): 38 trained men, 8 weeks, barbell vs machine versions of the same lifts (bench,
    squat, bench pull, shoulder press), everything else identical. Pec cross-sectional area grew in both groups. The
    difference in percentage change was 2.0% or less (P ≥ 0.208).
  - MarcosFrutos2025 (ABSTRACT): 37 sport-science students, 8 weeks, free-weight vs Smith-machine bench. Pec
    cross-sectional area improved "comparably". No numbers in the abstract.
  - Haugen2023 (FULL; 13 studies, 5 with a size measure): hypertrophy SMD −0.055 (95% CI −0.397 to 0.287). Heidel2022
    (ABSTRACT): ES −0.01, with a wide interval. Both pool whole-body programmes, and the intervals are wide enough to
    hide a small real difference.
  - Schwanbeck2020 (ABSTRACT; n = 46, 8 weeks): no difference in biceps or quadriceps thickness. Chest not measured.
- **Barbell vs dumbbell bench: no training study exists that I could find.** Strength: **very limited** (EMG only).
  - Saeterbakken2011 (ABSTRACT; EMG, 12 trained men): pec and front-delt activity was the same with Smith machine,
    barbell and dumbbells. Dumbbell loads were 17% lighter than barbell, and triceps activity was lower with dumbbells.
- **Flat vs incline: an incline press may grow the upper pec more. One study, in beginners.** Strength: **limited**.
  - Chaves2020 (ABSTRACT): 47 untrained men, 8 weeks, one session a week, sets equated. The upper-pec site (second
    intercostal space) grew more with incline than flat: difference 0.62 cm (95% CI 0.23 to 1.0). The other two pec
    sites did not differ. Isometric strength gains were the same.
  - Doing both (flat + incline) grew the upper site *less* than incline alone: difference 0.50 cm (0.14 to 0.86).
  - Only 1 of 3 sites differed, so this could partly be chance. Nobody has repeated it in trained lifters.
  - EMG points the same way (weak support): upper-pec activity peaked at about 30° (RodriguezRidao2020, ABSTRACT, n =
    30) or 44° (Trebs2010, ABSTRACT, n = 15). Above 45° the front delt takes over and pec activity falls.
  - Albarello2022 is often quoted here. It measured swelling straight after one session, not growth. Ignore it.
- **Decline bench: no training study found.** Strength: **none**.
- **Bench vs flyes, cable crossover or pec deck: no head-to-head training study found.** Strength: **very limited**.
  - Pinto2025 (ABSTRACT): pec deck alone, 15 untrained men, 12 weeks. Both pec heads grew about 17–21%. So a fly
    machine does grow the whole pec. It did not favour either head.
  - Solstad2020 (ABSTRACT; EMG, 17 trained men): barbell bench gave 8–81% higher pec, front-delt and triceps activity
    than dumbbell flyes at a 6RM load. EMG cannot capture any benefit of the deep stretch, so this proves little.
  - The only trial comparing isolation-only vs compound-only chest training with a pec measurement is Barbalho2021,
    which I do not trust (see above).
- **Push-ups vs bench press at the same load: similar growth and strength.** Strength: **limited**.
  - Kikuchi2017 (FULL): 18 men, 8 weeks, bench at 40% 1RM vs push-ups set to the same load, to failure. Pec thickness
    +19.4% (bench) vs +18.3% (push-up); triceps +10.3% vs +9.5%; 1RM 60.0 → 65.0 kg vs 61.1 → 64.2 kg.
    Nine per group, so it cannot show equivalence. Light loads only.
  - Audit caveat: these percentages are the ones the paper states, but they do not follow from its own printed
    means (bench triceps 26.3 → 27.8 mm is +5.7%, not +10.3%; bench pec 17.8 → 22.5 mm is +26%, not +19.4%). The
    paper's abstract, text and table disagree with each other. Trust the direction (both grew), not the decimals.
  - Calatayud2015 (ABSTRACT): 30 trained students, 5 weeks, 6RM bench vs band-loaded 6RM push-ups. Similar 1RM gains.
    No size measure.
  - Kotarsky2018 (ABSTRACT): 23 men, 4 weeks. Both raised bench 1RM. Too short to see growth.
- **Grip width: no training study found.** Strength: **very limited** (EMG only).
  - Saeterbakken2021 (ABSTRACT; EMG, n = 28): pec activity was similar across narrow, medium and wide grips. A wide grip
    lowered triceps activity. A narrow grip lowered the 6RM load.
- **What the bench press grows besides the pecs.** Strength: **limited**.
  - Lanza2024 (ABSTRACT): bench press only, 10 weeks, MRI, 13 trainees vs 11 controls. Pecs, pec minor, front delt and
    triceps all grew more than in controls. The pecs grew more than the pec minor and the triceps. **The side delt
    grew least**, and less than every other muscle measured.
  - Ogasawara2012 (ABSTRACT): bench only, 7 beginners, 24 weeks. Pecs and triceps grew. Biceps did not.

## 2. Back (lats, mid-back, traps)

- **There is no head-to-head training study of back exercises with a muscle-size outcome.** Strength: **very limited**.
  - I searched PubMed and Europe PMC for lat, trapezius and rhomboid size after pulldown, pull-up, row or pullover
    training. Nothing compared two exercises.
  - DiFonza2026 (FULL; review of 23 lat EMG studies) says so directly: none of the studies included a training
    intervention, and none reported growth or strength.
  - So lat pulldown vs pull-up, pulldown vs row, grip width, grip type, and the pullover have **never been tested for
    growth**. Anyone who tells you one is proven better is guessing.
- **EMG only (weak support): grip width hardly matters on the pulldown.**
  - Andersen2014 (ABSTRACT; n = 15): lat activity was similar at narrow, medium and wide pronated grips. The 6RM load
    was a little lower with the wide grip (77.3 kg vs about 80 kg).
  - Buonsenso2025 (ABSTRACT; 40 men with 5+ years of training): no difference in lat activity across seven pulldown
    variants (grip type, width, trunk lean).
  - Lusk2010 (ABSTRACT; n = 12): an overhand grip gave more lat activity than an underhand grip. Buonsenso2025, a
    larger study, did not confirm this.
- **EMG only: pull-up/chin-up vs pulldown.** Doma2013 (ABSTRACT): chin-ups gave more biceps activity than pulldowns,
  with no lat difference reported. Halet2009 (ABSTRACT; not EMG, a correlation study in 28 women swimmers): pull-up
  count and pulldown 1RM are only weakly related (r = 0.34, p = 0.08), because body weight decides pull-up
  performance.
- **EMG only: the pullover looks more like a chest exercise than a lat exercise.** DiFonza2026 (FULL).
- **Mid-back and traps:** no training study, and I did not find a usable EMG synthesis. **None.**

## 3. Shoulders

- **Dumbbell and cable lateral raises grow the side delt equally.** Strength: **limited** (one good study).
  - Larsen2025 (FULL): 24 trained lifters (about 7 years of training), one arm on each exercise, 8 weeks, 5 sets twice a
    week to failure. Side-delt thickness rose 3.3–4.6% in both. The cable-minus-dumbbell difference was −0.25 mm at one
    site and +0.20 mm at the other. Bayes factors (0.27 and 0.22) favoured "no difference".
  - The idea that cables are better because they load the stretched position was **not** supported here. Note that
    both arms stopped with the arm at the side, so neither got extra stretch.
  - Funded by Jaquish Biomedical, an equipment company. The authors say that, to their knowledge, no earlier training
    study had measured side-delt thickness. (Lanza2024 measured its cross-sectional area by MRI.)
- **Overhead press vs lateral raise for the side delt: no training study exists.** Strength: **very limited**.
  - EMG only: Campos2020 (ABSTRACT; 13 trained men, 60% 1RM) found side-delt activity of 30.3% of maximum in the lateral
    raise and 27.9% in the shoulder press. No difference between the two was reported. Both were far above the bench
    press (5%) and fly (3.4%).
  - So EMG does not show the press to be useless for side delts. Nobody has tested it for growth.
- **The bench press does little for side delts.** Strength: **limited**. Lanza2024: the side delt grew least, and the
  abstract does not list it among the muscles that out-grew the controls (see section 1). Campos2020 (EMG): 5% activity
  in the bench.
- **Front delts are covered by pressing.** Strength: **limited**.
  - Lanza2024: the front delt grew from bench pressing alone.
  - EMG only: front-delt activity was higher in the shoulder press (33.3%) than the bench (21.4%) (Campos2020), and it
    rises as the bench is inclined (RodriguezRidao2020, Trebs2010).
- **Lateral-raise technique: EMG only.** Coratella2020 (ABSTRACT; 10 bodybuilders): side-delt activity was higher with
  a neutral arm than with the arm turned outward, a bent elbow or a front raise. Turning the arm inward (thumbs down)
  raised rear-delt and upper-trap activity.
- **Rear delts: no training study exists.** Strength: **very limited** (EMG only, and it conflicts).
  - Franke2015 (ABSTRACT; n = 12): the reverse pec deck gave more rear-delt activity than the seated row or pulldown.
  - Rabello2024 (ABSTRACT; review of 33 EMG studies): pull-ups and inverted rows ranked highest for the rear delt.
  - These disagree on whether rows and pulls are enough. Nobody knows.

## 4. Biceps and other elbow flexors

- **Preacher vs incline curl: total growth is about the same. Each shifts growth slightly between muscles.**
  Strength: **moderate** (three trials agree the differences are small).
  - Kobayashi2026 (ABSTRACT): 21 beginners, one arm on each curl, 12 weeks, MRI. This is the best measurement so far.
    - Biceps: incline +22.1% vs preacher +18.9% (g = 0.33).
    - Brachialis: incline +17.1% vs preacher +21.1% (g = 0.50).
    - Brachioradialis: incline +13.5% vs preacher +17.6% (g = 0.47).
    - All elbow flexors together: +17.6% vs +19.2% (g = 0.22, P = 0.134). No real difference.
  - Kassiano2025 (ABSTRACT): 63 young women, 8 weeks. The site nearest the shoulder grew 0.08 cm more with incline
    (95% CI 0.02 to 0.13). The site nearest the elbow grew 0.10 cm more with preacher (0.04 to 0.15). These are
    differences of about one millimetre.
  - ZabaletaKorta2023 (ABSTRACT): 38 recreationally trained women, 9 weeks. Only the preacher group's lowest site
    grew, but the between-group test was not significant (p = 0.367). It does not show what its title suggests.
- **Shoulder position alone (arm behind the body vs in front) does not change biceps growth.** Strength: **moderate**.
  - Attarieh2025 (FULL): 15 beginners, 10 weeks, cable curls with the shoulder flexed vs extended, same resistance
    curve. Biceps +7% vs +9% (p = 0.314). Too small to rule out a slight edge for the stretched position.
  - Larsen2026 (FULL): 24 beginners, 10 weeks, shoulder neutral vs fully extended. Difference −0.40 mm (95% CrI −1.06 to
    0.26) at one site and +0.21 mm (−0.25 to 0.65) at the other. No meaningful difference.
- **Where in the curl the load is heaviest does not change growth.** Strength: **limited**.
  - Nunes2020 (FULL): 35 beginners, 10 weeks, cable preacher (hardest at the top) vs barbell preacher (hardest at the
    bottom). Biceps +7% vs +8% (p = 0.346). Strength at long muscle length rose more with the barbell (+39% vs +30%).
  - Varovic2025 (ABSTRACT; meta-analysis, 12 studies, all muscles): training at longer vs shorter length changed
    regional growth by a trivial 0.6–1.9%. Wolf2025 (ABSTRACT; 30 trained lifters): lengthened partials = full range
    for arm growth. Both are already in `top5/`.
- **Do rows and pulldowns grow the biceps as much as curls? The two direct tests disagree.** Strength: **limited**.
  - Mannarino2021 (ABSTRACT): 10 beginners, one arm did dumbbell rows and the other did curls, 8 weeks. Elbow-flexor
    thickness +11.06% with curls vs +5.16% with rows (p = 0.009). Curls gave about twice the growth.
  - Gentil2015 (FULL): 29 beginners, 10 weeks, wide-grip pulldown vs barbell curl as the only biceps work. Thickness
    +6.10% vs +5.83%. No difference.
  - A row is not a pulldown. The elbow bends less under load in a row, which may explain the split. Both studies are
    small and in beginners.
- **Does adding curls to a compound programme help?** Strength: **limited**, and nearly unknown in trained lifters.
  - Gentil2013 (ABSTRACT): 29 beginners, 10 weeks. Thickness +6.5% without curls vs +7.04% with. No difference.
  - deFranca2015 (ABSTRACT): 20 trained men, 8 weeks, tape-measure outcomes only. Arm muscle circumference +1.33%
    without isolation work vs +3.17% with it. Called "not significant" with 10 per group. That is an underpowered
    study, not evidence of no effect.

## 5. Triceps

- **Overhead extensions grow the triceps more than extensions with the arm at the side.** Strength: **limited** (one
  strong study; already in `top5/`).
  - Maeo2023 (ABSTRACT): 21 adults, one arm on each, 12 weeks, cable extensions, MRI.
    - Long head: +28.5% overhead vs +19.6% arm-at-side (d = 0.61).
    - Lateral + medial heads: +14.6% vs +10.5% (d = 0.39).
    - Whole triceps: +19.9% vs +13.9% (d = 0.54).
    - The overhead arm used 34–39% lighter loads and still grew more.
  - This is the largest between-exercise difference found anywhere in this note. It has not been repeated, and the
    abstract does not say whether the subjects were trained.
- **The bench press alone grows the long head less than triceps extensions do.** Strength: **limited**.
  (Corrected at audit: the draft said the bench "does not grow" the long head. The abstract only says it grew
  *less* than in the extension groups, and that whole-triceps growth was not significant with bench alone.)
  - Brandao2020 (ABSTRACT): 43 young men in four groups, MRI of each head.
    - Bench only: the **lateral head** grew more than with triceps extensions only. The whole triceps did not grow
      significantly, and the **long head grew less** than in every group that did lying triceps extensions.
    - Lying triceps extensions only: the long head grew, but the pecs grew less than in every bench group, and bench
      1RM did not rise.
    - Either order of bench + extension grew everything.
  - No effect sizes, trial length or training status are given in the abstract.
  - Lanza2024 and Ogasawara2012 agree that bench pressing grows the triceps somewhat, but less than the pecs.
  - Wakahara2012 and Wakahara2013 (ABSTRACT; 12 men each, 12 weeks, MRI) show that a single triceps exercise grows
    some regions of the muscle more than others. **Very limited**: no comparison group.

## 6. Forearms

- **No training study compares forearm exercises.** Strength: **none**.
- The only usable data point: brachioradialis (the big muscle on the thumb side of the forearm) grew +17.6% with
  preacher curls vs +13.5% with incline curls (Kobayashi2026). Curls grow it. Nothing is known about wrist curls,
  reverse curls or grip work for size.

## 7. Compound (multi-joint) vs isolation (single-joint) — arms and upper body

- **For whole-muscle size, the pooled evidence says compound and isolation work are about equal.** Strength:
  **limited**.
  - Rosa2023 (ABSTRACT; meta-analysis, 7 trials, 10 comparisons): "trivial" pooled difference. The abstract gives no
    numbers. The authors add that isolation work may grow specific parts of a muscle that compounds miss.
  - Audit: the pooled estimate very likely does **not** include Barbalho data. I could not see the paper's table of
    included trials, but its reference list (on Crossref) cites no Barbalho trial at all, and it does cite the 2020
    critique "Improbable data patterns in the work of Barbalho et al". Exactly seven head-to-head trials appear in
    the reference list, which matches the seven it pooled: Bezerra 2018, Brandao2020, deFranca2015, Gentil2013,
    Gentil2015, Mannarino2021 and Paoli2017. That list is my inference, not the paper's own table.
- **But the head-level studies show compounds leave gaps.** Strength: **limited**.
  - Bench press leaves the triceps long head behind (Brandao2020) and barely touches the side delt (Lanza2024).
  - Rows grew the biceps half as much as curls in one small study (Mannarino2021).
  - Lying triceps extensions alone grew the pecs less than any bench group (Brandao2020). Isolation work does not
    replace compounds either.
- **Compound-only programmes build more 1RM strength in compound lifts.** Strength: **limited**.
  - Paoli2017 (FULL): 36 active men, 8 weeks, isolation-only vs compound-only, volume load equated. Bench 1RM +8.1% vs
    +10.9%; squat +8.3% vs +13.8%. Fat-free mass (DXA) +3.5% vs +5.5% (p = 0.08).
  - The isolation group never practised the bench or squat, so part of this is skill. No direct muscle measurement.

## 8. Strength: how exercise-specific is it?

- **Very. You get strongest in the exact lift you train.** Strength: **strong**.
  - Heidel2022 (ABSTRACT; meta-analysis): tested on free weights, free-weight training wins (ES 0.655, 95% CI 0.269 to
    1.041). Tested on the machine, machine training wins (ES −0.784, −1.223 to −0.344). Tested on a neutral device, no
    difference (ES 0.128, −0.303 to 0.559).
  - Haugen2023 (FULL): free-weight tests favour free-weight training (SMD −0.210, −0.391 to −0.029). Machine tests
    lean to machine training (SMD 0.291, −0.017 to 0.600).
  - Saeterbakken2025 (FULL; 43 studies, 1,660 people): lifting raised strength in the trained lift by SMD 0.98 (0.91 to
    1.06), but in an untrained isometric test by only 0.42 (0.35 to 0.49). In trained lifters: 0.75 vs 0.29. Muscle
    growth did not predict the strength gain.
  - Single trials repeat the pattern: Kassiano2025 (each curl improved its own 3RM more), Mannarino2021,
    Brandao2020 (bench-only did not raise triceps-extension 1RM, and the reverse), HernandezBelmonte2023 and
    MarcosFrutos2025 (gains were larger in the trained modality), Schwanbeck2020 (machine bench +13.9% vs +8.6%).
- **Close cousins of a lift transfer well.** Strength: **limited**.
  - Langford2007 (ABSTRACT; n = 49, 10 weeks): machine, barbell and log bench training all raised each other's
    strength, with no significant group difference.
  - Saeterbakken2020 (ABSTRACT; 35 trained men, 10 weeks): after Smith, dumbbell or unstable chest-press training, the
    changes in lifting mechanics also showed up in the untrained barbell bench. No 6RM numbers in the abstract.
- **Bottom line:** if you care about your bench number, bench. Other presses build the muscle and carry over partly,
  but the test lift itself has to be practised.

## 9. Rotating exercises

- **Some planned variety is fine. Random rotation is not better and may cost strength.** Strength: **limited**.
  - Kassiano2022 (ABSTRACT; review, 8 studies, 241 young men): planned variation may help regional growth. Frequent
    random changes may hurt gains.
  - BazValle2019 (FULL): 19 trained men finished (21 started), 8 weeks, fixed exercises vs an app picking them at
    random. Size gains were similar. Bench 1RM effect size was 1.68 (fixed) vs 0.84 (random), not significantly
    different.
  - Costa2021 (ABSTRACT): 22 detrained men. The varied group grew at every arm site. The fixed group missed one.
    Within-group tests only.

---

## Verdict

For most of the upper body, science cannot tell you which exercise grows more muscle. The honest ranking is short.

- **Chest:** barbell, Smith and machine presses grow the pecs about equally (moderate evidence). Dumbbell presses
  have never been tested for growth against any of them. An incline press may add upper-pec growth (limited; one
  beginner study). Bench vs flyes has never been tested for growth. Push-ups match the bench when the load matches
  (limited).
- **Back:** no growth study compares any two back exercises. Grip width and grip type make little difference to lat
  EMG. Choose by feel, loadability and joint comfort.
- **Shoulders:** dumbbell and cable lateral raises are equal (limited, trained lifters). The bench press grows the
  front delt but does least for the side delt. Whether the overhead press is enough for side delts is untested. Rear
  delts are untested.
- **Biceps:** curl variants differ by millimetres. Incline curls lean slightly to the biceps, preacher curls slightly
  to the brachialis and brachioradialis. Curls grew the biceps about twice as much as rows in one small study, and the
  same as pulldowns in another.
- **Triceps:** the clearest result in this note. Overhead extensions grew the triceps about 1.4–1.5 times as much as
  arm-at-side extensions (one study, cable machine, training status not stated). The bench press alone grows the
  long head less than triceps extensions do.
- **Compound vs isolation:** about equal for whole-muscle size on average, but compounds leave specific gaps (triceps
  long head, side delt, possibly biceps). Isolation work fills them.
- **Strength:** highly specific. Train the lift you want to be strong in.
- **Reality check:** most of this comes from beginners over 8–12 weeks. Effort, weekly sets and progression (see
  `library/training/top-5-factors.md`) matter far more than which press or curl you pick.

## Practical recommendation for Kye

Ranked picks per muscle. Where I write "any", the evidence says they are equal or says nothing.

1. **Chest.**
   - First: one heavy press you can load and progress for years. Barbell, dumbbell, Smith or a good machine. Pick the
     one that feels best on your shoulders. If you care about your bench 1RM, make it the barbell bench.
   - Second: a low incline press (about 30–45°) for the upper pec. This rests on one beginner study plus EMG, so treat
     it as a sensible bet, not a fact. Above 45°, EMG shows the front delt taking over.
   - Third (optional): a fly or pec deck. It grows the whole pec. There is no evidence it beats or adds to pressing.
2. **Back.**
   - One vertical pull (pulldown or pull-up/chin-up) and one row. No study says which is better for size.
   - Use the grip that lets you feel the lats and train hard without elbow or shoulder pain. Width and overhand vs
     underhand are unproven either way.
   - Don't rely on pullovers for lats. EMG puts them closer to a chest exercise.
3. **Shoulders.**
   - Side delts: do lateral raises. Dumbbell or cable, your choice; they are equal. Don't count bench pressing toward
     side delts at all.
   - Front delts: your pressing already covers them. Extra front raises are unlikely to be needed.
   - Overhead press: keep it if you like it and want the strength. It is unproven for side-delt size.
   - Rear delts: add a reverse fly or reverse pec deck. This is EMG-based and unproven, but cheap insurance.
4. **Biceps.**
   - Do direct curls. Don't rely on rows. Pulldowns and chin-ups probably do more for the biceps than rows (my reading
     across Gentil2015, Mannarino2021 and Doma2013; no study compared them directly).
   - Any curl works. For completeness use two across the week: one with the arm behind you (incline dumbbell curl)
     and one with the arm in front (preacher curl). Expect the difference to be small.
5. **Triceps.**
   - First: an overhead cable or dumbbell extension. This is the best-supported single exercise choice in the upper
     body. (The study used a cable. The dumbbell version is a reasonable extension of it, not a tested result.)
   - Second: your pressing, which covers the lateral head.
   - Pushdowns are fine as a third option, but don't make them your only triceps exercise.
6. **Forearms.** No evidence to rank anything. Preacher curls grew the brachioradialis a little more than incline
   curls. Add wrist work only if you want to; nothing shows whether it helps.
7. **Strength.** Keep the lifts you want to be strong in, and train them every week. Swap accessories freely, but not
   every session.
8. **With 1.5 h a day** you have room for one compound and one isolation exercise per muscle. That covers every gap
   the studies have found. You do not need three chest presses or four curl variants.

## New avenues

1. **Back hypertrophy evidence gap.** Are there any preprints, theses or conference abstracts (SportRxiv was not
   searchable here) with lat, trap or rear-delt size measured after pulldown vs row, different grips, or lengthened
   partials? If still none, say so in the library and flag it for a re-check every few months.
2. **Counting sets from compounds.** How much do bench, overhead press, rows and pulldowns count toward triceps,
   delt and biceps volume? Check the "fractional set" methods used in volume meta-analyses and the 0.5-set convention
   Larsen2025 used, against the head-level data (Brandao2020, Lanza2024, Mannarino2021).
3. **Upper pec in trained lifters.** Has anyone repeated Chaves2020 (incline vs flat) in trained people, or tested
   low-incline angles, deep-stretch flyes vs presses, or dumbbell vs barbell pressing for pec growth?
4. **Triceps long head beyond one study.** Has Maeo2023 been repeated in trained lifters? Do skull-crushers, dips or
   close-grip presses grow the long head, or only overhead work?

## Doubts / audit flags

- **46 of 57 CSV rows are ABSTRACT only.** JSCR, Int J Sports Med, MSSE, IJSPP and J Sports Sci papers are paywalled
  and not in Europe PMC. Load-bearing numbers taken from abstracts: HernandezBelmonte2023, Chaves2020, Brandao2020,
  Maeo2023, Kobayashi2026, Kassiano2025, Mannarino2021, Lanza2024, Heidel2022. The auditor should open full texts if
  possible. Europe PMC returned HTTP 500 for the Chaves2020 (PMC7449336) and Ogasawara2012 (PMC3831787) full text.
- **Brandao2020:** the abstract gives no trial length, no training status and no effect sizes. The "bench alone grows
  the long head less" claim rests on its significance statements only. The abstract does not say whether the long
  head grew at all with bench alone.
- **Rosa2023:** not in PubMed. Abstract seen via OpenAlex and Semantic Scholar only (the auditor also saw it on
  Crossref). No numbers. The table of included trials was not seen. The auditor read the Crossref reference list: no
  Barbalho trial is cited (see section 7).
- **Barbalho papers:** Barbalho2020 retraction confirmed on PubMed and Crossref. Barbalho2018a Expression of Concern
  confirmed (doi 10.3390/sports14060240). For Barbalho2021, PubMed lists an erratum with doi 10.1055/a-1400-4290, but
  Crossref resolves that DOI to an unrelated 2016 correction. I could not verify what the erratum says. (Auditor: the
  erratum record, PMID 33733437, is tagged as a correction to both the 2016 paper and Barbalho2021, and its PMID
  dates from 2021. So a real 2021 correction to Barbalho2021 probably exists under a wrong title. Its content is
  still unread; the publisher's site is blocked.)
- **Larsen2025:** the full text prints the credible intervals as "0.72 to 0.22" and "0.57–0.94", which look like
  dropped minus signs. I report the point estimates and Bayes factors only. Funding: Jaquish Biomedical.
- **Kikuchi2017:** the abstract repeats the push-up group's pec values for the bench group. I used the full-text
  table (bench 17.8 → 22.5 mm). The paper calls its subjects "untrained" in one place and "≥1 year of resistance
  training" in another.
- **Heidel2022:** the abstract prints the hypertrophy interval as −0.525 to 0.545 around an estimate of −0.01, and
  one bound as "-0303". Probable typos.
- **Paoli2017:** text says the compound group gained 4.9% fat-free mass; the table says 5.5%. I used the table.
- **ZabaletaKorta2023, Costa2021:** conclusions rest on within-group significance, not a between-group test.
- **Training status missing from abstracts:** Maeo2023, Brandao2020, Lanza2024, Kassiano2025, Schwanbeck2020,
  MarcosFrutos2025, Langford2007. I wrote "not stated" in the CSV instead of guessing.
- **Exercise not named in abstracts:** Wakahara2012 and Wakahara2013. I did not name the exercises from memory.
- **"No study exists" claims** (dumbbell vs barbell bench, decline, bench vs flyes, grip width, every back
  comparison, overhead press vs lateral raise, rear delts, forearms) mean: not found in PubMed or Europe PMC today
  with the searches run. SportRxiv, theses and non-indexed journals were not searched. The DiFonza2026 review and
  Larsen2025's own statement back two of these gaps.
- **EMG rows** (RodriguezRidao2020, Trebs2010, Solstad2020, Saeterbakken2011, Saeterbakken2021, Andersen2014,
  Lusk2010, Buonsenso2025, Doma2013, Campos2020, Franke2015, Rabello2024, Coratella2020) are acute data. They must not
  be upgraded to training evidence in the library file.
- **Overlap:** Heidel2022 and Haugen2023 pool many of the same trials. Schoenfeld is a co-author on Larsen2025,
  Brandao2020, Rosa2023, Kassiano2022, Varovic2025, Wolf2025 and BazValle2019, so these are not fully independent.
- **Searches:** about 39 (PubMed E-utilities 30, Europe PMC 6, Crossref 1, Semantic Scholar 2). Both Semantic Scholar
  searches returned HTTP 429 and gave nothing. Every DOI in the CSV was resolved on Crossref and checked for
  `update-to`/`updated-by`, except Solstad2020 and Franke2015, which have no DOI in PubMed. No retractions other than
  Barbalho2020.

## Audit (2026-11-16)

Independent audit. Every DOI checked was resolved on Crossref and matched to its PubMed record (title, authors, year,
journal, volume, pages). Numbers were checked against PubMed abstracts and, where open, Europe PMC full text
(Larsen2025, Gentil2015, Kikuchi2017, Haugen2023, Saeterbakken2025, DiFonza2026, BazValle2019, Nunes2020, Larsen2026).
Retractions and corrections were checked through Crossref `updated-by` and the `updates:` filter, PubMed
comment/correction links, Europe PMC and OpenAlex. Publisher sites (Thieme, Taylor & Francis, BMJ, LWW) are blocked
here, and OpenAlex and Semantic Scholar ran out of quota part-way. 30 rows of this file were checked: 26 confirmed,
4 corrected, none rejected. Full detail is in `2026-11-16-audit.csv`.

**Load-bearing items**

| key | verdict | what was checked |
|---|---|---|
| HernandezBelmonte2023 | CONFIRMED | ABSTRACT. 38 trained men, 19 per group, 8 weeks; size difference ≤ 2.0% (P ≥ 0.208); strength difference ≤ 1.8%. Same in both notes. |
| Chaves2020 | CONFIRMED | ABSTRACT. 47 untrained men, once a week for 8 weeks; 0.62 cm (0.23 to 1.0) and 0.50 cm (0.14 to 0.86). Full text still not reachable, so the incline angle is unknown. |
| Larsen2025 | CONFIRMED | FULL (PMC12277279). 24 analysed of 26; about 7 years of training; +3.3–4.6%; −0.25 mm and +0.20 mm; Bayes factors 0.27 and 0.22; the garbled intervals are printed exactly as the note says; funded by Jaquish Biomedical. |
| Maeo2023 | CONFIRMED | ABSTRACT. +28.5% vs +19.6%, +14.6% vs +10.5%, +19.9% vs +13.9%; loads 34–39% lighter overhead. Cable machine only; training status not stated. |
| Brandao2020 | CORRECTED | ABSTRACT. The numbers-free findings are quoted correctly, but "the bench press alone does **not** grow the long head" overstated it. The abstract says the long head grew **less** with bench only. Fixed in section 5, the Verdict and the Doubts list. |
| Kobayashi2026 | CONFIRMED | **It exists** as a full journal article (J Sports Sci 2026;44(23):3288-3301, PMID 42829982). All six pairs of numbers match the abstract. |
| Mannarino2021 | CONFIRMED | ABSTRACT. 10 untrained men; +11.06% vs +5.16% (p = 0.009). |
| Gentil2015 | CONFIRMED | FULL (PMC4592763). 29 untrained men; +6.10% vs +5.83%; wide overhand pulldown vs barbell curl. |
| Heidel2022 | CONFIRMED | ABSTRACT. All five effect sizes match, including the two typos in the printed intervals. |
| Haugen2023 | CORRECTED | FULL (PMC10426227). All SMDs match. The CSV said "6 studies trained, 7 untrained". The paper's text says an even 6/6 split and its own table says 8 of 13 trained, so the paper is inconsistent. CSV fixed in both files. The text also says six studies measured size (the abstract says five), and only two used ultrasound. |
| Saeterbakken2025 | CONFIRMED | FULL (PMC12296774). 0.98 vs 0.42 overall; 0.75 vs 0.29 in trained lifters. |
| Lanza2024 | CONFIRMED | ABSTRACT. 13 trained vs 11 controls; the side delt grew less than every other muscle and is not listed among those that beat the controls. Light loads (50–55% 1RM). |
| DiFonza2026 | CONFIRMED | **It exists** (J Funct Morphol Kinesiol 2026;11(3):315, PMID 42647355). FULL: "None of the studies reviewed here included a longitudinal training intervention." The pullover finding rests on one small study. |
| Kikuchi2017 | CONFIRMED | FULL (PMC5812864). Every number is quoted as the paper states it. But the paper contradicts itself (see the caveat added in section 1). |
| Barbalho2020 | CONFIRMED | **Retracted** (doi 10.1080/17461391.2019.1611932; notice 10.1080/17461391.2022.2116178, August 2022). Confirmed on PubMed, Crossref, Europe PMC and OpenAlex. |
| Barbalho2018a | CONFIRMED | **Expression of Concern** confirmed and read (Sports 2026;14(6):240, 10 June 2026): concerns "regarding the validity of the data"; investigation still open. |
| Barbalho2021 | CONFIRMED | Abstract matches. No retraction or expression of concern anywhere. The erratum linked in PubMed could not be read. |
| Barbalho2018b | CONFIRMED | Abstract matches. No notice of any kind. |
| Rosa2023 | CORRECTED | Citation and abstract confirmed on Crossref. The note's worry that it "may contain flagged data" is very likely wrong: its reference list cites no Barbalho trial and cites the critique of Barbalho's data. Fixed in section 7. The paper's own table of included trials was not seen. |
| Larsen2026 | CONFIRMED | **It exists** (Front Physiol 2026;17:1750722). FULL: −0.40 mm (−1.06 to 0.26) and +0.21 mm (−0.25 to 0.65). |
| BazValle2019 | CORRECTED | FULL (PMC6934277). 21 started but **19 finished**. The note and CSV said 21; the lower-body file had it right. Effect sizes 1.68 and 0.84 confirmed. |
| Schwanbeck2020, MarcosFrutos2025, Kassiano2022, Costa2021, Varovic2025 | CONFIRMED | Shared with the lower-body note. Each abstract matches, and both CSVs give the same n, design and numbers. |

**Random sample** (seed 20261116; from this file: Halet2009, Nunes2020, Rabello2024, Trebs2010)

| key | verdict | what was checked |
|---|---|---|
| Halet2009 | CONFIRMED | r = 0.34 (p = 0.08) in 28 women swimmers. The note now says who was tested and that this is not an EMG study. |
| Nunes2020 | CONFIRMED | FULL (PMC7460162). 35 untrained adults, randomised; +7% vs +8% (p = 0.346); +30% vs +39% at long length. |
| Rabello2024 | CONFIRMED | 33 EMG studies; pull-ups and inverted rows highest for the rear delt. |
| Trebs2010 | CONFIRMED | 15 men; upper-pec activity higher at 44° than at 0° and 28°. |

**Corrections made**

- Brandao2020: "does not grow the long head" → "grows the long head less than triceps extensions do" (section 5,
  Verdict, Doubts).
- Rosa2023: "may contain flagged data" → very likely excludes Barbalho data, with the evidence (section 7, Doubts,
  CSV).
- Barbalho paragraph: "four trials … one retracted" → five trials, two retracted, one Expression of Concern, one
  with an unread erratum, one clean.
- BazValle2019: n 21 → 19 finished of 21 (note and CSV).
- Haugen2023: CSV population "6 trained, 7 untrained" → what the paper actually says (both CSVs).
- Verdict, chest line: dumbbells removed from the list of presses that "grow the pecs about equally". Nobody has
  tested them.
- Clarified, not wrong: Kikuchi2017 caveat; Halet2009 sample; Nunes2020 design ("randomised"); the cable-only origin
  of the overhead-extension recommendation.

**Still unverified**

- What the erratum to Barbalho2021 says (publisher blocked; the index record is mislabelled).
- Rosa2023's own table of included trials and its pooled numbers (journal not in PubMed, full text blocked).
- Full texts of Chaves2020, Brandao2020, Maeo2023, Kobayashi2026, Mannarino2021, Lanza2024, Heidel2022 and
  HernandezBelmonte2023. These stay ABSTRACT.
- The 27 CSV rows outside the audit list were not re-checked beyond matching every citation to its PubMed record.

**Key clashes to fix before merging.** Barbalho2020 and Nunes2020 each name two different papers across the two
files. Larsen2025 and Kassiano2025 here are also different papers from Larsen2025a/b and Kassiano2025a/b there.

**Verdict stands.** No ranking or recommendation changed. Two Verdict sentences were made more careful: the chest
line no longer implies dumbbells have been tested, and the triceps line now says the bench grows the long head
*less*, not that it fails to grow it. The practical advice (overhead extensions first; do not rely on pressing
alone for triceps) is the same.
