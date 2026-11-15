"""Builds TENSR-EFFORT-FAILURE-TRACKING.pdf from the failure/effort research round (X1-X4 + XA audit)."""
import csv, html
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, NextPageTemplate, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

D = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', D + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', D + 'DejaVuSans-Bold.ttf'))
registerFontFamily('DV', normal='DV', bold='DVB', italic='DV', boldItalic='DVB')

R = '/home/user/tenstresearch/failure/'
OUT = R + 'TENSR-EFFORT-FAILURE-TRACKING.pdf'
INK = colors.HexColor('#1b1f24'); MUTED = colors.HexColor('#5a6370'); ACC = colors.HexColor('#0b6e6e')
LINE = colors.HexColor('#d6dbe1'); BAND = colors.HexColor('#f2f5f7')
GOOD = colors.HexColor('#dff2e4'); MID = colors.HexColor('#fdf3d6'); RES = colors.HexColor('#e6ecf7')
BAD = colors.HexColor('#f9e0e0'); WARN = colors.HexColor('#fff8e8')

def st(n, **k): return ParagraphStyle(n, fontName=k.pop('f', 'DV'), textColor=k.pop('c', INK), **k)
H0 = st('h0', f='DVB', fontSize=25, leading=30, spaceAfter=6)
SUB = st('sub', fontSize=12, leading=16, c=MUTED, spaceAfter=4)
H1 = st('h1', f='DVB', fontSize=17, leading=21, c=ACC, spaceAfter=8)
H2 = st('h2', f='DVB', fontSize=12.5, leading=16, spaceBefore=9, spaceAfter=4)
H3 = st('h3', f='DVB', fontSize=10.5, leading=13.5, spaceBefore=6, spaceAfter=3)
P = st('p', fontSize=9.5, leading=13.4, spaceAfter=5)
PS = st('ps', fontSize=8.5, leading=11.5, spaceAfter=3, c=MUTED)
B = st('b', fontSize=9.5, leading=13.2, leftIndent=12, bulletIndent=2, spaceAfter=2)
C = st('c', fontSize=8.2, leading=10.6)
CB = st('cb', f='DVB', fontSize=8.2, leading=10.6)
T = st('t', fontSize=6.8, leading=8.5)
TB = st('tb', f='DVB', fontSize=6.9, leading=8.7)
CALL = st('call', fontSize=10, leading=14)

def esc(s): return html.escape(s or '', quote=False)
def para(t, s=P): return Paragraph(t, s)
def bullets(items, s=B): return [Paragraph(i, s, bulletText='•') for i in items]
def box(flow, bg=BAND, pad=8):
    t = Table([[flow]])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), bg), ('BOX', (0, 0), (-1, -1), 0.5, LINE),
                           ('LEFTPADDING', (0, 0), (-1, -1), pad), ('RIGHTPADDING', (0, 0), (-1, -1), pad),
                           ('TOPPADDING', (0, 0), (-1, -1), pad), ('BOTTOMPADDING', (0, 0), (-1, -1), pad)]))
    return t
