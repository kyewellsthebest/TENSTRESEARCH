"""Builds the JSON data files for the Research Progress dashboard from the repo.
Run from the repo root:  python3 knowledge-base/progress/build_progress.py
Writes knowledge-base/progress/out/*.json. Each round: append a row to rounds.csv first."""
import csv, json, os, re, collections, datetime
KB = 'knowledge-base'; OUT = KB + '/progress/out'; os.makedirs(OUT, exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def dump(name, rows):
    json.dump(rows, open(f'{OUT}/{name}.json', 'w'), indent=1, ensure_ascii=False)

# 1. Creatine funnel from records.csv
recs = list(csv.DictReader(open(KB + '/deep/creatine/records.csv')))
auto = [r for r in recs if r['screened_by'] == 'auto-filter']
man = [r for r in recs if r['ta_decision'] and r['screened_by'] != 'auto-filter']
dec = collections.Counter(r['ta_decision'] for r in man)
todo = sum(1 for r in recs if not r['ta_decision'])
dump('funnel', [
    {"order": 1, "stage": "Found in databases", "count": 7752},
    {"order": 2, "stage": "Unique after removing duplicates", "count": len(recs)},
    {"order": 3, "stage": "Left after automatic filters", "count": len(recs) - len(auto)},
    {"order": 4, "stage": "Screened by title and abstract", "count": len(man)},
    {"order": 5, "stage": "Kept for full-text reading", "count": dec['include'] + dec['maybe']},
])
dump('screening', [
    {"decision": "Included", "count": dec['include']},
    {"decision": "Maybe", "count": dec['maybe']},
    {"decision": "Excluded", "count": dec['exclude']},
    {"decision": "Still to screen", "count": todo},
])
names = {'E01': 'Animal / lab only', 'E02': 'Clinical, child or over-50 group', 'E03': 'Not creatine, or no training',
         'E04': 'No proper comparison group', 'E05': 'Wrong outcome', 'E06': 'Review, comment or case report',
         'E07': 'Too short', 'E14': 'Other ingredients muddy it', 'E12': 'Not English'}
ex = collections.Counter(r['ta_reason'][:3] for r in man if r['ta_decision'] == 'exclude')
dump('exclusions', [{"code": k, "reason": names.get(k, k), "count": v} for k, v in ex.most_common()])

# 2. Round history
rounds = list(csv.DictReader(open(KB + '/progress/rounds.csv')))
for r in rounds:
    for k in ('screened', 'included', 'maybe', 'excluded', 'to_screen'): r[k] = int(r[k])
dump('rounds', rounds)

# 3. Deep-dive phases for the active topic (from progress.md header)
prog = open(KB + '/deep/creatine/progress.md').read()
m = re.search(r'\*\*Current phase:\*\* (\d)', prog); cur = int(m.group(1)) if m else 1
phase_names = ['Protocol & search', 'Screening', 'Citation chasing', 'Full text & risk of bias', 'Synthesis & verdict', 'Audit']
total_to_screen = len(recs) - len(auto)
rows = []
for i, n in enumerate(phase_names, 1):
    if i < cur: st, pct = 'Done', 100
    elif i == cur: st, pct = 'In progress', (round(100 * len(man) / total_to_screen) if i == 2 else 0)
    else: st, pct = 'Not started', 0
    rows.append({"phase": i, "name": n, "status": st, "percent": pct})
dump('phases', rows)

# 4. Topic queue (deep-dive queue order from DEEP-DIVE.md)
dd = open(KB + '/DEEP-DIVE.md').read().split('## Deep-dive queue')[1]
q = [re.sub(r'\s*\(.*?\)', '', l.split('. ', 1)[1]).strip() for l in dd.splitlines() if re.match(r'^\d+\. ', l)]
paused = '**Paused' in open(KB + '/deep/creatine/progress.md').read()   # a pause note at the top of progress.md
dump('queue', [{"position": i + 1, "topic": t,
                "status": (('Deep dive paused (phase %d)' % cur if paused else 'Deep dive in progress') if i == 0 else 'Waiting')}
               for i, t in enumerate(q)])

# 5. Library verdicts so far (from library category READMEs)
verd = []
for cat in sorted(os.listdir('library')):
    p = f'library/{cat}/README.md'
    if not os.path.isfile(p): continue
    for line in open(p):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 4 and cells[0] not in ('Topic', '---') and not set(cells[0]) <= set('-'):
            verd.append({"category": cat.replace('-', ' ').capitalize(), "topic": cells[0], "verdict": cells[1], "confidence": cells[2]})
dump('verdicts', verd)

# 6. Totals
studies = list(csv.DictReader(open(KB + '/STUDIES.csv')))
log_rows = [l for l in open(KB + '/LOG.md') if l.startswith('| 2026')]
dump('totals', [{"metric": "Studies in database", "value": len(studies)},
                {"metric": "Research rounds logged", "value": len(log_rows)},
                {"metric": "Topics with a verdict", "value": len(verd)},
                {"metric": "Open topics in queue", "value": open(KB + '/TOPICS.md').read().count('- [ ] open')},
                {"metric": "Data built at (UTC)", "value": now}])
print('built', sorted(os.listdir(OUT)))
