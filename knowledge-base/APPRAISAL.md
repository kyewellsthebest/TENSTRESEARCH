# Appraisal protocol: how to find, screen, judge and discard studies

Written 2026-11-15. Every deep-dive topic follows this. It sits under `RUN.md`: RUN.md says *when* to research,
this file says *how*. Citation keys (`[Page2021]`) point to `appraisal-studies.csv`, where each source's DOI, access
level and how it was verified are recorded.

**The one-line version:** search wide, screen generously, read the full text, judge each study's risk of bias with
the right tool, write down every decision and its reason in a CSV, and rate the whole body of evidence with GRADE.
Don't trust any one study, abstract or author conclusion.

---

## 0. Ground rules

1. **Never invent anything.** That covers studies, DOIs, numbers, sample sizes and methods. If you can't verify it,
   write `UNVERIFIED`.
2. **Every decision goes in a file.** That includes every record found, every exclusion and its reason, and every
   risk-of-bias judgement and what drove it.
   - *Why:* PRISMA 2020 requires a flow of records with counts and reasons at each stage, and PRISMA-S requires a
     search that someone else can reproduce [Page2021; Rethlefsen2021].
   - Context windows end and the next session needs to pick up exactly where this one stopped.
3. **Full text before verdict.** An abstract can be used to *exclude* a study. It is never enough to *include* one
   in a verdict. Mark access as FULL, ABSTRACT or SECONDARY.
   - *Why:* spin is common in abstracts. In 72 RCTs whose primary outcome was not significant, 58% of the abstract
     conclusions still spun the result as positive [Boutron2010].
4. **Judge the study, not the journal, the authors or the conclusion.** Sport science reports supported hypotheses
   about 81–82% of the time, which is implausibly high [Buttner2020; Twomey2021]. Average statistical power is
   about 53% [Mesquida2023].
5. **Separate the evidence types:**
   - acute signalling (MPS, hormones, EMG);
   - measurement validation;
   - longitudinal training outcomes.

   Only the last one answers "does it build muscle or strength?" (SHARED-STANDARDS §4).

---

## 1. The funnel at a glance

| stage | what happens | what you record | file (per topic) |
|---|---|---|---|
| 1 Question | PICOS, outcomes, minimum duration, thresholds | protocol card | `protocol.md` |
| 2 Search | ≥3 sources plus citation chasing, with exact strings | string, source, date, hit count | `searches.csv` |
| 3 Deduplicate and auto-filter | DOI/PMID/title match; drop animal-only, wrong publication type and retracted records | one row per unique record | `records.csv` |
| 4 Title/abstract screen | generous include/exclude | decision and reason code | `records.csv` (screen columns) |
| 5 Full-text eligibility | apply PICOS strictly | decision, reason code and access level | `fulltext.csv` |
| 6 Appraise | RoB 2 / ROBINS-I / AMSTAR 2, TESTEX, integrity checks | per-domain judgement and its support | `rob.csv` |
| 7 Extract | participants, training, diet, outcomes, effects | the field list in §8 | `extraction.csv` |
| 8 Synthesise and grade | pool or narrate; GRADE each outcome | certainty level and the reasons | `grade.csv` and the note |

Files live in `knowledge-base/deep/<topic-slug>/`. When a review is finished:
- the included studies are copied into `STUDIES.csv` (RUN.md §5);
- the verdict goes into the dated note and the library page.

**Budget tiers.** Choose the tier at stage 1 and record it.

- **Tier A, umbrella first** (default when budget is tight).
  1. Find the recent systematic reviews and meta-analyses (last ~5 years).
  2. Appraise them with AMSTAR 2.
  3. Use the best one or two as the backbone.
  4. Run an *update search* from their search end date.
  5. Open the primary trials that drive the conclusion.
- **Tier B, full primary review.** Use it when there's no adequate review (AMSTAR 2 rates them low or critically
  low), the reviews are out of date, or the question is narrower than any review (for example, trained lifters
  only). Run the full funnel.
- In either tier, **the primary studies behind a load-bearing claim are always opened**. A meta-analysis's pooled
  number is only as good as its inputs and the way it pooled them.

---

## 2. Stage 1: the question (PICOS) and eligibility

Write `protocol.md` *before* searching. Changing criteria after seeing results is how reviews get biased.
AMSTAR 2's first critical domain is a protocol registered in advance [Shea2017].

