# A3 findings — wearable sensing, signal processing, algorithms / ML critique

Agent A3. Written 2026-11-02. Study rows are in `A3-studies.csv` and searches in `A3-searchlog.md`. The two scripts behind the derived numbers are `A3-sim-sampling.py` and `A3-sim-mdf-window.py`, in this folder.

## Summary (10 lines)

1. **Sampling rate: TENSR has to run the ADS1292R at 2 kSPS (DR = 100) for any spectral fatigue feature.** 1 kSPS is the floor, and only if the firmware compensates for the decimation filter and caps the band at about 400 Hz. **500 SPS cannot measure the 20–450 Hz band or median frequency.** Verified from datasheet mirrors: the filter is sinc3 and its −3 dB point is 0.262 × data rate, so **131 Hz at 500 SPS**.
2. Derived from that: at 500 SPS the filter cuts 2.5 dB at 120 Hz and 7.3 dB at 200 Hz, and the signal stops at 250 Hz. On a model EMG spectrum, a true MDF of 120 Hz reads **86 Hz**, and the fatigue drop of −25% reads **−17%**. At 2 kSPS the same spectrum reads 116 Hz and −24%.
3. The brief's "20–450 Hz band-pass" and `BRING-UP.md` §7's "500 SPS, RMS in 20–450 Hz" contradict each other, because 500 SPS has a 250 Hz Nyquist limit. The bring-up noise test is valid only as a datasheet-condition noise check.
4. SENIAM recommends a bipolar inter-electrode distance (IED) of 20 mm, electrodes ≤10 mm, alignment with the fibres, and placement between the innervation zone and the tendon. TENSR meets the size rule (7 mm). It breaks the IED rule (25.4 mm, which gives a larger detection volume and more crosstalk), and it cannot control orientation or innervation-zone position because the user sets both when putting the band on.
5. One fixed geometry for seven muscles of very different size is the main hardware limit on validity. On a small muscle (delt heads, calf heads), 25.4 mm plus a 22.6 mm RLD offset spans neighbouring muscles. No study validates this geometry on any of the seven.
6. Dry, passive electrodes with 200 kΩ in series: the best validation evidence (Athos garment, textile shorts) shows amplitude roughly agreeing with research systems when values are normalised to MVC, with CVs of 11–14%. Timing metrics do not agree, and none of these studies validated **spectral** variables. Searle & Kirkup's "dry as good as wet" result needed buffered, shielded electrodes, which TENSR does not have.
7. Single-rep MDF is noisy even in the best case: SD ≈ 9 Hz for a 0.5 s stationary burst, against a 30 Hz total fresh-to-failure change. Per-rep MDF has to be smoothed or regressed over reps. A live "about 2 reps left" from MDF alone is not supportable.
8. Between-day reliability of the MDF **slope** is the weak link (CVs of 14–27% reported; slope worse than initial or final values). Amplitude without MVC normalisation cannot be compared across days, after re-application, across muscles or between users.
9. IMU rep counting is the most mature feature: about 91–93% of sets within ±1 rep in lab/CrossFit studies, and poor in at least one independent smartwatch test. A limb-mounted IMU is not a bar-velocity sensor, and forearm-worn PUSH validity against linear transducers is poor except in narrow load ranges.
10. The ML literature on fatigue, failure and RIR from sEMG is small-n, mostly isometric or lab-based, and labelled with subjective scales. It rarely reports a simple baseline or external validation. Where a baseline was reported, the gain was modest: CNN RMSE 20.8% against linear regression 26.9%. No study validates RIR from sEMG during free-weight training with leave-one-subject-out testing and errors reported in reps.

**Access caveat for everything below.** In this session only web *search* was reachable. ti.com, doi.org, Crossref, PubMed and every publisher host returned a policy 403 or no DNS. Nothing was read in full text, so every source is ABSTRACT (an abstract seen through a search summary) or SECONDARY. The shared search budget ran out after about 37 queries, which left these UNVERIFIED and not used as sole support: SENIAM's exact per-muscle wording, the CEDE matrix cells, Ives & Wigglesworth 2003's findings, and LSM6DSO's full ODR table.

---

## Task 1 — SENIAM and CEDE, and TENSR against each

### 1.1 What the documents say

**SENIAM — Hermens et al. 2000, J Electromyogr Kinesiol 10(5):361–374** (bibliographic details ABSTRACT-level; recommendations SECONDARY, from search summaries of the paper and seniam.org):
- **IED 20 mm** for bipolar sensors. On relatively small muscles, the IED should not exceed ¼ of the muscle-fibre length. Part of the basis is model simulation. [Hermens2000; I; moderate as a consensus]
- **Electrode size ≤10 mm diameter** (the reference electrode is Ag/AgCl with gel). [Hermens2000]
- **Orientation:** parallel to the muscle fibres. [Hermens2000]
- **Location:** on the line between defined anatomical landmarks, between the motor end-plate (innervation) zone and the distal tendon, away from the edges of the muscle. Per-muscle landmarks exist for biceps, triceps, deltoid heads, vasti, rectus femoris, gastrocnemius, soleus and gluteus maximus. These were **not** retrieved in this session (UNVERIFIED). Note that SENIAM does not cover pectoralis major as a standard location. This is an UNVERIFIED recollection, flagged for A6 to check.
- **Reference electrode** on electrically inactive tissue: wrist, ankle or C7 are the usual choices. SECONDARY only; the SENIAM page itself was not reached.
- **Skin preparation:** shave, clean with alcohol, and in some protocols abrade. SECONDARY.
- SENIAM's consensus is about **Ag/AgCl gel electrodes**. It gives no guidance on dry electrodes.

