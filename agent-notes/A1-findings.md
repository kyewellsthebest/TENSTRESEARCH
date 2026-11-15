# A1 — Resistance-training outcomes: what produces hypertrophy and strength

Agent A1, 2026-11-02. Scope: RQ1 of `PROTOCOL.md`, plus a brief "can one band see it" note per topic (A4 does product translation in depth).

## Ten-line summary (most product-relevant)

1. **No defensible "optimal fatigue level", "optimal TUT" or universal RIR target exists in the outcome literature.** Every dose-response found is a shallow curve with wide uncertainty, not a threshold. A product that scores a set against such a target is inventing the target. (I, moderate)
2. **Proximity to failure matters for hypertrophy, weakly and non-linearly; it barely matters for strength.** Stopping 0–3 RIR gives similar growth to failure in trained lifters (Refalo 2023/2024, Grgic 2022, Robinson 2024). Failure matters most with **light loads** (Lasevicius 2022). (I, moderate)
3. **Humans already estimate RIR to within ~1 rep on average, with huge between-study spread** (Halperin 2022: underprediction 0.95 reps, 95% CI 0.17–1.73, I² 97.9%). A sensor RIR is only useful if its *individual* error is clearly smaller than that. Nothing in this review shows any sEMG feature does so. (I/H, limited)
4. **Acute sEMG amplitude is not a validated predictor of hypertrophy** (Vigotsky 2018, 2022). The one direct training test — Plotkin 2023 — found higher gluteal sEMG in hip thrusts but **no more gluteal growth** than squats. An "activation %" cannot be marketed as a growth or stimulus score. (D/M, moderate)
5. **Load per se does not determine hypertrophy when sets are effortful** (Schoenfeld 2017a, Lopez 2021, Morton 2016); heavy loads give more EMG amplitude and more 1RM strength, not more growth. So amplitude tracks load, not stimulus. (I, strong for hypertrophy equivalence across ~30–90% 1RM)
6. **Time under tension and tempo are not levers within 0.5–8 s/rep** (Schoenfeld 2015, Lacerda 2021). A TUT score has no outcome evidence to coach toward. (I, moderate)
7. **Weekly sets per muscle is the best-supported dose metric** (Schoenfeld 2017b; Pelland 2026 meta-regression: continued but diminishing returns for growth, sharper plateau for strength). A band can count sets only for the muscle it is on — and Pelland's "fractional set" model means compound lifts feed muscles the band is not on. (I, moderate)
8. **Muscle length/stretch matters more than full ROM per se, but effect sizes are uncertain** (Maeo 2021/2023, Pedrosa 2022, Kassiano 2023; Wolf 2023 lengthened partials vs full −0.28, CI −0.81 to 0.16; Wolf 2025 trained: no difference). Mostly untrained samples, 8–12 weeks. A single puck IMU sees one segment's orientation, not a joint angle. (I, limited–moderate)
9. **More local fatigue/metabolic stress is not shown to cause more growth when effort and tension are held** — cluster sets, supersets, drop sets and rest-pause give similar growth with very different fatigue (Davies 2021, Zhang 2025, Sødal 2023). The best "more fatigue = more growth" evidence (Pareja-Blanco 2017 VL40 vs VL20) is small, costs power, and used bar velocity, not EMG. Fatigue is best treated as a by-product. (I/M, moderate)
10. **Rest: >60–90 s is enough; beyond 90 s no appreciable difference** (Singer 2024). No trial shows a muscle-recovery-driven timer beats a fixed ≥2 min default. (I, limited–moderate)

---

## 0. Method and access limits (read first)

