# X1 — Physiology of approaching failure, and which signals track it

Agent X1, 2026-11-03. Question 1 of `BRIEF.md`. 32 WebSearches. WebFetch was tried on pmc.ncbi.nlm.nih.gov and paulogentil.com and **both failed with DNS refusal**, so **no full text was read**. Every number below is from an abstract or a search-engine summary of one (ABSTRACT), or from another paper or agent note (SECONDARY). Earlier agent notes (A2, A2-response, A6, F1) are built on, not redone. Study rows are in `X1-studies.csv`; every search is in `X1-searchlog.md`.

Evidence codes are as in PROTOCOL §5: **D** device validation, **I** acute measurement in people, **M** mechanism, **A** acute physiology, **H** hypothesis. Strengths run strong / moderate / limited / very limited.

## 10-line summary

1. **Failure is a mechanical event; proximity is a latent state.** Momentary failure means that despite trying, the current rep cannot be completed (Steele 2017, working definition via Armes 2020). That event is easy to detect: the concentric stalls, ROM is incomplete, the rep is reversed or racked. Estimating *how far away* it is is the hard part. (definition; H for detectability)
2. **What limits a set is mostly peripheral, with a central contribution that is task-dependent.** Peripherally: Pi accumulation and impaired SR Ca²⁺ release; H⁺ is less important than the textbook says (Allen 2008). Near failure, motor-unit discharge rates rise but never reach fresh maximal rates, and at failure sEMG amplitude is *sub-maximal*. That is a drive limit, not just cancellation (Martinez-Valdes 2020; Dideriksen 2011; isometric). (M, moderate)
3. **Velocity and rep duration are the most consistent signals across loads at group level.** % velocity loss maps onto % of possible reps done with R² 0.93–0.97, in a pattern that is nearly load-independent within an exercise (Izquierdo 2006; González-Badillo 2017; Rodríguez-Rosell 2020). The relationship differs by exercise (bench ≠ squat). (I, moderate)
4. **At the individual level, velocity is much weaker than those R²s suggest.** In 46 trained lifters, the % of reps done at a given velocity loss did not agree between two sessions, and individual equations predicted the next session poorly (Jukic 2023). Last-rep velocity had CV > 18% and ICC < 0.60 (García-Ramos 2020). Pooled R² is not individual accuracy. (I, moderate)
5. **No signal has a constant value AT failure.** Last-rep velocity is close to 1RM velocity *on average* (Izquierdo 2006) but is unreliable per person (point 4). MDF at failure depends on load, and even the direction of that dependence conflicts between studies (Jenkins 2015 / Tsoukos 2021 vs Yan 2025). EMG amplitude at failure depends on load: it is lower after light-load sets (Looney 2016), and at 80% 1RM it did not rise at all (Benitez 2023). (I, moderate)
6. **sEMG spectral decline (MDF/MPF) is the most consistent EMG feature.** It fell regardless of load or contraction type in biceps (Benitez 2023), and roughly linearly through the set (Sundstrup 2012). It is *early* (it starts from rep 1) but *linear*: it carries no knee that says "2 left". Its end value and its slope are load-dependent. (I, moderate)
7. **The "amplitude plateau 3–5 reps before failure" is weak evidence for a proximity marker.**
   - Sources: one study, 15 untrained women, elastic-tubing lateral raise, group-mean curve, MVC-normalised (Sundstrup 2012).
   - It was not found at 80% 1RM, where amplitude did not rise at all (Benitez 2023).
   - A plateau can only be called after several flat reps, so live it arrives late.

   Treat it as H for TENSR. (I, limited)
8. **MMG, tremor, NIRS and heart rate are poor proximity signals.**
   - MMG frequency falls like EMG MDF, but MMG amplitude is inconsistent and individual patterns vary widely.
   - Tremor rises with fatigue but peaked 10–15 min *after* the exercise in the one resistance study found.
   - SmO₂ reaches its nadir early in a set, and its fall was not affected by load or velocity loss.
   - Heart rate has no proximity data.

   (I, limited)
