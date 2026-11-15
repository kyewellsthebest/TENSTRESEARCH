# FA — search log

Agent FA, 2026-11-02. 70 WebSearch calls (standard mode), 1 WebFetch. All results were search-engine summaries.

## Fetch re-test

| # | call | result |
|---|---|---|
| F1 | WebFetch `https://doi.org/10.1007/s40279-025-02344-w` | `getaddrinfo ENOTFOUND doi.org`. Blocked. Not retried. |

## Board inspection (no search budget)

- `fputil.footprints(fputil.load(...))` returns pads as tuples without nets.
- Pad nets read by regex over `hardware/kicad/routed.kicad_pcb` footprint blocks: split on `\n  (footprint\n`,
  reference from `reference\n "X"`, pads split on `\n    (pad\n`, net from `(net k "NAME")`.
- Output recorded in `FA-audit.md` §2.

## Random sample

```python
# run in docs/research/top5/
import csv, random
named = [...]  # lower-case substrings of every key on the named list (refalo, grgic2022, robinson2024, hermann,
               # martikainen, santanielo, jukic2023, pareja, schoenfeld2017, krieger, pelland, baz, brigatto,
               # schoenfeld2019, rantila, remmert, barbalho, maeo, pallar, wolf2023, wolf2025, kassiano, goto,
               # gschneidner, larsen, varovic, warneke2024, currier, enes2025, silva2025, amdi, plotkin, davies2021,
               # cumming, singer, longo, souza, moesgaard, coleman2024, dankel, morton2018, jukic2024, banyard,
               # orange2019, vmaxpro, held2021, w8, qwik, plos2024, seel, fang2023, magfree, weygers)
rows = [(f, r['key']) for f in ['F1','F2','F3','F4','F5','F6']
        for r in csv.DictReader(open(f + '-studies.csv')) if not any(n in r['key'].lower() for n in named)]
random.seed(20261102)
sample = random.sample(rows, 15)   # 190 rows in the pool
```

Drawn: Ogasawara2013, Morton2016, Drummond2009, Cardiff2024, Lee2024_Amode, Ostrowski1997, Vigotsky2022,
BenavidesVillanueva2022, Nobrega2018, AlMohimeed2012, Damas2019freq, Schoenfeld2015a, VargasMolina2025,
ST_LSM6DSO_DS, Zhang2025.

## Searches

