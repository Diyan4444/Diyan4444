"""
Dusk Workspace Asset Generator for Diyan Shah's GitHub Profile
Aesthetic: Calm, warm, soothing personal notebook / quiet workspace.
Colours:
- Slate & Deep Charcoal background: #111622 / #161c28
- Card Surface: #18202d
- Borders: #253042
- Warm Ivory text: #f1ede6
- Slate silver text: #94a3b8 / #78889c
- Accent 1 (Warm Peach / Muted Coral): #ea937d / #f09a85
- Accent 2 (Sage / Soft Teal): #7eb2a8 / #86b9ac
- Accent 3 (Mellow Amber / Sand): #dfb17b / #e4be8f
"""

from pathlib import Path
import urllib.request
import json
import os
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Dusk Palette
BG_DARK = "#111622"
BG_SURFACE = "#161c28"
BG_CARD = "#192230"
BORDER_SUBTLE = "#253245"
BORDER_LIGHT = "#314159"
TEXT_TITLE = "#f1ede6"
TEXT_BODY = "#c7d2df"
TEXT_MUTED = "#8696a7"
ACCENT_PEACH = "#ea937d"
ACCENT_SAGE = "#7eb2a8"
ACCENT_AMBER = "#dfb17b"
ACCENT_TEAL = "#64a6bd"

def fetch_contributions(username="Diyan4444"):
    """Fetch real contribution activity with caching."""
    cache_path = ASSETS_DIR / "contributions_cache.json"
    url = f"https://github-contributions-api.jogruber.de/v4/{username}?y=last"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data and "contributions" in data:
                cache_path.write_text(json.dumps(data), encoding="utf-8")
                return data
    except Exception as e:
        print(f"[Notice] Contribution fetch failed ({e}), checking cache...")
    
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return None

def fetch_github_user_stats(username="Diyan4444"):
    """Fetch GitHub profile stats for repos, followers, languages, commits, PRs, and issues."""
    cache_path = ASSETS_DIR / "github_stats_cache.json"
    
    # Baseline defaults if cache does not exist
    stats = {
        "public_repos": 26,
        "followers": 1,
        "following": 1,
        "total_stars": 11,
        "total_contributions": 241,
        "total_commits": 163,
        "pull_requests": 9,
        "issues": 1,
        "current_streak": 9,
        "longest_streak": 13,
        "top_languages": [
            ("TypeScript", 66.5),
            ("JavaScript", 16.4),
            ("C++", 7.4),
            ("Python", 5.1),
        ]
    }

    # Load existing cached stats if available so we always preserve last good values
    if cache_path.exists():
        try:
            cached_data = json.loads(cache_path.read_text(encoding="utf-8"))
            if isinstance(cached_data, dict):
                stats.update(cached_data)
        except Exception:
            pass

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        # 1. User profile stats
        user_req = urllib.request.Request(f"https://api.github.com/users/{username}", headers=headers)
        with urllib.request.urlopen(user_req, timeout=10) as resp:
            u_data = json.loads(resp.read().decode("utf-8"))
            stats["public_repos"] = u_data.get("public_repos", stats["public_repos"])
            stats["followers"] = u_data.get("followers", stats["followers"])
            stats["following"] = u_data.get("following", stats["following"])

        # 2. Dynamic language calculation across authored (non-forked) repositories
        repo_req = urllib.request.Request(f"https://api.github.com/users/{username}/repos?per_page=100", headers=headers)
        with urllib.request.urlopen(repo_req, timeout=12) as resp:
            repos = json.loads(resp.read().decode("utf-8"))
            stars = sum(r.get("stargazers_count", 0) for r in repos)
            stats["total_stars"] = stars

            lang_bytes = {}
            for r in repos:
                # Calculate real languages exclusively from non-forked repos to reflect authored work
                if not r.get("fork", False):
                    l_url = r.get("languages_url")
                    if l_url:
                        try:
                            l_req = urllib.request.Request(l_url, headers=headers)
                            with urllib.request.urlopen(l_req, timeout=5) as l_resp:
                                l_data = json.loads(l_resp.read().decode("utf-8"))
                                for l_name, b_count in l_data.items():
                                    lang_bytes[l_name] = lang_bytes.get(l_name, 0) + b_count
                        except Exception:
                            pass

            tot_bytes = sum(lang_bytes.values())
            if tot_bytes > 0:
                sorted_l = sorted(lang_bytes.items(), key=lambda x: x[1], reverse=True)
                top_langs = []
                for l_name, b_count in sorted_l[:4]:
                    pct = round((b_count / tot_bytes) * 100, 1)
                    top_langs.append((l_name, pct))
                if top_langs:
                    stats["top_languages"] = top_langs

        # 3. Pull requests count via search API
        try:
            pr_req = urllib.request.Request(f"https://api.github.com/search/issues?q=author:{username}+type:pr", headers=headers)
            with urllib.request.urlopen(pr_req, timeout=10) as resp:
                stats["pull_requests"] = json.loads(resp.read().decode("utf-8")).get("total_count", stats.get("pull_requests", 9))
        except Exception:
            pass

        # 4. Issues count via search API
        try:
            iss_req = urllib.request.Request(f"https://api.github.com/search/issues?q=author:{username}+type:issue", headers=headers)
            with urllib.request.urlopen(iss_req, timeout=10) as resp:
                stats["issues"] = json.loads(resp.read().decode("utf-8")).get("total_count", stats.get("issues", 1))
        except Exception:
            pass

        # 5. Commits count via search API
        try:
            commit_headers = {**headers, "Accept": "application/vnd.github.cloak-preview"}
            com_req = urllib.request.Request(f"https://api.github.com/search/commits?q=author:{username}", headers=commit_headers)
            with urllib.request.urlopen(com_req, timeout=10) as resp:
                stats["total_commits"] = json.loads(resp.read().decode("utf-8")).get("total_count", stats.get("total_commits", 163))
        except Exception:
            pass

        # Persist successful telemetry to cache so future rate limits preserve last good state
        cache_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    except Exception as e:
        print(f"[Notice] User stats API fetch encountered ({e}); safely keeping last good cached metrics.")

    return stats