**CEDE electrode selection matrix — Besomi et al. 2019, JEK 48:128–144, doi:10.1016/j.jelekin.2019.07.008** (ABSTRACT/SECONDARY): a Delphi consensus that sets out when each electrode configuration is appropriate. From the summaries:
- Large IEDs increase the detection volume, which makes crosstalk more likely.
- Smaller IEDs narrow the depth and area that are recorded.
- Multichannel recording is suggested for locating the innervation zone.
- A 2024 opinion piece that cites the matrix gives the range as 1–2 cm "depending on muscle size".

The exact text of the matrix cells could not be read (UNVERIFIED). [Besomi2019; I; moderate as a consensus]

**CEDE amplitude normalisation matrix — Besomi et al. 2020, JEK 53:102438, doi:10.1016/j.jelekin.2020.102438** (ABSTRACT/SECONDARY). It covers six approaches: an MVC in the same task context, a task-specific isometric or dynamic MVC, peak or mean EMG within the task, non-normalised EMG, and M-wave normalisation. Its main points as summarised:
- Normalisation needs care in dynamic tasks.
- Neither isometric nor dynamic MVC guarantees a true maximal reference.
- Non-normalised amplitude cannot be compared between people or between sessions where the electrodes have been re-applied.

[Besomi2020; I; moderate]

Other CEDE matrices exist: terminology, and high-density sEMG (Martinez-Valdes et al. 2023). The HD matrix's ≤10 mm spacing applies to electrode grids, not to a single bipolar pair. Titles were seen in search results. A "McManus 2020" or "Gallina 2022" normalisation paper could **not** be confirmed (UNVERIFIED).

### 1.2 TENSR against each recommendation

| item | recommendation | TENSR | verdict |
|---|---|---|---|
| electrode size | ≤10 mm (SENIAM) | 7 mm ring stud | **meets** |
| electrode material | Ag/AgCl with gel (SENIAM reference) | dry stainless steel; snap could take gel electrodes (undecided) | **deviates**; see Task 3 |
| IED | 20 mm; ≤¼ of fibre length on small muscles | **25.4 mm, fixed** | **exceeds by 27%**. Detection volume and crosstalk go up and the innervation-zone sensitivity changes. Acceptable on a large quadriceps; questionable on deltoid heads, the lateral or medial gastrocnemius, or a small biceps. [M, derived from CEDE/SENIAM rationale; strength limited] |
| orientation | parallel to fibres | set by how the band sits on the limb; never measured | **uncontrolled**. A pennate muscle (deltoid, gastrocnemius, vastus lateralis) has fibres that are not parallel to the limb axis. Misalignment lowers amplitude and alters the spectrum (M). The IMU's axes could record the puck's orientation relative to the limb, but not relative to the fibres. |
| location relative to innervation zone and tendon | between innervation zone and tendon, landmarks defined | user's guess at "on the muscle"; band slides | **uncontrolled**. A pair straddling the innervation zone lowers amplitude and biases MDF; the IZ moves under the skin with joint angle during dynamic lifts (M). |
| reference electrode | electrically inactive site | E2 on the same muscle, 22.6 mm away, **driven by RLD** | **deviates, low concern** (derived). E2 is an RLD-driven common-mode electrode, not a monopolar reference. EMG under E2 shows up as common mode, and the network rejects common mode. A ≥40 dB CMRR is still plausible with mismatched dry skin (`afe-sim-results.md`, 100 pF case: 48 dB at 50 Hz with a 250k/375k mismatch). That leaves about 1% contamination. The real cost is that E2 needs good skin contact on a moving muscle, and RLD current flows through tissue that is contracting. |
| skin prep | shave, alcohol, abrade | none specified; consumer use | **deviates**. Hair and dry stratum corneum raise impedance and the mismatch between electrodes, and the AFE simulation shows mismatch is what limits CMRR. |
| sampling | A3 search could not reach the SENIAM text on sampling | 500 / 1000–2000 SPS (inconsistent) | see Task 2 |
| filtering | 20–450 Hz band-pass is typical; high-pass 20 Hz per De Luca 2010 (SECONDARY) | analysis brief says 20–450 Hz | consistent **only at ≥1 kSPS** |
| normalisation | MVC in matching context (CEDE 2020) | none planned; "activation %" feature implies one | **unsupported** until a calibration manoeuvre exists |

