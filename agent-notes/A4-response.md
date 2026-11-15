# A4 response to the A6 audit

A4, 2026-11-02. Response to `A6-audit.md`. My matrix is not rewritten. Where I now agree, §2 supersedes the matching row of `A4-feature-matrix.csv` for the merge. I cannot re-verify A6's new sources (Mills 1982, Zhao IJSM 2025, Sakamoto 2012) because fetch is still blocked. I take them as A6 reports them, marked SECONDARY.

---

## 1. Item responses

**C3: comb-filter dip and "MDF depends strongly on CV". ACCEPT.**
- My §4 Q3 sentence was wrong: CV is the fatigue signal. A6's run (−25.4% at 25.4 mm vs −25.0% at 20 mm) shows the relative trend intact. The IED point is now **absolute-Hz only**.
- What survives from Q3 is alignment and slip, not CV: a cross-fibre pair, or a band slipping across the innervation zone mid-set. Both belong under C14.

**C4 (as it touches §2.5 point 3 and the rest-timer row). ACCEPT.**
- Mills 1982 (force t½ ≈ 30 s, MPF t½ ≈ 3 min) makes my "MDF recovers faster than strength" unsupported in direction. At t½ ≈ 3 min a ~10 s strip-time gives little MDF recovery, so **I withdraw §2.5 point 3**. Points 1, 2 and 4 stand; the drop set is still not a valid pass criterion.
- Spectral rest timer stays research-only; the reason becomes "unvalidated, dissociation inconsistent".

**C5: "tempo-independent: contradicted". ACCEPT.**
- Sakamoto 2012 (similar post-fatigue MDF drop across four speeds) against Yan 2025 (fast tempo amplified it) is mixed evidence, not contradiction.
- Claim 9 moves from "U, contradicted" to **"U, not established; evidence mixed"**.
- At-failure MDF is still load-dependent (Tsoukos 2021; Jenkins per A6), so no single failure threshold transfers across loads.
- Claim 10 ("beats VBT") stays unsupported, on the absence of any head-to-head trial alone.

**C6: confound ranking (sweat moves amplitude more than MDF). ACCEPT the ranking, PARTLY on the mechanism.**
- The core argument is right. Impedance drift hits amplitude (gain, CMRR, noise) first. With 100 pF fitted, the input corner stays far above the band.
- Amplitude also plateaus before failure and drops at load changes. My own §2.5 point 1 said the second, so ranking amplitude as safer was inconsistent. I withdraw that ranking.
- **Caveat I keep: MDF is less exposed to impedance drift, not immune to it.**
  - Low SNR flattens the spectrum toward the noise floor and biases MDF upward. Residual 50 Hz and any notch distort the low end.
  - So a per-rep SQI gate (baseline noise, hum level) is needed before *either* trend is used.
- Net: both are unvalidated on TENSR, and amplitude is not the safer of the two.

**C7: slope precision (applies to my within-set fatigue row). ACCEPT.**
- t ≈ 2 at about rep 8 of 10 means no live use.
- My matrix said "relative within-set trend", not live. A6's wording ("post-set summary only") is the precise version, and I adopt it.

**C8: reference electrode on active muscle. ACCEPT.**
- Measured from the board: E2 is 25.92 mm from both E1 and E3. A6's equidistance argument holds, so activity under E2 is close to common mode.
- I framed the risk as physiological, and it is not. Revised Q5: **E2 contact loss on a moving belly** collapses the RLD loop and the CMRR. That is a lead-off / SQI item.
- Minor residual: the common-mode match is only approximate under tissue inhomogeneity. Not recommendation-changing.

**C9: Rodríguez-Rosell 2021 misapplied. REJECT as applied to A4.**
- I did not cite Rodríguez-Rosell 2021. The name appears in `A4-studies.csv` only as fourth author of González-Badillo 2017 (IJSM 38:217–225).
- My "beats VBT is unsupported" already rests only on the absence of a head-to-head trial. The C9 correction is for A2 alone.

**C10: three factual errors. ACCEPT all three.**
- (a) **Colyer 2018.** The reference was dry silver-bar Delsys Trigno, not gel. My "~40% even with gel electrodes" (findings §2.1 claim 11; Colyer2018 row) is wrong.
  - This strengthens the point: the 41–43% between-session ARV CV was on *dry* electrodes, closer to TENSR. Use A6's figures (42.6% vs 41.2%; within-session 13.8% vs 14.1%).
- (b) **Zhao 2025.** I cited only the null.
  - The same group's IJSM 2025;46(6):437–445 reports a spectral fatigue index correlated with velocity loss at r = 0.603.
  - Fair summary: the relation is inconsistent within one group's work. The row should carry both (null: PeerJ, DOI 10.7717/peerj.20426).
- (c) **"SJMSS2021bench" is Tsoukos 2021** (n = 14). Use A2's verified row and drop my UNVERIFIED-authors row.