| element | what to decide | default for Kye's library |
|---|---|---|
| **P**opulation | trained or untrained; age; sex; health | healthy adults aged 18–50. Report trained (≥1 year of consistent RT) separately. Include untrained, but flag them as *indirect*. |
| **I**ntervention | exact dose, form, timing, training variable | spell it out (e.g. "creatine monohydrate ≥3 g/d") |
| **C**omparator | placebo, no-supplement, other condition | a placebo or an active control matched on everything except the variable |
| **O**utcomes | primary and secondary, and how measured | see the measurement hierarchy (§2.2) |
| **S**tudy design | which designs count | RCTs (parallel or crossover) for interventions; SR/MA for mapping; cohorts only for things that can't be randomised (e.g. sleep, long-term safety) |
| Duration | minimum intervention length | hypertrophy ≥6 weeks (prefer ≥8); strength ≥4 weeks; acute performance can be single-session |
| Thresholds | what counts as trivial, small, moderate or large | write them down, e.g. lean mass trivial <0.3 kg; 1RM trivial <2% |

*Why thresholds:* GRADE certainty means "how sure are we the true effect is above (or below) a stated threshold".
You can't rate it without saying what the threshold is [Hultcrantz2017].

*Why ≥6–8 weeks for hypertrophy:* in untrained men, the 2.7% CSA rise at week 3 came with oedema-like swelling and
wasn't purely hypertrophy [Damas2016]. The exact cut-off is a judgement, not a law, so record it in the protocol and
don't move it.

### 2.1 Design hierarchy (for interventions)

1. Systematic review and meta-analysis of RCTs. It is a *map*, appraised with AMSTAR 2, and can't be better than
   its trials.
2. RCT with blinding (essential for supplements) and supervised, equated training.
3. RCT, unblinded or unsupervised.
4. Non-randomised controlled trial, or a within-subject unilateral design without randomisation.
5. Cohort or cross-sectional study. It can't establish an effect of the intervention. Use it for exposures, safety
   and associations.
6. Case series, single-arm pre/post designs with no control, narrative reviews, expert opinion. These can generate
   hypotheses only. **Single-arm pre/post studies are excluded from effect estimates.** Any training makes untrained
   people grow, so with no control the change can't be attributed to the intervention.

### 2.2 Outcome measurement quality (hypertrophy and strength)

Hypertrophy methods often disagree, so the measure matters as much as the result [Haun2019].

| rank | hypertrophy measure | notes |
|---|---|---|
| 1 | MRI or CT muscle CSA or volume | reference standard; best if multi-slice volume |
| 2 | Ultrasound muscle thickness or CSA | valid at a single time point. In n=9, the change in MT tracked the change in MRI ACSA (r=0.69) but **not** the change in volume (r=0.33) [Franchi2018]. Operator- and site-dependent: check the same assessor, blinding, and timing after training |
| 3 | Biopsy fibre CSA | direct but samples a tiny fraction of the muscle; high sampling error |
| 4 | DXA lean mass (whole-body or regional) | counts water and glycogen as "lean". Glycogen loading raised DXA lean mass 2–3% in trained cyclists with no tissue gain [Bone2017]. Needs a standardised protocol (fasted, rested, hydrated, same scanner) [Nana2015] |
| 5 | BIA or BIS, air displacement, hydrostatic weighing | hydration-sensitive; whole-body only |
| 6 | Skinfolds, circumferences, body mass | not a hypertrophy measure; record it, don't use it for a muscle verdict |

**Strength:**
- 1RM in the trained lift (most relevant to Kye);
- 1RM in an untrained lift, or isometric or isokinetic torque (measures transfer, not the trained skill);
- reps to failure at a fixed load (an endurance measure; motivation-sensitive).

Check for familiarisation sessions and blinded testers. Without familiarisation, early "gains" are partly learning
(our judgement). Express every measure against its typical error or minimal detectable change where reported
[Hopkins2000].

---

## 3. Stage 2: searching

### 3.1 Sources (what this environment can reach)

The ideal minimum is Embase + MEDLINE + Web of Science + Google Scholar. That combination gave 98.3% recall, and 16%
of included references appeared in only one database [Bramer2017]. **We can't reach Embase, Web of Science,
SPORTDiscus or Google Scholar.** Say so in every note's limitations, and compensate:

| source | role | how |
|---|---|---|
| **PubMed** (E-utilities) | primary, with MeSH | `esearch.fcgi?db=pubmed&term=...&retmax=500&retmode=json`, then `efetch` for abstracts |
| **Europe PMC** REST | primary, adds preprints, PMC full text and agricultural/other sources | `search?query=...&format=json&pageSize=1000&resultType=core`; preprints with `SRC:PPR`; dates with `FIRST_PDATE:[2025-01-01 TO 2026-12-31]`; full text with `/{PMCID}/fullTextXML` |
| **OpenAlex** | broad coverage; citation chasing | `works?filter=cites:W...` (forward) and `referenced_works` (backward). **Note:** the free daily budget per IP can run out (it did on 2026-11-15). If it does, use Semantic Scholar or Europe PMC instead |
| **Semantic Scholar** | citation chasing | `graph/v1/paper/DOI:<doi>/citations` and `/references` |
| **Europe PMC citations** | citation chasing | `/MED/<pmid>/citations` and `/MED/<pmid>/references` |
| **Crossref** | DOI check, metadata, **retraction check** | `works/<doi>`, then read `updated-by` |
| WebSearch | trial registries (ClinicalTrials.gov, ANZCTR), SportRxiv, theses | targeted searches only |

