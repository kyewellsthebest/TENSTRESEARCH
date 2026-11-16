# Exercise selection, lower body and trunk — which exercise grows more muscle and strength?

Run date: 2026-11-16 · Topic status: researched (needs audit) · Studies file:
`2026-11-16-exercise-selection-lower-body-studies.csv` (38 rows)

Covers quads, hamstrings, glutes, adductors, calves and abs/trunk, plus two cross-cutting questions: free weights vs
machines, and exercise variety. Chest, back, shoulders and arms are in the companion upper-body note.

**Evidence tags:** strength of evidence is given as strong / moderate / limited / very limited, followed by the citation
key from the CSV. Access is marked FULL (full text read), ABSTRACT or SECONDARY.

**Three warnings that apply to almost everything below.**

- **Almost every head-to-head trial used untrained people for 6–12 weeks.** Only five training studies here used
  trained lifters (HernandezBelmonte2023, BazValle2019, Rauch2020, Bartolomei2025, Larsen2025b), plus one in academy
  rugby players (Speirs2016) and two in trained women that I do not trust (Barbalho2020, Barbalho2021; see section 3).
  Beginners grow from nearly anything, which can hide or exaggerate exercise differences.
- **Most trials have 8–20 people per group.** "No significant difference" in these studies usually means "too small to
  tell", not "proven equal". I say so where it matters.
- **A lot of this literature comes from two labs:** Cyrino/Kassiano (Londrina, Brazil; ultrasound thickness in young
  women) and Maeo (Ritsumeikan, Japan; MRI volume, within-person leg-vs-leg designs). Their results fit together, but
  independent replication is thin.

Range of motion and lengthened-position training in general are already covered in `library/training/top-5-factors.md`
and `top5/`. They are only repeated here where muscle length explains why one exercise beat another.

---

## 1. Quadriceps

- **Squats grow the three vasti well but barely grow the rectus femoris. Leg extensions grow the rectus femoris.**
  Strength: **moderate** (three trials agree, all in untrained people).
  - Kassiano2026 (RCT; 63 untrained young women; 8 weeks; 3 sets of 8–12RM, 2 days a week; sets equated; ABSTRACT):
    Smith machine squat vs leg extension.
    - Rectus femoris thickness, leg extension vs squat: proximal +11.4% vs +2.0%; middle +12.3% vs +5.7%; distal +17.5%
      vs +7.9% (all p < 0.001).
    - Vastus lateralis, distal site: squat +18.2% vs leg extension +11.2% (p < 0.001).
    - No confidence intervals in the abstract.
  - Kubo2019 (randomised; 17 men, 8 and 9 per group; 10 weeks; MRI volume; ABSTRACT): full or half squats grew the knee
    extensors as a group by +4.9 ± 2.6% and +4.6 ± 3.1%, but **rectus femoris volume did not change in either group**.
  - ZabaletaKorta2021 (RCT; Smith squat vs leg extension, volume equated; ABSTRACT): all three rectus femoris regions
    grew with leg extensions; only the central vastus lateralis grew significantly with squats. The abstract gives no
    sample size and only within-group p-values, and a published letter criticised the paper. Treat it as weak support.
  - Why: the rectus femoris crosses the hip. In a squat it shortens at the hip while it lengthens at the knee, so it
    does little work. This is mechanism, not something these trials tested.
- **Leaning back on the leg extension grows the rectus femoris more than sitting upright.** Strength: **limited** (one
  trial).
  - Larsen2025a (22 untrained men; 10 weeks; each leg randomised to a condition; ABSTRACT): leg extension with the hip
    at 40° of flexion (leaning back) vs 90° (upright).
    - Rectus femoris grew more at 40°: Bayes factor > 100, posterior probability > 0.999 at both measured sites.
    - Vastus lateralis: strong evidence of no difference (Bayes factor 0.07).
    - The abstract does not give the size of the difference in millimetres.