**Seven muscles, one geometry.** The 25.4 mm × 22.6 mm triangle sits on a 38 mm band, so the active pair and E2 cover roughly a 32 × 30 mm patch of skin (per `CLAUDE.md`). Most crosstalk worries apply to small and layered muscles:
- **Deltoid:** the anterior and middle heads lie next to each other.
- **Calf:** the medial and lateral gastrocnemius heads, with soleus underneath.
- **Biceps in a lean arm:** brachialis lies underneath and brachioradialis distally.
- **Chest:** pectoralis has a fan-shaped fibre direction, so no single orientation is "parallel".

Crosstalk volume grows with IED (CEDE 2019, SECONDARY). Quadriceps (vastus lateralis or rectus femoris) and glute max are the most forgiving sites. **No study found validates this geometry on any of the seven muscles.** [H; none]

**What would satisfy the standards:** a per-muscle placement guide (SENIAM landmarks, fibre direction) in the app, an alignment mark on the puck, and a signal-quality check before each set (Task 4). It would also mean dropping the claim that the device works on every listed muscle until each muscle is validated.

---

## Task 2 — ADS1292R data rate, decimation filter, and what it does to the EMG band

### 2.1 What was verified

Access: SECONDARY. The TI datasheet SBAS502 could not be fetched (policy 403 on ti.com). These facts come from search summaries of TI-derived mirrors (Mouser, Hackaday, alldatasheet and Radiolocman copies of SBAS502). Two independent summaries agreed:
- **Data rates:** DR[2:0] in CONFIG1 gives 125, 250, 500, 1k, 2k, 4k and 8k SPS. DR = 000 is f_MOD/1024 = 125 SPS; DR = 110 is f_MOD/16 = 8 kSPS. The TI product page gives the range as 125 SPS to 8 kSPS. f_MOD = f_CLK/4 or f_CLK/16, depending on CLK_DIV. On the internal 512 kHz clock, f_MOD = 128 kHz, which matches `afe-sim-results.md`.
- **Decimation filter:** "variable decimation rate, **third-order** (sinc3), low-pass".
- **−3 dB bandwidth:** **32.75 Hz at 125 SPS, 65.5 Hz at 250 SPS, 131 Hz at 500 SPS**, from the datasheet's noise tables. The family relation is **0.262 × f_DR**, which gives 262 Hz at 1 kSPS and 524 Hz at 2 kSPS. That relation appears in the noise-table headers ("−3-dB bandwidth 0.262 f_DR Hz").
- **Noise rises with data rate** (rows seen for the family, gain-dependent). At gain 12 the figures were 1.1 µVrms at 1 kSPS and 1.7 µVrms at 2 kSPS. The gain 6 rows at 1 and 2 kSPS were **not** retrieved (UNVERIFIED).

**Cross-check (derived, strong).** A sinc3 filter, |sin(πfN/f_MOD)/(N·sin(πf/f_MOD))|³ with N = f_MOD/f_DR, gives −3 dB at **0.2615 × f_DR**: 32.7, 65.4, 130.8, 261.5 and 523.1 Hz. These match the datasheet figures to the stated precision, so the model can be used for the in-band calculations below (`A3-sim-sampling.py`).

### 2.2 Decimation-filter gain at the frequencies that matter (derived)

| data rate | −3 dB | 90 Hz | 120 Hz | 200 Hz | 250 Hz | 450 Hz | Nyquist |
|---|---|---|---|---|---|---|---|
| 500 SPS | 131 Hz | −1.40 dB | −2.52 dB | −7.26 dB | −11.8 dB | **not representable** | 250 Hz |
| 1 kSPS | 262 Hz | −0.35 | −0.62 | −1.74 | −2.74 | −9.34 dB | 500 Hz |
| 2 kSPS | 523 Hz | −0.09 | −0.15 | −0.43 | −0.67 | −2.21 dB | 1000 Hz |
| 4 kSPS | 1047 Hz | −0.02 | −0.04 | −0.11 | −0.17 | −0.54 dB | 2000 Hz |

This filter is ten to fifty times stronger than the analogue input filter that `AFE-DESIGN-REVIEW.md` §3.1 checked. That section reported a 0.5% tilt across 90–120 Hz and passed it. **It did not consider the decimation filter.** At 500 SPS the digital filter alone tilts 90–120 Hz by 1.1 dB, and at 1 kSPS by 0.27 dB.

### 2.3 Effect on median frequency (derived from a model; strength limited)

Method: a Shwedyk-type EMG power spectrum, scaled so that the true MDF within 20–450 Hz is 120 Hz ("fresh") or 90 Hz ("cooked"), as in `CLAUDE.md`. The model passes it through the sinc3 response, folds every alias band back into baseband, applies a 4th-order 20 Hz high-pass, and computes MDF over 20 Hz to min(450 Hz, Nyquist).

| data rate | measured MDF, fresh (true 120) | fatigued (true 90) | measured drop (true −25%) |
|---|---|---|---|
| 500 SPS | **86.3 Hz** | 71.4 Hz | **−17.2%** |
| 1 kSPS | 106.0 | 82.9 | −21.7% |
| 2 kSPS | 115.8 | 88.1 | −23.9% |
| 4 kSPS | 119.0 | 89.7 | −24.6% |

