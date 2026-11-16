"""Builds knowledge-base/digests/2026-11-16-digest.pdf (exercise selection). Adapted from make_digest_2026-11-15.py."""
import csv, html, os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, NextPageTemplate)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

D = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', D + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', D + 'DejaVuSans-Bold.ttf'))
registerFontFamily('DV', normal='DV', bold='DVB', italic='DV', boldItalic='DVB')

KB = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
DATE = '2026-11-16'
OUT = KB + 'digests/%s-digest.pdf' % DATE
INK = colors.HexColor('#1b1f24'); MUTED = colors.HexColor('#5a6370'); ACC = colors.HexColor('#0b6e6e')
LINE = colors.HexColor('#d6dbe1'); BAND = colors.HexColor('#f2f5f7')
GOOD = colors.HexColor('#dff2e4'); MID = colors.HexColor('#fdf3d6'); BAD = colors.HexColor('#f9e0e0')
WARN = colors.HexColor('#fff8e8')

def st(n, **k): return ParagraphStyle(n, fontName=k.pop('f', 'DV'), textColor=k.pop('c', INK), **k)
H0 = st('h0', f='DVB', fontSize=24, leading=29, spaceAfter=6)
SUB = st('sub', fontSize=11.5, leading=15.5, c=MUTED, spaceAfter=4)
H1 = st('h1', f='DVB', fontSize=16, leading=20, c=ACC, spaceAfter=7)
H2 = st('h2', f='DVB', fontSize=12, leading=15, spaceBefore=8, spaceAfter=4)
P = st('p', fontSize=9.3, leading=13, spaceAfter=4)
PS = st('ps', fontSize=8.3, leading=11.2, spaceAfter=3, c=MUTED)
B = st('b', fontSize=9.2, leading=12.6, leftIndent=12, bulletIndent=2, spaceAfter=2)
C = st('c', fontSize=8, leading=10.3)
CB = st('cb', f='DVB', fontSize=8, leading=10.3)
T = st('t', fontSize=5.8, leading=6.8)
TB = st('tb', f='DVB', fontSize=6.5, leading=8)

def esc(s): return html.escape(s or '', quote=False)
def cut(s, n): s = s or ''; return s if len(s) <= n else s[:n - 1].rstrip() + '…'
def para(t, s=P): return Paragraph(t, s)
def bullets(items): return [Paragraph(i, B, bulletText='•') for i in items]
def box(flow, bg=BAND, pad=8):
    t = Table([[flow]])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), bg), ('BOX', (0, 0), (-1, -1), 0.5, LINE),
                           ('LEFTPADDING', (0, 0), (-1, -1), pad), ('RIGHTPADDING', (0, 0), (-1, -1), pad),
                           ('TOPPADDING', (0, 0), (-1, -1), pad), ('BOTTOMPADDING', (0, 0), (-1, -1), pad)]))
    return t