- **Back squat vs leg press vs hack squat for quad size: no usable head-to-head study.** Strength: **very limited**.
  - Rossi2018 (squat vs leg press vs both; 10 weeks; ABSTRACT) reports strength, body composition and jump outcomes
    only. The abstract gives no sample size and no quad-size numbers. I could not reach the full text.
  - Amanuma2025 (8 untrained women; 9 weeks; lunge on one leg, incline leg press on the other; ABSTRACT): similar growth
    of vastus lateralis and rectus femoris at two sites each (no interaction, p = 0.59–0.82). With 8 people this cannot
    show the two are equal.
  - **No training study of the hack squat against any other exercise was found.** The hack squat only appears as part
    of a mixed programme (Kassiano2025b).
  - Indirect evidence: free-weight and machine squat patterns grow the quads equally in trained men (section 7).
- **Front squat vs back squat: no training study measuring muscle size or strength was found.** PubMed and Europe PMC
  returned only acute biomechanics and EMG papers. **Very limited** — there is nothing to rank them on.
- **Split squat or lunge vs bilateral squat: no hypertrophy difference shown, but the data are thin.**
  Strength: **limited**.
  - Kassiano2025a (meta-analysis, 9 studies, not lower-body only; ABSTRACT): unilateral vs bilateral training,
    hypertrophy effect size −0.21 (95% CI −3.56 to 3.13). That interval is so wide it tells you almost nothing.
  - Speirs2016 (18 academy rugby players; 5 weeks; rear-foot-elevated split squat vs back squat; ABSTRACT): both groups
    improved 1RM in both lifts (d ≈ 0.84–0.94), with no group difference. No muscle size was measured. It is too small
    and too short to settle anything.
- **Squat depth as an exercise choice.** Strength: **limited** (one small MRI trial).
  - Kubo2019: half squats grew the quads as much as full squats (+4.6% vs +4.9%). Depth mattered for the glutes and
    adductors, not the quads (see sections 3 and 4).

## 2. Hamstrings

- **Seated leg curl beats prone (lying) leg curl.** Strength: **moderate** (one well-run MRI trial, a second that points
  the same way, and a known mechanism).
  - Maeo2021 (20 adults with no resistance training in the past year; one leg did seated curls, the other prone curls;
    12 weeks; 5 × 10 at 70% 1RM, twice a week; MRI volume; FULL).
    - Whole hamstrings: seated +14.1% vs prone +9.3%.
    - Biceps femoris long head +14.4% vs +6.5%; semitendinosus +23.6% vs +19.3%; semimembranosus +8.2% vs +3.6% (all
      P ≤ 0.010).
    - Biceps femoris short head, which does not cross the hip: no difference (P = 0.190).
    - 1RM gains did not differ between legs (P = 0.663).
    - Why: sitting flexes the hip, which stretches the three hamstrings that cross it. This is the same muscle-length
      effect covered in the top-5 report, showing up as an exercise choice.
    - Funded by a Mizuno Sports Promotion Foundation grant; no conflicts declared.
- **A lengthened seated curl beats the Nordic curl for overall hamstring size.** Strength: **limited** (one trial; the
  two programmes differed in several ways at once).
  - Maeo2024 (42 young men, 14 per group; 12 weeks, 34 sessions; MRI; FULL): eccentric-focused curl on a modified
    seated machine with the hip flexed 120°, vs Nordic curls, vs no training.
    - Hamstring volume +18% vs +11%; biceps femoris long head +19% vs +5% (both P ≤ 0.001).
    - Nordics did better for the muscles that bend the knee but do not extend the hip (biceps femoris short head,
      sartorius): 1.9 times the growth.
    - Eccentric knee-flexion strength: +17% (seated), +11% (Nordic), +4% (control). Only seated vs control was
      significant.
- **Hip-hinge work (stiff-leg/Romanian deadlift, back extension) and knee-flexion work grow different hamstrings.**
  Strength: **limited** (three small trials, untrained, results not fully consistent).
  - Morin2025 (blinded RCT; 36 untrained adults in 3 groups; 9 weeks; 3D ultrasound volume; ABSTRACT): Nordic vs
    stiff-leg deadlift.
    - Whole hamstrings: Nordic +11.4 ± 6.5% vs stiff-leg deadlift +7.0 ± 8.1%. The authors call this similar; with
      about 12 per group it is simply unresolved.
    - Nordic mainly grew the semitendinosus (+24.3 ± 10.8%). The stiff-leg deadlift mainly grew the semimembranosus
      (+11.2 ± 12.7%).
  - Bourne2017 (RCT; 30 recreationally active men, 10 per group; 10 weeks; MRI; ABSTRACT): a hip-extension exercise
    grew the biceps femoris long head more than Nordics (d = 1.03, p = 0.037). Semitendinosus growth was not
    significantly different (d = 0.69, p = 0.239). The paper has a published correction that I did not read.
  - Crawford2025 (RCT; 32 young adults; only 6 weeks; ultrasound; ABSTRACT): Romanian deadlift vs Nordic, no difference
    in hamstring cross-sectional area (P = 0.60). Overall growth was 0.78 cm² (95% CI 0.45 to 1.11).