Aliasing is not the problem: the sinc3 nulls at multiples of f_DR leave less than 0.5% of output power aliased, even at 500 SPS. The problems are the **in-band droop and the truncation**:
- At 500 SPS, about 14% of the model's EMG power lies above the 250 Hz Nyquist limit and is simply gone.
- The power left between 130 and 250 Hz is attenuated by 3–12 dB.
- Together these pull MDF down by about 34 Hz and compress the fatigue change by about a third.
- The bias is **not constant**: it is larger when the spectrum is high (fresh), so it eats into exactly the change the product measures.

At 1 kSPS the bias is deterministic and mostly correctable. An inverse-sinc3 equaliser up to about 400 Hz is well-conditioned (−9 dB at 450 Hz is recoverable if the noise floor allows). At 500 SPS nothing above 250 Hz can be recovered.

**Recommendation:** DR = 100 (2 kSPS), with a 20–450 Hz analysis band. Optionally apply sinc3 compensation, since 450 Hz is still −2.2 dB at 2 kSPS. The extra noise at the higher data rate (+0.6 µVrms at gain 12) is small against EMG at 50 µV–5 mV. ESP32 and BLE bandwidth at 2 kSPS × 24 bit is 48 kbit/s of raw data, which is feasible but argues for on-device feature extraction (Task 8). The literature agrees with a sample rate of at least 1 kHz:
- A shoulder EMG spectral study gave a minimum of **1,340 Hz** for surface EMG (Henn & Hillstrom, SECONDARY).
- Ives & Wigglesworth 2003 (Clin Biomech 18:543–552) studied the effect of sampling rate on timing and amplitude. Its results could **not** be retrieved (UNVERIFIED), so it is not relied on here.

**Two caveats.**
- The model spectrum is a textbook shape, not a TENSR recording. Real dry-electrode spectra through 25.4 mm IED will differ. The direction and rough size of the bias hold for any spectrum with meaningful power above 130 Hz.
- An IED-dependent spectral dip also exists (M, derived). An ideal bipolar pair has a zero at f = v/IED. At 25.4 mm that is 157 Hz for a conduction velocity of 4 m/s and **118 Hz at 3 m/s**: inside the fatigue band, and moving with fatigue. At 20 mm the zeros sit at 200 and 150 Hz. In a single-velocity idealisation, the 25.4 mm pair lowers MDF by about 10 Hz more than a 20 mm pair. Real fibres have a spread of velocities, IZ geometry and finite length, all of which smear the dip, so treat this as an upper bound. It does mean TENSR's absolute MDF numbers will not match published 20 mm values. It also partly explains why MDF tracks conduction velocity at all. [M; limited]

### 2.4 LSM6DSO

From ST product-page and retailer summaries (SECONDARY):
- Accelerometer and gyroscope output data rates go up to **6.66 kHz**.
- 9 KB FIFO with batching and compression.
- Accelerometer ±2/4/8/16 g; gyroscope ±125–2000 dps.

The full ODR ladder (12.5 / 26 / 52 / 104 / … Hz) was not retrieved (UNVERIFIED). The brief's "100 Hz" would in practice be the nearest ODR step, believed to be 104 Hz. That is ample for rep segmentation (lifting cadence is below 1 Hz, and harmonics of interest are below 20 Hz). For motion-artefact reference signals, 200–400 Hz would be better (Task 4). The FIFO can timestamp and align IMU data to ADS1292R DRDY.

---

## Task 3 — Dry vs gel electrodes; skin, fat, sweat, pressure

**Wearable dry/textile vs research systems, during exercise**

| study | n | task | reference | finding |
|---|---|---|---|---|
| Lynn 2018, JSSM 17:205 (ABSTRACT) | not retrieved | dynamic knee extension / squat-type, Athos compression garment | research-grade sEMG worn **at the same time** | No significant system effect on peak, sum and 95th-percentile amplitude. Torque–EMG relation did not differ. Rep-to-rep variability of MVC-normalised amplitude 12% (Athos) vs 10.7% (research). |
| Colyer & McGuigan 2018, JSSM 17:101 (ABSTRACT) | 16 recreational males | run, cycle, squat | Delsys Trigno (silver-bar, dry) | Comparable amplitude; **poorer agreement at higher excitation**; **textile bursts consistently longer** (timing not interchangeable); within-session CV 13.8% vs 14.1%. |
| Finni 2007; Tikkanen 2013 (SECONDARY via Colyer) | — | isometric / static half-squat | gel | Close agreement in static tasks. |

These support TENSR **weakly and indirectly** [I; limited], for four reasons:
1. Both use **MVC-normalised amplitude**. Neither validated MDF or any spectral fatigue index from dry electrodes.
2. Garments spread their electrodes over large areas, whereas TENSR uses 7 mm studs.
3. Garment compression is consistent; a 38 mm band's contact force changes with the muscle's cross-section as it contracts.
4. "No significant difference" is not equivalence (standard 6). Neither abstract reported limits of agreement.

Lynn 2018 was co-authored by Athos staff (COI flag; author list from a search summary).

