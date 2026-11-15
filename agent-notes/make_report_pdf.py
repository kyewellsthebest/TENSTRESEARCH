import csv, html, sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, NextPageTemplate, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

D = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', D + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', D + 'DejaVuSans-Bold.ttf'))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('DV', normal='DV', bold='DVB', italic='DV', boldItalic='DVB')

R = '/home/user/tenstresearch/'
OUT = R + 'TENSR-RESEARCH-REPORT.pdf'

INK = colors.HexColor('#1b1f24'); MUTED = colors.HexColor('#5a6370'); ACC = colors.HexColor('#0b6e6e')
LINE = colors.HexColor('#d6dbe1'); BAND = colors.HexColor('#f2f5f7')
GOOD = colors.HexColor('#dff2e4'); MID = colors.HexColor('#fdf3d6'); RES = colors.HexColor('#e6ecf7'); BAD = colors.HexColor('#f9e0e0')

st = lambda n, **k: ParagraphStyle(n, fontName=k.pop('f', 'DV'), textColor=k.pop('c', INK), **k)
H0 = st('h0', f='DVB', fontSize=26, leading=31, c=INK, spaceAfter=6)
SUB = st('sub', fontSize=12, leading=16, c=MUTED, spaceAfter=4)
H1 = st('h1', f='DVB', fontSize=17, leading=21, c=ACC, spaceBefore=4, spaceAfter=8)
H2 = st('h2', f='DVB', fontSize=12.5, leading=16, spaceBefore=10, spaceAfter=4)
P = st('p', fontSize=9.6, leading=13.6, spaceAfter=5)
PS = st('ps', fontSize=8.6, leading=11.6, spaceAfter=3, c=MUTED)
B = st('b', fontSize=9.6, leading=13.4, leftIndent=12, bulletIndent=2, spaceAfter=2)
C = st('c', fontSize=8.4, leading=10.8)
CB = st('cb', f='DVB', fontSize=8.4, leading=10.8)
T = st('t', fontSize=6.9, leading=8.6)
TB = st('tb', f='DVB', fontSize=7.0, leading=8.8)
CALL = st('call', fontSize=10, leading=14, c=INK)

def esc(s): return html.escape(s or '', quote=False)
def para(t, s=P): return Paragraph(t, s)
def bullets(items, s=B): return [Paragraph(i, s, bulletText='•') for i in items]

def box(flow, bg=BAND, pad=8):
    t = Table([[flow]], colWidths=[None])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), bg), ('BOX', (0, 0), (-1, -1), 0.5, LINE),
                           ('LEFTPADDING', (0, 0), (-1, -1), pad), ('RIGHTPADDING', (0, 0), (-1, -1), pad),
                           ('TOPPADDING', (0, 0), (-1, -1), pad), ('BOTTOMPADDING', (0, 0), (-1, -1), pad)]))
    return t

def grid(rows, widths, head=True, style=C, hstyle=CB, shades=None):
    data = [[c if not isinstance(c, str) else Paragraph(c, hstyle if (head and i == 0) else style) for c in r]
            for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    ts = [('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
          ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    if head: ts.append(('BACKGROUND', (0, 0), (-1, 0), BAND))
    for (r, col) in (shades or []): ts.append(('BACKGROUND', (0, r), (-1, r), col))
    t.setStyle(TableStyle(ts)); return t

# ---------- page templates ----------
def deco(canv, doc):
    canv.saveState(); canv.setFont('DV', 7.5); canv.setFillColor(MUTED)
    w, h = canv._pagesize
    canv.drawString(15 * mm, 9 * mm, 'TENSR research report · 2 Nov 2026 · research only — not product claims')
    canv.drawRightString(w - 15 * mm, 9 * mm, str(doc.page)); canv.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='TENSR Research Report', author='TENSR research team (Claude Code)',
                      subject='Training science, studies found, and what TENSR can measure',
                      leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=16 * mm)
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm, id='p')], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(12 * mm, 14 * mm, lw - 24 * mm, lh - 26 * mm, id='l')], onPage=deco,
                 pagesize=landscape(A4)),
])
W = pw - 36 * mm
s = []

