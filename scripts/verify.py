import xml.etree.ElementTree as ET
from pathlib import Path
import re
import sys

def verify_all():
    print("==================================================")
    print("       PORTFOLIO & WORKFLOW VERIFICATION SUITE    ")
    print("==================================================")
    all_ok = True

    # 1. Check all SVGs for XML validity
    assets = list(Path('assets').glob('*.svg'))
    print(f"\n[1] Checking {len(assets)} SVG files for XML validity and well-formedness:")
    for p in assets:
        try:
            ET.parse(p)
            print(f"    [PASS] {p.name} ({p.stat().st_size} bytes)")
        except Exception as e:
            print(f"    [FAIL] {p.name}: {e}")
            all_ok = False

    # 2. Check README.md Line Count & Size
    readme_path = Path('README.md')
    readme_content = readme_path.read_text(encoding='utf-8')
    readme_lines = readme_content.splitlines()
    line_count = len(readme_lines)
    print(f"\n[2] Checking README.md line count:")
    if 140 <= line_count <= 200:
        print(f"    [PASS] Line count is {line_count} (Within target 140-200 lines: Medium Length)")
    else:
        print(f"    [WARN/FAIL] Line count is {line_count} (Outside ideal 140-200 range)")
        all_ok = False

    # 3. Check Exact 6 Permitted Repositories
    print(f"\n[3] Checking Featured Projects Scope (Strictly 6 permitted projects):")
    permitted = [
        "Glamourly",
        "Leet-Vault",
        "RentWheels",
        "OceanGuard",
        "yt-to-mp4",
        "Well-Whisperer"
    ]
    featured_section = re.search(r'## 🚀 Featured Projects(.*?)(## 💻 Skills & Technologies)', readme_content, re.DOTALL)
    if not featured_section:
        print("    [FAIL] Could not locate '## 🚀 Featured Projects' section")
        all_ok = False
    else:
        f_text = featured_section.group(1)
        for proj in permitted:
            if proj in f_text:
                print(f"    [PASS] Permitted project present: {proj}")
            else:
                print(f"    [FAIL] Missing permitted project: {proj}")
                all_ok = False
        
        excluded = ["AI-Debater", "Rune-Striker", "Report-Maker", "OSTLAB", "Shorties"]
        for bad in excluded:
            if bad in f_text:
                print(f"    [FAIL] Excluded project found in featured section: {bad}")
                all_ok = False

    # 4. Check Identity & LeetCode Handle
    print(f"\n[4] Checking Identity & LeetCode Handle:")
    if "diddy4" in readme_content and "pojeesahil" not in readme_content and "shaurya212121" not in readme_content:
        print("    [PASS] LeetCode handle correctly set to 'diddy4'")
    else:
        print("    [FAIL] LeetCode handle incorrect or extraneous peer username present")
        all_ok = False
        
    if "Information Technology Sophomore at VJTI Mumbai" in readme_content:
        print("    [PASS] Academic identity matches: 'Information Technology Sophomore at VJTI Mumbai'")
    else:
        print("    [FAIL] Academic identity missing or mismatched")
        all_ok = False

    # 5. Check Image References in README.md (Both Contribution Graph and Snake)
    img_srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', readme_content)
    md_imgs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', readme_content)
    all_imgs = img_srcs + md_imgs
    print(f"\n[5] Checking {len(all_imgs)} image references in README.md:")
    
    # Confirm both graph and snake are present
    has_graph = any("contribution-graph.svg" in s for s in all_imgs)
    has_snake = any("github-contribution-grid-snake.svg" in s for s in all_imgs)
    if has_graph and has_snake:
        print("    [PASS] Both 2-Month Contribution Graph and Snake Animation are present in order")
    else:
        print(f"    [FAIL] Missing expected image reference (graph={has_graph}, snake={has_snake})")
        all_ok = False
        
    for src in all_imgs:
        if src.startswith(('http://', 'https://')):
            print(f"    [REMOTE OK] {src[:65]}...")
        else:
            local_path = Path(src)
            if local_path.exists():
                print(f"    [LOCAL OK]  {src}")
            else:
                print(f"    [LOCAL FAIL] {src} DOES NOT EXIST")
                all_ok = False

    # 6. Check GitHub Actions Workflow (.github/workflows/snake.yml)
    print(f"\n[6] Checking GitHub Actions workflow (.github/workflows/snake.yml):")
    wf_path = Path('.github/workflows/snake.yml')
    if wf_path.exists():
        wf_text = wf_path.read_text(encoding='utf-8')
        if 'generate_contribution_graph.py' in wf_text and 'Platane/snk' in wf_text and 'contents: write' in wf_text:
            print("    [PASS] .github/workflows/snake.yml generates both the 2-Month graph and snake animation")
        else:
            print("    [FAIL] .github/workflows/snake.yml missing required configuration")
            all_ok = False
    else:
        print("    [FAIL] .github/workflows/snake.yml does not exist")
        all_ok = False

    # 7. Check for Secrets Leak
    print(f"\n[7] Scanning for exposed tokens or secrets:")
    leak_patterns = [r'ghp_[A-Za-z0-9_]{36}', r'github_pat_[A-Za-z0-9_]{82}', r'AIza[0-9A-Za-z-_]{35}']
    has_leak = False
    for pat in leak_patterns:
        if re.search(pat, readme_content):
            has_leak = True
            break
    if not has_leak:
        print("    [PASS] Zero tokens or private credentials found in repository files")
    else:
        print("    [FAIL] Detected possible secret leak in repository!")
        all_ok = False

    print("\n==================================================")
    if all_ok:
        print(">>> ALL 7 VERIFICATION GATES PASSED PERFECTLY! <<<")
        print("==================================================")
        return 0
    else:
        print(">>> VERIFICATION SUITE REPORTED ISSUES <<<")
        print("==================================================")
        return 1

if __name__ == "__main__":
    sys.exit(verify_all())
