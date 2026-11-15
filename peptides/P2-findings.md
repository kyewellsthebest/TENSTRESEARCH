# P2 — Growth-hormone and gonadal-axis peptides (plus MK-677): findings

Agent P2. Searched 2026-11-04. Rules followed: `BRIEF.md` and `../agent-notes/SHARED-STANDARDS.md`.
No dosing, cycling, reconstitution, injection or sourcing information is given for any unapproved
substance. For approved drugs a trial dose is mentioned only where it is needed to read a result.

**Access in this session.** WebSearch worked. WebFetch on `pmc.ncbi.nlm.nih.gov` failed with
`ENOTFOUND`, meaning the host is not on this session's network allow-list, so **no full text was
read**. Every source here is ABSTRACT (an abstract, a registry entry or a label excerpt returned by
search) or SECONDARY (news, a review or a commercial page that describes the study). Anything I
could not confirm is marked **UNVERIFIED**. To open the PMC full texts named below,
`pmc.ncbi.nlm.nih.gov` has to be allowed in the session's network settings.

## 10-line summary

1. Growth hormone itself is the best-studied substance here and the clearest negative result. In healthy older adults and in fit young adults it adds about 2 kg of lean mass and takes off about 2 kg of fat (lean mass includes water). **It does not increase strength or endurance**, except for one sprint result in one trial.
2. Its side effects are frequent and well characterised: oedema, joint pain, carpal tunnel syndrome, gynaecomastia, and impaired glucose tolerance or diabetes.
3. Tesamorelin is the only GH-axis peptide with a phase-3 programme and an FDA approval (2010). Its proven benefit is about 15% less **visceral** fat at 26 weeks, in people with HIV lipodystrophy (806 people across two phase-3 trials). One 60-person RCT shows a similar result in abdominally obese people without HIV. Nothing shows a gain in muscle or strength in healthy people.
4. MK-677 (ibutamoren, a non-peptide) raised fat-free mass by about 1.1 kg against a 0.5 kg loss on placebo in 65 healthy older adults. **Strength and function did not improve**, fasting glucose rose and insulin sensitivity fell. A trial in hip-fracture patients was stopped early over congestive heart failure.
5. For CJC-1295 the human data are phase-1 hormone-level data only (two small RCTs). Its one phase-2 trial, in HIV patients, was **halted in 2006 after a participant died**. Whether the drug caused the death was never established in any source I could reach.
6. Ipamorelin's only efficacy RCT (n=114, postoperative ileus, sponsored by the company developing it) was negative. There is **no** human body-composition trial of ipamorelin, GHRP-2, GHRP-6 or hexarelin. GHRP-2 and hexarelin also raise cortisol, ACTH and prolactin, and GHRP-6 strongly increases appetite.
7. Sermorelin: small trials in older adults show lean-mass gains in men only. Its US brand (Geref) left the market in 2008.
8. IGF-1: a 1-year RCT of recombinant IGF-1 in older women (n=16) was stopped early because **no outcome moved**. There are **no human data at all** for IGF-1 LR3, MGF or PEG-MGF, and follistatin has been tested in humans only as gene therapy (n=6, muscular dystrophy).
9. hCG, gonadorelin and kisspeptin act on the gonadal axis. hCG has an RCT showing it preserves testicular testosterone during testosterone use (n=29). None of the three has any trial showing a muscle or fat benefit in healthy people, and the FDA has said hCG does nothing for weight loss.
10. Every substance here is banned in sport at all times (WADA S2; follistatin under S4). The GH-axis peptides and MK-677 are Schedule 4 plus Appendix D in Australia. Grey-market testing finds wrong or missing active ingredients, and the epidemiology linking higher IGF-1 to breast, colorectal and prostate cancer is the main unknown hanging over long-term use.

## Evidence levels used

The brief's hierarchy, from strongest to weakest: **RCT** (human randomised controlled trial),
**NRS** (human non-randomised study), **CR** (human case report), **ANIMAL**, **INVITRO**, and **ANEC**
(anecdote or marketing). Strength is rated strong, moderate, limited, very limited or none.