# ---------- cover ----------
s += [Spacer(1, 40 * mm), para('TENSR', st('k', f='DVB', fontSize=11, c=ACC, leading=14)),
      para('What the science says, and what our band can actually do', H0),
      para('A plain-English breakdown of every study we found, the training approach the evidence supports, '
           'and how each part of it maps onto TENSR’s sensor.', SUB), Spacer(1, 8 * mm)]
s.append(box(para(
    '<b>How to read this report</b><br/>'
    '<b>Part 1</b> — the answer in one page.<br/>'
    '<b>Part 2</b> — the training approach the research supports, topic by topic.<br/>'
    '<b>Part 3</b> — what TENSR’s sensor can and cannot see.<br/>'
    '<b>Part 4</b> — how the training science turns into TENSR features: build, test, or avoid.<br/>'
    '<b>Part 5</b> — hardware problems the research found.<br/>'
    '<b>Part 6</b> — how to prove it works.<br/>'
    '<b>Part 7</b> — all 169 studies, grouped by area, with what each found and why it matters to TENSR.', CALL)))
s += [Spacer(1, 8 * mm), box(para(
    '<b>Honest limits.</b> Six research agents searched the literature on 2 Nov 2026 and an independent auditor '
    're-checked the important citations. This computer could not open full papers — only search summaries of '
    'abstracts and records — so every study here was checked at abstract level, not read in full. No citation was '
    'found to be made up, but the key ones should be re-read in full before anything goes on a website, in a pitch '
    'or into marketing. TENSR has not been built yet, so nothing in this report was measured on a real band.', PS),
    bg=colors.HexColor('#fff8e8'))]
s.append(PageBreak())

# ---------- Part 1 ----------
s.append(para('Part 1 — The answer in one page', H1))
s.append(para('<b>What the research says about building muscle and strength</b>', H2))
s += bullets([
    '<b>Effort matters more than almost anything else.</b> Sets need to end close to failure — roughly 0–3 reps '
    'short. Going all the way to failure adds little or nothing for most people, except with light weights.',
    '<b>Weight barely matters for growth.</b> Light (~30% of max) and heavy (~80%+) loads build similar muscle '
    'if the sets are hard. Heavy loads build more <i>strength</i>.',
    '<b>Volume is the best “dose” number.</b> More hard sets per muscle per week builds more muscle, with '
    'diminishing returns. There is no single perfect number.',
    '<b>Stretch helps.</b> Training a muscle at long lengths (deep in the stretch) looks at least as good as, '
    'and sometimes better than, full range. Short half-reps at the top look worse.',
    '<b>Tempo and “time under tension” don’t matter</b> anywhere between about 0.5 and 8 seconds per rep.',
    '<b>Rest at least 60–90 seconds.</b> Beyond ~90 s adds little for growth; 2–3 min helps heavy strength work.',
    '<b>Fatigue is a side effect, not the goal.</b> Drop sets, supersets, cluster sets and failure all change '
    'how tired you get without changing how much you grow.',
])
s.append(para('<b>What that means for TENSR</b>', H2))
s += bullets([
    '<b>There is no “optimal” fatigue level, time under tension or contraction score</b> in the research. '
    'Any score built around one would be invented.',
    '<b>More muscle signal (EMG) does not mean more growth.</b> In the one direct test, hip thrusts produced more '
    'glute EMG than squats but no more glute growth. So an “activation %” or “stimulus score” is not just unproven '
    '— the evidence points against it.',
    '<b>The fatigue signal TENSR is built around is real</b> — the EMG frequency drops ~20–30% over a hard set — '
    'but it is too noisy rep-by-rep to say “2 reps left” live. It can describe a set <i>after</i> it ends.',
    '<b>Strongest features to build first:</b> automatic rep and set counting, a weekly hard-set count for the '
    'muscle, and a rest timer with evidence-based defaults.',
    '<b>Fix first:</b> run the chip at 2,000 samples/second (not 500), and work out which way the electrodes point '
    'relative to the muscle fibres.',
])
s.append(Spacer(1, 4))
s.append(grid([
    ['Build now', 'Build after real testing', 'Research only', 'Don’t build'],
    ['Rep & set counting<br/>Set duration<br/>Rest timer (elapsed)<br/>Weekly set count',
     'After-set fatigue trend<br/>Lifting vs lowering timing (some exercises)',
     'Live “reps left”<br/>“Reached failure” score<br/>“Muscle recovered” timer<br/>Left/right (needs 2 bands)<br/>Signal-strength trend',
     'Activation %<br/>Contraction-quality score<br/>Hypertrophy / stimulus score<br/>“Time under tension” score'],
], [W / 4] * 4, shades=[]))
s.append(PageBreak())