All of the calls above were tested working on 2026-11-15.

### 3.2 Building the string

Use concept blocks combined with AND. Within each block, OR together a **controlled term (MeSH)** and **free-text
synonyms**. Truncate with `*` and use phrase quotes. Check the string with the PRESS elements before running it
[McGowan2016]:
- translation of the question;
- Boolean and proximity operators;
- subject headings;
- text words;
- spelling, syntax and line numbers;
- limits and filters.

Example (PubMed, creatine and resistance training, RCTs; 477 hits on 2026-11-15):

```
creatine[tiab]
AND ("Resistance Training"[MeSH] OR "resistance training"[tiab] OR "strength training"[tiab]
     OR "weight training"[tiab] OR "weight lifting"[tiab] OR "resistance exercise"[tiab])
AND (randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomized[tiab] OR placebo[tiab]
     OR drug therapy[sh] OR randomly[tiab] OR trial[tiab] OR groups[tiab])
NOT (animals[mh] NOT humans[mh])
```

The last two lines are the **Cochrane highly sensitive search strategy** for RCTs (sensitivity-maximising PubMed
version) [Higgins2024, ch. 4].
- Use it for primary-trial searches.
- For reviews, swap in
  `(systematic review[pt] OR meta-analysis[pt] OR "systematic review"[tiab] OR "meta-analy*"[tiab])`.
- Don't add an outcome block unless the hit count is unmanageable (more than ~3,000). Outcome terms are reported
  inconsistently in abstracts, so an outcome block costs recall.

Useful MeSH: `Resistance Training`, `Muscle Strength`, `Muscle, Skeletal/growth & development`, `Hypertrophy`,
`Body Composition`, `Dietary Supplements`, `Dietary Proteins`, `Athletes`, `Sports Nutritional Physiological
Phenomena`. Look up the exact heading with `esearch.fcgi?db=mesh&term=...` before relying on it.

Europe PMC equivalent:
`TITLE_ABS:"creatine" AND (TITLE_ABS:"resistance training" OR TITLE_ABS:"strength training") AND PUB_TYPE:"randomized controlled trial"`.
Also run it once without the PUB_TYPE filter, because PUB_TYPE indexing is incomplete.

### 3.3 Citation chasing (mandatory)

1. **Backward:** the reference lists of every included trial and every relevant review.
2. **Forward:** "cited by" for the key trials and the best review, to catch newer trials.
3. Repeat once on anything new that turns up.

*Why:* in one audit of a complex-evidence review, 51% of sources came from snowballing and only 30% from the
protocol searches [Greenhalgh2005]. That figure comes from complex service research, so expect less here, but our
database gap makes chasing more important, not less. Tools: [Haddaway2022], or the APIs in §3.1.

### 3.4 Grey literature, preprints, language

- **Grey literature and registries.** Search ClinicalTrials.gov or ANZCTR (via WebSearch) for registered,
  unpublished trials on the intervention. Published trials averaged a 9% larger effect than grey ones (ratio of
  odds ratios 1.09, 95% CI 1.03–1.16) [Hopewell2007].
  - A registered trial that finished years ago with no results is evidence of possible publication bias. Note it
    in the GRADE row.
- **Preprints** (Europe PMC `SRC:PPR`, SportRxiv). Include them, flag `preprint=yes`, and check whether a published
  version exists (dedupe to the published one). Run a sensitivity check without preprints. A conclusion must never
  rest on a preprint alone.
- **Conference abstracts and theses.** Record them. Use them only if they give enough data, and flag them as high
  risk of bias for reporting.
- **Language.** English-only is acceptable. Restricting to English showed no systematic bias in conventional
  medicine [Morrison2012]. Record how many non-English records were dropped.

### 3.5 Logging (PRISMA-S)

Every search gets a row in `searches.csv`:

`search_id,date,source,exact_string,filters,hits,new_after_dedup,notes`

That covers PRISMA-S's core items: database, interface, full string, limits, date and count [Rethlefsen2021].

---

## 4. Stages 3–4: handling thousands of records

### 4.1 Deduplicate, then auto-filter

Deduplicate in order:
1. DOI, lower-cased;
2. PMID;
3. normalised title (lower-case, strip punctuation) + year + first-author surname.

Staged matching like this catches what a single key misses [Bramer2016]. Keep the merged IDs in `records.csv`.

Then apply automated filters. Each one is a reason code, never a silent drop:
- animal-only (`NOT (animals[mh] NOT humans[mh])`);
- publication type is editorial, comment, letter or erratum;
- non-English (record the count);
- before the protocol's date floor, if one is set;
- **retracted.** For every DOI, call `api.crossref.org/works/<doi>` and check `updated-by` for `type: retraction`.
  Crossref now carries the Retraction Watch data [RetractionWatchCrossref]. PubMed's `"Retracted
  Publication"[pt]` is a backup.
  - **Retracted means excluded. Expressions of concern and corrections are flagged and read.**