| # | query (abridged) | used for | outcome |
|---|---|---|---|
| 1 | Kassiano 2023 calf raise initial/final/full medial/lateral | Kassiano | medial 15.2 / 6.7 / 3.4 (one summary) |
| 2 | "10.1007/s40279-025-02344-w" | Pelland DOI | no hit |
| 3 | Kassiano title + 14.9 / 6.2 / 7.3 | Kassiano | quote: "+15.2 vs FINAL +6.2, P<0.024 … FULL +7.3, P=0.060"; lateral 14.9 |
| 4 | Pelland Zourdos dose response Sports Med 2026 | Pelland | 67 studies / 2,058; fractional best; frequency negligible |
| 5 | Refalo 2023 proximity-to-failure meta | Refalo 2023 | V |
| 6 | Kassiano "INITIALROM" 3.4% lateral 6.7% | Kassiano | both heads reconstructed; resolution |
| 7 | Grgic 2022 JSHS failure meta | Grgic | V; 2 of 7 trained |
| 8 | Robinson 2024 dose-response proximity | Robinson | P; study counts not found |
| 9 | Refalo 2024 J Sports Sci | Refalo 2024 | P; 0.181 not found |
| 10 | Hermann 2025 MSSE single set | Hermann | V |
| 11 | Martikainen 2025 RIR 4→1 | Martikainen | P; triceps detail |
| 12 | Santanielo 2020 Biol Sport | Santanielo | V |
| 13 | Jukic 2023 VL meta | Jukic 2023 | P; unit unstated |
| 14 | Pareja-Blanco 2020 MSSE 0/10/20/40 | PB 2020 | not found; JSCR 2026 same design surfaced |
| 15 | "Velocity Loss as a Critical Variable…" | PB 2020 | not found |
| 16 | Pareja-Blanco 2017 SJMSS | PB 2017 | V |
| 17 | Schoenfeld 2017 volume meta | Schoenfeld 2017 | P; 0.37% not found |
| 18 | Krieger 2010 | Krieger | V |
| 19 | Baz-Valle 2022 J Hum Kinet | Baz-Valle | V + counting caveat |
| 20 | Brigatto 2022 | Brigatto | V |
| 21 | Schoenfeld 2019 MSSE volume | Schoenfeld 2019 | V |
| 22 | Räntilä 2026 | Räntilä | P; co-author Ahtiainen |
| 23 | Barbalho retraction IJSPP / women | Barbalho | men retracted |
| 24 | Remmert 2025 preprint per-session | Remmert | V; Pelland ~31 sets/wk point |
| 25 | Barbalho women MSSE retraction | Barbalho | PubMed: Retracted Publication |
| 26 | Maeo 2023 overhead triceps | Maeo 2023 | V |
| 27 | Wolf 2023 IJSC partial ROM meta | Wolf 2023 | P |
| 28 | Wolf 2025 PeerJ | Wolf 2025 | V |
| 29 | Goto 2019 partial ROM triceps | Goto | P; 49/28 from forum |
| 30 | Gschneidner preprint | Gschneidner | P; n from blog |
| 31 | Varovic 2025 IJSM | Varovic | P; 21.8% not found |
| 32 | Warneke 2024 SMO stretching | Warneke | V |
| 33 | Larsen 2025 EJSS | Larsen | V (n = 23) |
| 34 | Pallarés 2021 SJMSS | Pallarés | V |
| 35 | Maeo 2021 MSSE | Maeo 2021 | V |
| 36 | Currier 2023 BJSM | Currier | V |
| 37 | Enes 2025 tempo meta | Enes | V |
| 38 | Amdi & King 2025 | Amdi & King | V |
| 39 | Silva 2025 ecc vs con | Silva | P; 26 studies unconfirmed |
| 40 | Plotkin 2022 PeerJ | Plotkin | V |
| 41 | Cumming 2025 JAP | Cumming | P; author not confirmed |
| 42 | Davies 2021 cluster sets | Davies | V |
| 43 | Longo 2022 rest × volume load | Longo | V (JSCR) |
| 44 | Coleman 2024 deload | Coleman | P |
| 45 | Jukic 2024 RIR–velocity | Jukic 2024 | P; squat only |
| 46 | Held 2021 Vmaxpro | Held | P; conflicting n and ICC |
| 47 | Banyard 2017 PUSH | Banyard | V (n = 10) |
| 48 | Weakley 2021 VBT device review | Weakley | U; secondary + 2025 framework review |
| 49 | W8-Scope 97.5% | W8-Scope | P; magnetometer-based |
| 50 | PLOS ONE 2024 VBT apps | PLOS 2024 | V |
| 51 | RIR–velocity single-joint / isolation | engineering C4 | no velocity-RIR validation in isolation |
| 52 | Enode / Vitruve / Beast validity | engineering C2 | EnodePro failed on Smith (Sensors 2025) |
| 53 | two-IMU elbow angle in resistance exercise | engineering C7 | 1–7° lab; none in curls |
| 54 | Souza-Junior 2011 | Souza-Junior | V |
| 55 | Moesgaard 2022 | Moesgaard | P |
| 56 | Morton 2018 protein | Morton 2018 | P; trained moderator |
| 57 | Zhang 2025 supersets | sample | V |
| 58 | Damas 2019 frequency | sample | P |
| 59 | Ogasawara 2013 | sample | V |
| 60 | Drummond 2009 | sample | V |
| 61 | Nóbrega 2018 | sample | P |
| 62 | Lee 2024 A-mode | sample | V |
| 63 | Ostrowski 1997 | sample | P |
| 64 | Vargas-Molina 2025 | sample | V |
| 65 | LSM6DSO SDx/SCx Mode 1 | sample | P |
| 66 | exercise variation SR (Kassiano 2022) | ranking D4 | found |
| 67 | Dankel/Loenneke differential responders | Dankel | P; n = 151 |
| 68 | Hamilton 2024 JBMT pose (F6 "Cardiff2024") | sample | P |
| 69 | Benavides-Villanueva 2022 | sample | P; journal corrected |
| 70 | AlMohimeed & Ono 2012 | sample | V |

Total: **70 WebSearch calls**,
inside the ~70 budget.

## Not searched (carried or left open)

- Singer 2024, Morton 2016, Vigotsky 2022, Schoenfeld 2015a, Orange 2019: A6-verified; not re-searched.
- Baz-Valle 2021, Seel 2014, MagFree 2020, Fang 2023, Weygers: not searched by name.
- ADS1292R pin numbering against the TI datasheet: not searched.