# ---------- Part 2 ----------
s.append(para('Part 2 — The training approach the research supports', H1))
s.append(para('This is the “best training style” in the only sense the evidence allows: the set of choices that '
              'consistently work, with how sure we are about each. None of these is a single magic number — every '
              'one is a range, and people vary a lot.', P))
s.append(Spacer(1, 4))

conf = {'Strong': GOOD, 'Moderate': MID, 'Limited': RES, 'Very limited': BAD, 'None': BAD}
topics = [
 ('How hard each set is (proximity to failure)', 'Moderate',
  'Growth improves the closer sets end to failure, but most of the benefit is captured 0–3 reps short. Going to '
  'true failure adds little or nothing for trained lifters and costs extra fatigue. Light loads need to go closer '
  'to failure than heavy ones. Strength barely cares.',
  'Refalo 2023 & 2024; Grgic 2022; Robinson 2024; Lasevicius 2022',
  'Stop most sets about 1–3 reps short. With light weights, go closer.',
  'This is the most valuable thing TENSR could help with — and the hardest. Lifters already guess “reps left” to '
  'within about 1–1.5 reps. TENSR would have to do better than that, which no EMG device has shown.'),
 ('Weight (load) and rep range', 'Strong',
  'Similar muscle growth from roughly 30% to 80%+ of your max, as long as sets are hard. Heavier is better for '
  'max strength.',
  'Schoenfeld 2017a; Lopez 2021 (28 studies); Morton 2016',
  'Pick any rep range from ~5 to ~30 you can push hard; go heavier for strength.',
  'TENSR doesn’t know the weight. Heavy weights make bigger EMG signals but not more growth — so signal size can’t '
  'be a “stimulus” score.'),
 ('Volume (hard sets per week)', 'Moderate',
  'More weekly sets per muscle builds more muscle, with diminishing returns. Strength plateaus sooner. Sets on '
  'compound lifts count partly toward the helper muscles.',
  'Schoenfeld 2017b; Pelland 2026 (dose–response meta-regression)',
  'Track hard sets per muscle per week; add sets gradually; no universal ceiling.',
  'A natural fit: TENSR can count sets for the muscle it’s on. Whether a set was “hard” should come from the user, '
  'not a TENSR guess.'),
 ('Training at long muscle lengths (stretch)', 'Limited',
  'Training deep in the stretch (e.g. overhead triceps, seated leg curl, bottom-half calf raises) gave more growth '
  'in several studies, mostly in beginners over 8–12 weeks. In trained lifters one study found no difference.',
  'Maeo 2021, 2023; Pedrosa 2022; Kassiano 2023; Wolf 2023, 2025',
  'Favour exercises and ranges that load the muscle when stretched.',
  'Hard for TENSR: one sensor sees one limb segment, not the joint angle or the position of the other joint '
  '(e.g. arm overhead vs at the side).'),
 ('Full range vs partial reps', 'Moderate',
  'Short partials at the top (shortened position) look worse. Partials at the bottom (lengthened) look about as '
  'good as full range. Full range is better for strength through the whole movement.',
  'Pallarés 2021; Wolf 2023; Kassiano 2023',
  'Use full range, or bottom-half partials; avoid top-half-only reps.',
  'TENSR could notice range of motion shrinking during a set on some exercises — a possible future feature.'),
 ('Tempo and time under tension', 'Moderate',
  'Anything from about 0.5 to 8 seconds per rep gives similar growth. Only very slow reps (10 s+) look worse.',
  'Schoenfeld 2015 (8 studies); Lacerda 2021',
  'Lift with control at whatever tempo lets you train hard. No target tempo.',
  'TENSR can time reps, but there is nothing to score them against. Show “set duration”, not “time under tension”.'),
 ('Lifting vs lowering (concentric / eccentric / isometric)', 'Moderate',
  'All three build muscle. Lowering-only training was slightly ahead but not significantly.',
  'Schoenfeld 2017c; Oranchuk 2019',
  'Don’t rush the lowering, but no special emphasis needed.',
  'TENSR can split lifting vs lowering only on exercises where its limb segment moves.'),
 ('Pauses and squeezing at the top', 'None',
  'No long-term studies found. One small trial of flexing between sets.',
  'Schoenfeld 2020 (flexing, small)',
  'Optional. No evidence it adds growth.',
  'Risk: squeezing makes the EMG signal go up, so an EMG score would reward it with no evidence it helps.'),
 ('Strict form vs cheating / momentum', 'Very limited',
  'One study: cheat reps moved more weight and grew muscle about the same as strict reps. No study of “heavy '
  'cheat then strict” sequences.',
  'Augustin 2025 (one trial, beginners)',
  'Control reps mainly for safety and consistency.',
  'TENSR might detect momentum, but a “form score” has no growth evidence behind it.'),
 ('Compound vs isolation; machines vs free weights', 'Moderate',
  'Machines and free weights grow muscle about equally. Adding isolation on top of compounds didn’t add arm '
  'growth in beginners. Different exercises grow different parts of a muscle.',
  'Haugen 2023; Gentil 2013; Plotkin 2023',
  'Choose exercises you can load hard and safely; mix to hit all regions.',
  'TENSR sees one region of one muscle; it can’t judge exercise choice.'),
 ('Frequency', 'Moderate',
  'With the same weekly volume, training a muscle more often doesn’t add growth; it can help strength.',
  'Schoenfeld 2019; Pelland 2026',
  'Split weekly sets however suits your schedule.',
  'Logging only.'),
 ('Rest between sets', 'Limited',
  'Over 60–90 s helps; beyond ~90 s adds little for growth. 3 min beat 1 min for strength in trained men.',
  'Singer 2024; Schoenfeld 2016',
  'Rest at least 90 s; 2–3 min for heavy compound lifts.',
  'An elapsed-time timer with these defaults is solid. A “your muscle has recovered” timer is unproven — muscle '
  'signal and strength recover on different schedules (Mills 1982).'),
 ('Drop sets, supersets, rest-pause, cluster sets', 'Moderate',
  'These save time or change fatigue but give about the same growth as normal sets.',
  'Zhang 2025; Coleman 2022; Sødal 2023; Davies 2021',
  'Use them to save time, not to grow more.',
  'TENSR could detect a drop set, but a fatigue score rising in one isn’t evidence of more growth.'),
 ('Does more fatigue or “burn” mean more growth?', 'Moderate',
  'No. When studies changed fatigue but kept effort the same, growth didn’t change. One study found more '
  'within-set fatigue gave a bit more growth but hurt jump performance and needed 40% more reps.',
  'Davies 2021; Zhang 2025; Refalo 2024; Pareja-Blanco 2017',
  'Chase hard sets, not maximum fatigue.',
  'Central to TENSR: a fatigue number is not a growth number, and shouldn’t be presented as a target.'),
 ('Does more EMG signal mean more growth?', 'Moderate',
  'No. The only study measuring both found more glute EMG in hip thrusts but equal glute growth to squats. Heavy '
  'loads give more EMG but not more growth.',
  'Plotkin 2023; Vigotsky 2018, 2022; Morton 2019',
  '—',
  'Rules out “activation %”, “stimulus” and “set effectiveness” scores.'),
]
for (name, c, finding, studies, do, tensr) in topics:
    head = Table([[Paragraph('<b>%s</b>' % name, st('x', f='DVB', fontSize=10.5, leading=13)),
                   Paragraph('Confidence: <b>%s</b>' % c, st('y', fontSize=8.4, leading=11, alignment=2))]],
                 colWidths=[W * 0.72, W * 0.28])
    head.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), conf[c]), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                              ('LEFTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 4),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    body = grid([['What the studies show', finding], ['Key studies', studies], ['In practice', do],
                 ['What it means for TENSR', tensr]], [W * 0.22, W * 0.78], head=False)
    s.append(KeepTogether([head, body, Spacer(1, 7)]))