# ==============================================================================
# 1. HERO BANNER — "Notebook Cover Aesthetic"
# ==============================================================================
def generate_hero_banner():
    """
    Generates a calm, warm opening banner.
    Feels like the cover of a well-kept developer notebook.
    Features:
    - Subtle textured grid & soft gradient
    - Name in warm ivory with quiet peach glow
    - 'B.Tech IT sophomore at VJTI Mumbai'
    - Short, honest summary line
    - Quiet strip of core technology
    - Very slow, gentle ambient breathing pulse
    """
    width = 960
    height = 240
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="bannerBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="50%" stop-color="{BG_SURFACE}"/>
      <stop offset="100%" stop-color="#141924"/>
    </linearGradient>

    <linearGradient id="warmRule" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ACCENT_PEACH}" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="{ACCENT_AMBER}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{ACCENT_SAGE}" stop-opacity="0.4"/>
    </linearGradient>

    <pattern id="softGrid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="0.75" stroke-opacity="0.45"/>
    </pattern>

    <style>
      .name-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif;
        font-size: 34px;
        font-weight: 700;
        fill: {TEXT_TITLE};
        letter-spacing: 0.5px;
      }}
      .edu-sub {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 15px;
        font-weight: 500;
        fill: {ACCENT_PEACH};
        letter-spacing: 0.2px;
      }}
      .intro-line {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13.5px;
        fill: {TEXT_MUTED};
        line-height: 1.5;
      }}
      .tech-chip-text {{
        font-family: 'JetBrains Mono', Consolas, 'SF Mono', monospace;
        font-size: 11px;
        font-weight: 500;
        fill: {TEXT_BODY};
      }}
      .tag-quiet {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10.5px;
        font-weight: 600;
        fill: {ACCENT_SAGE};
        letter-spacing: 0.6px;
      }}
    </style>
  </defs>

  <!-- Card Background -->
  <rect width="{width}" height="{height}" rx="12" fill="url(#bannerBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
  <rect width="{width}" height="{height}" rx="12" fill="url(#softGrid)"/>

  <!-- Left Accent Notch (Notebook Spine Detail) -->
  <line x1="0" y1="20" x2="0" y2="220" stroke="{ACCENT_PEACH}" stroke-width="4" stroke-linecap="round"/>

  <!-- Top Status / Discipline Pill -->
  <g transform="translate(48, 30)">
    <rect width="180" height="24" rx="12" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    <circle cx="12" cy="12" r="3.5" fill="{ACCENT_SAGE}">
      <animate attributeName="opacity" values="0.5; 1; 0.5" dur="4s" repeatCount="indefinite"/>
    </circle>
    <text x="24" y="15.5" class="tag-quiet">DIYAN SHAH • MUMBAI</text>
  </g>

  <!-- Main Headline Block -->
  <g transform="translate(48, 76)">
    <text x="0" y="24" class="name-title">Diyan Shah</text>
    <text x="195" y="22" class="edu-sub">B.Tech IT sophomore at VJTI Mumbai</text>
    
    <text x="0" y="54" class="intro-line">
      I build full-stack web applications, browser tools, and hackathon prototypes.
    </text>
    <text x="0" y="73" class="intro-line">
      I like projects that solve one real problem well, and I learn best by shipping them.
    </text>
  </g>

  <!-- Calming Horizon Rule -->
  <line x1="48" y1="180" x2="{width - 48}" y2="180" stroke="url(#warmRule)" stroke-width="1"/>

  <!-- Quiet Core Tech Strip -->
  <g transform="translate(48, 204)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="10.5" fill="{TEXT_MUTED}" font-weight="600" letter-spacing="0.5">CORE TOOLKIT</text>
    <text x="100" y="0" class="tech-chip-text">
      TypeScript <tspan fill="{BORDER_LIGHT}">•</tspan> C++ (STL) <tspan fill="{BORDER_LIGHT}">•</tspan> Python <tspan fill="{BORDER_LIGHT}">•</tspan> Next.js <tspan fill="{BORDER_LIGHT}">•</tspan> FastAPI <tspan fill="{BORDER_LIGHT}">•</tspan> Node.js <tspan fill="{BORDER_LIGHT}">•</tspan> PostgreSQL <tspan fill="{BORDER_LIGHT}">•</tspan> Docker
    </text>
  </g>

  <!-- Right Notebook Stamp Motif -->
  <g transform="translate({width - 160}, 42)">
    <rect width="112" height="112" rx="10" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    <circle cx="56" cy="56" r="38" fill="none" stroke="{BORDER_LIGHT}" stroke-width="1" stroke-dasharray="3, 3">
      <animateTransform attributeName="transform" type="rotate" from="0 56 56" to="360 56 56" dur="36s" repeatCount="indefinite"/>
    </circle>
    <circle cx="56" cy="56" r="24" fill="none" stroke="{ACCENT_PEACH}" stroke-opacity="0.3" stroke-width="1.2"/>
    <text x="56" y="59" font-family="'JetBrains Mono', monospace" font-size="11" fill="{ACCENT_PEACH}" font-weight="700" text-anchor="middle" letter-spacing="1">VJTI</text>
  </g>