### 4.2 Title/abstract screening

- **Be generous.** Include whenever unsure. This stage only removes the obviously irrelevant.
- An AI worker screens as a **single reviewer**. Single screening misses about 13% of relevant studies (sensitivity
  86.6%) against 3% for dual screening [Gartlehner2020]; the median across evaluations is 5% [Waffenschmidt2019].
  So compensate:
  1. **Verification pass.** In a *separate session or agent*, re-screen every "maybe" plus a random 10% of excludes
     (seeded, with the seed recorded). If the second pass rescues even one eligible study, re-screen all the
     excludes from that batch.
  2. **Citation chasing** (§3.3) is the second safety net.
  3. Record `screened_by` and `verified_by` so the method is honest.
- Work in batches of about 200 records, with the decision written to the CSV after each batch, so a session can end
  at any point.
- Screen in this order: title, then abstract if the title is unclear, then full text if the abstract is unclear.

### 4.3 Exclusion reason codes (use exactly these)

| code | reason |
|---|---|
| E01 | Not human / in vitro / animal |
| E02 | Wrong population (e.g. clinical disease, older than protocol range, children) |
| E03 | Wrong intervention or exposure |
| E04 | Wrong or no comparator; single-arm pre/post |
| E05 | Wrong outcome, or outcome not measured by an eligible method |
| E06 | Wrong design (narrative review, editorial, case report, cross-sectional for a causal question) |
| E07 | Duration below protocol minimum |
| E08 | Duplicate or secondary report of an included study (link it to the primary) |
| E09 | Retracted |
| E10 | Insufficient data to extract and authors' data not obtainable |
| E11 | Full text not accessible (record what was tried; keep it as "awaiting") |
| E12 | Non-English (count only) |
| E13 | Conference abstract or protocol only, with no results |
| E14 | Co-intervention confounds the comparison (e.g. supplement + different training, protein not matched in a non-protein supplement trial) |
| E15 | Predatory or non-peer-reviewed venue with no verifiable methods (see §6.3) |
| E16 | Other (write it out) |

At full text, exactly one primary code per excluded study, plus free text. PRISMA wants the reasons counted
[Page2021], and AMSTAR 2 makes a justified list of excluded studies a critical domain [Shea2017].

---

## 5. Stage 5: full-text eligibility

- Read the methods and results, not only the abstract. Apply the PICOS strictly.
- Check the **trial registration** (registry ID in the paper, or a search of the registry). Compare the
  registered primary outcome, sample size and timepoints with what was published. 62% of trials changed,
  introduced or omitted a primary outcome compared with their protocol [Chan2004]. Record:
  `registered=yes/no/retrospective`, `outcome_switch=yes/no/unclear`.
- Look for multiple reports of one trial (the same n, authors and site) and merge them. A secondary paper that
  reports a "new" outcome from the same participants is not a new study (E08).

---

## 6. Stage 6: appraisal

### 6.1 Which tool when

| study type | tool | output | note |
|---|---|---|---|
| RCT (parallel, crossover, cluster) | **RoB 2** [Sterne2019] | low / some concerns / high, per outcome | judged **per outcome**, not per paper |
| Non-randomised intervention study | **ROBINS-I** [Sterne2016] | low / moderate / serious / critical | "low" means as good as a well-done RCT, which is rare. A V2 (cohort studies) exists; use the current version from riskofbias.info |
| Any exercise-training trial (add-on) | **TESTEX** [Smart2015] | 0–15 | captures exercise-specific reporting that RoB 2 ignores |
| RCT with only a quick score needed | PEDro [Maher2003; Cashin2020] | 0–10 | cross-check only; **never sum scores into a verdict** |
| Systematic review or meta-analysis | **AMSTAR 2** [Shea2017] | high / moderate / low / critically low | not a score; driven by critical flaws |
| Body of evidence per outcome | **GRADE** [Guyatt2008; Balshem2011] | high / moderate / low / very low | see §9 |

**RoB 2 domains** (each scored low / some concerns / high via signalling questions; check the official guidance
before scoring):
1. Bias from the randomisation process (sequence generation, allocation concealment, baseline imbalance).
2. Bias from deviations from intended interventions (blinding of participants and personnel, adherence,
   co-interventions).
3. Bias from missing outcome data (dropouts, especially if they differ by group or by reason).
4. Bias in measurement of the outcome (blinded assessor; could knowing the allocation change the measurement?).
5. Bias in selection of the reported result (a pre-specified analysis plan; multiple measures or analyses to choose
   from).

**Overall:** high if any domain is high, or several are "some concerns"; low only if every domain is low.

