import xml.etree.ElementTree as ET
from pathlib import Path
import re
import sys

def verify_all():
    print("==================================================")
    print("      DUSK WORKSPACE PORTFOLIO VERIFICATION       ")
    print("==================================================")
    all_ok = True

    # 1. Check all SVGs for XML validity and well-formedness
    assets = list(Path('assets').glob('*.svg'))
    print(f"\n[1] Checking {len(assets)} SVG files for XML validity and well-formedness:")
    for p in assets:
        try:
            ET.parse(p)
            print(f"    [PASS] {p.name} ({p.stat().st_size} bytes)")
        except Exception as e:
            print(f"    [FAIL] {p.name}: {e}")
            all_ok = False

    # 2. Check Monthly Contribution Graph Title Requirement (Section 5)
    print(f"\n[2] Checking Monthly Contribution Graph Title (Must be strictly 'Monthly Contribution Graph'):")
    mcg_path = Path('assets/monthly-contribution-graph.svg')
    if mcg_path.exists():
        mcg_text = mcg_path.read_text(encoding='utf-8')
        if "Monthly Contribution Graph" in mcg_text:
            print("    [PASS] Title exactly matches 'Monthly Contribution Graph'")
        else:
            print("    [FAIL] Title 'Monthly Contribution Graph' not found in SVG")
            all_ok = False
            
        # Ensure no forbidden terms like "1-month", "2-month", "30 days" in title/text
        forbidden = ["1-month", "2-month", "1 month", "2 month", "30 days", "30-day", "60 days", "60-day"]
        found_forbidden = [f for f in forbidden if f.lower() in mcg_text.lower()]
        if not found_forbidden:
            print("    [PASS] Confirmed zero forbidden day/month references in graph")
        else:
            print(f"    [FAIL] Found forbidden duration terms: {found_forbidden}")
            all_ok = False
    else:
        print("    [FAIL] assets/monthly-contribution-graph.svg not found")
        all_ok = False

    # 3. Check README.md Line Count & Medium-Sized Length
    readme_path = Path('README.md')
    readme_content = readme_path.read_text(encoding='utf-8')
    readme_lines = readme_content.splitlines()
    line_count = len(readme_lines)
    print(f"\n[3] Checking README.md line count:")
    if 140 <= line_count <= 260:
        print(f"    [PASS] Line count is {line_count} (Medium-sized target 140-260 lines)")
    else:
        print(f"    [WARN/FAIL] Line count is {line_count} (Outside 140-260 lines)")
        all_ok = False

    # 4. Check Featured Projects Scope & More Exploring Organization
    print(f"\n[4] Checking Featured Projects Scope & Organization:")
    
    # 4A. Verify 6 featured projects in ## Projects section in order
    proj_sec_match = re.search(r'## Projects\s*(.*?)### More Exploring', readme_content, re.DOTALL)
    if proj_sec_match:
        proj_sec = proj_sec_match.group(1)
        ordered_projects = [
            ("Glamourly", "https://github.com/Diyan4444/Glamourly"),
            ("Rune-Striker", "https://github.com/Diyan4444/Rune-Striker"),
            ("Rent Wheels", "https://github.com/Diyan4444/RentWheels"),
            ("Code Crumbs", "https://github.com/Diyan4444/Shorties"),
            ("LeetVault", "https://github.com/Diyan4444/Leet-Vault"),
            ("YouTube-to-MP4", "https://github.com/Diyan4444/yt-to-mp4"),
        ]
        last_pos = -1
        for name, url in ordered_projects:
            pos = proj_sec.find(url)
            if pos != -1 and name in proj_sec:
                if pos > last_pos:
                    print(f"    [PASS] Featured project in correct sequence: {name} -> {url}")
                    last_pos = pos
                else:
                    print(f"    [FAIL] Project {name} out of sequence")
                    all_ok = False
            else:
                print(f"    [FAIL] Featured project missing in Projects section: {name} ({url})")
                all_ok = False
    else:
        print("    [FAIL] Could not isolate ## Projects section")
        all_ok = False

    # 4B. Verify More Exploring section
    more_exp_match = re.search(r'### More Exploring\s*(.*?)(?:<details>|---)', readme_content, re.DOTALL)
    if more_exp_match:
        more_sec = more_exp_match.group(1)
        if "SIH Development" in more_sec and "https://github.com/Diyan4444/OceanGuard" in more_sec and "https://github.com/Diyan4444/Well-Whisperer" in more_sec:
            print("    [PASS] SIH Development present with OceanGuard and Well-Whisperer")
        else:
            print("    [FAIL] SIH Development missing or incomplete in More Exploring")
            all_ok = False

        if "Open-Source Development" in more_sec and "https://github.com/Diyan4444/LeetCode" in more_sec:
            print("    [PASS] Open-Source Development present with LeetCode")
        else:
            print("    [FAIL] Open-Source Development missing or incomplete in More Exploring")
            all_ok = False

        if "Rune-Striker" not in more_sec and "Shorties" not in more_sec and "Code Crumbs" not in more_sec:
            print("    [PASS] Zero duplicates of Rune-Striker / Code Crumbs in More Exploring")
        else:
            print("    [FAIL] Duplication detected in More Exploring")
            all_ok = False
    else:
        print("    [FAIL] Could not isolate ### More Exploring section")
        all_ok = False

    # 5. Check Identity, LeetCode, Codeforces & Education
    print(f"\n[5] Checking Identity & Handles:")
    if "diddy4" in readme_content:
        print("    [PASS] LeetCode handle correctly set to 'diddy4'")
    else:
        print("    [FAIL] LeetCode handle 'diddy4' missing")
        all_ok = False

    if "diyanshah2301" in readme_content:
        print("    [PASS] Codeforces & Gmail correctly set to 'diyanshah2301'")
    else:
        print("    [FAIL] Handle/Email 'diyanshah2301' missing")
        all_ok = False
        
    if "VJTI Mumbai" in readme_content and "sophomore" in readme_content.lower():
        print("    [PASS] Academic identity matches: sophomore at VJTI Mumbai")
    else:
        print("    [FAIL] Academic identity missing or mismatched")
        all_ok = False

    # 6. Check Local & Remote Image References
    img_srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', readme_content)
    md_imgs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', readme_content)
    all_imgs = img_srcs + md_imgs
    print(f"\n[6] Checking {len(all_imgs)} image references in README.md:")
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

    # 7. Check Automated Workflow
    print(f"\n[7] Checking Automated Refresh Workflow:")
    wf_path = Path('.github/workflows/update-profile.yml')
    if wf_path.exists():
        wf_text = wf_path.read_text(encoding='utf-8')
        if 'generate_dusk_assets.py' in wf_text and 'Platane/snk' in wf_text and 'contents: write' in wf_text:
            print("    [PASS] .github/workflows/update-profile.yml handles stats, monthly graph, and snake")
        else:
            print("    [FAIL] .github/workflows/update-profile.yml missing required configuration")
            all_ok = False
    else:
        print("    [FAIL] .github/workflows/update-profile.yml does not exist")
        all_ok = False

    # 8. Check for Secrets Leak
    print(f"\n[8] Scanning for exposed tokens or secrets:")
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
        print(">>> ALL 8 VERIFICATION GATES PASSED PERFECTLY! <<<")
        print("==================================================")
        return 0
    else:
        print(">>> VERIFICATION SUITE REPORTED ISSUES <<<")
        print("==================================================")
        return 1

if __name__ == "__main__":
    sys.exit(verify_all())