</svg>'''

    out_file = ASSETS_DIR / "hero-banner.svg"
    out_file.write_text(svg, encoding="utf-8")
    print(f"Generated {out_file.name}")
    return out_file


# ==============================================================================
# 2. MONTHLY CONTRIBUTION GRAPH — Exact specifications from Section 5
# ==============================================================================
def generate_monthly_contribution_graph(username="Diyan4444"):
    """
    Generates the Monthly Contribution Graph SVG.
    Strict specifications:
    - EXACT Title shown to visitors: "Monthly Contribution Graph"
      (never mentions '1-month', '2-month', '30 days', or numbers in title/text).
    - Rolling ~30 days of real GitHub contribution activity.
    - Rhythm line graph with gentle peaks and soft baseline.
    - Paired with a small calendar-style view of soft tiles that get warmer/deeper in color.
    - 4 friendly summary figures:
      1. Total contributions
      2. Active days
      3. Best day (softly highlighted)
      4. Daily average
    - Soft, soothing dusk theme.
    """
    data = fetch_contributions(username)
    all_days = data.get("contributions", []) if data else []
    
    # 30 rolling days
    days = all_days[-30:] if len(all_days) >= 30 else all_days
    if not days:
        print("[Warning] No contribution days found for Monthly Contribution Graph")
        return None

    counts = [d.get("count", 0) for d in days]
    total_contribs = sum(counts)
    active_days_count = sum(1 for c in counts if c > 0)
    best_item = max(days, key=lambda x: x.get("count", 0))
    best_count = best_item.get("count", 0)
    best_date_str = best_item.get("date", "")
    
    # Format best date e.g. "Oct 8"
    try:
        dt_best = datetime.strptime(best_date_str, "%Y-%m-%d")
        best_formatted = dt_best.strftime("%b %d").replace(" 0", " ")
    except Exception:
        best_formatted = best_date_str

    daily_avg = total_contribs / len(days) if days else 0.0

    width = 960
    height = 330
    
    # Line graph layout
    gx_start = 68
    gx_end = 900
    gy_top = 80
    gy_bottom = 195
    gw = gx_end - gx_start
    gh = gy_bottom - gy_top
    
    max_c = max(counts) if max(counts) > 0 else 6
    if max_c <= 6:
        y_max = 6
        ticks = [0, 2, 4, 6]
    elif max_c <= 12:
        y_max = 12
        ticks = [0, 4, 8, 12]
    elif max_c <= 16:
        y_max = 16
        ticks = [0, 4, 8, 12, 16]
    else:
        y_max = ((max_c // 4) + 1) * 4
        ticks = [0, y_max // 4, y_max // 2, (y_max * 3) // 4, y_max]

    num_pts = len(days)
    dx = gw / (num_pts - 1) if num_pts > 1 else gw
    
    points = []
    for i, d in enumerate(days):
        c = d.get("count", 0)
        px = gx_start + i * dx
        py = gy_bottom - (c / y_max) * gh
        points.append((px, py, c, d.get("date", "")))

    # Smooth curve construction
    line_d = f"M {points[0][0]:.2f} {points[0][1]:.2f}"
    for px, py, _, _ in points[1:]:
        line_d += f" L {px:.2f} {py:.2f}"

    area_d = f"M {points[0][0]:.2f} {gy_bottom:.2f} L {points[0][0]:.2f} {points[0][1]:.2f}"
    for px, py, _, _ in points[1:]:
        area_d += f" L {px:.2f} {py:.2f}"
    area_d += f" L {points[-1][0]:.2f} {gy_bottom:.2f} Z"

    # Grid lines & Y tick numbers
    grid_lines = []
    y_tick_svg = []
    for t in ticks:
        ty = gy_bottom - (t / y_max) * gh
        grid_lines.append(f'<line x1="{gx_start}" y1="{ty:.2f}" x2="{gx_end}" y2="{ty:.2f}" stroke="{BORDER_SUBTLE}" stroke-width="0.8" stroke-dasharray="2, 4"/>')
        y_tick_svg.append(f'<text x="{gx_start - 10}" y="{ty + 3.5:.2f}" font-family="\'JetBrains Mono\', monospace" font-size="9.5" fill="{TEXT_MUTED}" text-anchor="end">{t}</text>')

    # Graph point markers
    markers = []
    for px, py, c, dt_str in points:
        is_best = (c == best_count and c > 0)
        r = "4.2" if is_best else "2.8"
        fill = ACCENT_AMBER if is_best else (TEXT_TITLE if c > 0 else TEXT_MUTED)
        stroke = ACCENT_PEACH if is_best else BG_DARK
        tooltip = f"{c} contribution{'s' if c != 1 else ''} on {dt_str}"
        markers.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"><title>{tooltip}</title></circle>')

    # Calendar View Tiles (row of 30 soft tiles along the bottom)
    tile_w = 21
    tile_h = 16
    tile_gap = 6
    total_tiles_w = len(days) * (tile_w + tile_gap) - tile_gap
    cal_x_start = gx_start + (gw - total_tiles_w) / 2
    cal_y = 265
    
    cal_tiles = []
    # Color scale from quiet slate to warm coral
    # level 0: #1a2230, level 1: #2d3b45 (sage muted), level 2: #5c4a45 (warm), level 3: #b86a55 (coral), level 4: #ea937d (peach)
    TILE_COLORS = ["#1a2332", "#2e404b", "#6b4946", "#b86754", "#ea937d"]
    
    for i, d in enumerate(days):
        c = d.get("count", 0)
        # determine level
        if c == 0:
            lvl = 0
        elif c <= 2:
            lvl = 1
        elif c <= 5:
            lvl = 2
        elif c <= 8:
            lvl = 3
        else:
            lvl = 4
        color = TILE_COLORS[lvl]
        tx = cal_x_start + i * (tile_w + tile_gap)
        is_best = (c == best_count and c > 0)
        stroke_attr = f'stroke="{ACCENT_AMBER}" stroke-width="1.2"' if is_best else f'stroke="{BORDER_SUBTLE}" stroke-width="0.8"'
        
        # Day of month
        day_num = d.get("date", "").split("-")[-1].lstrip("0") or "0"
        cal_tiles.append(f'<g transform="translate({tx:.1f}, {cal_y})">')
        cal_tiles.append(f'  <rect width="{tile_w}" height="{tile_h}" rx="3" fill="{color}" {stroke_attr}><title>{c} on {d.get("date", "")}</title></rect>')
        cal_tiles.append(f'  <text x="{tile_w/2}" y="26" font-family="\'JetBrains Mono\', monospace" font-size="8" fill="{TEXT_MUTED}" text-anchor="middle">{day_num}</text>')
        cal_tiles.append('</g>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="mgBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>

    <linearGradient id="graphLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ACCENT_SAGE}"/>
      <stop offset="50%" stop-color="{ACCENT_PEACH}"/>
      <stop offset="100%" stop-color="{ACCENT_AMBER}"/>
    </linearGradient>

    <linearGradient id="graphArea" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{ACCENT_PEACH}" stop-opacity="0.22"/>
      <stop offset="60%" stop-color="{ACCENT_SAGE}" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="{BG_DARK}" stop-opacity="0.0"/>
    </linearGradient>

    <style>
      .graph-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 15px;
        font-weight: 700;
        fill: {TEXT_TITLE};
        letter-spacing: 0.3px;
      }}
      .stat-val {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 13.5px;
        font-weight: 700;
        fill: {TEXT_TITLE};
      }}
      .stat-lbl {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 11px;
        fill: {TEXT_MUTED};
      }}
      .section-sub {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10px;
        fill: {ACCENT_SAGE};
        letter-spacing: 0.8px;
        font-weight: 600;
      }}
    </style>
  </defs>

  <!-- Frame Background -->
  <rect width="{width}" height="{height}" rx="12" fill="url(#mgBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header with EXACT title requested in Section 5 -->
  <g transform="translate(40, 32)">
    <circle cx="0" cy="-2" r="4" fill="{ACCENT_PEACH}"/>
    <text x="14" y="2" class="graph-title">Monthly Contribution Graph</text>
  </g>

  <!-- 4 Summary Figures (Right aligned in header) -->
  <!-- Figure 1: Total -->
  <g transform="translate(390, 24)">
    <text x="0" y="0" class="stat-lbl">Contributions</text>
    <text x="0" y="16" class="stat-val" fill="{ACCENT_PEACH}">{total_contribs}</text>
  </g>

  <!-- Figure 2: Active Days -->
  <g transform="translate(520, 24)">
    <text x="0" y="0" class="stat-lbl">Active Days</text>
    <text x="0" y="16" class="stat-val">{active_days_count} / {len(days)}</text>
  </g>

  <!-- Figure 3: Best Day (Softly Highlighted) -->
  <g transform="translate(650, 24)">
    <rect x="-6" y="-12" width="125" height="34" rx="6" fill="{BG_CARD}" stroke="{ACCENT_AMBER}" stroke-width="0.9" stroke-opacity="0.6"/>
    <text x="0" y="0" class="stat-lbl" fill="{ACCENT_AMBER}">Best Day • {best_formatted}</text>
    <text x="0" y="16" class="stat-val" fill="{ACCENT_AMBER}">{best_count} commits</text>
  </g>

  <!-- Figure 4: Daily Average -->
  <g transform="translate(805, 24)">
    <text x="0" y="0" class="stat-lbl">Daily Average</text>
    <text x="0" y="16" class="stat-val">{daily_avg:.1f} / day</text>
  </g>

  <!-- Grid Lines -->
  {''.join(grid_lines)}

  <!-- Y Tick Labels -->
  {''.join(y_tick_svg)}

  <!-- Area Fill under curve -->
  <path d="{area_d}" fill="url(#graphArea)"/>

  <!-- Rhythm Line -->
  <path d="{line_d}" fill="none" stroke="url(#graphLine)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>

  <!-- Data Markers -->
  {''.join(markers)}

  <!-- Bottom Divider Line -->
  <line x1="40" y1="230" x2="{width - 40}" y2="230" stroke="{BORDER_SUBTLE}" stroke-width="0.8"/>

  <!-- Calendar Heatmap Row Label -->
  <g transform="translate(40, 252)">
    <text x="0" y="0" class="section-sub">DAILY RHYTHM CALENDAR</text>
  </g>

  <!-- Calendar Heatmap Tiles -->
  {''.join(cal_tiles)}

  <!-- Heatmap Legend (Right aligned at bottom) -->
  <g transform="translate({width - 150}, 248)">
    <text x="-8" y="5" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="{TEXT_MUTED}" text-anchor="end">Less</text>
    <rect x="0" y="-3" width="9" height="9" rx="2" fill="{TILE_COLORS[0]}"/>
    <rect x="13" y="-3" width="9" height="9" rx="2" fill="{TILE_COLORS[1]}"/>
    <rect x="26" y="-3" width="9" height="9" rx="2" fill="{TILE_COLORS[2]}"/>
    <rect x="39" y="-3" width="9" height="9" rx="2" fill="{TILE_COLORS[3]}"/>
    <rect x="52" y="-3" width="9" height="9" rx="2" fill="{TILE_COLORS[4]}"/>
    <text x="68" y="5" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="{TEXT_MUTED}">More</text>
  </g>
</svg>'''

    out_file = ASSETS_DIR / "monthly-contribution-graph.svg"
    out_file.write_text(svg, encoding="utf-8")
    print(f"Generated {out_file.name}")
    return out_file