def grid(rows, widths, shades=None):
    data = [[Paragraph(c, CB if i == 0 else C) for c in r] for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1)
    ts = [('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('BACKGROUND', (0, 0), (-1, 0), BAND),
          ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
          ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    for r, col in (shades or []): ts.append(('BACKGROUND', (0, r), (-1, r), col))
    t.setStyle(TableStyle(ts)); return t
def deco(c, d):
    c.saveState(); c.setFont('DV', 7.5); c.setFillColor(MUTED); w, h = c._pagesize
    c.drawString(15 * mm, 9 * mm, 'Research digest · %s · exercise selection · research summary, not medical advice' % DATE)
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='Exercise Selection Digest %s' % DATE, author='Kye research worker (Claude Code)',
                      subject='Which exercise grows more muscle and strength: upper body, lower body, free weights vs machines')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(10 * mm, 14 * mm, lw - 20 * mm, lh - 24 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm

studies = [r for r in csv.DictReader(open(KB + 'STUDIES.csv')) if r.get('run_date') == DATE]
audit = list(csv.DictReader(open(KB + 'notes/%s-audit.csv' % DATE)))
n_conf = sum(1 for a in audit if a['verdict'].upper().startswith('CONFIRM'))
n_corr = sum(1 for a in audit if a['verdict'].upper().startswith('CORRECT'))
n_full = sum(1 for r in studies if r['access'].upper().startswith('FULL'))
s = []

# ---------- page 1: cover + picks ----------
s += [Spacer(1, 4 * mm), para('RESEARCH DIGEST · %s' % DATE, st('k', f='DVB', fontSize=10.5, c=ACC, leading=14)),
      para('Which exercise grows more muscle and strength?', H0),
      para('Exercise selection for every muscle group, ranked by long-term training studies that measured muscle size '
           'and strength, not by EMG. For Kye: 87 kg, about 13.6% body fat, trains heavy about 1.5 h a day.', SUB),
      Spacer(1, 2 * mm)]
s.append(grid([
    ['Muscle', 'Best-supported pick', 'What the training studies show', 'Confidence'],
    ['<b>Chest</b>', 'One heavy press (barbell, Smith or machine) + a low incline press',
     'Barbell and machine programmes grew pecs the same (≤2% apart). Incline grew the upper pec 0.62 cm more in one beginner study. '
     'Bench vs flyes: never tested', 'Moderate / Limited'],
    ['<b>Back</b>', 'One vertical pull + one row, any grip that lets you train hard',
     '<b>No study compares any two back exercises for growth.</b> Pulldown vs pull-up vs rows is unanswered', 'None'],
    ['<b>Shoulders</b>', 'Lateral raises (dumbbell or cable)',
     'Dumbbell = cable (+3.3–4.6% both). Bench pressing grows the front delt and does least for the side delt', 'Limited'],
    ['<b>Biceps</b>', 'Direct curls, any variant',
     'Incline vs preacher: same total growth. Curls beat rows about 2:1 in one small study, but only matched pulldowns in another', 'Moderate / Limited'],
    ['<b>Triceps</b>', '<b>Overhead cable extension</b>',
     'Whole triceps +19.9% vs +13.9% for arm-at-side extensions. Bench alone grows the long head less', 'Limited (one study)'],
    ['<b>Quads</b>', 'Deep squat-pattern lift + leg extension',
     'Squats grow the vasti; rectus femoris grew 2–8% with squats vs 11–18% with leg extensions. Squat vs hack vs leg press: never tested', 'Moderate'],
    ['<b>Hamstrings</b>', 'Seated leg curl + a hip hinge',
     'Seated +14.1% vs lying +9.3%. Squats do not grow hamstrings (two MRI trials)', 'Moderate'],
    ['<b>Glutes</b>', 'Deep squat or leg press; hip thrust optional',
     'Hip thrust and squat grew glutes about equally (differences within ±6 cm²). Deep squat beat half squat (+6.7% vs +2.2%)', 'Limited'],
    ['<b>Calves</b>', 'Standing straight-knee calf raise',
     'Gastrocnemius +9–12% standing vs +1–2% seated; soleus no different', 'Moderate (one study)'],
    ['<b>Abs</b>', 'Unknown; train them like any other muscle', 'No study compares direct ab work with compound lifts only', 'Very limited'],
], [W * 0.145, W * 0.24, W * 0.445, W * 0.17],
    shades=[(1, MID), (2, BAD), (3, MID), (4, MID), (5, GOOD), (6, GOOD), (7, GOOD), (8, MID), (9, GOOD), (10, BAD)]))
CALL = st('call', fontSize=9.6, leading=13.2)
s += [Spacer(1, 3 * mm), box(para(
    '<b>The honest bottom line.</b> For most "A vs B" questions lifters ask, including lat pulldown vs pull-up and bench '
    'vs flyes, nobody has run the training study. Where studies exist, the lesson is less "this exercise is best" and more '
    '"<b>this compound lift leaves a gap</b>": pressing leaves the side delt and triceps long head behind, squats leave '
    'the rectus femoris and hamstrings behind. Fill the gaps with one isolation exercise each. Free weights and machines '
    'grow the same muscle. Strength is specific: you get strongest at the lift you train.', CALL)),
    Spacer(1, 2.5 * mm), box(para(
    '<b>How this was done.</b> Two research agents searched PubMed, Europe PMC, Crossref, OpenAlex and Semantic Scholar on '
    '%s; then an independent auditor re-checked %d study rows (the load-bearing ones plus a seeded random sample of 8). '
    'Result: %d confirmed, %d corrected, 0 rejected, and no verdict changed. %d studies were added to the database; only %d '
    'were read in full, because publisher sites were blocked. <b>Most trials are 6–12 weeks in beginners</b>, so for a '
    'trained lifter the direction of each result is the best available guess and the size is uncertain.'
    % (DATE, len(audit), n_conf, n_corr, len(studies), n_full), PS), bg=WARN)]
s.append(PageBreak())

# ---------- page 2: upper body ----------
s.append(para('Upper body: chest, back, shoulders, arms', H1))
s.append(grid([
    ['Question', 'Finding', 'Source'],
    ['Barbell vs machine programme, pec size', 'Difference ≤2.0% (P ≥ 0.208); 38 trained men, 8 weeks', 'Hernández-Belmonte 2023'],
    ['Incline vs flat bench, upper pec', '+0.62 cm more with incline (95% CI 0.23 to 1.0); 1 of 3 sites; 47 untrained men', 'Chaves 2020'],
    ['Push-ups vs bench at matched load', 'Similar pec growth; 18 men, 8 weeks, light loads', 'Kikuchi 2017'],
    ['Bench press only: what grows', 'Pecs and front delt grew; side delt grew least; 13 trainees vs 11 controls, MRI', 'Lanza 2024'],
    ['Dumbbell vs cable lateral raise', '+3.3–4.6% in both; Bayes factors 0.27 and 0.22 favour no difference; 24 trained lifters', 'Larsen 2025'],
    ['Overhead vs arm-at-side triceps extension', 'Long head +28.5% vs +19.6% (d 0.61); whole triceps +19.9% vs +13.9% (d 0.54); n = 21, MRI', 'Maeo 2023'],
    ['Bench press alone and the triceps', 'Lateral head grew; whole triceps not significantly; long head grew less than with extensions; 43 men', 'Brandão 2020'],
    ['Incline vs preacher curl', 'Biceps +22.1% vs +18.9%; brachialis +17.1% vs +21.1%; total +17.6% vs +19.2% (P = 0.134); 21 untrained', 'Kobayashi 2026'],
    ['Curls vs rows for biceps', '+11.06% vs +5.16% (p = 0.009); n = 10, untrained', 'Mannarino 2021'],
    ['Curls vs pulldowns for biceps', '+5.83% vs +6.10%: no difference; n = 29, untrained', 'Gentil 2015'],
], [W * 0.28, W * 0.50, W * 0.22]))
s += bullets([
    '<b>Chest:</b> one heavy press you can progress for years, plus a low incline press (30–45°) as a sensible bet. A fly is optional.',
    '<b>Back:</b> one vertical pull and one row. Grip width, overhand vs underhand and pulldown vs pull-up are all unproven for size. '
    'EMG puts the pullover closer to a chest exercise.',
    '<b>Shoulders:</b> do lateral raises; do not count bench pressing toward side delts. A reverse fly for rear delts is untested but cheap.',
    '<b>Arms:</b> do direct curls; make an overhead cable extension your first triceps exercise.'])
s.append(para('Never tested for muscle growth (upper body)', H2))
s += bullets([
    'Any back comparison: lat pulldown vs pull-up, pulldown vs row, grip width or type, pullover.',
    'Dumbbell vs barbell bench, decline bench, bench grip width, bench vs flyes, cable crossover or pec deck.',
    'Overhead press vs lateral raise for the side delt; rear-delt exercises vs rows; forearm exercises.'])
s.append(para('For these, EMG is all there is, and an EMG difference is not proof of more growth. In the one trial that checked, '
              'first-session EMG favoured the hip thrust but did not predict which exercise grew more muscle (Plotkin 2023).', PS))
s.append(PageBreak())

# ---------- page 3: lower body + cross-cutting ----------
s.append(para('Lower body: quads, hamstrings, glutes, calves', H1))
s.append(grid([
    ['Question', 'Finding', 'Source'],
    ['Leg extension vs Smith squat, rectus femoris', '+11.4/12.3/17.5% vs +2.0/5.7/7.9% (three sites); distal vastus lateralis +11.2% vs +18.2%; 63 untrained women', 'Kassiano 2026'],
    ['Full vs half squat', 'Knee extensors +4.9% vs +4.6%; rectus femoris and hamstrings unchanged; glute max +6.7% vs +2.2%; adductors +6.2% vs +2.7%; 17 men, MRI', 'Kubo 2019'],
    ['Seated vs lying leg curl', 'Hamstrings +14.1% vs +9.3%; biceps femoris long head +14.4% vs +6.5%; 20 adults, leg-vs-leg, MRI', 'Maeo 2021'],
    ['Lengthened seated curl vs Nordic curl', 'Hamstrings about +18% vs +11%; 42 young men, MRI', 'Maeo 2024'],
    ['Hip thrust vs squat, glutes', 'Differences −1.6 cm² (−6.1 to 2.0), −0.5 (−4.0 to 2.6), −0.5 (−5.8 to 4.1); 34 untrained, MRI', 'Plotkin 2023'],
    ['Hip thrust vs squat, quads and adductors', 'Squat grew quads +3.6 cm² (0.7 to 6.4) and adductors +2.5 cm² (1.2 to 3.9) more', 'Plotkin 2023'],
    ['Cable hip extension vs abduction', 'Glute max +9% vs +5%, opposite regional patterns; 17 adults, MRI', 'Attarieh 2026'],
    ['Standing vs seated calf raise', 'Lateral gastrocnemius +12.4% vs +1.7%; medial +9.2% vs +0.6%; soleus +2.1% vs +2.9%; 14 untrained, MRI', 'Kinoshita 2023'],
], [W * 0.28, W * 0.52, W * 0.20]))
s += bullets([
    '<b>Quads:</b> a deep squat, hack squat or leg press (none shown to beat the others) plus leg extensions, leaning back if the seat allows.',
    '<b>Hamstrings:</b> seated leg curl plus a Romanian deadlift or other hinge. Do not count squats or hip thrusts as hamstring work.',
    '<b>Glutes:</b> deep squats already count; hip thrusts are an equal alternative with less quad and lower-back fatigue.',
    '<b>Calves:</b> knee straight, full stretch at the bottom. Skip the seated calf raise or keep it as a minor extra.'])
s.append(para('Free weights vs machines, variety and strength', H1))
s.append(grid([
    ['Question', 'Finding', 'Source'],
    ['Free weights vs machines, muscle size', 'SMD −0.055 (95% CI −0.397 to 0.287): no difference; 13 studies, 1,016 people', 'Haugen 2023'],
    ['Free weights vs machines, strength', 'Free-weight-tested strength SMD −0.210 (−0.391 to −0.029), favouring free-weight training', 'Haugen 2023'],
    ['Strength in the trained lift vs an untrained test', 'SMD 0.98 vs 0.42 (0.75 vs 0.29 in trained lifters); 43 studies, 1,660 people', 'Saeterbakken 2025'],
    ['Hip thrust vs squat, 3RM', 'Squat 3RM +14 kg (9 to 18) for squatters; hip thrust 3RM +26 kg (16 to 34) for thrusters; deadlift equal', 'Plotkin 2023'],
    ['Fixed vs rotated exercises', 'Thickness +7.8–17.7% vs +7.5–19.3%; 1RM similar; 70 young women, 10 weeks', 'Kassiano 2025'],
], [W * 0.28, W * 0.52, W * 0.20]))
s += bullets([
    '<b>Equipment:</b> choose by comfort. Keep a barbell lift only if you care about that lift\'s number.',
    '<b>Variety:</b> two exercises per muscle group that hit different heads; keep them for a whole block. Rotating look-alike lifts adds nothing.',
    '<b>Never tested (lower body):</b> front vs back squat; hack squat vs anything; deadlifts, lunges or split squats for glute size; '
    'leg curl vs Romanian deadlift; direct ab work vs compounds only.'])
s.append(PageBreak())

# ---------- page 4: audit + new avenues ----------
s.append(para('Audit corrections', H1))
s.append(grid([
    ['Item', 'Correction'],
    ['Brandão 2020 (triceps)', '"Bench press alone does not grow the long head" was too strong. The abstract says it grew less than with extensions.'],
    ['Chest verdict', 'Dumbbell presses were listed as equal to barbell and machine. They have never been tested for growth; removed.'],
    ['Kassiano 2026 (quads)', '"Squats barely grow the rectus femoris" softened: it still grew 2–8% with squats, against 11–18% with leg extensions.'],
    ['Fonseca 2014 (variety)', 'Only the constant-intensity varied-exercise group gained the most squat strength, not both varied groups.'],
    ['Rossi 2018 (squat vs leg press)', 'Participants were trained, not untrained; Bod Pod only, no ultrasound. The leg-press carry-over claim was softened: size of the gap unknown.'],
    ['Kassiano 2023 (adding hip thrusts)', 'Not preprint-only: a peer-reviewed version exists (Int J Strength Cond 2024). Still very limited; volume was not equated.'],
    ['Haugen 2023; Baz-Valle 2019', 'Trained/untrained split and completer numbers corrected in the study table.'],
    ['Barbalho-group trials', 'Five trials: two retracted, one with a 2026 expression of concern, one with an unread erratum, one clean. None carries weight in a verdict.'],
    ['Still unverified', 'Chaves 2020 full text (incline angle unknown); full texts of Kassiano 2026 and Kubo 2019; the letter and reply on Zabaleta-Korta 2021.'],
], [W * 0.27, W * 0.73]))
s.append(para('New topics added to the queue', H1))
s += bullets([
    'Back hypertrophy evidence gap: any preprints or theses with lat, trap or rear-delt size after pulldown vs row or different grips?',
    'Counting sets from compounds: how much do bench, rows and pulldowns count toward triceps, delt and biceps volume?',
    'Upper pec and triceps long head in trained lifters: has incline vs flat or overhead vs pushdown been repeated?',
    'Do exercise-selection effects (seated curl, standing calf raise, leg extension) hold in trained lifters?',
    'Rectus femoris: what grows it best?',
    'Do direct ab exercises add size beyond heavy compound lifting?',
    'Deadlift variants, lunges and split squats for glutes; hack squat vs barbell squat vs leg press for quads.',
])
s.append(para('The queue now has 38 open topics. The creatine deep dive is paused at screening (4,000 of 4,587 records).', PS))

# ---------- study table ----------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 20 * mm
s.append(para('Every study added this round (%d)' % len(studies), H1))
names = [('exercise-selection-upper-body', 'Upper body'), ('exercise-selection-lower-body', 'Lower body'),
         ('exercise-selection-upper-body; exercise-selection-lower-body', 'Both: free weights vs machines, variety, strength specificity')]
cw = [LW * x for x in (0.15, 0.13, 0.40, 0.21, 0.055, 0.055)]
for topic, title in names:
    g = [r for r in studies if r['topic'] == topic]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [[Paragraph(x, TB) for x in ['Study', 'Design · n · who', 'Result (effect, uncertainty)', 'Limits / COI', 'Access', 'Audit']]]
    for r in g:
        v = r['verification']; aud = 'not sampled'
        if 'AUDIT:' in v: aud = v.split('AUDIT:')[-1].strip().split()[0]
        data.append([Paragraph('<b>%s</b><br/>%s' % (esc(r['key']), esc(cut(r['doi_or_link'].replace('https://doi.org/', ''), 45))), T),
                     Paragraph(esc(cut('%s · n = %s' % (r['design'], r['n']), 70)), T),
                     Paragraph(esc(cut(r['result_effect_uncertainty'], 150)), T),
                     Paragraph(esc(cut(r['limitations_coi'], 85)), T),
                     Paragraph(esc(cut(r['access'], 20)), T), Paragraph(esc(aud), T)])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('BACKGROUND', (0, 0), (-1, 0), BAND), ('LEFTPADDING', (0, 0), (-1, -1), 2.5),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 2.5), ('TOPPADDING', (0, 0), (-1, -1), 1),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
                           ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafbfc')])]))
    s.append(t)

doc.build(s)
print('ok', OUT, len(studies), len(audit), n_conf, n_corr, n_full)
