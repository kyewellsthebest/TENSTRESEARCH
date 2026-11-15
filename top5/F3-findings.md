# F3 — Muscle length, range of motion, lengthened partials, stretch-mediated hypertrophy

Agent F3, 2026-11-02. Scope per `BRIEF.md`. Evidence codes per `../PROTOCOL.md` §5 (D / I / M / A / H). Every
row keyed here is in `F3-studies.csv`. Search log in `F3-searchlog.md`.

**Access caveat, read first.** WebFetch was blocked on every host tried (peerj.com, pmc.ncbi.nlm.nih.gov,
pubmed.ncbi.nlm.nih.gov, www.ebi.ac.uk, journal.iusca.org, rgu-repository.worktribe.com). No full text was read.
Every number below comes from abstracts or abstract-level snippets returned by WebSearch (ABSTRACT), or from
secondary write-ups (SECONDARY, named). Nothing is marked FULL.

## Ten-line summary

1. **Short-range partials are probably worse than full ROM for growth** (Pallarés 2021: lower-limb hypertrophy ES 0.88, 16 studies; Kubo 2019 glutes/adductors; McMahon 2014). Most "partial" arms in those trials worked the *shortened* part of the range. (I, moderate)
2. **Choosing exercises that load a muscle at a long length beats loading it short, in untrained people.** Maeo 2021 seated vs prone curl, hamstrings +14% vs +9% (MRI). Maeo 2023 overhead vs neutral triceps, long head +28.5% vs +19.6% (secondary). Wolf 2025 SMHS review: 8 studies, about 120 people, size and fascicle length may grow more. (I, moderate in untrained; **no trained-lifter replication found**)
3. **"Lengthened partials beat full ROM" is not established.** Wolf 2023 subgroup: SMD −0.28 (95% CI −0.81 to 0.16) for the lengthened-partial vs full contrast. The direction favours lengthened partials but the interval includes zero and the subgroup is a handful of studies. (I, limited)
4. **In trained lifters every controlled test found ≈ no difference.** Wolf 2025 PeerJ (n = 30, 8 wk): similar. Gschneidner preprint (15 sites, n = 134 vs 163, 12 wk): similar, but muscle size was estimated. Larsen 2025 EJSS calves (n ≈ 23): +0.40 mm, credible interval crosses 0, BF 1.2. 2025 EJSS elbow flexors (n = 13): similar at 50%, SMD 0.10 at the distal 70% site. (I, limited, consistent null to trivial)
5. **"Long-length doubles growth" is cherry-picked.** It is true for one or two muscle regions in untrained people: Kubo glutes 6.7% vs 2.2%, Kassiano calves 15.2% vs 6.2% against *final* partials, McMahon distal ACSA 59% vs 16%. It is not true of whole-muscle growth or of lengthened-vs-full. Kassiano's lengthened-vs-full contrast was p = 0.060.
6. **Regional (distal) growth is the most consistent signal.** Pedrosa 2022/2023, Zabaleta-Korta 2023, the 2025 elbow study and McMahon 2014 all saw it. The pooled regional meta (Varovic 2025, 12 studies) found effects trivial, with only a ~22% mean length contrast. (I, limited)
7. **Mechanism is plausible but unproven in humans.** Total fibre tension at long lengths includes titin-borne passive tension. Animal stretch overload grows muscle massively (quail +53% to +318%, A). Fascicle length rises 5–23% in human long-length trials (I). None of this is shown to scale to trained human hypertrophy. Human static stretching alone gives d = 0.20 (Warneke 2024, 42 studies). (M/A, limited)
8. **Muscle length ≠ joint ROM.** The Maeo effects come from the *other* joint (hip, shoulder) with identical knee/elbow ROM. Maeo 2023's monoarticular triceps heads also grew more, and their length is not changed by shoulder angle. So length alone does not explain that study.
9. **Ranking verdict:** a real but second-tier factor for trained lifters. It is fully controllable (exercise choice plus where in the range you work) and costs nothing, but its proven effect in trained people is ~0 against full ROM. Practical rule: avoid short-range partials; full ROM or a lengthened bias are both fine.
10. **TENSR:** one puck IMU measures range only when the worn segment moves (squat thigh angle: yes; curl/pushdown/leg extension: no). With a per-user calibration of end positions it can log "% of calibrated range used and which end." A second IMU tag on the distal segment makes this general (H). **Product-critical side effect:** MDF and amplitude shift with muscle length (A2). A lifter switching to lengthened partials would move TENSR's fatigue score with no fatigue. Fatigue windows must be angle-gated.

