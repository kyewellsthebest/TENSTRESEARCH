# Claim verification — TENSR

2026-11-02. This file records what the independent auditor (A6) checked, what it found, how the other agents
responded, and which disagreements remain open. Source files: `agent-notes/A6-audit.md` and
`agent-notes/A1…A5-response.md`. Where a response differs from the agent's original findings, the response wins.

**Access caveat.** No source was read in full text (see `SEARCH-LOG.md`). "Verified" means the bibliographic
details and headline result match an independent abstract-level record. It does not mean the methods were checked.

---

## 1. The product brief's claims, verdict by verdict

These come from `CLAUDE.md` ("What the product is", the features list, the validation test). Each verdict is the
reconciled position after the audit.

| # | Claim in the brief | Verdict | Basis | Evidence code / strength |
|---|---|---|---|---|
| 1 | "Median frequency drops roughly 120 Hz fresh to 90 Hz cooked" | **Unsupported as absolute values.** A *relative* fall of roughly 20–30% over a set to failure is typical. Absolute Hz depends on muscle, electrode spacing, placement relative to the innervation zone, fat, load, joint angle and sampling rate. The one biceps figure found (~77–79 Hz *mean* frequency, isometric) is from a conference abstract. | Jenkins 2015; Dimitrov 2006; Tsoukos 2021; A6 C15 | I, moderate for the relative fall; limited for any absolute value |
| 2 | "That drop is the fatigue measurement" | **Partly.** MDF compression is a peripheral, metabolic marker linked to conduction velocity and pH. It is not capacity loss, not central fatigue, not task failure, and it largely misses type I fibre fatigue. | Cifrek 2009; Enoka & Duchateau; Gerdle 1992; Vestergaard-Poulsen (MDF vs pH r = 0.82) | M, strong for direction; I, limited for meaning |
| 3 | "It is tempo-independent" | **Not established; evidence mixed.** Sakamoto 2012: similar MDF drop across four bench-press speeds. Yan 2025 (n = 10): fast tempo amplified the decline. Fresh-state MDF also moves with joint angle and innervation-zone position, which tempo changes within each rep. | A2 C5 response; A6 C5 | I, limited |
| 4 | "Which is why this beats velocity-based training" | **Unsupported.** No head-to-head study exists. Rodríguez-Rosell 2021 was originally cited here and was **withdrawn as misapplied** (its EMG is a training-adaptation measure). | A6 C9 | none |
| 5 | "Amplitude rises at the same time (more fibres recruited)" | **Supported but not specific.** Amplitude also rises with load, speed and effort, plateaus 3–5 reps before failure, and is limited by cancellation. | Jenkins 2015; Sundstrup 2012; Keenan 2005 | I, moderate |
| 6 | "The two together are the fatigue score" | **Plausible, unvalidated.** The best published amplitude + spectral combinations explain ~47–50% of variance in power loss, group-level, n = 15, leg press. The figures appear in the 2009 working paper; the journal version was not confirmed. | González-Izal 2010b | I, limited; on TENSR: H |
| 7 | Rep counting — "each rep is a burst in the EMG" | **Plausible; IMU is the validated route.** Wrist/forearm IMU counting reaches ±1 rep in ~91–93% of sets. EMG-burst counting on a belly band is not validated. | RecoFit (Morris 2014); Soro 2019 | I, moderate (IMU); H (EMG) |
| 8 | Fatigue per rep, rep-of-failure | **Unsupported.** Single-rep MDF is too noisy (~9 Hz SD against a ~30 Hz total change). MDF at failure is load-dependent, and the direction of the load effect differs between studies. | A3/A6 simulations; Jenkins 2015; Tsoukos 2021; Yan 2025 | H; contradicted for a fixed failure value |
| 9 | Reps-in-reserve, live ("about 2 left") | **No evidence.** No dynamic free-weight sEMG RIR validation was found. The bar to beat is the lifter's own bias-corrected guess. | Halperin 2022; Jukic 2024; Garofalo 2026 (isometric) | none |
| 10 | Set score — "did this set actually reach failure" | **Unsupported, and the wrong target.** Rep count separates failure sets by construction. Outcome evidence does not support training to failure over 0–3 RIR. | Refalo 2023/2024; Grgic 2022; A6 C18 | I, moderate against the target |
| 11 | "Rest timer driven by the muscle's own recovery" | **Unvalidated.** Spectral and force recovery dissociate (Mills 1982: force ~30 s half-time, MPF ~3 min). No trial of EMG-guided rest exists. A2's original "contradicted" was corrected. | Mills 1982; A6 C4 | I, limited |
| 12 | Activation percentage — "is the target muscle doing the work" | **Unsupported in this form.** It needs a per-wear reference contraction. One channel cannot apportion work, and amplitude is not force. | Burden 2010; Besomi 2020; Vigotsky 2018 | I/M, moderate |
| 13 | Eccentric vs concentric split | **Only where the worn segment moves**; no outcome reason to coach it. | Schoenfeld 2017c | I, moderate (detection) / none (benefit) |
| 14 | Weekly volume and **stimulus** per muscle | **Volume yes, stimulus no.** Weekly sets are the best-supported dose metric. A stimulus score is contradicted by the evidence. | Schoenfeld 2017b; Pelland 2026; Plotkin 2023 | I, moderate / contradicted |
| 15 | "Logs a whole training split automatically" | **Overstated.** One band sees one muscle per session. Other muscles must come from exercise labels. | hardware | — |
| 16 | Validation test: "20–30 sets … separate cleanly … 9 times in 10" | **A pilot, not a validation.** Rep count separates the groups by construction. "3 short" has no ground truth unless continued to failure. One person's sets say nothing about other users. 27/30 has a 95% CI of 74–97%. | A4, A5, A6 C18 | — |
| 17 | Drop-set test: "the fatigue number must fall continuously and not reset when the weight changes" | **Not a valid pass criterion.** Amplitude falls when load drops. Lighter loads recruit fewer fast units, which lowers MDF on its own. Load change alters velocity, which alters MDF. A "pass" proves nothing. A4's fourth reason (partial MDF recovery during the strip) was withdrawn after Mills 1982. | A4 §2.5 + response | M |

