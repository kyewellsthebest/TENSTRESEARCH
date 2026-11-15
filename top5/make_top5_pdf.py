"""Builds TENSR-TOP5-FACTORS.pdf from the top-5 research round (F1-F6 + FA audit)."""
import csv, html, re, collections
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

R = '/home/user/tenstresearch/top5/'
OUT = R + 'TENSR-TOP5-FACTORS.pdf'
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
    data = [[Paragraph(c, CB if (head and i == 0) else style) if isinstance(c, str) else c for c in r]
            for i, r in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    ts = [('GRID', (0, 0), (-1, -1), 0.4, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
          ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
          ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    if head: ts.append(('BACKGROUND', (0, 0), (-1, 0), BAND))
    for r, col in (shades or []): ts.append(('BACKGROUND', (0, r), (-1, r), col))
    t.setStyle(TableStyle(ts)); return t
def deco(c, d):
    c.saveState(); c.setFont('DV', 7.5); c.setFillColor(MUTED); w, h = c._pagesize
    c.drawString(15 * mm, 9 * mm, 'TENSR · Top-5 muscle-growth factors · 2 Nov 2026 · research only — not product claims')
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='TENSR Top-5 Growth Factors',
                      author='TENSR research team (Claude Code)',
                      subject='The five training factors that matter most for hypertrophy in trained lifters, and how TENSR could track them')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(12 * mm, 14 * mm, lw - 24 * mm, lh - 26 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm
s = []

studies = list(csv.DictReader(open(R + 'TOP5-STUDIES.csv')))
n_all = len(studies)
n_meta = sum(1 for r in studies if re.search(r'meta|systematic|review|umbrella', r['design'], re.I))
n_aud = sum(1 for r in studies if r['audit_verdict'] and r['audit_verdict'] != 'not sampled')

# ---------------- cover ----------------
s += [Spacer(1, 34 * mm), para('TENSR', st('k', f='DVB', fontSize=11, c=ACC, leading=14)),
      para('The five things that matter most for muscle growth — and how TENSR could track them', H0),
      para('For intermediate and advanced lifters. What the studies show, why each factor works, which popular '
           'claims fell apart on fact-checking, and what the band would need — firmware, app, or extra hardware — '
           'to measure each one.', SUB), Spacer(1, 6 * mm)]
s.append(box(para(
    '<b>Inside</b><br/>'
    '<b>1</b> The answer in one page · <b>2</b> The five factors, one by one · <b>3</b> What didn’t make the top five, '
    'and why · <b>4</b> How TENSR can track them: what works now, what needs a second puck, what needs a new board · '
    '<b>5</b> Fact-check log · <b>6</b> How many studies, honestly · <b>7</b> Every study (%d)' % n_all, CALL)))
s += [Spacer(1, 6 * mm), box(para(
    '<b>How this was done.</b> Six research agents (effort; volume; muscle length; load and rep execution; rest and '
    'progression; sensing engineering) searched on 2 Nov 2026, then an independent auditor re-checked %d of the '
    'studies and the circuit-board facts. <b>Limits:</b> this computer could not open full papers — PubMed, PMC '
    'and doi.org were blocked — so every study was checked from its abstract or from other papers’ summaries. No '
    'citation was found to be made up, but read the key papers in full before using any number in marketing. Most '
    'training studies use 10–50 people for 8–12 weeks; “no difference” in a small study is not proof of “the same”.'
    % n_aud, PS), bg=WARN)]
s.append(PageBreak())

# ---------------- Part 1 ----------------
s.append(para('Part 1 — The answer in one page', H1))
s.append(para('The top five for trained lifters', H2))
top = [
 ['#', 'Factor', 'The rule the evidence supports', 'How sure'],
 ['1=', '<b>Effort</b> — how close each set gets to failure',
  'Sets must end close to failure to count: roughly 0–3 reps in reserve, closer with light weights. Going all the way '
  'to failure adds little or nothing for trained lifters and costs more fatigue.', 'Moderate'],
 ['1=', '<b>Volume</b> — hard sets per muscle per week',
  'More hard sets build more muscle, with diminishing returns. ~4 → 10+ sets/week roughly doubled growth in pooled '
  'data. No proven ceiling; gains flatten somewhere past ~20–30 sets.', 'Moderate'],
 ['3', '<b>Exercise selection &amp; muscle length</b>',
  'Avoid short top-half reps. Prefer exercises that load the muscle stretched (seated leg curl, overhead triceps, '
  'deep calf raises). Use more than one exercise per muscle so every region is trained.', 'Low–moderate'],
 ['4', '<b>Rest long enough to keep your reps</b>',
  'At least ~90 s, ~2–3 min on heavy compound lifts. Rest works mainly by protecting the next set’s reps — if you '
  'rest less, add sets to make up the volume.', 'Low–moderate'],
 ['5', '<b>Keep sets hard as you get stronger</b> (progressive overload, load ≥ ~30% of max)',
  'Add weight or add reps — both work equally. Any load from ~30% of max upward grows muscle if sets are hard; '
  'heavier builds more strength.', 'Moderate'],
]
s.append(grid(top, [W * 0.05, W * 0.27, W * 0.53, W * 0.15], shades=[(1, GOOD), (2, GOOD), (3, MID), (4, MID), (5, MID)]))
s.append(Spacer(1, 4))
s.append(para('<b>Effort or volume first?</b> The agents split. The effort agent ranks effort first because a set far '
              'from failure barely counts at all. The auditor ranks volume first because, among lifters who already '
              'train hard, adding sets moves growth more than going from 2 reps short to failure. They are both right: '
              '<b>effort is the gate, volume is the dial.</b> Factors 4 and 5 are best read as rules that protect 1 and '
              '2, not as separate levers — rest works through volume, progression works through effort.', P))
s.append(para('What surprised us', H2))
s += bullets([
    '<b>Tempo, time under tension, pauses, squeezing, slow eccentrics, drop sets, rest-pause, supersets</b> — none '
    'changes growth in trained lifters in any trial found. Several viral claims fell apart on checking (Part 3).',
    '<b>“Lengthened partials beat full range”</b> is not supported in trained lifters. Every trained-lifter test was '
    'null or trivial. The real rule is “don’t train only the short half”.',
    '<b>Protein</b> (~1.6 g/kg/day) has a clearer effect than several working-set factors but is outside this brief.',
])
s.append(para('Can TENSR track three of the five? Yes — with app and firmware only. Five needs a second puck.', H2))
s.append(grid([
 ['Factor', 'Band alone (firmware + app)', 'Add a second TENSR puck', 'Needs a new board?'],
 ['Effort', 'Your own reps-in-reserve tag; EMG fatigue trend is research-only', 'Clip it to the bar: rep speed and '
  'slow-down → personal reps-left model on barbell, Smith and machine lifts (must be validated)', 'No'],
 ['Volume', '<b>Yes</b> — counts sets and reps on the muscle wearing the band; you tag “hard”', 'Speed confirms which sets were hard', 'No'],
 ['Muscle length / ROM', 'Only where the band’s limb moves (squat, lunge, raises); can tell seated vs lying leg curl', 'Strap it to the next limb segment: a real joint angle (lab accuracy ~3–5° at the knee; untested under load)', 'No'],
 ['Rest', '<b>Yes</b> — rest timer plus next-set rep count', '—', 'No'],
 ['Progression', '<b>Yes, logged</b> — you enter weight; app tracks reps × weight and estimated max', 'Bar speed gives a strength trend without max testing', 'No'],
], [W * 0.15, W * 0.33, W * 0.38, W * 0.14], shades=[(2, GOOD), (4, GOOD), (5, GOOD)]))
s.append(PageBreak())

# ---------------- Part 2 ----------------
s.append(para('Part 2 — The five factors, one by one', H1))
def factor(num, title, conf, sections):
    out = [para('%s. %s' % (num, title), st('ft', f='DVB', fontSize=14, leading=18, c=ACC, spaceBefore=4, spaceAfter=2)),
           para('Confidence for trained lifters: <b>%s</b>' % conf, PS)]
    for h, body in sections:
        out.append(para(h, H3))
        if isinstance(body, list): out += bullets(body)
        else: out.append(para(body))
    return out

s += factor('1', 'Effort — proximity to failure', 'moderate as a threshold; weak as a dial', [
 ('What the studies show', [
   '<b>Hard sets are what make any load work.</b> Light (~30% of max) and heavy loads give similar growth only '
   'because the sets go close to failure (Schoenfeld 2017a, 21 studies; Morton 2016, 49 trained men).',
   '<b>Failure vs stopping 0–3 reps short is a small difference.</b> Refalo 2023 (15 studies): effect size 0.19 '
   '(0.00–0.37), and 0.12 (−0.13 to 0.37) when failure was defined strictly. Grgic 2022 (15 studies): 0.22 '
   '(−0.11 to 0.55).',
   '<b>Trials in trained lifters found no meaningful gap</b> between failure and 1–2 reps short: Refalo 2024 '
   '(quads +0.18 cm in both groups), Santanielo 2020, Martikainen 2025. Hermann 2025 (single set per exercise) '
   'showed a modest trend toward failure.',
   '<b>Light loads need to go closer.</b> Failure mattered at 30% of max but not at 80% (Lasevicius 2022, '
   'untrained). Robinson 2024’s meta-regression found the same pattern: proximity matters less with heavier loads.',
   '<b>Measured as bar slow-down:</b> more velocity loss gives slightly more growth (Jukic 2023: 0.006 per % '
   'point, 19 training studies) with a plateau around 20–25% velocity loss; at 40% you pay in fatigue and lose '
   'fast-twitch IIX fibres (Pareja-Blanco 2017).']),
 ('Why it works', [
   '<b>Size principle (Henneman):</b> muscle fibres are recruited small-to-large as effort rises. With light '
   'weights the biggest, most growth-prone fibres only switch on as the set gets hard (Muddle 2018; Morton 2019).',
   '<b>Force–velocity:</b> as reps slow down near failure, each active fibre shortens more slowly and carries more '
   'tension — and tension is the leading growth signal.',
   'Why failure itself adds little: by ~1–3 reps short the high-threshold fibres are already working; the last rep '
   'mainly adds fatigue.']),
 ('Fact-checked', [
   '<b>“Only the last 5 reps count” (“effective reps”)</b> is a coaching hypothesis, never directly tested. Its big '
   'predicted differences don’t appear in trials (Lacerda 2020; Santanielo 2020; Martikainen 2025).',
   'The four failure meta-analyses pool mostly the same trials — they are one body of evidence, not four.',
   'Robinson 2024’s reps-in-reserve values were estimated after the fact from study descriptions — direction '
   'credible, exact slope not.']),
 ('Intermediate / advanced specifics',
  'Lifters underestimate reps left by ~1 rep on average, with ~1.5 reps spread between people, and are worst on '
  'light, long sets (Halperin 2022) — exactly where proximity matters most. That is the opening for an objective '
  'measure.'),
 ('In practice', 'Most sets 1–3 reps short; push closer on light, high-rep sets; occasional failure on safe machine '
  'exercises is fine but not required.'),
])
s.append(PageBreak())
s += factor('1=', 'Volume — hard sets per muscle per week', 'moderate', [
 ('What the studies show', [
   '<b>Dose-response with diminishing returns.</b> Schoenfeld 2017 (15 studies): about 5.4%, 6.6% and 9.8% growth for '
   '<5, 5–9 and 10+ weekly sets. Krieger 2010: effect sizes 0.24, 0.34, 0.44 for 1, 2–3 and 4–6 sets per exercise.',
   '<b>Pelland 2026</b> (Sports Medicine; 67 studies, 2,058 participants — the biggest dose-response analysis): growth '
   'keeps rising with weekly sets but by less each time; strength plateaus sooner. Counting an indirect set (e.g. '
   'triceps on bench press) as half a set fit best. No detectable extra growth was reported beyond roughly '
   '31 fractional sets a week (cited via the Remmert 2025 preprint).',
   '<b>Only hard sets count.</b> Set counts predict growth for sets near failure in ~6–20+ reps (Baz-Valle 2021).',
   '<b>Above ~12–20 sets/week, trained-lifter trials disagree:</b> more helped in Schoenfeld 2019 (n = 34) and '
   'Brigatto 2022 (32 > 16 sets); no clear extra benefit in Heaselgrave 2019, Enes 2024, Barsuhn 2025, Räntilä 2026 '
   '(60 ≈ 40 sets). All are small, so “no difference” isn’t proof.',
   '<b>Frequency adds nothing on its own:</b> with weekly volume equal, training a muscle 1× vs 3× gives similar growth '
   '(Schoenfeld 2019, 25 studies; Pelland 2026).']),
 ('Why it works', [
   'One hard session raises muscle protein synthesis for ~24–36 h in trained men (MacDougall 1995); three sets raise '
   'it more than one (Burd 2010, acute). More weekly sets = more and longer “building windows”.',
   'Early in training much of that goes to repairing damage, not growth (Damas 2016) — so volume you can recover from '
   'counts more than heroic volume.',
   'Diminishing returns: synthesis saturates within a session, fatigue and damage rise, and at extreme volumes part of '
   'the measured “growth” may be fluid rather than contractile protein (Haun 2019, no control group).']),
 ('Fact-checked', [
   'The Barbalho group’s “volume ceiling” papers are <b>retracted</b> (men, IJSPP) and listed as retracted on PubMed '
   '(women, MSSE 2019). Excluded.',
   '“Hundreds of studies” overstates it: about 70 unique trials sit behind the volume evidence, 10–15 of them compare '
   'set counts in trained lifters.',
   'People vary a lot: only about 13 of 34 grew meaningfully more on 3 sets than 1 (Hammarström 2020).']),
 ('In practice', 'Track hard sets per muscle per week; for most trained lifters ~10–20 is a sensible working range; '
  'add sets when progress stalls and recovery allows. No universal “optimal” number.'),
])
s.append(PageBreak())
s += factor('3', 'Exercise selection & muscle length (range of motion)', 'low–moderate; mostly untrained data', [
 ('What the studies show', [
   '<b>Short top-half reps lose to full range.</b> Pallarés 2021 (16 studies): full range better for lower-body '
   'growth (ES 0.88) and strength (0.56) — though most partial groups trained the short end. Kubo 2019 squat depth: '
   'glutes +6.7% deep vs +2.2% half.',
   '<b>Exercises that load the muscle stretched grow it more</b> (untrained): seated vs lying leg curl, hamstrings '
   '+14% vs +9% (Maeo 2021, MRI); overhead vs pushdown, triceps long head +28.5% vs +19.6% (Maeo 2023).',
   '<b>Kassiano 2023 (calves, settled by the auditor):</b> medial gastrocnemius +15.2% bottom-half partials vs '
   '+6.7% full vs +3.4% top-half; lateral +14.9% vs +7.3% vs +6.2%. Untrained women.',
   '<b>“Lengthened partials beat full range” is not established:</b> Wolf 2023 meta-analysis −0.28 (−0.81 to 0.16), '
   'leaning lengthened but crossing zero. <b>Every trained-lifter test was null or trivial</b>: Wolf 2025 (n = 30), '
   'Larsen 2025 calves, a 297-person gym preprint (not peer-reviewed, size estimated not imaged).',
   'Different exercises grow different regions of a muscle (Plotkin 2023; Maeo 2021/2023) — but a 2025 meta-analysis '
   '(Varovic, 12 studies) found regional effects small overall.']),
 ('Why it works', [
   'At long lengths a muscle carries active <i>and</i> passive tension (the spring protein titin), so total tension '
   'per rep may be higher — plausible, not proven in humans.',
   'Animal stretch models show large growth (birds +53% to +318%) — animal evidence only. In humans, plain '
   'stretching gives a small effect (Warneke 2024: 42 studies, ES 0.20) at long daily doses.',
   'Maeo 2023’s triceps heads that don’t cross the shoulder also grew more overhead, so length isn’t the whole story.']),
 ('Fact-checked', [
   '“Long length doubles growth” is cherry-picked from single regions vs short-range partials in beginners. '
   'Whole-muscle gains are ~1.3–1.5×.',
   'Goto 2019’s “+49% vs +28% partial wins” traces to a forum post and blood-flow effects, not length — treated as an '
   'outlier.']),
 ('In practice', 'Use full range or the stretched half; include at least one exercise per muscle that loads it at long '
  'length; rotate exercises to cover regions.'),
])
s.append(PageBreak())
s += factor('4', 'Rest long enough to keep your reps', 'low–moderate', [
 ('What the studies show', [
   'Singer 2024 (Bayesian meta-analysis, 9 studies, mostly untrained): a small benefit for resting more than 60 s; '
   'nothing appreciable beyond 90 s.',
   '<b>Longo 2022 (n = 28, one leg per protocol) tests the mechanism:</b> ~13% growth whenever volume load was high, '
   'whether rest was 1 or 3 min; ~7% when it was low.',
   'Trained lifters: 3 min beat 1 min with sets matched (Schoenfeld 2016, n = 21 — the 1-min group lifted less '
   'volume); 2 min ≈ 5 min (Ahtiainen 2005). Longer than 2 min helps maximal strength (Grgic 2018).']),
 ('Why it works', 'Short rest cuts the reps you can do on the next set — less total hard work. Rest isn’t a growth '
  'signal itself; it protects volume and effort.'),
 ('Fact-checked', '“3 minutes grows more muscle” overstates Schoenfeld 2016: one measurement site was significant and '
  'the volumes differed. One trial (Souza-Junior 2011) doesn’t fit the volume explanation.'),
 ('In practice', '≥ 90 s generally, 2–3 min on heavy compound lifts. If you rest less, add sets to make up the lost reps.'),
])
s.append(Spacer(1, 6))
s += factor('5', 'Keep sets hard as you get stronger (progressive overload, adequate load)', 'moderate–strong for load; limited for progression method', [
 ('What the studies show', [
   '<b>Load barely matters for growth across ~30–85%+ of max when sets are hard</b>: Schoenfeld 2017a (21 studies), '
   'Lopez 2021 (28 studies, 747 people), Currier 2023 (network meta-analysis). Trained lifters: Morton 2016 (n = 49), '
   'Cumming 2025 (3–5RM ≈ 20–25RM). Heavier = more strength. Below ~20–30% growth may suffer (Lasevicius 2018/2022, untrained).',
   '<b>How you progress doesn’t matter:</b> adding load vs adding reps gave similar growth in trained lifters '
   '(Plotkin 2022, n = 43) and untrained (Chaves 2024).',
   'Periodisation: no growth effect (Moesgaard 2022, 35 studies, ES 0.13, −0.10 to 0.36) but helps strength. Deload: '
   'one trial, no growth difference (Coleman 2024).',
   'No trial compares progression vs no progression with effort held equal — progression is how you <i>keep</i> sets hard.']),
 ('Why it works', 'Mechanical tension on high-threshold fibres is the leading stimulus (mechanism shown acutely in '
  'humans, causally in mice — Drummond 2009; Goodman 2011). As you adapt, the same weight sits further from failure; '
  'progression restores effort.'),
 ('Fact-checked', '“Light weights beat heavy” (Burd 2010) rested on a 24-hour protein-synthesis spike, not growth; '
  'long-term trials show equal growth.'),
 ('In practice', 'Log weight and reps; when you beat your rep target at a weight, add weight or reps. Any rep range '
  'you can push hard works; go heavier if strength is a goal.'),
])
s.append(PageBreak())

# ---------------- Part 3 ----------------
s.append(para('Part 3 — What didn’t make the top five, and why', H1))
miss = [
 ['Idea', 'What trained-lifter evidence shows', 'Key evidence'],
 ['Tempo / time under tension', 'No effect anywhere from 0.5 to 8 s per rep. Only very slow (&gt;10 s) reps may be worse.', 'Enes 2025 (14 RCTs, ES 0.09, −0.04 to 0.22); Schoenfeld 2015 (8 studies)'],
 ['Slow / emphasised eccentrics', 'More strength, same size.', 'Silva 2025 (26 studies, ES 0.29 n.s., very low certainty); Amdi &amp; King 2025 (g = 0.05); Walker 2016'],
 ['Pause reps', 'No long-term trial exists.', '—'],
 ['Peak-contraction squeeze', 'No long-term trial; one small inter-set flexing study.', 'Schoenfeld 2020'],
 ['Drop sets, supersets, rest-pause, cluster sets, myo-reps', 'Save time; same growth.', 'Davies 2021 (29 studies); Coleman 2022; Sødal 2023; Enes 2021 (n = 28 trained) — Prestes 2019’s rest-pause win didn’t replicate'],
 ['Cheat reps', 'Similar growth, more weight moved — one untrained trial with influencer co-authors.', 'Augustin 2025'],
 ['Machines vs free weights', 'Similar growth.', 'Haugen 2023 (13 studies, SMD −0.06)'],
 ['Training frequency', 'No effect once weekly volume is equal.', 'Schoenfeld 2019; Pelland 2026'],
 ['Periodisation, deloads', 'No growth effect; periodisation helps strength.', 'Moesgaard 2022; Coleman 2024'],
 ['More fatigue / “burn”', 'Changing fatigue without changing effort didn’t change growth.', 'Davies 2021; Refalo 2024; Pareja-Blanco 2017'],
 ['More EMG / “activation”', 'More EMG did not mean more growth in the only direct test.', 'Plotkin 2023; Vigotsky 2018/2022; Morton 2019'],
 ['Protein (outside this brief)', 'Modest real effect up to ~1.6 g/kg/day; larger in trained people.', 'Morton 2018 (49 RCTs, 1,863 people); Nunes 2022'],
]
s.append(grid(miss, [W * 0.24, W * 0.40, W * 0.36]))
s.append(PageBreak())

# ---------------- Part 4 ----------------
s.append(para('Part 4 — How TENSR could track the five', H1))
s.append(para('What the current board can and can’t do (checked against the circuit-board file)', H2))
s.append(grid([
 ['Part', 'As built', 'Without a new board', 'Needs a new board'],
 ['EMG chip (ADS1292R)', 'One channel used; channel 2 inputs tied off', 'EMG at 2,000 samples/s; chip temperature', 'A second EMG pair; bioimpedance'],
 ['Motion sensor (LSM6DSO)', '6-axis, compass port tied to ground', 'High-rate motion (up to 6.6 kHz) for vibration research', 'Reading an external compass through the sensor (not recommended — steel racks distort it)'],
 ['Expansion header J3', '3.3 V, ground, I2C, two spare pins — top side', 'Add-on I2C sensors, a force sensor on a spare pin', 'Anything that must touch the skin'],
 ['ESP32-S3 Bluetooth', 'BLE to phone', 'BLE link to a <b>second puck</b>', '—'],
], [W * 0.19, W * 0.25, W * 0.28, W * 0.28]))
s.append(para('The roadmap, in three levels', H2))
lv = [
 ['Level', 'What’s added', 'Factors tracked', 'Board change?'],
 ['<b>A — firmware + app</b>', 'Rep/set/rest detection at 2 kSPS; manual weight entry; your reps-in-reserve tag; exercise-to-muscle map (half-sets for helper muscles)', '<b>3 of 5:</b> volume (counted), rest (timed), progression (logged). Effort only by your tag.', 'None'],
 ['<b>B — second TENSR puck as a clip</b>', 'Same board, new firmware modes: <b>bar clip</b> (rep speed and slow-down), <b>limb clip</b> (joint angle with the first puck)', '<b>4–5 of 5:</b> + effort on barbell/Smith/machine lifts via a personal speed-to-reps-left model; + range of motion via joint angle', 'None'],
 ['<b>C — phone camera</b>', 'Bar-speed or pose tracking in the app', 'Backup for effort and ROM without a second puck', 'None'],
 ['<b>v2/v3 — new board</b>', 'Second EMG pair (orientation backup); A-mode ultrasound for muscle thickness', 'Better EMG; ultrasound is the only route to measuring <i>growth itself</i> (research)', 'Yes'],
]
s.append(grid(lv, [W * 0.19, W * 0.36, W * 0.33, W * 0.12], shades=[(1, GOOD), (2, MID), (3, RES), (4, BAD)]))
s.append(para('Factor by factor', H2))
fx = [
 ['Factor', 'How TENSR would read it', 'Evidence that this can work', 'Honest limits'],
 ['Effort', 'Second puck on the bar measures each rep’s speed; slow-down within a set, matched to your own calibration sets taken to failure, estimates reps left.',
  'Personal speed models got under 2 reps of error in 46 trained lifters — <b>back squat only</b> (Jukic 2024). Commercial bar sensors like Vmaxpro agree with lab equipment (reliability ICC ~0.55–0.91 depending on lift; Held 2021).',
  'TENSR’s own speed algorithm is untested. No validation found for dumbbells, cables or isolation lifts. Needs calibration sets to failure per exercise. Must beat your own corrected guess (~1–1.5 reps).'],
 ['Volume', 'EMG bursts + motion count reps and sets on the muscle; you tag effort or the bar clip confirms it; app counts half-sets for helper muscles.',
  'Wrist motion sensors count reps within ±1 in ~91–93% of sets.', 'No study of rep counting from an upper-arm or thigh band yet; one band sees one muscle.'],
 ['Muscle length / ROM', 'One puck: angle of its own limb segment. Two pucks (one per segment): joint angle each rep, flagging reps that shorten near failure.',
  'Two motion sensors give knee angle within ~3–5° and elbow ~1–7° in lab studies.', 'Not yet tested under load with sweat and strap shift. One puck is blind on curls, pushdowns, leg extensions.'],
 ['Rest', 'Timer starts at the last rep; next set’s reps tell you whether rest protected volume.', 'Direct measurement.', '“Your muscle has recovered” is not validated — keep it a timer.'],
 ['Progression', 'You enter the weight; app tracks weight × reps and estimated max. With the bar clip: speed at a given weight tracks strength.',
  'Load–velocity profiles are established for compound barbell lifts.', 'The band cannot sense the weight. Weight-stack recognition needs a magnetometer — dropped.'],
]
s.append(grid(fx, [W * 0.13, W * 0.31, W * 0.30, W * 0.26]))
s.append(para('Also important: muscle length changes the EMG reading on its own', H3))
s.append(para('EMG frequency and amplitude move with joint angle even with no fatigue. If you change your range of '
              'motion between sets, TENSR’s fatigue number would move for no real reason. Tracking range of motion '
              '(Level B) keeps the EMG fatigue trend honest, not just coaching.', P))
s.append(para('What TENSR could honestly claim — after its own validation', H2))
s += bullets([
    '“Counts your sets and reps and times your rest.”',
    '“Measures bar speed and slow-down on barbell, Smith and machine lifts” (with a second puck).',
    '“Estimates reps in reserve on compound lifts <b>after you calibrate that exercise</b> — typical error up to ~2 reps.”',
    '“Logs the weight you enter and tracks your progression.”',
])
s.append(para('Not defensible:', H3))
s += bullets([
    '“Knows when you’re near failure” on isolation lifts; any speed claim on dumbbells or cables (untested).',
    '“Identifies the weight”; “measures muscle tension”; “your muscle has recovered”.',
    'An “optimal” weekly sets, tempo, fatigue or time-under-tension target; any growth or stimulus score.',
])
s.append(para('One trade-off to decide', H3))
s.append(para('A pair of pucks can either cover two muscles or have one on a muscle and one on the bar or next limb — '
              'not both at once. The $429 pair can be sold for either use, but marketing must not promise both '
              'simultaneously.', P))
s.append(PageBreak())

# ---------------- Part 5 ----------------
s.append(para('Part 5 — Fact-check log: what the auditor corrected', H1))
s.append(grid([
 ['Item', 'Correction'],
 ['Kassiano 2023 (calves)', 'Two heads had been mixed up across three agents. Settled: medial +15.2 / +6.7 / +3.4%; lateral +14.9 / +7.3 / +6.2% (bottom-half / full / top-half). Bottom-half beat full for the medial head (p ≤ 0.009).'],
 ['Weight-stack recognition', 'The 97.5% study used a magnetometer TENSR doesn’t have. Dropped from the plan.'],
 ['Barbalho volume papers', 'Men’s paper retracted; women’s paper listed as retracted on PubMed. Excluded.'],
 ['Pelland 2026', '67 studies / 2,058 participants confirmed. The DOI is still not confirmed by an exact search. Diminishing returns past ~31 fractional sets/week added.'],
 ['Goto 2019', 'The headline +49% vs +28% traces to a forum post. Treated as an outlier.'],
 ['Vmaxpro (Held 2021)', 'Only the best-case agreement had been quoted; the range is ICC 0.55–0.91.'],
 ['Jukic 2024', 'Validated on the back squat only — not on isolation lifts.'],
 ['Load ceiling “85%”', 'No evidence for an upper load limit for growth; Cumming 2025 found 3–5RM ≈ 20–25RM.'],
 ['Board facts', 'Confirmed from the board file: compass port tied to ground; J3 pins; EMG channel 2 tied off.'],
], [W * 0.25, W * 0.75]))
s.append(para('Disagreements kept open', H2))
s += bullets([
    '<b>Effort vs volume as #1</b> — presented as joint first (gate vs dial).',
    '<b>Is there a real 4th and 5th factor?</b> The auditor argues rest and progression are rules that protect volume '
    'and effort, not independent levers. Protein would rank higher on pure effect but is outside the working-set brief.',
    '<b>Does training at long lengths matter for trained lifters?</b> Plausible mechanism, positive in beginners, null '
    'in every trained test so far.',
])

# ---------------- Part 6 ----------------
s.append(para('Part 6 — How many studies, honestly', H1))
names = dict([('F1', 'Effort / proximity to failure'), ('F2', 'Volume and frequency'), ('F3', 'Muscle length and range of motion'),
          ('F4', 'Load, tension and rep execution'), ('F5', 'Rest, recovery and progression'),
          ('F6', 'Sensing and measurement validation'), ('FA', 'Added by the auditor')])
fcount = collections.Counter(names[r['found_by'].split(';')[0]] for r in studies)
s.append(para('This round recorded <b>%d unique studies</b>, of which <b>%d</b> are meta-analyses or systematic reviews '
              'and <b>%d</b> were independently re-checked by the auditor. The meta-analyses pool several hundred '
              'trials between them, but they overlap heavily — the four failure meta-analyses share most of their '
              'trials, and about 70 unique trials sit behind the volume evidence. Every study in this report was '
              'checked from abstracts or summaries; none was read in full text.' % (n_all, n_meta, n_aud), P))
s.append(grid([['Area', 'Studies recorded']] + [[k, str(v)] for k, v in fcount.most_common()], [W * 0.5, W * 0.2]))
s.append(Spacer(1, 6))
s.append(para('<b>To go deeper:</b> allow pmc.ncbi.nlm.nih.gov, pubmed.ncbi.nlm.nih.gov, doi.org and api.crossref.org in '
              'the environment’s network settings, so agents can read full papers and the per-set numbers in Pelland '
              '2026. A recurring scheduled search can then add new trials as they are published.', P))

# ---------------- Part 7 ----------------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 24 * mm
s.append(para('Part 7 — Every study recorded (%d)' % n_all, H1))
s.append(para('Grouped by research area. <b>Checked</b> is the auditor’s verdict where the study was re-checked; '
              '“not sampled” means it was not. <b>Access</b> says how much of the paper could be seen. Full detail is in '
              'TOP5-STUDIES.csv.', PS))
groups = [('F1', 'Effort / proximity to failure'), ('F2', 'Volume and frequency'), ('F3', 'Muscle length and range of motion'),
          ('F4', 'Load, tension and rep execution'), ('F5', 'Rest, recovery and progression'),
          ('F6', 'Sensing and measurement'), ('FA', 'Added by the auditor')]
cw = [LW * x for x in (0.24, 0.14, 0.27, 0.19, 0.08, 0.08)]
for code, title in groups:
    g = [r for r in studies if r['found_by'].split(';')[0] == code]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [[Paragraph(x, TB) for x in ['Study', 'Design · who', 'Result', 'Why it works / note', 'Access', 'Checked']]]
    for r in g:
        cit = '<b>%s</b><br/>%s' % (esc(r['key']), esc(r['citation']))
        if r['doi_or_link']: cit += '<br/><font color="#5a6370">%s</font>' % esc(r['doi_or_link'][:110])
        data.append([Paragraph(cit, T),
                     Paragraph('%s<br/>%s<br/>%s<br/>%s' % (esc(r['design']), esc(r['n_studies_or_participants']),
                                                            esc(r['trained_status']), esc(r['outcome_measure'])), T),
                     Paragraph(esc(r['result_effect_uncertainty']), T), Paragraph(esc(r['mechanism_note']), T),
                     Paragraph(esc(r['access']), T), Paragraph(esc(r['audit_verdict'][:160]), T)])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('BACKGROUND', (0, 0), (-1, 0), BAND), ('LEFTPADDING', (0, 0), (-1, -1), 3),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 3), ('TOPPADDING', (0, 0), (-1, -1), 2),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                           ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafbfc')])]))
    s.append(t)

doc.build(s)
print('ok', OUT, n_all, n_meta, n_aud, dict(fcount))