## Scorecard on the five ranking criteria

| criterion | score | basis |
|---|---|---|
| 1. Effect size at realistic contrasts | **Long vs short partial / exercise: small–moderate** (whole muscle ~1.3–1.5× relative gain in untrained; regional sometimes 2–3×). **Lengthened partial vs full: trivial–small, uncertain** (SMD −0.28, CI −0.81 to 0.16). **Full vs short partial: moderate** (Pallarés lower-limb ES 0.88) | Maeo 2021/2023, Pallarés 2021, Wolf 2023 |
| 2. Certainty | **Low–moderate.** About 8–24 trials per meta-analysis, heavily overlapping, n 10–45 per trial, mostly 8–12 wk, ultrasound at 1–3 sites. MRI only in Maeo and Kubo. Several meta-analyses share authors (Wolf, Schoenfeld, Steele, Androulakis-Korakakis) | see CSV overlap notes |
| 3. Trained-lifter evidence | **Very limited and null-to-trivial.** 4 trained trials for lengthened partials, none favouring them clearly. **Zero** trained trials found for long- vs short-length *exercise selection* (seated vs prone, overhead vs pushdown). Goto 2019 (trained) favoured a *mid-range* partial over full | Wolf 2025, Gschneidner preprint, Larsen 2025 EJSS, EJSS 2025 elbow, Goto 2019 |
| 4. Controllability set to set | **High.** Exercise choice, ROM and where the partial sits are fully in the lifter's hands, rep by rep | — |
| 5. Dose-response shape | **Unknown.** No trial varies "how long" in more than two levels. No harm zone shown for hypertrophy. Lengthened work raises damage/DOMS early (not quantified here). Fascicle-length gains appear to plateau (hypothesis: Henselmans commentary, not data) | — |

**Suggested rank among working-set factors:** below effort/proximity to failure, volume and (probably)
frequency/progression. A sensible fourth or fifth. Its value is "don't waste sets in the short range", not "a
multiplier on growth".

---

## 1. The evidence, separated by contrast

The literature confuses four different contrasts. Most striking claims come from mixing them.

### 1a. Full ROM vs partial ROM (partial location mostly *short* or unspecified)

- **Pallarés2021** (SJMSS 31(10):1866–1881; 16 studies; robust variance estimation). Full ROM beat partial for strength (ES 0.56, p = 0.004) and lower-limb hypertrophy (ES 0.88, p = 0.027). There were "no large differences" in architecture. ABSTRACT.
  - **Critique (Kassiano 2022 letter, answered by the authors):** the partial arms were mostly short-range, and work was not equated. The meta did not separate lengthened from shortened partials. (I, moderate for "short partials < full", limited beyond)
- **SchoenfeldGrgic2020** (SAGE Open Med 8:2050312120901559). Systematic review, no meta-analysis. Full ROM benefits lower-body hypertrophy; upper-body evidence limited and conflicting. Number of included studies not retrieved. ABSTRACT.
- **Kubo2019** (EJAP 119(9):1933–1942; n = 17 men; MRI; 10 wk). Full squat (~140° knee flexion) vs half squat (~90°):
  - glute max +6.7% vs +2.2%
  - adductors +6.2% vs +2.7%
  - quadriceps similar; hamstrings ~unchanged in both
  - SECONDARY. The deeper squat lengthens the glutes and adductors; the quads were not differentially affected. (I, moderate for these muscles)
- **Bloomquist2013** (deep vs shallow squat, 12 wk). Secondary source says deep squats grew the quads 4–7% across sites and shallow squats grew little. UNVERIFIED numbers.
- **McMahon2014** (JSCR 28(1):245–255; n = 8 per group; 8 wk plus 4 wk detraining). Long range beat short range:
  - distal ACSA 59 ± 15% vs 16 ± 10%
  - fascicle length 23 ± 5% vs 10 ± 2%
  - ABSTRACT. The snippet's strength figures read "4 ± 2 vs 18 ± 2%" with long range said to be greater, which is internally inconsistent; the source must be checked. Distal 59% in 8 weeks is an outlier magnitude on n = 8. (I, limited)