9. **Perceived effort is a read-out of central motor command (corollary discharge), not of the muscle.**
   - RPE, EMG and the motor-related cortical potential rise together with load and fatigue (de Morree 2012).
   - That is why the lifter's own effort sense tracks failure approach and is biased at light loads and high reps (Halperin 2022, via F1).
   - The sensor competes against a signal the brain already has. (M, moderate)
10. **For TENSR: earliest = MDF and velocity; most consistent across loads = relative velocity/rep-duration loss; only the failure event itself is near-certain.** A two-way "2 left vs failure now" split is plausible only from the shape of the last reps, meaning a sharp concentric slowdown, a grind in the sticking region and shortened ROM. That is limb IMU territory, with EMG as a secondary, within-set, load-confounded cue. No published dynamic-lifting study has validated an EMG proximity-to-failure estimate. (H)

---

## 1. Definitions — what "failure" means

| term | meaning | source / access |
|---|---|---|
| **Momentary (muscular) failure, MF** | "despite attempting to do so the trainee cannot complete the current repetition". This is a concentric event. | Steele, Fisher, Giessing & Gentil 2017, Muscle Nerve 56:368–374, proposed standard terms. The exact 2017 wording was **not reached**; this wording is the same group's working definition in Armes 2020 (Front Psychol). ABSTRACT/SECONDARY. |
| **Volitional failure / volitional interruption** | The lifter stops by choice. It may be before MF. | Halperin 2022 review (via search summary) lists momentary, volitional and undefined failure as used in studies. SECONDARY. |
| **Repetitions in reserve (RIR)** | How many more reps would have been possible before MF. It is latent: it is only known if the set is then taken to MF. | Zourdos 2016 JSCR 30:267; Steele 2017b PeerJ 5:e4105. ABSTRACT. |
| **Task failure** | The point where the specified task can no longer be done. The limiting mechanism is task-specific. | Enoka 2008/2016 (via A2). SECONDARY. |
| **Performance fatigability vs perceived fatigability** | An objective decline in capacity, as opposed to the sensation of fatigue. | Enoka & Duchateau 2016 (via A2). |
| **Perceived failure ≠ physical failure** | Lifters who perceive MF may still be able to continue. | Fisher, Steele & Smith review (via search summary). SECONDARY. |

**Consequence for TENSR (H).** Three different targets are in play:
- (a) the **MF event**, which is observable by a sensor;
- (b) **RIR**, which is latent and needs a set taken to MF to label it;
- (c) **fatigue**, the loss of capacity.

sEMG spectral change measures part of (c). Velocity loss measures (c) mechanically and correlates with (b) at group level. Only (a) is directly observable. Any validation study must label MF strictly. Volitional stops, and spotter assistance that is not recorded, contaminate the label.

## 2. What limits a set as it approaches failure

### 2.1 Peripheral (inside the muscle)
- **Allen, Lamb & Westerblad 2008, Physiol Rev 88:287–332.** The abstract states that intracellular H⁺/lactate acting on the contractile proteins "is probably of limited importance in mammals". Pi from phosphocreatine breakdown, and reduced SR Ca²⁺ release, are the leading mechanisms. **M, strong** (major review; ABSTRACT).
  - **Fact-check:** the popular "lactic acid causes failure" claim is not supported by this review.
  - Acidosis still matters indirectly, because the sEMG spectral shift is attributed to metabolite effects on sarcolemmal conduction (A2 §1.1). The metabolite that shifts the spectrum is not necessarily the one that stops the rep.
- **Dynamic sets differ from isometric holds.** Velocity loss in a set correlated with post-set lactate (squat r ≈ 0.97, bench ≈ 0.95) and ammonia (R² ≈ 0.85, curvilinear) (Sánchez-Medina & González-Badillo 2011, MSSE 43:1725).
  - **Fact-check:** these figures come from vendor blogs (Vitruve), not the abstract.
  - I believe, but **could not verify**, that the correlations were computed across protocol means, which would make them ecological correlations and not individual prediction. Treat r = 0.97 as an upper bound on what any individual relation could show.
  - **I, moderate (direction) / UNVERIFIED (magnitudes).**
