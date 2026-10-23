"""
Generates a dark-themed Contribution Graph SVG matching Diyan Shah's Flame/Ember theme.
Fetches public contribution activity and renders a clean, pixel-perfect 53-week heatmap.
"""

from pathlib import Path
import urllib.request
import json
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Theme Palette (Flame & Ember)
BG_CARD = "#0a0b0e"
BG_SURFACE = "#12141a"
BORDER_SUBTLE = "#331c22"
BORDER_ACCENT = "#4a242b"
TEXT_PRIMARY = "#ffffff"
TEXT_MUTED = "#94a3b8"
ACCENT_RED = "#ff3355"
ACCENT_ORANGE = "#ff6b35"

# Contribution Level Colors
COLOR_LEVELS = [
    "#161820",  # Level 0: Empty
    "#4c1d1d",  # Level 1: Deep Ruby
    "#881337",  # Level 2: Crimson Ember
    "#ea580c",  # Level 3: Blaze Orange
    "#ff6b35",  # Level 4: Vivid Flame
]

def fetch_contributions(username="Diyan4444"):
    url = f"https://github-contributions-api.jogruber.de/v4/{username}?y=last"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except Exception as e:
        print(f"Warning: Failed to fetch from jogruber API ({e}), attempting fallback...")
        return None

def generate_graph_svg(data=None, username="Diyan4444"):
    if not data:
        data = fetch_contributions(username)
    
    contributions = []
    total_count = 0
    if data and "contributions" in data:
        contributions = data["contributions"]
        total_count = data.get("total", {}).get("lastYear", sum(d.get("count", 0) for d in contributions))
    
    # SVG Dimensions
    cell_size = 11
    cell_gap = 3
    step = cell_size + cell_gap  # 14px
    start_x = 45
    start_y = 52
    
    # We organize contributions into 53 weeks of 7 days (Sunday=0 to Saturday=6)
    cells_svg = []
    month_labels = {}
    
    # Pre-parse dates
    days_by_week = []
    current_week = []
    
    for i, day in enumerate(contributions):
        dt = datetime.strptime(day["date"], "%Y-%m-%d")
        w_day = (dt.weekday() + 1) % 7  # Convert to Sunday=0 ... Saturday=6
        
        # Track months for header labels
        month_name = dt.strftime("%b")
        col_idx = len(days_by_week)
        if dt.day <= 7 and month_name not in month_labels.values():
            month_labels[col_idx] = month_name
            
        current_week.append((w_day, day))
        if w_day == 6 or i == len(contributions) - 1:
            days_by_week.append(current_week)
            current_week = []
            
    # Render cells
    for col_idx, week in enumerate(days_by_week):
        for w_day, day in week:
            x = start_x + col_idx * step
            y = start_y + w_day * step
            level = min(day.get("level", 0), 4)
            count = day.get("count", 0)
            date_str = day.get("date", "")
            color = COLOR_LEVELS[level]
            
            # Format count string
            cnt_label = f"{count} contribution{'s' if count != 1 else ''}" if count > 0 else "No contributions"
            tooltip = f"{cnt_label} on {date_str}"
            
            cell_xml = f'<rect class="day" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" fill="{color}"><title>{tooltip}</title></rect>'
            cells_svg.append(cell_xml)
            
    # Month Labels SVG
    months_svg = []
    for col_idx, m_name in month_labels.items():
        mx = start_x + col_idx * step
        months_svg.append(f'<text x="{mx}" y="42" class="lbl-month">{m_name}</text>')
        
    # Weekday Labels (Mon, Wed, Fri)
    weekdays_svg = [
        f'<text x="26" y="{start_y + 1 * step + 9}" class="lbl-weekday">Mon</text>',
        f'<text x="26" y="{start_y + 3 * step + 9}" class="lbl-weekday">Wed</text>',
        f'<text x="26" y="{start_y + 5 * step + 9}" class="lbl-weekday">Fri</text>',
    ]
    
    width = start_x + len(days_by_week) * step + 30
    height = 192
    
    legend_x = width - 180
    legend_y = height - 20
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="cgbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_CARD}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <style>
      .title-main {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13.5px; font-weight: 700; fill: {TEXT_PRIMARY}; }}
      .title-count {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 13.5px; font-weight: 800; fill: {ACCENT_ORANGE}; }}
      .lbl-month {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      .lbl-weekday {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9px; fill: {TEXT_MUTED}; text-anchor: middle; }}
      .lbl-legend {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      .day {{ transition: fill 0.2s ease; }}
      .day:hover {{ stroke: #ffffff; stroke-width: 1px; }}
    </style>
  </defs>

  <!-- Background Frame -->
  <rect width="{width}" height="{height}" rx="10" fill="url(#cgbg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Top Title & Badge -->
  <g transform="translate(30, 24)">
    <circle cx="6" cy="-4" r="4.5" fill="{ACCENT_RED}">
      <animate attributeName="opacity" values="0.4; 1; 0.4" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="18" y="0" class="title-main">
      GitHub Contribution Graph <tspan class="title-count">({total_count} contributions)</tspan>
    </text>
  </g>

  <!-- Month Labels -->
  {''.join(months_svg)}

  <!-- Weekday Labels -->
  {''.join(weekdays_svg)}

  <!-- Contribution Heatmap Cells -->
  {''.join(cells_svg)}

  <!-- Legend at Bottom-Right -->
  <g transform="translate({legend_x}, {legend_y})">
    <text x="0" y="8" class="lbl-legend">Less</text>
    <rect x="32" y="0" width="10" height="10" rx="2" fill="{COLOR_LEVELS[0]}"/>
    <rect x="46" y="0" width="10" height="10" rx="2" fill="{COLOR_LEVELS[1]}"/>
    <rect x="60" y="0" width="10" height="10" rx="2" fill="{COLOR_LEVELS[2]}"/>
    <rect x="74" y="0" width="10" height="10" rx="2" fill="{COLOR_LEVELS[3]}"/>
    <rect x="88" y="0" width="10" height="10" rx="2" fill="{COLOR_LEVELS[4]}"/>
    <text x="105" y="8" class="lbl-legend">More</text>
  </g>
</svg>'''
    
    out_file = ASSETS_DIR / "contribution-graph.svg"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {out_file.name} successfully! (Total contributions: {total_count})")
    return out_file

if __name__ == "__main__":
    generate_graph_svg()