- **Valamatos2018** (EJAP 118:1969–1983; within-subject; 15 wk; TUT-equated). Full ROM raised fascicle length (+4.9%) and specific tension. A secondary source says the partial leg gained more PCSA. (I, limited)
- **Pinto2012** (JSCR; PMID 22027847; untrained men, elbow flexors). Full ROM gave larger 1RM gains; muscle thickness rose in both groups. ABSTRACT-level via search snippet.
- **Goto2019** (JSCR 33(5):1286–1294; **n = 44 resistance-trained men**; 8 wk; triceps extension). Partial 45–90° vs full 0–120°, 3×8RM, "equivalent workload".
  - Partial gave larger CSA (+49% vs +28%) and MVC (+40% vs +24%). SECONDARY figures.
  - The partial is a **mid-range** partial, and the authors attribute the result to intramuscular hypoxia (sustained occlusion), not length.
  - **Fact-check:** a 49% CSA gain in 8 weeks in *trained* men is implausibly large next to every other trained study (typically 3–10%). Treat as unreplicated; the measurement method could not be checked. It contradicts "full ROM always wins" and is ignored by most long-length narratives.

### 1b. Lengthened (initial-range) partials vs shortened (final-range) partials vs full

- **Pedrosa2022** (EJSS 22(8):1250–1260; n = 45 untrained women; knee extension; 5 arms). The initial-range (lengthened) partial gave the greatest regional quadriceps growth; 1RM was similar. (I, limited)
- **Pedrosa2023** (Sports 11(2):39; untrained young women; within-subject; 8 wk; preacher curl). The initial range gave greater **distal** biceps growth than the final range, and a larger full-ROM strength gain. ABSTRACT. (I, limited)
- **Kassiano2023a** (JSCR 37(9):1746–1753; **n = 42 untrained young women**; 8 wk; 3×/wk; calf raise). Medial gastrocnemius: initial partial +15.2%, full +7.3%, final partial +6.2%.
  - Initial > final (p < 0.024).
  - **Initial vs full p = 0.060**, i.e. not significant.
  - ABSTRACT.
  - **Cross-check against A6:** A6's audit called A1's "+15.2%" wrong. The abstract-level text found here shows +15.2% for the initial arm. A1's *full* (6.7%) and *final* (3.4%) figures were wrong; A6's 7.3% / 6.2% are right. Flag for the coordinator: A6 over-corrected.
- **Larsen2025a** (Front Psychol 16:1494323; untrained men; 10 wk; within-subject). Failure plus lengthened partials past failure: +9.6% gastrocnemius, vs failure only +6.7%. BF = 13.3. ABSTRACT. A different contrast: extra lengthened work added on top of full-ROM failure, so it is partly a volume/effort contrast. (I, limited)
- **Robinson2023** is cited by Larsen 2025 as finding larger medial gastrocnemius gains with lengthened partials. Not verified; may be the Kassiano trial cited under another name, or a separate study. UNVERIFIED.

### 1c. Same joint ROM, different muscle length via the *other* joint (exercise selection)

This is the cleanest test of "muscle length" and the most cited.

- **Maeo2021** (MSSE 53(4):825–837; n = 20 untrained; 12 wk; 70% 1RM; within-subject; MRI). Seated (hip flexed) vs prone leg curl:
  - whole hamstrings +14% vs +9%
  - biarticular heads +8–24% vs +4–19%
  - monoarticular short head +10% vs +9%
  - ABSTRACT. The null in the monoarticular head is what a length mechanism predicts: its length does not depend on hip angle.
  - A secondary page said "no significant difference for any hamstring muscle"; that contradicts the abstract and is rejected. (I, moderate for untrained)
- **Maeo2023** (EJSS 23(7):1240–1250; n = 21 untrained; 12 wk; 5×10 at 70% 1RM, 2×/wk; MRI). Overhead vs neutral-arm cable elbow extension:
  - long head +28.5% vs +19.6% (p < 0.001; SECONDARY via Stronger by Science and sci-sport, consistent with A6)
  - whole triceps greater with overhead
  - monoarticular lateral+medial heads +14.6% vs +10.5% (per A6), even though shoulder angle does not change their length
  - Absolute loads were lower overhead throughout.
  - **So length cannot be the whole explanation.** Candidates: different relative effort, synergist load sharing, or chance. (I, limited–moderate)
