# FA — Independent audit of the top-5 hypertrophy-factor round (F1–F6)

Agent FA, 2026-11-02. Adversarial audit of F1–F6. Every verdict below comes from my own searches (`FA-searchlog.md`,
70 WebSearch calls) or my own parse of the board file. Nothing is taken on an agent's word. New and corrected rows are
in `FA-studies.csv`.

**Bottom line.**
- No load-bearing citation is fabricated. Every named study exists and its headline direction matches.
- **One number set is wrong and it matters: Kassiano 2023.** F3 put the lateral-head numbers on the medial head. A1
  had the medial numbers right; A6 "corrected" them wrongly; F3 then sided with A6. Medial initial-range partials beat
  full ROM **significantly** (p ≤ 0.009). Settled in §1c.
- **One engineering claim fails on its own source: W8-Scope.** Its 97.5% load identification uses a **magnetometer**
  sensing the iron plates. TENSR has no magnetometer, and F6 itself advises against adding one. F6's "stack mode =
  load ID, no respin" is unsupported.
- **One retraction status is wrong:** Barbalho's women's volume paper (MSSE 2019) is listed on PubMed as a
  *Retracted Publication*. F2 called it "unresolved".
- Board facts F6 used are **correct** pin for pin.
- On ranking: by the brief's own criteria **volume beats effort**. Effort's case for #1 rests on a contrast (sets far
  from failure) that has almost no trained-lifter data. And slots 4 and 5 of the coordinator view are not independent
  factors; they are implementation rules of #2 and #1. There are **three independent levers**, not five.

---

## 0. Access

- **WebFetch re-test, 2026-11-02:** `https://doi.org/10.1007/s40279-025-02344-w` returned
  `getaddrinfo ENOTFOUND doi.org`. Fetch is still blocked. doi.org (and PMC, PubMed) would have to be allowed in the
  session's network settings. Not retried.
- **Searches:** 70 WebSearch calls, standard mode.
- **Access level:** every verdict is at the level of search-engine summaries of abstracts, repository records and
  publisher snippets. **Nothing was read in full text.** VERIFIED means bibliographic details plus the headline
  numbers match an independent record. It does not mean methods were checked.
- **Search summaries contradict each other.** On Kassiano 2023 two summaries gave different numbers for the same head.
  I resolved it from the abstract's sentence structure (which head each p-value belongs to), not by majority vote.
  Treat any single-summary number below as provisional.
- **Retractions:** checked for Barbalho (both papers). Not exhaustively checked for anything else: the Retraction
  Watch database was not queryable. No other retraction surfaced in any search.

---

## 1. Citation verification

Verdicts: **V** verified · **P** partly (difference stated) · **U** unverifiable (reason stated) · **W** wrong.

### 1a. Effort (F1)

| item | verdict | what I found / what differs |
|---|---|---|
| Refalo 2023 Sports Med 53(3):649–665 | **V** | 15 studies; ES 0.19 (0.00–0.37), p = 0.045, any failure definition; momentary-failure subgroup no advantage; possible non-linearity. |
| Refalo 2024 J Sports Sci 42(1):85–101 | **P** | DOI 10.1080/02640414.2024.2321021; trained; FAIL vs 1–2 RIR similar quadriceps growth, 8 wk. **"0.181 vs 0.182 cm" not found** by my search (A6 had it). n = 26 is secondary only. |
| Grgic 2022 JSHS | **V** | 15 studies; hypertrophy 0.22 (−0.11 to 0.55); trained subgroup 0.15 (0.03–0.26); non-failure better for strength when volume not equated (−0.32). **Only 2 of 7 hypertrophy studies were trained.** |
| Robinson 2024 Sports Med 54(9):2209–2231 | **P** | DOI 10.1007/s40279-024-02069-2. Hypertrophy improves closer to failure; strength flat. Study counts (55/67) not found. "Strongest at 0–2 RIR" is a blogger's reading, not the paper's. |
| Hermann 2025 MSSE | **V** | DOI 10.1249/MSS.0000000000003728; n = 42 trained; single set × 9 exercises, 2×/wk, 8 wk; hypertrophy "leaned toward" failure, small absolute differences; strength and endurance similar. |
| Martikainen 2025 JSSE | **P** | DOI 10.1007/s42978-025-00338-8; 16 vs 15 completers, 10 wk; no between-group difference; lower session RPE in 4→1 RIR. **Omitted by F1:** triceps thickness rose only in the 4→1 RIR group (+5.8% vs +2.2%). It cuts slightly against "closer is better". |
| Santanielo 2020 Biol Sport | **V** | n = 14, within-leg, 10 wk; VL CSA +13.5% (failure) vs +18.1% (non-failure); similar. Non-failure is numerically higher. |
| Jukic 2023 Sports Med 53(1) | **P** | 18 acute + 19 longitudinal; hypertrophy b = 0.006 (0.001–0.012); strength unaffected; CMJ b = −0.040. **The unit of b is not stated in any abstract text.** F1 states "per percentage point" as fact; F4 correctly flags it UNVERIFIED. |
| Pareja-Blanco 2017 SJMSS 27(7):724–735 | **V** | 22 young men (VL20 n = 12, VL40 n = 10; two VL40 dropouts); VL40 more VL+VI hypertrophy; MHC IIX lost in VL40; CMJ +9.5% vs +3.5%; VL20 did 40% fewer reps. |
| Pareja-Blanco 2020 MSSE 52(8):1752–1762 | **U** | Two searches did not surface it. A same-design (VL0/10/20/40, squat) JSCR 2026 paper by Sánchez-Valdepeñas, Pareja-Blanco et al. (n = 51) did surface: CSA effect sizes largest at 40%, interaction n.s.; strength best at 20%. Do not quote MSSE 2020 numbers until checked. |
| Pareja-Blanco 2020 SJMSS (bench, VL0/15/25/50) | **P** | Title found in a repository PDF. n = 64 not confirmed. |

