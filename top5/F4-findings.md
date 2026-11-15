# F4: load / mechanical tension and rep execution

Agent F4, 2026-11-02. This covers load and rep range, mechanical tension as the stimulus, tempo/TUT, pauses, peak
contraction, eccentric emphasis, isometrics, cheat reps, set structures (cluster, rest-pause, drop, myo-reps, superset),
intra-set velocity loss and progressive-overload method. Prior work: A1 and A6 in `../agent-notes/`. Rows marked
"A6 V" were bibliographically verified by A6. **No full text was read.** WebFetch to PMC and doi.org is blocked
(ENOTFOUND), so every source is SECONDARY (search-index abstract text) unless the row says otherwise. Evidence codes:
I = indirect human outcome, M = mechanism, A = animal, H = product hypothesis.

## 10-line summary

1. **Mechanical tension is the stimulus. It is not a separate top-5 lever. It is what effort (factor #1) delivers.** Any load from ~30% to >85% 1RM gives the same growth when sets end near failure (Schoenfeld2017a 21 studies; Lopez2021 28 studies/747; Carvalho2022; trained: Morton2016 n=49, Schoenfeld2015b n=18, Cumming2025 n=14). (I, strong)
2. **Load choice is a strength lever, not a hypertrophy lever.** Heavy loads consistently win for 1RM. For size, the only qualifier is a **load floor**: ~20% 1RM lagged (Lasevicius2018, untrained), and light loads need failure where heavy ones do not (Lasevicius2022). (I, moderate)
3. **Candidate top-5 factor from this cluster: "progressive overload: keep each set hard as you adapt, by adding load OR reps."** Plotkin2022 (n=43 trained): rep progression ≈ load progression for growth (RF +2.8 mm, CI90% −0.5 to 5.8, favouring reps); load progression is slightly better for 1RM. This is effort over time, so it should be **merged with effort** rather than ranked as an independent factor. (I, limited–moderate)
4. **Tempo/TUT is not a lever within ~0.5–8 s per rep.** Schoenfeld2015a (8 studies); Enes2025 Bayesian (14 RCTs, 278): ES 0.09 (CrI −0.04 to 0.22); Amdi & King 2025 eccentric duration (9 studies, 166): hypertrophy g = 0.05 (−0.22 to 0.33). Only very slow reps (>10 s) look worse, on thin data. (I, moderate)
5. **Eccentric emphasis: no reliable hypertrophy advantage.** Silva2025 (26 studies, 682): ES 0.285, p = 0.18, I² 84%, GRADE very low; Schoenfeld2017c 10.0% vs 6.8%, n.s. In trained men, accentuated eccentric load gave more strength but similar size (Walker2016, n=28). Flywheel effect sizes are mostly pre-post or pooled across outcomes. (I, limited)
6. **Set structures are time tools, not growth tools.** Cluster sets: hypertrophy ES −0.05 (−0.32 to 0.23), 29 studies (Davies2021). Drop sets: n.s. (Coleman2022; Sødal2023), with ⅓–½ the time. Rest-pause and drop sets in trained men ≈ traditional (Enes2021, n=28). Supersets ≈ traditional (Zhang2025). (I, moderate)
7. **Pause reps, peak-contraction "squeeze", myo-reps (as a named protocol): no longitudinal hypertrophy trial found.** The closest are inter-set flexing (Schoenfeld2020, trained, small) and rest-pause. (Evidence: none / very limited)
8. **Cheat reps: one 8-week trial in untrained people** (Augustin2025) found growth similar to strict reps with more volume load. COI: content-creator co-authors. (I, very limited)
9. **Velocity loss within a set is the one execution variable with a dose-response.** Jukic2023 (19 longitudinal studies): more VL means more hypertrophy, b = 0.006 (0.001–0.012), and worse jump/sprint. This is proximity to failure measured differently, and the effect per step is small. (I, limited–moderate)
10. **For TENSR**: rep count, concentric velocity loss / rep slow-down, tempo and pause logging, eccentric:concentric split, momentum (jerk) and drop-set detection all run on the current IMU + ADS1292R with no hardware change. **Load cannot be sensed by the puck**, so it is user-entered. Only rep slow-down (an effort proxy) and rep/load progression logging map onto outcome-relevant factors; tempo, TUT, pause and squeeze scores would coach variables with no outcome effect. (H)

## Scorecard (the brief's five ranking criteria)

| Factor | 1. Effect size at realistic contrasts | 2. Certainty | 3. Trained-lifter evidence | 4. Controllable set to set | 5. Dose-response shape | Verdict |
|---|---|---|---|---|---|---|
| Load (~30–85% 1RM, effortful sets) | ~0 for hypertrophy; large for 1RM | high (4 metas, 21–119 studies, heavy overlap) | moderate (Morton2016, Schoenfeld2015b, Cumming2025, Schoenfeld2014) | yes | flat above a floor (~30% 1RM); below that, needs failure | **Not top-5 for size**; a constraint |
| Progressive overload (load or reps) | unquantified vs no progression; load ≈ reps | low–moderate (one trained RCT for method) | Plotkin2022 n=43 | yes, across sessions | unknown | **Merge with effort #1** ("stay hard over weeks") |
| Mechanical tension (mechanism) | n/a | M: human acute (Drummond2009) + A: mice (Goodman2011) | n/a | via load + effort | n/a | Explains #1; not a separate lever |
| Tempo / TUT (0.5–8 s) | ES ≈ 0.05–0.09, CIs span 0 | moderate (≥3 metas, ~8–14 studies) | ~46% trained in Amdi & King | yes | flat; >10 s/rep possibly harmful | **No effect** in normal range |
| Eccentric emphasis / AEL / flywheel | ES 0.29 n.s.; GRADE very low | low | Walker2016 (similar size) | partly | unknown | Minor / no reliable effect |
| Isometrics | builds muscle; long length better | limited (SR, no meta) | few | yes | length-dependent | Alternative modality, not a lever for dynamic lifters |
| Pauses / squeeze | no data | none | none | yes | unknown | **No evidence** |
| Cheat reps | ≈ strict | very limited (1 trial, untrained) | none | yes | unknown | No evidence of an effect either way |
| Cluster / drop / rest-pause / superset / myo-reps | ≈ 0 (ES −0.05 to 0.08) | moderate | Enes2021, Angleri2017, Prestes2019 | yes | n/a | **No effect on size**; saves time |
| Intra-set velocity loss | small positive slope | limited–moderate (19 studies) | mostly trained | yes (IMU-measurable) | monotonic, small; costs power | This is effort #1 by another name |

**Recommendation to the coordinator.** No factor in this cluster earns an independent top-5 slot on effect size.
The defensible way to carry it is inside factor #1:

- **effort, delivered as mechanical tension on the high-threshold fibres**;
- **a load floor of ~30% 1RM**;
- **progression (load or reps) to keep sets hard over weeks**.

If the coordinator needs a fifth factor and nothing else fills the slot, "progressive overload" is the only candidate
from F4. Its evidence base is thin (one trained RCT on method; nothing randomising progression against no
progression).

---

## 1. Load and rep range

**Meta-analyses.** These overlap heavily, so do not add their counts.

| Meta-analysis | Studies / n | Hypertrophy | Strength |
|---|---|---|---|
| Schoenfeld2017a | 21 studies | similar ≤60% vs >60% 1RM to failure | favours heavy |
| Lopez2021 (network) | 28 / 747 | load-independent | favours heavy |
| Carvalho2022 (volume-load matched) | count not seen | similar | favours heavy |
| Currier2023 (Bayesian network) | 119 / 3364 (hypertrophy); 178 / 5097 (strength) | every program > control; "higher-load multiset 2×/wk" ranked top, 0.66 (0.47–0.85) vs control | — |

The Currier ranking does not show a meaningful load difference. The authors' own conclusion is that people can choose
by preference. (I, strong for size equivalence across ~30–85% 1RM.)

**Trained lifters.** These are the primary studies that matter.

- **Morton2016** (n = 49, ≥2 y trained, 12 wk). 30–50% and 75–90% 1RM, both to failure, gave similar DXA lean mass
  and fibre CSA. (I, moderate)
- **Schoenfeld2015b** (n = 18, 8 wk). 25–35 RM and 8–12 RM gave similar elbow-flexor, elbow-extensor and quadriceps
  MT. Squat 1RM favoured heavy. Small n: "no difference" is not equivalence.
- **Cumming2025, J Appl Physiol 139:685** (n = 14 trained, within-subject leg vs leg, 9 wk). 3–5 RM and 20–25 RM
  gave MT +7 ± 17% (mid) and +8 ± 8% (distal) either way. Single-joint 1RM favoured heavy (9% vs −3%).
- **Schoenfeld2014** (trained, volume-equated). 3×10 and 7×3 gave similar size. 7×3 gave more strength and took
  about 4× the time. The n is reported as 17 in one source and 20 in another; unresolved.

**The load floor.**

- **Lasevicius2018** (untrained, volume-load equated): 40/60/80% 1RM were comparable and 20% lagged. Results are seen
  only via a blog, so they are limited and the numbers are UNVERIFIED.
- **Lasevicius2022**: failure mattered at 30% 1RM, not at 80%.

So light loads work only when taken close to failure; heavy loads give more margin for error on effort.

## 2. Mechanical tension: why it works (mechanism)

- **Leading stimulus.** Mechanical tension on the fibres is the best-supported stimulus. Metabolic stress, damage,
  hormones and hypoxia are unproven as causes (Wackerhage2019; M, moderate). The mechanosensor itself is not
  identified.
- **The pathway is mTORC1, with causal proof only in mice.**
  - Mechanical stimuli activate mTOR through phosphatidic acid: Hornberger2006, PLD-dependent; the later model adds
    DGKζ, TSC2 and lysosomal relocation, independent of PI3K/Akt and growth factors. (A)
  - In mice, mTOR kinase inside the fibre is **necessary** for overload hypertrophy. Rapamycin blocks it, and a
    rapamycin-resistant mTOR rescues it (Goodman2011). (A, strong within the model)
  - In humans, rapamycin blocks the acute ~40% rise in MPS after heavy contractions, and S6K1 phosphorylation
    (Drummond2009). (M, acute only)
  - **Human evidence that tension *causes* growth is inferential.** It is assembled from acute signalling plus
    training trials where tension is the common factor. No human trial blocks mTORC1 over weeks of training.
- **Why load does not matter but effort does (size principle).**
  - A heavy load recruits high-threshold motor units from rep 1.
  - A light load recruits them progressively as lower-threshold units fatigue. Muddle2018 (decomposed sEMG) found
    both conditions recruit higher-threshold units with fatigue, with heavy reaching larger units throughout.
  - At failure, type II fibres are depleted of glycogen regardless of load or rep duration (Morton2019).
  - **So the growth-relevant quantity is tension on the high-threshold fibres, and effort is how a light load gets
    there.** (M, moderate)
  - Corollary for TENSR: sEMG amplitude was unrelated to fibre glycogen depletion (Morton2019). Amplitude is not a
    stimulus meter (also A1/A6).
- **The "effective reps" idea**, that only the last ~5 reps near failure stimulate, is a hypothesis built on this
  mechanism. It is not a measured quantity. (H/M, limited) It is consistent with Lasevicius2022 and Jukic2023, but no
  trial tests it directly.

## 3. Tempo, repetition duration, time under tension

**Evidence.**

- Schoenfeld2015a (8 studies): 0.5–8 s per rep similar; >10 s possibly inferior (few studies).
- Enes2025, JSCR 39(12):1331, Bayesian, 14 RCTs, 278 participants: ES 0.09 (CrI −0.04 to 0.22), trivially favouring
  the faster tempo. The tested range is ~0.5 (or 0.25) to 4.5 s per action; sources disagree. Very slow reps were
  not covered.
- Amdi & King 2025, eccentric duration, 9 studies, 166 participants, 46% trained: hypertrophy g = 0.05 (90% CI −0.22
  to 0.33).
- Lacerda2021 (n = 10 untrained, 14 wk): 2 s vs 6 s reps to failure gave the same growth.

(I, moderate that tempo is not a lever in the normal range.)

**Why TUT does not matter (M).**

- Growth tracks the tension each recruited fibre experiences. Duration matters only insofar as it changes effort.
- When sets go to failure, a slow tempo just reaches failure in fewer reps with similar total stimulus (Lacerda2021).
  Fibre recruitment at failure is the same whatever the rep duration (Morton2019).
- Burd2012's higher MPS with 6 s reps came at 30% 1RM **not to failure**: slow reps made a sub-maximal set harder.
  It is acute, so it is not evidence for TUT per se.

**Why tempo extremes hurt (M, limited).**

- Very slow reps force a lighter load, because concentric force capacity is the limit and deliberate slowing lowers
  force output. Per-fibre tension is lower, and high-threshold units are recruited only late, if at all.
- Very slow reps also cut reps and volume load.
- Very fast or ballistic eccentrics with momentum offload tension from the target muscle for part of the rep. The
  Augustin2025 data say this costs nothing measurable, at least in untrained people.

## 4. Eccentric emphasis, AEL, flywheel, isometrics

- Silva2025 (26 studies, 682) supersedes Schoenfeld2017c (15 studies, 356) and Roig2009 (20 RCTs). There is no
  significant eccentric advantage for size, and the certainty is very low.
- **Striking claim, checked:** Roig2009's "eccentric better for mass" rested on girth, with CSA only a trend. Two
  later, larger meta-analyses do not reproduce it.
- **Trained:** Walker2016 (n = 28). Accentuated eccentric loading at concentric load + 40% gave more strength but
  similar hypertrophy.
- **Flywheel:**
  - Maroto-Izquierdo2017 SMD 0.63 pools functional and structural outcomes together, so it is not a hypertrophy
    estimate.
  - Petré2018 CSA ES 0.59 appears to be within-group change, so it is not superiority.
  - Neither supports "flywheel grows more".
- **Mechanism:** eccentric actions produce more force per active fibre at lower metabolic cost. That predicts strength
  and fascicle-length effects more than size. (M, limited)
- **Isometrics** build muscle, and long-length isometrics transfer better (Oranchuk2019, a systematic review with no
  meta-analysis). This is an alternative modality, not an add-on lever. (I, limited–moderate)

## 5. Pauses, squeeze, cheat reps

- **Pause reps**, at the stretched or the contracted position: **no longitudinal hypertrophy trial found** in two
  searches. Adjacent evidence:
  - lengthened partials and initial-ROM training (Kassiano, Maeo, Wolf; see A1 §2);
  - past-failure lengthened partials in calves (Larsen et al., seen only via a blog: +9.6% vs +6.7%, untrained;
    UNVERIFIED).
  - A pause at long length is a plausible way to add stretch-position tension, but it is **H**.
- **Peak-contraction squeeze:** only inter-set flexing (Schoenfeld2020, trained, small), with mixed MT and strength
  results. Evidence: very limited.
- **Cheat reps:** Augustin2025 (untrained, 8 wk, within-subject). Similar growth; more volume load. A6 corrected the
  author order. COI flag. Evidence: very limited. **No trial on "heavy cheat, then strict" sequencing.**

## 6. Set structures

| Method | Best evidence | Hypertrophy vs traditional | Note |
|---|---|---|---|
| Cluster sets | Davies2021, 29 studies | ES −0.05 (−0.32 to 0.23) | keeps velocity; no size cost |
| Drop sets | Coleman2022 (~5 studies); Sødal2023 (6 studies / 142, secondary) | trivial / n.s. | ⅓–½ the time |
| Rest-pause | Prestes2019 (n = 18 trained): RP > TRAD for thigh size; Enes2021 (n = 28 trained): no difference | inconsistent | **Prestes is the striking claim and it is not replicated** |
| Myo-reps | no named-protocol trial found | — | a rest-pause variant |
| Supersets | Zhang2025 | similar | time-efficient |

**Mechanism** (M). All of these keep effort and tension on the high-threshold fibres. They change rest, metabolite
build-up and session time, none of which is shown to drive growth independently.

## 7. Intra-set velocity loss

- Jukic2023 (18 acute + 19 longitudinal studies):
  - more velocity loss means more hypertrophy, b = 0.006 (0.001–0.012);
  - strength and endurance are unaffected;
  - jump and sprint get worse.
- If b is in SMD per percentage point of VL (the unit is UNVERIFIED), going from 20% to 40% VL buys about 0.12 SMD.
  That is small.
- Pareja-Blanco2017 (n = 22 trained): VL40 gave more hypertrophy than VL20; VL20 did 40% fewer reps and gained more
  jump.
- This is proximity to failure measured in velocity. It is not a separate factor.

## 8. Progressive overload method

- Plotkin2022 (n = 43, ≥1 y trained, 8 wk). Adding reps at a fixed load and adding load at a fixed rep range gave
  similar growth: RF favoured reps, 2.8 mm (CI90% −0.5 to 5.8). Strength slightly favoured load, 2.0 kg (−2.4 to 7.8),
  of questionable practical importance.
- **No trial randomised "progression vs no progression" with effort held constant.** The rationale for progression
  is therefore effort maintenance (M/I, limited): as the lifter adapts, a fixed load × reps moves further from
  failure.

## 9. Striking results, fact-checked

| Claim | Check | Verdict |
|---|---|---|
| "Light loads build more muscle than heavy" (Burd2010 title) | 4 h MPS equal (30FAIL = 90FAIL); only the 24 h point differed; acute only; long-term metas show equality | Overstated. Acute ≠ growth |
| "Eccentrics grow more muscle" (Roig2009) | girth outcome; Silva2025 and Schoenfeld2017c find n.s. | Not supported |
| "Longer eccentrics g = 0.33 for hypertrophy" (online summaries of Amdi & King) | 0.33 is **strength** in trained people; hypertrophy g = 0.05 | Misreported online |
| "Flywheel ES 0.59–0.63 for size" | pooled outcomes / within-group ES | Not a superiority estimate |
| "Rest-pause grows more" (Prestes2019, n = 18) | not replicated by Enes2021 (n = 28 trained) | Unreplicated single trial |
| "20% 1RM is not enough" (Lasevicius2018) | untrained; results seen only via a blog; consistent with Lasevicius2022 | Plausible floor, limited |
| "Higher-load multiset ranked #1" (Currier2023) | rank ≠ meaningful difference; the authors themselves say choose by preference | Do not cite as "heavy is best for size" |

**Not checked (budget):** retraction status of every study above. A1 flagged the Barbalho group; none of its papers
is used here. Funding and COI were checked only where already noted (Augustin2025).

## 10. Open disputes

- Is there a real load floor in **trained** lifters, and where is it: 20% or 30% 1RM?
- Does the >10 s/rep inferiority hold? It rests on very few studies.
- Do lengthened-position pauses add anything beyond lengthened partials? No data.
- Regional differences: Cumming2025's ±17% SD at mid-thigh shows huge individual spread. A group-level null hides
  individual responses (Angleri2017: 5 of 16 people responded differently).

## 11. What TENSR could track from this cluster (H, all needing validation)

All of the following run on the **current board**: LSM6DSO IMU plus ADS1292R.

| Metric | Sensor | Outcome relevance | Recommendation |
|---|---|---|---|
| Rep count per set | IMU (EMG bursts as a cross-check) | needed for rep-progression logging (Plotkin2022) | ship |
| Concentric rep slow-down / velocity loss within a set | IMU angular velocity of the limb segment (a proxy for bar velocity) | the only execution variable with a dose-response (Jukic2023); an effort / proximity-to-failure proxy | **highest value**; validate against true failure |
| Progression log (reps at load across sessions) | reps sensed; **load user-entered** | keeps sets hard over weeks | ship as logging |
| Tempo, TUT, pause detection, ecc:con split | IMU | none in the 0.5–8 s range | log only; never score. Flag only >10 s/rep extremes |
| Momentum / cheat detection | IMU jerk, EMG per unit of motion | none shown for growth | optional, framed as form, not stimulus |
| Drop-set / rest-pause detection | EMG amplitude step plus continued reps | none for growth; time-saving | log only |
| Load estimate | start-of-set EMG amplitude (relative to the person's own baseline) | strength-relevant, not size-relevant | **do not market as a stimulus score** (Morton2019, A1) |

**Not possible without added hardware:** absolute load. That needs a bar or stack sensor, or user entry.