- **Light loads produce more peripheral fatigue by failure.** Benitez/Bergstrom group (JSCR 2023, women): performance fatigability was 41.6 ± 18.6% after reps to failure at 30% 1RM, against 19.7 ± 8.5% at 80%. **I, limited** (ABSTRACT; author list not fully confirmed).
  - Failure is reached at a very different internal state depending on load. That is the root cause of every "value at failure" being load-dependent.

### 2.2 Central (drive)
- **Squat failure vs non-failure.** 12 resistance-trained men did 6 × 10RM squat to failure, against 6 × 5 reps. Peripheral fatigue markers were higher and longer-lasting after failure. Voluntary activation (twitch interpolation) was **comparable** between protocols and stayed depressed up to 48 h. **I, limited** (ABSTRACT; authors not identified, bisp-surf record PU202104002937).
  - Going the last few reps to failure adds peripheral, not central, fatigue in this design.
- **Light load vs heavy load central fatigue.** No peer-reviewed head-to-head was found. A blog (S&C Research) argues that light-load failure carries *more* central fatigue. **Not evidence.**

### 2.3 Motor units near failure
- **Size principle.** Recruitment of progressively higher-threshold units as fatigue sets in at a sub-maximal load is the accepted mechanism (via F1 point 8; Morton 2019, Muddle 2018). **M, moderate.**
- **Rate coding to failure** (isometric, HD-EMG decomposition). Martinez-Valdes, Negro, Falla, Dideriksen, Heckman & Farina 2020, J Neurophysiol 124:1110–1121, DOI 10.1152/jn.00447.2020, vastii:
  - discharge rates **fell until ~40% of endurance time, then rose until task failure**;
  - but at failure they **did not reach** the rates of a fresh 50% MVC.
  - The title is the conclusion: task failure is associated with an *inability to increase neural drive*.

  **M, moderate** (ABSTRACT via listing).
- **The pattern is task-dependent** (Valenčič 2024, J Physiol, isometric). The initial decrease appeared only at 20% MVT sustained. At 30% and 50%, sustained or intermittent, rates stayed stable and then rose continually until failure. **M, limited** (ABSTRACT snippet).
- **Why sEMG amplitude is sub-maximal at failure** (Dideriksen, Enoka & Farina 2011, J Appl Physiol, model). The main determinant is reduced net synaptic input to motoneurons. Amplitude cancellation stays at about **40%** throughout. "EMG amplitude cannot be used as an index of neural drive." **M, moderate** (model; ABSTRACT).
  - This is the most plausible mechanism for an amplitude **plateau** near failure. It also explains why the plateau value is not a fixed "100% recruited" level.
- **Caveat:** all of the decomposition evidence is isometric. Nothing equivalent for dynamic free-weight sets was found. Decomposition is not possible on one bipolar channel.

## 3. Signal by signal, rep by rep to failure (dynamic lifting)

Each row lists what happens across the set, whether the signal is early or late, its load dependence, and whether it has a value at failure.

**sEMG amplitude (RMS/ARV)** — **I, moderate (rise); limited (plateau)**
- **Across the set:** rises, usually curvilinearly.
  - Sundstrup 2012 (n = 15 untrained women, elastic lateral raise): trapezius 86% → 124% MVC, with a **plateau in the final 3–5 reps**.
  - Benitez 2023 (biceps, EJAP 123:2145): EMG amplitude rose at 30% 1RM but **did not change at 80% 1RM**.
  - van den Tillaar 2014 (6RM bench): agonists rose on the ascent.
- **Early or late:** rises early, at light and moderate loads only. A plateau can only be confirmed late, after 2–3 flat reps.
- **Load dependence:** strong. At failure it is *lower* at light loads than at heavy loads (Looney 2016 squat; 2017 leg-extension study via search summary; Jenkins 2015 via A2).
- **Value at failure:** **No.** It is sub-maximal and load-dependent (Dideriksen 2011).

**sEMG MDF/MPF** — **I, moderate**
- **Across the set:** falls roughly linearly (Sundstrup 2012), regardless of load or action type (Benitez 2023). The typical group fall is 20–30% (A2).
- **Early or late:** **earliest**, from rep 1. But it is linear, so it shows no knee near failure.
- **Load dependence:** the size of the fall is load-dependent, and the direction conflicts: larger at light loads (Jenkins 2015, Tsoukos 2021) vs largest at 80% with a fast tempo (Yan 2025).
- **Value at failure:** **No.**

