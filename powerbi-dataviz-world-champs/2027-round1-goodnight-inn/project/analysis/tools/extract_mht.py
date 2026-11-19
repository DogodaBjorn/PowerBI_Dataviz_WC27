import sys, email, re, html
from email import policy
msg = email.message_from_binary_file(open(sys.argv[1],'rb'), policy=policy.default)
parts=[]
for p in msg.walk():
    ct=p.get_content_type()
    if ct=='text/html':
        parts.append((p.get('Content-Location'), p.get_content()))
print(len(parts), 'html parts', [u for u,_ in parts][:5], file=sys.stderr)
h=max(parts, key=lambda x: len(x[1]))[1]
open(sys.argv[2],'w').write(h)
# crude text extraction
h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
h=re.sub(r'(?i)<br\s*/?>','\n',h); h=re.sub(r'(?i)</(p|div|li|h\d|tr|table|blockquote)>','\n',h)
links=re.findall(r'(?i)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',h)
t=re.sub(r'<[^>]+>','',h); t=html.unescape(t); t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[3],'w').write(t)
with open(sys.argv[3]+'.links','w') as f:
    for u,txt in links:
        txt=html.unescape(re.sub(r'<[^>]+>','',txt)).strip()
        f.write(f"{txt[:80]} -> {u}\n")
