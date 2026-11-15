# A2 findings — surface EMG and fatigue during dynamic resistance exercise

Agent A2, 2026-11-02. Evidence codes and strengths per PROTOCOL.md §5. Citation keys refer to `A2-studies.csv`.

**Access caveat that governs everything below.** DOI resolvers, PubMed, PMC, Crossref and publisher sites were all blocked from this environment (proxy 403 / DNS refusal). Only a web search engine worked. **No paper here was read in full text**; every number comes from an abstract, an abstract-level search summary, a repository record or another paper's citation, and is marked that way in the CSV. Where a DOI was seen only from memory and not confirmed by any reachable source, it is marked UNVERIFIED. The shared search budget ran out before the last three verification searches; they are listed in the search log as not run.

---

## Summary (10 lines)

1. **"MDF drops ~120 Hz fresh to ~90 Hz cooked" — UNSUPPORTED as stated.** MDF does fall during sets to failure (I, moderate), but the absolute values depend on muscle, electrode spacing, placement relative to the innervation zone, subcutaneous fat, load and joint angle; no source gives a universal start or end value, and the one biceps figure found was ~77–79 Hz *mean* frequency, isometric. On TENSR's planned 500 SPS bring-up rate a 120 Hz MDF would sit near the ADS1292R's own filter roll-off (H, to be checked by A3).
2. **"Tempo-independent" — CONTRADICTED / at best partly true.** One bench-press study found the MDF drop similar across four speeds (Sakamoto2012), another found fast tempo amplified the MDF decline (Yan2025), and fresh-state spectra shift with joint angle, muscle length and contraction velocity independent of fatigue (Potvin1997, Doud1995, MacIsaac2001). Neither study supports a tempo-free threshold.
3. **"Amplitude rises with fatigue" — SUPPORTED (I, moderate) but not specific:** it rises with load, velocity and effort as well, plateaus near failure, and is limited by amplitude cancellation, so a rise is not a fatigue-only signal.
4. **"The two together are the fatigue score" — PLAUSIBLE BUT UNVALIDATED (H).** Amplitude plus spectral features explain only about **half** the variance in power loss across dynamic sets (GonzalezIzal2010b, R² ≈ 0.47–0.50, n = 15). That is a group-level fit, not an individual score.
5. **Rep-of-failure — NO VALIDATED sEMG METHOD found for dynamic lifting.** MDF at failure is load-dependent: the last reps reached ~72% of baseline MPF at 30% 1RM against ~78% at 80% 1RM (Jenkins2015). There is no consistent failure value.
6. **Live RIR ("about 2 left") — NO EVIDENCE.** No peer-reviewed dynamic-lifting study that predicts RIR from sEMG was found. The closest is isometric (Garofalo2026, n = 12) or RPE-from-IMU+EMG, where EMG added little (arXiv2025, preprint). Humans miss by about 1 rep on average (Halperin2022), which is the baseline TENSR must beat.
7. **Set score (did it reach failure) — NOT SUPPORTED** for the same reason as 5: a single-channel spectral or amplitude value cannot tell "failure at a light load" from "3 short at a heavy load".
8. **Activation % — CONTRADICTED as a meaningful number without a reference contraction.** It needs MVC (or other) normalisation, which is itself variable. Amplitude is not force, not "tension" and not hypertrophy stimulus (Vigotsky2018, Morton2019, Keenan2005, Burden2010).
9. **Recovery-driven rest timer — CONTRADICTED as a performance-readiness measure.** MDF recovers within about 1–6 min and dissociates from force and pH recovery (lumbar and elbow-flexor data). "Spectrum back to baseline" does not mean "ready to perform".
10. **What survives:** within-set *relative* MDF/MNF decline and amplitude rise, within one person, one muscle, one exercise, one load, as a **trend** (I, moderate). Anything stated as a threshold, a universal Hz value, a rep count or a percentage is H and needs TENSR's own validation.

---

## 1. What the fatigue indices are and why they move

### 1.1 Spectral compression: the mechanism is real