**Dry vs wet, mechanistically**
- **Searle & Kirkup 2000** (Physiol Meas 21:271–283; SECONDARY) found dry and insulating electrodes could match wet Ag/AgCl, but only **when buffered and shielded** (active electrodes). TENSR's electrodes are passive, with 200 kΩ in series and roughly 10 mm traces to the AFE, so the result does not transfer. [I; limited]
- A dry-electrode comparison found Ag/AgCl about **three times better** than stainless steel in its test metric (SECONDARY; source not pinned down, UNVERIFIED).
- Reviews agree that dry electrodes have higher and more variable skin impedance and are more prone to motion artefact (SECONDARY).
- Under a dry electrode, sweat accumulates and impedance falls to a plateau over minutes. Gel electrodes dry over hours. Dry-electrode signal quality is therefore **time-varying within a session**: set 1 is recorded at higher impedance than set 4. That changes amplitude, the input-filter corner and CMRR (`afe-sim-results.md` §1b: the corner falls from 796 Hz to 354 Hz at 250 kΩ skin; with 100 pF C1/C2 it is about 3.5 kHz). **Within-session drift from impedance will look like a fatigue trend in amplitude.** [M; moderate]
- **Hair** stops a 7 mm stud making contact. Calves, quads and chests are often hairy. [M]

**Subcutaneous fat.**
- Nordander et al. 2003 (Eur J Appl Physiol 89:514–519, doi:10.1007/s00421-003-0819-1; SECONDARY) found that skin-to-muscle distance (ultrasound, skinfold, BMI) explained about 21% of the variance in amplitude at MVC and up to 33% in submaximal contractions.
- Baars et al. 2006 (conference abstract, SECONDARY), biceps, n = 27: fat attenuates both amplitude and frequency parameters. Tissue acts as a spatial low-pass filter.

Consequences: absolute amplitude and absolute MDF thresholds will not transfer between users, and **glute, quad and calf in people with more adipose tissue will read lower and lower in frequency** [I; moderate]. Larger IEDs record from deeper, which partly offsets this at the cost of crosstalk.

**Band pressure and contact force.** No study found that quantifies EMG quality against contact force for band-mounted studs. This is a gap [H; none]. It is mechanically plausible that contact force changes within each rep as the muscle's girth changes. That would modulate impedance at rep frequency, which is a motion artefact locked exactly to the reps.

**Gel snap electrodes.** If TENSR shipped with snap-on gel electrodes, the electrode-site impedance and mismatch problems would mostly go away (SENIAM-type electrodes). The geometry problems would remain, since the snaps fix the IED at 25.4 mm. **This is the single biggest signal-quality lever available without a respin.** [M; moderate]

---

## Task 4 — Artefacts, filtering, and when to withhold output

**Sources and spectra**
- **Motion and cable artefact:** mostly below 10–20 Hz. De Luca et al. 2010 (J Biomech 43:1573–1579, doi:10.1016/j.jbiomech.2010.01.027) weighed high-pass corners against artefact rejection. They are widely cited for a **20 Hz high-pass (2nd-order Butterworth)** as the best compromise. The exact recommendation was seen only in secondary form (SECONDARY; the full text at bu.edu was not reachable). TENSR has no cables, but it has a stud–skin interface that moves with every rep. Its dominant artefact will be electrode–skin shear and pressure change, which is rep-locked.
- **Mains:** 50 Hz plus harmonics. A battery-powered body-worn device has weak capacitive coupling to mains, but gyms have mains-powered machines. Mismatched dry-electrode impedance converts common mode to differential (28–48 dB ceiling in the AFE simulation). A 50 Hz notch distorts MDF slightly (it removes power near the low end of the spectrum, which raises MDF) and should be applied the same way every time.
- **Clipping / saturation:** at gain 6 with a 2.42 V reference (UNVERIFIED reference value), the input range is about ±400 mV, which is far above EMG. Electrode-offset drift on dry electrodes (hundreds of mV) is the realistic way to saturate. The ADS1292R's lead-off detection and DC monitoring can flag it.
- **Dropout:** a lost BLE packet or loss of skin contact. Dropout must be flagged in the data, never interpolated before spectral estimation.
- **Crosstalk:** worse with larger IED and on small muscles (CEDE 2019). It cannot be detected from a single channel.
- **ECG:** on chest and glute placements the QRS complex (energy 5–40 Hz) can leak through a 20 Hz high-pass. This is an issue for pectoralis.

**Filters and windows: effects on onset, timing and MDF**
- A 20 Hz high-pass removes most artefact. Its effect on MDF is small and consistent: with a 4th-order filter, the 120 Hz model MDF moved by under 1 Hz.
- An envelope (RMS or low-pass) delays onset and offset timing by a fraction of the window. Use a zero-phase filter offline and record the causal delay online.
- **MDF estimator variance** (derived, `A3-sim-mdf-window.py`): a stationary Gaussian signal with the model spectrum at 2 kSPS, Welch method with 125 ms Hann segments, 800 trials.

