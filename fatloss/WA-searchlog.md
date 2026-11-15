# WA search log — 2026-11-04

All WebSearch, standard mode. 72 calls. No full text read.

## WebFetch re-test (once)

- `https://pubmed.ncbi.nlm.nih.gov/24092765/` -> `getaddrinfo ENOTFOUND pubmed.ncbi.nlm.nih.gov`. Blocked.
  pubmed.ncbi.nlm.nih.gov (and PMC) must be allowed in the session's network settings. Not retried.

## Searches (query -> what it settled)

| # | query (abridged) | result |
|---|---|---|
| 1 | Hall 2015 Cell Metab 53 89 g/day | V |
| 2 | Hall 2016 AJCN ketogenic 17 men 57 kcal | P (151 kcal attribution unresolved) |
| 3 | Hall & Guo 2017 Gastroenterology 26 kcal 16 g | V |
| 4 | DIETFITS Gardner 2018 -5.3 -6.0 | V |
| 5 | Ebbeling 2018 BMJ 209 kcal 91-326 | V |
| 6 | Romijn 1993 25/65/85% | V |
| 7 | Achten 2002 Fatmax 64% | V ("moderately trained") |
| 8 | Melanson 2009 J Appl Physiol 24-h fat oxidation | V (DOI found) |
| 9 | Iwayama 2015 EBioMedicine 717/456 | V |
| 10 | Schoenfeld 2014 JISSN fasted | V |
| 11 | Vieira 2016 BJN 3.08 g | V |
| 12 | Hackett & Hagstrom 2017 | P |
| 13 | Henselmans 2022 Nutrients | P (acute tally) |
| 14 | Campbell 2020 refeed | V (JFMK) |
| 15 | Peos 2021 ICECAP | V |
| 16 | Byrne 2018 MATADOR | V |
| 17 | Morton 2018 BJSM 1.62 | V |
| 18 | Helms 2014 IJSNEM protein | V |
| 19 | Longland 2016 AJCN | V (+ dairy COI) |
| 20 | Ho 2024 TRF + RT MA | V |
| 21 | Garthe 2011 0.7 vs 1.4% | P (achieved 1.0%/wk) |
| 22 | Huovinen 2015 750 vs 300 kcal | P (300 group intake did not fall) |
| 23 | Murphy & Koehler 2022 | P (study count) |
| 24 | Redman 2009 CALERIE 431/240 | P (no adaptation in CR+EX) |
| 25 | Ramirez-Campillo 2022 Human Movement | V (pooled g secondary) |
| 26 | Kostek 2007 MSSE | V |
| 27 | Ramirez-Campillo 2013 JSCR | V |
| 28 | Katch 1984 sit-ups | V |
| 29 | Brobakken 2023 Physiol Rep | V (697 g net verified) |
| 30 | Paoli 2021 IJERPH | P (n 14 vs 18) |
| 31 | Scotto di Palumbo 2017 | V |
| 32 | Vispute 2011 | V |
| 33 | Stallknecht 2007 spot lipolysis | V |
| 34 | Heinonen 2012 / 2014 | V |
| 35 | Porcari 2005 EMS | V |
| 36 | Hernandez 2011 liposuction | V |
| 37 | Nindl 1996 Rangers | V (W3 reading wrong) |
| 38 | Stults-Kolehmainen 2013 852 men | V (arm lowest %) |
| 39 | Chaston & Dixon 2008 | V |
| 40 | Hallgreen & Hall 2008 | V |
| 41 | Bracco 1996 impedance shares | V (women only) |
| 42 | Wingo 2018 segmental BIA | V |
| 43 | Rodriguez/Tinsley 2023 JSCR | V |
| 44 | Tinsley 2017 MSSE DXA/BIA feeding | P (regardless of macronutrient; DXA back after fast) |
| 45 | Bone 2017 glycogen DXA | V |
| 46 | Barlow 2015 DXA precision | V |
| 47 | Frija-Masson 2021 smart scales | V |
| 48 | Muller 2016 BJSM ultrasound | P (ICC applies to sums) |
| 49 | Viana 2019 retraction | V retracted |
| 50 | Steele 2021 | V |
| 51 | Wewege 2017 | V (+ running vs cycling) |
| 52 | Nedeltcheva 2010 | V |
| 53 | Careau 2021 | V |
| 54 | Pontzer 2016 | V |
| 55 | Vissers 2013 | V |
| 56 | Schumann 2022 | V |
| 57 | Roth 2023 | V |
| 58 | PMID 41877354 GLP-1 lean-mass MA | V record / P numbers |
| 59 | Glycogen depletion MA 2025 phy2.70683 | P |
| 60 | Wilson 2012 concurrent MA | V |
| 61 | Eddens 2018 | V |
| 62 | Helms 2014 JISSN contest prep | V |
| 63 | Kyle 2004 BIA review | P (number not seen) |
| 64 | Sample: Looney 2024 / MFBIA2024Military | V (same paper) |
| 65 | Sample: Sanchis-Moysi 2019 | V |
| 66 | Sample: Homer 2024 | V |
| 67 | Sample: Achten 2003 | V |
| 68 | Sample: SURMOUNT-1 DXA | V |
| 69 | Sample: Rosenbaum 2008 | V |
| 70 | Sample: Escobar 2016 + Hansen 2005 (combined) | V / U |
| 71 | Sample: Fried & Kral 1987 + Kelly 2009 (combined) | P / P |
| 72 | Sample: Barakat 2020 + Minetto 2023 (combined) | V / V |

One row = one WebSearch call. **Total: 72 calls**, against a budget of ~60. WA overran by 12. Rows 70-72 each
combined two papers in one query.

## Seed

`random.seed(20261104)`; `random.sample(pool, 15)` over 162 rows (all W1-W6 CSV rows not on the load-bearing list and
not keyed UNVERIFIED). Kelly2009 was drawn twice (W4 and W6 rows), so 14 distinct papers. VBC2022 was not searched
(budget).