- **Network:** WebFetch, Crossref API, doi.org, PubMed/eutils and Europe PMC were all **blocked** in this session (proxy 403 / DNS refusal; recorded in `A1-searchlog.md`). Every source was reached only via the WebSearch tool, which returns a search-engine summary of abstracts and repository records. **No full text was read.** Access is therefore marked `SECONDARY (search-index abstract text)` where abstract wording/numbers were returned, and `SECONDARY (bibliographic record only)` where only citation details were. Nothing is marked FULL.
- **Search budget:** the session-wide WebSearch limit (200, shared across agents) was exhausted after A1's 53rd search. Studies I planned to verify but could not are listed in §17 as UNVERIFIED and are **not** used as sole support for any claim.
- **DOIs:** 43 of 46 CSV rows have a DOI confirmed in at least one search-returned bibliographic record (journal, repository or PubMed). Three are marked `DOI UNVERIFIED` (Wakahara 2013, Gentil 2013) or "confirm on publisher page" (Pelland 2026, whose DOI came from a single bibliographic record). The auditor (A6) should spot-check these first.
- **Evidence codes:** training-outcome studies are coded **I** (human, but not about the device); mechanistic reviews **M**; Plotkin 2023 is coded **D** because it is the only study here that measured sEMG during dynamic lifting *and* longitudinal hypertrophy. Product statements are **H**.
- **Outcome measures:** ultrasound muscle thickness (single site, operator-dependent, regional), MRI volume/CSA (best), DXA lean mass (coarse, includes water/glycogen). Where a study is ultrasound-only or DXA-only it is flagged; most "regional" findings are ultrasound at one or two sites.

---

## 1. Mechanical tension vs time under tension

**Outcome evidence.** Mechanical tension on the fibres is the leading candidate stimulus; metabolic stress and damage are candidates without proof (Wackerhage2019, M, moderate — much of the sensor biology is animal/in-vitro). "Time under tension" as a quantity has outcome support only in the trivial sense that more effortful reps add stimulus. The acute protein-synthesis study usually cited for TUT (Burd2012: 30% 1RM, 6 s/6 s reps raised 24–30 h myofibrillar PS vs a work-matched faster control) is mechanistic; acute MPS early in training does not track hypertrophy (Damas2016, M, moderate). Longitudinally, repetition duration from 0.5 to 8 s gives similar hypertrophy; only very slow (>10 s) reps look inferior (Schoenfeld2015, I, moderate; 8 studies, load not isolated). Lacerda2021 (n = 10 untrained, 2 s vs 6 s to failure, 14 wk) found no between-protocol difference — small, and non-significance is not equivalence.

**Optimal TUT?** None exists. No trial identifies a TUT per set that maximises growth independent of load and proximity to failure.

**Band:** The IMU can time concentric/eccentric phases and sum set duration; sEMG burst duration gives "electrical TUT". Neither has a validated target. Displaying TUT is harmless as a log; scoring it implies a dose-response that is not there. (H)

## 2. Long muscle lengths / stretch-mediated hypertrophy

**Outcome evidence.**
- Maeo2021 (MRI, n = 20 untrained, 12 wk): seated leg curl (hip flexed, hamstrings long) +14% vs prone +9% whole-hamstring volume; difference in biarticular heads only. (I, moderate for this muscle)
- Maeo2023 (MRI, n = 21 untrained, 12 wk): overhead elbow extension +19.9% vs pushdown +13.9% triceps volume (~1.4×); long head +28.5% (secondary-sourced numbers). Mono-articular heads also grew more, so length alone may not explain it. (I, limited–moderate)
- Pedrosa2022 (n = 45 untrained women, ultrasound): initial-range (lengthened) partial knee extension gave greater relative regional quadriceps growth than full or final-range partials; 1RM similar. (I, limited)
- Kassiano2023a (untrained women, B-mode ultrasound): initial-range calf raises gave the largest medial gastrocnemius gain (secondary figures +15.2% vs full +6.7% vs final +3.4%; UNVERIFIED). (I, limited)
- Reviews: Kassiano2023b (systematic review "Which ROMs lead to Rome?") and Wolf2023 (pre-registered Bayesian meta) — overall full vs partial trivial (SMD 0.12, CI crosses 0); lengthened partial vs full for hypertrophy −0.28 (95% CI −0.81 to 0.16), i.e. favouring lengthened partials but uncertain.
- **Trained lifters:** Wolf2025 (PeerJ, within-subject, n = 30 trained, lat pulldown, 8 wk) found lengthened partials and full ROM **similar**. COI note: several co-authors are fitness content creators.

**Strength of evidence:** Moderate that training a muscle at long lengths is at least as good as, and in several untrained studies better than, training at short lengths; **limited** that lengthened partials beat full ROM; **very limited** in trained populations. Short studies (8–12 wk), ultrasound-heavy, small n.

**Band:** The length effects in Maeo 2021/2023 are set by the *other* joint (hip, shoulder). A puck on the hamstring or triceps cannot see the hip or shoulder angle. Its IMU gives orientation of one segment; with gravity reference it can roughly tell overhead from neutral arm, and excursion of that segment, but not joint angle without assumptions about the adjacent segment. A "you trained at long lengths" feature is H, needing validation against motion capture. sEMG amplitude falls at long muscle lengths for a given effort and electrode-to-muscle geometry shifts with length — so EMG cannot index "stretch stimulus" either.

