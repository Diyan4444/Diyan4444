import urllib.request
import re

req = urllib.request.Request('https://github.com/Diyan4444/Diyan4444', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
for img in imgs:
    if any(k in img for k in ['hero-banner', 'snake', 'pipeline', 'network', 'matrix', 'workflow']):
        print('Image on GitHub:', img)

# Also check text in rendered markdown
print("\n--- Check rendered text snippets ---")
for phrase in ["Interactive Web Portfolio", "ship_next_project", "Automated animation refreshed", "Information Technology Sophomore", "Information Technology Student"]:
    if phrase in html:
        print(f"Found on page: '{phrase}'")
    else:
        print(f"NOT on page: '{phrase}'")
