# TENSR — scientific foundation report

2026-11-02. Synthesis of six research agents (A1 training outcomes, A2 sEMG and fatigue, A3 wearable sensing and
signal processing, A4 product translation, A5 validation design, A6 independent evidence auditor), reconciled after
the audit and the agents' responses.

**What this report is.** A map of what the literature supports, what TENSR's actual hardware can measure, and where
the two meet. **What it is not.** It is not full-text-verified. This environment blocked every full-text and DOI
route, so every source was seen at abstract level or through other papers (see `SEARCH-LOG.md`). Nothing here was
tested on a built TENSR board; none exists yet.

**Companion files:**
- `PROTOCOL.md` — registered before searching.
- `STUDY-EVIDENCE-TABLE.csv` — 169 studies, with audit verdicts.
- `TENSR-FEATURE-EVIDENCE-MATRIX.csv`
- `CLAIM-VERIFICATION.md` — the brief's claims, citation corrections, open disagreements.
- `TENSR-VALIDATION-PLAN.md`
- `OPEN-QUESTIONS.md`
- `agent-notes/` — every agent's full findings, studies, searches, scripts and responses.

**Evidence codes:**
- **D** — direct: comparable hardware and dynamic lifting.
- **I** — indirect human evidence.
- **M** — mechanistic.
- **A** — animal.
- **H** — product hypothesis.

Strength runs strong / moderate / limited / very limited / none.

---

## 1. What TENSR actually is (confirmed from the repo, not the brief)

| | Fact | Consequence |
|---|---|---|
| EMG | ADS1292R, **one channel** (CH2 tied off) | One muscle, one location. No left/right, agonist/antagonist or regional comparison from one band. |
| Electrodes | Three 7 mm stainless snap studs, dry. **Bipolar pair E1–E3, 25.4 mm** along the board's 44 mm axis. E2 is the driven reference, 22.6 mm off-axis, on the same muscle. | IED exceeds SENIAM's 20 mm. Orientation relative to the fibres is set by how the puck sits on the band, **which nothing records.** E2 is equidistant (25.92 mm) from E1 and E3, so activity under it is common mode. Its real risk is losing contact. |
| Input network | 200 kΩ per arm + 100 pF C0G; C27 4.7 nF across the PGA | Analogue corner far above the EMG band. |
| Sampling | **Inconsistent in the docs:** 500 SPS at bring-up; 1–2 kHz in the firmware brief; 20–450 Hz in the analysis brief | The sinc3 decimation filter is −3 dB at **0.262 × data rate**: 131 Hz at 500 SPS, 524 Hz at 2 kSPS (TI SBAS502C, verified). **500 SPS cannot represent a 20–450 Hz band.** |
| Motion | LSM6DSO 6-axis IMU on the puck, no magnetometer | Segment pitch/roll of the limb the band is on. Not bar velocity, not joint angle (needs a second segment), yaw drifts. |
| Not present | Load input, force sensor, bar sensor, second segment, heart rate | No direct measure of force, tension, load, velocity of the implement, or whole-body state. |
| Status | Designed and routed, never built; no firmware; no recorded EMG | Every TENSR-specific statement below is **H** until measured. |

---

## 2. Measurement definitions — the twelve constructs kept apart

