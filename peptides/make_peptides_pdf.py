"""Builds PEPTIDES-REPORT.pdf from the peptide research round (P1-P5 + PA audit)."""
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

R = '/home/user/tenstresearch/peptides/'
OUT = R + 'PEPTIDES-REPORT.pdf'
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
    c.drawString(15 * mm, 9 * mm, 'Peptides evidence review · 4 Nov 2026 · research summary — not medical advice, no dosing or sourcing')
    c.drawRightString(w - 15 * mm, 9 * mm, str(d.page)); c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title='Peptides Evidence Review',
                      author='TENSR research team (Claude Code)',
                      subject='48 peptides ranked by research volume, demonstrated benefit and side effects')
pw, ph = A4; lw, lh = landscape(A4)
doc.addPageTemplates([
    PageTemplate('P', frames=[Frame(18 * mm, 15 * mm, pw - 36 * mm, ph - 31 * mm)], onPage=deco, pagesize=A4),
    PageTemplate('L', frames=[Frame(12 * mm, 14 * mm, lw - 24 * mm, lh - 26 * mm)], onPage=deco, pagesize=landscape(A4))])
W = pw - 36 * mm
studies = list(csv.DictReader(open(R + 'PEPTIDE-STUDIES.csv')))
n_all = len(studies)
rk = {k: list(csv.DictReader(open(R + 'PA-rank-%s.csv' % k))) for k in ('research', 'benefit', 'safety')}
s = []

# ---------------- cover ----------------
s += [Spacer(1, 34 * mm), para('EVIDENCE REVIEW', st('k', f='DVB', fontSize=11, c=ACC, leading=14)),
      para('Peptides: 48 substances ranked by research, benefit and side effects', H0),
      para('From the approved weight-loss drugs to BPC-157, TB-500, growth-hormone secretagogues, melanotan and the '
           '“longevity” peptides — what has actually been shown in humans, what can go wrong, and what the law says.', SUB),
      Spacer(1, 6 * mm)]
s.append(box(para(
    '<b>Inside</b><br/><b>1</b> The answer in one page · <b>2</b> How to read the rankings · <b>3</b> Ranking A: most '
    'to least researched · <b>4</b> Ranking B: best to worst demonstrated benefit · <b>5</b> Ranking C: side effects, '
    'mildest to most serious · <b>6</b> The popular gym peptides, one by one · <b>7</b> Grey market and quality · '
    '<b>8</b> The law: Australia, sport, US · <b>9</b> Fact-check log · <b>10</b> Every study (%d)' % n_all, CALL)))
s += [Spacer(1, 6 * mm), box(para(
    '<b>How this was done.</b> Five research agents (metabolic/weight-loss; growth-hormone and gonadal axis; healing '
    'and recovery; cognitive, longevity, tanning and sexual; safety, quality and regulation) searched on 4 Nov 2026, '
    'then an independent auditor verified the load-bearing claims and built the three rankings. <b>Limits:</b> full '
    'papers could not be opened (PubMed/PMC blocked), so everything is at abstract or summary level. Several 2026 '
    'results come only from company announcements. <b>This report contains no dosing, cycling or sourcing '
    'information</b> and is not medical advice. Most substances here are prescription-only in Australia and banned in '
    'drug-tested sport.', PS), bg=WARN)]
s.append(PageBreak())