**ROBINS-I domains** [Sterne2016]:
1. confounding;
2. selection of participants;
3. classification of interventions;
4. deviations from intended interventions;
5. missing data;
6. measurement of outcomes;
7. selection of the reported result.

**TESTEX items** [Smart2015]:
- 1 eligibility specified;
- 2 randomisation specified;
- 3 allocation concealed;
- 4 groups similar at baseline;
- 5 assessor blinded;
- 6 outcomes assessed in ≥85% of participants (up to 3 points; covers adherence, adverse events and attendance);
- 7 intention-to-treat;
- 8 between-group comparisons (2 points);
- 9 point estimates and variability;
- 10 activity monitoring in the control group;
- 11 relative intensity kept constant (progressed);
- 12 exercise volume and energy expenditure reported.

Items 1–5 (1 point each) are the 5 quality points and items 6–12 are the 10 reporting points. The exact sub-point
wording should be checked against the paper (SECONDARY for the sub-points).

**AMSTAR 2 critical domains** (confirmed in full text) [Shea2017]:
- item 2: protocol registered in advance;
- item 4: adequate search;
- item 7: excluded studies listed with justification;
- item 9: risk of bias of the included studies assessed;
- item 11: appropriate meta-analytic methods;
- item 13: risk of bias considered when interpreting the results;
- item 15: publication bias assessed.

The ratings:
- **high:** no critical flaw and at most one non-critical weakness;
- **moderate:** more than one non-critical weakness, no critical flaw;
- **low:** one critical flaw;
- **critically low:** more than one critical flaw. Don't rely on it.

Sport-science meta-analyses also need these checks:
- whether they pooled change scores from studies of untrained and trained people as one population;
- double-counted a shared control group;
- mixed MRI and skinfold "hypertrophy";
- used one-tailed or MBI-based inputs.

### 6.2 Per-study risk-of-bias checklist (one row per study per outcome in `rob.csv`)

Columns: `study_key,outcome,tool,D1_randomisation,D2_deviations,D3_missing,D4_measurement,D5_reporting,overall,testex_score,support_text,flags`

Fill `flags` with every code that applies:

| flag | check | why |
|---|---|---|
| F-REG | Not registered, or registered retrospectively | outcome switching is common [Chan2004] |
| F-SWITCH | Primary outcome differs from the registry or protocol | [Chan2004] |
| F-BLIND | Supplement trial not double-blind or placebo not matched; no blinding check | unblinded trials exaggerate subjective outcomes (ROR 0.75) [Wood2008]. Non-blinded assessors inflated effects by 36% [Hrobjartsson2012]. Treat 1RM and reps-to-failure as **effort-dependent, so partly subjective** (our judgement) |
| F-ASSESS | Outcome assessor (ultrasound, DXA, 1RM tester) not blinded | [Hrobjartsson2012] |
| F-SMALLN | n<20 in total, or <10 per group, with no a priori power calculation | median n in J Sports Sci was 19 [Abt2020]; MBI papers had a median of 10 per group [Lohse2020]; average power about 53% [Mesquida2023]. Small studies that reach significance overestimate effects [Ioannidis2005] |
| F-NOCTRL | No control group, or a control that doesn't train | §2.1 |
| F-UNTRAINED | Untrained, elderly or clinical sample used to make a claim about trained lifters | GRADE indirectness [Guyatt2011f]. Beginners respond to almost any stimulus |
| F-DIET | Energy or protein intake not recorded, or not compared between groups | §7.2 |
| F-DRUGS | Trained-lifter sample with no stated screening for anabolic drug use | §7.2 |
| F-SUPERV | Training not supervised, or adherence not reported | TESTEX 6, 11 |
| F-EQUATE | Groups differ in volume, effort or proximity to failure beyond the variable under test | the comparison is confounded |
| F-SHORT | Below the protocol duration, or a hypertrophy measure taken in the swelling window | [Damas2016] |
| F-TIMING | Measurement timing not standardised (DXA after a carb load or creatine loading; ultrasound within ~48–72 h of a hard session, our judgement; no fasting or hydration control) | [Bone2017; Nana2015] |
| F-MULTI | Many outcomes or timepoints with no named primary outcome and no correction | MBI papers had a median of 30 tests and 14% named a primary outcome [Lohse2020] |
| F-MBI | Inference rests on magnitude-based inference ("likely beneficial") | Type I error of 12–22% for "likely" at n=8–15 per group [Lohse2020; Sainani2018; Sainani2019; Welsh2015]. **Re-read the result from the reported CI or SD. If none is given, treat it as unreported** |
| F-SPIN | Conclusion claims benefit where the primary outcome was not significant, or leans on secondary or within-group results | [Boutron2010] |
| F-WITHIN | Claims a group difference from "significant in A, not in B" without a between-group test | a standard error (TESTEX 8) |
| F-COI | Industry funding, or author ties to the product | industry-sponsored studies had favourable efficacy results more often (RR 1.27, 1.17–1.37) [Lundh2017]. Flag it; it doesn't exclude a study on its own |
| F-INTEGRITY | Fails the GRIM, statcheck or baseline check (§6.3) | [Brown2017; Nuijten2016; Carlisle2017] |
| F-FRAGILE | Dichotomous outcome with a fragility index of ≤3, or a continuous result whose CI just clears zero with small n | [Walsh2014] |
| F-PRED | Venue looks predatory | [Grudniewicz2019] |
| F-PREPRINT | Not peer-reviewed | §3.4 |
| F-RETRACT / F-EOC | Retracted (exclude) / expression of concern (flag) | §4.1 |