### 1b. Volume and frequency (F2)

| item | verdict | what I found / what differs |
|---|---|---|
| Schoenfeld 2017 J Sports Sci | **P** | DOI 10.1080/02640414.2016.1210197 (online 2016). 15 studies, 34 treatment groups; graded dose-response up to 10+ sets. **"0.37%/set" not found** (F2 already flags it). |
| Krieger 2010 JSCR 24(4):1150–1159 | **V** | 8 studies, 19 groups, 55 ES; multiple > single, difference 0.10 (0.02–0.19), p = 0.016; 0.24 / 0.34 / 0.44; 2–3 vs 4–6 p = 0.29. |
| Pelland 2026 Sports Med 56(2):481–505 | **P** | Citation, authors (Pelland, Remmert, Robinson, Hinson, Zourdos), 67 studies / 2,058 participants (now in a search summary of the abstract, not only blogs), fractional counting best, frequency compatible with negligible hypertrophy effect — all match. **DOI 10.1007/s40279-025-02344-w: exact-string search returned nothing, again.** F2's ResearchGate claim is not reproducible by me. Status stays UNVERIFIED-BY-SEARCH, not "verified". |
| Pelland 2026 — weekly point | **new** | The Remmert preprint cites Pelland as finding **no detectable superiority beyond ~31 fractional sets/week for hypertrophy** (~3 for strength). F2 wrote that the marginal gain was unreachable and "no clear plateau". F2 must add this. |
| Remmert 2025 SportRxiv 537 | **V** | Not peer reviewed. Per-session point of undetectable superiority ~11 fractional sets (hypertrophy), ~2 direct sets (strength). Same dataset as Pelland. |
| Baz-Valle 2022 J Hum Kinet 81:199–210 | **V** | 12–20 vs >20 sets: quads p = 0.19, biceps p = 0.59, triceps p = 0.01. **Caveat F2 omits:** multi-joint sets were counted toward arm volume, so the triceps result is not direct-set volume. |
| Baz-Valle 2021 JSCR | not re-searched | Carried; low stakes. |
| Brigatto 2022 JSCR 36(1):22–30 | **V** | 9 men per group (27), "intermediately trained"; 32 > 16 sets for lower-body MT and 1RM; 1-min rest. |
| Schoenfeld 2019 MSSE 51(1):94–103 | **V** | 34 trained men; 1/3/5 sets per exercise, 3×/wk, 8 wk; graded hypertrophy, strength similar. |
| Räntilä 2026 JSSE | **P** | Authors Räntilä & **Ahtiainen**; DOI 10.1007/s42978-026-00387-7; NOR n = 12 vs XTR n = 15 (~1.5× volume, targeting 40 vs 60 sets); non-response unaffected. **"No added growth" and "deadlift p = 0.043" not confirmed.** |
| Barbalho, IJSPP (men) | **V retracted** | Retraction Watch: retracted (April 2020 per one piece; another calls it a 2019 paper). Exclude. |
| Barbalho, MSSE 2019 51(3):515–522 (women) | **W in F2** | **PubMed publication type: "Retracted Publication".** Notice text not seen. F2 says "retraction status unresolved". Change to retracted. |
| Ostrowski 1997 JSCR 11(3):148–154 | **P** | 27 men, 3/6/12 sets per muscle per week, 10 wk, ultrasound; similar size; urinary T:C trend. **"Triceps 7/14/28" comes from a Summify entry that contradicts the abstract. Drop it.** |
| Damas 2019 (frequency) JSCR 33(4):897–901 | **P** | F2 had the citation UNVERIFIED. It exists; within-subject 5×/wk vs 2–3×/wk; no group difference; individuals split. n = 20 and "32% aligned" are secondary. |

### 1c. Muscle length / ROM (F3)

**Kassiano 2023 (JSCR 37(9):1746–1753; n = 42 untrained women; 8 wk) — RESOLVED.**