- **Leg curl vs stiff-leg/Romanian deadlift, head-to-head for hamstring size: no training study found.** They only
  appear together inside mixed programmes (Kassiano2025b). **Very limited.**
- **Squats do not grow the hamstrings.** Strength: **moderate** (two MRI trials agree).
  - Kubo2019: hamstring volume did not change after 10 weeks of full or half squats.
  - Plotkin2023 (FULL): hamstring cross-sectional area showed "little to no growth" after 9 weeks of squats or hip
    thrusts; the between-group difference was 0.1 cm² (95% CI −0.9 to 1.4).

## 3. Glutes

- **Hip thrust and deep back squat grew the glutes about the same in the one good trial.** Strength: **limited** (one
  MRI trial, untrained, wide intervals, conflict of interest).
  - Plotkin2023 (randomised; 34 untrained men and women; 9 weeks; sets equated; MRI; FULL). Differences in gluteus
    maximus cross-sectional area, where a negative number favours the hip thrust:
    - lower glute −1.6 cm² (95% CI −6.1 to 2.0);
    - middle −0.5 cm² (−4.0 to 2.6);
    - upper −0.5 cm² (−5.8 to 4.1).
  - The intervals are wide. The trial cannot rule out a real advantage of a few cm² either way.
  - Squats also grew the quads (+3.6 cm², 0.7 to 6.4) and adductors (+2.5 cm², 1.2 to 3.9) more than hip thrusts did.
  - Hip thrusts produced higher glute EMG in the first session, **but that did not predict growth.** This is a direct
    example of why EMG cannot rank exercises.
  - **Conflict of interest:** two co-authors sell hip-thrust products and services, and gift funds came partly from
    them. An October 2026 correction adds that BC Strength donated the hip thrust machine and that the trial was only
    registered after the fact. The journal judged the findings still reliable. No data were changed.
- **A study in trained women claims squats beat hip thrusts by a lot. Do not rely on it.** Strength: **very limited**.
  - Barbalho2020 (22 well-trained women; 12 weeks; ABSTRACT): glute thickness +9.4% (squat) vs +3.7% (hip thrust);
    quads +12.2% vs +2%.
  - Four other papers from the same first author and group have been retracted (confirmed in PubMed today). I found no
    retraction notice for this one in PubMed, Europe PMC, Crossref or OpenAlex. The gains are implausibly large for
    well-trained women doing about 6 sets a week.
  - Barbalho2021 (30 trained women; 6 months; multi-joint vs single-joint vs both; ABSTRACT) has the same trust
    problem, and volume was not equated.
- **Deeper squats grow more glute than half squats.** Strength: **limited** (one small trial).
  - Kubo2019: gluteus maximus volume +6.7 ± 3.5% (full squat, about 140° of knee bend) vs +2.2 ± 2.6% (half squat,
    90°), p = 0.008. Only 8 and 9 men per group.
- **Adding hip thrusts on top of leg press and stiff-leg deadlift gave more glute growth, but the hip thrust group also
  did more sets.** Strength: **very limited**.
  - Kassiano2023a (33 untrained young women; 10 weeks; ABSTRACT; **preprint only**): glute thickness +9.3% vs +6.0%
    (P = 0.016). It cannot separate "hip thrust" from "more glute volume".