# ---------------- Part 1 ----------------
s.append(para('Part 1 — The answer in one page', H1))
s += bullets([
    '<b>The research is extremely lopsided.</b> The approved weight-loss drugs — semaglutide (Ozempic/Wegovy), '
    'tirzepatide (Mounjaro), liraglutide — have tens of thousands of trial participants. Most gym peptides have '
    '<b>zero</b> controlled human trials.',
    '<b>Every strong benefit is in a patient population, not lean lifters.</b> The GLP-1 drugs cause large weight loss '
    'in obesity (semaglutide −14.9% vs −2.4%; tirzepatide up to −20.9%). Tesamorelin cuts abdominal visceral fat in HIV. '
    'Nothing here has been shown to build muscle or strength in healthy trained people.',
    '<b>Growth hormone itself</b> adds ~2 kg lean mass in athletes but <b>no strength or endurance</b>, and raises '
    'diabetes risk. MK-677 adds ~1 kg lean mass with <b>no strength gain</b>, worsens blood sugar, and a trial was '
    'stopped early with more heart failure.',
    '<b>BPC-157:</b> no controlled human trial; ~30 people in uncontrolled reports from one clinic owner who sold the '
    'injections; >80% of papers from one lab. <b>TB-500</b> is a 7-amino-acid fragment with zero human studies (even '
    'full thymosin beta-4 failed its phase-3 trial).',
    '<b>The only supplement with trial evidence in people who lift:</b> collagen peptides — a small fat-free-mass '
    'gain that may be connective tissue rather than muscle, mostly industry-funded.',
    '<b>Unknown is not safe.</b> Substances with essentially no human safety data rank below every studied one. The '
    'bottom: BPC-157, TB-500, epitalon, dihexa, MGF, IGF-1 LR3.',
    '<b>Grey market is a major risk on its own:</b> purity 5–75%, arsenic and lead, endotoxin, wrong doses both ways, '
    'and vials with no peptide. Victoria (2026) recorded 7 liver injuries from a “retatrutide” product and 13 '
    'anaphylaxis cases from unapproved peptides, at least one fatal.',
])
top = lambda k, n: ', '.join(r['substance'].replace(' (NON-PEPTIDE)', '*') for r in rk[k][:n])
bot = lambda k, n: ', '.join(r['substance'].replace(' (NON-PEPTIDE)', '*') for r in rk[k][-n:])
s.append(grid([
 ['Ranking', 'Top 5', 'Bottom 5'],
 ['A. Most researched', top('research', 5), bot('research', 5)],
 ['B. Best demonstrated benefit', top('benefit', 5), bot('benefit', 5)],
 ['C. Mildest / best-known side effects', top('safety', 5), bot('safety', 5)],
], [W * 0.24, W * 0.38, W * 0.38]))
s.append(para('* non-peptide, included because it is commonly grouped with peptides.', PS))
s.append(PageBreak())

# ---------------- Part 2 ----------------
s.append(para('Part 2 — How to read the rankings', H1))
s.append(grid([
 ['Ranking', 'Scoring'],
 ['<b>A. Research volume</b> (0–6)', 'Approval by FDA, EMA or TGA +3 (other regulators +1); an extra phase-3 programme beyond '
  'the approval +1; human RCT volume up to +2. Ties broken by trial participants. Unpublished conference abstracts score 0.'],
 ['<b>B. Benefit</b> (A–E)', '<b>A</b> ≥2 independent RCTs or a meta-analysis with a meaningful effect in that population · '
  '<b>B</b> ≥1 good RCT, or consistent RCTs in an adjacent population · <b>C</b> small/short RCTs, surrogate outcomes '
  'only, or mixed · <b>D</b> human case data or animal/lab only · <b>E</b> anecdote/marketing, or RCTs showing no effect. '
  'Down one grade for industry-only evidence, a gym claim resting on a patient population, or a clinic/vendor source.'],
 ['<b>C. Side effects</b>', '<b>C</b> = how well known: C1 ≥1,000 in RCTs plus post-marketing · C2 100–999 · C3 &lt;100 or '
  'case reports · <b>CU unknown</b>. <b>S</b> = worst plausible: S1 mild · S2 needs treatment/stopping · S3 serious '
  '(hospital, anaphylaxis, organ injury) · S4 life-threatening or irreversible. <b>Q</b> = supply: Q0 pharmaceutical · '
  'Q1 compounded · Q2 grey market only. Sorted by C, then S, then Q. <b>Every CU ranks below every characterised substance.</b>'],
], [W * 0.24, W * 0.76]))
s.append(para('Benefit grades for weight-loss drugs describe people with obesity. For a lean lifter the expected benefit '
              'is unknown and the lean-mass cost (25–40% of weight lost) matters more.', P))

