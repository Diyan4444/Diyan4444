import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

# List of profile repositories to inspect (Featured Projects + SIH Projects)
projects = [
    'Glamourly',
    'Rune-Striker',
    'RentWheels',
    'Shorties',
    'Leet-Vault',
    'yt-to-mp4',
    'OceanGuard',
    'Well-Whisperer'
]

for p in projects:
    print('=' * 60)
    print(f'INSPECTING {p}')
    print('=' * 60)
    
    # Try fetching README
    readme_text = None
    for branch in ['main', 'master']:
        url = f'https://raw.githubusercontent.com/Diyan4444/{p}/{branch}/README.md'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                readme_text = resp.read().decode('utf-8')
                print(f"Found README.md on {branch} ({len(readme_text)} bytes)")
                break
        except Exception:
            pass
            
    if readme_text:
        print("\n--- README Preview (first 15 lines) ---")
        for line in readme_text.splitlines()[:15]:
            print(" ", line)
    else:
        print("No README.md found directly.")

    # Try fetching root repo contents via API
    try:
        url = f'https://api.github.com/repos/Diyan4444/{p}/contents'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            files = json.loads(resp.read().decode('utf-8'))
            print("\nRoot Files/Dirs:")
            for f in files:
                print(f"  [{f['type']}] {f['name']}")
    except Exception as e:
        print(f"Could not list contents: {e}")