- **In trained lifters, a squat-and-step-up programme and a hip-thrust-and-reverse-hyper programme grew the glutes
  similarly.** Strength: **very limited**.
  - Bartolomei2025 (RCT; 19 resistance-trained adults; 6 weeks; repetitions equated; ABSTRACT): similar increases in
    glute thickness. Vastus medialis grew only in the squat group (+4.1% vs −7.9%, P = 0.009).
  - 19 people over 6 weeks is far too small to detect a modest difference.
- **Hip extension and hip abduction grow different parts of the glutes.** Strength: **limited** (one MRI trial).
  - Attarieh2026 (17 adults; one leg did cable hip extensions, the other cable hip abductions; 10 weeks; MRI; ABSTRACT).
    - Gluteus maximus overall: +9% (extension) vs +5% (abduction).
    - Extension grew the lower glute most (proximal +5%, middle +8%, distal +14%). Abduction grew the upper glute most
      (proximal +10%, middle +4%, distal +1%).
    - Gluteus medius and minimus: +2% vs +4%.
- **Deadlift, lunge, split squat and step-up for glute size: no study isolates any of them.** KrauseNeto2025 (systematic
  review, 12 studies; FULL) found none either, and its authors list these exercises as research gaps. Its pooled figure
  (SMD 0.71, 95% CI 0.50 to 0.91) is growth against baseline. It does not rank exercises, and it includes both Barbalho
  studies.

## 4. Adductors

- **Squats grow the adductors, deep squats more than half squats, and hip thrusts do not.** Strength: **limited** (two
  MRI trials; no study was designed around the adductors).
  - Kubo2019: adductor volume +6.2 ± 2.6% (full squat) vs +2.7 ± 3.1% (half squat), p = 0.026.
  - Plotkin2023: adductor cross-sectional area grew 2.5 cm² more with squats than with hip thrusts (95% CI 1.2 to 3.9).
- **No training study of the adduction machine, or of any other exercise, with adductor size as the target was
  found.**

## 5. Calves

- **Standing (straight-knee) calf raises grow far more calf than seated (bent-knee) calf raises.** Strength:
  **moderate** for the direction (one MRI trial with a very large effect and a clear mechanism); **limited** for the
  exact size.
  - Kinoshita2023 (14 untrained adults; one leg standing, the other seated; 12 weeks; 5 × 10 at 70% 1RM, twice a week;
    MRI volume; FULL).
    - Lateral gastrocnemius +12.4% vs +1.7%; medial gastrocnemius +9.2% vs +0.6%; whole calf +5.6% vs +2.1% (all
      p ≤ 0.011).
    - Soleus +2.1% vs +2.9% (p = 0.410). **The seated raise did not grow the soleus more.**
    - The gastrocnemius did not grow significantly in the seated leg at all.
    - Why: the gastrocnemius crosses the knee. Bending the knee slackens it, so it cannot work hard.
    - Limits: 14 people; no control group; measurement error for the lateral gastrocnemius was high (CV 9.8%).
- **The bottom (stretched) half of the calf raise does most of the work.** Strength: **limited**.
  - Kassiano2023b (RCT; 42 young women; 8 weeks; ABSTRACT): medial gastrocnemius thickness +15.2% with bottom-half
    partials vs +6.7% with full range and +3.4% with top-half partials (p ≤ 0.009).
  - Larsen2025b (23 **resistance-trained** adults; each leg a condition; 8 weeks; ABSTRACT): bottom-range partials vs
    full range followed by extra partials after failure. The difference favoured bottom-range partials by 0.40 mm (95%
    credible interval −0.06 to 0.85), with only "anecdotal" support (Bayes factor 1.2). In trained lifters the
    advantage is uncertain.
  - This is a range-of-motion finding already in the top-5 report. It is here because it changes how to do the
    exercise.
- **Toes out vs toes in may shift growth slightly between the two gastrocnemius heads.** Strength: **very limited**
  (one small trial, differences of a few percent, never replicated).
  - Nunes2020 (22 young men; 9 weeks; ABSTRACT): medial head +8.4% with toes out vs +3.8% with toes in; lateral head
    +9.1% with toes in vs +5.5% with toes out.

## 6. Abs / trunk

- **No training study was found that compares direct ab training with compound lifts only for ab muscle growth.**
  Three separate PubMed searches returned rehabilitation, electrical-stimulation and acute studies only. **Very
  limited** — this question is open.