| Construct | Physiological concept | Research-setting direct measure | What TENSR records | What could potentially be inferred | Assumptions and confounders | Calibration | Confidence and validation needed |
|---|---|---|---|---|---|---|---|
| **Muscle electrical activity** | Summed motor-unit action potentials in the detection volume | Gel bipolar sEMG at a SENIAM site, IED ≤ 20 mm, aligned to fibres; HD-EMG; intramuscular EMG | Differential E1–E3 voltage, one channel | Burst timing; relative amplitude and spectrum within one wear | Dry-contact impedance and sweat drift; crosstalk (25.4 mm IED); orientation unknown; fat thickness; innervation-zone position | Rest baseline per wear | **Measured** once built. Quality unknown until bench and Stage 2–3. |
| **Muscle force / joint torque** | Force the muscle produces; moment about the joint | Dynamometer, force plate, load cell, inverse dynamics | Nothing direct | At most an isometric, per-wear EMG–force curve | EMG–force is nonlinear, muscle- and velocity-specific; fatigue raises EMG at constant force; cancellation (Keenan 2005) | Multi-level contractions against known loads, every wear | **Not measured.** Research-only [I, limited]. |
| **Mechanical tension** | Active + passive force borne by fibres — the leading hypertrophy stimulus (M) | Not directly measurable in vivo; force × moment-arm models; elastography | Nothing | Nothing | Passive tension at long lengths produces no EMG at all | — | **Not measurable** with this hardware. |
| **Muscle length / stretch** | Fascicle / muscle-tendon length; excursion at long lengths | Ultrasound fascicle imaging; motion capture + musculoskeletal model | One segment's orientation | Segment ROM on exercises where the worn segment moves | Joint angle needs two segments; muscle length needs a model; yaw drift; belly bulge tilts the puck | Per exercise, assuming the other segment is static | **Not measured.** A ROM proxy is research-only. A-mode sonomyography (v3 idea) is the only route to thickness. |
| **Contraction duration / tempo** | Time per concentric and eccentric phase | Video, encoder, motion capture | EMG burst on/off; IMU angular velocity | Rep duration (all exercises); phase split (moving-segment exercises) | Threshold choice; static-segment exercises; low eccentric EMG | Per-exercise templates | **Inferable after validation** [I, moderate for rep duration]. |
| **Time under tension** | Duration the muscle produces force under load | Force or position trace plus load | EMG-active duration; IMU motion duration | "Set duration" / "active time" | Electrical activity ≠ tension (lockouts, eccentrics) | Per exercise | **Duration only.** The word "tension" is unsupported. |
| **Local muscular fatigue** | Reduced force or power capacity of this muscle (peripheral + central) | Pre/post MVC, twitch interpolation, power loss; sEMG spectral compression in controlled contractions | MDF/MNF and amplitude per rep window | **Within-set relative** spectral compression — a peripheral electrophysiological marker, not capacity loss | Joint angle, innervation-zone shift (up to 16 mm in biceps), load, tempo (mixed), temperature, contact quality; data rate; MDF misses type I fatigue | Baseline reps of the same set; phase-locked windows | **Inferable after substantial validation** as a post-set trend only [I/M, moderate direction; H on TENSR]. |
| **Whole-person fatigue** | Systemic / central fatigue, readiness | Questionnaires, CMJ, MVC batteries, HRV, blood markers | Nothing relevant | Nothing | One peripheral channel cannot see systemic state | — | **Unsupported.** Do not imply it. |
| **Proximity to failure / RIR** | Reps remaining before concentric failure at this load | Observed reps to failure; individualised velocity–RIR equations | EMG features + limb IMU; no load or bar data | Possibly an individual, per-exercise nearer/further estimate | Load-, exercise- and person-dependent; self-report bias ~0.95 reps, SD ~1.45 | Several calibration sets per user and exercise (velocity precedent) | **Research-only** [H, none for sEMG in dynamic lifting]. |
| **Contraction velocity / velocity loss** | Speed of the implement or limb; its decline over a set | Linear position transducer, optical, force plate | Segment angular velocity where the worn segment moves | Segment velocity loss on compound lifts with a moving instrumented segment | Segment ≠ bar. Limb-worn devices validate poorly against transducers (Orange 2019, PUSH). Nothing on static segments. | Per exercise | **After substantial validation**, restricted exercise list [I, limited]. |
| **Recovery between sets** | Restoration of force and power capacity | Repeat-set performance; MVC or power probes | Elapsed time; EMG only if a probe contraction is made | Time since set end; spectral recovery of a probe | Spectral and force recovery dissociate, direction inconsistent (Mills 1982) | Probe contraction per muscle | Timer: **measured**. "Recovery": **research-only** [I, limited]. |
| **Hypertrophy stimulus / long-term growth** | Anabolic signalling → CSA or volume change over weeks | MRI or ultrasound over weeks; biopsy | Nothing about growth | Counts of sets and reps on the instrumented muscle | Acute EMG ≠ growth (Plotkin 2023; load studies) | — | **Unsupported** as a score; **contradicted** as an EMG-derived stimulus. |

**Can EMG amplitude support claims about force, tension, contraction quality or growth in customer conditions?**
**No.**
- Amplitude is net neural drive minus cancellation, filtered by tissue and electrode geometry (Vigotsky 2018;
  Keenan 2005).
- It rises with fatigue at constant force, with load, with speed and with effort, and plateaus near failure
  (Sundstrup 2012).
- It varies ~41–43% between sessions even on a reference system (Colyer 2018).
- It needs a per-wear reference contraction to mean anything across time (Burden 2010; Besomi 2020).
- Higher acute amplitude did not mean more growth in the only direct test (Plotkin 2023), and heavier loads raise
  amplitude without raising growth (Schoenfeld 2017a; Lopez 2021; Morton 2016).

Within one set, on one wear, it is a relative trend at most, and with dry electrodes even that needs a reference
comparison before it reaches a user.

---

## 3. The target questions, answered directly

**Q1. Is there a defensible "optimal fatigue level" for hypertrophy?** **No.**
- No study defines or measures one.
- Fatigue in this literature is defined many ways: velocity loss %, reps lost, MVC decline, RPE, metabolite
  accumulation. None is a sEMG spectral index tied to an outcome.
- Where fatigue was manipulated while effort and end-point were held, growth did not follow fatigue:
  - cluster sets: less fatigue, same growth (Davies 2021);
  - supersets: more internal load, same growth (Zhang 2025);
  - drop sets: similar growth (Sødal 2023; Coleman 2022);
  - failure vs 1–2 RIR: more velocity loss, same quadriceps growth (Refalo 2024).
