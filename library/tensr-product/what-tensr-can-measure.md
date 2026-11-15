# What TENSR can and can't measure

**Verdict:** confidence **moderate**; last updated 2026-11-03.

- **Can measure:** reps, sets, set duration, rest time and weekly hard sets for one muscle.
- **Only after validation:**
  - a post-set EMG fatigue trend;
  - effort grades;
  - reps-in-reserve estimates on compound lifts, using a second puck clipped to the bar.
- **Avoid claiming:** optimal fatigue or time under tension, activation %, any hypertrophy or stimulus score,
  "recovered" timers, or anything clinical.
- **Hardware:**
  - Sample at 2 kSPS, not 500.
  - Fix and record the electrode orientation.
  - The ADS1292R's second channel, and the IMU's sensor hub for an external magnetometer, would each need a board
    respin.

**Reports:** [`TENSR-RESEARCH-REPORT.pdf`](../../TENSR-RESEARCH-REPORT.pdf) ·
[`top5/TENSR-TOP5-FACTORS.pdf`](../../top5/TENSR-TOP5-FACTORS.pdf) ·
[`failure/TENSR-EFFORT-FAILURE-TRACKING.pdf`](../../failure/TENSR-EFFORT-FAILURE-TRACKING.pdf)