Under sustained or repeated effort, muscle fibre conduction velocity (CV) falls, motor-unit action potentials lengthen, and the sEMG power spectrum shifts to lower frequencies. Reviews attribute this mostly to metabolite (H⁺/lactate) accumulation acting on the sarcolemma (Cifrek2009 — ABSTRACT; Brody1991 — SECONDARY, citation only; Dimitrova2003 — SECONDARY). Mean and median frequency (MNF/MDF) are the classical indices. **M, strong** for the direction of the effect under sustained isometric conditions.

Two important qualifications come from the same mechanistic literature:

- **CV is not the only driver.** Dimitrova & Dimitrov's review "Interpretation of EMG changes with fatigue: facts, pitfalls, and fallacies" (Dimitrova2003, JEK 13:13–36) argues that the shape of the intracellular action potential, not only CV, shapes the spectrum, and that ratios of spectral moments are more sensitive than MDF. Only the citation could be confirmed here; the content is SECONDARY via Dimitrov2006 and its users. **M, moderate.**
- **The MDF shift is a peripheral, metabolic marker.** It is not a measure of central fatigue or of task failure (Enoka2008, Enoka2016). See §4.

### 1.2 Indices proposed for dynamic work

- **MDF/MNF from short windows (STFT).** These were used in essentially every dynamic study below.
- **Time-frequency instantaneous MNF/MDF** (Cohen-class and wavelet distributions). These were developed because dynamic EMG is non-stationary: Bonato2001 (cyclic dynamic contractions, IEEE TBME 48:745–753; citation only) and Molinari 2006 (isokinetic; seen as preprint title only).
- **Dimitrov's FInsm5 spectral-moment ratio.** In 7 adults doing 10×15 knee extensions at 50% 1RM, the maximal change in FInsm5 was about **8-fold** against **32%** for MDF, with fair-to-good ICCs for both (Dimitrov2006, ABSTRACT). This is more sensitive, but it is n = 7, one muscle and metronome-paced, so it does not show tempo robustness.
- **Wavelet indices.** In 15 trained men doing 5×10 leg press with 2 min rest, wavelet indices explained **46.6%** of the variance in power change, and log-FInsm5 plus mean average voltage explained **49.8%** (GonzalezIzal2010b, ABSTRACT). A companion paper found linear and neural-network mappings equally good at estimating peak-power change (GonzalezIzal2010c). In biceps work the wavelet indices did not beat FInsm5 (a secondary mention).
- **JASA (joint analysis of spectrum and amplitude).** This is described in the reviews (Cifrek2009, GonzalezIzal2012), but no dynamic-resistance validation was found within this search.

**Verdict on indices (I, moderate).** In dynamic lab conditions, spectral-moment ratios and wavelet indices track group-level power loss *somewhat* better than MDF alone. Even so, the best published combinations leave about **half the variance unexplained**, in trained subjects on a fixed machine with a fixed load and tempo. That is the ceiling TENSR is working under, with fewer controls.

---

## 2. Dynamic contractions: what changes the spectrum other than fatigue

This is the core problem for a free-weight band, and the literature is consistent about it: **in dynamic work, MDF moves with joint angle, muscle length, force, velocity and electrode-to-innervation-zone geometry, and these effects are of the same order as the fatigue effect.**

