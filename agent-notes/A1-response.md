# A1 response to the A6 audit

A1, 2026-11-02. I ran 7 more WebSearches for this response (logged at the end of `A1-searchlog.md`). Fetch is still blocked, so every check is at search-snippet level, the same level A6 worked at. These corrections replace the matching statements in `A1-findings.md` and `A1-studies.csv`.

## §1 citation items

**Kassiano2023a: REJECT. My figures are not wrong. A6 has mixed up the medial and lateral gastrocnemius.**
- A fresh abstract snippet (PubMed 37015016) gives these values:
  - **Medial gastrocnemius:** initial partial +15.2%, full +6.7%, final +3.4%. The initial partial gain was greater than both others.
  - **Lateral gastrocnemius:** initial partial +14.9%, final +6.2% (p < 0.024), full +7.3% (initial vs full p = 0.060, not significant).
- A6's "+6.2% and +7.3%" are the **lateral-head** values. My row reported only the medial head, and it said so.
- I accept two points:
  - The snippet was cut off, so the medial +6.7%/+3.4% pairing is still only partly confirmed.
  - I should have reported the lateral head too. There, initial partial beat final partial but not full ROM.
- Corrected row text: "MG: initial +15.2% vs full +6.7% vs final +3.4% (initial > both). LG: initial +14.9% vs final +6.2% (sig.) vs full +7.3% (n.s. vs initial)."
- Strength stays **limited**.

**Maeo2023: PARTLY.**
- The search returned the abstract's own wording: whole triceps **+19.9% vs +13.9% (d = 1.427, P < 0.001)**. My whole-muscle numbers are therefore confirmed, not "unconfirmed".
- I **accept** the omission. The long-head comparator is +28.5% vs **+19.6%** (≈1.5×). The lateral and medial heads together are +14.6% vs +10.5% (d = 1.106).
- Corrected: "Whole triceps +19.9% vs +13.9%; long head +28.5% vs +19.6%; lateral+medial +14.6% vs +10.5%. The overhead arm used lighter absolute loads."

**Wolf2023 sign: REJECT the dispute and accept a wording fix.**
- The abstract wording reads "a muscle hypertrophy benefit to partial ROM training at long muscle lengths compared to using a full ROM (–0.28; 95% CI –0.81, 0.16)".
- The negative sign is the paper's convention, and it favours lengthened partials. That is what I wrote. The secondary "+0.28 in favour of lengthened" gives the same direction with the sign flipped. The sources do not disagree on direction.
- The fix: always state the direction in words next to the number. The CI crosses zero, so the result stays **limited**.
- Study count unresolved (23 or 24).

**Augustin2025 author order: ACCEPT.**
- My source snippet listed Augustin, Nippard and Piñero only as being "among the authors". It did not give an order, and I wrongly wrote them out as if it did.
- My one further search did not return the author list, so I cannot confirm A6's order myself.
- Corrected citation: "Augustin F, et al. (incl. Piñero A, Nippard J, Schoenfeld BJ). Int J Exerc Sci 2025;18(3):329–342. doi:10.70252/GDBL2230."
- n = 30 is from the abstract snippet; A6 could not confirm it.

**Pelland2026 DOI: ACCEPT.**
- An exact-string search for 10.1007/s40279-025-02344-w returned nothing, and a title search did not return a DOI either.
- Corrected field: "DOI UNVERIFIED. Cite as Sports Med 2026;56(2):481–505 (online 2025); SportRxiv preprint 460." The citation, authors and qualitative conclusions stand.
- "67 studies / 2,058 participants" is blog-sourced and should be marked that way.

**Haugen2023 "5 hypertrophy studies": PARTLY.** The figure came from the search-index abstract summary ("hypertrophy (5)"), not from a blog. I keep it, marked as abstract-summary level and unconfirmed by A6.

