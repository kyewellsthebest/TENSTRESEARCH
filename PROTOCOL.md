# TENSR science investigation — research protocol

**Registered:** 2026-11-02, before any literature search was run.
**Scope:** research only. No firmware, electronics or product-claim changes are made by this investigation.
**Owner:** Kye. Coordinated by Claude Code with six research agents.

Changes after registration are logged at the bottom of this file, dated, with a reason.

---

## 1. Hardware as confirmed from the repository (not from the brief)

| item | value | source |
|---|---|---|
| EMG front end | TI ADS1292R, 24-bit delta-sigma, **one channel used** (CH1); CH2 inputs tied to AVDD, PGA2 unconnected | `docs/AFE-DESIGN-REVIEW.md` §1 pin table |
| Electrodes | 3 stainless snap studs, 7.0 mm ring, 4.0 mm hole, on the board underside | `CLAUDE.md`, BOM |
| Detection pair | E1 (−12.7, −11.3) and E3 (+12.7, −11.3): **bipolar, 25.4 mm centre-to-centre**, along the board's 44 mm axis | `routed.kicad_pcb`, measured via `fputil.py` |
| Reference / RLD | E2 (0, +11.3), 22.6 mm perpendicular to the pair, **on the same muscle**, driven by the RLD amplifier | same |
| Electrode type | dry (skin contact, no gel stated); snap studs could take snap-on gel electrodes — undecided | `CLAUDE.md`; open question |
| Input network | 200 kΩ series per arm, C1/C2 100 pF C0G to ground, BAV199 clamp; C27 4.7 nF across PGA | `afe-sim-results.md` |
| Data rate | **500 SPS planned for bring-up** (datasheet noise conditions); firmware brief says 1–2 kHz; analysis brief says 20–450 Hz band-pass — **internally inconsistent** | `BRING-UP.md` §7, `CLAUDE.md` |
| Motion | ST LSM6DSO 6-axis IMU (accel + gyro), I²C, INT1 to MCU, on the same puck | BOM, `CLAUDE.md` |
| MCU / link | ESP32-S3-MINI, BLE | BOM |
| Other | haptic driver (DRV2605L) and coin motor; start/stop button | BOM |
| Status | board designed and routed; **never built**; no firmware; no recorded EMG | `CLAUDE.md` |
| Intended use | worn on one muscle (bicep, tricep, quad, calf, delt, chest, glute); rep count, fatigue, RIR, set score, rest timer, activation, weekly volume | `CLAUDE.md` |

Consequences fixed before searching: no left/right or agonist/antagonist comparison from one band; no force, load,
bar-velocity or joint-angle sensor; single bipolar location; IMU measures puck (limb-segment) motion, not the bar.

## 2. Research questions

RQ1. What produces hypertrophy and strength (tension, muscle length, ROM, effort/proximity to failure, volume, tempo, rest, fatigue techniques, regional growth)? Evidence strength per factor.
RQ2. What can surface EMG establish during *dynamic* resistance exercise about activation, force, fatigue and proximity to failure, and under what conditions does each inference break?
RQ3. What are the acquisition and processing requirements (electrodes, IED, orientation, sampling, filtering, windowing, artefact, normalisation, reapplication repeatability), and does TENSR meet them?
RQ4. Which candidate features can TENSR's actual hardware support, at what evidence level, with what calibration?
RQ5. How should accuracy, repeatability and decision benefit be validated, and with what statistics?
RQ6. Which claims in the current product brief are unsupported, overstated or contradicted?

Explicit sub-questions (from the brief): optimal fatigue level; fatigue→growth; EMG stop-point validated against failure/RIR/outcomes; optimal TUT; mechanical vs electrical TUT; meaning of a "contraction rating"; recovery readiness; within-person vs universal thresholds; comparability across days/muscles/exercises/users; justification for percentage scores.

## 3. Eligibility

