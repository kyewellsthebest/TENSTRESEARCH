# F2 search log — training volume and frequency

Agent F2, 2026-11-02. WebSearch budget: **35 used**, against the brief's limit of ~30. That is 5 over.

## Network access

- `WebFetch https://pubmed.ncbi.nlm.nih.gov/...` failed with **ENOTFOUND**, so the host is outside the session's allowed domains.
- `WebFetch https://sportrxiv.org/...` (the Pelland preprint) also failed with **ENOTFOUND**.
- I made no more fetch attempts, as the brief instructs. **No full text was read.** Every source came through WebSearch, which returns a search-engine summary of abstracts, repository records and blogs.
- The summaries sometimes mix figures from the primary abstract with figures from blogs. Where a number came only from a blog or podcast page, it is marked SECONDARY (blog) in the CSV.

## Searches

| # | query (abridged) | mode | useful hits |
|---|---|---|---|
| 1 | Pelland 2026 Sports Med dose-response meta-regression weekly sets fractional | std | sponet record (Sports Med 56:481–505); fractional coding; frequency affects strength only; preprints.org 202610.1022 reanalysis (once-weekly 9 sets = 0.69 of 3×/wk gain) |
| 2 | Pelland Zourdos "Resistance Training Dose Response" sportrxiv posterior probability | ext | Semantic Scholar; ResearchGate PDF header "Sports Medicine https://doi.org/10.1007/s40279-025-02344-w" (**resolves A6's unverifiable DOI**); frequency–hypertrophy 91.3% posterior |
| 3 | Pelland weekly sets "fractional" per set PUOS | std | blogs: 67 studies / 2,058 participants; MED ≈ 4 fractional sets/wk (blog); Remmert per-session PUOS ≈ 11 fractional sets for hypertrophy |
| 4 | Pelland abstract weekly volume posterior probability fractional | std | 35 studies / 220 hypertrophy effects (via reanalysis); frequency marginal slope 0.32%/session (95% CrI −0.14 to 0.82), secondary only |
| 5 | Pelland marginal slope % per set CrI | std | no per-set slope found; OSF archive named |
| 6 | Schoenfeld Ogborn Krieger 2017 volume meta J Sports Sci | std | J Sports Sci 35:1073–82; 15 studies / 34 treatment groups; <5, 5–9, 10+ sets = 5.4/6.6/9.8% (author blog); Räntilä 2026 found |
| 7 | "Exploring the Upper Limits of Resistance Training Volume…" | std | Räntilä & Ahtiainen, J Sci Sport Exerc 2026, DOI 10.1007/s42978-026-00387-7; n = 27 trained; ~40 vs ~60 sets/wk; no extra hypertrophy |
| 8 | Baz-Valle 2022 J Hum Kinet weekly sets trained | std | J Hum Kinet 81:199–210; 7 RCTs (6 meta-analysed); 12–20 vs >20: quads p = 0.19, biceps p = 0.59, triceps p = 0.01 favouring high |
| 9 | Schoenfeld 2019 MSSE volume trained men | std | MSSE 51(1):94–103, DOI 10.1249/MSS.0000000000001764; n = 34; 1/3/5 sets/exercise; 8 wk; dose-response for hypertrophy, not strength |
| 10 | Barbalho retraction | std | Retraction Watch: IJSPP retracted the men's "ceiling effect" volume paper; the women's paper was challenged and its status is unresolved |
| 11 | Brigatto 2022 16/24/32 sets | std | PubMed 31868813; 32 > 16 for lower-body MT and 1RM; 24 not different from either; 1-min rests |
| 12 | Aube 2022 12/18/24 sets | std | n = 35 trained, quads; DOI 10.1519/JSC.0000000000003524; hypertrophy result conflicts across secondary sources |
| 13 | Enes 2024 weekly set progressions | std | MSSE DOI 10.1249/MSS.0000000000003317; n = 31; constant 22 sets vs +4 or +6 sets per fortnight; strength dose-response, VL CSA p = 0.067, quad MT p = 0.076 |
| 14 | Haun 2019 high volume | std | Haun 2018 Front Nutr (extreme volume, ECW critique); Vann 2022 Front Physiol |
| 15 | Haun "Muscle fiber hypertrophy … sarcoplasmic" | std | PLoS ONE 2019;14:e0215267; n = 30 trained (15 responders analysed); fCSA +23%, actin/myosin concentration −30% |
| 16 | Heaselgrave 2019 biceps 9/18/27 | std | IJSPP, DOI 10.1123/ijspp.2018-0427; n = 49 trained; 4.3/9.5/5.4% (secondary); frequency confounded |
| 17 | Krieger 2010; Radaelli 2015 | std | Krieger: 8 studies, 55 ES; multiple > single by ES 0.10 (0.02–0.19); 0.24/0.34/0.44. Radaelli: 48 untrained, 6 mo, 5 sets > 1 and 3 for elbow flexor MT |
| 18 | Ostrowski 1997 | std | JSCR 11(3):148–154; 27 trained men; 3/6/12 sets; similar strength and size |
| 19 | Schoenfeld 2019 frequency meta | std | 25 studies; volume-equated frequency not significant; ES 0.07 (−0.02 to 0.17) quoted by a preprint, conflicts on the k |
| 20 | Schoenfeld 2016 frequency meta | std | Sports Med 46(11):1689–97; 10 studies; 0.49 ± 0.08 vs 0.30 ± 0.07, p = 0.002; mostly not volume-equated |
| 21 | Hammarström 2020 J Physiol ribosome | std | n = 34 untrained, within-subject 1 vs 3 sets, 12 wk; 3 sets better on average; 13/34 meaningfully more hypertrophy (secondary) |
| 22 | Damas 2019 frequency within-subject | std | JSCR 2019; n = 20 legs, 5×/wk vs 2–3×/wk; no group difference; individual pattern split; training status UNVERIFIED |
| 23 | Grgic 2018 frequency strength meta | std | volume-equated subgroup p = 0.421; Ralston 2018 Sports Med Open (PMC6081873); Grgic, Schoenfeld & Latella 2019 J Sci Med Sport review |
| 24 | "hard sets" definition; Baz-Valle 2019 | std | blogs only: 0–3 RIR, 6–20+ reps |
| 25 | Baz-Valle "Total number of sets as a training volume quantification method" | std | JSCR 35(3):870–878, DOI 10.1519/JSC.0000000000002776; 14 studies; sets valid for 6–20+ reps to or near failure |
| 26 | Remmert per-session meta-regression | std | SportRxiv DOI 10.51224/SRXIV.537; PUOS ≈ 2 direct sets per session (strength), ≈ 11 fractional sets per session (hypertrophy) |
| 27 | MPS time course MacDougall 1995 | std | +50% at 4 h, +109% at 24 h, ~baseline by 36 h (trained men); trained-state response is shorter |
| 28 | Burd 2010 1 vs 3 sets MPS | std | J Physiol 2010; n = 8; 3 sets > 1 set for MyoPS; Burd 2010 PLoS ONE (load) |
| 29 | Damas 2016 J Physiol | std | J Physiol 594(18):5209–22; MyoPS relates to hypertrophy only at weeks 3 and 10, after damage subsides |
| 30 | Barsuhn volume | std | J Appl Physiol 2025;138(1); 55 enrolled, 29 finished; +30% vs +60% vs maintain previous sets; maintaining was enough |
| 31 | Scarpelli 2022 | std | JSCR 36(4):1153–57; individualised (based on previous volume) beat standardised volume (secondary) |
| 32 | Ahtiainen 2016 responders | std | n = 287 untrained; 29% low responders for size against the control 95% CI |
| 33 | new volume metas 2023–2026 | std | nothing new beyond Pelland and Remmert; blogs disagree on the plateau (11 vs 43 sets) |
| 34 | Schoenfeld 2019 edema critique | std | Haun 2018 ECW critique (~20 sets/exercise/wk); Alvarez (7/14/21 sets): swelling resolved within 24 h, n = 13 |
| 35 | preprints.org 202610.1022 reanalysis | std | record not reached; authors unknown |

## Searches I wanted but did not run

These could not be verified this session:
- Pelland's per-set marginal slope and CrI; the paper's Table 2 or the OSF archive is needed.
- The exact training status of Damas 2019's participants.
- Schoenfeld 2019's per-site percentages.
- Grgic 2018's study count and k.
- Kumar 2009 (older men, MPS by number of sets).
- Figueiredo/Brook papers on ribosome biogenesis.
- Saric 2019 (3 vs 6 sessions per week) beyond its title record.
- The full status of the Barbalho women's paper.