s.append(para('<b>Putting it together — the evidence-based default</b>', H2))
s.append(box(para(
    'Hard sets ending about 1–3 reps short of failure (closer with light weights) · any rep range you can push hard '
    '(heavier for strength) · weekly hard sets per muscle tracked and built up gradually · exercises that load the '
    'muscle in a stretched position · controlled reps at any normal tempo · at least 90 s rest (2–3 min for heavy '
    'compounds) · fatigue techniques for saving time, not for extra growth. <br/><br/>'
    '<i>This is a starting point, not an optimum. People respond very differently, and most studies used beginners '
    'for 8–14 weeks.</i>', CALL), bg=GOOD))
s.append(PageBreak())

# ---------- Part 3 ----------
s.append(para('Part 3 — What TENSR’s sensor can and can’t see', H1))
s.append(para('TENSR (as designed in this repo) has <b>one EMG channel</b> — two dry 7 mm metal studs 25.4 mm apart '
              'plus a third reference stud — and a <b>motion sensor</b> on the puck. It has no weight input, no '
              'force sensor and no bar sensor. It has not been built yet.', P))
rows = [['Thing people care about', 'What TENSR records', 'What it can tell you', 'Verdict']]
meas = [
 ('Muscle electrical activity', 'EMG voltage from one spot on one muscle', 'When the muscle fires; how the signal changes within a set', 'Measured (quality unknown until built)', GOOD),
 ('Reps, sets, tempo', 'EMG bursts + limb motion', 'Rep count, rep and set duration, rest time', 'Measurable — needs testing', GOOD),
 ('Local muscle fatigue', 'EMG frequency and size per rep', 'A trend within a set, for one person, exercise and weight', 'After real testing; after-set only', MID),
 ('Reps left before failure', 'Nothing direct', 'Possibly a personal estimate — never shown to work', 'Research only', RES),
 ('Speed of the bar', 'Limb rotation speed (not the bar)', 'Slowing down on some exercises', 'After real testing, some exercises', MID),
 ('Recovery between sets', 'Time since last rep', 'Elapsed rest time', 'Timer yes; “recovered” no', MID),
 ('Force or muscle tension', 'Nothing', '—', 'Can’t measure', BAD),
 ('Time under tension', 'Duration only', '“Set duration”', 'Tension can’t be measured', BAD),
 ('Muscle length / stretch', 'One limb segment’s angle', 'Rough range on some exercises', 'Can’t measure properly', BAD),
 ('Whole-body fatigue', 'Nothing', '—', 'Can’t measure', BAD),
 ('Muscle growth', 'Nothing', 'Only how many sets you did', 'Can’t measure', BAD),
]
sh = []
for i, (a, b, c, d, col) in enumerate(meas, 1):
    rows.append([a, b, c, d]); sh.append((i, col))
