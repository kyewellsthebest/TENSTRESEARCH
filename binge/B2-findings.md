# B2 — Weekly eating patterns, cheat/refeed days and binge behaviour

Agent B2, 2026-11-08. Brief: `BRIEF.md` (registered before searching). Prior work not redone:
`../fatloss/W2-findings.md` (carb cycling, refeeds, diet breaks) and `../fatloss/WA-audit.md` (verification of
MATADOR, ICECAP, Campbell 2020). Rows for those studies are carried into `B2-studies.csv` with their earlier
verification status.

**Access, stated once.** WebFetch could not reach `pmc.ncbi.nlm.nih.gov` or `eprints.whiterose.ac.uk`. Both
failed with ENOTFOUND, because those hosts are not in this session's allowed network domains. No full text was
opened. Every source below is **ABSTRACT** (abstract text reached through search extracts) or **SECONDARY**
(seen only through a review, a press release or another paper). Numbers are given only where an abstract or
record stated them. Anything else is marked UNVERIFIED.

**Evidence codes**, adapted from PROTOCOL §5 for diet questions, as the fat-loss notes did:
- **D**: direct test in a comparable population (trained or free-living adults, weeks-long, body composition
  measured).
- **I**: indirect (other populations, such as obese, sedentary or clinical groups, or surrogate outcomes).
- **M**: mechanism or arithmetic.
- **H**: inference or hypothesis, not tested.

Grades are strong / moderate / limited / very limited / none.

---

## Plain-English summary

1. **Over a week, the weekly total is what counts for fat. The order of the days barely matters.** Pooled trials
   compared intermittent with continuous restriction at similar total intake: 5:2, alternate-day fasting,
   calorie shifting and 2-week diet breaks. They found about the same weight and fat loss. In trained lifters,
   weekly 2-day refeeds and 1-week diet breaks gave the same fat loss as continuous dieting. The one big "breaks
   work better" result (MATADOR) used 2-week blocks in obese men. It does not show that one big day a week is
   special. *(D/I, moderate)*
2. **Weekends are where diets leak, in the research as well as in Kye's week.**
   - In a 1-year trial (Racette 2008), dieters lost weight on weekdays and **stopped losing on weekends**.
   - The exercise group **gained** on weekends because it ate more.
   - At population level, adults eat about **80–115 kcal/day more** on Friday to Sunday than on Monday to
     Thursday (Haines 2003).
   - Kye's +1,000 kcal Sunday is roughly 10 times that. *(I, moderate)*
3. **A heavier Sunday or Monday on the scale is normal and is not fat.** Daily-weigh studies show weight peaks
   on Sunday or Monday and falls to a low on Friday:
   - Orsama 2014: n = 80.
   - Turicchi 2020: n = 1,421, swing about 0.35%.

   People who lost weight overall still showed the weekend bump. They "paid it back" during the week. On an 85 kg
   lifter, 0.35% is about 0.3 kg. Feeling "fatter" on Monday while the scale stays flat fits gut contents,
   glycogen and water, not new fat. *(I, moderate for the rhythm; M/H for the cause of the feeling)*
4. **Is a 1,000 kcal overshoot once a week alright? Yes, if the deficit on the other days is big enough to
   absorb it, and if it is a choice, not a loss of control.** The worked maths (section 4), Mon–Thu plus one
   more deficit day, Fri/Sat at true maintenance, Sunday +1,000:
   - At **250 kcal/day × 5**, the Sunday cancels **80%** of the week's deficit. Fat loss is essentially stalled
     (≈ 0.03 kg/week).
   - At **500 × 5** it cancels **40%** (≈ 0.2 kg/week instead of 0.3).
   - At **750 × 5** it cancels **27%** (≈ 0.36 kg/week instead of 0.5).

   The Sunday never "adds fat" over the week unless the week as a whole lands in surplus. That happens when the
   overshoot exceeds 5 × the daily deficit, or when Friday and Saturday are not really maintenance.
   *(M, strong for the arithmetic; the kcal-per-kg conversion is approximate)*