| head | initial (long) | full | final (short) | tests |
|---|---|---|---|---|
| **medial gastrocnemius** | **+15.2%** | **+6.7%** | **+3.4%** | initial > full and > final, **p ≤ 0.009** |
| **lateral gastrocnemius** | **+14.9%** | +7.3% | +6.2% | initial > final p < 0.024; initial vs full **p = 0.060** |

How settled: one summary quoted the medial sentence with 15.2/6.7/3.4 and p ≤ 0.009. A second quoted "+15.2% vs
FINAL +6.2%; P < 0.024 … FULL +7.3%; P = 0.060" and labelled it medial. A third reconstructed both sentences and
assigned 14.9/6.2/7.3 to the lateral head. Only the third reading makes every number and p-value fit two parallel
abstract sentences. Verdicts:
- **A1: right** (medial 15.2 / 6.7 / 3.4).
- **A6: wrong** to call A1 wrong. 6.2 and 7.3 are lateral.
- **F3: W.** It merged the heads (initial 15.2 medial with lateral full and final) and then used the lateral p = 0.060
  to argue "lengthened vs full not significant". **For the medial head it was significant.**

Consequence: F3's top-line ("lengthened partials beat full ROM is not established") survives on Wolf 2023 and the
trained nulls. Its use of Kassiano as support does not. Kassiano is the strongest untrained evidence *for* lengthened
partials over full ROM, on one head of one muscle.

| item | verdict | what I found / what differs |
|---|---|---|
| Maeo 2021 MSSE 53(4):825–837 | **V** | n = 20; seated vs prone; hamstrings +14% vs +9%; short head +10% vs +9%; damage protection similar. Untrained. |
| Maeo 2023 EJSS 23(7):1240–1250 | **V** | n = 21; long head +28.5% vs +19.6% (d = 0.61, p < 0.001); lateral+medial +14.6% vs +10.5%. |
| Pallarés 2021 SJMSS | **V** | 16 studies; strength ES 0.56 (p = 0.004); lower-limb hypertrophy ES 0.88 (p = 0.027). CIs not seen. |
| Wolf 2023 IJSC | **P** | Full vs partial SMD 0.12 (−0.02 to 0.26). Lengthened-partial subgroup −0.28 (−0.81 to 0.16), described by the authors as favouring partials. Study count 23 (secondary: 8 hypertrophy). Sign convention still not seen in a table. |
| Wolf 2025 PeerJ 13:e18904 | **V** | 30 trained, within-participant, 8 wk, 2×/wk, 4 exercises × 4 sets; similar MT and 10RM. |
| Goto 2019 JSCR 33(5):1286–1294 | **P** | 44 trained men (22/22), 45–90° vs 0–120°, 3×8RM, 8 wk; partial "more effective". **The +49% vs +28% figures trace to a forum post.** F3 labels them SECONDARY; they are UNVERIFIED. Single mid-belly slice (Henselmans critique). |
| Gschneidner preprint (SportRxiv 485) | **P** | 15-site cluster RCT, 12 wk, not peer reviewed. n = 297 (163 vs 134) and ES ≈ −0.03 arm / 0 thigh come from a blog only. CSA estimation method not confirmed. |
| Larsen 2025 EJSS (PMID 40850937) | **V** | n = 23 (16 men, 7 women) trained; 8 wk Smith calf raise; initial partials vs full + past-failure partials; +0.40 mm favouring initial (CrI −0.06 to 0.85), BF 1.2. Author order is inconsistent between DOAJ (Larsen first) and the preprint. |
| Varovic 2025 IJSM (DOI 10.1055/a-2615-4935) | **P** | 12 studies, Bayesian. Preprint said "small" effects favouring long; later summaries say "trivial". **The 21.8% length contrast was not found.** |
| Warneke 2024 SMO 10:45 | **V** | 42 studies, 1,318 participants; d = 0.20; higher doses d = 0.26–0.28; "minor effectiveness". "10–15 min/day" threshold is secondary only. |

### 1d. Load, tension, execution (F4)

