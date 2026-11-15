# A3 response to the A6 audit

2026-11-02. `A3-findings.md` is not rewritten; corrections are carried here.

**What I checked.**
- `A6-check-mdf.py` re-run with `python3 -I`; numbers reproduce exactly.
- Cosmetic: the script's printed header is one column out of step (the first data column is "500 raw"). A6's audit table reads the columns correctly.
- I recomputed C7 by hand. Slope SE = σ/√Σ(x−x̄)², with σ = 9.3 Hz, gives 2.94, 1.43 and 1.02 Hz/rep for 5, 8 and 10 reps. That confirms A6's figures.

---

## §1 Citation rows

| item | verdict | response |
|---|---|---|
| Lynn 2018: n = 12, isokinetic, VL/VM/BF, seven days | **ACCEPT** | My "n not retrieved, squat-type" is wrong. The correct description is isokinetic knee work, not free-weight lifting. |
| Colyer 2018: between-session ARV CV 42.6% (textile) vs 41.2% (surface) | **ACCEPT; material** | I reported only the within-session CVs (13.8 / 14.1%). The between-day figure is the one that matters for "weekly volume / stimulus". Even the reference system cannot compare raw amplitude across days. It supports A6's D1. |
| Besomi 2020: standardised submaximal reference omitted | **ACCEPT** | This is the most practical normalisation for TENSR: a fixed submaximal contraction or warm-up set per wear. It should replace my implied "MVC" in the calibration recommendation. |
| Nordander 2003: trapezius not named | **ACCEPT** | The CSV says trapezius, but the findings do not. The 21–33% figure is trapezius-specific and second-hand. Transfer to limb muscles is I, limited. |
| Garofalo 2026 baselines (linear, SVR); Baek 2025 DOI 10.3390/s25216588; Steele 2017 authors, PeerJ 5:e4105, n = 141; Hermens DOI 10.1016/S1050-6411(00)00027-4; Martinez-Valdes 2023 UNVERIFIED | **ACCEPT** | These are corrections and additions to my rows. Steele 2017 duplicates A5's row; merge. |

## §2 Challenges

**C2. "500 SPS cannot measure MDF" is overstated — ACCEPT the wording change, PARTLY on "correctable".**
- A6 is right that about half the compression is deterministic droop. Inverse-sinc3 compensation recovers the drop to −21.4 to −24.2%, against −25% true, across five spectral shapes.
- A 500 SPS MDF is a band-limited index that still tracks fatigue. My Task 2 sentence "cannot measure" should read: **"biased low, and the within-set trend compressed by about a third uncompensated or about 10% compensated. Not comparable with 20–450 Hz literature values."**
- A6's model has no noise. At 500 SPS, compensation applies up to +11.8 dB at 250 Hz, multiplying the noise floor by about 4 in the band carrying the high-frequency half of the spectrum. On low-amplitude reps the compensated estimate will be noisier than modelled.
- Compensation at 500 SPS is therefore correctable in principle and unproven in practice.
- We agree on the decision: **DR = 2 kSPS**.

**C3. The 25.4 mm dip is irrelevant to the relative trend — ACCEPT.**
- A6's run (−25.4% at 25.4 mm vs −25.0% at 20 mm) matches my own script's numbers: −26.2% vs −25.9%. I had reported absolute values only.
- I also accept the double-counting point. A Shwedyk-type spectrum is already fitted to bipolar recordings, so my "about 10 Hz lower" is an upper bound on an upper bound.
- Remaining point: absolute thresholds ("120 → 90 Hz") do not transfer between IEDs.
- The **A2 vs A3 sign disagreement** on how IED moves absolute MDF stays unresolved. My idealisation uses a single conduction velocity, and A2's simulation is a different model. Neither is TENSR data. It affects only absolute Hz.

**C7. A trend becomes detectable at about rep 8, not 4–6 — ACCEPT.**
- My "4–6 reps" took the 30 Hz range as the signal. It did not do the regression: at 3 Hz/rep, t ≈ 1.0 at 5 reps and ≈ 2.1 at 8.
- A 1 s phase-locked window and a one-sided test bring detection forward by about one rep. Still too late for live use.
- My Task 8 "say nothing until the trend is estimable" becomes, in practice, **post-set only**.

**C8. E2 is common mode by equidistant geometry; "1%" was loose — ACCEPT.**
- At 48 dB the contamination is about 0.4% at 50 Hz. It rises toward a few percent higher in the band as the RC-mismatch CMRR falls about 20 dB/decade. It is still low.
- I agree the real E2 risk is **contact loss**, which collapses the RLD drive and the CMRR. That belongs in the lead-off and signal-quality checks (my Task 4 table already gates on lead-off).

**C11. The per-rep agreement floor is about ±20–26 Hz — ACCEPT** (aimed at A5, but built on my numbers).
- √2 × 7–9 Hz ≈ 10–13 Hz SD for the difference, so the limits of agreement are about ±20–26 Hz with perfect hardware. With 1 s phase-locked windows they are about ±18 Hz.
- This is a floor. Real motor-unit territory differences between two pairs only widen it.
- I agree validation should gate on per-set slope and multi-rep means.

**C14. Electrode orientation was skipped — PARTLY.**
- **Reject "skipped"**: §1.2 rates orientation "uncontrolled", notes the pennate muscles, and recommends an alignment mark plus per-muscle placement guidance.
- **Accept the substance and the priority**:
  - I did not tie orientation to the board geometry. The pair runs along the puck's 44 mm axis.
  - If that axis follows the band around the limb, the pair runs **across** fusiform limb muscles by default. That is a design-level problem, not a user error.
  - I did not rank it. It should be **the top unanswered hardware question**, measured in Stage 3 with both orientations against a reference pair before any muscle is claimed.

**C17. A within-set MDF trend is defensible post-set only — ACCEPT.** Consistent with my summary points 7 and 10. Conditions:
- multi-rep regression;
- phase-locked concentric windows;
- DR ≥ 1 kSPS, preferably 2 kSPS;
- one person, one exercise, one load.

It is not supported as a live number, a rep-of-failure detector, a reps-in-reserve estimate, or anything compared across loads.

## §3 Feature audit and §4 disagreements

- **D7, D8, D13: ACCEPT**, as above. On D13 my E2 verdict stands, and orientation moves to the top.
- **D1 (amplitude internal only until Stage 3): AGREE.** It matches my Task 3 point that sweat-driven impedance drift will mimic a fatigue trend in amplitude, and Colyer's 42% between-day CV adds to it.
- **C6 (MDF is not the riskier feature): PARTLY.** I agree that the impedance change barely moves MDF through the input corner (about 3.5 kHz with 100 pF). I disagree that MDF is insulated from contact quality.
  - Impedance mismatch raises 50 Hz leakage.
  - Poorer contact raises low-frequency motion artefact.
  - Both put power below the median, so MDF reads lower: **the same direction as fatigue**.
  - MDF is more specific than amplitude only behind a signal-quality gate. Keep on record.
- **Electrical-activity duration: log, do not display. AGREE.** Colyer's timing bias is my own finding.
- **Rep counting: prototype. AGREE**, with A6's caveat that no belly-worn IMU has been validated (C13).

## Unchanged positions

- 2 kSPS is required for spectral features.
- The BRING-UP §7 instruction "20–450 Hz RMS at 500 SPS" is internally impossible.
- No validated sEMG reps-in-reserve method exists for dynamic lifting.
- Leave-one-subject-out and leave-one-session-out validation with re-applied bands, plus IMU-only and self-report baselines, are mandatory.
