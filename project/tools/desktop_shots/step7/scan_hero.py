import sys
from PIL import Image
def near(p,h,t=30):
    c=tuple(int(h[i:i+2],16) for i in (1,3,5)); return all(abs(a-b)<t for a,b in zip(p,c))
for path in sys.argv[1:]:
    im=Image.open(path).convert('RGB'); s=im.size[0]/1920; px=im.load()
    x=int(300*s); ys=[round(y/s,1) for y in range(int(262*s),int(284*s)) if near(px[x,y],'#4B5466')]
    x=int(563*s); segs=[]; cur=None
    for y in range(int(272*s),int(622*s)):
        on = not near(px[x,y],'#FFFFFF',40)
        if on and cur is None: cur=y
        if not on and cur is not None: segs.append((round(cur/s,1),round(y/s,1))); cur=None
    # reference line (Night, 1 px) at x 574: its vertical extent
    xr=None
    for xx in range(int(570*s),int(578*s)):
        col=[y for y in range(int(262*s),int(626*s)) if near(px[xx,y],'#12233D',40)]
        if len(col)>200*s: xr=(round(xx/s,1), round(col[0]/s,1), round((col[-1]+1)/s,1)); break
    print(path, 'rule', ys[:2], 'refline', xr, 'bars', [b for b in segs if b[1]-b[0]>10])