## Cross-cutting findings

### Peptide-clinic and vendor conflicts of interest

Most results for every query except tesamorelin and GH were commercial. They came from peptide
vendors, telehealth "peptide clinics", compounding-pharmacy marketers, and many look-alike
"guide" and "tracker" sites on `pages.dev` and `vercel.app` domains. Several of these pages:
- give study numbers that contradict the abstracts. Nass 2008 is quoted as both "+1.6 kg" and
  "+1.1 kg", and the abstract says +1.1 kg against −0.5 kg, so 1.6 kg is the between-group difference.
- cite trials that cannot be found (a "Johns Hopkins 87-person sermorelin trial"; a "2014 negative
  human MGF RCT").
- disagree on regulatory status. The FDA 503A categories for CJC-1295, ipamorelin and GHRP-6 are
  reported differently from one site to the next.

None of these pages was used as evidence for an outcome. The industry sponsors of the trials that
do exist are flagged per substance below.

### IGF-1 axis and cancer

This applies to everything here whose purpose is to raise GH or IGF-1.
- **Breast cancer** (UK Biobank, about 206,000 women): HR 1.11 per 5 nmol/L of IGF-1
  observationally; Mendelian-randomisation OR 1.05 (1.01–1.10). The authors judge the link probably
  causal. [NRS + MR, moderate, Murphy2020breast, ABSTRACT]
- **Colorectal cancer** (UK Biobank, 397,380 people; MR with 52,865 cases): OR 1.08 (1.03–1.12)
  per SD of genetically predicted IGF-1. [NRS + MR, moderate, Murphy2020crc, ABSTRACT]
- **Prostate cancer** (pooled analysis of 20 prospective studies plus MR): OR 1.09 (1.07–1.11) per
  SD observationally; aggressive disease 1.09 (1.03–1.16); colocalisation PP4 99%. The MR estimate
  was truncated in what I saw. [NRS + MR, moderate, Watts2023, ABSTRACT]
- **Treated patients** (SAGhE, 23,984 people treated with GH in childhood, follow-up independent of
  industry): no clear rise in cancer in otherwise-healthy short children. Bone and bladder cancer
  incidence was raised, Hodgkin lymphoma rose with follow-up, and **cancer mortality rose with
  daily dose in people treated after a previous cancer**. [NRS, moderate, Swerdlow2017, ABSTRACT]
- **Mecasermin** (approved IGF-1): its EU and Australian labels warn of benign and malignant
  neoplasia, and a December 2019 safety letter says to stop it permanently if a neoplasm appears.
  [regulatory, Increlex-DHPC2019, SECONDARY]

What this means: raising IGF-1 for years in healthy people **has never been studied for cancer
outcomes**. The epidemiology links higher IGF-1 within the normal range to modestly higher cancer
risk. Neither line of evidence proves harm from secretagogues, and neither rules it out. This is
the main unknown for every substance in this file.

### Grey-market quality

- Cologne anti-doping lab, 21 products sold as GH: **only 5 contained hGH**. The rest contained
  CJC-1295 (5), GHRP-6 (3), melanotan-II (3), sermorelin, ipamorelin and AOD-9604 (1 each).
  [Krug poster, SECONDARY/ABSTRACT]
- The same group has analysed 185 black-market or confiscated products since 2010. Its findings
  include **unpurified long-R3-IGF-1**, "GHRP-2" sold inside nutritional supplements, and
  undeclared glycine-extended analogues (Gly-GHRP-6, Gly-GHRP-2, Gly-ipamorelin) found in
  Germany, Norway and Poland. These analogues have never been tested in humans in any form.
  [Krug2018, ABSTRACT]
- A 2026 **preprint** (not peer reviewed) analysed 6,441 consumer- and vendor-submitted test
  results. It reports 22 CJC-1295, 6 ipamorelin and 11 tesamorelin samples with **no stated peptide
  present**, and a quality issue in about 15% of samples. The data are self-selected submissions.
  [Preprint2026, ABSTRACT]
- Certificates of analysis supplied by vendors (">99% HPLC") are not independent evidence. One I
  saw contradicted itself about its own method.

### Regulatory snapshot

**WADA, 2026 list.** All of these are prohibited at all times and are non-specified substances:
- S2.2.4: GHRH analogues (CJC-1295, sermorelin, tesamorelin), GH secretagogues (ibutamoren), and
  GHRPs (GHRP-2/pralmorelin, examorelin/hexarelin and others).
- S2.2.1, in males: hCG, LH, GnRH (gonadorelin), and kisspeptin with its agonist analogues.
- S2.3: IGF-1 and its analogues, and MGFs.
- S4: follistatin, as an agent preventing activin receptor IIB activation. I confirmed this on the
  2019–2021 lists; check the 2026 text.

**TGA, Australia.** The TGA lists GHRHs, GHRPs, GHSs, CJC-1295, GHRP-2, GHRP-6, hexarelin and
ipamorelin as **Schedule 4 and Appendix D Part 5** (an ACMS recommendation from 2015). Ibutamoren
is captured by the GHS entry, and a dedicated entry has been recommended. [TGA FOI docs, ABSTRACT]
I did not verify the scheduling of the other substances; the scores file says which.

**FDA 503A compounding categories.**
- **Ibutamoren mesylate and kisspeptin-10** are Category 2 ("significant safety risks") on the FDA
  page updated 22 Apr 2026. PCAC voted against adding both to the bulks list.
- **CJC-1295** was removed from Category 2 because its nominators withdrew; the FDA is evaluating
  it on its own initiative.
- **Ipamorelin**: an FDA evaluation document cites "significant safety concerns".
- **PEG-MGF** was among the 12 peptides taken off Category 2 on 15 Apr 2026, for PCAC review in
  July 2026. That puts it in pending review, not on Category 1. [SECONDARY]
- **GHRP-6**: the sources conflict (Category 2, or Category 3 per FDA's September 2023 document).

## Per substance

### Recombinant human GH (somatropin) in healthy adults

**Approved** for GH deficiency and other indications; it is not approved for ageing or performance.
- **Healthy elderly, systematic review.** Liu 2007, Ann Intern Med 146:104–15: 31 articles covering
  18 study populations. Fat mass −2.1 kg and lean mass +2.1 kg against control, which the authors
  call "small". No change in bone density. More soft-tissue oedema, arthralgia, carpal tunnel
  syndrome and gynaecomastia, and a trend to more diabetes or impaired fasting glucose. Conclusion:
  "cannot be recommended as an antiaging therapy". [RCT-SR, strong for "no meaningful benefit plus
  real harm", ABSTRACT]
  - Note: the task named this "Liu 2008". The elderly review is **2007**; the 2008 Liu paper is the
    one in athletes.
- **Healthy young athletes, systematic review.** Liu 2008, Ann Intern Med 148:747–58: 27 study
  samples, 303 people given GH (about 440 in all per AHRQ). Lean mass **+2.1 kg (95% CI 1.3–2.9)**.
  Strength and exercise capacity **did not improve**, lactate was higher in 2 of 3 studies, and
  oedema and fatigue were more frequent. [RCT-SR, moderate, ABSTRACT]
- **Meinhardt 2010** (Ann Intern Med 152:568–77): a placebo-controlled RCT of 96–103 recreational
  athletes over 8 weeks; the press releases disagree on n. Sprint capacity +3.9% overall and +8.3%
  in men given GH with testosterone. **No other performance measure changed**, and the effect was
  gone 6 weeks after stopping. The authors called it too small to judge safety. [RCT, limited,
  ABSTRACT/SECONDARY]
- **Blackman 2002** (JAMA 288:2282): 131 people aged 65–88. Lean mass up and fat down. Only a
  marginal strength gain, in men on GH plus sex steroid; women showed no gain. Diabetes or glucose
  intolerance in **18 GH-treated men against 7** (P=.006), and adverse effects in up to 40%.
  [RCT, moderate, ABSTRACT]
- **Unknowns:** cancer (see the cross-cutting section) and long-term cardiometabolic effects in
  healthy people.
- **Grey market:** products sold as "HGH" are frequently something else (5 of 21 genuine).

### Tesamorelin (Egrifta / Egrifta SV / Egrifta WR) — GHRH analogue

**FDA-approved (2010)** to reduce excess abdominal fat in adults with HIV lipodystrophy.
- **Falutz 2007**, NEJM 2007, doi 10.1056/NEJMoa072375 (PMID 18057338): 412 HIV patients over 26 weeks, on the approved
  regimen as trial context. VAT **−15.2% against +5.0%** on placebo; triglycerides and the
  total/HDL ratio improved; no glycaemic difference; IGF-1 +81%. Adverse events were similar
  overall, but **more withdrawals for AEs** on tesamorelin. [RCT, strong in its population,
  ABSTRACT]
- **Falutz 2010** (JCEM 95:4291): pooled analysis of the two phase-3 trials, n=806. VAT treatment
  effect −15.4%; no clinically meaningful glucose difference at 26 or 52 weeks. [RCT pooled, strong,
  ABSTRACT]
- **Makimura 2012** (JCEM 97:4769): 60 abdominally obese people **without HIV** but with reduced GH
  secretion, over 12 months. VAT treatment effect **−35 cm² (95% CI −58 to −12)**. No subcutaneous
  fat change. Triglycerides, CRP and carotid IMT improved, with no worsening of glucose.
  [RCT, limited, ABSTRACT]
- **Adverse events** (label, via secondary summaries): arthralgia about 13% (placebo about 11%),
  injection-site reactions, peripheral oedema about 6% (placebo about 2%), myalgia and limb pain
  about 6%. Discontinuation for AEs 9.6% against 6.8%. The label warns that glucose intolerance or
  diabetes may develop. [label, SECONDARY]
- **Not shown:** any muscle or strength benefit, or any effect in lean healthy people.
- **Sponsor:** the developer, Theratechnologies, sponsored the phase-3 programme. That is
  UNVERIFIED in this session, though the programme was company-run.
- **Grey market:** 11 consumer-tested "tesamorelin" samples contained no tesamorelin (preprint).
- **TGA:** I found no ARTG registration (UNVERIFIED); it falls under the S4/Appendix D GHRH entry.

### Sermorelin — GHRH(1-29)

- **FDA:** Geref was once approved. It was withdrawn from the US market in 2008; the reason is
  UNVERIFIED (often said to be commercial rather than safety, but I could not confirm that).
  Compounding status is unclear, with conflicting secondary sources.
- **Human data:**
  - A 5-month single-blind RCT of a GHRH(1-29) analogue ([Nle27]) in older men and women
    (PMID 9141536; likely Khorram 1997, authors not seen in the result). Lean mass rose **in men
    only**, insulin sensitivity rose in men only, and skin thickness rose in both sexes.
  - A secondary source describes 19 adults aged 55–71 over 16 weeks, with +1.26 kg lean mass in men.
    It is unclear whether this is the same trial.
  - Vittone 1997 studied nightly GHRH in elderly men. [RCT, very limited, ABSTRACT/SECONDARY]
- **AEs:** injection-site reactions and flushing in the old label (UNVERIFIED this session).
- **Unknowns:** no long-term data, plus the IGF-1 concern.

### CJC-1295 (with DAC; "without DAC" = modified GRF 1-29) — GHRH analogue

- **Teichman 2006** (JCEM 91:799–805): two placebo-controlled, ascending-dose RCTs in healthy
  adults aged 21–61, lasting 28 and 49 days. Half-life 5.8–8.1 days. GH rose 2–10-fold for 6 days
  or more and IGF-1 1.5–3-fold for 9–11 days, with a cumulative effect after repeat doses.
  "Relatively well tolerated". **Hormone levels only; no body-composition or strength outcome.**
  [RCT phase 1, very limited, ABSTRACT]
- **Phase 2 in HIV visceral obesity** (NCT00267527, ConjuChem; 192 enrolled): **halted July 2006
  after a participant in Argentina died**. The company called it "too early to know" whether the
  drug was involved. [SECONDARY news, aidsmap 2006]
  - Claims that the death was a myocardial infarction from pre-existing coronary disease, judged
    unrelated, appear **only on vendor pages: UNVERIFIED**. I found no peer-reviewed report.
  - Development stopped and the drug was never approved.
- **"Without DAC" (mod-GRF 1-29):** no published human trial was found.
- **Grey market:** it was found in products sold as hGH, and 22 consumer samples contained none of
  the labelled peptide (preprint).
- **Regulatory:** WADA S2. TGA S4 plus Appendix D. FDA unapproved, under FDA's own 503A evaluation.

### Ipamorelin — GHRP / ghrelin agonist

- **Beck 2014** (Int J Colorectal Dis 29:1527; NCT00672074; sponsor Helsinn): 117 enrolled and 114
  analysed after bowel resection. Time to a tolerated meal 25.3 h against 32.6 h, **p=0.15, not
  significant**. TEAEs 87.5% against 94.8%, a surgical population. [RCT phase 2, limited (negative)]
  - A second Helsinn phase-2 trial (NCT01280344) had no results found.
- **No human body-composition, strength or fat-loss trial exists.** The muscle claims rest on rat
  data. [ANIMAL]
- **AEs** in healthy users are not characterised by any trial. It is widely called "selective"
  (little cortisol or prolactin release) on the strength of early pharmacology; I did not verify
  that against human studies this session.
- **Regulatory:** WADA S2. TGA S4 plus Appendix D. An FDA evaluation document cites "significant
  safety concerns", and the compounding status is contested.
- **Grey market:** missing-content samples, and a glycine-extended analogue was found in seized
  products.

### GHRP-2 (pralmorelin)

- **Approved in Japan only, as a single-dose diagnostic** for GH deficiency (Kaken). The approval
  year is cited as both 2004 and 2006.
- **Human data:** acute GH-release studies only. In young adults (Arvat 1997, Peptides), GHRP-2 and
  hexarelin gave a GH response greater than GHRH, and also **raised ACTH, cortisol and prolactin**
  ("not fully specific"). [RCT/crossover acute, limited for endocrine effects, ABSTRACT]
- **No body-composition or performance trial.** One secondary page cites a 36% rise in food intake
  from a "2005 study" (UNVERIFIED).
- **Grey market:** found as an undeclared ingredient in "nutritional supplements" (Cologne).

### GHRP-6

- **Human data:** acute GH release only. It stimulates appetite through the ghrelin receptor; the
  quoted "~30% food intake" figure is UNVERIFIED (secondary only).
- **No human body-composition trial.** [none]
- **Grey market:** sold as "hGH" (3 of 21), and a modified GHRP-6 was found.
- **FDA:** category membership conflicts between sources (2 or 3).

### Hexarelin (examorelin)

- **Endocrine effects:** potent acute GH release, plus ACTH and cortisol (through AVP, not CRH) and
  prolactin, in small healthy-volunteer studies of 6–15 people. [acute, limited, ABSTRACT]
- **Rahim 1998** (GH & IGF Res; JCEM): the GH response fades with long-term use, but only partly,
  and it **recovers after stopping**. n and duration were not seen; the "45% by 16 weeks" figure is
  vendor-only and UNVERIFIED.
- **Cardiac claims** rest mostly on preclinical work, with one second-hand human LV-function report
  (Broglio 2000, UNVERIFIED).
- **No body-composition trial.**

### MK-677 / ibutamoren — **non-peptide**, oral ghrelin-receptor agonist (Merck compound)

- **Nass 2008** (Ann Intern Med 149:601–11): 65 healthy people aged 60–81, a 2-year modified
  crossover with the primary endpoints at 12 months.
  - GH and IGF-1 rose to young-adult levels.
  - Fat-free mass **+1.1 kg against −0.5 kg** (P<0.001); one secondary source says this was mainly
    body water.
  - Abdominal visceral fat fell.
  - **No change in strength or function.**
  - Fasting glucose **+0.3 mmol/L** (P=0.015) and **insulin sensitivity declined**.
  - Funding was not verified this session (PMC full text unreachable). [RCT, limited, ABSTRACT]
- **Murphy 1998** (JCEM 83(2), doi 10.1210/jcem.83.2.4551; the task said JBMR, but it is JCEM): 8 healthy young
  adults on calorie restriction, crossover. Nitrogen balance +0.31 against −1.48 g/day (P<0.01) and
  IGF-1 264 against 188 ng/mL. Short-term anti-catabolic effect only. [RCT crossover, very limited]
- **Adunsky 2011** (Arch Gerontol Geriatr; NCT00128115): 123 older people after hip fracture.
  - Gait speed improved modestly; most function measures did not.
  - **Stopped early. Abstract: "unfavourable safety profile".**
  - Congestive heart failure in 4/62 (6.5%) against 1/61 (1.7%), per secondary sources only.
  - The DOI is cited inconsistently between sources. [RCT, limited; safety signal]
- **Main AEs:** increased appetite, fluid retention, raised glucose and reduced insulin sensitivity,
  and CHF in frail older people. Cancer is the shared IGF-1 unknown.
- **Regulatory:**
  - Not approved anywhere.
  - FDA **Category 2** (significant safety risks; PCAC voted against).
  - TGA S4 plus Appendix D (GHS entry).
  - WADA S2.

### IGF-1: mecasermin (Increlex) and IGF-1 LR3

- **Mecasermin is approved** (FDA 2005) for severe primary IGF-1 deficiency in children.
  - Label: severe hypoglycaemia including seizures, lymphoid/tonsillar hypertrophy, benign and
    malignant neoplasia (2019 EU/UK safety letter: stop permanently if a neoplasm appears), and
    slipped capital femoral epiphysis (added to the US label in 2025).
- **Healthy adults, Friedlander 2001** (PMID 11297574): 16 postmenopausal women over 60, 1 year,
  dosed to raise IGF-1 to young-normal levels.
  - **No change in lean mass, fat, bone, grip/bench/leg-press strength, mood or memory**; the
    trial was stopped early because nothing was changing. [RCT, limited (negative)]
- **Thompson 1995:** 4 weeks in elderly women. Headache, lethargy, joint swelling and bloating at
  high dose. [RCT, very limited]
- **IGF-1 LR3** (Long R3, a cell-culture reagent analogue): **no human study of any kind**.
  Unpurified product has been found on the black market. Its hypoglycaemia and neoplasia risks are
  inferred from IGF-1 pharmacology. [none / ANEC]
- **Regulatory:** WADA S2.3. TGA scheduling of IGF-1 LR3 not verified.

### MGF / PEG-MGF (mechano growth factor, IGF-1Ec E-peptide)

- **No human intervention data** that I could verify. A vendor-page claim of a "2014 negative human
  RCT" is UNVERIFIED and may not exist.
- **Matheny 2010** (Endocrinology minireview): there is **inadequate evidence that MGF is even made
  as a distinct peptide in vivo**, and the synthetic peptide's actions should not be equated with
  the Igf1 gene's products. Later work found that IGF-1, but not MGF, drove muscle-cell
  proliferation in key experiments. [INVITRO/ANIMAL, very limited]
- **Regulatory:** WADA S2.3. FDA: PEG-MGF was moved off Category 2 in April 2026 pending PCAC
  review, which is **not** an approval. TGA not verified.

### Follistatin

- **Human data are gene therapy only.** Mendell 2015 was a phase 1/2a open-label trial,
  rAAV1.CMV.huFS344 injected into the quadriceps of 6 men with Becker muscular dystrophy. Six-minute
  walk +58, +125, +108 and +29 m in 4 of 6, no change in 2, and no adverse effects. **Uncontrolled.**
  [NRS, very limited]
- **BioViva CEO's self-administered follistatin plus telomerase gene therapy (2015):** unpublished,
  n=1, and anecdotal. [ANEC]
- **Injectable "follistatin-344" peptide (grey market): no human data.** It is a large protein, so
  stability and identity of grey-market product are serious doubts; no analytical data were found.
- **Regulatory:** WADA S4 (activin receptor IIB pathway). Unapproved everywhere.

### hCG (human chorionic gonadotrophin)

- **Approved** (FDA and others) for infertility and hypogonadotropic hypogonadism. Prescription
  only; TGA S4 (UNVERIFIED this session).
- **Coviello 2005** (JCEM 90:2595): 29 healthy men suppressed with testosterone. Testosterone plus
  placebo cut intratesticular testosterone by 94%; low-dose hCG kept it in the normal range,
  dose-dependently. **Endocrine endpoint only.** [RCT, moderate for that endpoint]
- **No RCT of hCG for muscle or strength in eugonadal men was found.** One retrospective case
  series (testosterone above 300 ng/dL) is uncontrolled. [NRS, very limited]
- **Weight loss:** the FDA says there is "no substantial evidence HCG increases weight loss beyond
  that resulting from the recommended caloric restriction". In 2011 the FDA and FTC sent warning
  letters over OTC "homeopathic" hCG.
- **AEs** (label-level, not re-verified): gynaecomastia, oedema, mood effects, and OHSS and
  thromboembolism in women.
- **WADA:** S2.2.1, prohibited in males.

### Gonadorelin (GnRH)

- **No human trial of body composition or performance was found.**
- Known clinically as a diagnostic or pulsatile-infertility agent. Typical reported AEs are
  headache, flushing, nausea and injection-site reactions (secondary only).
  - With continuous exposure, GnRH agonism **suppresses** the axis. This is pharmacology, not
    trial data here.
- **FDA status of the US product, and whether gonadorelin is on a compounding category:
  UNVERIFIED.** Search found no Category 2 listing.
- **WADA:** S2.2.1 (males).

### Kisspeptin and kisspeptin-10

- **George 2011** (JCEM 96:E1228): IV kisspeptin-10 in healthy men (n=6 for the bolus arm) raised
  LH dose-dependently. A 22.5-h infusion raised testosterone from **16.6 to 24.0 nmol/L**.
  [mechanistic, very limited]
- **A 2026 Eur J Endocrinol study** (doi 10.1093/ejendo/lvag134; authors not seen): subcutaneous
  kisspeptin-10 raised LH, FSH and testosterone. After 5 days of continuous exposure, testosterone
  stayed up but gonadotrophins returned to vehicle levels, which suggests tachyphylaxis.
  [mechanistic, very limited, ABSTRACT]
- **No muscle, strength or fat outcome in any human study.**
- **Regulatory:** FDA **Category 2** for kisspeptin-10 (PCAC against). WADA S2.2.1 (males). TGA not
  verified.

## What the evidence supports, in one line each

- **A body-composition change is shown in RCTs:**
  - rhGH: about +2 kg lean (partly water) and about −2 kg fat, **no strength gain**.
  - Tesamorelin: about −15% visceral fat (HIV); −35 cm² VAT in non-HIV abdominal obesity.
  - MK-677: +1.1 kg fat-free mass, **no strength gain**.
- **No body-composition benefit was shown in humans:** sermorelin (except a small gain in men only),
  CJC-1295, ipamorelin, GHRP-2, GHRP-6, hexarelin, IGF-1 (negative RCT), IGF-1 LR3, MGF/PEG-MGF,
  follistatin, hCG, gonadorelin and kisspeptin.
- **Best-characterised harms:**
  - rhGH: oedema, arthralgia, carpal tunnel, gynaecomastia, dysglycaemia.
  - Tesamorelin: arthralgia, oedema, injection site, glucose warning.
  - MK-677: glucose up, insulin sensitivity down, CHF in frail older people.
- **Least-known:** IGF-1 LR3, MGF/PEG-MGF, injectable follistatin, mod-GRF and the glycine-extended
  grey-market analogues. These have no human safety data at all, and grey-market identity is
  unreliable.