| item | verdict | what I found / what differs |
|---|---|---|
| Currier 2023 BJSM 57:1211–1220 | **V** | 178 studies / 5,097 (strength); 119 / 3,364 (hypertrophy); top hypertrophy rank 0.66 (0.47–0.85) vs control; "choose by preference". |
| Enes 2025 JSCR 39(12):1331–1339 | **V** | 14 RCTs, 278 participants; ES 0.09 (CrI −0.04 to 0.22). Tested range per action conflicts between sources (0.25 or 0.5 to 4.5 s). |
| Silva 2025 JSCR 39(1):115–134 | **P** | DOI 10.1519/JSC.0000000000004981; 682 participants; SMD 0.285 (−0.131 to 0.701), p = 0.179, I² 84.4%, GRADE very low. **"26 studies" not confirmed** (only "25" in an age subgroup table). **Omitted by F4:** an upper-limb subgroup favoured eccentric (low certainty). |
| Amdi & King 2025 J Sports Sci 43(20):2447–2464 | **V** | 9 studies, 166 (46% trained); hypertrophy g = 0.05 (90% CI −0.22 to 0.33); strength in trained g = 0.33; CMJ favours short eccentrics g = −0.73. |
| Plotkin 2022 PeerJ 10:e14142 | **V** | 43 trained (22 LOAD / 21 REPS), 8 wk; RF 2.8 mm (CI90% −0.5 to 5.8) favouring reps; strength 2.0 kg favouring load. |
| Davies 2021 Sports Med 51(4):707–736 | **V** | 29 studies; hypertrophy ES −0.05 (−0.32 to 0.23); strength −0.05; power 0.02. |
| Cumming 2025 J Appl Physiol 139(3):685–697 | **P** | Within-subject 3–5RM vs 20–25RM to failure; MT ~7% mid, ~8% distal either way; single-joint 1RM 9% vs −3%; multi-joint 21 ± 10% both. **Author name not confirmed by search.** |
| Zhang 2025 Sports Med (supersets) | **V** | F4 had counts UNVERIFIED: 19 studies, 313 participants; hypertrophy SMD −0.05 (p = 0.87). |
| Benavides-Villanueva 2022 | **P** | Journal is *Rev Ciencias de la Actividad Física UCM* 23(1):1–12 (DOI 10.29035/rcaf.23.1.12), not "Revista chilena". 4 studies, 113 participants. The authors say slower tempos associated with more growth; F4's row does not say so. |

### 1e. Rest, recovery, progression (F5)

| item | verdict | what I found / what differs |
|---|---|---|
| Singer 2024 FSAL 6:1429789 | V (A6) | Not re-searched; A6 verified. |
| Longo 2022 JSCR 36(6):1554–1559 | **V** | 1 vs 3 min, with and without volume-load equating, 80% 1RM; "volume load rather than rest interval" drives hypertrophy. |
| Souza-Junior 2011 JISSN 8:17 | **V** | 22 **recreationally** trained men, all on creatine; 2 min constant vs 2 min→30 s; MRI CSA; no between-group difference despite more volume in the constant group. The creatine confound is the authors' own caveat. |
| Moesgaard 2022 Sports Med 52(7):1647–1666 | **P** | Conclusion verified (periodisation helps 1RM, not hypertrophy, volume-equated). **ES 0.13 and "35 studies" not found.** |
| Coleman 2024 PeerJ 12:e16777 | **P** | 1-week cessation mid-way through 9 weeks; no hypertrophy effect, lower-body strength cost. n = 39 not confirmed. |
| Dankel 2019/2020 APNM 45(5) | **P** | F5 had n UNVERIFIED: **n = 151**, three groups, elbow flexion, 6 weeks; no true individual variability for hypertrophy above random error. Short and single-muscle; do not generalise. |
| Morton 2018 BJSM 52(6):376–384 | **P** | 49 studies, 1,863; FFM **+0.30 kg (0.09–0.52)**; breakpoint ~1.6 g/kg/d. **Omitted by F5: effect larger in resistance-trained participants.** Stronger by Science disputes the breakpoint's precision. |

### 1f. Sensing (F6)

| item | verdict | what I found / what differs |
|---|---|---|
| Jukic 2024 Physiol Rep 12(5):e15955 | **P** | Individual (not general) RIR–velocity relationships: mean error <2 reps next session, all loads, **free-weight back squat only**. n = 46 not confirmed by my search. |
| Banyard 2017 IJSPP | **V** | **n = 10** strength-trained men; PUSH valid only for peak force; GymAware valid. |
| Orange 2019 | V (A6) | Not re-searched. |
| Held 2021 IJERPH 18(17):9170 (Vmaxpro) | **P** | Sources conflict: n = 19 or 16. One summary: ICC 0.91–0.96, LoA <0.12 m/s. The **PMC abstract**: reliability ICC 0.55–0.91, LoA <0.16 m/s; displacement LoA 7.8–10.7 cm. **F6 quotes only the best case.** |
| W8-Scope (PerCom 2020 / PMC 2021) | **P — misapplied** | 50 subjects, 14 exercises, 97.5% weight ID. **Sensor = accelerometer + magnetometer; the magnetometer senses the iron plates.** TENSR has no magnetometer. See C1. |
| PLOS ONE 2024 (Renner, Mitter, Baca) | **V** | Qwik VBT ≈ RepOne LPT; Metric and MyLift limited. MyLift missed 175 reps, **84% failure on bench**. F6's "up to 30%" is the all-lift average. |
| Weakley 2021 Sports Med (VBT devices) | **U** | Not retrieved directly. Secondary: LPTs most accurate; accelerometers "questionable", not recommended to prescribe loads or reps. A 2025 PLOS ONE framework review: **5 of 66** validity studies met all criteria. |
| Seel 2014, MagFree 2020, Fang 2023, Weygers | **U** | Not searched by name. My general search found two-IMU elbow RMSE ~1–7° against optical capture, **no resistance-exercise or curl-specific validation**. |
| Hamilton 2024 J Bodyw Mov Ther 40:315–319 (F6 "Cardiff2024") | **P** | Real; HRNet ≈ MediaPipe; flexion/extension tasks agree better. "CV <10%" not confirmed. |
| Lee 2024 Bioengineering 11(2):149 | **V** | 30 adults; A vs B mode diff <0.91 mm; ICC >0.95 (preprint). |
| AlMohimeed & Ono 2012 | **V** | Proc. Symp. Ultrasonic Electronics 33:255–256; PVDF film; ~0.4 mm (5%) thickness change, isotonic forearm. |