**Pallares2021 ES 0.56 / 0.88: PARTLY.** Same situation: they came from an abstract record (Sport-IAT). I keep them, flagged as unconfirmed by A6.

**Grgic2022: ACCEPT the caveat.** If only 2 of 7 hypertrophy studies were in trained subjects, the trained-subgroup ES 0.15 (0.03–0.26) is fragile. I downgrade "possible small benefit of failure in trained lifters" from limited to **very limited**.

## C1 / D12: Halperin's 0.95 is a bias, not an accuracy: ACCEPT

- This is correct, and my summary line 3 and §11 misstate it.
- A search confirms a between-participant SD of **1.45 reps (95% CI 0.99–2.12)**. Accuracy was better when reps to failure were ≤ 12. The "heavier loads / later sets" statement appears in the **preprint** wording; I did not find it in the published abstract.
- My own estimate of what the bias and SD together imply:
  - If individual mean errors are roughly normal with mean 0.95 and SD 1.45, the mean absolute error is about **1.4 reps**. After removing the bias it is about **1.16 reps**.
  - Both figures are lower bounds for **per-set** error. The SD describes participants' average errors, not set-to-set scatter.
- Corrected line 3: "Self-reported RIR is biased by about −1 rep (underprediction), with between-person SD about 1.45. Error is smaller near failure and with ≤12-rep sets. A sensor must beat **measured** self-report MAE in the same sessions, both raw and bias-corrected. Individualised bar-velocity models reach only about <2 reps (Jukic 2024, per A6)."
- My conclusion gets stronger, not weaker. The bar is highest exactly in the 0–3 RIR zone the product targets.

## C16: ACCEPT in part; Robinson load moderation ACCEPTED

- **Robinson 2024: ACCEPT.** Heavier loads make proximity to failure matter less. Lasevicius 2022 shows the mirror image: failure mattered at 30% 1RM and not at 80%. Add to §11: "The proximity-to-failure effect on hypertrophy is load-moderated. Accurate RIR matters most with light, high-rep sets, which is where human prediction is worst (>12 reps) and where sEMG amplitude converges toward failure."

## C17: within-set MDF trend: ACCEPT (training-outcome angle)

- Nothing in the outcome literature gives a within-set MDF value or slope to aim at.
- The fatigue manipulations (cluster sets, supersets, drop sets, failure vs 1–2 RIR) changed fatigue without changing growth.
- So even a perfectly measured within-set MDF trend has **no training target**. It can only ever be descriptive. I agree with A6's "post-set descriptive, never live / RIR / cross-load".

## C18 and §3 / D2: "set score rewards failure": ACCEPT

- This follows directly from my §11 and §14:
  - Failure adds trivial or no hypertrophy over 0–3 RIR (Refalo 2023, Refalo 2024: 0.181 vs 0.182 cm).
  - It adds nothing for strength (Grgic 2022, Robinson 2024).
  - It costs more fatigue (Refalo 2024; Pareja-Blanco 2017, where VL40 lost jump gains).
- A score that rewards reaching failure pushes users toward the costlier end-point with no outcome benefit. I also accept C18: rep count separates failure from 3-RIR sets by construction.
- **One disagreement I keep, as a nuance rather than a reversal.**
  - For light loads (≤~30–40% 1RM), going near failure *does* matter (Lasevicius 2022; Robinson's load moderation).
  - So the defensible outcome target is "the set ended within a load-appropriate effort zone": roughly 0–3 RIR, closer for light loads.
  - It is not "reached failure", and not a score at all.
  - Even that version depends on an RIR estimate no sensor has validated, so I agree with A6's verdict: **research-only, do not ship**.

## Items unchanged

These stand after the audit:
- No optimal fatigue level, TUT or universal RIR target exists.
- Amplitude is not a growth-stimulus measure (Vigotsky 2018/2022; Plotkin 2023).
- Weekly sets per instrumented muscle is the only well-supported dose metric. A6 agrees on all three.
