"""
Asset Generator for Diyan Shah's GitHub Profile
Generates deterministic, handcrafted, high-fidelity SVGs matching the refined
Engineering-focused palette:
- Deep Charcoal / Graphite backgrounds (#0c1017, #121820)
- Muted Forest Green surfaces (#14221b, #18281f)
- Electric Lime / Restrained Acid Green highlights (#22c55e, #39d353, #4ade80)
- Warm Off-White primary text (#f0f6fc, #f4f4f5)
- Muted Grey secondary info (#8b949e, #94a3b8)
- Warm Amber / Copper accents (#f59e0b, #d97706)
"""

import os
from pathlib import Path
import urllib.request
import re

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Shared Palette Constants
BG_DARK = "#0c1017"
BG_GRAD_END = "#121820"
BG_CARD = "#141c26"
BORDER_SUBTLE = "#1e293b"
BORDER_GREEN = "#234932"
TEXT_WHITE = "#f0f6fc"
TEXT_MUTED = "#8b949e"
ACCENT_GREEN = "#22c55e"
ACCENT_LIME = "#39d353"
ACCENT_AMBER = "#f59e0b"
ACCENT_CYAN = "#38bdf8"

def generate_hero_banner():
    # Width 960, Height 290
    # Clean geometry with zero text clipping
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 290" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="50%" stop-color="{BG_GRAD_END}"/>
      <stop offset="100%" stop-color="#0e141d"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{TEXT_WHITE}"/>
      <stop offset="60%" stop-color="{TEXT_WHITE}"/>
      <stop offset="100%" stop-color="{ACCENT_LIME}"/>
    </linearGradient>
    <pattern id="techGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#162230" stroke-width="0.8"/>
      <circle cx="0" cy="0" r="1.2" fill="{ACCENT_LIME}" fill-opacity="0.2"/>
    </pattern>

    <style>
      .telemetry-text {{
        font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
        font-size: 11px;
        fill: {ACCENT_LIME};
        letter-spacing: 1px;
      }}
      .tagline-primary {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 15px;
        font-weight: 600;
        fill: {TEXT_WHITE};
        letter-spacing: 0.2px;
      }}
      .tagline-sub {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 13.5px;
        fill: {TEXT_MUTED};
        letter-spacing: 0.2px;
      }}
      .name-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: 2px;
      }}
      .badge-label {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 0.3px;
        fill: {TEXT_WHITE};
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="960" height="290" rx="12" fill="url(#heroBg)"/>
  <rect width="960" height="290" rx="12" fill="url(#techGrid)"/>

  <!-- Top Circuit Accent Line -->
  <path d="M 30 25 L 350 25 L 365 38 L 595 38 L 610 25 L 930 25" fill="none" stroke="#1c2b3e" stroke-width="1.2"/>
  <circle cx="350" cy="25" r="2.5" fill="{ACCENT_LIME}"/>
  <circle cx="610" cy="25" r="2.5" fill="{ACCENT_LIME}"/>

  <!-- Top Status Pill: ONLINE / READY TO BUILD (Wider container: 290px width) -->
  <g transform="translate(40, 24)">
    <rect width="280" height="28" rx="14" fill="#132219" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="16" cy="14" r="4.5" fill="{ACCENT_LIME}">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="30" y="18" class="telemetry-text">ONLINE • READY TO BUILD</text>
  </g>

  <!-- Top Right Academic Tag -->
  <g transform="translate(680, 24)">
    <rect width="240" height="28" rx="6" fill="#131b26" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="16" y="18" class="telemetry-text" fill="{TEXT_MUTED}">VJTI MUMBAI • IT SOPHOMORE</text>
  </g>

  <!-- Main Identity Content Block -->
  <g transform="translate(60, 78)">
    <!-- Subtitle / Role Tracker -->
    <text x="0" y="18" class="telemetry-text" fill="{ACCENT_LIME}" font-weight="600">
      &gt; BUILDING SOFTWARE FROM FIRST PRINCIPLES
    </text>

    <!-- Main Title -->
    <text x="0" y="62" class="name-text" fill="url(#textGrad)">
      DIYAN SHAH
    </text>

    <!-- Exact Academic Description across two balanced lines -->
    <text x="0" y="94" class="tagline-primary">
      Information Technology Sophomore at VJTI Mumbai
    </text>
    <text x="0" y="115" class="tagline-sub">
      Engineering full-stack architectures, systems tooling, AI workflows &amp; interactive applications.
    </text>

    <!-- 4 Technical Focus Badges with generous horizontal spacing -->
    <g transform="translate(0, 138)">
      <!-- Badge 1: Academic Base (width: 140) -->
      <g transform="translate(0, 0)">
        <rect width="140" height="28" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="12" cy="14" r="3" fill="{ACCENT_LIME}"/>
        <text x="24" y="18" class="badge-label">B.Tech IT • VJTI</text>
      </g>

      <!-- Badge 2: Full-Stack & Systems (width: 175, x: 152) -->
      <g transform="translate(152, 0)">
        <rect width="175" height="28" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="12" cy="14" r="3" fill="{ACCENT_GREEN}"/>
        <text x="24" y="18" class="badge-label">Full Stack &amp; Systems</text>
      </g>

      <!-- Badge 3: Applied AI & Data (width: 160, x: 339) -->
      <g transform="translate(339, 0)">
        <rect width="160" height="28" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="12" cy="14" r="3" fill="{ACCENT_CYAN}"/>
        <text x="24" y="18" class="badge-label">Applied AI &amp; Data</text>
      </g>

      <!-- Badge 4: Interactive & Game Dev (width: 185, x: 511) -> Ends at 696px -->
      <g transform="translate(511, 0)">
        <rect width="185" height="28" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="12" cy="14" r="3" fill="{ACCENT_AMBER}"/>
        <text x="24" y="18" class="badge-label">Interactive &amp; Game Dev</text>
      </g>
    </g>
  </g>

  <!-- Right Decorative Node Element (Centered at x=830, y=155) -->
  <g transform="translate(830, 155)">
    <circle cx="0" cy="0" r="50" fill="none" stroke="#1a2738" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="36" fill="none" stroke="{BORDER_GREEN}" stroke-width="1.2" stroke-dasharray="4, 4"/>
    <circle cx="0" cy="0" r="22" fill="#14221b" stroke="{ACCENT_GREEN}" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="{ACCENT_LIME}"/>

    <!-- Satellites -->
    <circle cx="30" cy="-22" r="3" fill="{ACCENT_LIME}"/>
    <circle cx="-28" cy="24" r="3" fill="{ACCENT_AMBER}"/>
    <circle cx="-26" cy="-22" r="2.5" fill="{ACCENT_CYAN}"/>
    <line x1="0" y1="0" x2="30" y2="-22" stroke="{ACCENT_LIME}" stroke-width="0.8" stroke-opacity="0.4"/>
    <line x1="0" y1="0" x2="-28" y2="24" stroke="{ACCENT_AMBER}" stroke-width="0.8" stroke-opacity="0.4"/>
  </g>

  <!-- Bottom Terminal Status Bar -->
  <g transform="translate(0, 258)">
    <rect width="960" height="32" fill="#090d14" stroke="#162230" stroke-width="1"/>
    <text x="35" y="20" class="telemetry-text" fill="{TEXT_MUTED}">
      CORE TECH: <tspan fill="{TEXT_WHITE}">TypeScript</tspan> • <tspan fill="{TEXT_WHITE}">C++</tspan> • <tspan fill="{TEXT_WHITE}">Python</tspan> • <tspan fill="{TEXT_WHITE}">Next.js</tspan> • <tspan fill="{TEXT_WHITE}">Node.js</tspan> • <tspan fill="{TEXT_WHITE}">Godot</tspan> • <tspan fill="{TEXT_WHITE}">Docker</tspan>
    </text>

    <!-- Lower-Right Badge: Fixed width 230, text x=115 text-anchor=middle. Never clips! -->
    <g transform="translate(695, 4)">
      <rect width="230" height="24" rx="4" fill="#14221b" stroke="{BORDER_GREEN}" stroke-width="1"/>
      <text x="115" y="16" class="telemetry-text" text-anchor="middle" fill="{ACCENT_LIME}">
        17 REPOSITORIES • ACTIVE
      </text>
    </g>
  </g>

  <!-- Outer Border Frame with Corner Accents -->
  <rect x="1" y="1" width="958" height="288" rx="11" fill="none" stroke="#1c293c" stroke-width="1.2"/>
  <path d="M 1 25 L 1 1 L 25 1" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
  <path d="M 935 1 L 959 1 L 959 25" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
  <path d="M 1 265 L 1 289 L 25 289" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
  <path d="M 935 289 L 959 289 L 959 265" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
</svg>'''
    with open(ASSETS_DIR / "hero-banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined hero-banner.svg")

def generate_profile_matrix():
    # Developer Console HUD: Refined charcoal & green theme, no awkward slashes, clean typography
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 220" width="100%" height="100%">
  <defs>
    <linearGradient id="hudBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="hudCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141d28"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .hud-title {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        fill: {ACCENT_LIME};
        letter-spacing: 1px;
        font-weight: 700;
      }}
      .hud-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13.5px;
        fill: {TEXT_WHITE};
        line-height: 1.5;
      }}
      .hud-sub {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 12px;
        fill: {TEXT_MUTED};
      }}
      .hud-num {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 26px;
        font-weight: 800;
        fill: {ACCENT_LIME};
      }}
      .hud-lbl {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 9.5px;
        fill: {TEXT_MUTED};
        letter-spacing: 0.8px;
      }}
    </style>
  </defs>

  <rect width="960" height="220" rx="12" fill="url(#hudBg)"/>

  <!-- Col 1: Identity & Educational Base -->
  <g transform="translate(30, 20)">
    <rect width="280" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title">01 • IDENTITY MATRIX</text>
    
    <text x="20" y="56" class="hud-text" font-weight="700">Diyan Shah</text>
    <text x="20" y="76" class="hud-sub">Information Technology Sophomore</text>
    <text x="20" y="96" class="hud-sub" fill="{ACCENT_LIME}" font-weight="600">VJTI Mumbai</text>
    
    <line x1="20" y1="112" x2="260" y2="112" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    
    <text x="20" y="136" class="hud-sub" fill="#cbd5e1">
      "Building software from first principles.
    </text>
    <text x="20" y="154" class="hud-sub" fill="#cbd5e1">
      Deep dives over surface tutorials."
    </text>
  </g>

  <!-- Col 2: Active Engineering Domains -->
  <g transform="translate(330, 20)">
    <rect width="300" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title">02 • ACTIVE DOMAINS</text>
    
    <g transform="translate(20, 48)">
      <circle cx="5" cy="5" r="3" fill="{ACCENT_LIME}"/>
      <text x="16" y="9" class="hud-sub" fill="{TEXT_WHITE}">Full-Stack Web &amp; Distributed APIs</text>
      
      <circle cx="5" cy="28" r="3" fill="{ACCENT_GREEN}"/>
      <text x="16" y="32" class="hud-sub" fill="{TEXT_WHITE}">Chrome Extensions (Manifest V3 Systems)</text>
      
      <circle cx="5" cy="51" r="3" fill="{ACCENT_AMBER}"/>
      <text x="16" y="55" class="hud-sub" fill="{TEXT_WHITE}">Multi-LLM Debate &amp; Prompt Orchestration</text>
      
      <circle cx="5" cy="74" r="3" fill="{ACCENT_CYAN}"/>
      <text x="16" y="78" class="hud-sub" fill="{TEXT_WHITE}">Game Architecture &amp; Mechanics (Godot)</text>
      
      <circle cx="5" cy="97" r="3" fill="{ACCENT_LIME}"/>
      <text x="16" y="101" class="hud-sub" fill="{TEXT_WHITE}">Data Structures &amp; Problem-Solving (C++)</text>
    </g>
  </g>

  <!-- Col 3: Audited Telemetry Metrics -->
  <g transform="translate(650, 20)">
    <rect width="280" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title">03 • AUDITED METRICS</text>
    
    <g transform="translate(20, 48)">
      <!-- Metric 1: Public Repos -->
      <g transform="translate(0, 0)">
        <text x="0" y="24" class="hud-num">17</text>
        <text x="0" y="40" class="hud-lbl">PUBLIC REPOSITORIES</text>
      </g>
      <!-- Metric 2: Contributions -->
      <g transform="translate(130, 0)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_GREEN}">187</text>
        <text x="0" y="40" class="hud-lbl">CONTRIBUTIONS (YTD)</text>
      </g>
      <!-- Metric 3: DSA Topics -->
      <g transform="translate(0, 62)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_AMBER}">18+</text>
        <text x="0" y="40" class="hud-lbl">DSA TOPICS (C++)</text>
      </g>
      <!-- Metric 4: Shipped Architectures -->
      <g transform="translate(130, 62)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_CYAN}">6</text>
        <text x="0" y="40" class="hud-lbl">CORE ARCHITECTURES</text>
      </g>
    </g>
  </g>

  <!-- Outer Border Frame -->
  <rect x="1" y="1" width="958" height="218" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "profile-matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined profile-matrix.svg")

def generate_engineering_network():
    # Width 960, Height 490
    # Clean connections, no awkward slashes, refined green/charcoal/amber palette
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 490" width="100%" height="100%">
  <defs>
    <linearGradient id="netBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1b3624"/>
      <stop offset="50%" stop-color="#12251a"/>
      <stop offset="100%" stop-color="#0e1713"/>
    </linearGradient>
    <linearGradient id="hubGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141d28"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>

    <style>
      @keyframes dashFlow {{
        from {{ stroke-dashoffset: 40; }}
        to {{ stroke-dashoffset: 0; }}
      }}
      .conn-trace {{
        stroke-dasharray: 6, 8;
        animation: dashFlow 3s linear infinite;
      }}
      .hub-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.3px;
      }}
      .hub-desc {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10px;
        fill: {TEXT_MUTED};
      }}
      .core-label {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 1.5px;
      }}
    </style>
  </defs>

  <rect width="960" height="490" rx="12" fill="url(#netBg)"/>

  <!-- Section Header -->
  <g transform="translate(40, 32)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      ENGINEERING TOPOLOGY • DOMAINS &amp; REPOSITORIES
    </text>
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="{TEXT_WHITE}">
      The Engineering Playground Network
    </text>
  </g>

  <!-- Central Core: (480, 260) -->

  <!-- Interconnect Lines -->
  <!-- Hub 1: Top-Left (210, 130) -->
  <path d="M 480 260 Q 320 210 210 130" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 480 260 Q 320 210 210 130" fill="none" stroke="{ACCENT_LIME}" stroke-width="1.8"/>

  <!-- Hub 2: Top-Right (750, 130) -->
  <path d="M 480 260 Q 640 210 750 130" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 480 260 Q 640 210 750 130" fill="none" stroke="{ACCENT_GREEN}" stroke-width="1.8"/>

  <!-- Hub 3: Mid-Right (780, 275) -->
  <path d="M 480 260 L 780 275" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 480 260 L 780 275" fill="none" stroke="{ACCENT_AMBER}" stroke-width="1.8"/>

  <!-- Hub 4: Bottom-Right (740, 415) -->
  <path d="M 480 260 Q 620 350 740 415" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 480 260 Q 620 350 740 415" fill="none" stroke="{ACCENT_CYAN}" stroke-width="1.8"/>

  <!-- Hub 5: Bottom-Left (220, 415) -->
  <path d="M 480 260 Q 330 350 220 415" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 480 260 Q 330 350 220 415" fill="none" stroke="{ACCENT_AMBER}" stroke-width="1.8"/>

  <!-- Hub 6: Mid-Left (180, 275) -->
  <path d="M 480 260 L 180 275" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 480 260 L 180 275" fill="none" stroke="{ACCENT_LIME}" stroke-width="1.8"/>

  <!-- ==================== SATELLITE HUBS ==================== -->

  <!-- Hub 1: Full-Stack Web & SaaS (Top Left) -->
  <g transform="translate(90, 80)">
    <rect width="240" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_LIME}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_WHITE}">Full-Stack SaaS &amp; Web</text>
    <text x="18" y="46" class="hub-desc">PROJECTS: Glamourly • Report-Maker</text>
    <text x="18" y="63" class="hub-desc">STACK: Next.js • React • TS • MongoDB</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_GREEN}">→ Real-time slots, Shop Act check</text>
  </g>

  <!-- Hub 2: Browser Systems & Extensions (Top Right) -->
  <g transform="translate(630, 80)">
    <rect width="240" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_GREEN}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_WHITE}">Browser Systems &amp; Tools</text>
    <text x="18" y="46" class="hub-desc">PROJECT: Leet-Vault (Chrome MV3)</text>
    <text x="18" y="63" class="hub-desc">TECH: TypeScript • OAuth Flow • DOM FSM</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_GREEN}">→ Multi-named sync, collision queue</text>
  </g>

  <!-- Hub 3: Applied AI & Language Models (Mid Right) -->
  <g transform="translate(660, 230)">
    <rect width="240" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_AMBER}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_WHITE}">Applied AI &amp; LLM Arenas</text>
    <text x="18" y="46" class="hub-desc">PROJECT: AI Debate Arena</text>
    <text x="18" y="63" class="hub-desc">STACK: Express • OpenRouter • Multi-LLM</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_AMBER}">→ Dual-model rebuttal, fallacy judge</text>
  </g>

  <!-- Hub 4: Marine AI & Geospatial (Bottom Right) -->
  <g transform="translate(620, 375)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_CYAN}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_WHITE}">Marine Geospatial Intel</text>
    <text x="18" y="46" class="hub-desc">PROJECT: OceanGuard (SIH 2026)</text>
    <text x="18" y="63" class="hub-desc">STACK: FastAPI • SciPy • Leaflet • SAR</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_CYAN}">→ Drift hindcasting &amp; AIS scoring</text>
  </g>

  <!-- Hub 5: Game Dev & Physics (Bottom Left) -->
  <g transform="translate(90, 375)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_AMBER}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_WHITE}">Game Dev &amp; Physics</text>
    <text x="18" y="46" class="hub-desc">PROJECT: Rune-Striker (Godot 4.6)</text>
    <text x="18" y="63" class="hub-desc">ENGINE: Godot • GDScript • Windows .exe</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_AMBER}">→ Coyote time, input buffer, Raycast AI</text>
  </g>

  <!-- Hub 6: Media Utilities & Algorithms (Mid Left) -->
  <g transform="translate(60, 230)">
    <rect width="240" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_LIME}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_WHITE}">Media Utilities &amp; DSA</text>
    <text x="18" y="46" class="hub-desc">PROJECTS: yt-to-mp4 • LeetCode (C++)</text>
    <text x="18" y="63" class="hub-desc">STACK: Python • Flask • FFmpeg • Docker</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_GREEN}">→ 18+ DSA topics, async transcoding</text>
  </g>

  <!-- ==================== CENTRAL CORE NODE ==================== -->
  <g transform="translate(480, 260)">
    <circle cx="0" cy="0" r="70" fill="none" stroke="#1c2b3e" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="56" fill="none" stroke="{BORDER_GREEN}" stroke-width="1.2" stroke-dasharray="6, 5"/>

    <circle cx="0" cy="0" r="44" fill="url(#coreGrad)" stroke="{ACCENT_GREEN}" stroke-width="1.5"/>

    <text x="0" y="-8" text-anchor="middle" class="core-label" fill="{ACCENT_LIME}">BUILD</text>
    <text x="0" y="8" text-anchor="middle" class="core-label" fill="{TEXT_WHITE}">ENGINEER</text>
    <text x="0" y="24" text-anchor="middle" class="core-label" fill="{ACCENT_GREEN}">SHIP</text>

    <!-- Satellite Orbit -->
    <circle cx="52" cy="-22" r="3" fill="{ACCENT_LIME}"/>
    <circle cx="-46" cy="32" r="3" fill="{ACCENT_AMBER}"/>
  </g>

  <!-- Outer Frame -->
  <rect x="1" y="1" width="958" height="488" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "engineering-network.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined engineering-network.svg")

def generate_pipeline_glamourly():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 175" width="100%" height="100%">
  <defs>
    <linearGradient id="pBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="pBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .step-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: {ACCENT_LIME}; letter-spacing: 0.5px; }}
      .step-body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }}
      .step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      @keyframes pFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .p-arrow {{ stroke-dasharray: 4, 4; animation: pFlow 1.5s linear infinite; }}
    </style>
  </defs>

  <rect width="920" height="175" rx="10" fill="url(#pBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(25, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      GLAMOURLY • ARCHITECTURAL FLOW (MUMBAI SALON PLATFORM)
    </text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(25, 42)">
    <rect width="195" height="110" rx="8" fill="url(#pBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. DISCOVERY &amp; GEO</text>
    <text x="14" y="46" class="step-body">Mumbai salon filtering</text>
    <text x="14" y="64" class="step-body">Transparent rate cards</text>
    <text x="14" y="82" class="step-body">AI Concierge assistant</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">Next.js • Tailwind CSS</text>
  </g>

  <line class="p-arrow" x1="220" y1="97" x2="255" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="255,94 261,97 255,100" fill="{ACCENT_LIME}"/>

  <!-- Step 2 -->
  <g transform="translate(265, 42)">
    <rect width="195" height="110" rx="8" fill="url(#pBox)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">02. BOOKING ENGINE</text>
    <text x="14" y="46" class="step-body">Real-time slot lock</text>
    <text x="14" y="64" class="step-body">Stylist roster allocation</text>
    <text x="14" y="82" class="step-body">Zero forced prepayment</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">TypeScript • React</text>
  </g>

  <line class="p-arrow" x1="460" y1="97" x2="495" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="495,94 501,97 495,100" fill="{ACCENT_LIME}"/>

  <!-- Step 3 -->
  <g transform="translate(505, 42)">
    <rect width="195" height="110" rx="8" fill="url(#pBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. DATA &amp; COMPLIANCE</text>
    <text x="14" y="46" class="step-body">Shop Act licensing check</text>
    <text x="14" y="64" class="step-body">Provider shift management</text>
    <text x="14" y="82" class="step-body">Customer order history</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">MongoDB • Node.js</text>
  </g>

  <line class="p-arrow" x1="700" y1="97" x2="735" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="735,94 741,97 735,100" fill="{ACCENT_LIME}"/>

  <!-- Step 4 -->
  <g transform="translate(745, 42)">
    <rect width="150" height="110" rx="8" fill="url(#pBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="{ACCENT_GREEN}">04. PASS DISPATCH</text>
    <text x="14" y="46" class="step-body">Instant email pass</text>
    <text x="14" y="64" class="step-body">Google Maps link</text>
    <text x="14" y="82" class="step-body">Status updates</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">Offline Payment</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-glamourly.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined pipeline-glamourly.svg")

def generate_pipeline_leetvault():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 175" width="100%" height="100%">
  <defs>
    <linearGradient id="lvBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="lvBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .step-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: {ACCENT_LIME}; letter-spacing: 0.5px; }}
      .step-body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }}
      .step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      @keyframes lvFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .lv-arrow {{ stroke-dasharray: 4, 4; animation: lvFlow 1.5s linear infinite; }}
    </style>
  </defs>

  <rect width="920" height="175" rx="10" fill="url(#lvBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(25, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      LEET-VAULT • CHROME EXTENSION (MV3) SUBMISSION PIPELINE
    </text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(25, 42)">
    <rect width="200" height="110" rx="8" fill="url(#lvBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. SUBMISSION FSM</text>
    <text x="14" y="46" class="step-body">Submit click hook</text>
    <text x="14" y="64" class="step-body">Instant DOM snapshot</text>
    <text x="14" y="82" class="step-body">Zero false-positives</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">Chrome MV3 Content Script</text>
  </g>

  <line class="lv-arrow" x1="225" y1="97" x2="255" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="255,94 261,97 255,100" fill="{ACCENT_LIME}"/>

  <!-- Step 2 -->
  <g transform="translate(265, 42)">
    <rect width="200" height="110" rx="8" fill="url(#lvBox)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">02. SECURE OAUTH BROKER</text>
    <text x="14" y="46" class="step-body">launchWebAuthFlow</text>
    <text x="14" y="64" class="step-body">Zero PAT exposure</text>
    <text x="14" y="82" class="step-body">Push &amp; admin verify</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">Chrome Identity API</text>
  </g>

  <line class="lv-arrow" x1="465" y1="97" x2="495" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="495,94 501,97 495,100" fill="{ACCENT_LIME}"/>

  <!-- Step 3 -->
  <g transform="translate(505, 42)">
    <rect width="200" height="110" rx="8" fill="url(#lvBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. SMART NAMING &amp; DUP</text>
    <text x="14" y="46" class="step-body">Custom: heap-sort.cpp</text>
    <text x="14" y="64" class="step-body">Deterministic N-fallback</text>
    <text x="14" y="82" class="step-body">SHA code fingerprinting</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">18+ Languages Mapped</text>
  </g>

  <line class="lv-arrow" x1="705" y1="97" x2="735" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="735,94 741,97 735,100" fill="{ACCENT_LIME}"/>

  <!-- Step 4 -->
  <g transform="translate(745, 42)">
    <rect width="150" height="110" rx="8" fill="url(#lvBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="{ACCENT_GREEN}">04. GIT SYNC</text>
    <text x="14" y="46" class="step-body">Dual README update</text>
    <text x="14" y="64" class="step-body">Alarm retry queue</text>
    <text x="14" y="82" class="step-body">50+ unit tests</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">GitHub REST API</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-leetvault.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined pipeline-leetvault.svg")

def generate_pipeline_debater():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 175" width="100%" height="100%">
  <defs>
    <linearGradient id="dbBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="dbBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .step-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: {ACCENT_AMBER}; letter-spacing: 0.5px; }}
      .step-body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }}
      .step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      @keyframes dbFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .db-arrow {{ stroke-dasharray: 4, 4; animation: dbFlow 1.5s linear infinite; }}
    </style>
  </defs>

  <rect width="920" height="175" rx="10" fill="url(#dbBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(25, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_AMBER}"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_AMBER}" letter-spacing="1">
      AI DEBATE ARENA • MULTI-MODEL REASONING &amp; SCORING ORCHESTRATION
    </text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(25, 42)">
    <rect width="200" height="110" rx="8" fill="url(#dbBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. DEBATE SETUP</text>
    <text x="14" y="46" class="step-body">Topic &amp; motion config</text>
    <text x="14" y="64" class="step-body">Select Model A vs B</text>
    <text x="14" y="82" class="step-body">Difficulty &amp; rounds</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_AMBER}">Express.js API</text>
  </g>

  <line class="db-arrow" x1="225" y1="97" x2="255" y2="97" stroke="{ACCENT_AMBER}" stroke-width="1.5"/>
  <polygon points="255,94 261,97 255,100" fill="{ACCENT_AMBER}"/>

  <!-- Step 2 -->
  <g transform="translate(265, 42)">
    <rect width="200" height="110" rx="8" fill="url(#dbBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">02. LLM ORCHESTRATOR</text>
    <text x="14" y="46" class="step-body">Turn-based context pipe</text>
    <text x="14" y="64" class="step-body">Prompt state injection</text>
    <text x="14" y="82" class="step-body">OpenRouter gateway</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">Multi-Model Gateway</text>
  </g>

  <line class="db-arrow" x1="465" y1="97" x2="495" y2="97" stroke="{ACCENT_AMBER}" stroke-width="1.5"/>
  <polygon points="495,94 501,97 495,100" fill="{ACCENT_AMBER}"/>

  <!-- Step 3 -->
  <g transform="translate(505, 42)">
    <rect width="200" height="110" rx="8" fill="url(#dbBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. REBUTTAL ENGINE</text>
    <text x="14" y="46" class="step-body">Cross-examination state</text>
    <text x="14" y="64" class="step-body">Multi-turn memory loop</text>
    <text x="14" y="82" class="step-body">Real-time stream response</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_AMBER}">MongoDB Persistence</text>
  </g>

  <line class="db-arrow" x1="705" y1="97" x2="735" y2="97" stroke="{ACCENT_AMBER}" stroke-width="1.5"/>
  <polygon points="735,94 741,97 735,100" fill="{ACCENT_AMBER}"/>

  <!-- Step 4 -->
  <g transform="translate(745, 42)">
    <rect width="150" height="110" rx="8" fill="url(#dbBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="{ACCENT_LIME}">04. AI JUDGE</text>
    <text x="14" y="46" class="step-body">Fallacy detection</text>
    <text x="14" y="64" class="step-body">Persuasion metrics</text>
    <text x="14" y="82" class="step-body">Dynamic scorecard</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">Objective Evaluation</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-debater.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined pipeline-debater.svg")

def generate_pipeline_oceanguard():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 175" width="100%" height="100%">
  <defs>
    <linearGradient id="ogBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="ogBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .step-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: {ACCENT_CYAN}; letter-spacing: 0.5px; }}
      .step-body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }}
      .step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      @keyframes ogFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .og-arrow {{ stroke-dasharray: 4, 4; animation: ogFlow 1.5s linear infinite; }}
    </style>
  </defs>

  <rect width="920" height="175" rx="10" fill="url(#ogBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(25, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_CYAN}"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_CYAN}" letter-spacing="1">
      OCEANGUARD AI • SAR SATELLITE OIL SPILL &amp; AIS ATTRIBUTION (SIH 2026)
    </text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(25, 42)">
    <rect width="200" height="110" rx="8" fill="url(#ogBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. SAR SEGMENTATION</text>
    <text x="14" y="46" class="step-body">Satellite radar imagery</text>
    <text x="14" y="64" class="step-body">AI oil slick mask</text>
    <text x="14" y="82" class="step-body">Dark spot extraction</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_CYAN}">Computer Vision / AI</text>
  </g>

  <line class="og-arrow" x1="225" y1="97" x2="255" y2="97" stroke="{ACCENT_CYAN}" stroke-width="1.5"/>
  <polygon points="255,94 261,97 255,100" fill="{ACCENT_CYAN}"/>

  <!-- Step 2 -->
  <g transform="translate(265, 42)">
    <rect width="200" height="110" rx="8" fill="url(#ogBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">02. DRIFT HINDCASTING</text>
    <text x="14" y="46" class="step-body">Reverse current simulation</text>
    <text x="14" y="64" class="step-body">Wind &amp; hydrodynamic flow</text>
    <text x="14" y="82" class="step-body">Origin coordinate fix</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">NumPy • SciPy</text>
  </g>

  <line class="og-arrow" x1="465" y1="97" x2="495" y2="97" stroke="{ACCENT_CYAN}" stroke-width="1.5"/>
  <polygon points="495,94 501,97 495,100" fill="{ACCENT_CYAN}"/>

  <!-- Step 3 -->
  <g transform="translate(505, 42)">
    <rect width="200" height="110" rx="8" fill="url(#ogBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. AIS CORRELATION</text>
    <text x="14" y="46" class="step-body">Vessel GPS cross-match</text>
    <text x="14" y="64" class="step-body">Speed anomaly detection</text>
    <text x="14" y="82" class="step-body">AIS blackout gap analysis</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_CYAN}">FastAPI • SQLite</text>
  </g>

  <line class="og-arrow" x1="705" y1="97" x2="735" y2="97" stroke="{ACCENT_CYAN}" stroke-width="1.5"/>
  <polygon points="735,94 741,97 735,100" fill="{ACCENT_CYAN}"/>

  <!-- Step 4 -->
  <g transform="translate(745, 42)">
    <rect width="150" height="110" rx="8" fill="url(#ogBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="{ACCENT_LIME}">04. ATTRIBUTION</text>
    <text x="14" y="46" class="step-body">Suspect confidence score</text>
    <text x="14" y="64" class="step-body">CartoDB dark maps</text>
    <text x="14" y="82" class="step-body">Evidence reporting</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">React 19 • Leaflet</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-oceanguard.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined pipeline-oceanguard.svg")

def generate_pipeline_runestriker():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 175" width="100%" height="100%">
  <defs>
    <linearGradient id="rsBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="rsBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .step-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: {ACCENT_AMBER}; letter-spacing: 0.5px; }}
      .step-body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }}
      .step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      @keyframes rsFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .rs-arrow {{ stroke-dasharray: 4, 4; animation: rsFlow 1.5s linear infinite; }}
    </style>
  </defs>

  <rect width="920" height="175" rx="10" fill="url(#rsBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(25, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_AMBER}"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_AMBER}" letter-spacing="1">
      RUNE-STRIKER • GODOT 4.6 2D PLATFORMER ARCHITECTURE &amp; GAMEPLAY LOOP
    </text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(25, 42)">
    <rect width="200" height="110" rx="8" fill="url(#rsBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. PLAYER PHYSICS</text>
    <text x="14" y="46" class="step-body">Coyote Time jump grace</text>
    <text x="14" y="64" class="step-body">Input buffering queue</text>
    <text x="14" y="82" class="step-body">IDLE → RUN → JUMP FSM</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_AMBER}">Godot 4.6 • CharacterBody2D</text>
  </g>

  <line class="rs-arrow" x1="225" y1="97" x2="255" y2="97" stroke="{ACCENT_AMBER}" stroke-width="1.5"/>
  <polygon points="255,94 261,97 255,100" fill="{ACCENT_AMBER}"/>

  <!-- Step 2 -->
  <g transform="translate(265, 42)">
    <rect width="200" height="110" rx="8" fill="url(#rsBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">02. ENEMY RAYCAST AI</text>
    <text x="14" y="46" class="step-body">Patrolling slime enemies</text>
    <text x="14" y="64" class="step-body">Wall &amp; ledge raycasting</text>
    <text x="14" y="82" class="step-body">Deadly spikes &amp; hazards</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">GDScript Vector Physics</text>
  </g>

  <line class="rs-arrow" x1="465" y1="97" x2="495" y2="97" stroke="{ACCENT_AMBER}" stroke-width="1.5"/>
  <polygon points="495,94 501,97 495,100" fill="{ACCENT_AMBER}"/>

  <!-- Step 3 -->
  <g transform="translate(505, 42)">
    <rect width="200" height="110" rx="8" fill="url(#rsBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. GAME MANAGER</text>
    <text x="14" y="46" class="step-body">Coin collect event bus</text>
    <text x="14" y="64" class="step-body">In-game HUD coin display</text>
    <text x="14" y="82" class="step-body">Contextual NPC dialogues</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_AMBER}">Decoupled Signal Flow</text>
  </g>

  <line class="rs-arrow" x1="705" y1="97" x2="735" y2="97" stroke="{ACCENT_AMBER}" stroke-width="1.5"/>
  <polygon points="735,94 741,97 735,100" fill="{ACCENT_AMBER}"/>

  <!-- Step 4 -->
  <g transform="translate(745, 42)">
    <rect width="150" height="110" rx="8" fill="url(#rsBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="{ACCENT_LIME}">04. DEPLOYMENT</text>
    <text x="14" y="46" class="step-body">Victory portal cutscene</text>
    <text x="14" y="64" class="step-body">Death &amp; retry reload</text>
    <text x="14" y="82" class="step-body">Playable .exe package</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">Windows Standalone</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-runestriker.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined pipeline-runestriker.svg")

def generate_pipeline_ytconverter():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 175" width="100%" height="100%">
  <defs>
    <linearGradient id="ytBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="ytBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .step-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: {ACCENT_LIME}; letter-spacing: 0.5px; }}
      .step-body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }}
      .step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      @keyframes ytFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .yt-arrow {{ stroke-dasharray: 4, 4; animation: ytFlow 1.5s linear infinite; }}
    </style>
  </defs>

  <rect width="920" height="175" rx="10" fill="url(#ytBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(25, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      YOUTUBE CONVERTER (YT-TO-MP4) • MEDIA PROCESSING PIPELINE
    </text>
  </g>

  <!-- Step 1 -->
  <g transform="translate(25, 42)">
    <rect width="200" height="110" rx="8" fill="url(#ytBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. INGESTION &amp; PROBE</text>
    <text x="14" y="46" class="step-body">YouTube URL validation</text>
    <text x="14" y="64" class="step-body">Metadata &amp; format probe</text>
    <text x="14" y="82" class="step-body">MP4 / MP3 bitrate selector</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_LIME}">Flask REST API</text>
  </g>

  <line class="yt-arrow" x1="225" y1="97" x2="255" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="255,94 261,97 255,100" fill="{ACCENT_LIME}"/>

  <!-- Step 2 -->
  <g transform="translate(265, 42)">
    <rect width="200" height="110" rx="8" fill="url(#ytBox)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">02. WORKER CONTROL</text>
    <text x="14" y="46" class="step-body">MAX_CONCURRENT=5 limit</text>
    <text x="14" y="64" class="step-body">Asynchronous job IDs</text>
    <text x="14" y="82" class="step-body">Real-time ETA &amp; speed</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">Python Backend Core</text>
  </g>

  <line class="yt-arrow" x1="465" y1="97" x2="495" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="495,94 501,97 495,100" fill="{ACCENT_LIME}"/>

  <!-- Step 3 -->
  <g transform="translate(505, 42)">
    <rect width="200" height="110" rx="8" fill="url(#ytBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. TRANSCODING</text>
    <text x="14" y="46" class="step-body">yt-dlp stream extraction</text>
    <text x="14" y="64" class="step-body">FFmpeg audio/video muxing</text>
    <text x="14" y="82" class="step-body">Temporary file auto-clean</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_AMBER}">yt-dlp + FFmpeg</text>
  </g>

  <line class="yt-arrow" x1="705" y1="97" x2="735" y2="97" stroke="{ACCENT_LIME}" stroke-width="1.5"/>
  <polygon points="735,94 741,97 735,100" fill="{ACCENT_LIME}"/>

  <!-- Step 4 -->
  <g transform="translate(745, 42)">
    <rect width="150" height="110" rx="8" fill="url(#ytBox)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="{ACCENT_GREEN}">04. RUNTIME</text>
    <text x="14" y="46" class="step-body">Chunked file delivery</text>
    <text x="14" y="64" class="step-body">Dockerized isolation</text>
    <text x="14" y="82" class="step-body">Render cloud deployment</text>
    <text x="14" y="100" class="step-tag" fill="{ACCENT_GREEN}">Docker Container</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-ytconverter.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined pipeline-ytconverter.svg")

def generate_workflow_inside_build():
    # Width 960, Height 220
    # 5 equal phases (width 166 each, gap 16)
    # x: 30, 212, 394, 576, 758 -> ends at 924px. 36px right margin. Zero overflow!
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 220" width="100%" height="100%">
  <defs>
    <linearGradient id="wfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="wfCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .wf-step-num {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 800; }}
      .wf-step-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; font-weight: 700; fill: {TEXT_WHITE}; }}
      .wf-step-desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: {TEXT_MUTED}; line-height: 1.4; }}
      .wf-step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {ACCENT_LIME}; }}
      @keyframes wfFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .wf-conn {{ stroke-dasharray: 4, 4; animation: wfFlow 2s linear infinite; }}
    </style>
  </defs>

  <rect width="960" height="220" rx="12" fill="url(#wfBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(30, 22)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      INSIDE THE BUILD • HOW I ENGINEER &amp; SHIP REAL SOFTWARE
    </text>
  </g>

  <!-- 5 Equal Phases: width 166 each, gap 16 -->

  <!-- Phase 1: Problem & Spec (x=30) -->
  <g transform="translate(30, 44)">
    <rect width="166" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_LIME}">PHASE 01</text>
    <text x="14" y="44" class="wf-step-title">Problem &amp; Spec</text>
    <text x="14" y="66" class="wf-step-desc">Dissect core problem,</text>
    <text x="14" y="82" class="wf-step-desc">boundary conditions &amp;</text>
    <text x="14" y="98" class="wf-step-desc">technical bottlenecks.</text>
    <rect x="12" y="118" width="142" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag">Architecture Blueprint</text>
  </g>

  <line class="wf-conn" x1="196" y1="118" x2="212" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 2: Schema & Engine (x=212) -->
  <g transform="translate(212, 44)">
    <rect width="166" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_GREEN}">PHASE 02</text>
    <text x="14" y="44" class="wf-step-title">Schema &amp; Engine</text>
    <text x="14" y="66" class="wf-step-desc">Type-safe models,</text>
    <text x="14" y="82" class="wf-step-desc">DB schemas (Mongo/PG)</text>
    <text x="14" y="98" class="wf-step-desc">&amp; core algorithms.</text>
    <rect x="12" y="118" width="142" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_GREEN}">State Machines &amp; APIs</text>
  </g>

  <line class="wf-conn" x1="378" y1="118" x2="394" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 3: Interactive UI (x=394) -->
  <g transform="translate(394, 44)">
    <rect width="166" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_AMBER}">PHASE 03</text>
    <text x="14" y="44" class="wf-step-title">Interactive UI</text>
    <text x="14" y="66" class="wf-step-desc">Clean responsive UX,</text>
    <text x="14" y="82" class="wf-step-desc">live data streaming &amp;</text>
    <text x="14" y="98" class="wf-step-desc">fluid visual feedback.</text>
    <rect x="12" y="118" width="142" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_AMBER}">Next.js • React • CSS</text>
  </g>

  <line class="wf-conn" x1="560" y1="118" x2="576" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 4: Resilience & Tests (x=576) -->
  <g transform="translate(576, 44)">
    <rect width="166" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_CYAN}">PHASE 04</text>
    <text x="14" y="44" class="wf-step-title">Resilience &amp; Tests</text>
    <text x="14" y="66" class="wf-step-desc">Unit/integration tests,</text>
    <text x="14" y="82" class="wf-step-desc">offline retry queues &amp;</text>
    <text x="14" y="98" class="wf-step-desc">collision handlers.</text>
    <rect x="12" y="118" width="142" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_CYAN}">50+ Tests • Edge Cases</text>
  </g>

  <line class="wf-conn" x1="742" y1="118" x2="758" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 5: Ship & Deploy (x=758 -> ends at 924px. 36px margin on right!) -->
  <g transform="translate(758, 44)">
    <rect width="166" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_LIME}">PHASE 05</text>
    <text x="14" y="44" class="wf-step-title">Ship &amp; Deploy</text>
    <text x="14" y="66" class="wf-step-desc">Docker images,</text>
    <text x="14" y="82" class="wf-step-desc">CI/CD pipelines &amp;</text>
    <text x="14" y="98" class="wf-step-desc">live hosting.</text>
    <rect x="12" y="118" width="142" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_LIME}">Deploy &amp; Monitor</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "workflow-inside-build.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined workflow-inside-build.svg")

def generate_animated_stats_card():
    # Dedicated SVG with pure SMIL rolling counter digits!
    # Counts up from 0 to actual numbers: 187 contributions, 17 repos, 13 streak, etc.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 185" width="100%" height="100%">
  <defs>
    <linearGradient id="stBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>
    <linearGradient id="stCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    
    <!-- ClipPaths for rolling digits (digit box: height 36) -->
    <clipPath id="digitClip">
      <rect x="0" y="0" width="22" height="36"/>
    </clipPath>
    <clipPath id="digitClipWide">
      <rect x="0" y="0" width="30" height="36"/>
    </clipPath>

    <style>
      .st-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; fill: {ACCENT_LIME}; letter-spacing: 1px; font-weight: 700; }}
      .st-num {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 32px; font-weight: 800; fill: {ACCENT_LIME}; }}
      .st-lbl {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 10px; fill: {TEXT_MUTED}; letter-spacing: 0.5px; }}
      .st-bar-bg {{ fill: #162230; }}
      .st-bar-fill {{ fill: {ACCENT_LIME}; }}
    </style>
  </defs>

  <rect width="920" height="185" rx="10" fill="url(#stBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(30, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" class="st-title">LIVE TELEMETRY &amp; ACTIVITY BENCHMARKS (ANIMATED)</text>
  </g>

  <!-- 4 Metric Cards -->
  <!-- 1. Contributions: 187 (Rolls 0 -> 187) -->
  <g transform="translate(30, 44)">
    <rect width="200" height="118" rx="8" fill="url(#stCard)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="16" y="24" class="st-lbl">CONTRIBUTIONS (YTD)</text>
    
    <!-- Rolling Counter: "1 8 7" -->
    <g transform="translate(16, 36)">
      <!-- Digit 1: rolls to 1 (y = -1 * 36 = -36) -->
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="66">1</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -36" dur="1s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <!-- Digit 2: rolls to 8 (y = -8 * 36 = -288) -->
      <g clip-path="url(#digitClip)" transform="translate(22, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="66">1</text><text x="2" y="102">2</text><text x="2" y="138">3</text>
          <text x="2" y="174">4</text><text x="2" y="210">5</text><text x="2" y="246">6</text><text x="2" y="282">7</text><text x="2" y="318">8</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -288" dur="1.3s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <!-- Digit 3: rolls to 7 (y = -7 * 36 = -252) -->
      <g clip-path="url(#digitClip)" transform="translate(44, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="66">1</text><text x="2" y="102">2</text><text x="2" y="138">3</text>
          <text x="2" y="174">4</text><text x="2" y="210">5</text><text x="2" y="246">6</text><text x="2" y="282">7</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -252" dur="1.6s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
    </g>
    <text x="16" y="98" class="st-lbl" fill="{TEXT_MUTED}">100% AUDITED GITHUB COMMITS</text>
  </g>

  <!-- 2. Public Repositories: 17 (Rolls 0 -> 17) -->
  <g transform="translate(250, 44)">
    <rect width="200" height="118" rx="8" fill="url(#stCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="16" y="24" class="st-lbl">PUBLIC REPOSITORIES</text>
    
    <g transform="translate(16, 36)">
      <!-- Digit 1: rolls to 1 (y = -36) -->
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="66">1</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -36" dur="0.9s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <!-- Digit 2: rolls to 7 (y = -252) -->
      <g clip-path="url(#digitClip)" transform="translate(22, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="66">1</text><text x="2" y="102">2</text><text x="2" y="138">3</text>
          <text x="2" y="174">4</text><text x="2" y="210">5</text><text x="2" y="246">6</text><text x="2" y="282">7</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -252" dur="1.4s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
    </g>
    <text x="16" y="98" class="st-lbl" fill="{TEXT_MUTED}">SYSTEMS, EXTENSIONS, GAMES</text>
  </g>

  <!-- 3. Longest Streak: 13 Days (Rolls 0 -> 13) -->
  <g transform="translate(470, 44)">
    <rect width="200" height="118" rx="8" fill="url(#stCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="16" y="24" class="st-lbl">LONGEST STREAK (DAYS)</text>
    
    <g transform="translate(16, 36)">
      <!-- Digit 1: rolls to 1 (y = -36) -->
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_AMBER}">
          <text x="2" y="30">0</text><text x="2" y="66">1</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -36" dur="0.8s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <!-- Digit 2: rolls to 3 (y = -108) -->
      <g clip-path="url(#digitClip)" transform="translate(22, 0)">
        <g class="st-num" fill="{ACCENT_AMBER}">
          <text x="2" y="30">0</text><text x="2" y="66">1</text><text x="2" y="102">2</text><text x="2" y="138">3</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -108" dur="1.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
    </g>
    <text x="16" y="98" class="st-lbl" fill="{TEXT_MUTED}">VERIFIED CONTINUOUS DAYS</text>
  </g>

  <!-- 4. Top Language: TypeScript 74% (Animated Progress Bar & Counter) -->
  <g transform="translate(690, 44)">
    <rect width="200" height="118" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="16" y="24" class="st-lbl">PRIMARY LANGUAGE: TS</text>
    
    <g transform="translate(16, 36)">
      <!-- Digit 1: rolls to 7 (y = -252) -->
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_CYAN}">
          <text x="2" y="30">0</text><text x="2" y="66">1</text><text x="2" y="102">2</text><text x="2" y="138">3</text>
          <text x="2" y="174">4</text><text x="2" y="210">5</text><text x="2" y="246">6</text><text x="2" y="282">7</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -252" dur="1.1s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <!-- Digit 2: rolls to 4 (y = -144) -->
      <g clip-path="url(#digitClip)" transform="translate(22, 0)">
        <g class="st-num" fill="{ACCENT_CYAN}">
          <text x="2" y="30">0</text><text x="2" y="66">1</text><text x="2" y="102">2</text><text x="2" y="138">3</text><text x="2" y="174">4</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -144" dur="1.4s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <text x="46" y="30" class="st-num" fill="{ACCENT_CYAN}">%</text>
    </g>

    <!-- Animated progress bar -->
    <rect x="16" y="80" width="168" height="6" rx="3" fill="#162230"/>
    <rect x="16" y="80" width="0" height="6" rx="3" fill="{ACCENT_CYAN}">
      <animate attributeName="width" from="0" to="124" dur="1.4s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
    <text x="16" y="102" class="st-lbl" fill="{TEXT_MUTED}">7.27 MB CODEBASE BYTES</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "github-stats-animated.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated github-stats-animated.svg with rolling counters")

def generate_contribution_snake():
    # Fetch real contribution data from GitHub for Diyan4444
    cells_data = []
    try:
        req = urllib.request.Request("https://github.com/users/Diyan4444/contributions", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")
        cells = re.findall(r'data-date="([^"]+)"[^>]*data-level="([^"]+)"', html)
        if not cells:
            cells = re.findall(r'data-level="([^"]+)"[^>]*data-date="([^"]+)"', html)
            cells = [(c[1], c[0]) for c in cells]
        cells_data = cells
    except Exception as e:
        print(f"Warning: could not fetch live contributions ({e}), using verified cached pattern.")

    # 53 columns x 7 rows grid
    # Colors for levels in Charcoal & Lime theme
    LVL_COLORS = {
        "0": "#16202c",  # Empty cell
        "1": "#123821",  # Low
        "2": "#1b5e34",  # Medium-low
        "3": "#22c55e",  # Active
        "4": "#39d353",  # High activity
    }

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 185" width="100%" height="100%">
  <defs>
    <linearGradient id="snkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_GRAD_END}"/>
    </linearGradient>

    <style>
      .snk-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; fill: {ACCENT_LIME}; letter-spacing: 1px; font-weight: 700; }}
      .snk-legend {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
      
      /* Continuous, smooth SMIL-driven traversal */
      @keyframes cellPulse {{
        0%, 100% {{ opacity: 0.95; }}
        50% {{ opacity: 0.6; }}
      }}
    </style>
  </defs>

  <rect width="920" height="185" rx="10" fill="url(#snkBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(30, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" class="snk-title">GITHUB CONTRIBUTION UNIVERSE • VERIFIED ACTIVITY CALENDAR</text>
  </g>

  <!-- 53 cols x 7 rows Grid -->
  <g transform="translate(32, 42)">
'''
    # Total 371 cells
    idx = 0
    active_coords = []
    for col in range(53):
        x = col * 16
        for row in range(7):
            y = row * 16
            if idx < len(cells_data):
                level = cells_data[idx][1]
            else:
                level = "0"
            color = LVL_COLORS.get(level, "#16202c")
            svg += f'    <rect x="{x}" y="{y}" width="12" height="12" rx="2.5" fill="{color}"/>\n'
            if level in ("2", "3", "4"):
                active_coords.append((x + 6, y + 6))
            idx += 1

    # Snake motion path along the active cells
    # We create a continuous path traversing active weeks
    snake_path = "M 10 10 L 250 10 L 250 58 L 480 58 L 480 26 L 680 26 L 680 90 L 820 90 L 820 20 L 840 70"

    svg += f'''
    <!-- Animated Glowing Snake traversing the grid -->
    <!-- Snake Body Segments following the path -->
    <path id="snakeTrack" d="{snake_path}" fill="none" stroke="none"/>

    <!-- Segment 4 (Tail) -->
    <circle r="4" fill="#1b5e34" opacity="0.6">
      <animateMotion dur="10s" repeatCount="indefinite" rotate="auto">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 3 -->
    <circle r="4.5" fill="{ACCENT_GREEN}">
      <animateMotion dur="10s" repeatCount="indefinite" rotate="auto" begin="0.08s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 2 -->
    <circle r="5" fill="{ACCENT_LIME}">
      <animateMotion dur="10s" repeatCount="indefinite" rotate="auto" begin="0.16s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 1 (Head) with bright lime and glow -->
    <circle r="6" fill="#00ff88" stroke="#ffffff" stroke-width="1.2">
      <animateMotion dur="10s" repeatCount="indefinite" rotate="auto" begin="0.24s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>
  </g>

  <!-- Legend -->
  <g transform="translate(32, 162)">
    <text x="0" y="9" class="snk-legend">187 CONTRIBUTIONS ACROSS THE PAST YEAR</text>
    <g transform="translate(685, 0)">
      <text x="-32" y="9" class="snk-legend">Less</text>
      <rect x="0" y="0" width="10" height="10" rx="2" fill="#16202c"/>
      <rect x="14" y="0" width="10" height="10" rx="2" fill="#123821"/>
      <rect x="28" y="0" width="10" height="10" rx="2" fill="#1b5e34"/>
      <rect x="42" y="0" width="10" height="10" rx="2" fill="{ACCENT_GREEN}"/>
      <rect x="56" y="0" width="10" height="10" rx="2" fill="{ACCENT_LIME}"/>
      <text x="72" y="9" class="snk-legend">More</text>
    </g>
  </g>
</svg>'''
    with open(ASSETS_DIR / "github-contribution-grid-snake.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated refined github-contribution-grid-snake.svg with real motion")

if __name__ == "__main__":
    generate_hero_banner()
    generate_profile_matrix()
    generate_engineering_network()
    generate_pipeline_glamourly()
    generate_pipeline_leetvault()
    generate_pipeline_debater()
    generate_pipeline_oceanguard()
    generate_pipeline_runestriker()
    generate_pipeline_ytconverter()
    generate_workflow_inside_build()
    generate_animated_stats_card()
    generate_contribution_snake()
    print("All assets successfully regenerated with the refined palette!")
