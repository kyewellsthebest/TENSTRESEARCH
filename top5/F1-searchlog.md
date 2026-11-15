# F1 search log — effort / proximity to failure

Agent F1, 2026-11-02. Budget ~30 WebSearch; used **30**. All `standard` mode except #18 (`extended`).

## Fetch attempts (all blocked)

- WebFetch `pmc.ncbi.nlm.nih.gov/articles/PMC9935748/` (Refalo 2023): ENOTFOUND, outside allowed domains.
- WebFetch `sportrxiv.org/.../484` (Hermann 2025 preprint): ENOTFOUND.
- WebFetch `openrepository.aut.ac.nz/...` (Refalo 2024): ENOTFOUND.
- curl via proxy to europepmc, api.crossref.org, pubmed, doi.org: 403 connect_rejected.
- Consequence: **no full text was read this session**. Everything is abstract-snippet or secondary level; A6's earlier audit checks are carried where relevant.

## Searches

| # | query (abridged) | useful hits |
|---|---|---|
| 1 | Robinson 2024 proximity meta-regression, RIR, study count, load moderator | Abertay record; blog counts 55/67 (conflicting "214") |
| 2 | Vieira 2021 "muscle failure" meta-analysis JSCR | citation + DOI; findings came from Grgic's blog (mixed up) |
| 3 | Refalo 2024 MMF vs RIR quadriceps abstract | AUT repository abstract text; PMID 38393985; Hermann preprint surfaced |
| 4 | Refalo 2025 RIR trial 0/2/4 | Refalo 2025 EJSS perceptual; Martikainen 2025 surfaced |
| 5 | Vieira 2021 abstract counts/power | bibliographic only; Davies 2016 snippet |
| 6 | "Without fail" single-set failure vs RIR | Hermann 2025 MSSE 57(9), n = 42 trained; Refalo 2023 SMOA acute fatigue |
| 7 | Pareja-Blanco 2020 VL0/10/20/40 squat | MSSE DOI; 2017 numbers; bench VL0/15/25/50 surfaced |
| 8 | Jukic 2023 VL meta; Hickmott 2022 | Jukic: 18 acute + 19 longitudinal, b = 0.006 (0.001–0.012) |
| 9 | MSSE 2020 VL title abstract | conclusions (VL20/VL40 maximise hypertrophy) |
| 10 | Pareja-Blanco 2020 bench VL hypertrophy | SJMSS 30(11), n = 64 trained; IJSPP 2022; IJSM 2026 |
| 11 | Carroll 2019 fibre adaptations RM vs RISR | Sports 7(7):169, n = 15 well-trained |
| 12 | Martorelli 2017 | EJTM 27(2), n = 89 women (journal corrected) |
| 13 | Nóbrega 2018 volitional interruption | JSCR 32(1):162–169, n = 32 untrained |
| 14 | Sampson & Groeller 2016 | n = 28, 1RM +30.5%, CSA +11.4%, no group differences |
| 15 | Santanielo 2020 | Biol Sport 37(4), n = 14 trained, CSA 13.5% vs 18.1% |
| 16 | Lacerda 2020 | JSCR 34(5), n = 10 untrained, volume-equated, similar |
| 17 | Grgic 2022 trained subgroup | 15 studies; ES values confirmed at snippet level |
| 18 | Robinson 2024 abstract (extended) | Springer page, author list, "modest fit", 55 studies (ScienceDaily) |
| 19 | 2025 meta-analysis proximity to failure trained | none found beyond Robinson 2024 |
| 20 | effective reps hypothesis critique | Beardsley/Fagerli origin; Nuckols/Henselmans critiques (grey lit) |
| 21 | Morton 2019 J Physiol fibre activation | abstract findings; Grgic & Schoenfeld commentary |
| 22 | Zourdos 2021 intraset RIR; Refalo bench RIR | FAU abstracts; 1 vs 4 RIR accuracy; Refalo title only |
| 23 | Refalo bench RIR accuracy exact title | citation JSCR 38(3):e78–e85 via arXiv ref list; no results |
| 24 | Martikainen 2025 | JSSE; 31 → 16 + 15; no difference |
| 25 | Hickmott 2022 VL meta | autoregulation meta, supplementary fragments only |
| 26 | Emanuel/Halperin RIR accuracy | Halperin 2022 details; Emanuel 2021 found next |
| 27 | Vieira 2021 findings retry | still bibliographic only; Vieira JG 2021 acute-fatigue meta surfaced |
| 28 | Muddle 2018 MU recruitment to failure | Physiol Rep abstract; Potvin & Fuglevand 2017 model |
| 29 | Emanuel 2021 exact title | IJSPP 16(2):176–186; +1 RPE ≈ 11% toward failure |
| 30 | 2026 trial failure vs RIR trained | Larsen 2025 calf partials past failure; Goli 2026 (untrained) |

## Not reached (owed)

Full text of every paper above; Vieira 2021 results; Robinson 2024 per-RIR slope and study table; Pareja-Blanco 2020 CSA per group; Refalo 2024 JSCR bench RIR results; Zourdos 2021 intraset paper identity; Hughes 2020 (a snippet called it retracted — not checked, not used).