- **ZabaletaKorta2023** (J Hum Kinet 88:259–270; n = 38 *recreationally trained* women; 9 wk). Incline vs preacher curl:
  - The only significant change was the 70% (distal) site in the preacher group (2.70 → 2.94 cm).
  - group × region interaction p = 0.367.
  - Note the ambiguity: the incline curl lengthens biceps at the shoulder, while the preacher curl loads hardest at an extended elbow. "Long length" is defined differently by different authors. ABSTRACT. (I, very limited)
- **Sato2021** (Front Physiol 12:734509). Elbow flexor training at 0–50° (long) vs 80–130° (short), trained and non-trained arm. Thickness results **not retrieved**. UNVERIFIED direction.
- **Stasinaki2018** (J Funct Morphol Kinesiol 3(2):28; triceps long vs short fascicle length; ~10 participants). Per the Varovic preprint, no significant long-head difference. SECONDARY.

### 1d. Isometric training at long vs short length

- **Noorkoiv2014** (MSSE; n = 16 men; 6 wk knee extension). Long length increased volume and CSA; short length gave mainly neural change. Fascicle length rose ~5.4% in both groups. ABSTRACT. (I, limited)
- **Alegre2014** (EJAP; DOI 10.1007/s00421-014-2967-x; 8 wk; 90° vs 50° knee). Muscle thickness rose in both; pennation rose only at long length; fascicle length unchanged. ABSTRACT. Author list inferred from repository links; check.
- **Oranchuk2019** (isometric training systematic review). Long-length isometrics give more hypertrophy and better transfer. Not re-verified this pass; carried from A1 (via A1).

### 1e. Meta-analyses that test "long" directly

| review | k studies (n) | finding | overlap |
|---|---|---|---|
| Wolf2023 IJSC (pre-registered, Bayesian) | 23–24 (sources differ); ~8 with hypertrophy (secondary) | full vs partial SMD 0.12 (−0.02, 0.26); lengthened partial vs full −0.28 (−0.81, 0.16), favouring lengthened, uncertain | includes Pedrosa2022, McMahon2014, Valamatos2018, Goto2019 (likely; list not retrieved) |
| Pallarés2021 SJMSS | 16 | full > partial: strength 0.56, lower-limb hypertrophy 0.88 | heavy overlap with Wolf2023 and Schoenfeld & Grgic 2020 |
| SchoenfeldGrgic2020 | not retrieved | full ROM better for lower body; upper body unclear | subset of the above |
| Kassiano2023b JSCR | 11 (secondary) | full and initial-range partial both beat final-range partial; consider initial-range partials | overlaps all three |
| Ottinger2023 SCJ | narrative | length-tension framework: muscles working on the descending limb benefit more from long ROM | — |
| Varovic2025 IJSM | 12 (Bayesian) | long vs short mean muscle length: regional effects trivial, "practically equivalent" at the typical ~21.8% length contrast | overlaps Wolf2025 SMHS |
| Wolf2025 SMHS | 8 (n ≈ 120, preprint count) | long-length training may increase size and fascicle length more than short-length | overlaps Varovic |
| ZabaletaKorta2020 SCJ | SR (count not retrieved) | regional hypertrophy is real and exercise-dependent | — |

**Do not add these up.** About 15–25 unique human trials sit under all of them, with Pedrosa, Kassiano, McMahon,
Valamatos, Maeo and Goto counted repeatedly.

### 1f. Stretching alone (no resistance)

| source | k studies (n) | finding |
|---|---|---|
| Warneke2024 Sports Med Open (10.1186/s40798-024-00706-8) | 42 (1,318) | static stretching hypertrophy d = 0.20; longer durations, longer interventions and higher frequency give d 0.26–0.28. "Minor effectiveness." |
| Panidi2023 Sports Med Open | 19 (467) | fascicle length up (trivial at rest); muscle thickness not significantly changed overall; high-intensity stretching subgroup increased thickness (p = 0.021) |
| Warneke2023 animal meta | 16 animal studies | stretch induces hypertrophy in animals; transfer to humans limited |
| Nunes2020 narrative review | — | not retrieved; UNVERIFIED (reportedly sceptical) |

