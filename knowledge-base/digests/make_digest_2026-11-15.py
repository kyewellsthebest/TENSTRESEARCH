"""Builds knowledge-base/digests/2026-11-15-digest.pdf (round 1: supplements). Adapted from binge/make_binge_pdf.py."""
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
DATE = '2026-11-15'
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
    c.drawString(15 * mm, 9 * mm, 'Research digest · %s · supplements round 1 · research summary, not medical advice' % DATE)
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='Supplements Digest %s' % DATE, author='Kye research worker (Claude Code)',
                      subject='Creatine, caffeine and pre-workouts, protein powders, beta-alanine/citrulline/nitrate/bicarbonate')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(10 * mm, 14 * mm, lw - 20 * mm, lh - 24 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm

studies = [r for r in csv.DictReader(open(KB + 'STUDIES.csv')) if r.get('run_date') == DATE]
audit = list(csv.DictReader(open(KB + 'notes/%s-audit.csv' % DATE)))
n_conf = sum(1 for a in audit if a['verdict'].upper().startswith('CONFIRM'))
n_corr = sum(1 for a in audit if a['verdict'].upper().startswith('CORRECT'))
s = []

# ---------- page 1: cover + verdicts ----------
s += [Spacer(1, 6 * mm), para('RESEARCH DIGEST · %s' % DATE, st('k', f='DVB', fontSize=10.5, c=ACC, leading=14)),
      para('Supplements, round 1: what is worth taking?', H0),
      para('Creatine · caffeine and pre-workouts · protein powders · beta-alanine, citrulline, beetroot nitrate and '
           'sodium bicarbonate. Verdicts for Kye: 87 kg, about 13.6% body fat, trains heavy about 1.5 h a day.', SUB),
      Spacer(1, 3 * mm)]
s.append(grid([
    ['Topic', 'Verdict in one line', 'Confidence', 'Take it?'],
    ['<b>Creatine monohydrate</b>', 'About +1.4 kg fat-free mass and a few kg on your lifts; kidney-safe (but skews '
     'blood tests); the hair scare is unfounded', 'Strong', '<b>Yes</b>: 5 g/day, any time'],
    ['<b>Caffeine</b>', 'About +1–2% 1RM and about 1 extra rep per set; costs sleep; no extra muscle long-term',
     'Strong (acute)', '<b>Yes, on hard days</b>: 175–260 mg, ≥8–10 h before bed'],
    ['<b>Pre-workout blends</b>', 'Mostly caffeine plus under-dosed extras and hidden blends; documented '
     'banned-stimulant contamination', 'Moderate', '<b>No</b>: use plain caffeine'],
    ['<b>Protein powder</b>', 'Total protein matters, not the source; whey ≈ soy; powder is convenience only',
     'Moderate', '<b>If handy</b>: whey, 30–40 g a serve'],
    ['<b>Beta-alanine</b>', 'Small gain for 0.5–10 min efforts; nothing for straight 6–12-rep sets or muscle',
     'Moderate', 'Optional: only for short-rest, high-rep work'],
    ['<b>Beetroot nitrate</b>', 'SMD about 0.4 on reps to failure, but from 5–6 small studies; no long-term data',
     'Limited', 'Optional: cheap to test'],
    ['<b>Sodium bicarbonate</b>', 'Most reliable rep booster (SMD 0.37); nothing for strength; GI upset and about 7 g sodium',
     'Moderate (low certainty)', '<b>No</b> for routine training'],
    ['<b>Citrulline</b>', 'Weakest of the lot (SMD about 0.16–0.20); good trials in trained lifters were null',
     'Moderate', '<b>No</b>'],
], [W * 0.19, W * 0.45, W * 0.14, W * 0.22],
    shades=[(1, GOOD), (2, GOOD), (3, BAD), (4, MID), (5, MID), (6, MID), (7, BAD), (8, BAD)]))
s += [Spacer(1, 4 * mm), box(para(
    '<b>The honest bottom line.</b> Of everything here, only creatine changes what you build over months, and even '
    'that is about a kilo. Caffeine gives a reliable small bump on the day. The rest are rounding errors next to '
    'effort, volume, total protein and sleep. Your full stack is <b>5 g creatine daily + caffeine on hard days + '
    'about 140–190 g protein from whatever source is cheapest</b>. Everything else is optional.', CALL := st('call', fontSize=9.8, leading=13.6))),
    Spacer(1, 3 * mm), box(para(
    '<b>How this was done.</b> Four research agents searched PubMed, PMC, Europe PMC, Crossref, OpenAlex and Semantic '
    'Scholar on %s; then an independent auditor re-checked %d study rows: the load-bearing ones plus a seeded random '
    'sample of 8. Result: %d confirmed, %d corrected, 0 wrong, and no verdict changed. %d studies were added to the '
    'database. Many papers were read as abstracts only (marked in the table). Research summary, not medical advice.'
    % (DATE, len(audit), n_conf, n_corr, len(studies)), PS), bg=WARN)]
s.append(PageBreak())

# ---------- page 2: creatine + caffeine ----------
s.append(para('Creatine monohydrate', H1))
s.append(grid([
    ['Question', 'Finding (95% CI)', 'Source'],
    ['Fat-free mass (61 trials)', '+1.39 kg (1.07 to 1.70); trained +1.82 kg (1.10 to 2.55)', 'Ashtary-Larky 2025'],
    ['Independent team (no industry ties)', '+1.14 kg lean mass (0.69 to 1.59)', 'Desai 2024'],
    ['Muscle size, measured directly', 'SMD 0.11 (−0.02 to 0.25): about +0.1–0.16 cm thickness', 'Burke 2023'],
    ['Strength', 'Bench +1.43 kg (0.53 to 2.34); squat +5.64 kg (3.87 to 7.40)', 'Kazeminasab 2025'],
    ['Kidneys', 'Estimated GFR −10.75 mL/min, but measured GFR unchanged: a test artefact', 'Tsiaras 2026; de Souza Almeida 2026'],
    ['Hair/DHT', 'One 2009 study (n = 20, hair not measured); a 2025 RCT found no change', 'van der Merwe 2009; Lak 2025'],
], [W * 0.27, W * 0.48, W * 0.25]))
s += bullets(['<b>Do:</b> 5 g/day every day; timing doesn’t matter. Loading (20 g/day for 5–7 days) is optional. '
              'Expect about +1 kg of water weight.',
              '<b>Tell your GP before blood tests.</b> Ask for a cystatin C eGFR if kidney function is in question.',
              '<b>Caveat:</b> much of the field is industry-linked (AlzChem/Creapure advisers), but independent '
              'meta-analyses agree.'])
s.append(para('Caffeine and pre-workouts', H1))
s.append(grid([
    ['Question', 'Finding (95% CI)', 'Source'],
    ['1RM strength', 'SMD 0.20 (0.03 to 0.36): about +1–2%', 'Grgic 2018'],
    ['Reps to failure', 'SMD 0.30 (0.21 to 0.38): bench about +0.9 reps', 'Bilondi 2024; Ferreira 2021'],
    ['Low dose (0.9–2 mg/kg)', 'Still works: strength d 0.17, endurance d 0.21', 'Grgic 2022'],
    ['Sleep', 'Total sleep −45 min, efficiency −7%, deep sleep −11 min', 'Gardiner 2023'],
    ['Long-term', 'Bench +13.5% vs +11.3% with placebo over 4 weeks: no difference', 'Giráldez-Costas 2021'],
    ['Pre-workouts', '254 mg caffeine per serving on average; 44% of ingredients in hidden blends; 9 banned stimulants found', 'Jagim 2019; Cohen 2021'],
], [W * 0.27, W * 0.48, W * 0.25]))
s += bullets(['<b>Do:</b> 2–3 mg/kg (175–260 mg) 45–60 min before key sessions; keep the day ≤400 mg (EFSA). '
              'Last dose ≥8–10 h before bed.',
              '<b>Skip branded pre-workouts</b>, and never use products listing DMAA, DMHA, BMPEA or "geranium extract".',
              '<b>Habituation is partial:</b> daily use fades in about 2–3 weeks, so save it for hard days.'])
s.append(PageBreak())

# ---------- page 3: protein + buffers ----------
s.append(para('Protein powders', H1))
s.append(grid([
    ['Question', 'Finding (95% CI)', 'Source'],
    ['Protein supplementation (49 RCTs)', 'Fat-free mass +0.30 kg (0.09 to 0.52); trained +1.05 kg (0.61 to 1.50)', 'Morton 2018'],
    ['Plateau', '1.62 g/kg/day (1.03 to 2.20); 2.2 g/kg is a safe upper target', 'Morton 2018'],
    ['Soy vs milk', 'SMD −0.02 (−0.20 to 0.16): no difference', 'Reid-McCann 2025'],
    ['Non-soy plant proteins', 'SMD −0.58 (−1.06 to −0.09), only 5 trials', 'Reid-McCann 2025'],
    ['Vegan + soy vs omnivore + whey', 'Same leg lean-mass gain (about +1.2 kg each)', 'Hevia-Larraín 2021'],
    ['Contamination (Australia)', '35% of 200 supplements bought online had banned substances; 1 of 14 protein powders', 'Barker 2025'],
], [W * 0.27, W * 0.48, W * 0.25]))
s += bullets(['<b>Do:</b> hit about 140 g protein a day (1.6 g/kg), up to about 190 g when cutting. Whey concentrate or '
              'isolate, 30–40 g a serve.',
              '<b>Plant:</b> soy or a pea + rice blend, +10–20% per serve; avoid chocolate (more lead and cadmium).',
              '<b>Caveat:</b> trained-lifter trials are tiny and industry-funded (dairy, soy, rice-protein makers).'])
s.append(para('Beta-alanine, citrulline, beetroot nitrate, sodium bicarbonate', H1))
s.append(grid([
    ['Supplement', 'Acute effect (95% CI)', 'Long-term / other'],
    ['Beta-alanine', 'ES 0.18 (0.08 to 0.28); trained men, 0.5–10 min efforts: 0.39 (0.09 to 0.69)',
     'Fat-free mass +0.05 kg (−0.71 to 0.82); harmless tingling'],
    ['Citrulline', 'SMD 0.20 (0.01 to 0.39): about +3 reps across 5 sets', 'Null in 35 trained lifters (Haugen 2023)'],
    ['Beetroot nitrate', 'Reps to failure SMD 0.43 (0.16 to 0.69), 5–6 small studies', 'No long-term data in lifters'],
    ['Bicarbonate', 'Endurance SMD 0.37 (0.15 to 0.59); strength 0.02', 'No added adaptation over 10 weeks; GI risk'],
], [W * 0.18, W * 0.45, W * 0.37]))
s += bullets(['<b>Skip citrulline.</b> Bicarbonate only for a 30 s–10 min test or event, trialled first.',
              '<b>Beta-alanine (3.2–6.4 g/day, ≥4 weeks)</b> only for high-rep, short-rest or density work.',
              '<b>Beetroot:</b> 1–2 concentrated 70 mL shots 2–3 h before a key session, if curious.',
              '<b>Treat with caution:</b> Pouresmaeili 2026’s claimed big muscle gain (single-blind, n = 10 per group).'])

# ---------- page 4: audit + new avenues ----------
s.append(para('Audit corrections', H1))
s.append(grid([
    ['Item', 'Correction'],
    ['Pouresmaeili 2026 (buffers)', 'Placebo muscle-CSA gain was +5–9%, not +5% (so 2.5–5×, not 4×); recreationally active, '
     'not untrained; single-blind. Still very limited.'],
    ['Barker 2025 (protein)', '200 products bought (201 samples), not 201 supplements'],
    ['Prokopidis 2023 (creatine)', 'The "young adults" memory subgroup covers ages 11–31'],
    ['Framing (caffeine)', 'The 260 mg ceiling is 3 mg/kg: above EFSA’s absolute 200 mg single-dose figure, consistent with its per-kg basis'],
    ['Framing (protein)', '1.62 g/kg is an average plateau, not a proven individual minimum'],
    ['Unverified', 'AIS Group A status checked via web search only (PDFs blocked); citrulline’s AIS group unknown'],
], [W * 0.3, W * 0.7]))
s.append(para('New topics added to the queue', H1))
s += bullets([
    'Creatine during a calorie deficit: does it preserve lean mass and strength in trained lifters who are cutting?',
    'Reading kidney blood tests as a muscular, creatine-using lifter: cystatin C vs creatinine-based eGFR.',
    'Creatine responders: how common are true non-responders, and what predicts them?',
    'Does caffeine-related sleep loss (30–45 min a night) cut hypertrophy or strength gains over 8+ weeks?',
    'Does 7–14 days off caffeine restore the full lifting effect in heavy habitual users?',
    'Collagen protein: does it count toward hypertrophy protein targets?',
    'Protein powder vs whole food at matched intake during a cut.',
    'Beta-alanine or bicarbonate in short-rest hypertrophy programmes: more volume, more muscle?',
])
s.append(para('The queue now has 32 open topics. Next round: vitamin D, omega-3, magnesium and zinc, then test '
              'boosters (ashwagandha, tongkat ali, fenugreek).', PS))

# ---------- study table ----------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 20 * mm
s.append(para('Every study added this round (%d)' % len(studies), H1))
names = {'creatine': 'Creatine', 'caffeine-preworkout': 'Caffeine & pre-workouts', 'protein-powders': 'Protein powders',
         'buffers-nitrates': 'Beta-alanine, citrulline, nitrate, bicarbonate'}
cw = [LW * x for x in (0.15, 0.13, 0.40, 0.21, 0.055, 0.055)]
for topic, title in names.items():
    g = [r for r in studies if r['topic'] == topic]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [[Paragraph(x, TB) for x in ['Study', 'Design · n · who', 'Result (effect, uncertainty)', 'Limits / COI', 'Access', 'Audit']]]
    for r in g:
        v = r['verification']; aud = 'not sampled'
        if 'AUDIT:' in v: aud = v.split('AUDIT:')[-1].strip().split()[0]
        data.append([Paragraph('<b>%s</b><br/>%s' % (esc(r['key']), esc(cut(r['doi_or_link'].replace('https://doi.org/',''), 45))), T),
                     Paragraph(esc(cut('%s · n = %s' % (r['design'], r['n']), 70)), T),
                     Paragraph(esc(cut(r['result_effect_uncertainty'], 165)), T),
                     Paragraph(esc(cut(r['limitations_coi'], 95)), T),
                     Paragraph(esc(cut(r['access'], 20)), T), Paragraph(esc(aud), T)])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('BACKGROUND', (0, 0), (-1, 0), BAND), ('LEFTPADDING', (0, 0), (-1, -1), 2.5),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 2.5), ('TOPPADDING', (0, 0), (-1, -1), 1),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
                           ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafbfc')])]))
    s.append(t)

doc.build(s)
print('ok', OUT, len(studies), len(audit), n_conf, n_corr)
