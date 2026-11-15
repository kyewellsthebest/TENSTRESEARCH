# Top-5 muscle-growth factors for trained lifters — summary

2026-11-02. Full report: `TENSR-TOP5-FACTORS.pdf` (built by `make_top5_pdf.py`). Evidence: `TOP5-STUDIES.csv`
(260 unique studies, 84 meta-analyses/reviews, 64 re-checked by the auditor). Agent notes: `F1`–`F6`, audit `FA-audit.md`.
All sources were checked at abstract/summary level only. Full text was blocked by the network policy.

| # | Factor | Rule | Confidence |
|---|---|---|---|
| 1= | Effort (proximity to failure) | Sets end ~0–3 reps in reserve, closer with light loads; failure adds little | Moderate (threshold) |
| 1= | Weekly hard-set volume per muscle | More hard sets, diminishing returns; ~10–20/week a sensible working range; no universal optimum | Moderate |
| 3 | Exercise selection & muscle length | Avoid short-range-only reps; load muscles stretched; cover regions | Low–moderate (null in trained so far) |
| 4 | Rest that preserves reps | ≥90 s; 2–3 min heavy compounds; add sets if resting less | Low–moderate |
| 5 | Keep sets hard as you adapt | Add load or reps (equal); any load ≥~30% 1RM | Moderate |

Effort is the gate and volume is the dial. Factors 4–5 are rules that protect 1–2 rather than independent levers
(auditor's view, kept). Protein (~1.6 g/kg/day) has a real effect but is outside the working-set brief.

**No effect in trained lifters:** tempo/TUT (0.5–8 s), eccentric emphasis, pauses (no trials), squeezing (no
trials), drop sets, supersets, rest-pause, cluster sets, frequency (volume-equated), periodisation, cheat reps
(one trial), more fatigue, more EMG.

**TENSR tracking.** None of the levels below needs a new board.
- **Level A (firmware + app):** tracks 3 of 5. Volume is counted, rest is timed, progression is logged from entered
  weight. Effort comes from the user's own tag.
- **Level B (second TENSR puck as a clip):** tracks 4–5 of 5.
  - On the bar: rep speed and velocity loss give a personal reps-left model. It is validated only on the back squat
    (Jukic 2024), and TENSR's own algorithm is untested.
  - On the next limb segment: joint angle for range of motion. Accurate to about 3–5° in the lab, untested under load.
- **New board (v2/v3):** a second EMG pair, or A-mode ultrasound for muscle thickness. Ultrasound is the only route
  to measuring growth itself.

Weight-stack load identification was dropped, because it needs a magnetometer.

The auditor confirmed the board facts from `routed.kicad_pcb`: the LSM6DSO sensor-hub pins are tied to GND, the J3
pinout is as documented, and ADS1292R CH2 is tied off.