def rank_table(key, title, intro, score_hdr):
    s.append(para(title, H1)); s.append(para(intro, P))
    rows = [['#', 'Substance', 'Class', score_hdr, 'Why', 'Key source']]
    sh = []
    for i, r in enumerate(rk[key], 1):
        rows.append([esc(r['rank']), '<b>%s</b>' % esc(r['substance']), esc(r['class']), esc(r['score_or_grade']),
                     esc(r['one_line_reason']), esc(r['key_citation'])])
        g = r['score_or_grade']
        if key == 'benefit':
            col = {'A': GOOD, 'B': GOOD, 'C': MID, 'D': RES, 'E': BAD}.get(g.strip()[:1])
        elif key == 'safety':
            col = BAD if g.startswith('CU') else (GOOD if g.startswith('C1') else MID)
        else:
            try: v = int(g.strip()[0]); col = GOOD if v >= 5 else (MID if v >= 2 else BAD)
            except Exception: col = None
        if col: sh.append((i, col))
    t = grid(rows, [W * 0.05, W * 0.17, W * 0.13, W * 0.13, W * 0.34, W * 0.18], style=st('rt', fontSize=7.2, leading=9.2), shades=sh)
    s.append(t); s.append(PageBreak())

rank_table('research', 'Part 3 — Ranking A: most to least researched',
           'How much human evidence exists, regardless of whether it is positive.', 'Score (0–6)')
rank_table('benefit', 'Part 4 — Ranking B: best to worst demonstrated benefit',
           'Best demonstrated human benefit, with the population it applies to. A high grade in obesity or HIV is not '
           'evidence for a lean lifter.', 'Grade')
rank_table('safety', 'Part 5 — Ranking C: side effects, mildest and best-known first',
           'Top = mildest and best characterised. Bottom = serious, or unknown because nobody has studied it in humans.', 'C · S · Q')

# ---------------- Part 6 ----------------
s.append(para('Part 6 — The popular gym peptides, one by one', H1))
gym = [
 ['Peptide', 'What’s been shown in humans', 'Known / possible harms', 'Australia · Sport'],
 ['BPC-157', 'No controlled trial. ~30 people in 3 uncontrolled reports by a clinic owner who sold the injections; enema '
  'trials only as conference abstracts.', 'Unknown. Theoretical cancer concern (promotes blood-vessel growth). Grey-market '
  'content up to ±80% off label.', 'S4 prescription-only · WADA S0 (banned)'],
 ['TB-500', 'None — it is a fragment, not thymosin beta-4. Full Tβ4 (~1,700 trial participants) missed its phase-3 '
  'dry-eye endpoints; wound gels no better than placebo.', 'Unknown. Products didn’t match labels.', 'S4 (secondary source) · WADA S2'],
 ['CJC-1295', 'Hormone levels only (phase 1). Phase-2 trial halted in 2006 after a participant died.', 'Unknown; '
  'theoretical IGF-1/cancer; preprint found no labelled peptide in 22 samples.', 'S4 · WADA S2'],
 ['Ipamorelin', 'Only efficacy trial (post-surgical gut) negative.', 'Little data; FDA cites significant safety concerns.', 'S4 · WADA S2'],
 ['GHRP-2 / GHRP-6 / hexarelin', 'No body-composition trial.', 'Raise cortisol and prolactin; appetite (GHRP-6).', 'S4 · WADA S2'],
 ['MK-677*', '+1.1 kg fat-free mass vs −0.5 kg in older adults (Nass 2008); no strength or function gain; visceral fat '
  'not significantly changed.', 'Higher blood sugar, lower insulin sensitivity; heart-failure signal in a stopped trial.', 'S4 · WADA S2'],
 ['IGF-1 LR3 / MGF', 'None.', 'Unknown; theoretical cancer; unpurified product found.', 'WADA S2'],
 ['AOD-9604', 'Failed obesity trials.', 'Few reported; unpublished data.', 'WADA S2'],
 ['Melanotan II', 'No trials for tanning.', 'Case reports: moles changing, melanoma, priapism, kidney and muscle damage; '
  'vials 43–88% of label.', 'Not specifically scheduled; under TGA review'],
 ['Collagen peptides', 'Small fat-free-mass gain with lifting (ES 0.48, 19 studies); may not be muscle.', 'GI upset; allergy by source.', 'Food supplement · not banned'],
]
s.append(grid(gym, [W * 0.15, W * 0.36, W * 0.30, W * 0.19], style=st('g', fontSize=7.6, leading=9.8)))
s.append(para('* non-peptide.', PS))