5. **A planned high day and a binge are different things, and the difference is control, not calories.**
   - Restraint research (Herman & Mack 1975; Polivy et al. 2010) shows the **"what-the-hell" effect**. Rigid
     dieters who think they have "blown it" eat *more*, not less.
   - **Rigid**, all-or-nothing dieting goes with more binge eating and higher BMI. **Flexible** dieting goes with
     less of both (Westenhoefer 1999; Smith 1999; Stewart 2002). These are cross-sectional associations.
   - In people without an eating disorder, supervised dieting does not reliably *cause* binge eating (da Luz
     2015).
   - Planned "cheat meals" are near universal in young adults. Their frequency is associated with binge episodes
     and eating-disorder symptoms, at least in men (Murray 2018; Ganson 2022).
   - There is **no trial** showing a planned weekly high day improves or harms adherence in lifters.
   - *(I, limited)*
6. **Physique athletes are the warning case, not the model.** In surveys of natural bodybuilders:
   - **46%** reported binge eating after competitions and 85% regained weight (Andersen 1995, n = 45).
   - Female fitness athletes showed worse disordered-eating scores one month after a show than during
     preparation (Mathisen 2019).
   - Hard, prolonged cuts are where loss-of-control eating shows up. Kye's moderate cut is not that, but the
     direction of risk is the same. *(I, limited)*
7. **When to get help (Australia), without alarm.** It is worth talking to a GP or the **Butterfly Foundation
   National Helpline, 1800 33 4673 (1800 ED HOPE)** if any of these hold:
   - Sundays feel *out of control*: you can't stop, you eat far past full, you eat in secret, or you feel guilt
     or disgust afterwards.
   - It happens about weekly for months.
   - It is followed by fasting or extra cardio to "make up for it".
   - It is causing real distress.

   The number was checked against Butterfly's own pages. One large, enjoyed, chosen meal is not a disorder.

**Bottom line for Kye.** A chosen +1,000 kcal Sunday is compatible with fat loss if:
- the weekday deficit is about 500 kcal/day or more;
- Friday and Saturday are genuinely maintenance, not "maintenance-ish";
- Sunday is actually about +1,000 and not +2,000 uncounted;
- Monday is a normal deficit day, not a punishment fast.

At a 250 kcal/day deficit, the Sunday is most of the reason the scale won't move. The Monday "fat" feeling is
water, glycogen and gut contents. Judge progress on the weekly-average or Friday-to-Friday trend, never on the
Monday weigh-in.

---

## 1. Does the weekly pattern matter if the weekly total is the same?

### 1a. Intermittent vs continuous energy restriction (IER vs CER), pooled evidence

- **Schroor 2024** (Adv Nutr 15(1)): 28 RCTs in healthy adults, 2–52 weeks:
  - **Trials:** TRE k = 7, ADF k = 10, 5:2 k = 11.
  - **Pooled result:** the three IER diets combined "did not lead to superior improvements" in anthropometrics
    or cardiometabolic markers vs CER.
  - **Lean and waist:** IER lost slightly more fat-free mass (WMD −0.20 kg, 95% CI −0.39 to −0.01) and slightly
    more waist (−0.91 cm, CI −1.76 to −0.06).
  - **Subgroups:** TRE alone reduced weight, FM and FFM more than CER. BMI fell less with 5:2.
  - **Caveat:** energy intake was comparable in only 17 of 28 trials, lower with IER in 5, and unreported in 6.
  - ABSTRACT. *(I, moderate)*
- **Cioffi 2018** (J Transl Med; 11 RCTs): IER gave "comparable" weight loss to CER. Long-term trials are
  needed. ABSTRACT. *(I, moderate)*
- **Headland 2016** (Nutrients; trials ≥ 6 months, 981 randomised): no significant difference in weight loss.
  Most trials had fewer than 50 completers. ABSTRACT. *(I, moderate)*
- **Davis 2016** (Eur J Clin Nutr; 8 studies): IER gave comparable weight loss to daily restriction "when overall
  energy restriction remained similar". SECONDARY (search extract of abstract). *(I, limited–moderate)*