- **One indirect data point.** HernandezBelmonte2023 (38 resistance-trained men; 8 weeks; ABSTRACT). The abstract
  lists only four trained exercises: full squat, bench press, prone bench pull and shoulder press. Rectus abdominis
  cross-sectional area still increased significantly in both the free-weight and the machine group. There was no
  ab-training arm, so this does not show that compound lifts are enough or that direct ab work adds nothing. I could
  not confirm from the full text that the programme had no ab exercise at all.
- No longitudinal study comparing ab exercises with each other (crunch vs leg raise vs rollout) was found. Any ranking
  of ab exercises rests on EMG, which is not evidence of growth.

## 7. Cross-cutting 1: free weights vs machines

- **Muscle growth is the same.** Strength: **moderate** (two meta-analyses and one good trial in trained men agree,
  but few studies measured muscle directly).
  - Haugen2023 (meta-analysis; 13 studies, 1,016 participants, 6 studies in trained people; only 5 studies measured
    hypertrophy; FULL): hypertrophy SMD −0.055 (95% CI −0.397 to 0.287). No funding, no conflicts declared.
  - Heidel2022 (meta-analysis; ABSTRACT): hypertrophy effect size −0.01, with a printed interval of −0.525 to 0.545.
    The interval is not centred on the estimate, so there is probably a typo. The conclusion is still "no
    difference".
  - HernandezBelmonte2023 (38 resistance-trained men; 8 weeks; identical programmes done with barbells or on machines;
    ABSTRACT): quadriceps, pectoralis and rectus abdominis cross-sectional area grew in both groups; between-group
    differences were ≤ 2.0 percentage points (P ≥ 0.208). Joint discomfort fell in both groups.
  - Schwanbeck2020 (46 young adults; 8 weeks; ABSTRACT) and MarcosFrutos2025 (37 students; 8 weeks; free-weight vs
    Smith machine squat and bench; ABSTRACT): no difference in muscle size.
- **Strength is specific to what you train.** Strength: **strong** (consistent across both meta-analyses and the
  trials).
  - Haugen2023: tested with free weights, free-weight training wins (SMD −0.210, 95% CI −0.391 to −0.029). Tested on
    machines, machine training tends to win (SMD 0.291, −0.017 to 0.600). Compared directly, no difference (0.084,
    −0.106 to 0.273).
  - Heidel2022: free-weight tests favour free-weight training (ES 0.655, 0.269 to 1.041); machine tests favour machine
    training (ES −0.784, −1.223 to −0.344); a neutral test shows no difference (ES 0.128, −0.303 to 0.559).
  - Wirth2016 (RCT; 78 students including controls; 8 weeks; ABSTRACT): squat training raised squat jump by 12.4% and
    countermovement jump by 12.0%; leg press training by 3.5% and 0.5% (not significant). For jumping, squats
    transferred better.

## 8. Cross-cutting 2: exercise variety

- **Muscles do not grow evenly, and the exercise decides which part grows.** Strength: **moderate** (several
  independent trials in sections 1–5).
  - Squat grows the vasti; leg extension grows the rectus femoris (Kassiano2026, Kubo2019).
  - Seated curl grows the hip-crossing hamstrings; Nordic grows the short head; stiff-leg deadlift grows the
    semimembranosus (Maeo2021, Maeo2024, Morin2025).
  - Hip extension grows the lower glute; hip abduction grows the upper glute (Attarieh2026).
  - Standing calf raise grows the gastrocnemius; seated does not (Kinoshita2023).
  - **This is the real argument for more than one exercise per muscle group: pick exercises that cover different
    muscles or heads.**
