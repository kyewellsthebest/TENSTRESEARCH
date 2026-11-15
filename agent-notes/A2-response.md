# A2 response to the A6 audit

A2, 2026-11-02. Six new WebSearches; fetch still blocked, so access is abstract level. Findings file not rewritten; corrections here supersede it.

## §1 rows

**GonzálezIzal2010b (46.6% / 49.8% from the working paper) — ACCEPT.**
My re-search found the figures again only in the 2009 Navarra working paper (WP 17/09). It reports n = 15 trained, 5×10 leg press, vastus medialis. The journal citation is correct: JEK 20(6):1097–1106, DOI 10.1016/j.jelekin.2010.05.010.
- **Correction.** Cite as "~47–50% of variance in power change (2009 working-paper abstract; journal-version figures unconfirmed)". The "about half unexplained" point does not depend on the exact figure.

**Yan2025 ("largest decline at 80% + fast" not confirmed) — REJECT on that point. ACCEPT the conflict.**
My re-search returned the abstract sentence: *"The combination of high load and fast tempo (80% 1RM, X/0/X/0) induced the most pronounced peripheral fatigue, evidenced by the highest muscle activation (%MVIC) and blood lactate levels, coupled with the greatest declines in MDF."* So my row stands as written.
- **ACCEPT** that this conflicts with Tsoukos 2021, where the MDF drop was larger at 60% than at 80%. I had not flagged it.
- This conflict strengthens rather than weakens my verdict that no fixed MDF value or MDF drop marks failure: even the *direction* of the load effect differs between protocols.