s.append(grid(rows, [W * 0.22, W * 0.26, W * 0.30, W * 0.22], shades=sh))
s.append(Spacer(1, 8))
s.append(para('Why EMG signal size can’t stand in for force or growth', H2))
s += bullets([
    'It goes <b>up</b> as you tire even when the weight stays the same.',
    'It also goes up with heavier weight, faster reps and more effort — so a rise could mean any of those.',
    'It flattens out 3–5 reps before failure.',
    'It varies about <b>40%</b> between days even on lab equipment (Colyer 2018), and with body fat, sweat and '
    'exactly where the band sits.',
    'Bigger signal didn’t mean more growth when tested (Plotkin 2023).',
])
s.append(PageBreak())

# ---------- Part 4 ----------
s.append(para('Part 4 — How the training science turns into TENSR features', H1))
s.append(para('Every feature idea was put through the same questions by an independent auditor: Does it measure what it '
              'claims? Has it been shown to work in real lifting? Could band movement or technique fake the result? '
              'Is there a real threshold behind it? Can the user act on it? Could it push people into unnecessary '
              'fatigue or bad habits?', P))
feat = list(csv.DictReader(open(R + 'TENSR-FEATURE-EVIDENCE-MATRIX.csv')))
colmap = {'Suitable': GOOD, 'Potentially': MID, 'Research': RES, 'Unsupported': BAD}
for f in feat:
    col = next((v for k, v in colmap.items() if f['Recommendation'].startswith(k)), BAND)
    head = Table([[Paragraph('<b>%s</b>' % esc(f['Feature']), st('x2', f='DVB', fontSize=10, leading=12.5)),
                   Paragraph(esc(f['Recommendation']), st('y2', fontSize=7.8, leading=10))]],
                 colWidths=[W * 0.45, W * 0.55])
    head.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), col), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                              ('LEFTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 4),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    body = grid([['Why a user would want it', esc(f['User benefit'])],
                 ['What TENSR actually measures', esc(f['What is actually measured'])],
                 ['Evidence', esc(f['Evidence strength'])],
                 ['Does the hardware fit?', esc(f['Hardware fit'])],
                 ['Main limits', esc(f['Expected limitations'])],
                 ['Testing needed', esc(f['Validation required'])]],
                [W * 0.22, W * 0.78], head=False, style=st('cs', fontSize=7.8, leading=10))
    s.append(KeepTogether([head, body, Spacer(1, 7)]))