- **A second, similar exercise adds little.** Strength: **limited**.
  - Kassiano2025b (RCT; 70 young women; 10 weeks; ABSTRACT): leg press plus stiff-leg deadlift every session, vs
    rotating leg press / hack squat / Smith squat and stiff-leg deadlift / prone curl / seated curl across the week.
    - Thigh thickness at every site: +7.8–17.7% (constant) vs +7.5–19.3% (varied), p > 0.05.
    - 1RM: +24.4–32.1% vs +29.0–30.1%, p > 0.05.
    - This is the largest trial on variety, and it found nothing. Rotating between three squat-type lifts is redundant.
  - Fonseca2014 (RCT; 49 physically active people in 5 groups; 12 weeks; MRI; ABSTRACT): whole-quad growth was the
    same with constant or varied exercises (9.3–12.2%). Only the varied groups significantly grew every quad head; the
    constant groups missed the rectus femoris and/or vastus medialis. The varied-exercise group also gained the most
    squat strength. A reported secondary detail (via BazValle2019) is that the constant groups did squats only, which
    fits section 1.
  - Costa2021 (22 detrained men; 9 weeks; ABSTRACT): varied exercises grew all measured sites; fixed exercises missed
    two. Within-group p-values only, 11 per group.
- **Random rotation is not better and may be slightly worse.** Strength: **limited** (one small trial in trained
  men).
  - BazValle2019 (19 resistance-trained men completed; 8 weeks; FULL): exercises picked at random by an app each
    session vs a fixed list. Squat and bench 1RM and quad thickness rose similarly. Vastus intermedius grew
    significantly only in the fixed group. Motivation improved only in the random group.
  - Kassiano2022 (systematic review; 8 studies, 241 young men; no pooled estimate; ABSTRACT): some planned variation
    helps regional growth and strength; frequent or random rotation may hurt.
- **Letting trained lifters choose their own exercises did no harm.** Strength: **very limited**.
  - Rauch2020 (17 strength-trained men; 9 weeks; DXA; ABSTRACT): lean mass +2.47% (self-selected) vs +1.37% (fixed).
    The self-selected group also lifted more total volume, so the comparison is not clean.
- **Training at longer muscle lengths does not, on average, shift where along the muscle growth happens.**
  Strength: **limited**.
  - Varovic2025 (Bayesian meta-analysis; 12 studies; ABSTRACT): differences at proximal, middle and distal sites were
    trivial (SMD 0.05–0.09, all intervals crossing or touching zero). The compared conditions differed by only about
    22% of muscle length, so strong contrasts like seated vs prone curls may be diluted.

## 9. How exercise-specific is lower-body strength?

- **Very. You get strongest at the lift you train, and transfer to other lifts is partial.** Strength: **strong**.
  - Plotkin2023 (FULL): squat 3RM improved 14 kg more in the squat group (95% CI 9 to 18). Hip thrust 3RM improved
    26 kg more in the hip thrust group (16 to 34). Deadlift 3RM, which neither group trained, improved equally
    (difference 0 kg, −4 to 3).
  - Kassiano2026: squat 3RM +46.7% after squat training vs +21.3% after leg extension training (p < 0.001). Leg
    extension 3RM rose about equally in both (+19.8% vs +23.4%, p = 0.824).
  - Kubo2019: full-squat 1RM +31.8% after full-squat training vs +11.3% after half-squat training (p = 0.003). The
    reverse did not hold: half-squat 1RM rose similarly in both groups (p = 0.132). The deep lift transferred to the
    shallow one better than the other way round.
  - Bartolomei2025 (trained): hip thrust 1RM rose more in the hip thrust group (+17.9%, P = 0.004); squat 1RM rose more
    in the squat group (+10.5%, P = 0.007).
  - Rossi2018: squat training transferred to squat strength better than leg press training did (no numbers in the
    abstract).
  - Kassiano2025a (meta-analysis): bilateral training wins on bilateral strength (ES 0.56, 0.16 to 0.96); unilateral
    training wins on unilateral strength (ES −0.65, −0.93 to −0.37).
  - Saeterbakken2025 (meta-analysis; 43 studies, 1,660 participants; ABSTRACT): strength on the trained dynamic lift
    rose about twice as much as strength on an untrained isometric test (SMD 0.98 vs 0.42). Muscle growth did not
    predict either.
  - Morin2025: Nordic and stiff-leg deadlift training each carried over only partly to the other lift (+10.7% and
    +20.7%), and hamstring growth barely predicted the carry-over.

---

## Verdict

There is no single best leg exercise. Each compound lift grows some muscles and leaves others nearly untouched, and for
most direct "A vs B" questions lifters ask, no training study exists.