### 1g. Seeded random sample (15 rows)

`random.seed(20261102)`, `random.sample` over the **190** rows of F1–F6 CSVs whose key matched none of the named
items (script in `FA-searchlog.md`).

| key (agent) | verdict | note |
|---|---|---|
| Ogasawara2013 (F5) | **V** | EJAP 113:975–985; 14 men; 3 × (6 wk + 3 wk off) ≈ continuous at 24 wk. |
| Morton2016 (F1) | V (A6) | Not re-searched; carried. |
| Drummond2009 (F4) | **V** | J Physiol 587:1535–1546; ~40% MPS rise blocked; S6K1 ~6× in controls; ERK1/2 also blocked. |
| Cardiff2024 (F6) | **P** | It is Hamilton et al. 2024 (above). |
| Lee2024_Amode (F6) | **V** | Above. |
| Ostrowski1997 (F2) | **P** | Above; drop "triceps 7/14/28". |
| Vigotsky2022 (F1) | V (A6) | Not re-searched. |
| BenavidesVillanueva2022 (F4) | **P** | Wrong journal name; omitted direction. |
| Nobrega2018 (F1) | **P** | JSCR 32(1):162–169; within-subject 4 protocols (80/30% × failure/volitional); all similar. n = 32 not confirmed. |
| AlMohimeed2012 (F6) | **V** | Above. |
| Damas2019freq (F2) | **P** | Above. |
| Schoenfeld2015a (F4) | V (A6) | Not re-searched. |
| VargasMolina2025 (F5) | **V** | EJAP 125(6):1725–1734; n = 10 trained (7 M, 3 F); cluster ≈ traditional. F5 had citation "not retrieved". |
| ST_LSM6DSO_DS (F6) | **P** | Third-party pin tables agree: SDx/SCx to VDDIO or GND in Mode 1; master I²C in Mode 2. ST datasheet itself not retrieved. |
| Zhang2025 (F4) | **V** | Above. |

**Sample result:** 0 W, 8 P, 7 V (3 of them carried from A6). The P verdicts are missing counts, unconfirmed n and one
wrong journal name. **No fabricated row.** The error pattern is the same as the named list: secondary numbers quoted
as if read.

---

## 2. Board facts (read from `hardware/kicad/routed.kicad_pcb`)

`fputil.footprints()` returns pads without nets, so I parsed the footprint blocks directly (regex over the
`(footprint … (pad "N" … (net k "NAME")))` text).

| part | pads → net | F6 claim | verdict |
|---|---|---|---|
| U6 LSM6DSO | 1 GND · **2 GND · 3 GND** · 4 IMU_INT1 · 5 3V3 · 6 GND · 7 GND · 8 3V3 · 9 — · 10 — · 11 3V3 · 12 3V3 · 13 I2C_SCL · 14 I2C_SDA | SA0 = GND (0x6A); SDx (2) and SCx (3) to GND; INT2/OCS_Aux NC; SDO_Aux and CS to 3V3 | **CONFIRMED.** Mode-2 sensor hub needs a respin. |
| J3 | 1 3V3 · 2 GND · 3 I2C_SDA · 4 I2C_SCL · 5 EXP_GPIO2 · 6 EXP_GPIO18 | same | **CONFIRMED.** |
| U1 ADS1292R | 1 PGA1N_FILTER · 2 PGA1P_FILTER · 3 EMG_IN_N · 4 EMG_IN_P · **5 3V3_A · 6 3V3_A** · **7 — · 8 —** · … · **29 3V3_A** · 30 RLD_OUT · **31 3V3_A · 32 3V3_A** · 33 GND | IN2N/IN2P (5, 6) → 3V3_A; PGA2N/P (7, 8) NC; RESP_MODP/N (31, 32) → AVDD | **CONFIRMED at net level.** AVDD is the 3V3_A net. |

**Caveat F6 did not state.** That pins 5/6 are IN2N/IN2P and 31/32 are RESP_MODP/RESP_MODN comes from the project's
own pin map (`docs/AFE-DESIGN-REVIEW.md` table), whose section 0 says the TI datasheet could not be opened. I did not
independently confirm the ADS1292R pin numbering either. The *nets* are certain; the pin *functions* rest on the
project's map.

---

## 3. Ranking — my top-5 for trained lifters, and where I disagree

### 3a. The coordinator's emerging view

1 effort (threshold) · 2 weekly hard-set volume · 3 exercise selection / muscle length · 4 load ~30–85% + progressive
overload · 5 rest ≥ ~90–120 s.