s.append(para('Claims to avoid in marketing', H2))
s += bullets([
    '“Optimal” fatigue, tempo or time under tension; any contraction rating or percentage score; “activation %”.',
    'Hypertrophy, stimulus or set-effectiveness scores.',
    'Live “about 2 reps left”; “your muscle has recovered” / “ready”; “did you reach failure” as a score.',
    '“120 Hz → 90 Hz”, “tempo-independent”, “beats velocity-based training”.',
    'Left/right imbalance from one band; “logs your whole split automatically”.',
    'Anything about injury, rehab, diagnosis or health readiness — this would break the TGA wellness exemption.',
])
s.append(PageBreak())

# ---------- Part 5 ----------
s.append(para('Part 5 — Hardware problems the research found', H1))
hw = [['Issue', 'What we found', 'What to do'],
 ['Sample rate', 'Bring-up plans 500 samples/s. The ADS1292R’s own digital filter is already 3 dB down at 131 Hz '
  'at that rate, and nothing above 250 Hz exists. A real 25% fatigue drop reads as ~16%. Confirmed against the TI '
  'datasheet. The existing design review only checked the analogue filter.',
  'Run at <b>2,000 samples/s</b> (DR = 100). Free in hardware. Decide it on the bench (Part 6, stage 1).'],
 ['Electrode direction', 'The two sensing studs sit along the puck’s long (44 mm) axis. Nothing records how the '
  'puck sits on the band. If that axis wraps around the arm or leg, the studs run <b>across</b> the muscle fibres '
  'instead of along them.', 'Decide and record the orientation; test both ways against lab EMG before naming any muscle.'],
 ['Electrode spacing', '25.4 mm apart vs the 20 mm standard (SENIAM). More pickup from neighbouring muscles, worst '
  'on small muscles (delts, calves). It shifts absolute frequencies but barely changes the relative fatigue trend.',
  'Accept for v1; test per muscle; reconsider for v2.'],
 ['Dry electrodes', 'No dry or wearable EMG system has validated the fatigue (frequency) measure. Sweat changes '
  'contact over minutes, which looks like a fatigue trend in signal size.',
  'Consider snap-on gel electrodes for testing; add a signal-quality check that shows “no reading” instead of guessing.'],
 ['Reference stud', 'Sits on the working muscle, but at equal distance from both sensing studs, so it barely '
  'contaminates the signal. The real risk is it lifting off the skin.', 'Lead-off detection on all three studs.'],
 ['Motion sensor', 'Measures the limb the band is on, not the bar or a joint angle. On curls or leg extensions '
  'that limb barely moves — untested whether rep counting still works there.', 'Test per exercise.']]
s.append(grid(hw, [W * 0.17, W * 0.50, W * 0.33]))
s.append(PageBreak())

# ---------- Part 6 ----------
s.append(para('Part 6 — How to prove it works', H1))
s.append(para('Five stages. Each one has to pass before the next is worth running. Numbers marked as targets are our '
              'proposals, not published thresholds. Full detail: TENSR-VALIDATION-PLAN.md.', P))
