import json, sys, os, glob, re
root = sys.argv[1]
pj = json.load(open(os.path.join(root,'pages','pages.json'),encoding='utf-8-sig'))
print('pageOrder', pj.get('pageOrder'), 'active', pj.get('activePageName'))
for pid in pj.get('pageOrder', []):
    p = json.load(open(os.path.join(root,'pages',pid,'page.json'),encoding='utf-8-sig'))
    print('\n######## PAGE', pid, '|', p.get('displayName'), '|', p.get('width'), 'x', p.get('height'), '| vis:', p.get('visibility'))
    for vf in sorted(glob.glob(os.path.join(root,'pages',pid,'visuals','*','visual.json'))):
        v = json.load(open(vf,encoding='utf-8-sig'))
        vis = v.get('visual',{})
        pos = v.get('position',{})
        print(f"  -- {v.get('name')} type={vis.get('visualType')} pos=({pos.get('x'):.0f},{pos.get('y'):.0f},{pos.get('width'):.0f}x{pos.get('height'):.0f})")
        s = json.dumps(v, ensure_ascii=False)
        # text runs
        for m in re.finditer(r'"value":\s*"((?:[^"\\]|\\.)*)"', s):
            t = m.group(1)
            if len(t) > 2 and not t.startswith("'") : print('     txt:', t[:600])
        # field refs
        props = set(re.findall(r'"Property":\s*"([^"]+)"', s)); ents=set(re.findall(r'"Entity":\s*"([^"]+)"', s))
        if props: print('     fields:', sorted(ents), sorted(props))
        for m in re.finditer(r'"url":\s*"([^"]+)"', s): print('     url:', m.group(1))