- The best counter-example is Pareja-Blanco 2017: 40% vs 20% velocity loss gave more vastus hypertrophy, at a cost
  in jump performance, with 40% more reps (n ≈ 22).
- Fatigue is best read as a **by-product** of effortful tension that becomes a cost at the extremes [I/M, moderate].

**Q2. Does greater local fatigue predict greater growth?** **Not demonstrated, and it can rise without benefit.**
See Q1. The metabolite-stress hypothesis lacks direct support (Dankel 2017, M).

**Q3. Can wearable EMG identify a useful point to stop a set? Has it been validated?** **No.**
- No study was found validating sEMG-based RIR, failure prediction or stop-point detection during dynamic free-weight
  training with subject-independent testing and error in reps.
- The nearest is an isometric biceps model (Garofalo 2026, n = 12) and an IMU + EMG RPE preprint in which EMG added
  little over the IMU (Thomas & Wahlström 2025).
- MDF at failure is load-dependent, and even the direction of the load effect differs between studies (Tsoukos 2021
  vs Yan 2025), so no fixed stop value exists.
- With realistic estimator noise (~9 Hz per rep), the MDF slope becomes statistically visible only around rep 8 of
  10, by which point the lifter is already near the stop.
- **The bar is high:**
  - lifters' own RIR has mean bias ~0.95 reps and SD ~1.45 (Halperin 2022), roughly 1.2–1.4 reps MAE by our
    estimate;
  - accuracy is best near failure;
  - the best objective method, individualised bar-velocity models, reaches only <2 reps error (Jukic 2024).

**Q4. Is there an optimal TUT per rep, set or session?** **No.**
- Repetition duration 0.5–8 s gives similar hypertrophy (Schoenfeld 2015, 8 studies); only >10 s/rep looks inferior.
- Lacerda 2021 (n = 10) found no difference between 2 s and 6 s reps to failure.
- Once load, ROM, rep count and proximity to failure are separated, TUT has no independent dose-response in the
  evidence.
- Within that tempo range, the load and the proximity to failure carry the effect.

**Q5. Can TENSR measure mechanical TUT?** **No.** It records the duration of electrical activity and of segment
motion. Electrical activity is not tension: there is passive tension with no EMG, and EMG with little tension near
lockout. Call it **set duration**.

**Q6. Can a "contraction rating" be physiologically meaningful?** **Not as proposed.**
- It would have to represent something — amplitude relative to a reference contraction, ROM consistency, phase timing
  — and each of those is either an amplitude claim (confounded, needs per-wear normalisation) or an IMU kinematic
  claim (moving-segment exercises only).
- It would fail to capture tension, muscle length, load, and whether the rep contributed to growth.
- Strict vs momentum reps gave similar growth in the one trial (Augustin 2025, untrained, 8 weeks).
- The only defensible fragment is a narrow, descriptive IMU flag for **ROM shrinking within a set** on moving-segment
  lifts [H].

**Q7. Can the band estimate recovery well enough to recommend starting another set?** **No.**
- Spectral recovery and force recovery follow different time courses, and the direction differs across paradigms
  (Mills 1982: force half-recovered ~30 s, MPF ~3 min).
- No trial tests EMG-guided rest.
- The outcome literature already gives a usable default: ≥ 60–90 s, little extra growth beyond ~90 s (Singer 2024);
  longer (2–3 min) supports strength and volume (Schoenfeld 2016).
- An **elapsed-time timer with those defaults** is defensible. A "recovered" signal is not.

**Q8. Are personalised within-person trends more defensible than universal thresholds?** **Yes — by a wide margin,
but they are not automatically valid.**
- Every spectral and amplitude feature depends on person, muscle, placement and load.
- The velocity literature shows individual models beat general equations (Jukic 2024; García-Ramos 2018).
- But a within-person trend still needs to be shown reproducible after the band is taken off and put back
  (validation S2-b) and to agree with a reference (S3-a).

**Q9. Can readings be compared across days, muscles, exercises or users?**

| Comparison | Answer | Why |
|---|---|---|
| Raw amplitude across days | **No** | ~42% between-session CV even on the reference system (Colyer 2018) |
| Normalised amplitude across days | Only with a same-session reference contraction, and it is unproven on dry studs | Burden 2010; Besomi 2020 |
| Absolute MDF across days | Unproven; needs S2-a | Between-day MDF reliability ranges from poor to excellent; slopes are worst |
| Within-set relative MDF slope across days | Possibly, if S2-b passes | It is the most portable quantity |
| Across muscles, exercises or loads | **No** | MDF and amplitude depend on joint angle, load and muscle; at-failure MDF is load-dependent |
| Across users | **No** | Fat thickness alone explains 21–33% of amplitude variance (trapezius, Nordander 2003); absolute Hz is not transferable |