- **Harvie 2011** (Int J Obes; n = 107 premenopausal women, 6 months):
  - **Diet:** 2 consecutive days per week at 25% of needs (the 5:2 prototype) vs CER.
  - **Weight:** −6.4 kg (95% CI −7.9 to −4.8) vs −5.6 kg (−6.9 to −4.4), P = 0.4.
  - **Insulin:** slightly better insulin sensitivity with IER.
  - **Dropout:** 11 vs 7 withdrew.
  - ABSTRACT. *(I, moderate)*

**Reading.** At matched weekly energy, the weekly *shape* of intake has no meaningful effect on fat loss in
non-athletes. Where IER looks better or worse, the arms usually differed in actual intake. *(I, moderate)*

### 1b. Calorie cycling / "zig-zag"

- **Davoodi 2014** (Int J Prev Med; n = 74 overweight women, 6 weeks plus 4-week follow-up):
  - **Diet:** calorie shifting (cycles of 11 restricted days and 3 free days) vs fixed restriction.
  - **Result:** both lost weight. The abstract reports losses of 6.02 and 5.15 kg, falling to 5.24 and 4.3 kg at
    follow-up. It does not clearly assign these to arms (UNVERIFIED which is which). The authors report better
    adherence and "greater improvement in some anthropometric measures" with shifting.
  - **Limits:** small, short, one centre, untrained women.
  - ABSTRACT (and W2). *(I, limited)*

### 1c. Refeeds and diet breaks in trained people (from W2/WA, not re-searched)

- **Campbell 2020**: n = 27 resistance-trained adults, 7 weeks, 5 days at about 25% deficit plus 2 high-carb
  refeed days per week vs continuous. No fat-loss advantage. On reanalysis, only dry FFM differed. *(D,
  limited)*
- **Peos 2021 ICECAP**: n = 61 resistance-trained adults; 4 × 3-week restriction with 1-week maintenance breaks vs
  continuous. Fat loss and FFM were similar. Appetite was lower with breaks. *(D, moderate)*
- **Byrne 2018 MATADOR**: n = 51 obese men; 2-week blocks of restriction and maintenance vs continuous.
  - **Fat loss:** INT lost more fat, 12.3 ± 4.8 vs 8.0 ± 4.2 kg, in a completer analysis.
  - **Follow-up:** about 8 kg more weight lost from baseline at 6 months (press and interview figures; exact
    table UNVERIFIED).
  - **Design:** 2-week blocks, not a weekly high day.
  - **Generalising:** obese untrained men; not replicated in trained people (ICECAP was the replication attempt,
    and it was null for fat).
  - *(I, limited)*

**Answer to 1.** A weekly high day is a way of *distributing* the same weekly energy. It does not change fat
balance. It is neither a metabolic trick nor a metabolic penalty. What it can change is **adherence and
appetite**. That is a behavioural effect, and it can go either way (section 3). *(D/I, moderate)*

---

## 2. Weekends and weekly weight cycles

### 2a. Weekend eating stalls dieting

**Racette 2008** (Obesity 16:1826; CALERIE sub-study, n = 48 adults aged 50–60, 1 year):
- **Arms:** calorie restriction, daily exercise, or control.
- **Measures:** food diaries and accelerometers, validated against doubly labelled water.
- **Baseline:** participants gained on weekend days, +0.06 ± 0.03 kg/day (mean ± SE, P = 0.02), and not on
  weekdays, −0.02 ± 0.02 kg/day.
- **During intervention:** the CR group lost on weekdays and **stopped losing on weekends**. The exercise group
  **gained** on weekends, +0.08 ± 0.03 kg/day, attributed to higher weekend intake.
- **Authors' reading:** this is "one explanation for the relatively slow rates of weight loss observed in many
  studies".
- **Limits:** ABSTRACT. Older, non-lifting adults. The "9 lb/year" figure is from the press release, not the
  abstract.
- *(I, moderate)*

### 2b. How big is a typical weekend surplus?