| analysis window | MDF SD | 95% range |
|---|---|---|
| 0.25 s | 13.3 Hz | ±26 Hz |
| 0.5 s | 9.3 Hz | ±18 Hz |
| 1.0 s | 6.7 Hz | ±13 Hz |
| 2.0 s | 4.7 Hz | ±9 Hz |

  This is the **floor**: a real dynamic contraction adds non-stationarity, changes in joint angle and force, innervation-zone shift and electrode movement. Farina & Merletti 2000 (JEK 10:337–349, doi:10.1016/S1050-6411(00)00025-0; ABSTRACT-level bibliographic) compared estimators, and longer epochs reduced estimate variance (SECONDARY). Bonato et al. 2001 (IEEE TBME 48:745–753; SECONDARY) argue that dynamic contractions need time-frequency (Cohen-class) instantaneous MDF, computed at matched joint-angle phases of each cycle.
- **Implication for the product:** a concentric phase of about 0.5–1 s gives a per-rep MDF with SD ≥ 7–9 Hz, against a 30 Hz total change from first rep to failure. Single-rep MDF cannot decide "2 reps left". A **regression of MDF on rep number** over several reps can show a trend [M/derived; moderate for the statistics, none for TENSR]. Estimating at a matched phase of each rep is better than over whole-rep windows, and the IMU can supply that phase.

**Signal-quality indices and withholding output** [H; proposal for A5 to test]

| SQI | computed from | withhold or flag when |
|---|---|---|
| lead-off / contact | ADS1292R lead-off comparators, DC offset | any electrode off; offset near the rails |
| low-frequency power ratio | power below 20 Hz / power 20–450 Hz, per rep | above a validated threshold (motion artefact) |
| mains ratio | power at 50 Hz ± 1 Hz / band power, between reps | above threshold (CMRR collapse, usually electrode mismatch) |
| rep SNR | rep-burst RMS / inter-rep baseline RMS | low SNR (light load, wrong muscle, poor contact) |
| clipping count | samples at full scale | any |
| packet continuity | sequence numbers | any gap inside the analysis window |
| IMU–EMG coupling | coherence between acceleration jerk and EMG low-frequency power | high coherence means artefact |
| impedance drift | baseline noise RMS over the session | monotonic drift: flag amplitude trends as unreliable |
| spectral plausibility | MDF of each rep within a per-user range | outside the range |

**Rule:** a set whose reps fail the SQI should show "no reading", not a number. Showing a number for every set is what makes a consumer device misleading.

---

## Task 5 — Repeatability across sessions and re-application

- **Within session, dynamic tasks:** amplitude ICCs are usually high. Fauth et al. 2010 (JSCR 24(4); ABSTRACT), on isometric and ballistic quadriceps and hamstrings tasks: most ICCs above 0.90, **but CV_intra 11.5–49.3% and CV_inter 5.4–148.7%**. High ICC with large CV is the classic case where correlation is mistaken for individual precision (standard 6). [I; moderate]
- **Between days:**
  - A 2026 study of landing and cutting (Frampton et al., Applied Sciences; ABSTRACT): within-session ICCs moderate to excellent, between-session ICCs **poor to excellent**. The authors advise caution between days.
  - A 2017 quadriceps study (PMC5427161; ABSTRACT): sEMG reliability is "typically modest even with rigorous methods", and averaging **two sites** improves it. TENSR has one site.
- **Spectral fatigue indices:**
  - Mathur et al. 2005 (PubMed 15642658, JEK; ABSTRACT), quadriceps sustained contractions, n = 22, one week apart: initial and final MDF and amplitude ICC 0.59–0.88 (MDF) and 0.58–0.99 (amplitude). Normalised final values were more reliable than slopes.
  - A review summary reports **MDF-slope CVs of 14–27%** at about 50% MVC, with initial MDF more stable than slope (SECONDARY).
  - Repetitive lifting, PubMed 12165687, 2002 (ABSTRACT; authors not retrieved): instantaneous MDF and its change over time were reproducible at 2 h and 2 weeks.
  - Repeated maximal concentric knee extensions (Larsson et al. 2003, JEK 13:281–287; SECONDARY): ICC for slope over the total time 0.65–0.90, with mean-frequency slope less reliable at some muscle sites.
  - Isometric back extension, 1 week, n = 20 (PubMed 18396412; ABSTRACT): reliable. [I; moderate that initial MDF is reproducible; limited that the slope is]
- **SEM and MDC** were not retrieved for a dynamic, free-weight, re-applied, dry-electrode protocol. **None of the studies above tests a band put on by the user**, and that is TENSR's real condition. [none]

**Implication:** an amplitude-based "activation %" or "weekly stimulus" that compares days needs (a) a per-session reference contraction for normalisation and (b) an MDC estimated on re-applied TENSR bands. A5 should power a test-retest study to get the SEM and MDC (minimal detectable change) of per-set MDF slope and normalised amplitude with re-application.

---

## Task 6 — IMU: reps, velocity, artefact