**Spectral-moment ratio FInsm5** — **I, limited**
- **Across the set:** ~8-fold change vs 32% for MDF (Dimitrov 2006, n = 7, via A2).
- **Early or late:** early; more sensitive than MDF.
- **Load dependence:** not tested.
- **Value at failure:** **No** data.

**Mean concentric velocity / velocity loss** — **I, moderate (group); limited (individual)**
- **Across the set:** falls progressively and accelerates at the end. % VL ↔ % reps done: R² 0.97 bench, 0.93 squat (Rodríguez-Rosell 2020, n = 20). Very similar across loads, especially 50–70% (González-Badillo 2017).
- **Early or late:** early (the drop is measurable from about rep 2–3) and most curvilinear near the end.
- **Load dependence:**
  - The *relative* pattern is close to load-independent within an exercise (Izquierdo 2006, 60–75%).
  - Total VL at failure is larger at light loads, because the first rep is faster (Tsoukos 2021; Rodríguez-Rosell 2020).
  - Exercise-dependent: bench drops faster than squat.
- **Value at failure:** Vlast is close to V1RM **on group average** (Izquierdo 2006), but per person CV > 18% and ICC < 0.60 (García-Ramos 2020). Velocities at 2/4/6/8 RIR were "very similar" across loads within an exercise (Morán-Navarro 2019, ABSTRACT). That conflicts with Jukic 2023 (see §4).

**Rep / concentric duration** — **I, moderate**
- **Across the set:** rises as velocity falls ("lower barbell velocities and longer lifting times", van den Tillaar 2014). Concentric fatigue exceeds eccentric fatigue: eccentric speed is preserved (Tsoukos/Bogdanis 2023, PMC10407316, title-level).
- **Early or late:** early and accelerating.
- **Load dependence:** as velocity.
- **Value at failure:** the failed rep itself has a stall.

**Sticking region / ROM** — **I, limited**
- **Across the set:** peak power in the early acceleration phase fell about 55% in the final 2 reps of a 6-rep bench set (2007 study, PubMed 17530976, ABSTRACT).
  - A sticking region was **observable only at 90–100% 1RM** (2021 study).
  - In 6RM squats, only 10 of 15 people showed one.
  - Failure does not always occur in the sticking region.
- **Early or late:** **late** (last 1–2 reps).
- **Load dependence:** strongly load-dependent.
- **Value at failure:** event-level only.

**MMG** — **I, limited**
- **Across the set:** MPF falls (Benitez 2023: regardless of load and action). Amplitude rose in concentric but fell or stayed flat in eccentric.
  - Leg extension at 70% 1RM to failure (n = 11, Bergstrom group): MPF had a negative linear trend, but individual and limb-to-limb patterns varied so much that the authors urged individual reporting.
  - At critical load, MMG MPF fell only at 100% of reps, and amplitude did not change.
- **Early or late:** MPF is early or late depending on the study.
- **Load dependence:** amplitude is action- and load-dependent.
- **Value at failure:** **No.**

**Physiological tremor (8–12 Hz)** — **I, very limited**
- **Across the set:** rises with fatigue. In a resistance protocol (85% 1RM to failure, older study, ABSTRACT) tremor **peaked 10–15 min into recovery**, not in the set.
  - A "98% early vs late fatigue" accelerometer claim is not resistance exercise and was **not verified**.
  - Wrist tremor at 30% 1RM bench predicted EMG (n = 11 untrained).
- **Early or late:** not established within a set.
- **Load dependence:** unknown.
- **Value at failure:** **No.**

**NIRS SmO₂** — **I, limited**
- **Across the set:** falls early, to a nadir.
  - 2025 squat study: the size of the SmO₂ fall was **not influenced by intensity or velocity-loss magnitude**.
  - Acta Bioeng Biomech 2022 (n = 16, VL to failure): short high-intensity sets did **not significantly modify** SmO₂; haemoglobin rose.