**Haines 2003** (Obes Res 11:945; US national survey data):
- Weekend days (Friday to Sunday) carried **+82 kcal/day** vs Monday to Thursday for everyone aged 2 and over.
- For adults aged 19–50 it was **+115 kcal/day**, with more fat and alcohol.
- ABSTRACT. *(I, moderate)*

So the "ordinary" weekend surplus is about 250–350 kcal over three days. Kye's planned Sunday is +1,000 on one
day, roughly 3–4 times a typical whole weekend's excess. That is not abnormal for a deliberate high day, but it
is large. *(M)*

### 2c. The weekly weight rhythm

- **Orsama 2014** (Obes Facts 7:36–47; n = 80 adults, 4,657 self-weighings pooled from four studies):
  - **Rhythm:** weight rises from Saturday, starts falling on Tuesday, and is lowest late in the week.
  - **Peaks and troughs (press summary):** in people losing weight, the weekly maximum fell on Sunday or Monday
    in about 59% of weeks and the minimum on Friday or Saturday in about 60% (SECONDARY; the exact abstract
    numbers are UNVERIFIED).
  - **Compensation:** the weekday "compensation" was strongest in people who lost or maintained weight and
    weakest in slow gainers. The authors say weekend–weekday variation "should be considered as normal".
  - **Caution:** retrospective. A co-author (B. Wansink) later had multiple retractions for misconduct. No
    retraction of this paper was found, but treat it with caution (UNVERIFIED whether it has been examined).
  - ABSTRACT. *(I, limited–moderate)*
- **Turicchi 2020** (PLoS One 15:e0232152; NoHoW trial smart-scale data, weekly analysis n = 1,421, adults
  maintaining weight loss):
  - Weight was highest on Monday, fell through the week, and was lowest on Friday.
  - The within-week swing is about **0.35%**. One extract attributes that figure to an earlier cited study
    rather than to NoHoW itself, so the exact NoHoW amplitude is UNVERIFIED.
  - A separate Australian dataset (n = 368, cited secondarily) reported a Friday weight 0.18% below Monday's.
  - ABSTRACT / SECONDARY. *(I, moderate for the direction; limited for the amplitude)*

**What this means for "I feel fatter on Monday but the scale is the same".**
- The normal Monday peak is a few tenths of a kilo: 0.3–0.35% of 85 kg is about 0.25–0.3 kg. That is water,
  glycogen, sodium and gut contents. It is not fat, because a 1,000 kcal surplus can make at most about 0.1 kg of
  fat even if every calorie were stored (section 4).
- If Kye's scale reads the *same* on Monday, his weekend added less transient mass than the typical rhythm. The
  "fatter" feeling is most likely bloating, a fuller gut and a softer look from extra subcutaneous water and
  sodium, plus the expectation effect of having eaten a lot.
- *(M/H; acute fluid and glycogen physiology is covered elsewhere in this binge series and in W2)*

**Practical: how to read the scale.** Compare like with like:
- Friday to Friday, or a 7-day rolling average.
- The Monday weigh-in is the noisiest point of the week for anyone with a heavier weekend.