**Q10. What evidence would justify a percentage score? When is it false precision?**
- A percentage implies a defined 0% and 100% and an error small relative to the range.
- It would need:
  1. a construct with a reference measurement;
  2. a known maximum (e.g. MVC, measured each wear);
  3. MDC well below the displayed resolution;
  4. agreement with the reference in dynamic lifting.
- None of the proposed percentages ("activation %", "fatigue %", "set effectiveness %") meets (1)–(4).
- A per-rep MDF expressed as "% of fresh" would have an estimator noise of roughly ±8% (9 Hz on ~110 Hz) per rep
  before any physiological variation. Displaying integers would be false precision.
- **Use descriptive feedback instead:** counts, durations, and, after validation, a post-set direction-of-change
  statement with a confidence band.

**If no defensible universal optimum exists, what is appropriate?**
- Descriptive logs: reps, sets, durations, weekly set counts.
- Evidence-based defaults that are labelled as defaults: rest ≥ 90 s; a 0–3 RIR effort range that the **user**
  judges.
- Later, personalised trends shown with uncertainty, never as a target to chase.

---

## 4. Training science, connected to TENSR

Each topic gives the outcome research first, then whether TENSR could tell the conditions apart. Full detail is in
`agent-notes/A1-findings.md`.

| Topic | What the outcome research supports | Could TENSR distinguish it or give useful feedback? |
|---|---|---|
| **Mechanical tension vs TUT** | Tension is the leading stimulus hypothesis (M; Wackerhage 2019, much of it animal and in-vitro). TUT has no independent dose-response (Schoenfeld 2015) [I, moderate]. | Neither. Duration yes, tension no. |
| **Long muscle lengths / stretch-mediated hypertrophy** | Training at long lengths looks favourable, mostly in untrained people over 8–12 weeks. Maeo 2021 hamstrings +14% vs +9%; Maeo 2023 triceps long head +28.5% vs +19.6%; Pedrosa 2022; Kassiano 2023a calf (medial +15.2% initial-range vs +6.7% full). Wolf 2025 (trained): no difference [I, limited–moderate]. Depends on the angle of the other joint. | Barely. One segment's orientation, not a joint angle. Hip or shoulder position (overhead vs pushdown) is invisible. Possible only with an exercise label. |
| **Full ROM vs lengthened/shortened partials** | Short-length partials are probably inferior. Lengthened partials are roughly equal to full ROM: Wolf 2023 −0.28, CI −0.81 to 0.16, favouring lengthened, uncertain. Full ROM beats unspecified partials for strength and lower-limb growth (Pallarés 2021) [I, moderate for avoiding short partials; limited otherwise]. | Plausibly detects **ROM shrinkage within a set** on moving-segment lifts [H]. Cannot tell lengthened from shortened partials without a joint-angle reference. |
| **Concentric, eccentric, isometric** | All build muscle. Eccentric 10.0% vs concentric 6.8%, not significant (Schoenfeld 2017c). Long-length isometrics may transfer better (Oranchuk 2019) [I, moderate that all work]. | Phase split only when the instrumented segment moves. Isometrics defeat IMU rep counting; EMG becomes the only signal. |
| **Tempo, pauses, peak-contraction squeezing** | Tempo 0.5–8 s/rep is equivalent. **No longitudinal trial** of pauses or peak squeezing; inter-set flexing helped mid-thigh thickness in one small trial (Schoenfeld 2020) [none to very limited]. | IMU detects pauses easily. Nothing to score them against. EMG amplitude during a squeeze would rise and reward it with no outcome basis — a risk, not a feature. |
| **Strict vs momentum; heavy cheat then strict isolation** | Momentum vs strict: similar growth, more volume load (Augustin 2025; one untrained trial; content-creator co-authors). Cheat-then-strict sequencing: **no trial** [I, very limited]. | Momentum is plausibly detectable (jerk, trunk swing). A "form penalty" has no outcome justification. Safety framing is outside this review and would brush against TGA injury language. |
| **Compound vs isolation** | Adding isolation to compound work did not add elbow-flexor growth in untrained men (Gentil 2013). Barbalho-group trials were excluded over retractions [I, limited]. | One band sees one muscle. Compound lifts feed other muscles fractionally (Pelland 2026). |
| **Machines, free weights, cables, stability** | Free weights vs machines: similar hypertrophy, SMD −0.055 (−0.397 to 0.287) (Haugen 2023). Strength is modality-specific. Cables and unstable surfaces **not assessed** [I, moderate for equivalence]. | Not usefully. Stability changes co-contraction and amplitude, but higher amplitude is not more growth. |
| **Load and rep ranges** | Hypertrophy is similar from ~30% to >80% 1RM when sets are effortful (Schoenfeld 2017a; Lopez 2021, 28 studies). Heavier is better for 1RM [I, strong]. | **This is why amplitude cannot be a stimulus score.** Heavy loads give more EMG, not more growth. TENSR does not know the load. |
| **Volume** | Graded dose-response with diminishing returns for growth, sharper plateau for strength. Weekly sets per muscle is the best dose metric (Schoenfeld 2017b; Pelland 2026, exact estimates not retrieved) [I, moderate]. No individual optimum. | Counts sets for the instrumented muscle. "Hard set" needs effort, which needs RIR: use user tags. |
| **Frequency** | No hypertrophy effect when volume-equated (Schoenfeld 2019); effects for strength (Pelland 2026) [I, moderate]. | Logging, not sensing. |
| **Proximity to failure** | Growth improves modestly and non-linearly closer to failure; 0–3 RIR captures most of it in trained lifters (Refalo 2023, 2024; Grgic 2022 trained ES 0.15, 0.03–0.26; Robinson 2024). Failure matters more at light loads (Lasevicius 2022; Robinson load moderation). Strength is insensitive [I, moderate]. | The feature with the most outcome relevance and the highest bar. TENSR would need to beat bias-corrected self-report. **Unvalidated.** |
| **Rest intervals** | >60–90 s is enough for growth; little gain beyond ~90 s (Singer 2024). 3 min > 1 min in trained men for strength and some sites (Schoenfeld 2016) [I, limited–moderate]. | Elapsed-time timer with these defaults. "Recovered" detection: no. |
| **Progression** | Not specifically reviewed beyond load and volume. Users progress by load or reps at a given effort. | TENSR has no load input. Progression must come from logged load (user entry). |
| **Supersets, drop sets, rest-pause, cluster sets** | Time and fatigue tools, not growth levers. Supersets SMD −0.05 (Zhang 2025); drop sets ES 0.08 (Coleman 2022); cluster sets equal with less fatigue (Davies 2021). Rest-pause: unverified [I, moderate]. | Detecting a drop set is plausible from EMG/IMU continuity. A fatigue score that rises in drop sets would be physiologically correct but **not** evidence of more growth. The brief's drop-set validation criterion is invalid (CLAIM-VERIFICATION claim 17). |
| **Muscle-specific and regional hypertrophy** | Real and exercise-dependent (Maeo 2021, 2023; Pedrosa 2022; Plotkin 2023). Mostly single-site ultrasound in untrained people [I, moderate that it exists; limited for prescriptions]. | **No.** A 25.4 mm bipolar pair samples one region; moving the band changes what it sees. |