- **Early or late:** early, then at a floor.
- **Load dependence:** weakly; heavier loads may desaturate less at matched effort (search summary).
- **Value at failure:** **No.** The floor is reached before failure.

**Heart rate** — **none** (for proximity)
- **Across the set:** rises with time under work. No study related within-set HR to RIR. Post-set sympathetic markers were higher after 80% failure sets (Güngör 2024).
- **Early or late:** lags.
- **Load dependence:** depends on set duration.
- **Value at failure:** **No.**

**RPE / RIR rating** — **I, moderate**
- **Across the set:** rises with load and fatigue, together with motor-command markers (de Morree 2012).
- **Early or late:** continuous. Accuracy depends on proximity and on reps per set (2021 study; direction not confirmed here).
- **Load dependence:** less accurate at light loads and above 12 reps (Halperin 2022, via F1).
- **Value at failure:** RPE 10 by definition, but biased by about 1 rep (Halperin).

### 3.1 Notes on the striking claims

- **"EMG plateaus 3–5 reps before failure, so the plateau marks proximity" — NOT ESTABLISHED.**
  1. It is one group-mean curve, from untrained women, with an elastic band, on one exercise. The authors' own conclusion was about recruitment ("not necessary to go to failure"), not detection.
  2. A group-mean plateau is compatible with individual curves that plateau anywhere, or never.
  3. At heavy loads amplitude may not rise at all (Benitez 2023 at 80%), so there is nothing to plateau.
  4. Normalising to MVC builds in a soft ceiling. Dideriksen 2011 says the ceiling reached at failure is a drive limit and varies.
  5. Live, a plateau is only recognisable 2–3 reps after it begins, which leaves about 0–2 reps of warning.

  **Grade: H for TENSR.**
- **"Velocity loss predicts reps left with R² ≈ 0.97" — TRUE AS REPORTED, MISLEADING AS STATED.** The R² is for pooled group relations of % VL vs % reps completed. Jukic 2023 (n = 46 trained, back squat, 70/80/90%) found that agreement across two sessions was **unacceptable regardless of load**. Individual equations predicted the next session poorly, and the authors call VL "a flawed method" for volume prescription in the free-weight squat. The best individualised velocity RIR model reached only "< 2 reps" mean error (Jukic 2024, via A6).
- **"Last-rep velocity is constant per exercise per person" — PARTLY TRUE ON AVERAGE, NOT RELIABLE INDIVIDUALLY.** Izquierdo 2006 found Vlast ≈ V1RM at group level. García-Ramos 2020 (n = 96, Smith bench) found Vlast between-session CV > 18.3% and ICC < 0.60, with Vlast–V1RM correlations of r = 0.18 (paused) and 0.37 (touch-and-go). A related figure for back squat MVT (CV 22.5%, ICC 0.42) came only from a search summary, unattributed. **The specific "0.17 m/s bench / 0.3 m/s squat" numbers were not found in any reachable source** and should not be quoted.
- **"Lactic acid makes you fail" — NOT SUPPORTED** (Allen 2008).

## 4. Which signals change earliest, and most consistently across loads, people and exercises?

**Earliest.**
1. sEMG MDF/MPF, and MMG MPF. These decline from the first reps, roughly linearly (Sundstrup 2012; Benitez 2023).
2. Mean concentric velocity and rep duration. These decline from about rep 2–3, and the fall steepens near the end (Izquierdo 2006; van den Tillaar 2014).
3. EMG amplitude. It rises early but only at light and moderate loads.
4. Sticking-region and ROM changes, tremor and the failure stall. These appear in the last 1–2 reps or later.

**Most consistent across loads (30–85% 1RM).**
- **Relative velocity loss versus relative reps done** is the only relation reported as nearly load-invariant within an exercise (I, moderate, group level).
- **The direction of the MDF decline** is consistent across loads. Its magnitude is not.
- **EMG amplitude is the least consistent:** it rises at 30%, and is flat at 80% in biceps.