# ==============================================================================
# 3. GITHUB SUMMARY & TELEMETRY CARD — Auto-updating live numbers
# ==============================================================================
def generate_github_summary(username="Diyan4444"):
    """
    Self-hosted GitHub Summary Card.
    Avoids brittle external Vercel widgets by generating deterministic SVG in repo.
    Includes:
    - Repos count & followers count (auto-updated)
    - Total contributions, stars, current streak, longest streak
    - Top languages breakdown with soft progress bars
    """
    stats = fetch_github_user_stats(username)
    contrib_data = fetch_contributions(username)
    total_contribs = contrib_data.get("total", {}).get("lastYear", stats["total_contributions"]) if contrib_data else stats["total_contributions"]
    
    # Calculate streak from calendar if available
    days = contrib_data.get("contributions", []) if contrib_data else []
    longest_streak = stats["longest_streak"]
    current_streak = stats["current_streak"]
    if days:
        cur = 0
        longest = 0
        streak = 0
        for d in days:
            if d.get("count", 0) > 0:
                streak += 1
                if streak > longest:
                    longest = streak
            else:
                streak = 0
        longest_streak = longest
        
        rev = list(reversed(days))
        start_idx = 1 if (rev and rev[0].get("count", 0) == 0) else 0
        for d in rev[start_idx:]:
            if d.get("count", 0) > 0:
                cur += 1
            else:
                break
        current_streak = cur

    width = 960
    height = 200
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="sumBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>

    <style>
      .sum-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 14.5px;
        font-weight: 700;
        fill: {TEXT_TITLE};
      }}
      .sum-sub {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10px;
        fill: {ACCENT_PEACH};
        letter-spacing: 0.8px;
        font-weight: 600;
      }}
      .card-num {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 26px;
        font-weight: 700;
      }}
      .card-label {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 11px;
        fill: {TEXT_MUTED};
        letter-spacing: 0.2px;
      }}
      .lang-label {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10.5px;
        fill: {TEXT_BODY};
      }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" rx="12" fill="url(#sumBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Section Header -->
  <g transform="translate(40, 30)">
    <text class="sum-sub">ACTIVITY &amp; COMMUNITY SNAPSHOT</text>
    <text y="20" class="sum-title">GitHub Overview &amp; Languages</text>
  </g>

  <!-- Metric Tile 1: Repositories & Followers -->
  <g transform="translate(40, 80)">
    <rect width="160" height="96" rx="8" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    <text x="16" y="24" class="card-label">Repositories &amp; Stars</text>
    <text x="16" y="58" class="card-num" fill="{TEXT_TITLE}">{stats["public_repos"]} <tspan font-size="13" font-weight="500">repos</tspan></text>
    <text x="16" y="80" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="{ACCENT_SAGE}">• {stats["followers"]} follower · {stats["total_stars"]} stars</text>
  </g>

  <!-- Metric Tile 2: Commits & Contributions -->
  <g transform="translate(215, 80)">
    <rect width="160" height="96" rx="8" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    <text x="16" y="24" class="card-label">Commits &amp; Activity</text>
    <text x="16" y="58" class="card-num" fill="{ACCENT_PEACH}">{stats.get("total_commits", 163)} <tspan font-size="13" font-weight="500">commits</tspan></text>
    <text x="16" y="80" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="{TEXT_MUTED}">• {total_contribs} yr contributions</text>
  </g>

  <!-- Metric Tile 3: Pull Requests, Issues & Streak -->
  <g transform="translate(390, 80)">
    <rect width="160" height="96" rx="8" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    <text x="16" y="24" class="card-label">PRs, Issues &amp; Streak</text>
    <text x="16" y="58" class="card-num" fill="{ACCENT_AMBER}">{current_streak} <tspan font-size="13" font-weight="500">day streak</tspan></text>
    <text x="16" y="80" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="{ACCENT_AMBER}">• {stats.get("pull_requests", 9)} PRs · {stats.get("issues", 1)} issue</text>
  </g>

  <!-- Languages Breakdown (Right Card) -->
  <g transform="translate(565, 80)">
    <rect width="355" height="96" rx="8" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    <text x="18" y="22" class="card-label">Authored Languages</text>
    {''.join([
        f'''
    <!-- Language {idx+1}: {l_name} ({pct}%) -->
    <g transform="translate(18, {33 + idx * 15})">
      <text x="0" y="8" class="lang-label">{l_name}</text>
      <text x="110" y="8" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="{TEXT_MUTED}" text-anchor="end">{pct}%</text>
      <rect x="120" y="1" width="195" height="7" rx="3.5" fill="{BG_DARK}"/>
      <rect x="120" y="1" width="{max(4, min(195, round((pct / 100.0) * 195, 1)))}" height="7" rx="3.5" fill="{[ACCENT_PEACH, ACCENT_SAGE, ACCENT_AMBER, ACCENT_TEAL][idx % 4]}"/>
    </g>'''
        for idx, (l_name, pct) in enumerate(stats.get("top_languages", [])[:4])
    ])}
  </g>
</svg>'''

    out_file = ASSETS_DIR / "github-summary.svg"
    out_file.write_text(svg, encoding="utf-8")
    print(f"Generated {out_file.name}")
    return out_file


# ==============================================================================
# 4. RESTYLED ARCHITECTURE DIAGRAMS (Dusk Palette)
# ==============================================================================
def restyle_pipeline_diagrams():
    """
    Restyles the project architecture flow diagrams to match the calm dusk palette.
    These are placed inside the expandable <details> area so they don't crowd the page.
    """
    diagrams = {
        "pipeline-leetvault.svg": {
            "title": "LEET-VAULT • ARCHITECTURAL FLOW (CHROME MV3 EXTENSION)",
            "steps": [
                ("01. SUBMISSION CAPTURE", "Strict submission FSM", "Watches leetcode.com DOM", "Code &amp; runtime snapshot", "TypeScript • Manifest V3", ACCENT_PEACH),
                ("02. MULTI-SOLUTION", "User-defined naming", "Deterministic fallback", "Multi-language mapping", "Vite • Vitest", ACCENT_SAGE),
                ("03. GITHUB SYNC", "Chrome WebAuthFlow", "OAuth broker (zero PAT)", "Direct GitHub REST API", "chrome.identity API", ACCENT_AMBER),
                ("04. RELIABILITY QUEUE", "Chrome alarm retry queue", "Duplicate &amp; SHA match", "Root &amp; problem READMEs", "Chrome Storage API", TEXT_TITLE),
            ]
        },
        "pipeline-glamourly.svg": {
            "title": "GLAMOURLY • ARCHITECTURAL FLOW (MUMBAI SALON PLATFORM)",
            "steps": [
                ("01. SALON DISCOVERY", "Curated Mumbai directory", "Transparent rate cards", "Leaflet geo directions", "Next.js • Tailwind CSS", ACCENT_PEACH),
                ("02. DIRECT BOOKINGS", "Real-time slot lock", "100% pay-at-salon model", "Zero forced prepayment", "React • TypeScript", ACCENT_SAGE),
                ("03. PROVIDER PORTAL", "Staff roster &amp; schedules", "Shop Act statutory check", "Branch appointment board", "MongoDB (Mongoose)", ACCENT_AMBER),
                ("04. INSTANT CONFIRM", "Email booking passes", "Customer history portal", "Direct salon contact link", "NextAuth • Netlify", TEXT_TITLE),
            ]
        },
        "pipeline-oceanguard.svg": {
            "title": "OCEANGUARD AI • ARCHITECTURAL FLOW (SIH 2026)",
            "steps": [
                ("01. SAR SEGMENTATION", "Satellite radar imagery", "Dark slick boundary mask", "AI image segmentation", "NumPy • SciPy", ACCENT_PEACH),
                ("02. DRIFT HINDCAST", "Wind &amp; ocean currents", "Backward-in-time drift", "Origin coordinate solve", "Python • Hydrodynamics", ACCENT_SAGE),
                ("03. AIS CORRELATION", "Global vessel GPS paths", "Spatial-temporal matching", "Speed anomaly detection", "FastAPI • SQLite", ACCENT_AMBER),
                ("04. VESSEL ATTRIBUTION", "AIS blackout analysis", "Ranked suspect scoring", "Dark-tile map visualization", "React 19 • Leaflet", TEXT_TITLE),
            ]
        },
        "pipeline-wellwhisperer.svg": {
            "title": "WELL-WHISPERER • ARCHITECTURAL FLOW (SIH 2026 PS 121)",
            "steps": [
                ("01. OFFSET WELL LOGS", "Historical drilling data", "Wellbore trajectory logs", "Synthetic field benchmarks", "FastAPI • Python 3.12", ACCENT_PEACH),
                ("02. DRILLING INTEL", "Nearby wells correlation", "Formation pressure curves", "Hazard &amp; loss prediction", "NumPy • SciPy • Pandas", ACCENT_SAGE),
                ("03. 3D TRAJECTORY HUD", "Interactive 3D wellbore", "Real-time advisory alerts", "Spatial distance mapping", "React 19 • Three.js", ACCENT_AMBER),
                ("04. PERSISTENT STORAGE", "Offset database storage", "High-performance queries", "eRTMAC operational sync", "Supabase PostgreSQL", TEXT_TITLE),
            ]
        },
        "pipeline-ytconverter.svg": {
            "title": "YT-TO-MP4 • ARCHITECTURAL FLOW (CONTAINERISED WEB APP)",
            "steps": [
                ("01. RESPONSIVE WEB UI", "Dark-mode web client", "Real-time progress &amp; ETA", "Format &amp; bitrate picker", "Vanilla JavaScript", ACCENT_PEACH),
                ("02. FLASK SERVER", "Concurrency limiter", "URL format verification", "Metadata probing &amp; title", "Python • Flask", ACCENT_SAGE),
                ("03. MEDIA TRANSCODING", "Stream video/audio fetch", "MP4 &amp; MP3 conversion", "Lossless audio extract", "yt-dlp • FFmpeg", ACCENT_AMBER),
                ("04. CONTAINER CLOUD", "Multi-worker Gunicorn", "Ephemeral scratch purge", "Production container", "Docker • Gunicorn", TEXT_TITLE),
            ]
        },
        "pipeline-rentwheels.svg": {
            "title": "RENTWHEELS • ARCHITECTURAL FLOW (VEHICLE RENTAL CATALOG)",
            "steps": [
                ("01. SEMANTIC CATALOG", "Structured vehicle markup", "Multi-category layout", "Accessible page hierarchy", "Semantic HTML5", ACCENT_PEACH),
                ("02. RESPONSIVE DESIGN", "Fluid grid &amp; cards", "Clean typography &amp; layout", "Zero CSS framework", "Modern CSS3", ACCENT_SAGE),
                ("03. CLIENT INTERACTION", "Category filtering logic", "Interactive rental cart", "Daily pricing calculation", "Vanilla JavaScript", ACCENT_AMBER),
                ("04. EDGE HOSTING", "Zero runtime dependencies", "Instant asset loading", "Production deployment", "Netlify Edge", TEXT_TITLE),
            ]
        },
        "pipeline-runestriker.svg": {
            "title": "RUNE-STRIKER • ARCHITECTURAL FLOW (2D RETRO PLATFORMER)",
            "steps": [
                ("01. KINEMATIC FSM", "Coyote time jump cushion", "Input buffer queue", "Responsive state machine", "Godot 4.6 • GDScript", ACCENT_PEACH),
                ("02. PATROL AI", "Raycast barrier detection", "Ledge turnaround logic", "Autonomous slime patrol", "2D Vector Physics", ACCENT_SAGE),
                ("03. SIGNAL EVENT BUS", "Decoupled coin pickup signal", "HUD counter refresh", "Audio bus triggers", "Godot Signals", ACCENT_AMBER),
                ("04. DESKTOP RELEASE", "Optimized draw calls", "Asset texture atlas pack", "Standalone Windows .exe", "Windows Executable", TEXT_TITLE),
            ]
        }
    }

    width = 920
    height = 175
    for filename, pdata in diagrams.items():
        step_boxes = []
        for i, (title, l1, l2, l3, tag, color) in enumerate(pdata["steps"]):
            bx = 25 + i * 220
            step_boxes.append(f'''
  <!-- Step {i+1} -->
  <g transform="translate({bx}, 42)">
    <rect width="195" height="110" rx="8" fill="{BG_CARD}" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" font-family="'JetBrains Mono', Consolas, monospace" font-size="10.5" font-weight="700" fill="{color}" letter-spacing="0.5">{title}</text>
    <text x="14" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="{TEXT_BODY}">{l1}</text>
    <text x="14" y="64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="{TEXT_BODY}">{l2}</text>
    <text x="14" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" fill="{TEXT_BODY}">{l3}</text>
    <text x="14" y="100" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5" fill="{TEXT_MUTED}">{tag}</text>
  </g>''')
            if i < 3:
                arrow_x1 = bx + 195
                arrow_x2 = arrow_x1 + 25
                step_boxes.append(f'''
  <line x1="{arrow_x1}" y1="97" x2="{arrow_x2}" y2="97" stroke="{BORDER_LIGHT}" stroke-width="1.5" stroke-dasharray="3, 3"/>
  <polygon points="{arrow_x2},94 {arrow_x2+6},97 {arrow_x2},100" fill="{BORDER_LIGHT}"/>''')

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="pBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
  </defs>

  <rect width="{width}" height="{height}" rx="10" fill="url(#pBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(25, 24)">
    <circle cx="6" cy="4" r="3.5" fill="{ACCENT_PEACH}"/>
    <text x="18" y="8" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" font-weight="600" fill="{TEXT_TITLE}" letter-spacing="0.8">
      {pdata["title"]}
    </text>
  </g>

  {''.join(step_boxes)}
</svg>'''

        out_file = ASSETS_DIR / filename
        out_file.write_text(svg, encoding="utf-8")
        print(f"Generated restyled {out_file.name}")


# ==============================================================================
# 5. RESTYLED CONTRIBUTION SNAKE (Calm Dusk Palette & Soft Card Container)
# ==============================================================================
def generate_calm_contribution_snake(username="Diyan4444"):
    """
    Renders or updates the contribution snake animation with the calm dusk palette.
    Ensures a soft card container background (#161c28) is present so the visual looks
    seamless and crisp in both GitHub Dark and Light modes.
    """
    snake_file = ASSETS_DIR / "github-contribution-grid-snake.svg"
    if snake_file.exists():
        content = snake_file.read_text(encoding="utf-8")
        svg_end = content.find("</svg>")
        if svg_end != -1:
            content = content[:svg_end + 6]
        bg_rect = '<rect x="-16" y="-32" width="880" height="192" rx="10" fill="#161c28" stroke="#253245" stroke-width="1.2"/>'
        if bg_rect not in content:
            desc_end = content.find("</desc>")
            if desc_end != -1:
                content = content[:desc_end + 7] + bg_rect + content[desc_end + 7:]
            else:
                svg_start = content.find(">")
                if svg_start != -1:
                    content = content[:svg_start + 1] + bg_rect + content[svg_start + 1:]
        snake_file.write_text(content, encoding="utf-8")
        print("Injected soft dusk card container into github-contribution-grid-snake.svg")
    print("Calm contribution snake configured for workflow palette:")
    print("  color_snake=#ea937d")
    print("  color_dots=#161e2b,#253644,#3d5761,#6b8782,#7eb2a8")


if __name__ == "__main__":
    generate_hero_banner()
    generate_monthly_contribution_graph("Diyan4444")
    generate_github_summary("Diyan4444")
    restyle_pipeline_diagrams()
    generate_calm_contribution_snake("Diyan4444")
    print("\n>>> All Dusk Workspace assets generated successfully! <<<")
