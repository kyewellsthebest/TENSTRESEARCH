# X3 search log — velocity / rep-duration methods beyond barbell squat and bench

Agent X3, 2026-11-03. Tool: WebSearch (search-engine summaries of abstracts and repository records).
**WebFetch is blocked for every host tried** (DNS refusal from the session's network allow-list):
pmc.ncbi.nlm.nih.gov, lida.sport-iat.de, peerj.com and rke.abertay.ac.uk. **No full text was read this round.**
Every number below comes from an abstract excerpt or a secondary summary, and is marked that way in `X3-studies.csv`.

Searches: 36 (budget ~35). Fetches: 4, all failed.

| # | query (abridged) | mode | useful hits |
|---|---|---|---|
| F1 | WebFetch PMC10901726 (Jukic 2024) | – | FAILED: host not allowed |
| 1 | VL %reps completed dumbbell OR machine | std | Smith squat %Rep under fatigue (Applied Sci 2024, abs. error >10%); Smith BP SEE 7-10% |
| 2 | VBT single-joint biceps curl VL RIR | ext | Paulsen 2025 PeerJ (PMC12360324); coaches' eye 2.6 reps error; nothing single-joint |
| 3 | MVT leg press, lat pulldown, seated row | ext | NSCA VBT table: pulldown 0.47, row 0.40, leg press 0.21 m/s; García-Ramos 2020 Vlast |
| 4 | Morán-Navarro 2019 RIR velocity | std | Rodríguez-Rosell 2020; IJSM 2024 individual %rep-%VL slightly stronger than general |
| 5 | "Movement velocity as a measure of level of effort..." | std | JSCR 33(6):1496; n=30; 4 exercises; velocity at RIR stable across loads and levels |
| 6 | "Exercise type, training load, VL threshold, and sets..." | std | Paulsen 2025 PeerJ |
| F2/F3 | WebFetch lida, peerj | – | FAILED |
| 7 | Morán-Navarro exercises list | std | Rodríguez-Rosell 2020 R2 0.97/0.93; Paulsen r2~0.3 |
| 8 | Jukic 2023 individual vs general | ext | EJAP >10% error; Physiol Behav 1.96 vs 2.81 reps; Applied Sci 2024 stability |
| F4 | WebFetch Abertay PDF | – | FAILED |
| 9 | Jukic 2024 46 participants | std | n=46 (15F/31M), 72 h apart, individual <2 reps |
| 10 | VL RIR isolation lifts + LPT | ext | Mansfield 2023; older-adult RIR studies; none isolation |
| 11 | García-Ramos last-rep velocity reliability | std | PeerJ 2020: CV >18.3%, ICC <0.60, n=96 |
| 12 | Mansfield 2023 results | std | 30.9% reps correctly classified; BP + prone row |
| 13 | VL %reps pulling exercises | std | Sánchez-Moreno 2017 pull-up R2 .88 n=52; pulldown/row 1RM study n=23 |
| 14 | leg press VL %reps 2024 | std | postmenopausal women LP/BP n=35, high intercept variability |
| 15 | wrist IMU smartwatch Apple Watch | ext | Achermann 2023; Beast wrist (Balsalobre 2017) |
| 16 | concentric duration as failure predictor | ext | nothing direct |
| 17 | Apple Watch validity paper | std | wrist r .952-.965, SEE 0.064 m/s |
| 18 | PUSH forearm Balsalobre/Lake/Sato | std | Banyard 2017, Callaghan 2022, Pérez-Castilla 2021 |
| 19 | IMU forearm angular velocity curl fatigue | ext | Elshafei 2021 wrist IMU curls |
| 20 | dumbbell VBT validity | ext | Sato 2015 (n=5), PUSH DB press 12.6/14.0% deviation (unsourced) |
| 21 | PUSH dumbbell r=0.86 | std | Sato 2015 r .80-.92 pooled; Orange 2019 critique |
| 22 | Elshafei 2021 accuracy | std | design only |
| 23 | L-V leg extension / leg curl MVT | ext | SSH 2025 ten lower-limb exercises; PLOS ONE 2019 leg ext; leg curl r<=0.22 |
| 24 | Smith vs free weight VL | std | Miras-Moreno 2023 Heliyon PBP; Marcos-Frutos 2025 training |
| 25 | controlled tempo VL proximity | ext | Qin 2025 (PMID 40133968); inter-rep interval paper; nothing on tempo |
| 26 | Weakley 2020 VL RPE | std | Weakley 2020 VL10/20/30 squat; Paulsen detail (19 lifters, 2,972 obs) |
| 27 | "Gauging proximity to failure in the bench press" | std | Qin 2025: general RIR-velocity bias -0.4 to +0.6 reps |
| 28 | 40% VL reaches failure 56% | std | NOT confirmed; claim dropped |
| 29 | Sánchez-Medina 2011 details | std | secondary only (r 0.97 / ~0.95 vs lactate) |
| 30 | González-Badillo 2017 | std | n=22+28, Smith BP, equations; R2 not captured |
| 31 | Hernández-Belmonte level of effort | std | squat/shoulder press/PBP; SEM <=1.9 reps; R2 >=0.97 |
| 32 | VL RIR machine exercises 2023-25 | ext | nothing machine-specific |
| 33 | repetition duration across set to failure | std | Izquierdo 2006; Rodríguez-Rosell 2020 |
| 34 | thigh / upper-arm IMU bar velocity | std | nothing; Vmaxpro Biol Sport 2023; IMU SR 2021 |
| 35 | general vs individual MVT | std | Janicijevic 2021; García-Ramos 2023 optimal MVT (n=126) |
| 36 | Elshafei accuracy / subject-independent | std | 2022 personalisation follow-up; arXiv 2510.03197 RPE estimation (not opened) |

**Searched for and not found:** any VL→RIR or VL→%reps validation on a single-joint/isolation exercise
(curl, triceps extension, lateral raise, leg extension, leg curl); any on cables; any on dumbbells; any
validation of a thigh- or upper-arm-worn IMU against bar velocity; any study of concentric duration as a
failure predictor; any study of velocity-based RIR under an imposed slow tempo.
