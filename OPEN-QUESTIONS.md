# Open questions and remaining research

2026-11-02. This tracks what was **not** settled. The investigation did not cover everything, and this file says
what is left rather than pretending otherwise.

## A. Decisions for Kye (design facts the research depends on)

| # | Question | Why it matters | Who raised it |
|---|---|---|---|
| K1 | **What is the measurement data rate?** Bring-up uses 500 SPS; the firmware brief says 1–2 kHz; the analysis brief says 20–450 Hz. | At 500 SPS the sinc3 filter is −3 dB at 131 Hz and the band ends at 250 Hz. Every agent recommends 2 kSPS (DR = 100) for spectral features. | A3, A4, A5, A6 |
| K2 | **How does the puck sit on the band relative to the E1–E3 axis?** | If the 44 mm axis runs around the limb, the bipolar pair is across the fibres of biceps, triceps, quads and calf. This is the top unanswered hardware question. Nothing in the repo records it. | A4, A6 C14 |
| K3 | Dry studs only, or snap-on gel electrodes too? | Gel is the biggest signal-quality lever without a respin. Validation must use what ships. | A3, A4 |
| K4 | Raw stream over BLE, or features on the puck? | Validation needs raw logging. The product likely needs on-puck features with one per-rep record (A3: 0.3–0.6 s after the rep). | A3, A4 |
| K5 | Which muscles will be named at launch? | Each must pass Stage 3 separately. The geometry is likely worst on small muscles (deltoid heads, calf heads) and on pectoralis. Whether SENIAM covers pectoralis major was not verified. | A3, A6 |
| K6 | Motion-artefact filtering and IMU-gated rejection strategy | The 20 Hz high-pass convention (De Luca 2010) and the SQI design are proposals until bench-tested. | A3, A4 |

## B. Scientific disagreements preserved (see CLAIM-VERIFICATION.md §4)

- O1: Does a larger IED raise or lower absolute MDF? (A2 vs A3) Absolute Hz only.
- O2: Is the IED effect irrelevant only if the pair is aligned and stable? (A4 qualifies A6)
- O3: Is MDF really more robust than amplitude with dry electrodes? (A6 vs A3/A4) Both need SQI gating.
- O4: Is there an established long-term benefit of training feedback? (A6 vs A5)
- O5: Should the Stage 3 gate include an absolute usefulness ceiling? (A5 vs A6). The coordinator adopted A5's
  version.
- O6: Should a research test of live MDF be run? (A5 yes; A6 no live use). Kept as a research arm.
- O7: Can the IMU see reps when the worn segment is static (belly tilt)? Untested.
- O8: Log an IMU-detected stalled rep, or rely on user tags? Test both.
- O9: What replaces the set score: an effort zone (A1) or nothing (A6)? It depends on RIR, so not now.
- O10: Is 500 SPS MDF usefully correctable? Moot if 2 kSPS is adopted.

## C. Evidence not reached (verify before relying on it)

**Access.** No paper was read in full text. WebFetch, doi.org, PubMed, PMC, Crossref and publisher hosts were
blocked. Re-verify load-bearing rows with full-text access before any external publication or claim.

**Unverified or partly verified items:**
- **Pelland 2026** DOI, and its numeric dose-response estimates (not retrieved).
- **Vieira 2021**: citation confirmed, results not retrieved.
- **Morton 2019** details beyond the abstract.
- **Schoenfeld 2014** (EMG at low vs high loads).
- **Lixandrão 2018**, **Kubo 2019**, **Zourdos 2021**, **rest-pause trials** (Prestes 2019): listed by A1 as not
  checked.
- **SENIAM:**
  - per-muscle landmark wording;
  - reference-electrode wording;
  - whether pectoralis major is covered;
  - the exact ≤10 mm electrode-size wording (confirmed only secondarily).
- **CEDE matrix cell values** (Besomi 2019); the HD-sEMG matrix (Martinez-Valdes 2023) journal details.
- **LSM6DSO full ODR table.**
- **ADS1292R datasheet items already owed** by `docs/AFE-DESIGN-REVIEW.md` §6:
  - supply sequencing;
  - RLD stability criterion;
  - PGA output resistance (what C27 actually filters).
- **Ives & Wigglesworth 2003** results; **Karthick 2018**; arXiv 2512.11854 details.
- **Garofalo 2026**: validation scheme and error units.
- **Thomas & Wahlström 2025** (preprint): exact numbers.
- **Sakamoto 2012** DOI; **Gentil 2013** and **Wakahara 2013** DOIs.
- **Jiménez-Alonso 2022**: result not retrieved.
- **de Vet 2006** (SDC terminology).
- **Kassiano 2023a**: medial-head pairing only partly confirmed (snippet truncated).
- **Inara**'s current claims and pricing: site unreachable.

**Topics not searched or only touched:**
- Cables, unstable surfaces and stability effects on hypertrophy.
- Heavy-cheat-then-strict sequencing: no trial found; one search.
- Pauses and peak-contraction squeezing: no longitudinal trial found; limited searching.
- Muscle oxygenation/NIRS and mechanomyography as alternative fatigue constructs: compared only briefly.
- Temperature effects on conduction velocity and MDF in gym conditions.
- Sex differences in sEMG fatigue indices and in RIR accuracy.
- Hair, skin tone and tattoo effects on dry-electrode contact: proposed for Stage 3 recording, not reviewed.
- Accelerometer mechanomyography (high-rate IMU logging) as a cheap second fatigue channel: research idea from A4,
  not reviewed.

## D. Stale statements found in existing project docs (reported, not edited)

This investigation changes no project files. These are listed for Kye.

- `docs/afe-sim-results.md` §1/§1b still analyses C1/C2 at 1 nF; 100 pF is fitted.
- `docs/BRING-UP.md` §7: "RMS in 20–450 Hz" at 500 SPS is impossible as written (Nyquist 250 Hz).
- `docs/BRING-UP.md` §8 treats 100 pF as pending; it is decided.
- `docs/BRING-UP.md` §7a.3 says U1.12 is 2.58 mm from its capacitor; it is now 1.15 mm.
- `docs/BRING-UP.md` §9 repeats the drop-set "must not reset" criterion. See CLAIM-VERIFICATION claim 17.
- `docs/AFE-DESIGN-REVIEW.md` §3.1 "the product's core measurement is safe" checks only the analogue filter. The
  sinc3 decimation filter is not modelled.
- `CLAUDE.md` product claims: see CLAIM-VERIFICATION §1. **Not edited**; the brief asked for no claim changes during
  research.

## E. Next research steps, in order

1. Re-run citation verification with full-text access (allow doi.org, PMC and ti.com).
2. Answer K1 and K2. Both are needed before Stage 1 can be specified exactly.
3. Get the three datasheet items owed (Kye is pulling them).
4. A short targeted review of electrode orientation effects on dynamic MDF slopes. The evidence is thin: one vastus
   lateralis study, p = 0.09.
5. A targeted review of the IMU on the upper arm or thigh (not wrist) for rep counting.
