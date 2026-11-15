"""Builds FAT-LOSS-REPORT.pdf from the fat-loss research round (W1-W6 + WA audit)."""
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

R = '/home/user/tenstresearch/fatloss/'
OUT = R + 'FAT-LOSS-REPORT.pdf'
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
    c.drawString(15 * mm, 9 * mm, 'Fat loss and regional fat · 4 Nov 2026 · research summary, not medical advice')
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='Fat Loss Research Report',
                      author='TENSR research team (Claude Code)',
                      subject='Fat loss for trained lifters: energy balance, carbs, fasted cardio, spot reduction and regional fat')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(12 * mm, 14 * mm, lw - 24 * mm, lh - 26 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm
studies = list(csv.DictReader(open(R + 'FATLOSS-STUDIES.csv')))
n_all = len(studies); n_aud = sum(1 for r in studies if r['audit_verdict'] != 'not sampled')
s = []

def verdict_table(rows):
    shade = {'Right': GOOD, 'Mostly right': GOOD, 'Partly right': MID, 'Wrong': BAD, 'Most likely': MID}
    sh = []
    for i, r in enumerate(rows[1:], 1):
        for k, v in shade.items():
            if r[1].startswith(k): sh.append((i, v)); break
    return grid(rows, [W * 0.30, W * 0.16, W * 0.54], shades=sh)

# ---------------- cover ----------------
s += [Spacer(1, 34 * mm), para('RESEARCH REPORT', st('k', f='DVB', fontSize=11, c=ACC, leading=14)),
      para('Losing fat while keeping muscle — what the studies actually show', H0),
      para('Energy deficits, “carbs first, then fat”, fasted cardio, carb cycling, spot reduction, and why your arms '
           'can read fatter than your belly or chest. Your model, tested claim by claim against the research.', SUB),
      Spacer(1, 6 * mm)]
s.append(box(para(
    '<b>Inside</b><br/>'
    '<b>1</b> The answer in one page · <b>2</b> Your model, claim by claim · <b>3</b> How fat is actually burned · '
    '<b>4</b> The deficit: how big? · <b>5</b> Fasted cardio · <b>6</b> Carbs, carb cycling and being “flat” · '
    '<b>7</b> Spot reduction · <b>8</b> Why your arms read fatter than your belly or chest · <b>9</b> Measuring '
    'fat properly · <b>10</b> Training and lifestyle while cutting · <b>11</b> The plan · <b>12</b> Fact-check log · '
    '<b>13</b> Every study (%d)' % n_all, CALL)))
s += [Spacer(1, 6 * mm), box(para(
    '<b>How this was done.</b> Six research agents (energy balance; fasted cardio and carb cycling; spot reduction; '
    'regional fat biology; exercise strategy; measurement) searched on 4 Nov 2026, then an independent auditor '
    're-checked %d studies and all the arithmetic. <b>Limits:</b> full papers could not be opened (PubMed and PMC were '
    'blocked), so everything was checked at abstract or summary level. No citation was found to be made up; one '
    'retracted paper was identified and excluded. Many diet studies are in people with overweight rather than lean '
    'lifters — the mechanisms carry over; exact effect sizes may not. This is a research summary, not medical advice.'
    % n_aud, PS), bg=WARN)]
s.append(PageBreak())

# ---------------- Part 1 ----------------
s.append(para('Part 1 — The answer in one page', H1))
s += bullets([
    '<b>You’re right that the deficit is what drives fat loss.</b> Over weeks, fat lost tracks the energy gap. At equal '
    'calories, low-carb vs high-carb makes almost no difference.',
    '<b>Your deficit is on the small side.</b> 200–300 kcal/day is at most ~0.2–0.3 kg of fat a week — about the size '
    'of normal calorie-logging error, so you may not actually be in a deficit. A better default is ~0.5% of '
    'bodyweight a week (~450–500 kcal/day at 85 kg), set from your weekly average morning weight, not a calculator.',
    '<b>“Glucose first, then fat” is not how the body works.</b> You burn fat and carbs at the same time, all day. At '
    'rest and in moderate exercise, fat supplies most of the energy even with full glycogen. Exercise intensity sets '
    'the mix — not whether glycogen is empty. A lifting session only uses ~24–40% of muscle glycogen anyway.',
    '<b>Burning more fat in a session ≠ losing more body fat.</b> Fasted cardio burns ~3 g more fat per session, but '
    'fat loss over weeks is the same fasted or fed. In a metabolic ward, low-carb raised fat burning yet removed '
    '<i>less</i> body fat than low-fat at the same calories.',
    '<b>Being “flat” is glycogen plus water, not a fat-burning state.</b> Low-carb rest days lose no extra fat at '
    'the same weekly calories. Putting carbs around hard sessions is fine for performance.',
    '<b>You can’t spot-reduce arms or legs.</b> A meta-analysis of 13 studies (1,158 people) found no effect; training '
    'one arm for 12 weeks took fat off both arms equally (MRI). For the belly, a small effect isn’t ruled out — a few '
    'hundred grams at most.',
    '<b>Your arms probably aren’t really fatter.</b> In 852 young men measured by DXA, the arm was the <i>leanest</i> '
    'region. An “arms fatter than belly” reading most likely comes from a smart scale or InBody, or from how a '
    'percentage works on a thin limb vs a thick torso. Belly fat in men also hides inside the abdomen, where a pinch '
    'or the mirror can’t see it.',
])
s.append(PageBreak())

# ---------------- Part 2 ----------------
s.append(para('Part 2 — Your model, claim by claim', H1))
s.append(verdict_table([
 ['Your claim', 'Verdict', 'Why'],
 ['Fat loss = a 200–300 kcal/day deficit', 'Right in kind, small in size', 'Energy deficit is the driver (strong). '
  '200–300 kcal is the slow end and as small as logging error, so check it against your weekly weight trend.'],
 ['Carbs are the #1 fuel; only when glucose is “flattened” does the body burn fat', 'Wrong as a mechanism', 'Fat is '
  'burned continuously; intensity and recent meals shift the mix. The short-term shift is real, but it doesn’t change '
  'fat lost over weeks (strong).'],
 ['That’s why fasted cardio works', 'Wrong for fat loss', 'More fat burned during the session, same fat lost over '
  '4–6 weeks (limited–moderate; small trials).'],
 ['Lifters need carbs to fuel sessions', 'Partly right', 'Mainly for high-volume sessions or instead of training '
  'fasted; little effect at normal volumes when fed (moderate).'],
 ['Low-carb rest days to be “flat” burn more fat', 'Wrong', 'No trial shows extra fat loss at equal weekly calories; '
  '“flat” is glycogen and water (limited–moderate).'],
 ['You can lose fat from specific limbs', 'Wrong', 'Strong evidence against for arms and legs; belly uncertain and tiny.'],
 ['My arms carry more body-fat % than my belly/chest', 'Most likely a measurement artefact', 'Device or percentage '
  'maths; belly fat in men is often internal (moderate).'],
]))

# ---------------- Part 3 ----------------
s.append(para('Part 3 — How fat is actually burned', H1))
s += bullets([
    '<b>Fat supplies most energy at rest</b> after an overnight fast, and most of the fuel at 25% and 65% of maximum '
    'aerobic capacity — with glycogen still full (Romijn 1993). Fat burning peaks around 64% of max (Achten 2002).',
    '<b>The “crossover” idea</b> (Brooks &amp; Mercier 1994): as exercise gets harder, the mix shifts toward carbs. '
    'That’s intensity, not an empty tank.',
    '<b>Lifting never empties glycogen:</b> a session drains about 24–40%; more sets drain more, trained lifters less '
    '(2025 meta-analysis, 20 studies).',
    '<b>Why burning more fat now doesn’t mean losing more fat:</b> your body matches the carbs it burns to the carbs '
    'you eat. Any overall energy surplus or deficit ends up in or out of the fat store — so over days and weeks, fat '
    'balance follows energy balance (Flatt; Schutz 1989).',
    '<b>The decisive test (Hall 2015, metabolic ward, n = 19):</b> with calories matched, cutting carbs raised fat '
    'burning and lowered insulin — but removed less body fat than cutting fat (53 vs 89 g/day). A keto ward study '
    '(Hall 2016) found fat loss slowed when fat burning rose. Pooled controlled-feeding studies found under 20 g/day '
    'difference either way (Hall &amp; Guo 2017).',
    '<b>Real-world diets:</b> in the year-long DIETFITS trial (609 people) low-fat lost 5.3 kg and low-carb 6.0 kg — '
    '0.7 kg apart (CI −0.2 to 1.6).',
])
s.append(para('<b>Mechanism in plain words:</b> fat cells release and re-store fat all day. You lose fat when, over '
              'the day, more leaves than comes back — which happens when you eat less energy than you use. Which '
              'fuel you burned in the gym an hour ago is washed out by what you eat afterwards.', P))
s.append(PageBreak())

# ---------------- Part 4 ----------------
s.append(para('Part 4 — The deficit: how big?', H1))
s.append(grid([
 ['Daily deficit (85 kg man)', 'Fat loss per week (approx.)', '% bodyweight per week', 'Notes'],
 ['200–300 kcal', '0.15–0.27 kg', '0.2–0.3%', 'Gentle on muscle, but as small as calorie-logging error and partly '
  'absorbed by metabolic adaptation — may not show'],
 ['450–500 kcal', '~0.4 kg', '~0.5%', '<b>Recommended default</b> for lean trained lifters'],
 ['~650 kcal', '~0.6 kg', '~0.7%', 'Upper end; watch strength'],
 ['&gt;850 kcal', '&gt;0.75 kg', '&gt;1%', 'Faster; more risk to muscle'],
], [W * 0.22, W * 0.20, W * 0.18, W * 0.40], shades=[(2, GOOD)]))
s.append(para('Range uses 7,700 kcal/kg (scale weight) to ~9,400 kcal/kg (pure fat).', PS))
s += bullets([
    '<b>Slower protects muscle better:</b> elite athletes losing ~0.7%/week gained 2.1% lean mass vs none when losing '
    '~1.0%/week (Garthe 2011) — the slow group also dieted longer, and 12-month results didn’t differ.',
    'Lean-mass gains stop at roughly a 500 kcal/day deficit (Murphy &amp; Koehler 2022, a regression estimate that has '
    'been criticised).',
    'Huovinen 2015 is often quoted as “300 kcal does nothing”, but that group never showed a real reduction in intake — '
    'so it doesn’t test a 300 kcal deficit.',
    '<b>Your body adapts:</b> in CALERIE, daily energy use fell beyond what body-size change explains (−431 and −240 '
    'kcal/day at 3 and 6 months) in the diet-only groups; the diet-plus-exercise group didn’t show this.',
    '<b>Practical rule:</b> weigh every morning, compare 7-day averages, and adjust by 100–200 kcal/day every 2–3 weeks '
    'if the trend misses ~0.5%/week.',
])

# ---------------- Part 5 ----------------
s.append(para('Part 5 — Fasted cardio', H1))
s += bullets([
    '<b>During the session:</b> fasted exercise burns ~3 g more fat (95% CI ~0.8–5.4 g; Vieira 2016 meta-analysis).',
    '<b>Over 24 hours:</b> exercise before breakfast raised 24-h fat burning from 456 to 717 kcal (Iwayama 2015, 10 men, '
    'one day, at energy balance).',
    '<b>Over weeks:</b> no extra fat loss — Schoenfeld 2014 (20 women, in a deficit, 4 weeks), Gillen 2013, Hackett &amp; '
    'Hagstrom 2017 (5 studies, 96 people; only body-mass differences were reported between groups).',
    '<b>Best-case ceiling:</b> even if none of those 3 g were offset, that’s about half a kilo of fat a year.',
    '<b>Verdict:</b> do cardio when it suits you. Don’t train fasted to “burn fat”. Lifting fasted is where carbs most '
    'clearly help performance.',
])
s.append(PageBreak())

# ---------------- Part 6 ----------------
s.append(para('Part 6 — Carbs, carb cycling and being “flat”', H1))
s += bullets([
    '<b>Do lifters need carbs?</b> A review of 49 studies (Henselmans 2022) found carbs had little effect on fed '
    'lifting up to about 10 sets per muscle per session. Benefits appear in high-volume sessions and against training '
    'fasted.',
    '<b>Carb cycling for fat loss:</b> no peer-reviewed trial in lifters at matched weekly calories was found. The '
    'mechanism (Part 3) says it shouldn’t matter. It’s a legitimate way to <i>place</i> carbs around training or to '
    'make a diet easier to stick to.',
    '<b>What “flat” is:</b> low muscle glycogen and the water stored with it (≥3 g water per g glycogen). Whole-body '
    'swings of ~1.6–3 kg are possible — equal to 3–5 weeks of fat loss at a 250 kcal deficit. Carb-loading measurably '
    'thickened muscle on ultrasound in bodybuilders.',
    '<b>Staying flat for long may backfire:</b> low glycogen is one of the signals that helps slow metabolism early in '
    'a diet.',
    '<b>Refeeds and diet breaks:</b> no extra fat loss in trained people (ICECAP, 61 people: same fat loss, less '
    'hunger). The big MATADOR benefit was in obese untrained men. Useful for adherence.',
    '<b>Time-restricted eating:</b> strength and muscle were kept in lifters; any modest extra fat loss (≈1.5 kg) is '
    'likely from eating less.',
    '<b>Keto:</b> short-term strength kept; “lean mass loss” is partly water; keto groups usually just ate less.',
    '<b>Protein matters more than carb timing:</b> 1.6 g/kg is the floor; while dieting aim for 2.0–2.4 g/kg '
    'bodyweight (about 170–205 g at 85 kg).',
])

# ---------------- Part 7 ----------------
s.append(para('Part 7 — Spot reduction', H1))
s.append(grid([
 ['Region', 'Key evidence', 'Verdict'],
 ['Arms', 'Kostek 2007: 104 people trained one arm 12 weeks; MRI showed equal fat loss in both arms. Child tennis '
  'players: same fat in racket and non-racket arm (MRI).', '<b>No spot reduction</b>'],
 ['Legs', 'Ramírez-Campillo 2013: ~1,000 leg-press reps per session on one leg — no significant fat loss in that leg; '
  'arms lost 10%, trunk 7%. Walts 2008 (181 people): no change.', '<b>No spot reduction</b>'],
 ['Abdomen', 'Katch 1984 (5,004 sit-ups; fat cells shrank equally everywhere), Vispute 2011, Kordi 2015: nothing. '
  'Brobakken 2023 (16 men) and Paoli 2021 (14–18 people) claim a small effect.', '<b>Unresolved; tiny if real</b> — a '
  'few hundred grams'],
 ['Pooled', 'Ramírez-Campillo 2022 meta-analysis: 13 studies, 1,158 people, g = −0.03 (−0.10 to 0.05)', '<b>No effect</b>'],
], [W * 0.13, W * 0.62, W * 0.25], shades=[(1, BAD), (2, BAD), (3, MID), (4, BAD)]))
s.append(para('Why it doesn’t work', H3))
s.append(para('Fat right next to a working muscle does get more blood flow and releases more fat <i>during</i> the '
              'session (Stallknecht 2007; Heinonen PET studies). But that fat is burned anywhere in the body, and the '
              'spot refills from food afterwards. Where fat is stored is set by hormones and genes, not by which '
              'muscle you trained. Skinfolds can make spot reduction look real because a growing muscle stretches '
              'the fat over it.', P))
s.append(para('Gadgets and procedures', H3))
s += bullets([
    '<b>Ab EMS belts:</b> strength up, no fat change (Porcari 2005).',
    '<b>Sauna suits and wraps:</b> water loss only. <b>Fat-burning creams:</b> small old studies measuring girth only.',
    '<b>Fat freezing (cryolipolysis):</b> removes ~10–25% of the treated fat layer; rarely, the area grows instead.',
    '<b>Liposuction:</b> total fat came back within a year, mostly to the upper belly (Hernandez 2011).',
])
s.append(PageBreak())

# ---------------- Part 8 ----------------
s.append(para('Part 8 — Why your arms read fatter than your belly or chest', H1))
s.append(para('Ranked from most to least likely, with how to check each:', P))
s.append(grid([
 ['#', 'Explanation', 'How to check'],
 ['1', '<b>The device.</b> Smart scales and InBody don’t measure fat — they model it from electrical resistance. The '
  'arms make up ~half the body’s resistance but ~11% of its lean mass; the trunk ~10% of resistance but ~half the '
  'lean mass, so trunk fat is barely sensed (Bracco 1996). Foot-only scales never pass current through your arms — '
  'their arm figure is a guess. Readings shift ~1 kg after upper-body training and with water.',
  'Does it have hand electrodes? Re-test 3 mornings, fasted, no training for 12–24 h. If the arm number jumps around, '
  'ignore it.'],
 ['2', '<b>The percentage maths.</b> A segment’s % = fat ÷ everything in that segment. The same 6 mm fat layer is '
  '~18% of a 40 cm arm but ~9% of an 85 cm waist. DXA also counts organs, gut and blood as trunk “lean”, pulling '
  'trunk % down.', 'Compare fat thickness in <b>mm</b> (skinfolds or ultrasound), or DXA fat in <b>kg</b>, not %.'],
 ['3', '<b>Belly fat in men is largely inside the abdomen</b> (visceral). It doesn’t show in a pinch or the mirror.',
  'Waist circumference; DXA visceral-fat estimate.'],
 ['4', '<b>Where you are in the cut.</b> In dieting men, trunk and visceral fat often come off faster early; that edge '
  'shrinks as loss continues (Chaston &amp; Dixon 2008). In Army Rangers, every region including arms lost about '
  'half its fat (Nindl 1996) — “limb fat goes last” is the authors’ interpretation, weakly supported.',
  'Repeat measurements over the cut.'],
 ['5', '<b>Genuine individual pattern.</b> Fat distribution is strongly inherited (~0.4–0.9). But arm % above trunk % on '
  'DXA would be unusual: in 852 young men the arm was the leanest region.', 'Only if a proper DXA confirms it; then a '
  'GP check of hormones is reasonable.'],
 ['6', '<b>“Stubborn” arm fat cells.</b> Fat depots do differ in how readily they release fat, but no human study of '
  'the upper-arm depot exists.', 'Not actionable.'],
], [W * 0.05, W * 0.60, W * 0.35], shades=[(1, MID), (2, MID)]))
s.append(para('<b>What to do about it:</b> lose total body fat — your arms will lean out with everything else. Train '
              'arms for muscle: a bigger muscle under the same fat looks leaner and reads lower on DXA %.', P))

# ---------------- Part 9 ----------------
s.append(para('Part 9 — Measuring fat properly', H1))
s.append(grid([
 ['Method', 'Good for', 'Watch out for'],
 ['Morning weight, 7-day average', 'The trend that matters', 'Daily swings of glycogen and water bigger than a week of fat loss'],
 ['Waist tape, weekly', 'Belly fat including internal fat', 'Same spot, same time of day'],
 ['Skinfolds or B-mode ultrasound (mm)', 'Comparing sites (triceps vs abdomen) every 2–4 weeks', 'Same trained '
  'tester; skinfold technique varies'],
 ['DXA every 8–12 weeks', 'Regional fat in kg', 'Arm fat is DXA’s least precise region (CV ~3–8%); a real change needs '
  '~9–11% of that region’s fat. Eating before the scan shifts readings; multi-day carb loading moved lean mass ~3%. '
  'Scan fasted, no training that day.'],
 ['Smart scales / InBody', 'Weight (to ~0.3 kg)', 'Fat mass off by a median 2–4 kg for individuals; limb readings least '
  'trustworthy'],
], [W * 0.25, W * 0.30, W * 0.45]))
s.append(PageBreak())

# ---------------- Part 10 ----------------
s.append(para('Part 10 — Training and lifestyle while cutting', H1))
s += bullets([
    '<b>Keep lifting heavy.</b> Diet plus resistance training kept lean mass where diet alone or diet plus cardio lost '
    'it (Hunter 2008; Geliebter 1997). In 38 trained men in a deficit, 3 sets per exercise did as well as 5 (Roth 2023).',
    '<b>Cardio type doesn’t change fat loss:</b> intervals and steady cardio give the same result (Steele 2021, high '
    'certainty). The meta-analysis claiming intervals burn 28.5% more fat (Viana 2019) was <b>retracted</b>.',
    '<b>Interference is small:</b> cardio doesn’t compromise muscle growth on average (Schumann 2022); running costs more '
    'than cycling (Wilson 2012). Lift first or separate sessions by ≥3 hours to protect strength.',
    '<b>Exercise burns less than it looks:</b> about 28% of exercise energy is offset by a lower resting burn (Careau '
    '2021), and total energy use plateaus at high activity (Pontzer 2016). Don’t eat back exercise calories; keep a '
    'daily step floor.',
    '<b>Visceral fat responds to exercise even without weight loss</b> (Vissers 2013).',
    '<b>Sleep:</b> 5.5 h instead of 8.5 h cut fat loss by 55% and raised lean loss by 60% in a small 2-week study '
    '(Nedeltcheva 2010).',
    '<b>Recomposition:</b> possible in trained lifters but slow (Barakat 2020) — in a cut, aim to keep muscle.',
    '<b>Context — GLP-1 drugs:</b> lean share of weight lost ~25–35%, similar to diet alone; resistance training '
    'appears to lower it. Industry-funded trials.',
])

# ---------------- Part 11 ----------------
s.append(para('Part 11 — The plan (fact-checked)', H1))
plan = [
 ['#', 'Do this', 'Evidence'],
 ['1', 'Deficit set by outcome: ~0.5% bodyweight/week on 7-day average morning weight (~450–500 kcal/day at 85 kg; '
  'range 0.3–0.7%)', 'Moderate'],
 ['2', 'Adjust by 100–200 kcal/day every 2–3 weeks if the trend misses — never from one weigh-in', 'Measurement logic'],
 ['3', 'Protein 2.0–2.4 g/kg/day (170–205 g at 85 kg); floor 1.6 g/kg', 'Moderate'],
 ['4', 'Keep lifting heavy and progressively, 0–3 reps in reserve; 3 sets per exercise is enough', 'Strong (untrained); limited–moderate (trained)'],
 ['5', 'Put carbs around hard or high-volume sessions; fewer on rest days only if weekly calories stay the same', 'Moderate'],
 ['6', 'Don’t train fasted to “burn fat”', 'Limited'],
 ['7', 'Cardio 2–4× 20–40 min, low-impact (cycling, incline walk, rowing); any intensity; lift first or 3 h apart', 'Strong (fat); moderate (interference)'],
 ['8', 'Don’t eat back exercise calories; keep a daily step floor', 'Moderate / limited'],
 ['9', 'Sleep 7–9 h', 'Limited, large effect'],
 ['10', 'Diet breaks optional — for hunger, not extra fat loss', 'Moderate'],
 ['11', 'Settle the arm question once: DXA fasted, regional fat in kg; plus triceps and abdominal skinfolds or '
  'ultrasound in mm; ignore smart-scale limb %', 'Moderate'],
 ['12', 'Ignore spot work for fat, sauna suits, EMS belts, creams, “stubborn fat” protocols. Train arms for muscle.', 'Strong'],
]
s.append(grid(plan, [W * 0.05, W * 0.70, W * 0.25]))

# ---------------- Part 12 ----------------
s.append(para('Part 12 — Fact-check log', H1))
s.append(grid([
 ['Item', 'Correction'],
 ['Viana 2019 (HIIT 28.5% more fat loss)', 'Retracted — excluded'],
 ['Huovinen 2015', 'The 300 kcal group never showed a real intake drop — doesn’t prove “300 kcal does nothing”'],
 ['Garthe 2011', 'The fast group lost 1.0%/week, not the 1.4% target'],
 ['Nindl 1996', 'Measured: every region lost about half its fat. “Limb fat goes last” is interpretation'],
 ['Tinsley 2017 (DXA)', 'Readings shifted after eating regardless of macros; back to baseline next morning. Glycogen '
  'effect on DXA is better shown by Bone 2017 (~3% lean change after multi-day loading)'],
 ['Redman 2009 (CALERIE)', 'Metabolic adaptation was in diet-only groups, not diet-plus-exercise'],
 ['Hackett 2017', 'Only body-mass differences were given between groups'],
 ['Müller 2016 ultrasound', 'ICC 0.998 / ±1 mm applies to sums of sites, not single sites'],
 ['Longland 2016', 'Dairy-industry funding'],
 ['Arm geometry', 'Correct maths, but overstated — in 852 young men the arm was the leanest DXA region, so an '
  '“arms fattest” reading points even more to the device'],
], [W * 0.30, W * 0.70]))
s.append(para('<b>Still missing from the literature:</b> a carb-cycling trial at matched weekly calories in trained men; '
              'a fasted-vs-fed body-composition trial in trained men; a one-arm training trial under a controlled '
              'deficit measured by MRI. None was found.', P))

# ---------------- Part 13 ----------------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 24 * mm
s.append(para('Part 13 — Every study recorded (%d)' % n_all, H1))
s.append(para('Grouped by research area. <b>Checked</b> is the auditor’s verdict where re-checked. Full detail in '
              'FATLOSS-STUDIES.csv.', PS))
groups = [('W1', 'Energy balance and fuel use'), ('W2', 'Fasted cardio, carbs, carb cycling, protein'),
          ('W3', 'Spot reduction'), ('W4', 'Regional fat distribution'), ('W5', 'Exercise strategy while cutting'),
          ('W6', 'Measuring body fat'), ('WA', 'Added by the auditor')]
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
                     Paragraph('%s<br/>n = %s<br/>%s<br/>%s' % (esc(r['design']), esc(r['n']), esc(r['population']),
                                                              esc(r['duration'])), T),
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