**Interpretation:** loaded stretch in humans needs long durations (often 15 min to 1 h/day in the positive trials,
per Warneke's own work, SECONDARY) to produce small effects. The stretch component of a few lengthened reps is
orders of magnitude below that dose. So "stretch-mediated hypertrophy" in the animal sense is very unlikely to be
what lengthened partials do. The better hypothesis is higher *active plus passive* tension at long lengths during
loaded contractions. (M, limited)

---

## 2. Why it might work — mechanism

| claim | code | strength | evidence |
|---|---|---|---|
| Fibres at long lengths sit on the descending limb of the length–tension curve; titin-borne passive force adds to active force, so total fibre tension per unit activation can be higher | M | moderate (physiology), very limited as a hypertrophy cause | Ottinger2023 framework; Warneke2023 review notes **no human study tested the mechanism** |
| Titin acts as a mechanosensor (signalling via its kinase domain) | M/A | limited | not searched this pass; general physiology, UNVERIFIED citation |
| Chronic stretch adds sarcomeres in series (fascicle lengthening) | A strong; I limited | animal: Williams 1988, Alway 1994 (via review); human: fascicle length +5–23% in McMahon, Valamatos, Noorkõiv, Panidi meta | ultrasound fascicle length is extrapolated beyond the probe and error-prone |
| Stretch overload grows muscle massively in birds | A | strong in model | Antonio & Gonyea 1993: quail ALD mass +53.1%, length +26.1%, fibre number unchanged; progressive model up to +318% (protocol details disputed between sources). 24 h/day stretch — not comparable to lifting |
| Distal/regional growth at long lengths (longitudinal growth or local strain) | I | limited | Pedrosa 2022/2023, McMahon 2014, ZabaletaKorta2023, EJSS 2025 elbow; Varovic 2025 pooled says trivial |
| More muscle damage at long lengths drives growth | M | very limited / disputed | Maeo2021 found similar damage *protection*; damage is not a validated hypertrophy driver |
| Partial vs full confounded by sticking point: full-ROM sets in many exercises fail at the short or mid range, so the long region never gets near-failure tension | M | plausible | Larsen2025 rationale; argues for lengthened partials *after* failure, which is a volume/effort intervention |

**Honest mechanism verdict:** "higher mechanical tension at long length" is the most coherent story, and it
predicts the Maeo 2021 head-by-head pattern. It does not explain Maeo 2023's monoarticular heads. The passive-tension
component has no direct human hypertrophy evidence. Fascicle-length gains appear early and may plateau; the
"plateau in trained lifters" is a hypothesis from commentators (Henselmans), not data.

## 3. Trained lifters specifically

| study | n | contrast | result | weight |
|---|---|---|---|---|
| Wolf2025 PeerJ 13:e18904 | 30 trained, within-subject, 8 wk | lengthened partials vs full, upper limb; MT at 45%/55% humerus | similar MT and pulldown 10RM | the best-controlled trained test; null ≠ equivalence; 8 wk; COI: several authors run commercial fitness content |
| Gschneidner preprint (SRXIV.485) | 297 (134 full, 163 LP), 15 sites, 12 wk, low volume 2×/wk | LP vs full | similar estimated CSA and e1RM | large but **not peer-reviewed** and size **estimated** (likely anthropometric); cluster design |
| Larsen2025b EJSS (PMID 40850937) | ~23 trained (secondary count) | initial partial vs full + past-failure partials, calves | +0.40 mm favouring initial; CrI crosses 0; BF 1.2 (anecdotal) | small n; the comparator also included lengthened work |
| "Partial Range, Full Gains?" EJSS 2025 | 13 trained, mostly men | initial partial 0–70° vs full 0–140° preacher curl | similar at 50%; SMD 0.10 at 70% (BF 4.87) | tiny n; trivial effect |
| Goto2019 JSCR | 44 trained men | mid-range partial vs full, triceps | partial **larger** (+49% vs +28% CSA, SECONDARY) | implausible magnitude; not about length |
| ZabaletaKorta2023 | 38 recreationally trained women | incline vs preacher curl | distal site only in preacher; no interaction | weak |

**Verdict:** across four trained-lifter tests of lengthened partials, none shows a meaningful advantage over full
ROM. There is **no** trained-lifter test of the "long vs short exercise" contrast (Maeo-type). The advice "pick the
seated curl and the overhead extension" is an extrapolation from untrained MRI trials. It is cheap and low-risk,
but it is an extrapolation. (I, limited)

## 4. Striking claims fact-checked

| claim | verdict | why |
|---|---|---|
| "Lengthened partials beat full ROM" | **Not supported** | Wolf2023 CI crosses 0; Kassiano initial vs full p = 0.060; all trained tests null or trivial |
| "Training at long lengths doubles growth" | **Misleading** | True only for selected regions or muscles vs *short* partials in untrained samples (Kubo glutes 3×, Kassiano 15.2 vs 6.2, McMahon distal 59 vs 16). Whole-muscle Maeo effects are 1.3–1.5× relative, about 4–9 percentage points |
| "Full ROM is always best" (Pallarés) | **Overstated** | the partials were mostly short; lengthened partials ≈ full |
| "Stretch-mediated hypertrophy makes you grow" | **Animal-strong, human-weak** | birds +53–318% under continuous load (A); human static stretching d = 0.20 with long doses |
| "Overhead triceps grows the long head because it is stretched" | **Partly** | the monoarticular heads also grew more; not purely length |
| Goto 2019 partial +49% vs +28% | **Treat as outlier** | magnitude far above other trained data; unreplicated; mechanism hypoxia, not length |
| A6's correction of Kassiano 2023a "+15.2%" | **A6 over-corrected** | abstract-level text gives initial +15.2%, full +7.3%, final +6.2% |
| Secondary claim "Maeo 2021 found no significant differences" | **Wrong** | the abstract reports greater whole and biarticular volumes seated |

## 5. Open disputes

1. Is the long-length effect a length effect, or an effort/sticking-point effect? This matters because lengthened partials *past failure* (Larsen) add sets' worth of near-failure work.
2. Does the effect vanish with training age? The fascicle-plateau hypothesis is untested; the trained nulls are short (8–12 wk) and underpowered for a ~0.2 SMD.
3. Is muscle thickness at 1–2 sites a valid outcome for a regional question? The Varovic meta says regional effects are trivial; the single-site trials say distal.
4. How should "long length" be defined (joint angle, mean muscle length, peak length, or where peak torque occurs)? Different papers use different definitions, and pooling them (Varovic) dilutes the contrast to ~22%.
5. Wolf 2023 sign convention and study count (23 vs 24): direction agreed (favours lengthened); count unresolved without full text (see A6).

## 6. TENSR — what the band can and cannot track for this factor

| what to track | current board | how | limits | code |
|---|---|---|---|---|
| Rep excursion of the **worn** segment (e.g. thigh in squat/lunge/RDL, upper arm in pulldown/press/fly) | yes, LSM6DSO | gravity-referenced pitch/roll per rep; depth = thigh angle at bottom | yaw drifts (no magnetometer); useless when the worn segment is static (curl, pushdown, leg extension, leg curl) — A4 §joint angle | H |
| "% of your own calibrated range used, and which end" | yes, with calibration | lifter does 2 slow full-ROM reps; the band stores the end orientations; each later rep is scored as the fraction and the location (lengthened half vs shortened half) | only for exercises where the worn segment moves; per-exercise calibration UX | H |
| Joint angle for isolation exercises | needs added part | second IMU tag (BLE) on the distal segment, or the phone camera; then relative orientation gives joint angle | pairing, sync, cost; the board has I2C on J3 for a wired prototype | H |
| Muscle *length* (biarticular, other joint) | no | needs both joints plus a musculoskeletal model | out of scope; a "seated vs prone" tag is cheaper as an exercise label in the app | H |
| Fascicle length / regional thickness | no | A-mode sonomyography (v3 idea) gives thickness at one site, not fascicle length | v3, research | M |

**Product-critical consequence (I, moderate, A2 §dynamic confounds):** sEMG median frequency and amplitude
change with muscle length independent of fatigue (MDF falls as the muscle lengthens). A user who changes ROM between
sets, or does lengthened partials after failure, will shift TENSR's fatigue score with no fatigue change.

- The IMU range measurement above is therefore **needed for the fatigue score itself**: compute MDF in fixed angular windows and flag sets whose range differs from the calibrated one.
- This is a stronger reason to build the ROM tracker than the hypertrophy coaching use.

**Recommended band copy, if any:** "Range used: 92% of your calibrated range, bottom half emphasised" as a
*log*. Never "this set grew more muscle". No target or score for long-length work is evidence-based in trained
lifters.