- **Rep counting:**
  - Morris et al. 2014 (RecoFit, CHI; ABSTRACT): forearm IMU, no per-user training, **±1 rep in 93% of sets**, 114 participants, 146 sessions. Shipped in Microsoft Band.
  - Soro et al. 2019 (Sensors 19(3):714; ABSTRACT): smartwatch IMU and a CNN on 10 CrossFit exercises, **±1 rep in 91% of sets**.
  - A conference abstract testing Garmin wrist devices on squats, lunges, push-ups and presses found **no device valid** (MAPE and CCC thresholds); manual counting is advised (IJESAB; not peer reviewed; flagged).

  A ±1-rep error matters when RIR is the target: "2 left" against "3 left" is the same size. TENSR's IMU sits **on the trained segment**, which is probably better than a wrist for single-joint lifts and worse for exercises where the segment barely moves (calf raise: small shank rotation; isometric holds). Counting from EMG bursts and the IMU together is plausible but unvalidated [H]. **Rep counting is the most defensible feature.** [I; moderate]
- **Velocity:** a limb-mounted IMU measures that segment's motion, not the bar's.
  - Orange et al. 2019 (JSCR; ABSTRACT), PUSH band on the forearm vs linear transducer, squat and bench at 20–90% 1RM: valid and reliable only at isolated loads (e.g. mean power at 40% 1RM bench, r = 0.89, ICC = 0.83).
  - van den Tillaar & Ball 2019: mean-velocity r = 0.62–0.70 with a systematic underestimate.
  - Lake et al. 2019, with the PUSH **on the bar**: peak velocity valid, mean velocity not, with proportional bias.

  Conclusion: TENSR must not claim bar velocity or velocity loss. [I; moderate]
- **Artefact rejection:** the IMU on the same puck gives a direct reference for electrode movement. Accelerometer jerk and gyroscope changes can gate or regress out low-frequency EMG contamination. No validation for TENSR-like hardware was found [H]. Use a higher ODR (≥200 Hz) for this role, synchronised to DRDY.

---

## Task 7 — ML critique

| study | target / label | n | validation | realistic? | error reported | baseline | external | key problem |
|---|---|---|---|---|---|---|---|---|
| Garofalo et al. 2026, JEK, doi:10.1016/j.jelekin.2026.103111 (ABSTRACT) | proximity to failure (continuous) | 12; 192 recordings | leave-one-out (subject level stated in summary) | **isometric** biceps holds, lab | MSE 49.4 ± 18.3 (units unclear, not reps) | yes; deep models beat baselines | no | isometric only; small n; error not in interpretable units |
| Thomas & Wahlström 2025, arXiv 2510.03197 (**preprint**) | RPE per set | not retrieved | not retrieved | dumbbell curls; Delsys Trigno EMG + IMU | reported in summary as 41.4% exact / 85.9% ±1 RPE (summary only, UNVERIFIED) | IMU-only vs IMU + EMG | no | EMG added "slightly"; strongest predictor was **eccentric rep time**, a kinematic feature |
| arXiv 2602.15684, ICRA 2026 (**preprint**; authors not retrieved) | fatigue fraction (time to failure) | 10 | not retrieved | robot-guided arm motions | RMSE: CNN 20.8 ± 4.3%, RF 23.3%, XGB 24.8%, **linear regression 26.9%** | **yes** | no | the simple baseline is within about 6 points of deep learning |
| Al-Mulla et al. 2015, J Med Syst (ABSTRACT) | fatigue vs non-fatigue (2 classes) | 13 | 70/30 split of **trials** (subject-dependent risk) | dynamic biceps curls, lab | accuracy 87.9% | none reported | no | labels from segmenting each trial; likely within-subject leakage |
| Al-Mulla et al. 2011, Med Eng Phys (ABSTRACT) | fatigue classes | 10 | not retrieved | semi-isometric | 88.4% | — | no | isometric |
| Karthick et al. 2018, Comput Methods Programs Biomed (**details UNVERIFIED**) | fatigue vs non-fatigue | not retrieved | not retrieved | biceps, lab | not retrieved | — | — | bibliographic only; not used as support |
| Baek et al. 2025, Sensors (PMC12609798; ABSTRACT) — non-EMG comparator | RPE | 32 men, 64 limbs | not retrieved | robotic isokinetic bench, load cell | 93% within ±1 RPE | RF best of several | no | shows **force-time data alone** predicts RPE as well as most EMG models; label is subjective |
| Soro et al. 2019 (ABSTRACT) | exercise class + rep start | not retrieved | not retrieved | CrossFit, smartwatch | 99.96% recognition; ±1 rep 91% | — | no | IMU, not EMG |
| Morris et al. 2014 (ABSTRACT) | exercise segmentation, class, count | 114 / 146 sessions | cross-validation + a separate evaluation study | gym circuits | ±1 rep 93% | — | partial (a separate study) | the strongest validation design in this table |
| "Rep Smarter, Not Harder", arXiv 2512.11854 (**preprint**, UNVERIFIED details) | real-time RIR on Apple Watch | not retrieved | not retrieved | — | not retrieved | — | — | claims to be the first complete wearable RIR pipeline; nothing verified |

The search also returned an unattributed dynamic-contraction fatigue study (n = 15) in which inter-subject classification fell to a **correct-classification rate of 0.68 ± 0.04**, well below within-subject results. It is UNVERIFIED, not in the CSV, and not used as support.

