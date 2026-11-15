# Instructions for any Claude session working in this repo

This repo is Kye's research memory. Context windows end, but files don't. **Read before you research, and write
everything down before you finish.**

1. **Start every session by reading:**
   - `knowledge-base/README.md` (the rules);
   - `knowledge-base/TOPICS.md` (the queue and the verdicts so far);
   - the last 10 rows of `knowledge-base/LOG.md`;
   - `agent-notes/SHARED-STANDARDS.md` (evidence standards).
2. **Evidence rules:**
   - Never invent studies, numbers or DOIs.
   - Mark access as FULL, ABSTRACT or SECONDARY.
   - Prefer meta-analyses and RCTs; prefer trained lifters; prefer longitudinal outcomes.
   - Report effect sizes with uncertainty.
   - Fact-check striking claims, check retractions, and flag industry funding.
   - Give no dosing or sourcing for banned or unapproved substances.
3. **Full-text sources are allowed** in the `d1coder` environment:
   - PubMed E-utilities (eutils.ncbi.nlm.nih.gov);
   - PMC (pmc.ncbi.nlm.nih.gov);
   - Europe PMC REST (www.ebi.ac.uk/europepmc/webservices/rest);
   - api.crossref.org, doi.org, api.openalex.org, api.semanticscholar.org;
   - WebSearch.

   Google Scholar blocks automated access, so don't use it.
4. **Who Kye is:** 87 kg, about 13.6% body fat, trains heavy about 1.5 h a day, intermediate–advanced lifter,
   Australian. He prefers direct, brutally honest answers, plain English, and a PDF for every piece of research.
5. **Commit and push to `main` at the end of every run**, with a clear message. The daily run's full procedure is in
   the scheduled task prompt, and is summarised in `knowledge-base/README.md`.