# ---------------- Part 7 ----------------
s.append(para('Part 7 — Grey market and quality', H1))
s += bullets([
    '<b>Belgium (Janvier 2018):</b> falsified peptide drugs 5–75% pure; arsenic and lead up to ~10× injectable limits.',
    '<b>Online semaglutide (Ashraf 2024, JAMA Netw Open):</b> 7–14% pure vs 99% claimed, 29–39% more drug than labelled, '
    'endotoxin in one sample. The FDA reported 5–20× overdoses from compounded vials.',
    '<b>“TB500” and “SGF1000” (Delcourt 2023):</b> didn’t match labels; SGF1000 was mostly sheep protein.',
    '<b>Denmark:</b> 9 of 36 seized samples had no peptide at all. <b>Norway:</b> melanotan II labelled as an antifungal.',
    '<b>Growth hormone:</b> only 5 of 21 products sold as GH contained it (Cologne anti-doping lab).',
    '<b>“Research use only / not for human consumption”</b> labels are how these avoid medicine regulation — no sterility, '
    'endotoxin or content control applies. Vendor certificates of analysis aren’t independent evidence.',
    '<b>Australia 2026:</b> 7 liver injuries from a “retatrutide” product and 13 anaphylaxis cases from unapproved peptides '
    'in Victoria, at least one fatal.',
])

# ---------------- Part 8 ----------------
s.append(para('Part 8 — The law', H1))
s += bullets([
    '<b>Australia (TGA):</b> BPC-157, CJC-1295, ipamorelin, GHRPs and MK-677 are Schedule 4 (prescription only) and '
    'Appendix D; none is on the ARTG. TB-500’s scheduling is from a secondary source. Illegal peptides are a named '
    '2026 compliance priority; a peptide clinic was fined A$10M in 2019. GLP-1 compounding was banned from 1 Oct 2024.',
    '<b>Sport (WADA):</b> BPC-157 named under S0; GH secretagogues, GHRPs, GHRH analogues, TB-500, AOD-9604 and MK-677 '
    'under S2 — banned at all times. Semaglutide and tirzepatide are not prohibited. An athlete got a 1-year ban from a '
    'supplement contaminated with BPC-157.',
    '<b>US (FDA):</b> about 17 peptides were put in compounding “Category 2” (significant safety risk) in 2023; most came '
    'off in 2024 and April 2026 because nominations were withdrawn, not because of new safety data. In July 2026 an '
    'advisory panel voted to recommend BPC-157 (8–6–1), TB-500, KPV, MOTS-c (7–5–2), epitalon (7–4–1) and semax for '
    'compounding over FDA staff opposition; DSIP was rejected. Nothing is compoundable until the FDA completes rulemaking.',
])