- **Muscle length / joint angle.** MNF and MDF fall as the muscle lengthens. This is well reported in biceps; Doud1995 is cited for it, and a 2015 review sentence states it generally. Potvin1997 recorded biceps in 15 men doing repeated elbow flexion-extension with 7 kg to exhaustion and analysed amplitude and MPF against joint kinematics. It is cited as the explanation for MNF rising as the muscle shortens, and it found concentric aEMG ~10% MVC higher than eccentric in the rested state (ABSTRACT fragments). **I, moderate.**
- **Innervation-zone shift.** In biceps, the IZ moves under the skin as the elbow angle changes (MartinMacIsaac2006, citation). In continuous dynamic contraction the shift averaged **3.9 mm at acute angles but 16 mm at obtuse angles** (Nishihara2013, ABSTRACT). An IZ under or near the electrodes lowers amplitude and *raises* MNF (vastus medialis, secondary). With TENSR's 25.4 mm bipolar pair on a band that is not placed relative to a located IZ, a 16 mm IZ excursion means the IZ can cross the detection volume *within each rep*. **M/I, moderate.**
- **Force/load.** MPF has been reported to rise with contraction force, depending on fibre type and electrode spacing (secondary). Load also changes the *size* of the fatigue-related drop (§3). **I, moderate.**
- **Velocity.** No study was found that cleanly isolates contraction velocity's effect on fresh-state MDF in free-weight lifting. That is a gap, not a reassurance. MacIsaac2001 (biceps, conference paper) reported that conduction velocity may be more resilient than MNF to joint angle and force, but that estimates fail at extreme shortening. Farina2006's review (ESSR 34:121–127) concludes that dynamic-task EMG needs cautious interpretation; one secondary source says that, at that time, the only confirmed dynamic application was timing of muscle activation. **I/M, moderate** that dynamic confounds are large; **none** for a quantified velocity correction.
- **Electrode geometry.** Simulation work reports that increasing inter-electrode distance (IED) raises ARV and MDF, while fibre inclination lowers both (2023 simulation, ABSTRACT). An EJAP study compared IEDs of 10–50 mm on the vasti. Bipolar spacing acts as a spatial comb filter whose notch frequencies depend on IED/CV, which is textbook M. TENSR's 25.4 mm is longer than common 20 mm practice; A3 owns this question, but it bears directly on spectral fatigue indices: **an MDF read through a 25 mm bipolar filter is not comparable to published MDF values from other spacings.**
- **Fat.** In one isometric biceps sample, subcutaneous tissue thickness correlated with lower amplitude and frequency (r = −0.362), with MPF ~79 Hz (men) and ~77 Hz (women) (conference abstract, SECONDARY). **I, limited.** Values from different people are therefore not interchangeable.

**Practical consequence (H).** A per-rep MDF from a free-weight lift is a mixture of fatigue, the joint-angle trajectory of that rep, the load and the IZ position. Any TENSR method needs, at minimum: (a) windows locked to the same phase and joint angle of each rep, which the IMU can approximate; (b) comparison only within a set and against the same person's own first reps; (c) no comparison of absolute Hz across people, muscles or placements.

---

## 3. Magnitude of MDF decline across a set to failure, and whether there is a value "at failure"

| study | task | n | spectral change | load/tempo dependence |
|---|---|---|---|---|
| Jenkins2015 | leg extension, 3 sets to failure, 80 vs 30% 1RM | 18 (9M/9F) | MPF fell across reps in both; last reps **71.6% vs 78.1% of MVIC MPF** (30% vs 80%) | larger decline at light load |
| Sakamoto2012 | bench press to fatigue, 40–80% 1RM × 4 speeds | 13 trained men | MDF similar across conditions *before* fatigue; post-fatigue drop similar across speeds | larger drop at lighter loads |
| Tsoukos2021 | bench press, max intended velocity, to failure at 40/60/80% 1RM | 14 men | MDF decline greater at 40 and 60% than 80% (p < 0.05) | load-dependent; velocity loss also load-dependent |
| Yan2025 | bench press 60 vs 80% 1RM × fast (X/0/X/0) vs 2/0/2/0 tempo | 10 bodybuilders | largest MDF decline at 80% + fast tempo | load × tempo interaction |
| Dimitrov2006 | knee extension 10×15 at 50% 1RM | 7 | max ΔMDF **32%**; FInsm5 ~8-fold | metronome-paced; not tested |
| Sundstrup2012 | lateral raise, 3RM vs ~15RM to failure, elastic tubing | 15 untrained women | MPF fell steadily through the failure set; normalised EMG amplitude rose (trapezius 86% → 124% MVC) and **plateaued in the last 3–5 reps** | — |
| Walker2012 | leg press 15×1RM vs 5×10RM | 13 untrained men | EMG amplitude and MDF assessed throughout; hypertrophic protocol → more peripheral fatigue (secondary) | protocol-dependent |
| Tsoukos2024 | bench press, repeated sets, full vs partial ROM | — | sEMG amplitude rose and MDF fell in all muscles; fatigue tracked velocity more than force loss | ROM-dependent (detail not reached) |

