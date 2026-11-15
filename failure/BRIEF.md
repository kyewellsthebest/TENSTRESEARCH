# Failure / effort tracking — research brief (registered 2026-11-03, before searching)

**Kye's framing (adopted).** Effort — how close a set gets to muscular failure — is the most important growth
factor, so *tracking proximity to failure is TENSR's core feature*, not a side feature. Earlier rounds established:
effort is #1 (as a threshold); failure vs 1–3 RIR adds little for trained lifters; no wearable has yet shown it can
estimate reps-in-reserve better than the lifter. This round's job is constructive: **how do we make failure/effort
tracking work, and how well can it work?**

**Questions.**
1. What physiologically happens as a set approaches failure, and which measurable signals change most reliably and
   earliest (EMG amplitude, spectral shift, rep duration / velocity slow-down, ROM shrink, tremor/MMG, oxygenation,
   compensation patterns)? Which separate "2 reps left" from "failure now"?
2. What has actually been achieved detecting failure or estimating RIR/RPE with sensors during dynamic lifting
   (EMG, IMU, bar velocity, MMG, NIRS, fusion, ML)? Best results, with honest error, validation design, and replication.
3. Do velocity / rep-duration methods (velocity loss, minimal velocity threshold, last-rep velocity, concentric
   slow-down) work beyond barbell squat/bench — dumbbells, machines, cables, isolation lifts — and from a limb-worn
   sensor instead of a bar sensor?
4. How should TENSR detect failure, estimate proximity to it, and present it (a per-set "how close you got" effort
   readout, a live proximity cue, a failure/stall flag), using the current board first, then the second-puck clip?
   What calibration, what validation, and what would make it better than the lifter's own guess?

**Population.** Intermediate–advanced lifters. **Rules** as `../top5/BRIEF.md` and `../agent-notes/SHARED-STANDARDS.md`:
no invented studies or numbers, mark access, fact-check striking results, report error not just accuracy, flag
subject-dependent splits and data leakage.

**Output** (only inside `docs/research/failure/`): `<ID>-findings.md` (10-line summary first), `<ID>-studies.csv` with header
`key,topic,citation,doi_or_link,design,n,trained_status,exercise,sensor_or_method,target_definition,validation_design,result_error_uncertainty,limitations,access,verification`
(quote all fields), `<ID>-searchlog.md`. Search budget ~35 WebSearches per agent (shared pool).