### 3b. Scoring on the brief's five criteria

| factor | 1 effect at realistic contrasts | 2 certainty | 3 trained evidence | 4 set-to-set control | 5 shape | independent? |
|---|---|---|---|---|---|---|
| **Weekly hard-set volume** | **Largest.** ~2× growth from <5 to 10+ sets (Schoenfeld 2017); ES 0.24→0.44 (Krieger) | moderate; ~70 unique trials, heavy overlap | **best of all factors**: ~10 trials (Schoenfeld 2019, Brigatto, Ostrowski, Aube, Heaselgrave, Enes, Barsuhn, Räntilä) | high | concave; no detectable gain past ~31 fractional sets/wk (Pelland via Remmert) and ~11/session (preprint) | yes |
| **Effort / proximity** | **small** at the contrast lifters argue about: failure vs 0–3 RIR ES 0.12–0.19; trained subgroup 0.15 on 2 studies; trained trials null (Refalo 2024, Santanielo, Martikainen) | moderate; four metas on one evidence base | moderate, all null-to-small | high in principle, biased self-report | threshold, load-moderated | yes, but it **defines** the volume unit |
| **Exercise selection / ROM / length** | moderate vs short partials (Pallarés lower limb 0.88; Kassiano medial 15.2 vs 3.4%); trivial vs full ROM in trained (Wolf 2025, Larsen) | low–moderate; mostly untrained | **weak**: 4 trained null tests; 0 trained tests of Maeo-type exercise choice | high | unknown | yes |
| **Load 30–85% + progression** | ~0 for size across 30–90% (Currier, Lopez, Morton 2016, Cumming); progression mode ~0 (Plotkin) | high for "load does not matter" | moderate | high | flat above a floor | **no**: the floor is an effort rule; progression is effort over time |
| **Rest interval** | small (Singer: >60 s helps, >90 s nothing appreciable); 1 vs 3 min gap disappears when volume load is matched (Longo) | low–moderate, mostly untrained | 3 small trials | high | floor then flat | **no**: works through volume load |

### 3c. My ranking