**Across people.** Every signal is weak individually.
- velocity: Jukic 2023, García-Ramos 2020;
- MMG: wide individual and limb differences (Bergstrom group);
- MDF: slope reliability is poor (A2 §3);
- RIR self-report: between-person SD ≈ 1.45 reps (Halperin 2022, via F1).

**Across exercises.** The velocity-loss relation differs between bench and squat (Rodríguez-Rosell 2020). Sticking regions are exercise- and load-specific. EMG depends on muscle and placement (A2 §2). Nothing generalises without per-exercise calibration.

**Load-dependent at failure.**
- MDF at failure (Jenkins 2015; Tsoukos 2021; Yan 2025 in the opposite direction);
- EMG amplitude at failure (Looney 2016; Benitez 2023);
- total % velocity loss at failure (Rodríguez-Rosell 2020);
- peripheral fatigability (Benitez/Bergstrom 2023);
- the existence of a sticking region (90–100% only).

**Any consistent value AT failure?** Only the **mechanical event**: concentric velocity falls to about zero, or the rep is incomplete. That is near-tautological, but it is the one thing a limb IMU can see directly.
- Last-rep mean velocity is the nearest thing to a "failure constant". It holds on average per exercise (Izquierdo 2006), and the velocities at given RIR were reported similar across loads (Morán-Navarro 2019).
- Per-person between-session reliability is poor (García-Ramos 2020; Jukic 2023).

**Verdict: no physiological signal has a consistent value at failure. Mechanical stall is definitional.** (I, moderate)

## 5. What separates "2 reps left" from "failure now"? (H, built from the above)

- Two reps out, velocity has typically fallen a lot but the rep is still completed through full ROM.
- At failure the concentric stalls.

The evidence-supported discriminators are therefore mechanical:
- the size and acceleration of the drop in concentric velocity or rep duration over the last reps (the velocity–reps curve is curvilinear and steepens near the end);
- a grind in the mid-range (sticking-region slowdown, heavy loads only);
- ROM shrinking or a partial rep.

EMG adds, at best:
- a within-set MDF trend (early, load-confounded);
- possibly an amplitude flattening at light and moderate loads.

Neither has been shown to separate 2 RIR from 0 RIR in any dynamic study found. For an IMU on the limb (TENSR's puck), the transfer of bar-velocity findings to segment angular velocity is **untested here**; that is question 3 for another agent.

## 6. Implications for TENSR (H, for the coordinator)

1. **Build the failure *event* detector first.** A concentric stall or an incomplete rep from the puck IMU is the label generator for everything else. It is close to definitional, so high accuracy is plausible, but it still needs validation against video.
2. **The proximity estimate should lead with rep-duration and velocity loss from the IMU, normalised to the set's own best rep.** It must be calibrated per person and per exercise. Expect individual error of ±2 reps or worse (Jukic 2023/2024).
3. **Use sEMG only as a within-set, within-load relative feature** (MDF slope, amplitude-trend shape), and test whether it *adds* to IMU-only. There is no evidence yet that it does. A2-response C17 conditions apply.
4. **Do not ship "plateau = 3 reps left"**, "MDF X Hz = failure", or any fixed threshold. Every candidate threshold is load-dependent.
5. **Validation must vary load (≈30–85% 1RM) within person** and label momentary failure strictly. Otherwise a load-confounded feature will look predictive.
6. **The benchmark** is the lifter's own RIR call, raw and bias-corrected (Halperin 2022; A6 C1). Effort perception is a direct read-out of motor command (de Morree 2012), so the sensor competes against a signal the brain already has. Expect to win mainly at light loads and in high-rep sets, where self-report is worst.

## Access and limits
- Fetch was blocked (pmc.ncbi.nlm.nih.gov and paulogentil.com: DNS refusal). Everything is ABSTRACT or SECONDARY.
- Unverified: the Steele 2017 exact definitions, the Sánchez-Medina 2011 magnitudes and correlation unit, the author list of the squat VA study, the Morán-Navarro 2019 author list and exercise list, the 0.17/0.3 m/s MVT values, the squat MVT CV 22.5% source, and the tremor "98%" claim.
- Isometric mechanism studies (Martinez-Valdes, Valenčič, Dideriksen) may not transfer to dynamic sets.
