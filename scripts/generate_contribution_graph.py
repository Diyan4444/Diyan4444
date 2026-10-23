"""
Generates the 2-Month GitHub Contribution Line Graph SVG.
Recreated faithfully from the user's reference design (Image 1):
- Solid dark background (#000000)
- Centered bright cyan title with sparkles
- Cyan-and-magenta theme:
  - Bright neon magenta connecting line (#D500F9 / #E040FB)
  - White circular vertex data points (#FFFFFF)
  - Bright cyan axis labels, tick numbers, and day numbers (#00E5FF)
  - Cyan dotted horizontal and vertical grid lines
  - Subtle dark area fill below the line
- Retrieves actual public contribution telemetry for Diyan4444 (last 60 days)
- Handles GraphQL API (with GITHUB_TOKEN in CI) and public HTTPS fallback
"""

import os
from pathlib import Path
import urllib.request
import json
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Exact colors from reference Image 1
COLOR_BG = "#000000"
COLOR_TITLE = "#00E5FF"       # Bright Cyan
COLOR_SPARKLE = "#F59E0B"     # Amber Gold
COLOR_AXIS = "#00E5FF"        # Bright Cyan
COLOR_TICKS = "#00E5FF"       # Bright Cyan
COLOR_LINE = "#E040FB"        # Bright Neon Magenta
COLOR_POINT = "#FFFFFF"       # Solid White
GRID_CYAN = "#00E5FF"         # Cyan Dotted Grid
BORDER_COLOR = "#00E5FF"      # Subtle border