1. **Weekly hard-set volume per muscle** (fractional counting; a set counts only if it is "hard", see #2).
2. **Effort threshold** — end sets within about 0–3 RIR, closer on light loads. Failure itself adds little.
3. **Exercise selection and range** — full ROM or a lengthened bias; do not live in the short range; pick variants
   that load the muscle long. Moderate evidence in untrained people, null-to-trivial in trained people.
4. **Volume-preserving rest** — ≥ ~2 min on heavy multi-joint lifts, ≥ ~90 s otherwise, or add sets to make up lost
   reps. *A rule serving #1.*
5. **Keep sets hard as you adapt** — load ≥ ~30% 1RM and progress load or reps. *A rule serving #2.*

### 3d. Disagreements with the coordinator view

**D1. Volume, not effort, is #1 by the brief's own criteria.**
- Criterion 1 (realistic contrast): failure vs 1–3 RIR is ES ~0.1–0.2 and null in every trained trial. Going from
  ~5 to ~10+ hard sets roughly doubles growth.
- Criterion 3 (trained evidence): volume has the most trained trials of any factor.
- "Effort is #1" depends on the contrast "near failure vs far from failure". In trained lifters at moderate-to-heavy
  loads that contrast is **barely tested**: Martikainen's 4-RIR weeks, and Robinson's RIR values that were estimated
  after the fact. Lasevicius 2022 (untrained) found failure mattered at 30% 1RM and not at 80%.
- Effort is a **gate on the unit of volume**. It is not a bigger lever. Call it #1-as-precondition if you must, but do
  not tell users it is the biggest dial. It is not.

**D2. Slots 4 and 5 are double counts.**
- "Load 30–85% + progressive overload": load has ~0 effect on size inside the range, so it is a **constraint**, not a
  lever. Progression has **no trial against no progression**; it exists to keep sets hard. That is #2 by another name.
- "Rest ≥ 90–120 s": Longo 2022 shows the rest effect disappears when volume load is matched. It is #1 by another name.
- Honest framing: **three independent levers (volume, effort, exercise selection/ROM) and two implementation rules.**
  Present them that way to Kye.

**D3. The 85% upper bound is arbitrary.** Cumming 2025 (3–5RM vs 20–25RM, trained, within-subject) and Morton 2016
(up to 90%) show equal growth. The real costs of very heavy work are time (Schoenfeld 2014: 7×3 took ~4× as long) and
that heavy low-rep sets are poorly counted by set-volume models (Baz-Valle 2021: 6–20+ reps). Write "any load from
~30% 1RM up, with heavy low-rep sets counted cautiously".

**D4. Is there a better 5th?** I checked four candidates.
- **Frequency:** no. Volume-equated frequency is compatible with zero for hypertrophy (Pelland 2026; Schoenfeld 2019).
  Its only role is the per-session ceiling (~11 fractional sets, **one preprint**). That makes "spread volume over ≥2
  sessions per week" a **co-equal alternative to rest as rule #4/5**. It is no more independent than rest.
- **Protein:** the largest independent non-training effect (Morton 2018: +0.30 kg FFM, larger in trained people,
  49 RCTs). It is **out of scope**: the brief asks for working-set factors. Mention it outside the list. Do not
  smuggle it in.
- **Exercise variation / regional coverage:** Kassiano 2022 JSCR SR (8 studies, 241 trained men, secondary count):
  some systematic variation improves regional hypertrophy; excessive rotation hurts. This is the same lever as #3
  ("which exercises"). **Merge it into #3** as "choose exercises that cover the muscle's regions and its long
  length". Do not create a sixth item.
- **Tempo, eccentric emphasis, set structures, periodisation, deloads:** all ~0 for size (Enes, Amdi & King, Silva,
  Davies, Zhang, Moesgaard, Coleman). None qualifies.
- **Verdict:** rest stays at #5 only because it has direct trained RCTs (Schoenfeld 2016) and the per-session rule
  rests on a preprint. Label it "volume-preserving rest".

**D5. Exercise selection at #3 is generous.** Its trained-lifter evidence is the weakest of the three levers. It earns
#3 only because it is free and every trained test is null-to-positive, never negative. Say "extrapolated from
untrained MRI trials" every time it is stated.

---

## 4. Challenge to the engineering plan (F6: a second puck as bar / stack / limb clip)

**C1. Stack-mode load ID is not supported.** W8-Scope identifies the weight with a **magnetometer** reading the iron
plates, plus an accelerometer. TENSR's LSM6DSO has no magnetometer, and the sensor-hub route is grounded (§2). A J3
I2C magnetometer could restore it, but F6 itself calls a magnetometer "actively worse near steel racks" and "not
recommended". F6 cannot hold both positions. **Either add a J3 magnetometer specifically for stack mode, or drop the
load-ID claim.** Stack *velocity* (a linear, vertical, single-axis motion with natural zero-velocity points) remains
plausible and is the best single use of a clip.

**C2. Bar-IMU validity is device- and algorithm-specific, and the literature is not kind.**
- Vmaxpro: the PMC abstract gives reliability ICC 0.55–0.91 and LoA <0.16 m/s. F6 quoted only 0.91–0.96 / <0.12.
- EnodePro on a Smith machine (Sensors 2025): did **not** meet the precision needed.
- Weakley 2021 (via secondary): accelerometer-based devices questionable for prescription.
- 2025 PLOS ONE framework review: 5 of 66 validity studies met all criteria.
- PUSH worn on the forearm: valid for peak force only (Banyard 2017, n = 10).
- **TENSR's own integration algorithm has zero validation.** "Same board, new firmware" is not a validation path.
  An LPT comparison per mounting (bar, Smith, stack, dumbbell) is the minimum.

**C3. Dumbbells and cables are the weak mountings.** I found no validation of a clipped IMU on dumbbells. Dumbbells
rotate and translate in 3D; zero-velocity-update integration assumes a known axis. Cable handles swing. Hypertrophy
training is dominated by machines, dumbbells and cables, not by the free-weight squat.

**C4. Velocity → RIR is validated only on compound lifts.**
- Jukic 2024: free-weight **back squat only**. Individual models <2 reps mean error; general models fail.
- I found **no validation of velocity-loss → RIR in single-joint or isolation exercises** (curls, leg extension,
  lateral raise). A thesis found self-reported RIR agreement weak on leg extension (ICC 0.18–0.66) and moderate on
  curls. A 2024 study found load–velocity relationships inadequate for 1RM prediction in lower-limb single-joint
  exercises.
- Velocity changes little in many isolation exercises at light absolute loads, and lifters alter ROM near failure.
- **<2 reps is not better than a lifter.** Halperin 2022: self-report bias −0.95 reps, SD ~1.45. A bias-corrected
  self-estimate may already be near 1–1.5 reps near failure on heavy compounds (A6 C1). The device has to beat
  *that*, in the same sessions.

**C5. "Calibration sets to failure" is a real cost, not a footnote.**
- Jukic's method needs sets to failure **per exercise**, and individual relationships were tested only across a short
  gap. Strength changes over a block move the relationship; recalibration is periodic.
- A typical split has 12–20 exercises. That is dozens of failure sets before the feature works everywhere.
- Free-weight squat and bench to failure need a spotter or safety arms. On machines and Smith it is acceptable for
  trained lifters.
- I found **no data** on user acceptance of calibration-to-failure. It is an untested product assumption.

**C6. The pair price is being spent twice.** F6 says "$429 pair already assumes two pucks". If the second puck is on
the bar it is not on a second muscle. The pair cannot both double muscle coverage and sense velocity.

**C7. Two-IMU joint angle in lifting is unvalidated.** Lab elbow RMSE ~1–7°, calibration-dependent (6.3–7.2° in one
13-subject study). No curl or press validation under load, with sweat and strap shift. Phone pose is worse at
the elbow (a 2024 study: MediaPipe ~17° mean error vs YOLO v7 ~5°).

**What is defensible to claim (after TENSR's own LPT validation, not before):**
- "Measures bar or stack velocity and within-set velocity loss on barbell, Smith and pin-loaded machine lifts."
- "Estimates reps in reserve on compound lifts **after you calibrate that exercise**; typical error up to ~2 reps."
- "Counts sets and reps and times your rest" (Tier 0, once detection is validated on the worn muscle).
- "Logs the load you enter."

**Not defensible:** "knows when you're near failure" on isolation lifts; "identifies the weight" without a
magnetometer; "measures muscle tension"; any velocity claim on dumbbells or cables; "rest timer driven by your
muscle's recovery".

---

## 5. Corrections each agent must accept or rebut

**F1**
1. State the unit of Jukic 2023's b = 0.006 as UNVERIFIED. Do not write "per percentage point" as fact.
2. Pareja-Blanco 2020 MSSE: details unverified (not found by search). Do not quote its numbers.
3. Martikainen 2025: add that triceps thickness rose only in the 4→1 RIR arm (+5.8% vs +2.2%).
4. Refalo 2024 "0.18 cm both arms": the exact values were not reproduced by my search. Mark A6-sourced.
5. Accept D1: on the brief's criteria effort ranks below volume as a lever. F1's own summary line 10 already says
   this; the coordinator should not override it.

**F2**
1. **Barbalho MSSE 2019 (women): PubMed lists it as a Retracted Publication.** Change "status unresolved".
2. Pelland DOI: still not reproducible by exact-string search. Downgrade "confirmed this session" to "claimed from a
   ResearchGate copy; not independently reproduced". The 67 / 2,058 counts are now abstract-level, not blog-only.
3. Add Pelland's **~31 fractional sets/week** point of no detectable superiority (cited in the Remmert preprint).
   "No clear plateau" needs that qualifier.
4. Ostrowski 1997: delete "triceps 7/14/28"; its source contradicts the abstract.
5. Räntilä 2026: co-author is Ahtiainen; arms are NOR n = 12 vs XTR n = 15. Mark "no added growth" and "deadlift
   p = 0.043" UNVERIFIED.
6. Baz-Valle 2022: add that multi-joint sets were counted toward arm volume.

**F3**
1. **Kassiano 2023: accept the table in §1c.** Medial: initial 15.2 > full 6.7 > final 3.4 (p ≤ 0.009). Lateral:
   14.9 / 7.3 / 6.2, initial vs full p = 0.060. Remove "A6 over-corrected"; A6 was wrong, A1 was right. Rewrite
   summary item 5 and §4 accordingly: for the medial head, lengthened partials beat full ROM significantly
   (untrained women).
2. Goto 2019 +49% / +28%: trace to a forum post. Mark UNVERIFIED, not SECONDARY.
3. Varovic 2025 "21.8%": not found. Mark UNVERIFIED.
4. Gschneidner n and effect sizes: blog-only. Say so.

**F4**
1. Silva 2025: "26 studies" unconfirmed; add the upper-limb subgroup favouring eccentrics (low certainty).
2. Benavides-Villanueva 2022: correct the journal; add that the authors associated slower tempos with more growth.
3. D3: the "85%" ceiling is not an evidence boundary. Cumming 2025 used 3–5RM.
4. Zhang 2025 counts are now verified (19 studies, 313; SMD −0.05). Update the row.

**F5**
1. Morton 2018: add +0.30 kg (0.09–0.52) and that the effect was larger in trained participants.
2. Dankel: n = 151, elbow flexors, 6 weeks; APNM 45(5) (2019 online). Limit the generalisation.
3. Moesgaard 2022: ES 0.13 and 35 studies unconfirmed.
4. Souza-Junior 2011: "recreationally trained", not "trained".
5. Vargas-Molina 2025: citation now found (EJAP 125(6):1725–1734, n = 10 trained).

**F6**
1. **W8-Scope uses a magnetometer. Withdraw "stack mode = load ID, no respin", or make it conditional on a J3
   magnetometer and reconcile with your own advice against one.**
2. Held 2021: report the conflicting n (16/19) and the PMC abstract's ICC 0.55–0.91 / LoA <0.16 m/s, not only the
   best case.
3. Jukic 2024 is **back squat only**. Say so in every place it supports an RIR claim. No isolation-exercise
   validation exists.
4. State that calibration-to-failure is per exercise, needs recalibration, needs spotting on free weights, and has
   no user-acceptance data.
5. Pin functions for U1.5/6/31/32 rest on the project's own pin map, not the TI datasheet. Say so.
6. "$429 pair already assumes two pucks": the second puck cannot both instrument a second muscle and sit on the bar.

**A6 (previous round)**
- Kassiano 2023a: A6's "A1 numbers WRONG" verdict is itself wrong. A1's medial figures were correct; A6's 6.2 / 7.3
  are the lateral head.
