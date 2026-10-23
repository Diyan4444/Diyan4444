import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

refs = ['shreyansdeshp', 'ShriyansBharuka', 'shaurya212121', 'pojeesahil']

for u in refs:
    p = Path(f'{u}_readme.md')
    if not p.exists():
        continue
    content = p.read_text(encoding='utf-8')
    lines = content.splitlines()
    words = len(content.split())
    
    print('=' * 60)
    print(f'ANALYSIS OF {u} (Lines: {len(lines)}, Words: {words}, Size: {len(content)} bytes)')
    print('=' * 60)
    
    headings = re.findall(r'^(#+\s+.*)', content, re.MULTILINE)
    print('\n[Headings]:')
    for h in headings:
        print(' ', h)
        
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content) + re.findall(r'!\[[^\]]*\]\(([^)]+)\)', content)
    print(f'\n[Images/Badges/SVGs ({len(imgs)} total)]:')
    for img in imgs[:12]:
        print(' ', img)
    if len(imgs) > 12:
        print(f'  ... and {len(imgs) - 12} more')
        
    widgets = []
    if 'streak-stats' in content: widgets.append('Streak Stats')
    if 'github-readme-stats' in content: widgets.append('GitHub Readme Stats')
    if 'snake' in content.lower(): widgets.append('Snake Animation')
    if 'trophy' in content.lower(): widgets.append('GitHub Trophies')
    if 'activity-graph' in content or 'github-readme-activity-graph' in content: widgets.append('Activity Graph')
    if 'visitor' in content.lower() or 'hits' in content or 'komarev' in content: widgets.append('Visitor Counter')
    if 'capsule-render' in content: widgets.append('Capsule Render')
    if 'skillicons.dev' in content: widgets.append('SkillIcons.dev')
    if 'shields.io' in content: widgets.append('Shields.io Badges')
    if 'github-readme-streak-stats' in content: widgets.append('Streak Stats')
    print('\n[Widgets/Services]:', widgets)
    
    # Project showcase style
    print('\n[Projects mentioned / showcase style]:')
    matches = re.findall(r'(https://github\.com/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+)', content)
    unique_repos = set(matches)
    for r in list(unique_repos)[:8]:
        print(' ', r)