### 6.3 Integrity checks (fast, run on every included study)

1. **Retraction.** Crossref `updated-by` (§4.1). Also look for corrections; a correction can change the numbers.
2. **GRIM** [Brown2017]. For a mean of integer data (rep counts, Likert items, RPE) with n<100, check that
   mean × n is within rounding of a whole number.
   - Python: `import math; ok = any(round(T/n, d) == m for T in (math.floor(m*n), math.ceil(m*n)))`, where d is the
     number of decimals reported. `ok == False` means the mean is impossible for that n.
   - A failure isn't proof of fraud, but email-level doubt goes in the flags.
   - SPRITE can test whether the mean and SD are possible together [Heathers2018]; it's a preprint method, so use
     it only as a supporting check.
3. **Statistics recompute** [Nuijten2016]. Where t, F and df are reported, recompute p (`scipy.stats`). Check that
   the reported SDs, SEs and CIs agree with each other. SE mislabelled as SD is common, and it makes effects look
   three to four times bigger.
4. **Baseline plausibility** [Carlisle2017]. In randomised groups, baseline differences that are implausibly
   *small* across many variables, or huge, are a warning.
5. **Impossible effects.** A lean-mass gain above ~1 kg per month in trained natural lifters, a supplement that
   beats the training effect, or a d above 1.5 for a supplement should all trigger a closer look at the methods,
   SD/SE and units. These numbers are our judgement, not cited.
6. **Predatory venue** [Grudniewicz2019]. Check that the journal is in PubMed/MEDLINE or DOAJ, has an identifiable
   editor and peer review, and isn't on a known-hijack list. A paper outside MEDLINE that can't be verified gets
   E15 or F-PRED.
7. **Funding and COI.** Read the funding and disclosure statements. In supplement research, note whether the
   product was donated, whether the company funded the study, and whether authors consult for it.

---

## 7. Sports-science pitfalls, and participant factors

### 7.1 The pitfalls in one place (each is a flag in §6.2)

- **Tiny samples.** n<20 is the norm, not the exception. Small significant studies overstate effects, and an
  "n.s." result in a small study is not evidence of no effect (SHARED-STANDARDS §6).
- **No control group or a non-training control.** Training effects swamp supplement effects.
- **The untrained-to-trained leap.** Downgrade for indirectness [Guyatt2011f]. Report trained-only estimates
  separately whenever they exist.
- **Non-blinded supplement trials.** Expectation effects; effort-dependent outcomes.
- **No dietary control.** Unequal protein or energy intake confounds any body-composition result.
- **Uncontrolled drug use.** In advanced-lifter samples, undeclared anabolic use is plausible, and few trials test
  for it.
- **Adherence and supervision.** Unsupervised training and unchecked supplement intake (no capsule counts) dilute
  effects and hide non-compliance.
- **Training not equated.** Volume or effort differs between arms.
- **Short durations; measurement timing and swelling.**
- **Magnitude-based inference** (see F-MBI).
- **Multiple outcomes and selective emphasis.**
- **Responder claims.** "Some people respond and some don't", read from individual pre/post changes, is mostly
  measurement error and random variation. True individual differences are only shown when the **SD of change in
  the intervention arm is larger than in the control arm** [Atkinson2015; Hecksteden2015]. Without a control arm, a
  responder/non-responder claim is unsupported.

### 7.2 Participant factors: what to extract, and what you can honestly conclude

Extract these for every study, at the group level (mean ± SD per arm), with `NR` when not reported:

| factor | fields |
|---|---|
| Demographics | age, sex (n male / n female), body mass, height, BMI, body fat % (with method) |
| Training status | definition used, years of training, current frequency, baseline 1RM (absolute and relative to body mass), "trained" verified or self-reported |
| Habitual diet | energy (kcal/d), protein (g/kg/d), carbohydrate (g/kg/d), assessment method (weighed record, recall, FFQ, app) |
| Diet control level | **4** all food provided · **3** prescribed and recorded, adherence checked · **2** recorded only · **1** not recorded. Also: were energy and protein *matched* between arms? |
| Supplement use | habitual creatine, protein or caffeine use; washout required? |
| Drug use | screened or tested for anabolic agents? excluded? not stated? |
| Sleep | duration or quality, if reported (rare) |
| Health | exclusions; medications |
| Genetics / responders | genotype if measured; SD of change in each arm (for the responder test above) |