All access is ABSTRACT or SECONDARY; no SDs or individual data could be extracted.

**Findings.**

- **Direction.** MDF/MNF falls across a set to failure in dynamic lifts. This is consistent in every study found. **I/D (lab, wired sEMG, dynamic lifting), moderate.**
- **Magnitude.** The typical *group-mean* decline is about **20–30% of baseline** (Jenkins2015's ~22–28%, Dimitrov2006's 32% maximum). The CLAUDE.md figure of 120 → 90 Hz is a 25% fall and is in this range, so the *proportion* is plausible. The absolute numbers are not sourced anywhere in this search, and the ~77–79 Hz biceps MPF baseline found suggests that "120 Hz fresh" is high for a typical bipolar biceps recording. That depends on IED, fat, muscle and filter; **H, unverified.**
- **No consistent value at failure.** Every multi-load study found that the spectral decline at failure **depends on load**: lighter loads to failure produce *larger* MDF falls (Jenkins2015, Sakamoto2012, Tsoukos2021), and tempo interacts with load (Yan2025). So there is **no fixed MDF, or fixed % drop, that marks failure**, even within one exercise in one person, once the load changes. **I, moderate.**
- **Between-subject variability.** No dynamic study's individual-level spread could be extracted. Reliability work shows that *initial* or normalised MDF values are moderately to highly reliable (elbow flexors at 75% 1RM: MF ICC 0.90–0.98, between days), but MDF **slopes** are the least reliable fatigue measure. In isometric quadriceps at 80% MVC, slopes had "a large degree of variability and low ICCs", and neck-muscle MF slope had between-day ICC 0.28–0.61 (secondary summaries; primary authors not confirmed). **I, limited–moderate.** This matters directly: a "fatigue per rep" score is a slope.

---

## 4. Peripheral fatigue, central fatigue, task failure and performance decline

- **Definitions.** Fatigue is a decline in maximal force or power capacity, and the mechanisms are **task-specific** (Enoka2008). Enoka2016 separates *performance fatigability* (objective decline) from *perceived fatigability*. Task failure is the point where the task can no longer be done, and its limiting mechanism varies by task.
- **What sEMG sees.** Spectral compression reflects peripheral, mainly metabolic, change at the sarcolemma. Amplitude reflects the net of recruitment, rate coding, cancellation and peripheral changes. Neither separates central from peripheral fatigue; that needs evoked responses (twitch interpolation, M-waves), which TENSR cannot deliver. **M, strong.**
- **Dissociations.** In Walker2012's design, central versus peripheral contributions differed by loading protocol (secondary). MDF recovers on a different time course from force and pH (§7). Velocity loss relates to metabolic markers (Sánchez-Medina2011: velocity loss correlated with lactate and ammonia; exact coefficients seen only in secondary summaries). One bench study concluded that fatigue tracked velocity loss more than force loss (Tsoukos2024).
- **Implication.** "Fatigue score" in CLAUDE.md conflates at least three constructs: peripheral electrophysiological change (what MDF sees), loss of capacity (what velocity or force sees) and proximity to task failure (what RIR means). sEMG measures the first directly; the other two only indirectly, at group level. **I, moderate.**

---

## 5. Amplitude, force and "activation %"