## 3. Full ROM vs lengthened/shortened partials

See §2. Pallares2021 (16 studies) found full ROM better for strength (ES 0.56) and lower-limb hypertrophy (ES 0.88), but did not separate lengthened from shortened partials — the point raised in Kassiano's 2022 letter. Wolf2023 did, and the advantage of full ROM disappears or reverses for lengthened partials. Strength gains are ROM-specific (Wolf2023). **Conclusion:** short-length partials are probably inferior; lengthened partials ≈ full ROM. (I, moderate for "avoid short partials", limited otherwise.)

**Band:** IMU excursion per rep within a session is plausible for detecting *ROM shrinkage* as a set progresses (rep-to-rep change), which is useful regardless of the optimal ROM debate. Absolute ROM needs calibration per exercise. (H)

## 4. Concentric / eccentric / isometric

- Schoenfeld2017c (meta): eccentric-only ~10.0% vs concentric-only 6.8% growth, not statistically different; a 2025 JSCR meta (seen only in a search summary, UNVERIFIED) found no difference. (I, moderate that both work; limited for an eccentric advantage)
- Isometric training builds muscle and strength, with long-length isometrics transferring better (Oranchuk2019, I, limited–moderate; systematic review without meta-analysis).
- Inter-set no-load "flexing" (Schoenfeld2020, trained, small RCT) improved mid-thigh thickness but possibly hurt leg-press strength — the only trial resembling "squeezing". (I, very limited)

**Band:** Eccentric/concentric split by IMU (direction of segment rotation) is plausible; the EMG eccentric/concentric amplitude ratio is a real acute phenomenon (lower EMG for the same force eccentrically), but there is no outcome evidence that steering the split improves growth. Isometrics defeat IMU rep counting (no motion) and leave EMG as the only signal. (H)

## 5. Tempo, pauses, peak-contraction squeezing

- Tempo: §1. Wilk2021 (narrative review) argues tempo is a programmable variable; it does not establish an optimum. (I, limited)
- Pauses within a rep: **no longitudinal hypertrophy trial found** (one search; budget prevented a second). Evidence: none.
- Peak-contraction squeezing: no direct trial; the nearest is Schoenfeld2020 (inter-set flexing). Evidence: none to very limited.

**Band:** IMU detects pauses easily. Nothing to score them against. (H)

## 6. Strict vs cheating/momentum; heavy cheat then strict isolation

Augustin2025 (Int J Exerc Sci, within-subject, 30 untrained, 8 wk, curls and pushdowns): momentum ("cheat") limb lifted markedly more volume load; muscle thickness and circumference changes **similar** to strict. One short trial in untrained people; COI (content-creator co-authors). "Heavy cheat then strict isolation" sequencing: **no trial found**. (I, very limited)

**Band:** Momentum is plausibly detectable from IMU (jerk, acceleration profile, possibly trunk swing transmitted to a biceps-worn puck), and EMG-per-unit-movement drops when momentum does the work. But there is no evidence strictness changes growth, so a "form penalty" for momentum is not outcome-justified; it may be justified on safety grounds, which is outside this review. (H)

## 7. Compound vs isolation; machines / free weights / cables / stability

- Adding single-joint elbow work to a multi-joint program did not add elbow-flexor growth in untrained men over 10 weeks (Gentil2013, n = 29; DOI unverified). A 2016 Sports Med review reached the same conclusion (seen only via search). Barbalho-group studies on the same question were **not used**: that group has had multiple papers retracted (this retraction status was not re-checked in this session — flagged for A6). (I, limited; untrained only)
- Free weights vs machines: no difference in hypertrophy (Haugen2023: SMD −0.055, 95% CI −0.397 to 0.287; only 5 hypertrophy studies); strength gains are specific to the trained modality. (I, moderate for equivalence, limited precision)
- Cables, stability/unstable surfaces: not searched (budget). Evidence status: not assessed.
- Exercise selection does shift **where** in a muscle and **which** synergists grow (Plotkin2023: squat grew quadriceps and adductors more, hip thrust and squat grew glutes equally; Maeo2021/2023).