**The rule this table enforces:** the exercise or condition producing the largest EMG signal is not assumed to
produce the most growth. Where it was tested, it did not (Plotkin 2023; the load literature).

---

## 5. Surface EMG in dynamic resistance exercise

Full detail in `agent-notes/A2-findings.md` and `A3-findings.md`.

### 5.1 Fatigue features

**MDF/MNF.**
- They fall as conduction velocity slows with metabolite accumulation (M, strong for direction).
- In dynamic sets to failure, the typical relative fall is ~20–30%:
  - Jenkins 2015: last reps at 71.6% of baseline MPF at 30% load vs 78.1% at 80%;
  - Dimitrov 2006: up to 32%.
- These are group-level results from lab gel systems [I, moderate].

**Other indices.**
- **FInsm5 (Dimitrov's spectral-moment ratio)** is more sensitive (~8-fold change vs 32% for MDF; n = 7, rectus
  femoris).
- **Wavelet indices** do not clearly beat it.
- **Amplitude + spectral combinations** explain ~47–50% of variance in power loss (González-Izal 2010b, figures from
  the 2009 working paper).
- **IEMG/RMS** rises, but is not specific.

**Interpretability under changing conditions — the central weakness.**
- In fresh muscle, MDF moves with joint angle, muscle length, contraction velocity and innervation-zone position
  (Potvin 1997; Doud 1995; MacIsaac 2001; Nishihara 2013: IZ shift 3.9–16 mm in biceps).
- Tempo effects are mixed (Sakamoto 2012 vs Yan 2025).
- Load changes the at-failure value.
- **Consequences:**
  - windows must be **phase-locked** (same joint-angle segment each rep, using the IMU);
  - comparisons must stay **within one exercise and load**;
  - the output is a **relative trend**.

**What the signals can and cannot separate.**
- MDF compression is a peripheral, largely type II, metabolic marker. It misses type I fatigue (Gerdle 1992).
- It does not measure central fatigue, task failure, or declining performance.
- Performance can decline while the spectrum is stable, and the reverse.

### 5.2 Electrodes and placement (SENIAM, CEDE)

**SENIAM (Hermens 2000).**
- IED 20 mm.
- Electrode ≤ 10 mm (confirmed only secondarily).
- Aligned with the fibres.
- Between the innervation zone and the distal tendon.
- Reference electrode on electrically inactive tissue.
- Skin preparation.
- Its consensus concerns Ag/AgCl gel; it says nothing about dry electrodes.

