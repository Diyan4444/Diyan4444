"""
Generates an Activity Line & Area Contribution Graph SVG matching Diyan Shah's Flame/Ember theme,
inspired directly by the github-readme-activity-graph reference design.
Fetches public GitHub contribution telemetry and renders a 2-month activity timeline.
"""

from pathlib import Path
import urllib.request
import json
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Flame & Ember Theme Palette
BG_DARK = "#0a0b0e"
BG_SURFACE = "#12141a"
BORDER_SUBTLE = "#331c22"
LINE_COLOR_1 = "#ff3355"  # Crimson Red
LINE_COLOR_2 = "#ff6b35"  # Blaze Orange
AREA_COLOR_1 = "#ff3355"
AREA_COLOR_2 = "#ff6b35"
POINT_FILL = "#ffffff"
POINT_STROKE = "#ff3355"
TEXT_TITLE = "#ffffff"
TEXT_SPARKLE = "#f59e0b"
TEXT_AXIS = "#ff6b35"
TEXT_TICKS = "#94a3b8"
GRID_LINE = "#221922"
GRID_DOT = "#1c141d"

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

def generate_activity_graph_svg(username="Diyan4444", days_count=60):
    data = fetch_contributions(username)
    all_days = []
    if data and "contributions" in data:
        all_days = data["contributions"]
    
    # Take the last `days_count` days
    days = all_days[-days_count:] if len(all_days) >= days_count else all_days
    if not days:
        print("Error: No contribution days retrieved.")
        return None
    
    counts = [d.get("count", 0) for d in days]
    max_count = max(counts) if max(counts) > 0 else 5
    
    # Round max_count up to a nice round number for ticks (e.g. 6, 8, 10, 15, 20)
    if max_count <= 6:
        y_max = 6
        ticks = [0, 1, 2, 3, 4, 5, 6]
    elif max_count <= 10:
        y_max = 10
        ticks = [0, 2, 4, 6, 8, 10]
    elif max_count <= 15:
        y_max = 15
        ticks = [0, 3, 6, 9, 12, 15]
    elif max_count <= 20:
        y_max = 20
        ticks = [0, 4, 8, 12, 16, 20]
    else:
        y_max = ((max_count // 5) + 1) * 5
        step_val = y_max // 5
        ticks = [i * step_val for i in range(6)]

    # Layout coordinates
    width = 880
    height = 270
    x_start = 68
    x_end = 845
    y_top = 62
    y_bottom = 212
    
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
        
    # Build area path and line path
    line_d = f"M {points[0][0]:.2f} {points[0][1]:.2f}"
    for px, py, _, _ in points[1:]:
        line_d += f" L {px:.2f} {py:.2f}"
        
    area_d = f"M {points[0][0]:.2f} {y_bottom:.2f} L {points[0][0]:.2f} {points[0][1]:.2f}"
    for px, py, _, _ in points[1:]:
        area_d += f" L {px:.2f} {py:.2f}"
    area_d += f" L {points[-1][0]:.2f} {y_bottom:.2f} Z"
    
    # Horizontal grid lines and Y-axis numbers
    h_grid_lines = []
    y_tick_labels = []
    for t in ticks:
        ty = y_bottom - (t / y_max) * plot_height
        h_grid_lines.append(f'<line x1="{x_start}" y1="{ty:.2f}" x2="{x_end}" y2="{ty:.2f}" stroke="{GRID_LINE}" stroke-width="0.9" stroke-dasharray="3, 3"/>')
        y_tick_labels.append(f'<text x="{x_start - 12}" y="{ty + 4:.2f}" class="axis-number" text-anchor="end">{t}</text>')
        
    # Vertical grid lines and X-axis day numbers
    v_grid_lines = []
    x_day_labels = []
    for i, (px, py, c, dt_str) in enumerate(points):
        # Vertical dotted line
        v_grid_lines.append(f'<line x1="{px:.2f}" y1="{y_top}" x2="{px:.2f}" y2="{y_bottom}" stroke="{GRID_DOT}" stroke-width="0.8" stroke-dasharray="2, 4"/>')
        # Day number (e.g. "25", "1")
        dt_day = dt_str.split("-")[-1].lstrip("0") or "0"
        x_day_labels.append(f'<text x="{px:.2f}" y="{y_bottom + 16}" class="day-number" text-anchor="middle">{dt_day}</text>')
        
    # Circle markers for points
    circles = []
    for px, py, c, dt_str in points:
        tooltip = f"{c} contribution{'s' if c != 1 else ''} on {dt_str}"
        circles.append(f'<circle class="point-dot" cx="{px:.2f}" cy="{py:.2f}" r="3.2" fill="{POINT_FILL}" stroke="{POINT_STROKE}" stroke-width="1.6"><title>{tooltip}</title></circle>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="60%" stop-color="{BG_SURFACE}"/>
      <stop offset="100%" stop-color="#140d12"/>
    </linearGradient>

    <!-- Line Gradient (Crimson Red to Blaze Orange) -->
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{LINE_COLOR_1}"/>
      <stop offset="50%" stop-color="{LINE_COLOR_2}"/>
      <stop offset="100%" stop-color="{LINE_COLOR_1}"/>
    </linearGradient>

    <!-- Area Gradient under Curve -->
    <linearGradient id="areaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{AREA_COLOR_1}" stop-opacity="0.50"/>
      <stop offset="60%" stop-color="{AREA_COLOR_2}" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="{BG_DARK}" stop-opacity="0.0"/>
    </linearGradient>

    <!-- Pulsing Glow Filter for Line -->
    <filter id="flameGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <style>
      .main-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 15px;
        font-weight: 700;
        fill: {TEXT_TITLE};
        letter-spacing: 0.5px;
      }}
      .sparkle {{
        fill: {TEXT_SPARKLE};
        font-size: 16px;
      }}
      .axis-title {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11.5px;
        font-weight: 700;
        fill: {TEXT_AXIS};
        letter-spacing: 0.8px;
      }}
      .axis-number {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10.5px;
        fill: {TEXT_TICKS};
        font-weight: 600;
      }}
      .day-number {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 8.5px;
        fill: {TEXT_TICKS};
        font-weight: 500;
      }}
      .point-dot {{
        transition: r 0.2s, stroke 0.2s;
        cursor: pointer;
      }}
      .point-dot:hover {{
        r: 5.5;
        stroke: #ffffff;
        stroke-width: 2.2;
      }}
    </style>
  </defs>

  <!-- Card Background & Border -->
  <rect width="{width}" height="{height}" rx="12" fill="url(#bgGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Centered Top Header -->
  <g transform="translate({width / 2}, 30)" text-anchor="middle">
    <text class="main-title">
      <tspan class="sparkle">&#x2728; </tspan>
      Diyan&apos;s 2-Month Contribution Graph
      <tspan class="sparkle"> &#x2728;</tspan>
    </text>
  </g>

  <!-- Horizontal Grid Lines -->
  {''.join(h_grid_lines)}

  <!-- Vertical Grid Lines -->
  {''.join(v_grid_lines)}

  <!-- Y-Axis Number Labels -->
  {''.join(y_tick_labels)}

  <!-- X-Axis Day Number Labels -->
  {''.join(x_day_labels)}

  <!-- Y-Axis Label: "Contributions" (Rotated 90 deg) -->
  <text transform="translate(22, {(y_top + y_bottom) / 2}) rotate(-90)" class="axis-title" text-anchor="middle">
    Contributions
  </text>

  <!-- X-Axis Label: "Days" (Centered at Bottom) -->
  <text x="{(x_start + x_end) / 2}" y="{height - 10}" class="axis-title" text-anchor="middle">
    Days
  </text>

  <!-- Shaded Area Under Curve -->
  <path d="{area_d}" fill="url(#areaGrad)"/>

  <!-- Glowing Underline Wave -->
  <path d="{line_d}" fill="none" stroke="{LINE_COLOR_1}" stroke-width="4.5" stroke-opacity="0.3" filter="url(#flameGlow)"/>

  <!-- Main Flame Line -->
  <path d="{line_d}" fill="none" stroke="url(#lineGrad)" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>

  <!-- Data Point Circles with Tooltips -->
  {''.join(circles)}
</svg>'''

    out_file = ASSETS_DIR / "contribution-graph.svg"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {out_file.name} successfully as a 2-Month Activity Line & Area Graph! (Points: {len(points)}, Y-Max: {y_max})")
    return out_file

if __name__ == "__main__":
    generate_activity_graph_svg()
