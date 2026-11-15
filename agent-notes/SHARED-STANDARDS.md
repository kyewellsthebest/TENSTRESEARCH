# Shared standards for every research agent

Read `docs/research/PROTOCOL.md` first (hardware facts §1, evidence codes §5).

1. Never invent a citation, DOI, statistic, sample size or method detail. If you cannot verify it, write UNVERIFIED and say what you could and could not reach.
2. Mark access per source: FULL (full text read), ABSTRACT (abstract only), SECONDARY (only seen via a review/another paper — say which).
3. Use reviews to map; open the primary studies behind any conclusion that matters.
4. Separate: acute physiology vs measurement validation vs longitudinal training outcome. An acute EMG difference is never evidence of a long-term training effect on its own.
5. Use evidence codes D / I / M / A / H and strengths strong / moderate / limited / very limited / none.
6. Report effect sizes and uncertainty (CI, SD, limits of agreement, SEM/MDC) where available, not just p-values. Non-significance ≠ equivalence. Correlation ≠ individual predictive accuracy.
7. Flag: small n, multiple comparisons, selective reporting, untrained-only samples, overlapping samples across meta-analyses, conflicts of interest, retractions/corrections.
8. Always ask: does this transfer to ONE bipolar dry-electrode channel at 25.4 mm IED on a band, with an IMU on the same puck, in an uncontrolled gym, on arbitrary exercises?

## Output (write both files; the coordinator merges them)

- `docs/research/agent-notes/<ID>-findings.md` — your findings, organised by question, every claim tagged with evidence code + strength + citation key.
- `docs/research/agent-notes/<ID>-studies.csv` — one row per materially important study, header exactly:
  `key,citation,doi_or_link,status,design,n,participants,evidence_category,exercise_muscle_contraction,hardware_processing,comparator_reference,results_effects_uncertainty,limitations_coi,tentsr_applicability,evidence_code,access,found_by`
  (quote every field; `found_by` = your ID). `key` = FirstAuthorYear (add a/b if needed).
- Append every search you ran (string, source, date, useful hits) to `docs/research/agent-notes/<ID>-searchlog.md`.

Do not edit any file outside `docs/research/agent-notes/`. Do not change firmware, hardware or claims.
