# Peptides — research brief (registered 2026-11-04, before searching)

**Kye's request.** Mass research on peptides used for physique, performance, recovery, fat loss, cognition and
"longevity". Rank them (a) most to least researched, (b) best to worst benefits, (c) side effects from mildest /
best-characterised to most serious / least known.

**Scope.** Peptides discussed in gym and wellness circles, plus approved peptide drugs relevant to body composition.
Also include MK-677 (ibutamoren), because it is commonly grouped with peptides; label it as a non-peptide.

**Rules** (in addition to `../agent-notes/SHARED-STANDARDS.md`):
- Never invent studies, numbers or DOIs. Mark access (FULL / ABSTRACT / SECONDARY).
- Separate the evidence levels: human RCTs; human non-randomised studies; human case reports; animal studies;
  in-vitro studies; anecdote and marketing.
- Report benefits ONLY as demonstrated outcomes, with population and effect size.
- **No dosing protocols, cycling advice, reconstitution or injection instructions, and no sourcing or vendor
  information for unapproved substances.** For approved drugs, cite trial doses only as context for the results.
- For every substance record: regulatory status (TGA Australia scheduling, FDA approval or the 2023 compounding
  category-2 list, WADA Prohibited List class); known adverse events and their frequency; unknowns, including
  long-term and cancer/growth-promotion concerns; and grey-market quality data (purity, contamination,
  mislabelling).
- Industry funding and the conflicts of interest of "peptide clinics" must be flagged.

**Research-volume metric.** Number of human RCTs and the approximate total participants, plus whether a phase-3
programme or an approval exists. A PubMed hit count is only a secondary indicator, and only if obtainable.

**Output** (only inside `docs/research/peptides/`):
- `<ID>-findings.md`: a 10-line plain-English summary, then one section per substance.
- `<ID>-studies.csv`, with header
  `key,substance,citation,doi_or_link,design,n,population,duration,outcome,result_effect_uncertainty,adverse_events,limitations_coi,evidence_level,access,verification`
  (quote all fields).
- `<ID>-scores.csv`, with header
  `substance,class,human_rcts,approx_participants,approved_anywhere,evidence_volume_rank_note,best_demonstrated_benefit,benefit_strength,main_adverse_effects,serious_risks,unknowns,tga_status,wada_status,fda_status`
  (one row per substance).
- `<ID>-searchlog.md`.

**Search budget:** about 30 WebSearches per agent.
