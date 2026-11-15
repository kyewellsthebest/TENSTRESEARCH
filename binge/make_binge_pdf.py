"""Builds BINGE-REPORT.pdf from the one-day overeating research round (B1-B2 + BA audit)."""
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

R = '/home/user/tenstresearch/binge/'
OUT = R + 'BINGE-REPORT.pdf'
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
    c.drawString(15 * mm, 9 * mm, 'One big day a week · 8 Nov 2026 · research summary, not medical advice')
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='Binge Day Research Report',
                      author='TENSR research team (Claude Code)',
                      subject='Does a weekly 1,000 kcal overeat undo a diet? Physiology, weekly maths, behaviour, and your numbers')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(12 * mm, 14 * mm, lw - 24 * mm, lh - 26 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm
studies = list(csv.DictReader(open(R + 'BINGE-STUDIES.csv')))
n_all = len(studies); n_aud = sum(1 for r in studies if r['audit_verdict'] != 'not sampled')
s = []

# ---------------- cover ----------------
s += [Spacer(1, 34 * mm), para('RESEARCH REPORT', st('k', f='DVB', fontSize=11, c=ACC, leading=14)),
      para('One big day a week: does a 1,000-calorie Sunday undo your diet?', H0),
      para('What happens to the extra food, why Monday feels worse than it is, how the weekly maths works, when a '
           'planned big day helps or hurts — and what your own numbers say about your current stall.', SUB),
      Spacer(1, 6 * mm)]
s.append(box(para(
    '<b>Inside</b><br/><b>1</b> The answer in one page · <b>2</b> Where 1,000 extra calories go · <b>3</b> Why Monday '
    'feels fatter · <b>4</b> The weekly maths · <b>5</b> Your numbers and your stall · <b>6</b> Does the pattern matter? · '
    '<b>7</b> The behaviour side · <b>8</b> Fact-check log · <b>9</b> Every study (%d)' % n_all, CALL)))
s += [Spacer(1, 6 * mm), box(para(
    '<b>How this was done.</b> Two research agents (overfeeding physiology; weekly patterns and binge behaviour) '
    'searched on 8 Nov 2026, then an independent auditor re-checked %d studies, all the arithmetic and your '
    'maintenance estimate. <b>Limits:</b> full papers could not be opened, so everything is at abstract or summary '
    'level. No study matches your exact pattern; single-day figures are scaled from 1–14-day overfeeding studies, '
    'mostly in untrained people. Your personal numbers come from what you told me in chat. Research summary, not '
    'medical advice.' % n_aud, PS), bg=WARN)]
s.append(PageBreak())

# ---------------- Part 1 ----------------
s.append(para('Part 1 — The answer in one page', H1))
s += bullets([
    '<b>One +1,000 day adds at most ~100–125 g of body fat</b> — not a lot. About 5–25% of the extra is burned off that '
    'day through digestion and heat; the rest is stored.',
    '<b>Whether it matters depends on your weekly total.</b> It doesn’t create a separate lump of fat — it simply '
    'cancels part of the week’s deficit. With a big deficit (like your stated 1,800–2,000 a day) it costs ~12–22% of '
    'the week. With a small one (250 a day) it wipes out most of it.',
    '<b>The “fatter on Monday” feeling is water, glycogen, salt and food in your gut</b> — typically ~0.3 kg on '
    'average in daily-weighing studies, up to ~2 kg after a very big day, gone in 2–5 days. The real fat is about the '
    'volume of a small glass of water spread over your whole body: you can’t see or feel it.',
    '<b>Weight normally peaks Sunday/Monday and bottoms Friday</b> in people who are losing. Judge progress Friday to '
    'Friday or on 7-day averages, never on Monday.',
    '<b>Your stall is the more important finding.</b> On paper, 1,800–2,000 a day is a ~1,250-calorie deficit and '
    'you’d be losing ~0.7 kg a week. You’re not — so your real average intake (weekdays plus weekend) is probably '
    'close to your maintenance right now. Part 5 shows how to fix it.',
    '<b>Is a binge here and there alright?</b> Yes — if it’s planned and bounded, your weekly deficit is real '
    '(about 500 a day or more), and it doesn’t feel out of control. The risk is the “I’ve blown it” mindset, not the '
    'calories.',
])
s.append(PageBreak())

# ---------------- Part 2 ----------------
s.append(para('Part 2 — Where 1,000 extra calories go', H1))
s.append(grid([
 ['What happens', 'Evidence'],
 ['5–25% (≈50–250 kcal) is burned off that day as digestion and heat', 'One day at double energy needs raised 24-h energy '
  'use by ~11% (Thearle 2013); ~9–11% of a fat surplus burned off (Dallosso 1984)'],
 ['Fat in the binge is stored very efficiently (~90–95%); carbs less so (~75–85%)', 'Horton 1995'],
 ['Carbs make fat mainly by sparing the fat you eat, not by turning into fat', 'Fat burning fell and dietary fat '
  'absorbed most of a carb surplus (Jebb 1996, only 3 men); turning carbs into fat needs days of huge overfeeding '
  '(Acheson 1988; McDevitt 2001)'],
 ['Glycogen refills fully within ~24 h', 'Bussau 2002'],
 ['Net: ~750–950 kcal stored ≈ <b>100–125 g of body fat</b> at most', 'Arithmetic (≈7,700–9,400 kcal per kg)'],
 ['“A big day boosts metabolism” — real but tiny; it never pays for itself. Leptin rises ~28% for about a day after a '
  'carb overfeed; appetite doesn’t reliably drop the next day', 'Dirlewanger 2000; Halliday 2020'],
 ['A protein-heavy binge: total fat gain was similar at 5%, 15% and 25% protein in an 8-week overfeeding study — extra '
  'protein added lean mass on top rather than cutting fat storage', 'Bray 2012 (corrected by the auditor)'],
], [W * 0.55, W * 0.45]))

# ---------------- Part 3 ----------------
s.append(para('Part 3 — Why Monday feels fatter', H1))
s.append(grid([
 ['Source of Monday weight', 'Typical size', 'Gone in'],
 ['Glycogen refilled + ~3 g water per gram', '~0.4–1.2 kg', '2–5 days'],
 ['Salt-driven water', '0 to ~1 kg (evidence mixed)', '1–3 days'],
 ['Food in your gut', 'roughly 0.5–1.5 kg (estimate; never measured)', '1–2 days'],
 ['<b>Actual new fat</b>', '<b>~0.1 kg</b>', 'cancelled by the next ~1–2 deficit days'],
], [W * 0.45, W * 0.33, W * 0.22]))
s.append(para('These are upper bounds; daily-weighing studies show a typical within-week swing of about 0.35% of body '
              'weight (~0.3 kg for you; Turicchi 2020). Bloating and puffiness are what you feel — not fat.', P))

# ---------------- Part 4 ----------------
s.append(para('Part 4 — The weekly maths (5 deficit days, Fri/Sat at maintenance, Sun +1,000)', H1))
s.append(grid([
 ['Deficit on 5 days', 'Week total', 'Share of deficit cancelled by Sunday', 'Fat loss/week (approx.)'],
 ['250 kcal/day', '−250 kcal', '~60–80%', '~0.03 kg — stalled'],
 ['500 kcal/day', '−1,500 kcal', '~30–40%', '~0.2 kg'],
 ['750 kcal/day', '−2,750 kcal', '~27%', '~0.36 kg'],
 ['~1,250 kcal/day (your stated intake)', '−5,250 kcal', '~16%', '~0.7 kg'],
], [W * 0.28, W * 0.18, W * 0.30, W * 0.24], shades=[(1, BAD), (2, MID), (3, GOOD), (4, GOOD)]))
s.append(para('The range in the “cancelled” column depends on whether the 5–25% burned off on the day is counted. '
              '<b>The real danger is when Friday and Saturday aren’t really maintenance:</b> +300 each turns a 250/day '
              'week into a surplus and takes ~64% of a 500/day week.', P))
s.append(PageBreak())

# ---------------- Part 5 ----------------
s.append(para('Part 5 — Your numbers and your stall', H1))
s.append(grid([
 ['', 'Value'],
 ['Weight · body fat', '87 kg · 13.6% (device unknown)'],
 ['Lean mass', '≈75.2 kg'],
 ['Resting burn (Cunningham — the most accurate equation in recreational athletes; ten Haaf 2014)', '≈2,150 kcal'],
 ['Estimated maintenance (resting burn + digestion + ~90 min heavy lifting + cardio + daily movement)',
  '<b>≈2,900–3,500, central ~3,150</b> — biggest unknown is your daily steps'],
 ['Stated intake', '1,800–2,000 kcal on deficit days'],
 ['What that would predict', '~0.5–1 kg loss per week'],
 ['What actually happened', '−9 kg since 28 May (~23 weeks, ~0.4 kg/week); stalled for ~6 weeks'],
], [W * 0.55, W * 0.45]))
s.append(para('What the stall tells you', H2))
s += bullets([
    '<b>A flat weight means your average intake across the week now equals your maintenance.</b> The formulas say '
    'you should be losing; the scale says you aren’t. The scale wins.',
    '<b>Dropping 3 cardio sessions</b> removed only ~600 kcal a week (~85 a day) — not enough on its own.',
    '<b>You also burn less than in May:</b> 9 kg lighter, plus the body’s usual adaptation during a long cut — mostly '
    'moving a bit less without noticing. Roughly 200–300 kcal a day.',
    '<b>Under-reporting is the most common cause:</b> even dietitians under-reported by ~220 kcal a day and '
    'non-dietitians by ~430 (Champagne 2002); “diet-resistant” people under-reported by ~47% (Lichtman 1992). Oils, '
    'sauces, drinks, tastes and weekend meals are the usual leaks.',
    '<b>Weekend “maintenance” is often a surplus.</b> Example: true weekdays ~2,375, Friday and Saturday +300 each, '
    'Sunday really +1,500 → only ~0.23 kg a week, which looks like a stall with normal water swings on top.',
    '<b>You may be recomping.</b> You’re still gaining strength and muscle. Check your waist at the navel each morning: '
    'if it’s shrinking while weight is flat, fat loss is continuing.',
])
s.append(para('Your options', H2))
s.append(grid([
 ['Goal', 'What to do'],
 ['<b>Keep cutting</b>', 'Treat your current weekly average as maintenance. Lower it by ~3,000–3,500 kcal a week '
  '(~450–500 a day): log weekends honestly, weigh food for 2 weeks, cap Sunday at ~+500, or add back 1–2 cardio '
  'sessions or ~3,000 extra daily steps. Target ~0.4–0.6 kg a week on 7-day averages.'],
 ['<b>Take a planned break</b>', '1–2 weeks at true maintenance, then resume. No extra fat loss, but it helped hunger '
  'and adherence in trained people (ICECAP).'],
 ['<b>Recomp on purpose</b>', 'Hold intake, keep lifting hard, protein 175–210 g a day. Slow but valid if strength '
  'climbs and your waist holds or drops.'],
], [W * 0.22, W * 0.78]))
s.append(para('Check in 4 weeks: compare the 7-day average weight and waist now with 4 weeks later.', P))
s.append(PageBreak())

# ---------------- Part 6 ----------------
s.append(para('Part 6 — Does the pattern of the week matter?', H1))
s += bullets([
    '<b>Weekly total decides fat loss.</b> Intermittent vs continuous dieting gave comparable fat loss across five '
    'meta-analyses and trials (Schroor 2024, 28 RCTs; Cioffi 2018; Headland 2016; Davis 2016; Harvie 2011). Schroor '
    'found slightly more lean loss with intermittent dieting (−0.20 kg), with intake matched in only 17 of 28 trials.',
    '<b>Refeeds and diet breaks in trained lifters:</b> no extra fat loss (Campbell 2020; ICECAP); breaks lowered hunger.',
    '<b>Weekends are where diets leak:</b> dieters stopped losing on weekends (Racette 2008, 48 people, 1 year). '
    'Adults typically eat ~80–115 kcal a day more Friday–Sunday (Haines 2003) — your +1,000 is about 10× that.',
])

# ---------------- Part 7 ----------------
s.append(para('Part 7 — The behaviour side', H1))
s += bullets([
    '<b>The “what-the-hell” effect:</b> restrained eaters who think they’ve blown it eat more afterwards (Herman &amp; '
    'Mack 1975; Polivy 2010).',
    '<b>Rigid all-or-nothing dieting</b> goes with more binge eating and higher BMI; flexible dieting with less '
    '(Westenhoefer 1999; Stewart 2002; Linardon &amp; Mitchell 2017 — associations, not proof).',
    '<b>Dieting and binges:</b> in people without an eating disorder, 4 of 11 diet interventions increased binge eating, '
    '5 decreased it (da Luz 2015) — it depends on how the diet is run.',
    '<b>Cheat meals are near-universal</b>; 1,000–1,499 kcal is the most common size (Ganson 2022, 2,717 people). In men, '
    'more frequent cheat meals went with more binge episodes (Murray 2018). One small study found planned treats helped '
    'goal-keeping (Coelho do Vale 2016). No trial has tested a planned weekly high day in lifters.',
    '<b>Bodybuilders show the extreme:</b> 46% of drug-free male bodybuilders binged after competing and 85% regained '
    '(Andersen 1995). Deeper, longer, more appearance-driven cuts carry more rebound risk.',
])
s.append(box(para(
    '<b>When it’s worth getting help</b> — if eating feels out of control, happens most weeks, and leaves you '
    'distressed or guilty (the core of binge eating disorder: loss of control, about weekly for 3 months, marked '
    'distress, no regular compensating). Start with a GP, or the <b>Butterfly Foundation National Helpline 1800 33 4673</b> '
    '(8am–midnight AEST/AEDT, 7 days). In a crisis: <b>000</b> or <b>Lifeline 13 11 14</b> (24/7). A planned, '
    'enjoyed big day that you’re in control of is not this.', P), bg=RES))

# ---------------- Part 8 ----------------
s.append(para('Part 8 — Fact-check log', H1))
s.append(grid([
 ['Item', 'Correction'],
 ['Bray 2012', 'Fat gain was similar at all protein levels — protein added lean mass, it didn’t reduce fat storage'],
 ['da Luz 2015', '4 of 11 interventions increased binge eating in people without BED — stronger than first stated'],
 ['Jebb 1996', 'Only 3 men'],
 ['Kolaczynski 1996', 'The ~40% leptin rise came from ~10,000 kcal for someone your size — 10× your Sunday'],
 ['McDevitt 2001', 'Glucose didn’t raise fat synthesis in obese women; only sucrose did'],
 ['Orsama 2014 / Helander 2016', 'Co-authored by Wansink; no retraction or concern notice found (web search, not exhaustive)'],
 ['Monday weight swing', '0.5–2.5 kg is a sum of upper bounds; typical is ~0.3 kg (Turicchi 2020)'],
 ['Weekly tables', 'Earlier 40–80% figures assumed small deficits; they don’t apply to your stated intake'],
 ['Maintenance multiplier', '1.5–1.6 is low for your training; a bodybuilder study measured ~2.0'],
], [W * 0.27, W * 0.73]))

# ---------------- Part 9 ----------------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 24 * mm
s.append(para('Part 9 — Every study recorded (%d)' % n_all, H1))
groups = [('B1', 'Overfeeding physiology'), ('B2', 'Weekly patterns, cheat days and binge behaviour'), ('BA', 'Added by the auditor')]
cw = [LW * x for x in (0.22, 0.14, 0.16, 0.24, 0.16, 0.08)]
for code, title in groups:
    g = [r for r in studies if r['found_by'].split(';')[0] == code]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [[Paragraph(x, TB) for x in ['Study', 'Design · who', 'Compared', 'Result', 'Limits', 'Checked']]]
    for r in g:
        cit = '<b>%s</b><br/>%s' % (esc(r['key']), esc(r['citation']))
        if r['doi_or_link']: cit += '<br/><font color="#5a6370">%s</font>' % esc(r['doi_or_link'][:100])
        data.append([Paragraph(cit, T),
                     Paragraph('%s<br/>n = %s<br/>%s<br/>%s' % (esc(r['design']), esc(r['n']), esc(r['population']), esc(r['duration'])), T),
                     Paragraph('%s<br/><i>%s</i>' % (esc(r['intervention_comparison']), esc(r['outcome_measure'])), T),
                     Paragraph(esc(r['result_effect_uncertainty']), T),
                     Paragraph(esc(r['limitations_coi']) + '<br/><font color="#5a6370">Access: %s</font>' % esc(r['access']), T),
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