**Band:** One band sees one muscle. Compound lifts load muscles the band is not on, so per-muscle weekly volume is only measured for the instrumented muscle and must otherwise be inferred from exercise labels. (H)

## 8. Load and repetition ranges

- Hypertrophy is similar across low (≤60% 1RM) and high loads when sets go to or near failure (Schoenfeld2017a, 21 studies; Lopez2021 network meta, 28 studies, 747 adults). 1RM strength favours heavy loads. (I, **strong** for hypertrophy equivalence across ~30–80+% 1RM when effortful; strong for heavier = more 1RM)
- In trained men (Morton2016, n = 49, 12 wk), 20–25 reps (~30–50% 1RM) vs 8–12 reps to failure produced similar hypertrophy (DXA lean mass and fibre CSA) and similar strength except 1RM bench; acute hormones were unrelated. (I, moderate)
- Schoenfeld2021 (narrative): wide hypertrophy "rep continuum" given effort.

**Band:** sEMG amplitude is higher with heavier loads at the start of a set and converges toward failure. Since growth is similar across loads, **amplitude at the start of a set cannot be a stimulus score**. (M/H)

## 9. Volume dose-response

- Schoenfeld2017b (15 studies): graded dose-response; 10+ sets/muscle/week ~2× the gain of <5 (category comparison P = 0.074); little data at high volumes. (I, moderate)
- **Pelland et al. — verified as published:** Sports Med 2026;56(2):481–505, DOI 10.1007/s40279-025-02344-w per the bibliographic record (SportRxiv preprint 2024). 67 studies; indirect sets counted "fractionally" (0.5) as the best-supported model. Hypertrophy continues to rise with weekly volume with diminishing returns; strength shows more pronounced diminishing returns; frequency has identifiable effects for strength only. **Exact estimates were not reached** — do not quote numbers from it until A6 reads it. (I, moderate)
- No defensible upper limit or optimal number of weekly sets is established for an individual; between-person variance in response is large.

**Band:** Counting hard sets for the muscle the band is on is plausible (rep bursts + a hard-set criterion). The definition of a "hard set" is itself the RIR problem (§11). (H)

## 10. Frequency

Volume-equated frequency has no clear hypertrophy effect (Schoenfeld2019f, 25 studies); Pelland2026 agrees for hypertrophy and finds effects for strength. (I, moderate.) **Band:** frequency is logging, not sensing.

## 11. Proximity to failure and RIR

**Outcomes.**
- Refalo2023 (15 studies): trivial advantage for failure under any definition; none in the momentary-failure subgroup; possible non-linear relation. (I, moderate)
- Grgic2022 (15 studies): strength ES −0.09 (−0.22 to 0.05), hypertrophy ES 0.22 (−0.11 to 0.55); in resistance-trained subgroup hypertrophy ES 0.15 (0.03 to 0.26) favouring failure; when volume not equated, non-failure favoured for strength. (I, moderate; subgroup result limited)
- Vieira2021 (JSCR): citation verified, **results not retrieved — UNVERIFIED**; not used.
- Robinson2024 (meta-regressions on *estimated* RIR): hypertrophy increases as sets end closer to failure; strength is minimally affected; authors call it exploratory. RIR was estimated post hoc from study descriptions, which adds large measurement error. (I, limited–moderate)
- Refalo2024 (trained, 8 wk, ultrasound): failure vs 1–2 RIR gave ~identical quadriceps thickness gains (~0.18 cm each); failure caused more velocity/repetition loss. (I, moderate for "1–2 RIR is enough" in trained lower-body)
- Lasevicius2022 (untrained, volume-equated): failure mattered at 30% 1RM, not at 80%. (I, limited)

**Is there a universal RIR target?** No. The best summary is: growth improves on average as sets end closer to failure, most of that is captured by ~0–3 RIR, light loads need to be closer to failure than heavy loads, and strength is insensitive. No study defines an individual optimum.

**RIR estimation accuracy.**
- Halperin2022 (12 studies, 414 participants): mean underprediction 0.95 reps (95% CI 0.17–1.73), I² = 97.9%; accuracy improves closer to failure; training status did not clearly matter. (I, moderate for "humans are ~1 rep off on average"; very limited for any individual-level error bound)
- Zourdos2016 (n = 29): RIR-based RPE correlates strongly with bar velocity; experienced lifters rate more accurately at 1RM. Correlation, not individual accuracy. (I, limited)
- Zourdos 2021 and Refalo's bench-press RIR accuracy paper were planned but not verified (§17).