**Include:** peer-reviewed human studies, systematic reviews and meta-analyses (any date; priority to 2015–2026 for training outcomes); methodological consensus (SENIAM, CEDE matrices in J Electromyogr Kinesiol); manufacturer datasheets for the hardware on the board; preprints only if flagged as such and never as sole support for a key claim.
**Priority:** (a) longitudinal training outcomes for training recommendations; (b) sEMG during dynamic resistance exercise with wearable or comparable bipolar hardware for measurement claims; (c) validation studies with agreement statistics.
**Exclude as primary support:** marketing material, non-peer-reviewed blogs, studies with no extractable method, animal-only evidence for a human product claim (may be cited as mechanistic, labelled).
**Retractions/corrections:** checked for every study carried into the evidence table where feasible; recorded.

## 4. Search methods

- Web search (general and scholarly-indexed), PubMed/PMC, publisher pages, Google Scholar-indexed pages, DOI resolution via doi.org/Crossref where reachable.
- Seed with recent systematic reviews/meta-analyses per topic, then inspect the primary studies behind important conclusions (backward citation) and newer citing work (forward citation) where reachable.
- Every search string, source and date recorded in `SEARCH-LOG.md`.
- **Access limits of this environment are recorded honestly:** full text vs abstract-only is marked per study. A citation that cannot be verified is marked UNVERIFIED and is not used as sole support.

## 5. Evidence assessment

Evidence levels used throughout:

| code | meaning |
|---|---|
| D | Direct: comparable hardware (wearable/bipolar sEMG) and realistic dynamic lifting |
| I | Indirect human evidence (lab sEMG, isometric, different muscle/population) |
| M | Mechanistic / physiological explanation |
| A | Animal or in-vitro |
| H | Product hypothesis — requires validation |

Grading per conclusion: **strong / moderate / limited / very limited / none**, judged on design, consistency, sample size, risk of bias, directness and precision (GRADE-like, not formal GRADE).

Checks applied: small samples; multiple comparisons; selective reporting; measurement error in the reference; correlation reported as individual accuracy; non-significance read as equivalence; overlapping samples in meta-analyses; data leakage and subject-dependent splits in ML; whether a simpler baseline was tested.

For every materially important study, `STUDY-EVIDENCE-TABLE.csv` records: citation + DOI/link, status (incl. corrections/retractions), design, n, participants and training status, evidence category (acute / measurement validation / longitudinal), exercise/muscle/contraction, hardware + electrode configuration + processing, comparator, results with effect size and uncertainty, limitations/COI, TENSR applicability, access level.

## 6. Team and process

Batch 1 (parallel): A1 training outcomes; A2 sEMG and fatigue; A3 wearable sensing and signal processing (incl. SENIAM/CEDE, ML critique); A4 product translation (reads the repo); A5 validation design.
Batch 2: A6 independent auditor — verifies a sample of every agent's citations independently, challenges each feature against the eight audit questions. Batch 1 agents' positions are then put against the audit; disagreements preserved in `CLAIM-VERIFICATION.md`.
Synthesis by the coordinator; nothing in the synthesis is stated more strongly than the audited evidence supports.

## 7. Deliverables

`START-HERE.md`, `TENSR-SCIENCE-REPORT.md`, `TENSR-FEATURE-EVIDENCE-MATRIX.csv`, `STUDY-EVIDENCE-TABLE.csv`, `CLAIM-VERIFICATION.md`, `TENSR-VALIDATION-PLAN.md`, `SEARCH-LOG.md`, `OPEN-QUESTIONS.md`, all in `docs/research/`.

---

## Change log

| date | change | reason |
|---|---|---|
| 2026-11-02 | protocol registered | — |
| 2026-11-02 | Full-text, DOI and PubMed access found blocked; all sources assessed at abstract/secondary level, marked per study | environment network policy; recorded in SEARCH-LOG.md |
| 2026-11-02 | WebSearch budget (~200 per coordinator turn, shared) exhausted in batch 1; unverified items listed rather than guessed; auditor run in a later turn | tool limit |
| 2026-11-02 | Added a response round: A1-A5 answered the audit in writing; responses supersede original findings where they differ | reconcile rather than merge |
| 2026-11-02 | Audit random sample fixed at 15 rows, seed 20261102, over rows not on the named load-bearing list | reproducibility |
| 2026-11-02 | No new agents launched after the response round; coordinator wrote the deliverables from agent files | user asked to limit usage |