**CEDE.**
- Besomi 2019: a larger IED increases detection volume and crosstalk.
- Besomi 2020 normalisation matrix: task-specific MVC, standardised isometric MVC, a **standardised submaximal
  reference** (the most practical for TENSR), task peak/mean, non-normalised, or M-wave.

**TENSR against these.**

| Item | Status |
|---|---|
| Electrode size (7 mm) | Passes |
| IED (25.4 mm) | Fails |
| Orientation | Uncontrolled |
| Innervation-zone position | Uncontrolled |
| Skin preparation | Uncontrolled |
| Normalisation | Absent |
| Reference on active muscle | Acceptable by symmetry; contact loss is the risk |

The 25.4 mm IED shifts absolute MDF but leaves the relative trend essentially unchanged in simulation (−25.4% vs
−25.0%), **if** the pair is aligned and stable. One fixed geometry for seven muscles of very different size is the
main validity limit, worst for deltoid heads, calf heads and (possibly) pectoralis.

### 5.3 Dry electrodes, skin and the band

- The best dry/textile validations agree with research systems on MVC-normalised amplitude, with ~11–14% within-session
  CV (Lynn 2018 Athos, n = 12, isokinetic, company-affiliated; Colyer 2018 textile, n = 16).
- Timing and agreement degrade at high effort.
- **Between-session amplitude CV is ~42% even on the reference.**
- **No dry or wearable system has validated spectral variables.**
- Searle & Kirkup's "dry as good as wet" required buffered, shielded electrodes, which TENSR lacks.
- Sweat lowers impedance over minutes and mimics an amplitude trend.
- Fat thickness attenuates amplitude (trapezius, Nordander 2003).
- Hair and band pressure change contact.
- Snap-on gel electrodes are the largest available lever.

### 5.4 Acquisition and processing

**Sampling.**
- At 500 SPS, a true MDF of 120 Hz reads ~86 Hz, and a −25% drop reads −16 to −18% (−21 to −24% with inverse-sinc
  compensation, at ~4× noise near 250 Hz).
- At 2 kSPS, 116 Hz and −24% (A3 and A6 models across five spectral shapes).
- **Recommendation: 2 kSPS (DR = 100).** It costs nothing in hardware and keeps comparability with the literature.

**Filtering.**
- 20 Hz high-pass for motion artefact (De Luca 2010 convention).
- 50 Hz handling (notch or adaptive) must be tested for its effect on MDF.
- Filter choice and window length change onset times and MDF estimates, so they are fixed before validation and
  applied identically to the reference.

**Window length.**
- Estimator SD ~9.3 Hz at 0.5 s and ~4.7 Hz at 2 s on an ideal stationary signal; reps are ~0.5–2 s.
- Per-rep MDF is therefore noisy, and single-rep decisions are not supportable.

**Artefacts.**
- Motion artefact (< 20 Hz), electrode movement, mains, clipping, BLE dropout, crosstalk (one channel cannot reject
  it).
- Poor contact adds mains and motion energy that **lowers** MDF in the same direction as fatigue, so MDF is only
  more specific than amplitude behind a quality gate.

**Signal quality: when to withhold.**
- Lead-off on any electrode (including E2).
- Clipping.
- 50 Hz ratio above threshold.
- Low-frequency energy above threshold.
- Baseline-noise trend.
- Too few clean reps for a slope.
- Any of these gives **"no reading"**, never a guessed number. Thresholds are engineering targets set on the bench
  (S1.11).

**IMU.**
- Improves rep segmentation (validated for wrist/forearm), phase-locking of EMG windows, and artefact rejection
  (motion spikes).
- Does not provide bar velocity (PUSH vs GymAware: valid only in narrow load ranges, Orange 2019).
- Belly-worn and upper-arm placement are untested.

**Latency.**
- Compute features on the puck and send one per-rep record.
- About 0.3–0.6 s after the rep ends is realistic for a haptic cue.
- But the MDF trend is not reliable until late in the set, so a responsive live MDF cue would be an unreliable one.
  The trade-off resolves to **post-set summary**.

### 5.5 Other methods measure different constructs

| Method | What it measures | Relation to TENSR's EMG |
|---|---|---|
| Force / dynamometry | Output force or torque; MVC decline = capacity loss | The reference for "fatigue" as lost capacity. EMG does not measure it. |
| Bar-velocity tracking | Implement velocity; velocity loss ~ proximity to failure (Sánchez-Medina 2011, group level) | Strongest practical fatigue proxy; individualised models <2 reps RIR error. TENSR's IMU is not a bar sensor. |
| Mechanomyography | Mechanical vibration of contracting fibres | Different construct; possible from a high-rate accelerometer. Research-only, not reviewed. |
| NIRS | Local oxygenation / deoxygenation | Metabolic state, not electrical; not reviewed in depth. |

None is a universal ground truth; each is the reference for its own construct.

---

## 6. Algorithms and machine learning — critical assessment