vs = [['Stage', 'Question', 'How', 'Pass if'],
 ['1. Bench', 'Does the board give the right answer from a known fake signal?',
  'Signal generator plays fake EMG with known frequency through the board at 500 and 2,000 samples/s; fault '
  'injection; electrical-safety check before anyone wears it.', 'Fatigue slope recovered within 10%; faults trigger “no reading”; currents within medical-device limits.'],
 ['2. Repeatability', 'Same person, nothing changed — do you get the same number?',
  'Repeat sets in one session, after taking the band off and on, and on different days.',
  'The within-set fatigue slope is reproducible after re-fitting the band.'],
 ['3. Agreement', 'Does TENSR agree with lab equipment during real lifts?',
  'Lab gel EMG right next to TENSR; bar-speed sensor; video; both electrode orientations; several muscles and exercises.',
  'Disagrees with lab EMG no more than two lab sensors disagree with each other. Muscles that fail are dropped.'],
 ['4. Prediction', 'Can it tell how close you are to failure?',
  'Every set continued to true failure; models tested on people they never saw.',
  'Beats the lifter’s own (bias-corrected) guess <b>and</b> a motion-sensor-only model.'],
 ['5. Benefit', 'Does feedback actually help people train better?',
  'Short crossover first (does it make people stop where they meant to?), then a 8–12 week trial.',
  'No over-reaching; then measurable gains beyond what normal training gives.']]
s.append(grid(vs, [W * 0.13, W * 0.24, W * 0.36, W * 0.27]))
s.append(Spacer(1, 6))
s.append(para('<b>Why the “20–30 sets” test in the brief isn’t enough:</b> failure sets have more reps by '
              'definition, so rep count alone separates them; one person’s sets say nothing about other users; and '
              '27/30 correct still means somewhere between 74% and 97%. It’s a good first pilot, not proof.', P))
s.append(para('<b>Before testing on people:</b> ethics (HREC) approval, informed consent, health screening, spotters '
              'on failure sets, nickel-allergy check for the metal studs, electrical-safety check, and privacy '
              'rules for body data. Someone other than the product owner should analyse the final test set.', P))

# ---------- Part 7: studies ----------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 24 * mm
s.append(para('Part 7 — Every study we found (169)', H1))
s.append(para(
    'Grouped by research area. <b>Type</b>: D = direct (similar hardware, real lifting) · I = human but indirect · '
    'M = mechanism / theory · H = untested product idea. <b>Checked</b>: the auditor’s verdict — V verified, '
    'P partly verified, U unverifiable, W wrong / misapplied; “not sampled” means the auditor didn’t re-check it. '
    '<b>Access</b>: how much of the paper could be seen — none were read in full. Full detail (including '
    'limitations and conflicts of interest) is in STUDY-EVIDENCE-TABLE.csv.', PS))
groups = [('A1', 'Training outcomes — what builds muscle and strength'),
          ('A2', 'Surface EMG and muscle fatigue'),
          ('A3', 'Sensors, signal processing and machine learning'),
          ('A4', 'Products, competitors and regulation'),
          ('A5', 'Validation and statistics methods'),
          ('A6', 'Added by the independent auditor')]
rows = list(csv.DictReader(open(R + 'STUDY-EVIDENCE-TABLE.csv')))
def short_verdict(v):
    v = (v or '').strip()
    if not v or v.startswith('not in'): return 'not sampled'
    return v
cw = [LW * x for x in (0.24, 0.13, 0.30, 0.22, 0.04, 0.07)]
for code, title in groups:
    g = [r for r in rows if r['found_by'].split(';')[0].strip() == code]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [['Study', 'Design · who', 'What it found', 'Why it matters for TENSR', 'Type', 'Checked']]
    for r in g:
        cit = '<b>%s</b><br/>%s' % (esc(r['key']), esc(r['citation']))
        if r['doi_or_link']: cit += '<br/><font color="#5a6370">%s</font>' % esc(r['doi_or_link'][:110])
        des = '%s<br/>n = %s<br/>%s' % (esc(r['design']), esc(r['n']), esc(r['participants']))
        acc = esc(r['access'])
        data.append([Paragraph(cit, T), Paragraph(des, T),
                     Paragraph(esc(r['results_effects_uncertainty']), T),
                     Paragraph(esc(r['tentsr_applicability']) + '<br/><font color="#5a6370">Access: %s</font>' % acc, T),
                     Paragraph(esc(r['evidence_code']), T), Paragraph(esc(short_verdict(r['audit_verdict'])), T)])
    data[0] = [Paragraph(c, TB) for c in data[0]]
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('BACKGROUND', (0, 0), (-1, 0), BAND), ('LEFTPADDING', (0, 0), (-1, -1), 3),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 3), ('TOPPADDING', (0, 0), (-1, -1), 2),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                           ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafbfc')])]))
    s.append(t)

doc.build(s)
print('ok', OUT)