*(I, moderate; consistent with WA-audit's "adjust from the trend, never a single weigh-in")*

---

## 3. Binges as behaviour

### 3a. Restraint theory and the "what-the-hell" effect

- **Herman & Mack 1975** (the founding preload study):
  - **Design:** participants drank 0, 1 or 2 milkshakes, then had an ad-lib ice-cream "taste test".
  - **Result:** unrestrained eaters ate less after more milkshake. **Restrained eaters ate more**
    ("counter-regulation").
  - **Follow-up:** a preload *labelled* high-calorie produced the effect even when it was not (Polivy 1976, as
    cited).
  - SECONDARY (review extracts). *(I/M, moderate as a lab phenomenon)*
- **Polivy, Herman & Deo 2010** (Appetite 55:426): everyone got the same pizza slice. Restrained eaters who
  *believed* theirs was bigger than another person's ate more cookies afterwards; unrestrained eaters ate fewer.
  Polivy calls this the **"what-the-hell effect"**: the diet is "broken" anyway, so why be good. ABSTRACT, plus a
  SECONDARY source (University of Toronto Magazine) for the phrase. *(I, limited–moderate)*
- **Polivy & Herman 1985** ("Dieting and binging: a causal analysis", Am Psychol) is the theoretical statement
  that dieting precedes and promotes binging. It was not reached in this search: **UNVERIFIED** content. It is
  cited here only as the origin of the idea.

**Transfer to Kye.** The danger in a "cheat day" is not the planned 1,000 kcal. The danger is the framing.
- If Sunday is defined as "the day the diet is off", the first unplanned excess can turn into "Sunday's ruined,
  might as well…", and the overshoot is no longer 1,000.
- If Sunday is a *planned, budgeted* higher day, it is part of the diet, and there is nothing to "break".
- *(H, built on I-level lab evidence)*

### 3b. Rigid vs flexible restraint

- **Westenhoefer 1999** (Int J Eat Disord 26:53; validation of TFEQ subscales):
  - **Flexible control** went with lower disinhibition, lower BMI, **less frequent and less severe binges**,
    lower intake, and a higher chance of successful weight loss in a 1-year programme.
  - **Rigid control** went with higher disinhibition, higher BMI and **more frequent and severe binges**.
  - ABSTRACT. *(I, moderate)*
- **Smith 1999** (Appetite 32:295): canonical correlations, cross-sectional.
  - Flexible dieting went with no overeating, lower BMI and less depression and anxiety (r = 0.65).
  - Rigid calorie counting and conscious dieting went with overeating alone and higher BMI (r = 0.59).
  - ABSTRACT. *(I, limited)*
- **Stewart 2002** (Appetite 38:39; n = 188 non-obese women): rigid dieting went with eating-disorder symptoms,
  mood disturbance and shape concern. Flexible dieting did not. The authors note that a cross-sectional design
  cannot address causality. ABSTRACT. *(I, limited)*
- **Linardon & Mitchell 2017** (Eat Behav 26:16; n = 372): intuitive eating predicted lower disordered eating more
  consistently than rigid control. Flexible control's benefit appeared only once rigid control was accounted
  for. ABSTRACT. *(I, limited)*

**Reading.** These are associations, mostly cross-sectional and in women. They are consistent across 25 years.
They do **not** prove that switching to flexible dieting prevents binges. *(I, limited–moderate)*

### 3c. Does restriction cause binges?

- **da Luz 2015** (Obes Rev 16:652; 15 supervised interventions in 10 papers, mostly women, overweight or obese):
  - In people **with** pre-treatment BED, severe restriction **reduced** binge eating during the programme.
  - In people **without** BED (11 interventions), there was "no consistent association" between severe
    restriction and the onset of binging.
  - Some lower-quality studies showed a transient rise, usually just after the diet.
  - ABSTRACT. *(I, moderate for supervised clinical diets)*
- **Hoddy 2015** (Nutr J 14:44; alternate-day fasting, 59 of 74 completers, 8 weeks, obese adults, single arm):
  binge-eating score fell from 33 to 30 and restrictive eating rose. Purging was unchanged. Dropouts were not
  assessed. ABSTRACT. *(I, limited)*
- **Stice and colleagues** (prospective adolescent cohorts): elevated dieting predicted later binge-eating onset
  in adolescent girls (2-year study). Body dissatisfaction was the stronger predictor in an 8-year cohort.
  ABSTRACT/SECONDARY. *(I, limited for adult men)*

**Reading.** Moderate, structured dieting in adults without a history of disordered eating does not reliably
produce binge eating. Self-directed, rigid, appearance-driven dieting in young people is a risk factor. The
risk tracks *how* someone diets and *why*, more than the deficit size. *(I, limited–moderate)*

### 3d. Planned high days / cheat meals: adherence aid or trigger?

- **Coelho do Vale 2016** (J Consum Psychol 26:17): two experiments (one simulated, one with real dieters) and a
  third study. Diets with **planned** "hedonic deviations" were followed as well as or better than strict
  straight-line plans. Participants reported more self-regulatory resources and motivation. Short, small,
  consumer-psychology design; effect sizes not reached. ABSTRACT. *(I, limited)*
- **Murray 2018** (Appetite 130:274; n = 248 young adults):
  - 89% had cheat meals, planned or spontaneous. Planned ones were mostly to manage cravings and sustain strict
    regimens.
  - In **men**, cheat-meal frequency was associated with eating-disorder symptoms (P = 0.04) and objective binge
    episodes (P = 0.03).
  - It was not associated with distress or impairment.
  - Cross-sectional, "preliminary". ABSTRACT. *(I, limited)*
- **Ganson 2022** (J Eat Disord 10:113; n = 2,717 Canadian 16–30-year-olds):
  - Past-year cheat meals: 60.9% of men, 53.7% of women.
  - **1,000–1,499 kcal was the most common reported size.**
  - Engagement was associated with eating-disorder behaviours, including binge-related ones.
  - Cross-sectional. ABSTRACT. *(I, limited)*
- **Pila 2017** (Int J Eat Disord; content analysis of 600 #cheatmeal Instagram images): cheat meals are framed as
  goal-directed practice in physique culture. ABSTRACT. *(I, very limited)*
- **ICECAP** (Peos 2021): lower appetite with planned maintenance weeks, in trained people. *(D, moderate; an
  appetite outcome, not binge eating)*

**Reading.** Kye's +1,000 Sunday is **exactly the modal "cheat meal" size** in the largest survey. No trial has
tested whether a planned weekly high day improves or harms adherence in lifters.
- **For:** small experiments and ICECAP's appetite result point to a planned deviation helping. *(I/D, limited)*
- **Against:** cross-sectional surveys show that people who cheat-meal often also report more binge episodes.
  That may mean cheat meals feed binging, that people who binge relabel binges as "cheat meals", or both. The
  surveys cannot tell which. *(I, limited)*

### 3e. Physique athletes: post-diet rebound

- **Andersen 1995** (Int J Eat Disord 18:49; n = 45 drug-free male bodybuilders, surveyed on competition
  morning):
  - Mean 6.8 kg lost per season and 6.2 kg regained.
  - **46% reported binge eating after competitions**; 85% reported gaining weight afterwards; 81.5% were
    preoccupied with food at least sometimes.
  - ABSTRACT. *(I, limited)*
- **Goldfield 2006** (Can J Psychiatry 51:160; 27 competitive and 25 recreational male bodybuilders, plus 22 men
  with bulimia nervosa): high rates of binge eating and BN in bodybuilders, **especially competitors**. Exact
  percentages not reached. ABSTRACT. *(I, limited)*
- **Mathisen 2019** (Sports 7:236; 25 female fitness athletes and 26 controls, measured at baseline, 2 weeks
  before a show and 1 month after):
  - Restraint rose and disordered-eating symptoms *fell* at competition.
  - **One month after**, "self-control deteriorated" with higher disordered eating and shape concern.
  - Binge eating as a separate figure was not reached.
  - ABSTRACT. *(I, limited)*
- **Female physique thesis** (SECONDARY; LJMU 2024 PhD, Alwan):
  - Figure athletes gained 5.5% body mass in the 7 days after competition.
  - 34% of novice figure athletes reported binge eating at least once.
  - Thesis, not peer-reviewed in this form.
  - *(I, very limited)*
- **Suffolk 2015** (n = 78 over a 10-month season, SECONDARY): disordered eating rose before competition and
  returned to baseline afterwards. Cross-sectional snapshots may overstate pathology. *(I, limited)*
- **Buechel 2026** (JISSN; 19 natural physique athletes, about 21 weeks of preparation then 12 weeks of
  recovery): eating-disorder symptom severity (EDE-QS) was highest during preparation and declined in recovery.
  A larger post-show intake increase went with better RMR recovery (exploratory). ABSTRACT. *(I, limited)*
- **Chappell 2018** (JISSN; 51 British natural bodybuilders): contest-prep practices, including planned refeeds.
  Post-competition outcomes were not reached. ABSTRACT. *(context only)*

**Reading.** Long, deep cuts to stage-lean are associated with post-diet binge eating in a large minority of
competitors, roughly half of men in the one quantified survey. The evidence comes from small, mostly
self-report samples. Kye is not on a stage cut. The lesson that transfers is that **the deeper and longer the
restriction, and the more appearance-driven, the more likely loss-of-control rebound**. That is one reason to
prefer a sustainable deficit over a hard one. *(I, limited; transfer H)*

### 3f. Binge eating disorder in plain words (DSM-5)

This is for orientation only. It is not a diagnosis. DSM-5 binge eating disorder needs **all** of:

1. **Episodes** of eating an amount most people would see as definitely large, in a bounded period (about
   2 hours), **with a sense of loss of control**: you can't stop, or can't control what or how much.
2. **At least three of:**
   - eating much faster than normal;
   - eating until uncomfortably full;
   - eating large amounts when not hungry;
   - eating alone because of embarrassment;
   - feeling disgusted, depressed or very guilty afterwards.
3. **Marked distress** about the binge eating.
4. **About once a week or more, for three months.**
5. **No regular "compensating"** by vomiting, laxatives, fasting or excessive exercise. That pattern points
   towards bulimia nervosa instead, which also warrants help.

Severity is graded by episodes per week: mild 1–3, moderate 4–7, severe 8–13, extreme 14+. (ABSTRACT/SECONDARY
via the DSM-5 table reproduced in PMC and InsideOut Institute's criteria sheet; APA text not opened directly.)

**What separates Kye's planned Sunday from this:**
- Was it decided in advance?
- Was the amount roughly chosen?
- Did it stop when planned?
- Is there no guilt spiral and no Monday "punishment"?

Calories alone do not decide it. A 1,000 kcal planned meal eaten with control is not a binge. A 600 kcal
episode with no ability to stop, eaten in secret, followed by disgust, is closer to one.

### 3g. When to talk to someone (Australia), without alarm

These are worth raising with a GP or the Butterfly Foundation:
- Sundays (or any day) increasingly feel **out of control** rather than chosen.
- The "1,000 over" keeps becoming 2,000–3,000.
- You eat in secret.
- You feel shame or disgust afterwards.
- You "compensate" with fasting or extra cardio.
- It happens roughly weekly for months.
- Food and body thoughts take up a lot of the day.

Contacts:
- **Butterfly Foundation National Helpline: 1800 33 4673 (1800 ED HOPE)**, plus webchat and email. Butterfly's
  pages give **8 am to midnight AET, 7 days**, closed on national public holidays. The number was confirmed on
  butterfly.org.au and the healthdirect partner page. The hours come from search extracts of Butterfly's
  helpline page; check them before quoting in a product.
- It is not a crisis line. In an emergency, call 000. For crisis support, call Lifeline on **13 11 14**.
- A GP is the usual first step for assessment and referral. Australian GPs can arrange eating-disorder
  treatment plans (the Medicare item details were not verified in this search).

None of this applies to one big, enjoyed, chosen meal a week. It is about *control and distress*, not
calories.

---

## 4. Worked weekly maths: is a 1,000 kcal overshoot once a week "alright"?

**Assumptions** (M):
- 5 deficit days at D kcal/day below maintenance.
- Friday and Saturday at true maintenance (0).
- Sunday at +1,000.
- Weight change uses about 7,700 kcal/kg, the classic 3,500 kcal/lb rule. Hall 2008 shows the rule
  *overestimates* the energy cost per kg in leaner people, and that early-diet tissue loss carries less energy
  per kg (about 4,860 kcal/kg at week 4 in CALERIE data, SECONDARY). The kg figures below are therefore
  order-of-magnitude, and the **percentages are exact**.

| deficit D on 5 days | 5-day deficit | Sunday | weekly net | share of deficit cancelled | ≈ fat change/week | without the Sunday |
|---|---|---|---|---|---|---|
| 250 | −1,250 | +1,000 | **−250** | **80%** | ≈ −0.03 kg | ≈ −0.16 kg |
| 500 | −2,500 | +1,000 | **−1,500** | **40%** | ≈ −0.19 kg | ≈ −0.32 kg |
| 750 | −3,750 | +1,000 | **−2,750** | **27%** | ≈ −0.36 kg | ≈ −0.49 kg |

**What the Sunday does on its own.** Even if every one of the 1,000 kcal were stored as fat (they are not; some
is spent on digestion and some goes to glycogen), that is about 1,000 / 9,400 kcal per kg of pure fat ≈
**0.11 kg**. The week's *net* is what decides whether fat goes up. A single +1,000 day inside a week that is
still net negative does not leave the week fatter. *(M, strong)*

**When it erases progress:**
1. **The weekday deficit is small.** At 250 kcal/day, the Sunday cancels 80%. Break-even is a Sunday of
   5 × D: 1,250 at D = 250, 2,500 at D = 500, 3,750 at D = 750. *(M)*
2. **"Maintenance" Friday and Saturday aren't.** Racette's dieters lost nothing on weekends, and typical adults
   add about 80–115 kcal/day on weekends without trying. If Friday and Saturday each run +300 above true
   maintenance, the 500/day week drops from −1,500 to −900 (60% cancelled). The 250/day week turns into a
   **surplus** (+350). *(I + M)*
3. **The overshoot is bigger than it feels.** Free-eating days are the least accurately logged. People
   systematically under-report intake (well established; specific figures not verified in this search).
   A "1,000" Sunday that is really 1,500–2,000 erases a 250/day week outright and halves a 500/day one.
   *(H, plausible)*
4. **It becomes a loss-of-control pattern.** Then the size is no longer bounded, and the what-the-hell dynamic
   can spread it into Monday (section 3a). *(I, limited)*
5. **Monday "makes up for it" with a fast.** Compensatory restriction is the restriction–binge cycle that the
   restraint literature describes. The weekly maths already includes Sunday, so Monday needs nothing extra.
   *(H, built on I-level evidence)*

**When it is fine:**
- D ≥ about 500 kcal/day on the deficit days.
- Friday and Saturday really are maintenance (tracked at least roughly).
- Sunday is planned, roughly counted and bounded.
- Monday is a normal day.

The weekly trend then still falls at roughly 60–75% of the no-Sunday rate. That may be a fair price for a
diet he can keep up. *(M + I, moderate)*

**A simpler equivalent, if Kye wants Sunday without the arithmetic.** Spread the 1,000 across the 5 deficit days
by deepening each by 200 kcal. Or accept the slower rate and judge it on the weekly-average trend. The trial
evidence (section 1) says either distribution gives the same fat loss at the same weekly total. Choose
whichever he sticks to. *(I, moderate)*

---

## 5. Gaps and caveats

- **No full text was opened.** PMC and White Rose are blocked in this session. Every number is from an abstract
  or extract, and those are listed as such in the CSV.
- **No RCT** has tested "planned weekly high day vs evenly spread intake" in resistance-trained adults with
  adherence, binge episodes and body composition as outcomes. Campbell 2020 is the nearest (2-day carb refeeds,
  n = 27, no eating-behaviour outcome).
- The rigid/flexible restraint and cheat-meal literature is **cross-sectional**, mostly in women or young
  adults, and mostly self-report.
- The physique-athlete binge data are small surveys, partly decades old (Andersen 1995). They concern stage cuts,
  not moderate deficits.
- **Not reached (UNVERIFIED):**
  - Polivy & Herman 1985 content.
  - The exact Turicchi NoHoW amplitude.
  - Orsama's exact day percentages.
  - Which Davoodi arm each loss figure belongs to.
  - The MATADOR 6-month table.
  - The Goldfield 2006 percentages.
  - Medicare eating-disorder plan details.
- **Acute overfeeding physiology** (thermic effect, glycogen and water, de novo lipogenesis after a single big
  day) is out of scope here. It is referenced only as far as the "≤ 0.11 kg fat" ceiling, which is arithmetic.