A3 reviewed 10 studies; A6 audited a subset (`agent-notes/A3-findings.md` Task 7; `A6-audit.md`).

| Check | What the field shows |
|---|---|
| Target definition and labelling | Usually subjective (RPE, Borg) or time-segment labels ("first third = fresh"). Rarely true reps to failure. |
| Reliability of the target | Self-report targets carry bias ~0.95 reps, SD ~1.45; not reported as a limitation in most studies. |
| New people / sessions / exercises | Mostly trial-level or record-wise splits. Leave-one-subject-out is rare. Electrode re-application is never tested. New-exercise testing is essentially absent. |
| Window-overlap leakage | Overlapping windows across train and test splits are common where splits are record-wise. |
| Calibration | Per-user calibration usually implicit; rarely reported as a requirement. |
| Participants and conditions | n ≈ 10–32; mostly isometric or lab tasks; few free-weight sessions. |
| Error vs accuracy | Accuracy or R² reported; error in reps rare; uncertainty rarely given. |
| External validation | None found. |
| Simple baselines | When reported, the gain is modest: CNN RMSE 20.8% vs linear regression 26.9%. Kinematics alone predicted effort well; eccentric rep time was the top predictor (Thomas & Wahlström 2025, preprint). A load cell alone was within ±1 RPE in a high share of sets (Baek 2025; figure not confirmed). |

**Conclusion.** High classification accuracy in small controlled experiments does not show that a consumer band can
coach arbitrary exercises. The validation plan's Stage 4 requires:
- leave-one-subject-out and new-session testing, with the band re-applied;
- reps-to-failure labels;
- error in reps with clustered CIs;
- calibration plots;
- beating IMU-only and bias-corrected self-report baselines.

---

## 7. Adversarial audit — summary

The auditor verified every load-bearing citation plus a seeded random sample of 15 (60 of 169 rows audited).