**What these can and can't support. Be honest about it in every note.**

- **Only what's reported is usable.** Many trials report no diet data, no training age, no drug screening. Missing
  is missing; don't assume it was controlled.
- **Person-level questions need individual participant data (IPD).** "Does creatine work better in vegetarians?" or
  "does age moderate the protein effect?" can only be answered properly with each person's data. Study means can
  hide a real interaction, and can show a spurious one. One worked example found a patient-level effect modifier
  that group-level meta-regression missed [Berlin2002; Riley2010]. We almost never have IPD, so person-level
  moderation claims are **hypotheses, not findings**.
- **Meta-regression can test study-level moderators.** Examples: mean protein intake, mean age, training status as
  a study-level category, duration, dose.
  - It is **observational**, even when the trials inside it are randomised [Thompson2002].
  - It needs enough studies. The Cochrane Handbook's usual guidance is ~10 studies per covariate [Higgins2024,
    SECONDARY].
  - Using study averages of participant characteristics risks the **ecological fallacy**: "trials with older
    samples showed smaller effects" doesn't mean older individuals respond less [Thompson2002; Berlin2002].
  - Pre-specify the moderators in `protocol.md`; data-dredged moderators are p-hacking [Head2015; Simmons2011].
- **Subgroups within a trial.** Believe them only if pre-specified, tested by interaction (not "significant in men,
  not in women"), and plausible.
- **Applying a result to Kye** (87 kg, about 13.6% body fat, trained, high volume, adequate protein). The closest
  evidence is trained, young, male, protein-replete samples. If the evidence comes only from untrained, older or
  protein-deficient people, say so plainly and downgrade for indirectness.

---

## 8. Stage 7: extraction field list (`extraction.csv`)

One row per study arm per outcome per timepoint (long format). Columns:

```
study_key, doi, pmid, registration_id, registered(yes/no/retro), outcome_switch(yes/no/unclear),
design(parallel/crossover/unilateral/cohort), randomised(yes/no), blinding(none/single/double/assessor),
funding, coi(text), country, setting,
arm, n_randomised, n_analysed, dropouts_reason,
age_mean, age_sd, n_male, n_female, body_mass_mean, body_mass_sd, height_mean, bmi_mean, bodyfat_pct_mean, bodyfat_method,
trained_definition, training_years_mean, baseline_1rm_lift, baseline_1rm_mean, baseline_1rm_sd,
energy_kcal_mean, protein_gkg_mean, carb_gkg_mean, diet_assessment_method, diet_control_level(1-4), energy_protein_matched(yes/no/NR),
other_supplements, drug_screening(tested/excluded_self_report/NR), sleep(NR or value), health_exclusions,
intervention_detail(dose/form/timing), comparator_detail, adherence_method, adherence_pct,
training_supervised(yes/partial/no), training_program(CERT: exercises, sets x reps, load, proximity to failure, frequency, weeks, progression),
volume_equated(yes/no), effort_equated(yes/no),
outcome, outcome_method, measurement_timing_standardised(yes/no/NR), assessor_blinded(yes/no/NR),
timepoint_weeks, baseline_mean, baseline_sd, post_mean, post_sd, change_mean, change_sd, sd_or_se_as_reported,
between_group_effect, effect_metric(MD/SMD/%), ci_low, ci_high, p_value, primary_outcome(yes/no),
stats_method(NHST/Bayesian/MBI), access(FULL/ABSTRACT/SECONDARY), extracted_by, checked_by, notes
```

- Training-programme description follows CERT and TIDieR [Slade2016; Hoffmann2014].
- Prefer the **between-group** difference in change, with its CI.
- Record whether a dispersion is SD or SE, as reported.
- If only figures are available, digitise the plot and flag `digitised` in notes.

---

## 9. Stage 8: synthesis and the GRADE verdict

### 9.1 Pooling

- **Pool** only studies that are similar enough in population, intervention, comparator and outcome method. Use a
  random-effects model.
  - Report the pooled MD (natural units, e.g. kg lean mass, kg 1RM) or the SMD, with the 95% CI.
  - Report I² [Higgins2003] and a **95% prediction interval** [IntHout2016]. The prediction interval is the range
    Kye could actually expect.
  - Run the analysis with and without high-risk-of-bias studies.
- Don't mix measurement methods in one pool (e.g. MRI with skinfold). Pool by method, or use the best method only.
- **Crossover and unilateral designs** need correct paired SEs. If they can't be computed, narrate instead.
- **Small-study effects.** A funnel plot and Egger's test [Egger1997] only with ≥10 studies [Sterne2011]. Asymmetry
  ≠ proof of publication bias, because small studies can differ for real reasons. Trim-and-fill is a sensitivity
  analysis at most [Duval2000].
  - Combine it with the registry check (§3.4): finished-but-unpublished trials are stronger evidence than a funnel.
- If pooling isn't sensible, **narrate by direction and size**, grouped by risk of bias. Don't vote-count
  significant versus non-significant.

### 9.2 GRADE, per outcome (`grade.csv`)

Columns: `outcome,n_studies,n_participants,design_start,rob,inconsistency,indirectness,imprecision,pub_bias,upgrades,certainty,effect_summary,threshold_used,plain_statement`

**Start:** RCTs start at **high**, observational studies at **low** [Balshem2011].

**Downgrade one level (two if very serious) for:**

1. **Risk of bias.** Most of the evidence weight comes from studies rated high or "some concerns" [Guyatt2011b].
2. **Inconsistency.** Effects point in different directions, CIs barely overlap, the prediction interval crosses
   the threshold, or I² is high and unexplained [Guyatt2011e].
3. **Indirectness.** Untrained, older, clinical or protein-deficient populations; a surrogate outcome (MPS, DXA
   lean mass with water shifts) used for a real one (muscle tissue, 1RM) [Guyatt2011f].
4. **Imprecision.** The CI crosses the stated threshold (trivial versus meaningful), or the total sample is small
   (roughly n<400 for a continuous outcome, a rule of thumb from GRADE's optimal-information-size guidance;
   SECONDARY, not re-read) [Guyatt2011d].
5. **Publication bias.** Asymmetry with ≥10 studies, unpublished registered trials, all small industry-funded
   positives [Guyatt2011c].

**Upgrade** (observational evidence only, rarely): large effect, dose–response, or plausible confounding that would
shrink the effect.

**Mapping to the library's confidence words, and the wording to use** [Santesso2020]:

| GRADE | library confidence | how to phrase it for Kye |
|---|---|---|
| High | Strong | "X increases/reduces Y" |
| Moderate | Moderate | "X probably / likely increases Y" |
| Low | Limited | "X may increase Y" |
| Very low | Very limited | "We don't know whether X affects Y" |

**Each verdict states:**
- the size of the effect in real units, with its CI, against the threshold;
- the certainty;
- the biggest reason it isn't higher;
- whether the evidence includes trained lifters.

"No significant effect" is never written as "doesn't work" unless the CI excludes a meaningful effect.

---

## 10. Working across sessions (files and resume rules)

```
knowledge-base/deep/<topic-slug>/
  protocol.md      PICOS, thresholds, tier, moderators, date floor - frozen once searching starts (changes logged with date and reason)
  searches.csv     search_id,date,source,exact_string,filters,hits,new_after_dedup,notes
  records.csv      record_id,doi,pmid,title,year,first_author,source_ids,dup_of,auto_filter_code,
                   ta_decision(include/exclude/maybe),ta_reason,screened_by,verified_by,session_date
  fulltext.csv     record_id,study_key,access,decision,reason_code,reason_text,registration_id,linked_reports
  rob.csv          (section 6.2)
  extraction.csv   (section 8)
  grade.csv        (section 9.2)
  progress.md      one line per session: date, stage reached, last record_id screened, what is next
```

**Resume rules:**
1. Read `progress.md` first.
2. Never re-screen a record that already has a decision, except in the verification pass.
3. Write to the CSVs after every batch, never only at the end.
4. Quote every CSV field (`csv.QUOTE_ALL`).
5. `record_id` = `S<search_id>-<n>`, never reused.
6. On finishing:
   - copy the included studies into `knowledge-base/STUDIES.csv` in RUN.md's columns;
   - put the PRISMA counts (identified → deduplicated → screened → full-text assessed → included, with excluded
     counts by code) in the dated note;
   - record the verdict in TOPICS.md and the library.

**Minimum PRISMA flow numbers for every note:** records per source; after deduplication; excluded by auto-filter
(by code); title/abstract excluded; full texts sought; not retrieved; full-text excluded (by code); included
(studies and reports).

---

## 11. What this protocol can't do (state it in every note)

- There's **no access to Embase, Web of Science, SPORTDiscus or Google Scholar**, so expect lower recall than a
  formal review [Bramer2017].
- There's **single-reviewer screening** with a verification sample, not true dual screening [Gartlehner2020].
- Some sources are paywalled; their access is ABSTRACT, and they can't carry a verdict alone.
- Tool descriptions here (RoB 2 domains, PEDro items) were written partly from established knowledge, not re-read
  this session; see each source's `access` and `verification` columns. Check the official guidance when a
  judgement is borderline.
- Individual-level conclusions (Kye's genetics, his exact response) are outside what aggregate trial data can
  support.

**Background reading** (in the CSV, not cited above):
- reporting standards for trials [Schulz2010; Hopewell2025];
- the GRADE series introduction [Guyatt2011a];
- sport-science research quality [Halperin2018; Caldwell2020; Mesquida2022];
- screening software [Ouzzani2016].