**Weaknesses across the field** [I; moderate that they are common in the studies found; the sample is small because the search budget ran out]
1. **The target is weakly defined.** "Fatigue" is variously a time fraction, a subjective rating (RPE or Borg), a segment of a trial (first third vs last third), or task failure. Only task failure or reps-to-failure is objective and relevant to the product, and almost no study uses it in dynamic free-weight lifting.
2. **Labels are circular.** Splitting each trial into "non-fatigued" and "fatigued" segments by time means the classifier can learn **time-on-task** (rising amplitude, electrode drift, sweat-driven impedance fall) rather than fatigue.
3. **Validation leaks.** Random 70/30 splits of trials or overlapping windows put windows from the same set and the same person in both train and test. Accuracy then reflects subject identity and temporal neighbours. Where leave-one-subject-out results appear, they fall sharply.
4. **No re-application.** No study found re-applies the electrodes between training and test sessions, which is exactly what a consumer does.
5. **Lab conditions.** Gel electrodes, shaved and abraded skin, research amplifiers at 1–2 kHz or more, single isolated exercises, isometric or machine-guided motion.
6. **Accuracy instead of error.** Class accuracy, or MSE in unclear units, rather than error in reps with limits of agreement.
7. **Baselines and external validation are rare.** Where a simple baseline was reported, the gain from complex models was small (26.9% vs 20.8% RMSE). Two results suggest kinematic, rep-time or force-time features carry much of the signal: eccentric rep time was the top RPE predictor, and a load cell alone predicted RPE to ±1 in 93% of cases. That raises the question of whether EMG adds value beyond an IMU on the same puck.
8. **n is small** (10–32), mostly young and untrained or recreational, often men only.
9. **Preprints dominate the most product-relevant work** (RIR or RPE from wearables), with no peer review.

**What TENSR's own validation must do (handed to A5):**
- Validate leave-one-subject-out **and** leave-one-session-out with the band re-applied.
- Use objective reps-to-failure as the label.
- Report error in reps with Bland–Altman limits.
- Compare against three baselines: (a) rep-velocity or rep-duration slowdown from the IMU alone, (b) MDF slope alone, (c) the person's own RIR guess.
- Test on mixed tempos and free weights.

---

## Task 8 — Real-time latency vs reliability for per-rep feedback over BLE

Derived and mechanistic; no TENSR-specific literature found [M/H].

- **What sets latency:** the end of the rep must first be detected, which takes the IMU or EMG offset plus a short guard of about 100–300 ms. A spectral window then needs about 0.5–1 s of the rep's own data. That is already available when the rep ends if features are computed over the concentric phase. Computation on an ESP32-S3 for a 1–2k-point FFT takes milliseconds. Transport is one BLE connection interval: the core spec minimum is 7.5 ms, and phones commonly negotiate 15–50 ms (UNVERIFIED in this session). The app adds rendering time. A total of **0.3–0.6 s after the rep ends** is realistic, which is acceptable for between-rep feedback.
- **Trade-off:** reliability comes from **more data per decision**: longer windows, several reps in a regression, SQI gating. The SD of a single-rep MDF (≥9 Hz) against the 30 Hz full-range change means a reliable trend needs about 4–6 reps. "Live RIR" in the first reps of a set will therefore be either noisy or late, so the honest design is to **say nothing until the trend is estimable**.
- **Architecture:** compute features on the puck and send one small record per rep (count, MDF, RMS, SQI flags, timestamps). Stream raw 2 kSPS data only for logging or research mode. Raw at 2 kSPS × 3 bytes is 6 kB/s, which is feasible with BLE data-length extension but power-hungry and vulnerable to dropouts. Drive the haptic motor from the puck so that BLE is not in the feedback loop.
- **Reliability rule:** never fill missing packets by interpolation before a spectral estimate. Mark the rep invalid.

---

## Evidence position for the coordinator (RQ3 and RQ4)

| question | answer | code | strength |
|---|---|---|---|
| Does the board's planned 500 SPS support MDF fatigue? | No. −3 dB at 131 Hz, Nyquist 250 Hz; MDF biased about 30% low and fatigue change compressed by about a third | M (datasheet + derived) | strong (datasheet relation cross-validated by model) |
| Minimum data rate | 1 kSPS with sinc3 compensation; **2 kSPS recommended** | M | moderate |
| Does TENSR meet SENIAM? | Size yes; IED no (25.4 vs 20 mm); orientation, IZ, skin prep and reference uncontrolled or different | I/M | moderate |
| Are dry-wearable amplitude measures valid during exercise? | Roughly, when MVC-normalised, in garments (Athos, textile shorts); timing not interchangeable; spectral not validated | I | limited |
| Is per-rep MDF precise enough for RIR? | No. Single-rep SD ≥9 Hz against a 30 Hz full change; needs multi-rep trends | M (derived) | moderate |
| Between-day comparability | Initial or final MDF moderately reproducible; slopes and non-normalised amplitude are not; re-application by the user untested | I | limited |
| IMU rep count | ±1 rep in about 91–93% of sets in lab studies; mixed independent evidence | I | moderate |
| IMU bar velocity | Not supportable from a limb puck | I | moderate |
| ML fatigue/RIR from sEMG in free-weight training | No adequately validated study found | — | none |