- **Quads (moderate):** squat-type lifts grow the vasti; they barely grow the rectus femoris. Leg extensions grow the
  rectus femoris, and more so when you lean back. Nothing ranks back squat, front squat, hack squat, leg press and split
  squat against each other for quad size.
- **Hamstrings (moderate):** seated leg curl beats lying leg curl by about half again (+14% vs +9% in 12 weeks). Hinges
  and curls grow different hamstrings, so do both. Squats do not grow hamstrings.
- **Glutes (limited):** hip thrust and deep squat grew the glutes about equally in the one good trial, which was in
  beginners and had hip-thrust-industry involvement. Deep squats beat half squats. Nothing isolates deadlifts, lunges
  or step-ups.
- **Adductors (limited):** deep squats grow them; hip thrusts do not.
- **Calves (moderate):** standing, straight-knee raises. Seated raises barely grew the gastrocnemius and did not grow
  the soleus more.
- **Abs (very limited):** no study compares direct ab work with compounds only. Unknown.
- **Free weights vs machines (moderate for size, strong for strength):** same growth. Strength goes to whichever you
  train on.
- **Variety (moderate for the principle, limited for the details):** use two exercises per muscle group when they hit
  different heads. Swapping between look-alike exercises, or rotating at random, adds nothing.
- **Strength (strong):** it is specific. To get strong at a lift, train that lift.

## Practical recommendation for Kye

Ranked picks per muscle. "Evidence" says how much weight each pick can bear. Nearly all of it comes from beginners, so
for an intermediate–advanced lifter treat the size of each effect as uncertain and the direction as the best available
guess.

1. **Quads — two exercises, not one.**
   1. A deep squat-pattern lift you can load hard and progress: back squat, hack squat or leg press. Evidence: moderate
      that this grows the vasti; none that one of the three beats the others. Pick on comfort and on which lift you
      want to be strong at. Go deep, because depth also buys glute and adductor growth.
   2. Leg extension, leaning back if the seat allows it. Evidence: moderate that squats alone leave the rectus femoris
      behind; limited (one trial) for the lean-back detail.
   - If you only squat, expect the front-middle of your thigh to lag.
2. **Hamstrings — two exercises, not one.**
   1. Seated leg curl. Evidence: moderate. If your gym only has a lying curl, it still works; it is just less
      effective for three of the four hamstrings.
   2. A hip hinge: Romanian or stiff-leg deadlift, or a 45° back extension. Evidence: limited, but hinges and curls
      grow different hamstrings and the strength barely carries over between them.
   3. Optional: Nordic curls. They favour the short head of the biceps femoris and the semitendinosus. Evidence:
      limited.
   - Do not count squats, leg press or hip thrusts as hamstring work.
3. **Glutes.**
   1. Your deep squat or leg press already counts. Evidence: limited.
   2. Add hip thrusts if you want more glute work without more quad and lower-back fatigue. Evidence: limited that
      they match squats; very limited that adding them on top gives extra.
   3. A hip abduction exercise if you want the upper glute and gluteus medius. Evidence: limited (one trial).
   - Honest caveat: there is no good trial of any of this in trained lifters.
4. **Adductors.** Deep squats cover them. If they matter to you, an adduction machine is a reasonable guess, but no
   growth study backs it.
5. **Calves.**
   1. Standing or leg-press calf raises with the knee straight. Sink into a full stretch at the bottom and do not rush
      out of it. Evidence: moderate for straight-knee; limited for the stretch emphasis.
   2. Skip the seated calf raise, or keep it as a minor extra. In the one trial it grew the gastrocnemius by about 1%
      and did not grow the soleus more than standing raises did.
6. **Abs.** Nobody knows whether direct work adds size beyond heavy compounds. If you want thicker abs, the sensible
   default is to train them like any other muscle: a loaded flexion exercise, 2–3 hard sets, a couple of times a week.
   That is reasoning from general principles, not a tested result.
7. **Free weights or machines.** Choose by preference, comfort and available equipment. Growth is the same. If you
   care about your barbell squat number, keep barbell squats in. If you do not, a hack squat or leg press costs you
   nothing in size.
8. **Variety.** Keep the same exercises for a whole block so you can add load and reps. Choose them to cover different
   heads (squat + leg extension; seated curl + hinge; hip extension + abduction). Do not rotate between near-identical
   lifts hoping for "confusion". Change an exercise when it hurts, stalls for weeks, or bores you.