- **Amplitude is not force.** The sEMG–force relation has "no simple closed-form" description. Amplitude depends on muscle length, contraction velocity and contraction type, and **fatigue biases the amplitude–force relation** (Disselhorst-Klug 2009 and the 2020 follow-up, ABSTRACT; Dideriksen simulation, secondary). **I/M, strong.**
- **Amplitude cancellation.** Summing MUAPs before rectification loses amplitude. Simulated cancellation reaches **62% at maximal activation**, and up to **85%** when MUAP amplitude ranges narrow as they can with fatigue (Keenan2005, ABSTRACT). Farina2014's update puts cancellation first among the limits on reading amplitude as neural drive. **M, strong.**
- **Amplitude rises at constant force as fatigue develops.** Additional motor units are recruited to hold force, with mixed rate-coding evidence (secondary). So, as CLAUDE.md says, amplitude does rise with fatigue, but it also rises with load (Schoenfeld2014, Jenkins2015), with faster velocity (Sakamoto2012) and with effort, and it can **plateau** in the last reps (Sundstrup2012). A rising RMS is not specific to fatigue. **I, moderate.**
- **Amplitude is not hypertrophy stimulus.** Comparative amplitude studies are frequently over-interpreted as predicting strength or hypertrophy (Vigotsky2018). Directly: in Morton2019, **sEMG amplitude was not related to fibre glycogen depletion or anabolic signalling**, while those two were related to each other, and fibre-level depletion did not differ by load when sets went to failure. Schoenfeld2014 (n = 10 trained men, leg press 75% vs 30% 1RM to failure: mean EMG 63.7 ± 37.2 vs 41.6 ± 28.0) and Jenkins2015 found higher amplitude at heavy loads. That is an acute EMG difference, and **is not evidence of differential growth** (SHARED-STANDARDS rule 4). **I, strong** that amplitude ≠ growth stimulus.
- **"Activation %" needs a denominator, and every denominator has problems.** Burden2010's review of eight normalisation methods endorses isometric MVC as the reference, but says "neither [isometric nor dynamic MVC] is guaranteed to reveal how active a muscle is in relation to its maximal activation capacity". Task-peak or task-mean normalisation reduces between-subject variability but removes the very comparison an activation score claims to make. In cycling, a submaximal dynamic reference (ICC 0.87) beat MVC (0.66) for repeatability (secondary). For TENSR this means:
  - an un-normalised "activation %" is meaningless across sessions (electrode-skin impedance, placement and sweat all change raw µV);
  - an MVC-normalised one requires a reliable MVC per muscle per session, which a gym user will not perform consistently;
  - normalising to the set's own peak makes "100%" a tautology.

  **Activation % as a cross-muscle or cross-session number: contradicted. Within-set relative amplitude: I, moderate.**
- **Crosstalk.** It is named in Farina2004 as the worked example of a measurement error that distorts conclusions. A single bipolar pair at 25.4 mm IED on small muscles (biceps/brachialis, the deltoid heads) will pick up neighbours; "is the target muscle doing the work" cannot be separated from crosstalk with one channel. **M, strong** that this is a risk; quantification is A3's job.

---

## 6. Predicting RIR, failure or velocity loss from sEMG

- **No validated study of sEMG-based RIR prediction in dynamic resistance exercise was found** in two extended searches. **Evidence: none** (absence after a reasonable but not exhaustive search, limited by access).
- **Closest direct attempts.**
  - Garofalo2026 (JEK, DOI 10.1016/j.jelekin.2026.103111): deep learning on sEMG spectrograms for **isometric** biceps holds to failure, 12 participants, 192 recordings, leave-one-out cross-validation (whether by subject is not stated in the abstract). The best LSTM had MSE **49.44 ± 18.34**. The units are not given in the abstract; if they are squared percent of time-to-failure, that is an RMSE of ~7%, but this is UNVERIFIED. A secondary site's "87% accuracy" could not be confirmed. **I, very limited**: isometric, small, not reps.
  - arXiv 2510.03197 (preprint): RPE from IMU + EMG during dumbbell curls, 69 sets / 1003 reps, trained 18–25-year-olds. **Adding EMG only slightly improved accuracy over inertial sensors alone, and eccentric rep time was the strongest predictor.** That is a direct warning that TENSR's IMU may carry more of the useful information than its EMG. **D, very limited; preprint, not to be used as sole support.**
  - A 2026 basketball pilot with participant-level LOSO got only **0.68–0.70** accuracy for classical EMG fatigue classifiers, "markedly lower than usual published values". This is the expected collapse once subject leakage is removed. **I, very limited.**
