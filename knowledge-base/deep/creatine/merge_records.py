import csv, re, sys, unicodedata, collections
D = sys.argv[1]
def norm_title(t):
    t = unicodedata.normalize('NFKD', t or '').lower()
    return re.sub(r'[^a-z0-9]+', '', t)
def surname(a):
    a = (a or '').strip()
    if not a: return ''
    parts = a.replace(',', ' ').split()
    # pubmed "Ingwall", epmc "Burke BI", s2 "Paulina Malon"
    if len(parts) >= 2 and parts[-1].isupper() and len(parts[-1]) <= 3: return parts[0].lower()
    return parts[-1].lower() if len(parts) >= 2 and not parts[-1].isupper() else parts[0].lower()
order = ['P1','P2','P3','P4','P5','P6','P7','P8','E1','E2','E3','E4','E5','E6','O1','S1']
rank = {q:i for i,q in enumerate(order)}
src = []
for r in csv.DictReader(open(D+'/raw/pubmed.csv')):
    src.append(dict(db='pubmed', sid='PMID:'+r['pmid'], pmid=r['pmid'], doi=r['doi'], title=r['title'], year=r['year'],
        fa=r['first_author'], pt=r['pub_types'], lang=r['language'], hum=r['mesh_humans'], ani=r['mesh_animals'], extra='', q=r['query_ids'].split(';')))
for r in csv.DictReader(open(D+'/raw/europepmc.csv')):
    src.append(dict(db='europepmc', sid='EPMC:%s:%s'%(r['source'],r['id']), pmid=r['pmid'], doi=r['doi'], title=r['title'], year=r['year'],
        fa=r['first_author'], pt=r['pub_type'], lang=r['language'], hum='', ani='', extra=r['source'], q=r['query_ids'].split(';')))
for r in csv.DictReader(open(D+'/raw/semanticscholar.csv')):
    src.append(dict(db='s2', sid='S2:'+r['s2_id'], pmid=r['pmid'], doi=r['doi'], title=r['title'], year=r['year'],
        fa=r['first_author'], pt=r['type'], lang=r['language'], hum='', ani='', extra='', q=r['query_ids'].split(';')))
for s in src:
    s['q'] = sorted({x.strip() for x in s['q'] if x.strip()}, key=lambda x: rank.get(x, 99))
    s['doi'] = (s['doi'] or '').strip().lower().replace('https://doi.org/','')
    s['pmid'] = (s['pmid'] or '').strip()
# process in order of first query so record ids follow search order; pubmed first within ties
src.sort(key=lambda s: (rank.get(s['q'][0], 99) if s['q'] else 99, {'pubmed':0,'europepmc':1,'s2':2}[s['db']]))
recs = []; by_doi = {}; by_pmid = {}; by_tk = {}
how = collections.Counter()
for s in src:
    tk = (norm_title(s['title']), s['year'], surname(s['fa'])) if s['title'] else None
    r = None
    if s['doi'] and s['doi'] in by_doi: r = by_doi[s['doi']]; how['doi'] += 1
    elif s['pmid'] and s['pmid'] in by_pmid: r = by_pmid[s['pmid']]; how['pmid'] += 1
    elif tk and tk[0] and tk in by_tk: r = by_tk[tk]; how['title+year+author'] += 1
    if r is None:
        r = dict(members=[], qs=[]); recs.append(r)
    r['members'].append(s); r['qs'] += s['q']
    if s['doi']: by_doi.setdefault(s['doi'], r)
    if s['pmid']: by_pmid.setdefault(s['pmid'], r)
    if tk and tk[0]: by_tk.setdefault(tk, r)
counters = collections.Counter(); first_new = collections.Counter()
out = []
for r in recs:
    m = r['members']; pm = [x for x in m if x['db']=='pubmed']
    best = pm[0] if pm else m[0]
    pick = lambda k: next((x[k] for x in ([best]+m) if x[k]), '')
    qs = sorted(set(r['qs']), key=lambda x: rank.get(x, 99)); fq = qs[0] if qs else 'X'
    first_new[fq] += 1; counters[fq] += 1
    rid = 'S%s-%04d' % (fq, counters[fq])
    pts = ';'.join(sorted({p.strip() for x in m for p in re.split(r'[;,]', x['pt']) if p.strip()}))
    langs = {x['lang'] for x in m if x['lang']}
    # auto filters, priority order
    code = ''
    ptl = pts.lower()
    if 'retracted publication' in ptl or 'retraction of publication' in ptl: code = 'E09'
    elif pm and pm[0]['ani']=='yes' and pm[0]['hum']=='no': code = 'E01'
    elif ptl and all(p.strip().lower() in {'editorial','comment','letter','published erratum','news','erratum','newspaper article','retraction of publication'} for p in pts.split(';')): code = 'E06'
    elif any(x['extra']=='PAT' for x in m) and len(m)==1: code = 'E16'
    elif langs and 'eng' not in langs and not any(x['db']=='s2' and not x['lang'] for x in m if False): code = 'E12'
    reason = {'E09':'auto: PubMed pub type Retracted Publication','E01':'auto: MeSH animals without humans',
              'E06':'auto: pub type editorial/comment/letter/erratum/news only','E16':'auto: patent record (Europe PMC PAT)',
              'E12':'auto: non-English (%s)' % ','.join(sorted(langs))}.get(code,'')
    out.append(dict(record_id=rid, doi=pick('doi'), pmid=pick('pmid'), title=pick('title'), year=pick('year'),
        first_author=pick('fa'), source_ids=';'.join(x['sid'] for x in m), query_ids=';'.join(qs), pub_types=pts,
        language=';'.join(sorted(langs)), dup_of='', auto_filter_code=code,
        ta_decision=('exclude' if code else ''), ta_reason=reason, screened_by=('auto-filter' if code else ''),
        verified_by='', session_date='2026-11-15'))
cols = ['record_id','doi','pmid','title','year','first_author','source_ids','query_ids','pub_types','language','dup_of',
        'auto_filter_code','ta_decision','ta_reason','screened_by','verified_by','session_date']
with open(D+'/records.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL); w.writeheader(); w.writerows(out)
# merge searches and fill new_after_dedup
rows = list(csv.DictReader(open(D+'/searches.csv'))) + list(csv.DictReader(open(D+'/searches-epmc-oa.csv')))
rows.sort(key=lambda r: rank.get(r['search_id'], 99))
for r in rows: r['new_after_dedup'] = str(first_new.get(r['search_id'], 0))
with open(D+'/searches.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_ALL); w.writeheader(); w.writerows(rows)
per_db = collections.Counter(s['db'] for s in src)
print('source rows', dict(per_db), 'total', len(src))
print('dup matches', dict(how)); print('unique records', len(out))
print('new per search', dict(first_new))
print('auto filter', collections.Counter(r['auto_filter_code'] or 'pass' for r in out))
