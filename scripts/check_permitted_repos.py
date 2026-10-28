import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

# List of verified profile repositories (Featured Projects + SIH Projects)
projects = [
    'Glamourly',       # 1. Glamourly
    'Rune-Striker',    # 2. Rune-Striker
    'RentWheels',      # 3. Rent Wheels
    'Shorties',        # 4. Code Crumbs
    'Leet-Vault',      # 5. LeetVault
    'yt-to-mp4',       # 6. YouTube-to-MP4
    'OceanGuard',      # SIH Development: OceanGuard AI
    'Well-Whisperer'   # SIH Development: Well-Whisperer
]

print("=== CHECKING DIYAN'S 6 PERMITTED REPOSITORIES ===")
for p in projects:
    api_url = f'https://api.github.com/repos/Diyan4444/{p}'
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"\n[FOUND] {data['name']}")
            print(f"  Description: {data.get('description')}")
            print(f"  Language: {data.get('language')}")
            print(f"  Topics: {data.get('topics')}")
            print(f"  Homepage: {data.get('homepage')}")
            print(f"  Stars: {data.get('stargazers_count')}, Forks: {data.get('forks_count')}")
            print(f"  Created: {data.get('created_at')}, Updated: {data.get('updated_at')}")
    except urllib.error.HTTPError as e:
        print(f"\n[HTTP {e.code}] {p} - Trying case variations or user repos search...")
    except Exception as e:
        print(f"\n[ERROR] {p}: {e}")