# ---------------- Part 9 ----------------
s.append(para('Part 9 — Fact-check log', H1))
s.append(grid([
 ['Item', 'Correction'],
 ['Nass 2008 (MK-677)', 'Did <b>not</b> significantly reduce visceral fat — an agent’s summary said it did'],
 ['NAION (semaglutide eye risk)', 'EMA wording is “up to 1 in 10,000 users”, not per 10,000 person-years'],
 ['Retatrutide approval timeline', '“Filing Q1 2027” unverifiable; phase-3 results are company toplines, unpublished'],
 ['Afamelanotide approvals', 'EC 2014, FDA 2019, TGA 2020'],
 ['FDA panel votes (July 2026)', 'Exist and are verified (one agent said “not found”)'],
 ['Victoria alerts', 'At least one anaphylaxis case fatal; liver injuries now 7'],
 ['Melanotan II scheduling', '“Schedule 4 since 2018” unproven; a TGA page says it is not specifically scheduled'],
 ['GH meta-analyses', 'Healthy elderly = Liu 2007; athletes = Liu 2008'],
 ['CJC-1295', 'Trial halted 17 July 2006 after a death (confirmed); the cause in a company report was not read'],
 ['TB-500 / AOD-9604', 'WADA S2, not S0'],
 ['BPC-157 FDA Category 2 removal', 'Announced 15 April 2026, effective ~22–23 April'],
 ['Tirzepatide antibodies (51%)', 'From type 2 diabetes trials'],
], [W * 0.32, W * 0.68]))
s.append(para('<b>Still unconfirmed:</b> TGA scheduling of CJC-1295, ipamorelin, MK-677 and melanotan II against the '
              'current Poisons Standard; a claimed retraction of dihexa’s founding papers; several 2026 results that '
              'exist only as company announcements.', P))

# ---------------- Part 10 ----------------
s.append(NextPageTemplate('L')); s.append(PageBreak())
LW = lw - 24 * mm
s.append(para('Part 10 — Every study recorded (%d)' % n_all, H1))
s.append(para('Grouped by research area. The auditor’s rows re-check studies also listed in other sections, so some '
              'appear twice. Full detail in PEPTIDE-STUDIES.csv.', PS))
groups = [('P1', 'Metabolic and weight-loss peptides'), ('P2', 'Growth-hormone and gonadal axis'),
          ('P3', 'Healing and recovery'), ('P4', 'Cognitive, longevity, tanning, sexual'),
          ('P5', 'Safety, quality and regulation'), ('PA', 'Auditor’s verification rows')]
cw = [LW * x for x in (0.19, 0.08, 0.12, 0.23, 0.18, 0.12, 0.08)]
for code, title in groups:
    g = [r for r in studies if r['found_by'].split(';')[0] == code]
    if not g: continue
    s.append(para('%s (%d)' % (title, len(g)), H2))
    data = [[Paragraph(x, TB) for x in ['Study', 'Substance', 'Design · who', 'Result', 'Adverse events', 'Limits', 'Checked']]]
    for r in g:
        cit = '<b>%s</b><br/>%s' % (esc(r['key']), esc(r['citation']))
        if r['doi_or_link']: cit += '<br/><font color="#5a6370">%s</font>' % esc(r['doi_or_link'][:90])
        data.append([Paragraph(cit, T), Paragraph(esc(r['substance']), T),
                     Paragraph('%s<br/>n = %s<br/>%s<br/>%s' % (esc(r['design']), esc(r['n']), esc(r['population']), esc(r['duration'])), T),
                     Paragraph(esc(r['result_effect_uncertainty']), T), Paragraph(esc(r['adverse_events']), T),
                     Paragraph(esc(r['limitations_coi']) + '<br/><font color="#5a6370">%s · %s</font>' % (esc(r['evidence_level']), esc(r['access'])), T),
                     Paragraph(esc((r['audit_verdict'] or '')[:120]), T)])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.3, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('BACKGROUND', (0, 0), (-1, 0), BAND), ('LEFTPADDING', (0, 0), (-1, -1), 3),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 3), ('TOPPADDING', (0, 0), (-1, -1), 2),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                           ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafbfc')])]))
    s.append(t)

doc.build(s)
print('ok', OUT, n_all)