**Band:** This is the feature with the most outcome relevance and the highest bar. To be worth anything, the band's RIR error (per person, per set, per exercise) must be shown smaller than self-report's ~1 rep with wide spread, against true failure. sEMG median frequency and amplitude change during a set, but how many reps remain depends on load, exercise and person; whether any single-channel feature predicts reps-to-failure to ±1 rep across loads is A2's question and is **H** here. The Lasevicius result implies the hardest case — light loads — is where accurate RIR matters most.

## 12. Rest intervals

- Schoenfeld2016 (21 trained men, 8 wk): 3 min > 1 min for 1RM and some thickness sites; volume load lower with 1 min. (I, limited)
- Singer2024 (Bayesian meta, 9 studies, 19 measurements): small benefit >60 s; no appreciable difference beyond 90 s; heterogeneous; set end-point did not modify the effect. (I, moderate for ">60–90 s"; limited precision)

**Band:** A "rest timer driven by the muscle's recovery" has **no outcome trial**. The literature supports rest long enough to preserve the next set's reps; whether EMG recovery (e.g. median frequency returning toward baseline) predicts next-set performance better than a fixed 2–3 min default is untested (H). Note EMG spectral recovery after a set is fast (seconds to a minute) and does not equal force/rep-capacity recovery — A2 should confirm.

## 13. Supersets, drop sets, rest-pause, cluster sets

- Supersets: chronic hypertrophy SMD −0.05 (p = 0.87), strength 0.10; shorter sessions, higher RPE and lactate; same-muscle supersets cut volume load (SMD −1.08) (Zhang2025, 19 studies, 313 participants; short interventions). (I, moderate)
- Drop sets: similar hypertrophy in about half to one-third the time (Sødal2023, Sports Med Open — title/details secondary; Coleman 2022 IJSC meta also: hypertrophy ES 0.08, −0.08 to 0.24, 5 studies). (I, limited)
- Cluster sets: equal strength/hypertrophy with less fatigue (Davies2021, 29 studies). (I, moderate)
- Rest-pause: one trial (Prestes 2019) recalled but **not verified** in session. (UNVERIFIED)

**Band:** These are time/fatigue tools, not growth levers. Detecting them (drop-set load changes from IMU/EMG continuity) is plausible; a fatigue score that rises in drop sets would be correct physiologically but not evidence of more growth. (H)

## 14. Fatigue, metabolic stress and EMG as growth predictors

### 14.1 Does more local fatigue or metabolic stress produce more growth?
- Metabolites probably do not drive growth directly; any effect may be via higher fibre recruitment (Dankel2017, M, limited).
- Studies that manipulate fatigue while holding effort/end-point: cluster sets (less fatigue, same growth: Davies2021), supersets (more internal load, same growth: Zhang2025), drop sets (more fatigue per unit time, same growth: Sødal2023), failure vs 1–2 RIR (more velocity loss, same growth: Refalo2024). Consistent pattern: **fatigue varies, growth does not.** (I, moderate)
- Counter-evidence: Pareja-Blanco2017 (n ≈ 22, 8 wk, Smith squat): 40% velocity loss gave more vastus lateralis/intermedius hypertrophy than 20%, but similar squat strength, worse jump gain (3.5% vs 9.5%) and loss of type IIX fibres, with 40% more reps. So more within-set fatigue bought some hypertrophy (also more volume) at a performance cost. (I, limited.) It used a bar transducer, not EMG.
- Acute markers early in training (damage, MPS) are poor proxies (Damas2016, M).
- **"Fatigue as a by-product" vs "fatigue as a stimulus":** the evidence above supports treating fatigue as a by-product of effortful tension that becomes a cost at the extremes. No study isolates an "optimal fatigue level". (I/M, moderate)