---

## 2. Hardware and design claims checked during the investigation

| # | Claim | Verdict | Basis |
|---|---|---|---|
| H1 | ADS1292R decimation filter is sinc3 with −3 dB at 0.262 × data rate | **Verified** (TI SBAS502C via document viewer; independently, only a third-order sinc gives 0.2615) | A3, A6 |
| H2 | 500 SPS supports the fatigue measurement | **No.** At 500 SPS, −3 dB is at 131 Hz and the band ends at 250 Hz. A true −25% MDF drop reads about −16 to −18% raw, or −21 to −24% with inverse-sinc compensation, which raises noise ~4× near 250 Hz. "Cannot measure" (A3's original wording) was corrected to "biased low and compressed". 2 kSPS (DR = 100) is recommended by every agent. | A3, A6 C2, A3 response |
| H3 | `BRING-UP.md` §7: "RMS in 20–450 Hz at 500 SPS" | **Internally impossible.** Nyquist is 250 Hz. Valid only as a datasheet-condition noise check. | A3 |
| H4 | `AFE-DESIGN-REVIEW.md` §3.1: "the product's core measurement is safe" (−0.042 dB tilt 90–120 Hz) | **Incomplete.** It checked only the analogue input filter. The digital decimation filter, which dominates at 500 SPS, was not modelled. | A3, A4 |
| H5 | Electrode geometry suits the seven target muscles | **Unverified.** 25.4 mm IED vs SENIAM 20 mm (Hermens 2000). 7 mm electrodes pass the ≤10 mm rule. Orientation relative to the fibres depends on how the puck sits on the band, which nothing records. | A3, A4, A6 C14 |
| H6 | Reference/RLD electrode on the active muscle contaminates the signal | **Low concern.** E2 is 25.92 mm from both E1 and E3 (A4 measured from the board), so activity under it is common mode. Estimated contamination ~0.4% at 50 Hz. **Real risk: E2 losing contact**, which collapses RLD and CMRR. | A6 C8; A3, A4 responses |
| H7 | The 25.4 mm IED's comb-filter dip (~118–157 Hz) confounds fatigue | **Not for the relative trend** (−25.4% at 25.4 mm vs −25.0% at 20 mm in simulation). It shifts absolute Hz only. A4 adds: true only if the pair is aligned with the fibres and stable. | A6 C3 |
| H8 | Single-rep MDF can drive live feedback | **No.** The estimator floor is ~9.3 Hz SD (0.5 s window) and 4.7 Hz (2 s). With a 3 Hz/rep decline, the slope reaches t ≈ 2 only around rep 8 of 10. | A3, A6 C7, A3 response |

---

## 3. Citation audit — corrections that change something

Load-bearing citations were all found to exist. **No fabricated citation was found.** The corrections:

| Study | Problem | Resolution |
|---|---|---|
| Halperin 2022 | 0.95 reps was used as an "accuracy" by A1, A2 and A5. It is a **mean signed bias**; the between-person SD is ~1.45 reps (95% CI 0.99–2.12). Accuracy is better near failure and in sets of ≤12 reps. | All three accepted. The comparator for any RIR feature is now same-session, bias-corrected self-report error. |
| Kassiano 2023a | A6 said A1's figures were wrong (+6.2% / +7.3%). A1 says A6 read the **lateral** gastrocnemius; A1's +15.2 / +6.7 / +3.4% are **medial**. | **Reconciled:** both sets are probably correct for different heads. Medial pairing only partly confirmed (snippet truncated). Direction (lengthened partials largest) holds. |
| Maeo 2023 | Long-head comparator omitted. | Long head +28.5% vs +19.6%; lateral + medial +14.6% vs +10.5%; whole triceps +19.9% vs +13.9% (A1, abstract wording). |
| Wolf 2023 | Sign of −0.28 disputed. | A1: −0.28 favours lengthened partials in the abstract's convention. **Always state direction in words.** CI crosses zero: limited. |
| Pelland 2026 | DOI 10.1007/s40279-025-02344-w could not be found by exact search. | Citation (Sports Med 2026;56(2):481–505) verified; DOI **UNVERIFIED**. "67 studies / 2,058 participants" is from a blog only. |
| Augustin 2025 | Author order wrong. | Cite as Augustin F, et al. (incl. Piñero, Nippard, Schoenfeld). |
| Colyer 2018 | A4 said the reference was gel. It was dry silver-bar Delsys Trigno. A3 omitted between-session CV 42.6% (textile) vs 41.2% (reference). | Both accepted. Raw amplitude is not comparable across days even on the reference system. |
| Lynn 2018 (Athos) | A3 said n not retrieved and squat-type. | n = 12, isokinetic, seven sessions. Athos-affiliated authors. |
| Besomi 2020 | Standardised submaximal reference omitted. | Added. It is the most practical normalisation for TENSR. |
| Nordander 2003 | The 21–33% amplitude variance from fat applies to **trapezius**. | Muscle named. |
| Rodríguez-Rosell 2021 | Misapplied (training-adaptation EMG, not within-set). | Removed from the VBT argument (A2). |
| Orange 2022 | Misapplied by A5: VBT prescription vs %1RM, not feedback vs none. | Retired as a feedback precedent. |
| Weakley 2023 | A5 omitted the authors' conclusion that feedback improved chronic adaptations. | Reported. A5 still reads it as "not established" (see §4). |
| Zhao 2025 | A4 cited only the null MDF–velocity-loss result. The same group's IJSM 2025;46(6):437–445 found r = 0.603. | Evidence is inconsistent within one group. |
| Elfving 2002 | A2 attributed "clear dissociation from pH and force" to it. No source contains that sentence. | **Withdrawn** by A2. |
| Oliveira & Gonçalves 2008 | Light one-minute bouts, no force measured; cannot show a dissociation. | Downgraded. |
| Gerdle 1992 | A2 omitted the key finding: MPF misses type I/hypoxic fatigue. | Added. |
| Yan 2025 | A6 could not confirm "largest MDF decline at 80% + fast". A2 cites abstract wording: "the greatest declines in MDF" at that condition, with a load × tempo interaction. | Kept. This conflicts with Tsoukos 2021 (larger drop at lighter loads), which strengthens the case against any fixed failure value. |
| González-Izal 2010b | 46.6% / 49.8% figures are from the 2009 working paper. | Cite as "~47–50%, journal figures unconfirmed". |
| Barbalho group | Retractions in 2020–2021. | **No agent relied on them.** A1 excluded them deliberately. Gentil 2013 is not a Barbalho paper; no retraction found. |

The full verdict per study is in the `audit_verdict` and `audit_note` columns of `STUDY-EVIDENCE-TABLE.csv`. 60 of
169 rows were audited: every named load-bearing study, plus a seeded random sample of 15 (seed 20261102).

---

## 4. Disagreements that remain open

These were argued and not resolved. They are preserved, not averaged.

| # | Between | Issue | Positions | Why it matters |
|---|---|---|---|---|
| O1 | A2 vs A3 | Does a wider IED raise or lower absolute MDF? | A2 cites a simulation where larger IED raises MDF. A3's idealisation lowers it. | Absolute Hz only; the relative trend is unaffected. |
| O2 | A6 vs A4 | Is the IED effect "irrelevant"? | A6: irrelevant to the relative trend. A4: only if the pair is aligned with fibres and stable over the innervation zone, which is untested. | Decides whether orientation testing must precede any MDF claim. **Coordinator: A4's qualification is correct;** orientation testing is in Stage 3. |
| O3 | A6 vs A3/A4 | Is MDF the safer trend than amplitude? | A6: yes, because sweat moves amplitude, not MDF. A3/A4: MDF is not immune. Poor contact adds mains and motion artefact, and low SNR biases MDF. | Both trends need a per-rep signal-quality gate. Not a reversal. |
| O4 | A6 vs A5 | Is long-term benefit of feedback established? | A6: low-certainty evidence exists (Weakley 2023 authors' conclusion). A5: few trials, magnitude-based inference: "not established". | Neither transfers to EMG feedback (H). No product decision depends on it now. |
| O5 | A6 vs A5 | Stage 3 criterion | A6: the two-reference-pair floor should be the only criterion. A5: keep an absolute usefulness ceiling too, because the floor passes any device where two gel pairs disagree badly. | **Coordinator: adopt A5's version** — floor primary, ceiling secondary. |
| O6 | A6 vs A5 | Run a research test of live MDF? | A6: no live use is defensible. A5: agreed for product, but pre-register a research test because a documented null retires the brief's central claim. | Kept as a research-only arm of Stage 4. |
| O7 | A6 vs A4 | IMU on static-segment exercises | A4 originally: the IMU sees almost no rep motion. A6: untested; belly tilt may help counting. A4 now: untested both ways; keep phase, ROM and velocity features to moving-segment lifts. | Test both in Stage 3. |
| O8 | A6 vs A4 | Log an IMU-detected stalled final rep? | A6: user tags only. A4: log as user-confirmed metadata, test which users correct less. | Minor; test both. |
| O9 | A1 vs A6 | What replaces the set score? | A1: a load-appropriate effort zone (~0–3 RIR, closer for light loads) is the defensible target. A6: research-only. | Both agree it cannot ship, because it needs a validated RIR. |
| O10 | A3 vs A6 | Is 500 SPS MDF "correctable"? | A6: about half the compression is correctable droop. A3: compensation boosts noise ~4× near 250 Hz and is unproven on real data. | No disagreement on the decision: 2 kSPS. |

---

## 5. Unsupported leaps the audit caught

These are reasoning errors, not citation errors. Each was accepted by the responsible agent.

1. **Bias read as accuracy** (Halperin). Fixed throughout.
2. **"500 SPS cannot measure MDF."** It measures a band-limited, biased index. The decision still stands.
3. **"Spectral recovery is faster than force recovery, so the timer ends early."** Mills 1982 shows the reverse in its
   paradigm. The timer is unvalidated for a different reason.
4. **"A trend is visible after 4–6 reps."** Arithmetic on the authors' own noise figures puts it near rep 8 of 10.
5. **Per-rep MDF agreement targets (±10 Hz; SD < 3 Hz).** Both are below the physical floor of spectral estimation.
   They test nothing about the board. Replaced with slope-based gates.
6. **"Amplitude is the safer within-set feature."** It is the more confounded one with dry electrodes.
7. **Two-group separation (failure vs 3 RIR) as evidence of a fatigue sensor.** Rep count does it by construction;
   only matched-rep comparisons count.
8. **One participant's confidence interval generalised to users.**
9. **An acute EMG difference read as a training recommendation.** This leap appears in the brief (activation %,
   stimulus) and is contradicted by Plotkin 2023 and the load literature.
