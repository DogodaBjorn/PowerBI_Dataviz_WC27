import json, re, sys
J=json.load(open(sys.argv[1]))
num=re.compile(r'^-?\d+(\.\d+)?$')
def fix(o):
    if isinstance(o,dict): return {k:fix(v) for k,v in o.items()}
    if isinstance(o,list): return [fix(v) for v in o]
    if isinstance(o,str) and num.match(o): return float(o) if '.' in o else int(o)
    return o
J=fix(J)
t=open(sys.argv[2],encoding='utf-8').read()
assert '/*__DATA__*/' in t
out=t.replace('/*__DATA__*/', json.dumps(J,separators=(',',':'),ensure_ascii=False))
open(sys.argv[3],'w',encoding='utf-8').write(out); print('written', len(out))