### 14.2 Does acute EMG amplitude predict hypertrophy?
- Vigotsky2018 and Vigotsky2022: amplitude depends on cancellation, crosstalk, electrode geometry, muscle length, normalisation and fatigue; each premise linking acute amplitude to longitudinal growth has counter-evidence; amplitude is "not a validated predictor of muscle hypertrophy". (M, moderate)
- Plotkin2023 (direct test, coded D): higher gluteal sEMG during hip thrusts did not consistently predict gluteal hypertrophy; both exercises grew the glutes similarly (MRI); squats grew quadriceps and adductors more. (D, limited — one untrained 9-week study, but it is the right design)
- Load studies (§8): heavy loads produce higher amplitude yet similar growth. (I, strong by inference)
- Regional exception: Wakahara2013 found regions more activated in a session (MRI T2 mapping, not sEMG) grew more. Suggestive that *regional* activation matters, but T2 MRI is not a single bipolar surface channel. (I, limited)
- Schoenfeld/Contreras-era acute EMG comparisons and Schoenfeld 2014 (EMG low vs high load in trained men) were planned but not re-verified (§17).

**Band:** "Activation %" as a measure of *whether the target muscle is working* is a measurement claim (A2/A3). As a measure of *stimulus* or predicted growth it is **contradicted** by the outcome literature above. Keep "activation" out of any growth/stimulus language.

## 15. Regional / muscle-specific hypertrophy

Regional growth is real and exercise-dependent (Maeo2021: biarticular hamstrings; Maeo2023: triceps long head; Pedrosa2022: distal quadriceps; Plotkin2023: quads/adductors with squat). Most measures are single-site ultrasound; MRI studies are few and untrained. (I, moderate that regional growth differs; limited for specific prescriptions.) A preprint meta (Varovic 2024, SportRxiv — preprint, not used as support) reportedly found long mean muscle length did *not* produce greater regional growth overall.

**Band:** A 25.4 mm bipolar pair samples one region of one muscle. It cannot report regional distribution, and relocating the band changes what it sees.

---

## 16. Is there an "optimal" anything? — plain answer

| proposed target | outcome support | verdict |
|---|---|---|
| optimal fatigue level per set | none; fatigue manipulations without effort change do not change growth | **does not exist in the literature** |
| optimal TUT per set/rep | 0.5–8 s/rep equivalent; no TUT dose-response | **does not exist** |
| universal RIR target | 0–3 RIR captures most hypertrophy on average; light loads need closer; strength insensitive | **no universal number**; a range with load dependence |
| optimal rest | >60–90 s, no gain beyond ~90 s on pooled data | a floor, not an optimum |
| optimal weekly sets | graded with diminishing returns; no individual optimum | a curve, not a target |
| optimal ROM | long-length emphasis plausible; short partials worse | direction, not a number |
| activation level that maximises growth | amplitude not validated as predictor; one direct test negative | **no** |

---

## 17. Not verified in this session (do not cite until checked)

Search budget ran out before these could be verified: Morton 2019 J Physiol (fibre activation unaffected by load at task failure); Schoenfeld 2014 Eur J Appl Physiol (EMG low vs high load); Lixandrão 2018 Sports Med (BFR meta); Kubo 2019 Eur J Appl Physiol (squat depth and gluteal/adductor volume); Bloomquist 2013 (deep vs shallow squat); Schoenfeld 2019 MSSE (volume in trained men); Zourdos 2021 JSCR (intraset RIR accuracy); Refalo 2024 JSCR (bench-press RIR accuracy); Prestes 2019 (rest-pause); Jukic 2023 Sports Med (velocity-loss meta); Hickmott 2022 (autoregulation meta); Remmert per-session volume preprint; Warneke stretch-mediated hypertrophy reviews; Zabaleta-Korta 2021 regional-hypertrophy review; Barbalho retraction status; the 2025 JSCR eccentric vs concentric meta. Vieira 2021's results.

## 18. Cross-cutting caveats

- **Untrained samples dominate** the long-length/ROM, cheating, compound/isolation and regional studies. Trained-lifter results (Wolf2025, Refalo2024, Morton2016, Schoenfeld2016) are fewer and tend to show smaller or no differences.
- **Durations are 8–14 weeks**; no study here tests whether any of these factors compounds over a year.
- **Overlapping samples:** the failure meta-analyses (Refalo2023, Grgic2022, Vieira2021, Robinson2024) share most primary studies; they are not independent confirmations. Same for Schoenfeld2017a/Lopez2021 on load, and Wolf2023/Kassiano2023b/Pallares2021 on ROM.
- **COI:** several recent trials (Wolf2025, Augustin2025) include fitness-media co-authors; Schoenfeld is an author on a large share of this literature. Not disqualifying; worth noting.
- **Non-significance ≠ equivalence:** most "similar" results come from studies powered to detect moderate effects only.