- **EMG versus velocity loss.**
  - Tsoukos2021 measured both in the same sets: MDF decline and velocity loss were both larger at lighter loads. Co-variation at group level is shown; no individual-level agreement statistic was found.
  - In Rodríguez-Rosell2021 (8-week squat training at 10/30/45% velocity loss, n = 33), **no significant EMG changes** were seen in any group, while performance outcomes differed. EMG was insensitive to a training manipulation that velocity tracked.
  - GonzalezIzal2010b/c: EMG features explain ~50% of power-loss variance, group-level.

  **I, limited.** No study reports limits of agreement between an EMG index and velocity loss or RIR.
- **The bar to clear.** People underpredict reps to failure by **0.95 reps (95% CI 0.17–1.73)**, I² = 97.9%, across 12 studies and 414 participants, and are more accurate closer to failure (Halperin2022). Velocity-based methods are the established objective alternative (Sánchez-Medina2011). A TENSR RIR feature has to beat a lifter's own guess and a velocity-loss rule, with agreement statistics, in held-out subjects. Nothing published shows sEMG can.

---

## 7. Recovery between sets

- **MDF recovers fast.** It recovered within 1–6 min after lumbar fatigue, with a "clear dissociation" from the recovery of intracellular pH and force-generating capacity. Elbow-flexor spectral recovery was rapid then plateaued at 2–5 min. After biceps resistance exercise, most EMG variables, MDF included, were back near reference by **1 min**. Vasti MNF and CV can overshoot to **supernormal** values at 20 min. After eccentric exercise MDF recovered in 2 days, then fell again at 7 days. (All ABSTRACT/SECONDARY; primary authors are not confirmed for every item, see CSV.) **I, moderate** that spectral recovery is fast and dissociates from force.
- **Performance recovers more slowly and over longer.** Bar velocity in the 4th set relative to the 1st depends strongly on rest interval (30 s to 5 min, secondary). Force recovery is biphasic, with a fast ~2 min phase and a slow phase lasting tens of minutes (secondary).
- **Verdict (I, moderate).** A rest timer that ends when the spectrum has recovered will end early, before performance capacity has returned, and the spectral signal will have recovered by the time the set-to-set performance difference still exists. "Recovery driven by the muscle's own recovery" is therefore **contradicted** as a readiness measure. It could be offered as a measured *minimum* (H).

---

## 8. Other sensing constructs (for context; not on TENSR)

- **Bar velocity / velocity loss.** This is a mechanical performance output, related at group level to metabolic stress (Sánchez-Medina2011), and the leading objective proximity-to-failure proxy. TENSR's IMU is on the limb segment, not the bar; A3/A4 own whether segment velocity substitutes.
- **Force/dynamometry.** This is the reference for fatigue as capacity loss (Enoka2008). TENSR has none.
- **MMG.** It is generated by muscle mechanical activity during dynamic actions, and is affected by torque, muscle length and tissue thickness (Beck2005). In fatiguing isokinetic work MMG amplitude tracked torque more closely than EMG did (dissertation, SECONDARY). It is a different construct: mechanical, not electrical.
- **NIRS.** It measures local O₂ saturation, which falls during strength protocols (pre ~68–78%, post ~10–46%; only 4 eligible studies) (MirandaFuentes2021). It is a metabolic/perfusion construct and does not need skin-electrode contact quality, but it does need a stable optical coupling.

None of these is interchangeable with sEMG MDF; each measures a different link in the chain from drive to output.

---

## 9. Transfer to TENSR's hardware (rule 8)

Each item is **H** unless marked otherwise.