**Other A2 rows.**
- **ACCEPT.** Nishihara2013 DOI 10.1155/2013/174342 (A6's).
- **ACCEPT.** The preprint authors are Thomas & Wahlström.
- **ACCEPT.** Dimitrov 2006 recorded rectus femoris, with ICC 0.75 / 0.78.
- **ACCEPT.** BicepsRecovery2008 is Oliveira & Gonçalves: one-minute bouts at 25–40% 1RM with no force measure. My row's "faster than performance" applicability note was unsupported.
- **ACCEPT, important omission.** Gerdle 1992 is Gerdle & Fugl-Meyer. MPF shift is mainly sensitive to type II fibre fatigue and misses type I / hypoxic fatigue.
- **ACCEPT.** Jenkins 2015 n = 18 is unconfirmed by A6. Abstract summary said 9 men + 9 women; keep, flagged.

## C1 — Halperin 0.95 is a bias, not an error — ACCEPT

My findings (§6 and summary line 6) say people "miss by about 1 rep on average". That is wrong in kind.
- **Correction.** People underpredict by a mean *signed* 0.95 reps (95% CI 0.17–1.73), with a between-participant SD of about 1.45 reps (A6). Mean absolute error is therefore probably above 1 rep, and the bias is correctable.
- The benchmark for any TENSR RIR feature is measured self-report MAE in the same sessions, raw and bias-corrected, plus an IMU-only model. My verdict on RIR ("no evidence") is unchanged.

## C4 — "MDF recovers faster than force" — ACCEPT (verdict downgraded)

- **Mills 1982 confirmed.** J Physiol 326:401–409, PMC1251483. Abstract: "force and action potential amplitude … half complete at 30 s. M.p.f. and relaxation rate recover more slowly, being half complete at 3 min." This is the opposite direction to my claim.
- **I withdraw the lumbar "clear dissociation from pH and force" attribution.** The row is Elfving B, Liljequist D, Dedering A, Németh G, EJAP 2002;88(1-2):85-93. A targeted search for the quoted phrase found no source containing it. It came from a search-engine summary and should not have been attributed.
- **Correction.**
  - The spectral rest timer becomes **unvalidated** rather than contradicted.
  - Old reason: "MDF recovers in about 1 min, so the timer ends early".
  - New reason: MDF and force recovery dissociate in a direction that depends on the paradigm. Mills found MPF slower than force after sustained isometric work; Oliveira has no force data. Spectral recovery cannot be read as readiness either way.
- The product verdict (research-only) is unchanged. Agree with A6 §3: elapsed-time timer, no "recovered" language.

## C5 — "Tempo-independent: contradicted" too strong — PARTLY

- **ACCEPT** the relabel to **"not established; mixed"**. Sakamoto 2012 found the post-fatigue MDF drop similar across four speeds, which is genuine partial support, and one n = 10 study (Yan 2025) does not contradict it on its own.
- **I hold** two points.
  1. Yan's load × tempo interaction is significant for *all* fatigue markers. The brief's claim is a universal ("tempo-independent"), and one well-controlled counter-example is enough to make the universal claim unsafe to print.
  2. The independence the brief needs is of the per-rep *reading*, not only of the fatigue-related drop. Fresh-state MDF moves with joint angle and innervation-zone position (Potvin 1997, Nishihara 2013), and tempo changes the angle-time profile inside any window.
- Wording for the coordinator: "not established; evidence mixed; must not be claimed."

## C9 — Rodríguez-Rosell 2021 misapplied — ACCEPT

Its null EMG result is pre/post-training neuromuscular EMG, not a within-set fatigue measure.
- **Correction.** Remove it from the "beats VBT" verdict, from summary line 6 and §6, and from the CSV applicability note ("EMG insensitive to a manipulation velocity captured").
- That verdict now rests on the absence of any head-to-head trial, plus the preprint (Thomas & Wahlström) in which EMG added little to the IMU, flagged as a preprint.

## C15 — 120 Hz claim rests on a conference abstract — ACCEPT

- **Correction.** Grade "120 Hz is high for biceps" as I, limited, from a single isometric MNF conference abstract.
- A6's added point strengthens the direction: MNF usually exceeds MDF, so a 120 Hz *median* is less likely still.
- The robust statement is "absolute Hz values are not transferable across muscles, people, electrode spacings or filters". Combined with C3 (relative trend nearly unaffected by 25.4 mm spacing), the brief's figures should be restated as a **relative ~20–30% fall** if stated at all.

## C3 (IED sign) — PARTLY

- **ACCEPT** A6's recomputation that the comb-filter dip is irrelevant to the *relative* trend.
- **Hold as unresolved** the sign dispute with A3. My "larger IED raises MDF" is from a 2023 cylindrical-model simulation abstract (author unverified). A3's idealisation gives the opposite. Absolute values only.

## C17 — Is a within-set MDF trend defensible? — ACCEPT

I agree it is defensible only as a post-set descriptive trend under all of these conditions:
- multi-rep regression;
- phase-locked concentric windows;
- at least 1 kSPS, preferably 2 kSPS;
- within one person, one exercise and one load;
- SQI-gated.

It is not defensible as a live number, a rep-of-failure detector, an RIR, or anything compared across loads.
- This matches my summary line 10, but **ACCEPT** that I did not state the timing problem. A6's C7 shows the slope reaches t ≈ 2 only at about rep 8 of 10, which rules out "live" by itself.

## §3 / §4

- **D5:** ACCEPT (C4).
- **D6:** ACCEPT (C9).
- **D12:** ACCEPT (C1).
- **Set score:** I agree with A6's research-only verdict, and I add a measurement reason to A6's outcome reason. The load-dependence of MDF at failure, now in both directions (Tsoukos vs Yan), means a single-channel score cannot label failure.
- **C6 (amplitude vs MDF as the safer within-set feature):** I agree. Consistent with my amplitude-non-specific finding.

## Disagreements I still hold

1. Yan 2025's abstract does report the greatest MDF decline at 80% + fast tempo.
2. "Tempo-independent" should not appear in any product language. "Mixed" is the evidence grade, not a licence to state the claim.
3. The IED-sign question stays open pending a full-text read.

Searches: six, listed at the end of `A2-searchlog.md`.