**C13: "IMU sees almost no rep motion" on static segments. PARTLY.**
- I accept that the claim is untested and that I wrongly treated the bulge-induced puck tilt purely as artefact. It is rep-locked and may *help* counting.
- I also accept that free-weight curls move the upper arm more than a strict model assumes.
- What I keep: segment kinematics on a strict curl, pushdown, leg extension or bench press carry little phase or ROM information (A6 agrees on phase split), and belly-tilt as a counting aid is equally untested.
- Revised wording: "IMU contribution on static-segment exercises is unknown; belly-tilt may aid rep counting; phase split, ROM and velocity loss from the IMU are restricted to exercises where the worn segment moves. Validate per exercise."

**C14: orientation. AGREE.** No change. It stays my top hardware question, now ranked above IED (see C3). A6's one vastus lateralis result is a reason to test, not to assume (parallel −0.13 vs perpendicular −0.21 slope, p = 0.09). The test is both orientations against a reference pair in Stage 3.

**C18: brief's 20–30-set test. ACCEPT the addition.**
- Compare features at a **matched rep index**, using only data available before the stop decision. This sharpens my rep-count confound point.
- A one-participant Wilson CI says nothing about other users (C11).

**C1 (RIR benchmark, indirectly on my RIR row). ACCEPT.**
- Comparator: measured, bias-corrected self-report MAE in the same sessions; individualised velocity reaches only "<2 reps" (Jukic 2024). Verdict unchanged: research-only.

---

## 2. §3 / §4 disagreements: revised recommendations

| feature | my draft | A6 | revised A4 position |
|---|---|---|---|
| Relative amplitude trend (D1) | Suitable to prototype | Internal only until Stage 3 | **ACCEPT.** Internal/research view only, SQI-gated. Not user-facing until it agrees with an adjacent reference pair |
| Within-set MDF trend | After substantial validation | Post-set summary, ≥1–2 kSPS, SQI-gated, dropped if it does not beat IMU-only | **ACCEPT.** Same tier, A6's wording |
| Set score "reached failure" (D2) | After substantial validation | Research-only; rewards failure | **ACCEPT** as a *score*. Outcome evidence (Refalo, Grgic, as A6 reports) gives no reason to reward failure, and C18 makes it trivially separable. One reservation, in §3 |
| Tempo claim (D3) | U, contradicted | Not established, mixed | **ACCEPT** (C5) |
| IED dip (D4) | Strong dependence on CV | Absolute-only | **ACCEPT** (C3) |
| IMU on static segments (D14) | "Almost no rep motion" | Untested | **PARTLY** (C13). Revised wording above |
| Electrical-activity duration (D15) | Prototype, descriptive | Log, not displayed | **ACCEPT.** Display "set duration" only (merged with the TUT row); log burst on/off times internally |
| Spectral rest timer | Research-only | Research-only, different reason | **ACCEPT** the reason (C4) |
| Elapsed-time rest timer | Prototype | Ship, with ≥90 s / 2–3 min defaults | **ACCEPT**, including no "recovered" wording |
| Rep counting; L/R; technique; hypertrophy score; activation %; ecc/con split; weekly counts; live RIR | as drafted | agree | **No change.** I adopt A6's stronger "contradicted" for the hypertrophy/effectiveness score, on the outcome studies A6 lists. I have not verified them myself |

**Brief-audit classifications that change:**
- claim 9: tempo-independent → not established, mixed;
- rest timer: reason only;
- claim 11: Colyer corrected to dry electrodes;
- §2.5: point 3 withdrawn.

---

## 3. Disagreements I still hold

1. **MDF is not immune to impedance drift (C6, partial).** Low SNR and mains residue bias MDF too. Neither trend should be shown, or used internally, without a per-rep signal-quality gate (baseline noise, 50 Hz level, lead-off status). This is a caveat on A6's ranking, not a reversal of it.
2. **IMU on static segments (C13).** I keep the restriction of IMU-derived phase, ROM and velocity-loss features to moving-segment exercises. "Belly tilt helps counting" is a hypothesis on the same footing as my original claim, and needs the same per-exercise validation.
3. **Auto-detected failure as log metadata (D2, narrow).** Not a score or goal. But weekly volume needs an effort tag, and an IMU-detected stalled final rep, *offered for user confirmation*, is a reasonable logging aid on moving-segment lifts. A6 prefers user tags only; I would test both and keep whichever users correct less.
4. **Alignment and slip still matter for the *relative* MDF trend (C3 residual).** A6's simulation assumes an aligned pair over a fixed innervation zone. Until C14 is measured, "irrelevant to the relative trend" should read "irrelevant if aligned and stable".
5. **Sample rate.** Not a real disagreement with C2. At 500 SPS the brief's absolute "120 Hz fresh" still cannot be shown. A6's quantification of the *trend* (about a third compressed uncompensated, about 10% compensated) should replace my wording.