1. **One bipolar channel at 25.4 mm IED, dry, on a band.** Every study above used gelled, wired, lab electrodes placed by SENIAM-type rules relative to the muscle. None used a 25.4 mm band-mounted dry pair. Spectral values are spacing- and contact-dependent (§2). Directness: low.
2. **Sampling.** PROTOCOL §1 records 500 SPS for bring-up. Published dynamic MDF work uses ≥1 kHz and 10/20–450/500 Hz bands. At 500 SPS the usable band ends below 250 Hz, and the ADS1292R's decimation filter rolls off below that (exact −3 dB point to be confirmed by A3 against the datasheet; not verified here). A spectrum truncated near 130–250 Hz will give a biased MDF. A "120 Hz fresh" value read through such a filter is not interpretable. **Highest-priority hardware question for any spectral feature.**
3. **No load, bar-velocity or joint-angle input.** Load changes the MDF-at-failure relation (§3), and TENSR does not know the load. The IMU can phase-lock windows, but cannot supply load.
4. **Arbitrary exercises and muscles.** The evidence is per muscle and per task. Nothing transfers a threshold from bench press to curls to calf raises.
5. **Uncontrolled gym.** Motion artefact, sweat, band migration and band pressure changes will move impedance and placement between and within sets. Reliability evidence (§3) is from lab re-application and is already weak for slopes.

---

## 10. Verdicts on the CLAUDE.md claims

| claim | verdict | code / strength | key support |
|---|---|---|---|
| MDF drops ~120 Hz → ~90 Hz | **Unsupported as absolute values.** A ~20–30% relative fall is typical; the Hz values are not universal and are likely high for bipolar biceps. | I moderate (relative); H (absolute) | Jenkins2015, Dimitrov2006, biceps MPF abstract |
| "tempo-independent" | **Contradicted / not established.** Mixed (Sakamoto2012 vs Yan2025), and dynamic confounds (length, angle, IZ shift) are not tempo-free. | I moderate | Sakamoto2012, Yan2025, Potvin1997, Nishihara2013, Farina2006 |
| "why this beats velocity-based training" | **Unsupported.** No head-to-head; EMG insensitive where velocity was not (Rodríguez-Rosell2021); IMU > EMG for RPE (preprint). | I limited | Rodríguez-Rosell2021, arXiv2025, Sánchez-Medina2011 |
| amplitude rises with fatigue | **Supported, non-specific.** It also rises with load, speed and effort, and plateaus near failure. | I moderate | Sundstrup2012, Jenkins2015, Keenan2005 |
| MDF + amplitude = fatigue score | **Plausible, unvalidated.** ~50% of variance in power loss at group level. | I limited; H as a score | GonzalezIzal2010b/c, GonzalezIzal2012 |
| rep-of-failure | **Unsupported.** No fixed spectral value at failure; it is load-dependent. | I moderate (against) | Jenkins2015, Tsoukos2021, Sakamoto2012 |
| live RIR "about 2 left" | **No evidence.** No dynamic validation found; humans ±~1 rep is the bar. | none / H | Halperin2022, Garofalo2026 |
| set score (reached failure?) | **Unsupported**, as rep-of-failure. | H | as above |
| rest timer from muscle recovery | **Contradicted** as readiness. Spectral recovery is faster than, and dissociated from, force recovery. | I moderate | MDF-recovery studies, §7 |
| activation % | **Contradicted** without valid normalisation; amplitude ≠ force/tension/stimulus. | I strong | Burden2010, Vigotsky2018, Morton2019, Keenan2005 |

## 11. What TENSR would need to show (handed to A5)

1. On its own hardware, at its real sample rate: within-set MDF decline in a phase-locked window, compared against a gelled 20 mm reference pair on the same muscle. This answers whether TENSR sees the same physiology.
2. For each muscle and exercise: the per-person distribution of MDF/amplitude change at failure across at least 3 loads, to quantify the load dependence found in Jenkins2015/Tsoukos2021 on TENSR's own data.
3. RIR/failure prediction tested on **held-out subjects**, reported as mean error and limits of agreement in reps, against two baselines: the lifter's own RIR estimate (Halperin2022) and an IMU-only model (arXiv2025).
4. Between-day reliability (ICC, SEM, MDC) of the per-rep slope after band re-application.
5. The rest timer tested against set-to-set performance (reps achieved, or segment velocity), not against spectral recovery.
