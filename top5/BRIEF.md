# Top-5 hypertrophy factors — research brief (registered 2026-11-02, before searching)

**Question from Kye.** For intermediate-to-advanced lifters, what are the five most important *working-set / training*
factors for muscle growth (effort is presumed #1 — test that too), how strong is the evidence for each (as many
studies as can be found and checked), *why* each works (mechanism), and how could TENSR track at least three of them —
with the current board or with added components?

**Population focus.** Resistance-trained (≥1 yr consistent training). Untrained-only evidence is reported but
down-weighted and labelled.

**Ranking criteria for "most important"** (each agent scores its factor on these, the coordinator ranks):
1. Size of the effect on hypertrophy (SMD/ES or % difference) at realistic contrasts.
2. Certainty (number of studies, consistency, risk of bias, MRI/ultrasound quality).
3. Evidence in trained lifters specifically.
4. Whether a lifter can actually control it set to set.
5. Dose-response shape (is there a plateau, a threshold, a harm zone?).

**Rules.** Same as `../agent-notes/SHARED-STANDARDS.md`: never invent a study, number or DOI; mark access (FULL /
ABSTRACT / SECONDARY / via-meta-analysis); separate acute signalling from longitudinal growth; no non-significance
read as equivalence. **Fact-check any striking result**: find replications or contradictions, check sample size,
trained status, measurement method, conflicts of interest, retraction status.

**Counting studies honestly.** "Hundreds of studies" is achievable only via meta-analyses that pool them. List every
meta-analysis/systematic review you find with its number of included studies and participants, and list primary
studies individually where you can identify them (access = "listed in <meta-analysis>" if that is all you saw).
Do not double count: record which meta-analyses overlap.

**Search budget.** WebSearch is shared, ~200 per coordinator turn across all agents: use at most ~30. Try WebFetch
on PMC/doi.org once; if it is blocked, say so and carry on.

**Output** (write only inside `docs/research/top5/`):
- `<ID>-findings.md` — top: 10-line summary + scorecard on the 5 ranking criteria; then evidence, mechanism ("why it
  works", with evidence code M/A/I), trained-lifter specifics, striking results fact-checked, open disputes.
- `<ID>-studies.csv` — header exactly:
  `key,factor,citation,doi_or_link,design,n_studies_or_participants,trained_status,outcome_measure,result_effect_uncertainty,mechanism_note,access,verification`
  (quote all fields).
- `<ID>-searchlog.md`.