9. **Strength.** Train the exact lift you want to be strong at. Leg press strength will not give you most of your
   squat strength.

## New avenues

1. **Do exercise-selection effects hold in trained lifters?** Seated vs lying curls, standing vs seated calf raises and
   squat vs leg extension have only been tested in beginners. Are there any trials since 2024 in people with 2+ years
   of training, or any registered and under way?
2. **Rectus femoris: what grows it best?** Leaning-back leg extension vs sissy squat vs reverse Nordic vs
   hip-flexion work. Only one hip-angle trial was found.
3. **Do direct ab exercises add rectus abdominis and oblique size beyond heavy compound lifting?** This run found no
   training study. A wider search (older literature, non-PubMed journals, theses) is needed before calling it
   untested.
4. **Deadlift variants, lunges, split squats and step-ups for glute and adductor growth.** No trial isolates any of
   them. Also: hack squat vs barbell squat vs leg press for quad size, and front vs back squat.

## Doubts / audit flags

- **Barbalho2020 and Barbalho2021.** I recall concerns being raised about the squat-vs-hip-thrust paper, but I could
  not find a retraction or expression of concern for it in PubMed, Europe PMC, Crossref or OpenAlex. That recollection
  is UNVERIFIED. The auditor should check the publisher's page for both papers. PubMed also links Barbalho2021 to an
  erratum whose DOI resolves to an unrelated 2016 correction; the record looks mis-linked. Neither paper carries any
  weight in the verdict.
- **31 of the 38 rows are ABSTRACT only.** Publisher sites were blocked and most papers have no Europe PMC full text.
  Only Plotkin2023, Maeo2021, Maeo2024, Kinoshita2023, Haugen2023, BazValle2019 and KrauseNeto2025 were read in full,
  and for those I read the methods, results, limitations and funding sections rather than every page. The abstract-only
  papers that carry the most weight are Kassiano2026, Kubo2019, HernandezBelmonte2023, Kassiano2025b, Larsen2025a,
  Morin2025, Bourne2017, Attarieh2026 and Heidel2022. The auditor should try the full text of Kassiano2026 and Kubo2019
  first, since the quad verdict rests on them.
- **Missing sample details.** Rossi2018 and ZabaletaKorta2021 give no sample size in the abstract. Kubo2019,
  Attarieh2026, Kassiano2023b, Kassiano2025b and Crawford2025 do not state training status in the abstract.
- **Heidel2022 hypertrophy interval** is printed as −0.01 (−0.525 to 0.545), which is not centred. Probably a typo in
  the abstract.
- **Kassiano2023a is a preprint.** No journal version was found today, although KrauseNeto2025 cites it as 2024. The
  auditor should check whether it was published and whether the numbers changed.
- **Bourne2017 has a correction** (doi 10.1136/bjsports-2016-096130corr1) that I did not read.
- **Plotkin2023 correction.** I read it in full. It changes the funding, conflict-of-interest and registration
  statements only. The retrospective registration and the equipment donation are worth keeping in mind.
- **"No study found" claims** (front vs back squat; hack squat; deadlift, lunge and step-up for glutes; leg curl vs
  Romanian deadlift; direct ab training; adductor exercises) rest on about 30 searches of PubMed and Europe PMC.
  Studies in journals not indexed there could have been missed. The KrauseNeto2025 review independently lists the
  glute gaps.
- **Secondary details.** Protocol details for Barbalho2020/2021, the squat depths in Kubo2019 (140° and 90°), the
  training experience in Bartolomei2025, and the "squat only" detail for Fonseca2014 come from other papers
  (KrauseNeto2025, BazValle2019), not the originals.
- **Kassiano2025b participants** are described as young women. I wrote "likely untrained" in the CSV; that is my
  inference, not a statement in the abstract.
- **Section 1 mechanism** (why squats miss the rectus femoris) is standard anatomy, not a tested finding in these
  trials.
- All 38 DOIs resolved on Crossref today. Corrections were found for Plotkin2023 and Bourne2017 only. No retractions
  were found among the cited papers.