- **No citation was fabricated.**
- Errors found:
  - three misapplications (Rodríguez-Rosell 2021, Orange 2022, one-sided Zhao 2025);
  - one wrong description (Colyer 2018's reference electrodes);
  - one withdrawn sentence with no source (lumbar "pH/force dissociation");
  - several number-level corrections.
- Nine reasoning leaps were caught and accepted. The most consequential:
  1. self-report bias read as accuracy;
  2. per-rep MDF targets below the physical floor of spectral estimation;
  3. "a trend after 4–6 reps" when the arithmetic says ~8 of 10;
  4. failure-vs-3-RIR separation achieved by rep count alone.
- Ten disagreements remain open and are preserved in `CLAIM-VERIFICATION.md` §4. None changes a feature
  recommendation.

**Per-feature audit verdicts** (eight questions each) are in `agent-notes/A6-audit.md` §3 and are reflected in the
matrix. The questions that most often failed:
- "is the threshold evidence-based?" — never, for any proposed threshold;
- "does it generalise beyond the original participants and exercise?" — no published basis for any EMG feature;
- "could feedback encourage unnecessary fatigue?" — yes, for any RIR cue, set score, rising-amplitude display or
  falling-MDF display.

---

## 8. Feature recommendations (summary of the matrix)

| Feature | Recommendation |
|---|---|
| Rep counting and timing | **Suitable to prototype** |
| Elapsed-time rest timer (≥ 90 s default; 2–3 min heavy compound) | **Suitable to prototype**, no "recovered" wording |
| Weekly set counts for the instrumented muscle, user-tagged effort | **Suitable to prototype** |
| Set duration (in place of TUT) | **Suitable to prototype** as plain duration |
| Within-set spectral fatigue trend | **Potentially useful after substantial validation**: post-set, descriptive, SQI-gated, ≥ 1–2 kSPS, dropped if it does not beat IMU-only |
| Eccentric/concentric split | **Potentially useful after substantial validation**: moving-segment lifts only, logged |
| Relative amplitude trend | **Research-only / internal** until Stage 3 |
| Live RIR / proximity to failure | **Research-only** |
| Set score ("reached failure") | **Research-only** |
| Muscle-driven recovery estimate | **Research-only** |
| Left/right comparison | **Research-only**; needs two bands |
| Activation % | **Unsupported or misleading** |
| Technique / contraction quality | **Unsupported or misleading** |
| TUT as "tension" | **Unsupported or misleading**; rename to set duration |
| Hypertrophy / set-effectiveness / stimulus score | **Unsupported or misleading — contradicted. Do not build.** |

---

## 9. Validation programme (summary)

Five stages, each gating the next. Full detail with labelled criteria is in `TENSR-VALIDATION-PLAN.md`.

1. **Bench.** Known-MDF synthetic EMG through the full chain. **Data rate decided here.** SQI fault injection and
   electrical-safety limits before any human contact.
2. **Repeatability.** Within session, doff/don and between days. ICC(A,1) with CI, SEM, MDC95, repeated-measures
   Bland–Altman. The key new gate is **slope reproducibility after re-application.**
3. **Agreement.** Adjacent SENIAM gel reference at ≥ 2 kHz, two-reference-pair floor, both orientations,
   single-joint and compound lifts, TOST equivalence. Muscles that fail are dropped.
4. **Prediction.** True reps to failure (sets continued to failure); leave-one-subject-out; matched-rep comparisons.
   **Must beat bias-corrected self-report and IMU-only.**
5. **Benefit.** Acute crossover with a safety gate on over-reaching, then an RCT only if Stages 4 and 5a pass.

**Sample sizes** are planned from the claim and required precision. Worked examples are in the plan; there is no
universal n.

**Ethics.** HREC (likely higher-risk), screening, nickel and skin checks, IEC 60601-1 BF limits as internal targets,
Privacy Act, TGA wellness boundary, independent analysis of the held-out set.

---

## 10. Final answers

**1. What can our existing band realistically measure?**
- The electrical activity of one region of one muscle, as a single bipolar dry-electrode channel. Quality is unknown
  until built.
- The orientation and motion of the limb segment it sits on.
- From those, once validated: rep and set counts, rep and set duration, rest time, and weekly set counts for that
  muscle.

That is the measured layer. Nothing about force, tension, load, muscle length, growth or whole-body state.

**2. What can it estimate only after validation?**
- A **post-set, within-person spectral fatigue trend**: a peripheral electrophysiological marker, for one exercise
  at one load. It needs 2 kSPS, a quality gate, known electrode orientation, and Stage 2–4 evidence that it is
  reproducible, agrees with a reference, and adds information beyond the IMU.
- **Eccentric/concentric timing and within-set ROM shrinkage**, on exercises where the worn segment moves.
- A within-set amplitude trend, if Stage 3 shows it is not driven by impedance drift.

Live reps-in-reserve and recovery readiness are research questions, not validation tasks yet.

**3. Can we justify optimal fatigue, time-under-tension or contraction targets?** **No.**
- The outcome literature has no optimum for any of them.
- Fatigue varies without growth following it.
- Tempo is equivalent across 0.5–8 s per rep.
- "Contraction quality" has no defined construct.

Defensible alternatives: logged descriptions; evidence-based defaults labelled as defaults (rest ≥ 90 s; 0–3 RIR
judged by the lifter, closer to failure for light loads); and, later, personal trends with uncertainty.

**4. Which three features offer the strongest combination of usefulness and scientific defensibility?**
1. **Automatic rep and set counting with set duration.** It is the most mature sensing (IMU ±1 rep in ~91–93% of sets
   at the wrist) and the foundation for everything else.
2. **Weekly set count per instrumented muscle, with user-tagged effort.** It tracks the best-supported dose variable
   in the hypertrophy literature (weekly sets per muscle) without inventing a stimulus score.
3. **Elapsed-time rest timer with evidence-based defaults**, auto-started at set end. It is simple, actionable and
   backed by rest-interval meta-analysis.

The within-set spectral fatigue trend is the fourth candidate. It is the only feature that uses what makes TENSR
different from an IMU band, but it must earn its place in Stage 4 by beating the IMU-only baseline.

**5. Which appealing claims should we avoid?**
- "Optimal fatigue", "optimal TUT", "contraction rating", any **percentage score**.
- **"Activation %"** as proof the muscle is "doing the work".
- Any **hypertrophy, stimulus or set-effectiveness score** — contradicted.
- **Live "about 2 reps left"**.
- **"Rest timer driven by your muscle's recovery" / "ready for the next set"**.
- **"Did this set reach failure" as a score**, which rewards a target the evidence does not support.
- **"120 Hz → 90 Hz"** or any absolute Hz.
- **"Tempo-independent"** and **"beats velocity-based training"**.
- **"Time under tension"** (call it set duration).
- **Left/right imbalance** on one band; "imbalance" also drifts toward injury language.
- **"Logs your whole split automatically"**.
- Anything about injury, rehab, recovery as health, or readiness (TGA wellness boundary).

**6. What are the most important experiments before giving training recommendations?**
1. **Bench test at 500 SPS vs 2 kSPS** with known-MDF synthetic EMG through the real chain (S1.3), plus SQI fault
   injection and electrical safety.
2. **Electrode orientation and agreement study:** TENSR vs an adjacent SENIAM gel pair, both orientations, per muscle,
   in real lifts, judged against the two-reference-pair floor (S3-a/b/g).
3. **Re-application repeatability of the within-set MDF slope** (S2-b). If a user cannot take the band off and get the
   same slope back, no trend feature survives.
4. **Matched-rep reps-to-failure study** with sets continued to failure, leave-one-subject-out, against bias-corrected
   self-report and IMU-only baselines (R4.1–R4.5). This decides whether EMG adds anything a cheaper IMU band could not.
5. **Only then, an acute feedback crossover** with a safety gate on over-reaching (S5.1), before any outcome trial.