def fetch_contributions_graphql(username="Diyan4444", token=None):
    """Fetch contribution calendar using GitHub's authenticated GraphQL API."""
    if not token:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        return None
    
    query = """
    query($user: String!) {
      user(login: $user) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Diyan4444-Profile-Workflow"
    }
    payload = json.dumps({"query": query, "variables": {"user": username}}).encode("utf-8")
    try:
        req = urllib.request.Request(url, data=payload, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            calendar = data.get("data", {}).get("user", {}).get("contributionsCollection", {}).get("contributionCalendar", {})
            weeks = calendar.get("weeks", [])
            days = []
            for w in weeks:
                for d in w.get("contributionDays", []):
                    days.append({"date": d["date"], "count": d["contributionCount"]})
            if days:
                print(f"[GraphQL] Successfully fetched {len(days)} contribution days for {username}")
                return days
    except Exception as e:
        print(f"[GraphQL] API request failed ({e}), falling back to public endpoint...")
    return None

def fetch_contributions_public(username="Diyan4444"):
    """Fetch contribution calendar from maintained public endpoint."""
    url = f"https://github-contributions-api.jogruber.de/v4/{username}?y=last"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            days = data.get("contributions", [])
            if days:
                print(f"[Public API] Successfully fetched {len(days)} contribution days for {username}")
                return days
    except Exception as e:
        print(f"[Public API] Request failed ({e})")
    return None

def get_60_day_contributions(username="Diyan4444"):
    """Retrieve exactly the last 60 days of contribution data with fallbacks."""
    days = fetch_contributions_graphql(username)
    if not days:
        days = fetch_contributions_public(username)
    
    if not days:
        # Fallback to cached file if exists
        cache_file = ASSETS_DIR / "contributions_cache.json"
        if cache_file.exists():
            print("[Cache] Using cached contribution telemetry")
            days = json.loads(cache_file.read_text(encoding="utf-8"))
        else:
            print("[Error] No contribution data could be retrieved.")
            return []
            
    # Save cache for resilience
    try:
        (ASSETS_DIR / "contributions_cache.json").write_text(json.dumps(days), encoding="utf-8")
    except Exception:
        pass
        
    return days[-60:] if len(days) >= 60 else days

def generate_activity_graph_svg(username="Diyan4444"):
    days = get_60_day_contributions(username)
    if not days:
        print("Cannot render graph: empty dataset")
        return None

    counts = [d.get("count", 0) for d in days]
    max_count = max(counts) if max(counts) > 0 else 6
    
    # In Image 1, Y ticks are scaled to 6. For Diyan (max 19), scale evenly up to 20: 0, 4, 8, 12, 16, 20
    if max_count <= 6:
        y_max = 6
        ticks = [0, 1, 2, 3, 4, 5, 6]
    elif max_count <= 10:
        y_max = 10
        ticks = [0, 2, 4, 6, 8, 10]
    elif max_count <= 20:
        y_max = 20
        ticks = [0, 4, 8, 12, 16, 20]
    else:
        step_val = ((max_count // 5) + 1)
        y_max = step_val * 5
        ticks = [i * step_val for i in range(6)]

    # Layout dimensions matching Image 1 aspect ratio
    width = 880
    height = 250
    x_start = 68
    x_end = 845
    y_top = 58
    y_bottom = 202
    
    plot_width = x_end - x_start
    plot_height = y_bottom - y_top
    
    num_pts = len(days)
    dx = plot_width / (num_pts - 1) if num_pts > 1 else plot_width
    
    points = []
    for i, d in enumerate(days):
        c = d.get("count", 0)
        px = x_start + i * dx
        py = y_bottom - (c / y_max) * plot_height
        points.append((px, py, c, d.get("date", "")))

    # Line and Area SVG paths
    line_d = f"M {points[0][0]:.2f} {points[0][1]:.2f}"
    for px, py, _, _ in points[1:]:
        line_d += f" L {px:.2f} {py:.2f}"

    area_d = f"M {points[0][0]:.2f} {y_bottom:.2f} L {points[0][0]:.2f} {points[0][1]:.2f}"
    for px, py, _, _ in points[1:]:
        area_d += f" L {px:.2f} {py:.2f}"
    area_d += f" L {points[-1][0]:.2f} {y_bottom:.2f} Z"

    # Horizontal Cyan Dotted Grid Lines and Y-Axis numbers
    h_grid_lines = []
    y_tick_labels = []
    for t in ticks:
        ty = y_bottom - (t / y_max) * plot_height
        h_grid_lines.append(
            f'<line x1="{x_start}" y1="{ty:.2f}" x2="{x_end}" y2="{ty:.2f}" stroke="{GRID_CYAN}" stroke-width="0.75" stroke-dasharray="2, 4" stroke-opacity="0.30"/>'
        )
        y_tick_labels.append(
            f'<text x="{x_start - 12}" y="{ty + 4:.2f}" class="axis-number" text-anchor="end">{t}</text>'
        )

    # Vertical Cyan Dotted Grid Lines and X-Axis day numbers (day of the month)
    v_grid_lines = []
    x_day_labels = []
    for px, py, c, dt_str in points:
        v_grid_lines.append(
            f'<line x1="{px:.2f}" y1="{y_top}" x2="{px:.2f}" y2="{y_bottom}" stroke="{GRID_CYAN}" stroke-width="0.75" stroke-dasharray="2, 4" stroke-opacity="0.18"/>'
        )
        dt_day = dt_str.split("-")[-1].lstrip("0") or "0"
        x_day_labels.append(
            f'<text x="{px:.2f}" y="{y_bottom + 15}" class="day-number" text-anchor="middle">{dt_day}</text>'
        )

    # Solid White Circular Data Markers at EVERY point (matching Image 1)
    markers = []
    for px, py, c, dt_str in points:
        tooltip = f"{c} contribution{'s' if c != 1 else ''} on {dt_str}"
        markers.append(
            f'<circle class="data-dot" cx="{px:.2f}" cy="{py:.2f}" r="3" fill="{COLOR_POINT}"><title>{tooltip}</title></circle>'
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <!-- Dark Subtle Area Gradient under line -->
    <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_LINE}" stop-opacity="0.28"/>
      <stop offset="65%" stop-color="#1a0b1f" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{COLOR_BG}" stop-opacity="0.0"/>
    </linearGradient>

    <!-- Subtle Line Glow -->
    <filter id="lineGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <style>
      .title-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 15.5px;
        font-weight: 700;
        fill: {COLOR_TITLE};
        letter-spacing: 0.4px;
      }}
      .sparkle {{
        fill: {COLOR_SPARKLE};
        font-size: 16px;
      }}
      .axis-label {{
        font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
        font-size: 11px;
        font-weight: 700;
        fill: {COLOR_AXIS};
        letter-spacing: 0.8px;
      }}
      .axis-number {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10px;
        fill: {COLOR_TICKS};
        font-weight: 600;
      }}
      .day-number {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 8.5px;
        fill: {COLOR_TICKS};
        font-weight: 600;
      }}
      .data-dot {{
        transition: r 0.2s;
        cursor: pointer;
      }}
      .data-dot:hover {{
        r: 5;
        fill: #00E5FF;
      }}
    </style>
  </defs>

  <!-- Pitch Black Card Background (Image 1) -->
  <rect width="{width}" height="{height}" rx="10" fill="{COLOR_BG}"/>

  <!-- Centered Bright Cyan Header with Amber Sparkles -->
  <g transform="translate({width / 2}, 28)" text-anchor="middle">
    <text class="title-text">
      <tspan class="sparkle">&#x2728; </tspan>
      Diyan&apos;s 2-Month Contribution Graph
      <tspan class="sparkle"> &#x2728;</tspan>
    </text>
  </g>

  <!-- Cyan Dotted Horizontal Grid Lines -->
  {''.join(h_grid_lines)}

  <!-- Cyan Dotted Vertical Grid Lines -->
  {''.join(v_grid_lines)}

  <!-- Y-Axis Number Labels -->
  {''.join(y_tick_labels)}

  <!-- X-Axis Day Number Labels -->
  {''.join(x_day_labels)}

  <!-- Left Vertical Axis Label: "Contributions" -->
  <text transform="translate(20, {(y_top + y_bottom) / 2}) rotate(-90)" class="axis-label" text-anchor="middle">
    Contributions
  </text>

  <!-- Bottom Horizontal Axis Label: "Days" -->
  <text x="{(x_start + x_end) / 2}" y="{height - 8}" class="axis-label" text-anchor="middle">
    Days
  </text>

  <!-- Subtle Shaded Area Under Curve -->
  <path d="{area_d}" fill="url(#areaGradient)"/>

  <!-- Bright Neon Magenta Connecting Line with Soft Glow -->
  <path d="{line_d}" fill="none" stroke="{COLOR_LINE}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round" filter="url(#lineGlow)"/>

  <!-- Solid White Circular Markers at Every Vertex (Image 1) -->
  {''.join(markers)}
</svg>'''

    out_file = ASSETS_DIR / "contribution-graph.svg"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {out_file.name} successfully! (Points: {len(points)}, Y-Max: {y_max}, Date Range: {days[0]['date']} to {days[-1]['date']})")
    return out_file

if __name__ == "__main__":
    generate_activity_graph_svg()
