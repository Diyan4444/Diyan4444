import xml.etree.ElementTree as ET
from pathlib import Path
import re

assets = list(Path('assets').glob('*.svg'))
print(f"Checking {len(assets)} SVG files for XML validity and well-formedness...")
all_valid = True
for p in assets:
    try:
        ET.parse(p)
        print(f"  [OK] {p.name} ({p.stat().st_size} bytes)")
    except Exception as e:
        print(f"  [FAIL] {p.name}: {e}")
        all_valid = False

readme = Path('README.md').read_text(encoding='utf-8')
img_srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', readme)
md_imgs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', readme)
all_imgs = img_srcs + md_imgs
print(f"\nChecking {len(all_imgs)} image references in README.md...")
local_ok = True
for src in all_imgs:
    if src.startswith(('http://', 'https://')):
        print(f"  [REMOTE OK] {src[:60]}...")
    else:
        local_path = Path(src)
        if local_path.exists():
            print(f"  [LOCAL OK]  {src}")
        else:
            print(f"  [LOCAL FAIL] {src} DOES NOT EXIST")
            local_ok = False

# Check preview/index.html
preview = Path('preview/index.html').read_text(encoding='utf-8')
p_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', preview)
print(f"\nChecking {len(p_imgs)} image references in preview/index.html...")
preview_ok = True
for src in p_imgs:
    resolved = (Path('preview') / src).resolve()
    if resolved.exists():
        print(f"  [PREVIEW OK]  {src} -> {resolved.name}")
    else:
        print(f"  [PREVIEW FAIL] {src} -> {resolved} DOES NOT EXIST")
        preview_ok = False

if all_valid and local_ok and preview_ok:
    print("\n>>> ALL ASSETS, PATHS, AND XML CHECKS PASSED PERFECTLY! <<<")
else:
    print("\n>>> VERIFICATION FOUND ISSUES <<<")