def grid(rows, widths, head=True, style=C, shades=None):
    data = [[Paragraph(c, CB if (head and i == 0) else style) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    ts = [('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
          ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    if head: ts.append(('BACKGROUND', (0, 0), (-1, 0), BAND))
    for r, col in (shades or []): ts.append(('BACKGROUND', (0, r), (-1, r), col))
    t.setStyle(TableStyle(ts)); return t
def deco(c, d):
    c.saveState(); c.setFont('DV', 7.5); c.setFillColor(MUTED); w, h = c._pagesize
    c.drawString(15 * mm, 9 * mm, 'TENSR · Tracking effort and failure · 3 Nov 2026 · research only — not product claims')
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='TENSR Effort and Failure Tracking',
                      author='TENSR research team (Claude Code)',
                      subject='How TENSR can track proximity to failure — the #1 growth factor')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(12 * mm, 14 * mm, lw - 24 * mm, lh - 26 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm
studies = list(csv.DictReader(open(R + 'FAILURE-STUDIES.csv')))
n_all = len(studies); n_aud = sum(1 for r in studies if r['audit_verdict'] != 'not sampled')
s = []

# ---------------- cover ----------------
s += [Spacer(1, 34 * mm), para('TENSR', st('k', f='DVB', fontSize=11, c=ACC, leading=14)),
      para('Tracking effort: how TENSR can measure how close each set gets to failure', H0),
      para('Effort — proximity to failure — is the #1 factor for muscle growth. Measuring it is TENSR’s core job. '
           'This report covers what happens in the muscle as a set nears failure, what sensors have achieved so far, '
           'where a sensor can beat the lifter’s own guess, and a concrete design for doing it on the current board.', SUB),
      Spacer(1, 6 * mm)]
s.append(box(para(
    '<b>Inside</b><br/>'
    '<b>1</b> The answer in one page · <b>2</b> Why tracking failure is tracking effort · <b>3</b> What happens as a '
    'set approaches failure · <b>4</b> What sensors have achieved so far · <b>5</b> Rep speed beyond the barbell · '
    '<b>6</b> Where TENSR can beat your own guess · <b>7</b> The TENSR design · <b>8</b> How to prove it · '
    '<b>9</b> What TENSR can claim, stage by stage · <b>10</b> Fact-check log · <b>11</b> Every study (%d)' % n_all, CALL)))
s += [Spacer(1, 6 * mm), box(para(
    '<b>How this was done.</b> Four research agents (physiology; sensor results; rep speed beyond the barbell; TENSR '
    'design) searched on 3 Nov 2026, then an independent auditor re-checked %d studies and the design’s maths. '
    '<b>Limits:</b> full papers could not be opened — PubMed, PMC and arXiv were blocked — so every study was checked '
    'at abstract or summary level. No citation was found to be made up. TENSR has not been built, so nothing here has '
    'been measured on a real band.' % n_aud, PS), bg=WARN)]
s.append(PageBreak())

# ---------------- Part 1 ----------------
s.append(para('Part 1 — The answer in one page', H1))
s += bullets([
    '<b>Tracking proximity to failure is tracking effort, the #1 growth factor.</b> It should be TENSR’s core feature. '
    'The only nuance from the research: the band should measure <i>how close</i> you got and let you choose where to '
    'stop — not score a set higher for hitting absolute failure, because 1–3 reps short grows about as much.',
    '<b>Failure itself is easy to see:</b> a rep that stalls or reverses before the top is a mechanical event the motion '
    'sensor can catch. Build this first.',
    '<b>“How many reps are left” is hard:</b> no signal sits at a fixed value at failure. Rep slow-down is the best '
    'predictor, but only when calibrated to you and to each exercise.',
    '<b>Best results so far are about 1–2 reps of error</b>, and only with a sensor on the bar or weight stack for '
    'compound or machine lifts. No wearable on the muscle has published a validated reps-left estimate. TENSR would '
    'be first.',
    '<b>You are already good at judging effort near failure — but bad far from it.</b> Coaches watching video were '
    '<b>4.8 reps off</b> a third of the way into a ~14-rep set (Emanuel 2022), and error grows with longer sets. '
    'The commonest real gym mistake is a set stopped 4–6 reps short that felt like 1–2. That is where TENSR can win.',
    '<b>First product:</b> after every set the band says <b>Failure</b> (stall detected), <b>Hard</b> (≤3 reps left), '
    '<b>Not hard</b> (≥4 left) or <b>Unsure</b>. That feeds an honest weekly hard-set count. A reps-left number comes '
    'later, per exercise, once validation passes.',
    '<b>No new board needed.</b> Everything here runs on the current hardware; a second puck clipped to the bar or next '
    'limb improves it.',
])
s.append(Spacer(1, 4))
s.append(grid([
 ['', 'Today (no band built)', 'After lab validation', 'Never'],
 ['What TENSR can say', '“Designed to count reps, flag sets you take to failure and count your hard sets.”',
  '“Calls hard vs not-hard sets correctly X% of the time” — per exercise class, with a confidence interval. “More '
  'accurate than your own guess” only where the test passed.', '“Grows more muscle”, injury or clinical language.'],
], [W * 0.17, W * 0.27, W * 0.36, W * 0.20], shades=[(1, GOOD)]))
s.append(PageBreak())

# ---------------- Part 2 ----------------
s.append(para('Part 2 — Why tracking failure is tracking effort', H1))
s.append(para('Your point is right, and it fits the evidence. The growth research says:', P))
s += bullets([
    '<b>Effort is the gate.</b> Light and heavy weights build similar muscle only because hard sets push both close to '
    'failure (Schoenfeld 2017a, 21 studies; Morton 2016, 49 trained men).',
    '<b>Sets far from failure barely count</b> — that is the costly mistake, and it is common.',
    '<b>Light loads need to go closer to failure</b> than heavy ones (Lasevicius 2022; Robinson 2024).',
    '<b>Absolute failure vs 1–3 reps short adds little</b> for trained lifters (Refalo 2023/2024; Grgic 2022) — so '
    'failure is a useful <i>marker</i> of effort, not a target in itself.',
])
s.append(para('So the product goal is: <b>tell the lifter, honestly and automatically, how close each set got to '
              'failure</b> — and catch it when it actually happens. Detecting failure sets is valuable because they are '
              'the clearest proof a set was hard, and because they calibrate the band to you.', P))
s.append(para('What changed from our earlier reports', H2))
s.append(para('Earlier we put “did this set reach failure” as a score in research-only. That was about <i>scoring '
              'failure higher than 1–3 reps short</i>, which the evidence doesn’t support. <b>Detecting</b> failure and '
              '<b>measuring</b> how close you got are now the centre of the product.', P))

# ---------------- Part 3 ----------------
s.append(para('Part 3 — What happens in the muscle as a set approaches failure', H1))
s += bullets([
    '<b>Failure</b> (momentary failure) = you cannot complete the current rep despite trying (Steele 2017).',
    '<b>What limits the set is mostly in the muscle:</b> phosphate build-up and impaired calcium release (Allen 2008). '
    'Going to failure added peripheral but not central fatigue in a squat study of trained men.',
    '<b>Motor units</b> fire faster as fatigue builds but never get back to fresh firing rates (Martinez-Valdes 2020; '
    'isometric).',
    '<b>Perceived effort</b> tracks the brain’s own motor command (de Morree 2012) — you already have a built-in effort '
    'sensor. TENSR is competing with it.',
])
s.append(para('Which signals track proximity to failure?', H2))
s.append(grid([
 ['Signal', 'How it behaves rep by rep', 'Same value at failure?', 'Usefulness for TENSR'],
 ['Rep speed / rep duration', 'Slows from about rep 2–3, steeper near failure. % speed lost tracks % of reps done '
  'very closely on group averages (R² 0.93–0.97; Rodríguez-Rosell 2020).', 'No — last-rep speed varies too much '
  'between sessions for one person (CV &gt;18%; García-Ramos 2020, n = 96).', '<b>Best predictor</b>, once '
  'calibrated per person and exercise. Use the slow-down within the set, not a fixed threshold.'],
 ['Stall (failed rep)', 'The rep stops or reverses before the top.', 'Yes — it <i>is</i> failure.', '<b>Most solid</b> — '
  'a mechanical event the motion sensor can detect.'],
 ['EMG frequency (MDF)', 'Falls from rep 1 in a fairly straight line.', 'No — depends on load, studies disagree on '
  'direction.', 'Shows the set getting harder, but no warning bend near the end. Supporting signal.'],
 ['EMG amplitude', 'Rises, sometimes flattens near failure; at 80% in biceps it didn’t rise at all (Benitez 2023).',
  'No — lower after light-load sets in one study; similar across loads in another.', 'Weak. The “plateau 3–5 reps '
  'before failure” rule rests on one study (Sundstrup 2012).'],
 ['Range of motion', 'Shrinks in some lifters; skilled squatters kept full ROM to failure.', 'No', 'Part of the '
  'stall detector, not a predictor.'],
 ['Tremor / MMG, oxygen (NIRS), heart rate', 'Tremor peaks after exercise; oxygen bottoms out early; no heart-rate '
  'link to reps left.', 'No', 'Not useful as proximity markers.'],
], [W * 0.17, W * 0.33, W * 0.24, W * 0.26], shades=[(1, GOOD), (2, GOOD)]))
s.append(PageBreak())

# ---------------- Part 4 ----------------
s.append(para('Part 4 — What sensors have achieved so far', H1))
s.append(grid([
 ['Approach', 'Best honest result', 'Caveats'],
 ['Bar velocity, personal model (squat)', 'Fastest-rep speed predicted reps to failure within 1.96 reps (personal) vs '
  '2.81 (general) (Jukic 2023, 46 trained lifters).', 'The three Jukic papers are <b>one dataset</b> of 46 people, '
  'not three replications. “&lt;2 reps” in Jukic 2024 is a threshold, not a measured error.'],
 ['Bar velocity, Smith machine', '1.1–1.8 reps (Janicijevic 2024, wrestlers); 1.3 ± 0.7 reps (Qin 2025, bench).',
  'Personal fits looked better but weren’t more accurate in absolute error.'],
 ['Bar velocity, recreational lifters', 'Wrong reps-in-reserve on 69% of reps (Mansfield 2023, exact match).',
  'Velocity models overestimate reps left later in a session (Miras-Moreno 2023).'],
 ['Encoder on machines incl. knee extension', 'Reps-to-failure estimates within ±2 reps in &gt;90% of sets for '
  'lat pulldown and bench; knee extension worse (Külkamp 2024, 57 men, self-selected speed).', 'One study.'],
 ['Wrist motion sensor, “≤2 left” flag', 'F1 ≈ 0.82 (King 2025, 13 people, preacher curl).', 'Unknown split; every '
  'set went to failure; no baseline; not replicated.'],
 ['Motion + EMG, effort rating (RPE)', '41% exact, 86% within ±1 (Thomas &amp; Wahlström 2025, 5 men).',
  'Preprint; EMG may have been used only for labels; top feature was lowering time.'],
 ['EMG alone, dynamic lifting', 'No published result in reps. EMG explained ~half the variance of power loss on leg '
  'press (González-Izal 2010).', 'No study shows EMG beating a rep-timing baseline.'],
 ['Consumer devices (WHOOP, Apple, Garmin, Inara, Vitruve, Enode, RepOne, Metric)', 'No published validation of any '
  'effort, reps-left or failure feature.', 'WHOOP publishes repeatability only.'],
], [W * 0.24, W * 0.42, W * 0.34]))
s.append(para('The human benchmark', H2))
s += bullets([
    'Lifters underestimate reps left by ~0.95 on average, with ~1.45 reps spread between people (Halperin 2022). '
    'Corrected for that bias, a lifter is about 1.2 reps off near failure (our estimate).',
    'Your history is already a strong predictor: reps to failure at a fixed weight vary only 0.7–1.1 reps week to week '
    'in trained bench pressers (Mitter 2022, lab conditions).',
    '<b>Far from failure humans are much worse:</b> coaches 4.8 / 2.0 / 1.2 reps off at 33 / 66 / 90% through a set '
    '(Emanuel 2022); error grows with set length at 3–5 reps in reserve but not at 1 (Zourdos 2021).',
])

# ---------------- Part 5 ----------------
s.append(para('Part 5 — Rep speed beyond the barbell', H1))
s.append(grid([
 ['Exercise type', 'Puck clipped to bar / stack', 'Puck on the muscle', 'What TENSR can offer first'],
 ['Barbell, Smith, pull-ups', '~1–2 reps with personal calibration; ~2–3 general', 'Squat/lunge: slow-down from the '
  'thigh, unvalidated; bench: chest puck sees nothing', 'Hard / not hard grade; later a reps-left range'],
 ['Pin-loaded machines, cables', 'Est. 1.5–3 reps, per-machine calibration', 'Works where the worn limb moves (pulldown, '
  'raises); unvalidated', 'Hard / not hard grade'],
 ['Dumbbells', 'Unvalidated', 'Works where the worn limb moves; unvalidated', 'Stall flag + grade'],
 ['Isolation: curl, pushdown, leg extension, leg curl', 'Stack clip on machines', '<b>Blind</b> — the worn segment '
  'doesn’t move; EMG burst timing stands in (untested)', 'Stall flag; wide ranges until a second puck is added'],
], [W * 0.20, W * 0.25, W * 0.30, W * 0.25]))
s.append(para('Calibration means one or two sets taken to failure per exercise at working weights. Personal models have '
              'only been tested across 72 hours, so how often to recalibrate is a guess. A strict slow tempo breaks '
              'speed-based estimates; expect only a stall flag in the last 1–2 reps.', P))
s.append(PageBreak())

# ---------------- Part 6 ----------------
s.append(para('Part 6 — Where TENSR can beat your own guess', H1))
s.append(grid([
 ['Situation', 'How good humans are', 'TENSR’s chance'],
 ['Near failure on heavy compound lifts', 'Good — about 1 rep off, best at 1 rep in reserve', 'Low. Bar-speed methods '
  'only roughly match the lifter. Value is consistency and logging, not accuracy.'],
 ['Light weights, sets over ~12 reps', 'Poor — error grows with set length', '<b>Good.</b> The commonest mistake '
  '(stopping at 4–6 left thinking it’s 1–2) is a big margin and a binary call.'],
 ['Early in the set', 'Poor — 4.8 reps off at a third of the way (coaches on video)', 'Moderate — slow-down hasn’t '
  'started yet; history and calibration help.'],
 ['Isolation lifts', 'Self-report agreement weak on leg extension', 'Moderate with EMG timing or a stack clip; '
  'unvalidated.'],
], [W * 0.27, W * 0.33, W * 0.40], shades=[(2, GOOD)]))
s.append(para('Why combining your guess with the sensor may add little', H3))
s.append(para('If your bias-corrected guess is ~1.0 rep off and the sensor ~1.5, and their errors are correlated, combining '
              'them barely helps (1.0 → 0.98). It also needs you to tag every set, which conflicts with “no typing”. '
              'So the sensor must earn its place where humans are worst: light, long and isolation sets.', P))

# ---------------- Part 7 ----------------
s.append(para('Part 7 — The TENSR design', H1))
s.append(para('What you see after each set', H2))
s.append(grid([
 ['Readout', 'Meaning', 'Based on'],
 ['<b>Failure</b>', 'A rep stalled or reversed before the top — confirmed with one tap', 'Detected event'],
 ['<b>Hard</b>', '≤3 reps left — counts toward weekly hard sets', 'Estimate with confidence'],
 ['<b>Not hard</b>', '≥4 reps left — doesn’t count', 'Estimate with confidence'],
 ['<b>Unsure</b>', 'Estimate straddles the line, or poor signal', 'No guess shown'],
], [W * 0.15, W * 0.55, W * 0.30], shades=[(1, BAD), (2, GOOD), (3, MID), (4, RES)]))
s.append(para('No reps-left number is shown until validation passes for that exercise class. Nothing rates failure above '
              '1–3 reps short.', PS))
s.append(para('How the estimate works', H2))
s += bullets([
    '<b>Starting point:</b> your own history of weight vs reps achieved for that exercise (population priors can come '
    'from large training-log datasets — one has 303,494 near-failure sets across 388 exercises).',
    '<b>During the set:</b> it updates on how much each rep slows down compared with reps 1–3.',
    '<b>Signals, in order:</b> lifting-phase time, segment speed, lowering time, pauses between reps; then EMG frequency '
    'trend over 5+ reps, and EMG amplitude early in the set only. EMG stays only if it beats motion alone.',
    '<b>Static-segment exercises</b> (curl with upper-arm puck, pushdown, leg extension, chest work): EMG burst duration '
    'stands in for rep time — untested — until a second puck goes on the forearm, shin, bar or stack.',
])
s.append(para('How it learns you — without forced failure sessions', H2))
s += bullets([
    'It picks up natural failure sets <b>only when a failed rep is actually detected</b>. A set you stop and call '
    '“failure” must not teach it, or it learns your ~1-rep under-estimate instead of correcting it.',
    'Every set you stop short still tells it “at least this many reps”.',
    'Optional one-tap reps-in-reserve tag, entered before you see its estimate — it learns your personal bias.',
    'Optional “check set” every 4–6 weeks on safe exercises (machines, Smith with safeties, isolation): press the '
    'button at “2 left”, then continue to failure.',
    'Confidence widens over time without a new failure set, and after a PR.',
])
s.append(para('The live buzz — rules', H2))
s += bullets([
    'Only “you’ve reached your target zone”, never “keep going”.',
    'Only when the exercise is calibrated and validated, the signal is clean, the estimate is tight, at least 3 reps are '
    'done, and you opted in. Free-weight squat, bench and overhead press also need a “safeties/spotter set” switch.',
    '<b>Known risk:</b> once you rely on the buzz, a missing or late buzz reads as “keep going”. The auditor flagged this; '
    'the buzz stays off until validation shows it is reliably on time.',
])
s.append(para('Firmware and hardware', H2))
s.append(grid([
 ['Item', 'Value'],
 ['EMG', '2,000 samples/s; RLDREF_INT = 1; respiration off (per CLAUDE.md)'],
 ['Motion sensor', '416 samples/s'],
 ['Compute', 'Per-rep features well under 1 ms; a 1024-point FFT ≈ 0.4 ms on the ESP32-S3'],
 ['Latency', '~0.2–0.4 s from end of rep to buzz; estimate runs on the puck so Bluetooth dropouts can’t delay it'],
 ['Bluetooth', '~40 bytes per rep normally; raw streaming (~11 kB/s) only for validation builds'],
 ['Haptic motor', 'Blank EMG <i>and</i> motion data until the buzz has settled — interference must be measured on the bench'],
 ['Board changes', '<b>None needed.</b> A second puck (bar/stack/limb clip) improves coverage.'],
], [W * 0.22, W * 0.78]))
s.append(PageBreak())

# ---------------- Part 8 ----------------
s.append(para('Part 8 — How to prove it works', H1))
s.append(grid([
 ['Stage', 'What', 'Pass if (proposed engineering targets)'],
 ['A Bench', 'Playback signals, haptic interference, latency, Bluetooth', 'Buzz artefact suppressed; latency within spec'],
 ['B Pilot (8–12 lifters)', 'Rep counting and stall detection vs video', 'Measured counts; stall detection reported per exercise (no published precedent exists)'],
 ['C Lab (~30–40 trained lifters)', 'Two visits, every labelled set continued to true failure, tested on people the model never saw, band re-fitted', 'Hard vs not-hard call beats your bias-corrected guess; sensor adds ≥0.3 reps over history alone; EMG adds ≥0.2 reps over motion alone or is dropped; 80% ranges contain the truth 75–85% of the time'],
 ['D Gym field study', 'Real training, real logs', 'Withheld-set rate, agreement with the lifter'],
 ['E Crossover', 'Does feedback make people stop where they intended?', 'No unsafe overshoot before any further claim'],
], [W * 0.20, W * 0.40, W * 0.40]))
s.append(para('<b>Mandatory comparisons:</b> rep count plus your own history with no sensor; motion-only; your raw '
              'guess; your bias-corrected guess; a lab bar-speed reference. Comparisons happen at matched rep numbers '
              'so set length can’t give the answer away.', P))
s.append(para('<b>If the sensor can’t beat your history:</b> the product is still automatic failure detection, honest '
              'hard-set counting and bias-corrected tags — useful, but the marketing must not say “more accurate than you”.', P))

# ---------------- Part 9 ----------------
s.append(para('Part 9 — What TENSR can claim, stage by stage', H1))
s.append(grid([
 ['Stage', 'Can claim', 'Cannot claim'],
 ['Now (not built)', '“Designed to count reps, flag sets you take to failure and track hard sets per muscle.” '
  '“Built on the published science of effort and velocity loss.”', 'Any accuracy. “Knows how many reps you have left.” '
  '“Detects failure before it happens.” “Tempo-independent.” “90 Hz = cooked.”'],
 ['After bench', 'Engineering facts: latency, battery, Bluetooth', 'Anything about people'],
 ['After pilot', 'Measured counts on named exercises, labelled exploratory', 'Reps-left accuracy; comparisons with lifters'],
 ['After lab', 'Per exercise class: “calls hard vs not-hard sets correctly X% of the time”; “more accurate than your '
  'own guess” only where that test passed', 'Claims for exercise classes that failed'],
 ['After field + crossover', '“Works in a real gym”; “helps lifters finish sets closer to their target” with effect size',
  'Growth outcomes without a trial; injury, rehab or clinical language — ever'],
], [W * 0.17, W * 0.45, W * 0.38]))
s.append(para('<b>True today and worth saying:</b> it logs without typing, timestamps every rep, and counts hard sets '
              'the same way every time. Consistency and automatic logging are real value — just not accuracy.', P))

# ---------------- Part 10 ----------------
s.append(para('Part 10 — Fact-check log', H1))
s.append(grid([
 ['Item', 'Finding'],
 ['Jukic 2023 ×2 and 2024', 'One dataset (46 lifters, back squat), analysed three ways — not three replications'],
 ['Light-load “1 rep in reserve” rule', 'Not supported at that precision; Lasevicius 2022’s non-failure groups stopped '
  '~15 and ~5–6 reps short'],
 ['“Every velocity study used maximal speed”', 'Wrong — Külkamp 2024 used self-selected speed (ICC 0.88), and included knee extension'],
 ['Armes 2020', 'Published (Front Psychol); one exercise; very wide uncertainty'],
 ['Refalo bench self-report 0.65 ± 0.78 reps', 'Still from one secondary source — unverified'],
 ['Thomas &amp; Wahlström 2025', 'n = 5 confirmed; EMG possibly used only for labels'],
 ['King 2025', 'F1 0.82 for the near-failure flag; data split unknown'],
 ['Day-to-day variability 0.7–1.1 reps', 'Real (Mitter 2022, 24 trained, bench, lab) — a floor, not gym variability'],
 ['Looney 2016', 'Was a drop set; a 2023 companion paper found final-rep EMG similar at 30% and 80%'],
 ['“Minimum velocity 0.17 m/s bench / 0.3 squat”', 'Not found in any reachable source — don’t quote'],
 ['Design maths (fusion, FFT, Bluetooth, sample rates)', 'Recomputed and correct'],
], [W * 0.32, W * 0.68]))
s.append(Spacer(1, 6))
s.append(para('This round recorded <b>%d unique studies</b>; <b>%d</b> were re-checked by the auditor. Every study was '
              'checked from abstracts or summaries. Allowing pmc.ncbi.nlm.nih.gov, arxiv.org and doi.org in the '
              'environment’s network settings would let agents read the two most product-relevant papers in full '
              '(King 2025, Thomas &amp; Wahlström 2025).' % (n_all, n_aud), P))

# ---------------- Part 11 ----------------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 24 * mm
s.append(para('Part 11 — Every study recorded (%d)' % n_all, H1))
s.append(para('Grouped by research area. <b>Checked</b> is the auditor’s verdict where re-checked. Full detail in '
              'FAILURE-STUDIES.csv.', PS))
groups = [('X1', 'Physiology of approaching failure'), ('X2', 'What sensors have achieved'),
          ('X3', 'Rep speed beyond the barbell'), ('X4', 'Design evidence'), ('XA', 'Added by the auditor')]
cw = [LW * x for x in (0.22, 0.14, 0.14, 0.26, 0.16, 0.08)]
for code, title in groups:
    g = [r for r in studies if r['found_by'].split(';')[0] == code]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [[Paragraph(x, TB) for x in ['Study', 'Design · who', 'Exercise · sensor', 'Result · error', 'Limits', 'Checked']]]
    for r in g:
        cit = '<b>%s</b><br/>%s' % (esc(r['key']), esc(r['citation']))
        if r['doi_or_link']: cit += '<br/><font color="#5a6370">%s</font>' % esc(r['doi_or_link'][:100])
        data.append([Paragraph(cit, T),
                     Paragraph('%s<br/>n = %s<br/>%s' % (esc(r['design']), esc(r['n']), esc(r['trained_status'])), T),
                     Paragraph('%s<br/>%s' % (esc(r['exercise']), esc(r['sensor_or_method'])), T),
                     Paragraph(esc(r['result_error_uncertainty']), T),
                     Paragraph(esc(r['limitations']) + '<br/><font color="#5a6370">Access: %s</font>' % esc(r['access']), T),
                     Paragraph(esc(r['audit_verdict'][:140]), T)])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('BACKGROUND', (0, 0), (-1, 0), BAND), ('LEFTPADDING', (0, 0), (-1, -1), 3),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 3), ('TOPPADDING', (0, 0), (-1, -1), 2),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                           ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafbfc')])]))
    s.append(t)

doc.build(s)
print('ok', OUT, n_all, n_aud)
