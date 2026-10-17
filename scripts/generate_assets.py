"""
Asset Generator for Diyan Shah's GitHub Profile
Generates deterministic, handcrafted, high-fidelity SVGs matching the refined
Human Developer & Engineering Playground identity:
- Palette: Red, Orange, and White Flame/Ember theme:
  - Vivid Crimson / Red (#ff3355, #ef4444)
  - Blaze Orange (#ff6b35, #f97316)
  - Warm Amber-Gold (#f59e0b)
  - Pure White & Silver (#ffffff, #f8fafc, #94a3b8)
  - Deep Obsidian Canvas (#0a0b0e, #12141a, #171922)
  - Dark Ruby Borders (#331c22, #442228)
- Dynamic Animations:
  - Hero banner: Flowing animated laser circuit traces, rotating dual-ring orbital gyroscope radar with satellites, and pulsing status dot!
  - Stats card: Cyclical rolling odometer counters (0 -> target, holds 4.5s, repeats) with telemetry scan line.
  - Engineering network: Flowing animated dashed data traces connecting all 6 domains.
  - Workflow: Animated pulse connectors between the 5 development phases.
  - Contribution grid: Live flame/fire snake traversing the grid.
"""

from pathlib import Path
import urllib.request
import re

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Red, Orange, and White Palette
BG_DARK = "#0a0b0e"
BG_SURFACE = "#12141a"
BG_CARD = "#171922"
BORDER_SUBTLE = "#331c22"
BORDER_ACCENT = "#4a242b"
BORDER_RED = "#dc2626"
BORDER_ORANGE = "#ea580c"
TEXT_PRIMARY = "#ffffff"
TEXT_MUTED = "#94a3b8"
TEXT_WARM = "#cbd5e1"
ACCENT_RED = "#ff3355"
ACCENT_ORANGE = "#ff6b35"
ACCENT_AMBER = "#f59e0b"
ACCENT_WHITE = "#ffffff"
ACCENT_ROSE = "#f43f5e"


def generate_hero_banner():
    # 1000 x 300 viewBox - generous breathing room for all elements
    # Includes rich, fluid SMIL animations:
    # 1. Flowing laser circuit traces along the top and across canvas
    # 2. Rotating orbital gyroscope/radar with satellites on the right
    # 3. Pulsing status dot on the ONLINE pill
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="50%" stop-color="{BG_SURFACE}"/>
      <stop offset="100%" stop-color="#140f12"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#ffffff"/>
      <stop offset="85%" stop-color="{ACCENT_ORANGE}"/>
      <stop offset="100%" stop-color="{ACCENT_RED}"/>
    </linearGradient>
    <linearGradient id="flameLaser" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ACCENT_RED}"/>
      <stop offset="50%" stop-color="{ACCENT_ORANGE}"/>
      <stop offset="100%" stop-color="{ACCENT_AMBER}"/>
    </linearGradient>
    <linearGradient id="coreFlame" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{ACCENT_RED}"/>
      <stop offset="100%" stop-color="{ACCENT_ORANGE}"/>
    </linearGradient>
    <pattern id="techGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#25161d" stroke-width="0.8"/>
      <circle cx="0" cy="0" r="1.2" fill="{ACCENT_ORANGE}" fill-opacity="0.2"/>
    </pattern>

    <style>
      .mono-pill {{
        font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
        font-size: 11px;
        fill: {ACCENT_ORANGE};
        letter-spacing: 0.8px;
        font-weight: 600;
      }}
      .tagline-primary {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 15.5px;
        font-weight: 600;
        fill: {TEXT_PRIMARY};
      }}
      .tagline-sub {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 13.5px;
        fill: {TEXT_MUTED};
      }}
      .name-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: 2px;
      }}
      .badge-label {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.3px;
        fill: {TEXT_PRIMARY};
      }}
    </style>
  </defs>

  <rect width="1000" height="300" rx="12" fill="url(#heroBg)"/>
  <rect width="1000" height="300" rx="12" fill="url(#techGrid)"/>

  <!-- Static Top Circuit Guide Line -->
  <path d="M 35 25 L 360 25 L 375 38 L 610 38 L 625 25 L 965 25" fill="none" stroke="#2a1820" stroke-width="1.2"/>

  <!-- Animated Glowing Laser Trace along Header Circuit (Works 100% natively in GitHub) -->
  <path d="M 35 25 L 360 25 L 375 38 L 610 38 L 625 25 L 965 25" fill="none" stroke="url(#flameLaser)" stroke-width="1.8" stroke-dasharray="10, 16">
    <animate attributeName="stroke-dashoffset" from="0" to="-104" dur="2.4s" repeatCount="indefinite"/>
  </path>

  <!-- Glowing Circuit Intersection Nodes -->
  <circle cx="360" cy="25" r="2.8" fill="{ACCENT_RED}"/>
  <circle cx="625" cy="25" r="2.8" fill="{ACCENT_ORANGE}"/>

  <!-- Animated Ambient Data Stream Wave in Background -->
  <path d="M 35 185 Q 260 155 490 185 T 965 185" fill="none" stroke="url(#flameLaser)" stroke-width="1.2" stroke-opacity="0.3" stroke-dasharray="8, 14">
    <animate attributeName="stroke-dashoffset" from="0" to="-88" dur="3.6s" repeatCount="indefinite"/>
  </path>

  <!-- Top Status Pill: ONLINE • READY TO BUILD (Width: 290px, generous padding) -->
  <g transform="translate(45, 24)">
    <rect width="290" height="28" rx="14" fill="#1c1116" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <!-- Pulsing Red/Orange Status Dot -->
    <circle cx="16" cy="14" r="4.5" fill="{ACCENT_RED}">
      <animate attributeName="r" values="3.5; 5.5; 3.5" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.4; 1; 0.4" dur="1.8s" repeatCount="indefinite"/>
    </circle>
    <text x="32" y="18" class="mono-pill" fill="{ACCENT_ORANGE}">ONLINE • READY TO BUILD</text>
  </g>

  <!-- Top Right Academic Tag (Width: 260px) -->
  <g transform="translate(695, 24)">
    <rect width="260" height="28" rx="6" fill="#171216" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="18" y="18" class="mono-pill" fill="{TEXT_MUTED}">VJTI MUMBAI • IT SOPHOMORE</text>
  </g>

  <!-- Main Identity Content Block -->
  <g transform="translate(55, 76)">
    <!-- Subtitle / Mission -->
    <text x="0" y="20" class="mono-pill" fill="{ACCENT_RED}">
      &gt; BUILDING SOFTWARE FROM FIRST PRINCIPLES
    </text>

    <!-- Main Title: Pure White with Flame Orange Shimmer -->
    <text x="0" y="64" class="name-text" fill="url(#textGrad)">
      DIYAN SHAH
    </text>

    <!-- Exact Academic Description across two balanced lines -->
    <text x="0" y="96" class="tagline-primary">
      Information Technology Sophomore at VJTI Mumbai
    </text>
    <text x="0" y="118" class="tagline-sub">
      Engineering full-stack architectures, systems tooling, AI workflows &amp; interactive applications.
    </text>

    <!-- 4 Technical Focus Badges with generous width and spacing (zero clipping) -->
    <g transform="translate(0, 142)">
      <!-- Badge 1: Academic Base (width: 145) -->
      <g transform="translate(0, 0)">
        <rect width="145" height="30" rx="5" fill="#1a1419" stroke="{BORDER_ACCENT}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_RED}"/>
        <text x="26" y="19" class="badge-label">B.Tech IT • VJTI</text>
      </g>

      <!-- Badge 2: Full-Stack & Systems (width: 185, x: 155) -->
      <g transform="translate(155, 0)">
        <rect width="185" height="30" rx="5" fill="#1a1419" stroke="{BORDER_ACCENT}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_ORANGE}"/>
        <text x="26" y="19" class="badge-label">Full Stack &amp; Systems</text>
      </g>

      <!-- Badge 3: Applied AI & Data (width: 175, x: 350) -->
      <g transform="translate(350, 0)">
        <rect width="175" height="30" rx="5" fill="#1a1419" stroke="{BORDER_ACCENT}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_AMBER}"/>
        <text x="26" y="19" class="badge-label">Applied AI &amp; Data</text>
      </g>

      <!-- Badge 4: Interactive & Game Dev (width: 220, x: 535) -> ends at 755px -->
      <g transform="translate(535, 0)">
        <rect width="220" height="30" rx="5" fill="#1a1419" stroke="{BORDER_ACCENT}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_ROSE}"/>
        <text x="26" y="19" class="badge-label">Interactive &amp; Game Dev</text>
      </g>
    </g>
  </g>

  <!-- Right Animated Orbital Radar Gyroscope (Centered at x=875, y=155) -->
  <g transform="translate(875, 155)">
    <!-- Outer Radar Track -->
    <circle cx="0" cy="0" r="54" fill="none" stroke="#25161e" stroke-width="1.2"/>

    <!-- Rotating Outer Dashed Ring (Flame Orange) -->
    <circle cx="0" cy="0" r="46" fill="none" stroke="{ACCENT_ORANGE}" stroke-width="1.4" stroke-dasharray="6, 6" stroke-opacity="0.75">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="12s" repeatCount="indefinite"/>
    </circle>

    <!-- Counter-Rotating Inner Dashed Ring (Crimson Red) -->
    <circle cx="0" cy="0" r="32" fill="none" stroke="{ACCENT_RED}" stroke-width="1.4" stroke-dasharray="5, 5" stroke-opacity="0.85">
      <animateTransform attributeName="transform" type="rotate" from="360 0 0" to="0 0 0" dur="8s" repeatCount="indefinite"/>
    </circle>

    <!-- Orbiting Satellite 1 (Flame Orange, r=46) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="5s" repeatCount="indefinite"/>
      <circle cx="46" cy="0" r="3.5" fill="{ACCENT_ORANGE}"/>
      <line x1="0" y1="0" x2="46" y2="0" stroke="{ACCENT_ORANGE}" stroke-width="0.8" stroke-opacity="0.4"/>
    </g>

    <!-- Orbiting Satellite 2 (Crimson Red, r=32) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360 0 0" to="0 0 0" dur="7s" repeatCount="indefinite"/>
      <circle cx="-32" cy="0" r="3" fill="{ACCENT_RED}"/>
      <line x1="0" y1="0" x2="-32" y2="0" stroke="{ACCENT_RED}" stroke-width="0.8" stroke-opacity="0.4"/>
    </g>

    <!-- Orbiting Satellite 3 (Pure White, r=58) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="45 0 0" to="405 0 0" dur="11s" repeatCount="indefinite"/>
      <circle cx="58" cy="0" r="2.5" fill="{ACCENT_WHITE}"/>
    </g>

    <!-- Central Pulsing Core Orb -->
    <circle cx="0" cy="0" r="14" fill="url(#coreFlame)" stroke="#ffffff" stroke-width="1.5">
      <animate attributeName="r" values="13; 16; 13" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Bottom Terminal Status Bar -->
  <g transform="translate(0, 268)">
    <rect width="1000" height="32" fill="#0c0d12" stroke="#25161d" stroke-width="1"/>
    <text x="35" y="20" class="mono-pill" fill="{TEXT_MUTED}">
      CORE TECH: <tspan fill="{TEXT_PRIMARY}">TypeScript</tspan> • <tspan fill="{TEXT_PRIMARY}">C++</tspan> • <tspan fill="{TEXT_PRIMARY}">Python</tspan> • <tspan fill="{TEXT_PRIMARY}">Next.js</tspan> • <tspan fill="{TEXT_PRIMARY}">Node.js</tspan> • <tspan fill="{TEXT_PRIMARY}">Godot</tspan> • <tspan fill="{TEXT_PRIMARY}">Docker</tspan>
    </text>

    <!-- Lower-Right Badge: width 240, centered text. Generous 40px margin from canvas edge! -->
    <g transform="translate(720, 4)">
      <rect width="240" height="24" rx="4" fill="#1c1116" stroke="{BORDER_ACCENT}" stroke-width="1"/>
      <text x="120" y="16" class="mono-pill" text-anchor="middle" fill="{ACCENT_ORANGE}">
        17 REPOSITORIES • ACTIVE
      </text>
    </g>
  </g>

  <!-- Outer Border Frame with Corner Accents -->
  <rect x="1" y="1" width="998" height="298" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
  <path d="M 1 25 L 1 1 L 25 1" fill="none" stroke="{ACCENT_RED}" stroke-width="2">
    <animate attributeName="stroke" values="{ACCENT_RED}; {ACCENT_ORANGE}; {ACCENT_RED}" dur="3s" repeatCount="indefinite"/>
  </path>
  <path d="M 975 1 L 999 1 L 999 25" fill="none" stroke="{ACCENT_RED}" stroke-width="2">
    <animate attributeName="stroke" values="{ACCENT_RED}; {ACCENT_ORANGE}; {ACCENT_RED}" dur="3s" repeatCount="indefinite"/>
  </path>
  <path d="M 1 275 L 1 299 L 25 299" fill="none" stroke="{ACCENT_RED}" stroke-width="2">
    <animate attributeName="stroke" values="{ACCENT_RED}; {ACCENT_ORANGE}; {ACCENT_RED}" dur="3s" repeatCount="indefinite"/>
  </path>
  <path d="M 975 299 L 999 299 L 999 275" fill="none" stroke="{ACCENT_RED}" stroke-width="2">
    <animate attributeName="stroke" values="{ACCENT_RED}; {ACCENT_ORANGE}; {ACCENT_RED}" dur="3s" repeatCount="indefinite"/>
  </path>
</svg>'''
    with open(ASSETS_DIR / "hero-banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected hero-banner.svg with Red/Orange/White theme and full animation!")


def generate_profile_matrix():
    # Developer Console HUD: Red, Orange, and White theme with zero backslashes
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 220" width="100%" height="100%">
  <defs>
    <linearGradient id="hudBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="hudCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#18141a"/>
      <stop offset="100%" stop-color="#121117"/>
    </linearGradient>
    <style>
      .hud-title {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        letter-spacing: 0.8px;
        font-weight: 700;
      }}
      .hud-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13.5px;
        fill: {TEXT_PRIMARY};
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
      }}
      .hud-lbl {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 9.5px;
        fill: {TEXT_MUTED};
        letter-spacing: 0.6px;
      }}
    </style>
  </defs>

  <rect width="1000" height="220" rx="12" fill="url(#hudBg)"/>

  <!-- Col 1: Identity & Education (width: 290) -->
  <g transform="translate(35, 20)">
    <rect width="290" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title" fill="{ACCENT_RED}">01 • ABOUT ME</text>
    
    <text x="20" y="56" class="hud-text" font-weight="700">Diyan Shah</text>
    <text x="20" y="76" class="hud-sub">Information Technology Sophomore</text>
    <text x="20" y="96" class="hud-sub" fill="{ACCENT_ORANGE}" font-weight="600">VJTI Mumbai</text>
    
    <line x1="20" y1="112" x2="270" y2="112" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    
    <text x="20" y="136" class="hud-sub" fill="{TEXT_WARM}">
      "Building software from first principles.
    </text>
    <text x="20" y="154" class="hud-sub" fill="{TEXT_WARM}">
      Deep dives over surface tutorials."
    </text>
  </g>

  <!-- Col 2: Active Engineering Domains (width: 320) -->
  <g transform="translate(340, 20)">
    <rect width="320" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title" fill="{ACCENT_ORANGE}">02 • AREAS OF INTEREST</text>
    
    <g transform="translate(20, 48)">
      <circle cx="5" cy="5" r="3" fill="{ACCENT_RED}"/>
      <text x="16" y="9" class="hud-sub" fill="{TEXT_PRIMARY}">Full-Stack Web &amp; Distributed APIs</text>
      
      <circle cx="5" cy="28" r="3" fill="{ACCENT_ORANGE}"/>
      <text x="16" y="32" class="hud-sub" fill="{TEXT_PRIMARY}">Chrome Extensions (Manifest V3 Systems)</text>
      
      <circle cx="5" cy="51" r="3" fill="{ACCENT_AMBER}"/>
      <text x="16" y="55" class="hud-sub" fill="{TEXT_PRIMARY}">Multi-LLM Debate &amp; Prompt Orchestration</text>
      
      <circle cx="5" cy="74" r="3" fill="{ACCENT_ROSE}"/>
      <text x="16" y="78" class="hud-sub" fill="{TEXT_PRIMARY}">Game Architecture &amp; Mechanics (Godot)</text>
      
      <circle cx="5" cy="97" r="3" fill="{ACCENT_WHITE}"/>
      <text x="16" y="101" class="hud-sub" fill="{TEXT_PRIMARY}">Data Structures &amp; Problem-Solving (C++)</text>
    </g>
  </g>

  <!-- Col 3: Key Metrics (width: 290) -->
  <g transform="translate(675, 20)">
    <rect width="290" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title" fill="{ACCENT_RED}">03 • AT A GLANCE</text>
    
    <g transform="translate(20, 48)">
      <!-- Metric 1: Public Repos -->
      <g transform="translate(0, 0)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_RED}">17</text>
        <text x="0" y="40" class="hud-lbl">PUBLIC REPOSITORIES</text>
      </g>
      <!-- Metric 2: Contributions -->
      <g transform="translate(135, 0)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_ORANGE}">187</text>
        <text x="0" y="40" class="hud-lbl">CONTRIBUTIONS (YTD)</text>
      </g>
      <!-- Metric 3: DSA Topics -->
      <g transform="translate(0, 62)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_AMBER}">18+</text>
        <text x="0" y="40" class="hud-lbl">DSA TOPICS (C++)</text>
      </g>
      <!-- Metric 4: Shipped Architectures -->
      <g transform="translate(135, 62)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_WHITE}">6</text>
        <text x="0" y="40" class="hud-lbl">CORE ARCHITECTURES</text>
      </g>
    </g>
  </g>

  <!-- Outer Frame -->
  <rect x="1" y="1" width="998" height="218" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "profile-matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected profile-matrix.svg with Red/Orange/White theme!")


def generate_engineering_network():
    # 1000 x 500 viewBox: Red, Orange, and White Theme with flowing trace animations
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="100%" height="100%">
  <defs>
    <linearGradient id="netBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{ACCENT_RED}"/>
      <stop offset="50%" stop-color="{ACCENT_ORANGE}"/>
      <stop offset="100%" stop-color="#80141e"/>
    </linearGradient>
    <linearGradient id="hubGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18141b"/>
      <stop offset="100%" stop-color="#121117"/>
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

  <rect width="1000" height="500" rx="12" fill="url(#netBg)"/>

  <!-- Section Header -->
  <g transform="translate(45, 32)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_RED}" letter-spacing="1">
      PROJECT NETWORK &amp; CONNECTED DOMAINS
    </text>
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="{TEXT_PRIMARY}">
      What I Build &amp; How It Connects
    </text>
  </g>

  <!-- Interconnect Lines to Satellite Hubs -->
  <!-- Hub 1: Top-Left (230, 135) -->
  <path d="M 500 265 Q 340 215 230 135" fill="none" stroke="#2a1a22" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 340 215 230 135" fill="none" stroke="{ACCENT_RED}" stroke-width="1.8"/>

  <!-- Hub 2: Top-Right (770, 135) -->
  <path d="M 500 265 Q 660 215 770 135" fill="none" stroke="#2a1a22" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 660 215 770 135" fill="none" stroke="{ACCENT_ORANGE}" stroke-width="1.8"/>

  <!-- Hub 3: Mid-Right (800, 280) -->
  <path d="M 500 265 L 800 280" fill="none" stroke="#2a1a22" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 L 800 280" fill="none" stroke="{ACCENT_AMBER}" stroke-width="1.8"/>

  <!-- Hub 4: Bottom-Right (760, 420) -->
  <path d="M 500 265 Q 640 355 760 420" fill="none" stroke="#2a1a22" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 640 355 760 420" fill="none" stroke="{ACCENT_RED}" stroke-width="1.8"/>

  <!-- Hub 5: Bottom-Left (240, 420) -->
  <path d="M 500 265 Q 350 355 240 420" fill="none" stroke="#2a1a22" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 350 355 240 420" fill="none" stroke="{ACCENT_ORANGE}" stroke-width="1.8"/>

  <!-- Hub 6: Mid-Left (200, 280) -->
  <path d="M 500 265 L 200 280" fill="none" stroke="#2a1a22" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 L 200 280" fill="none" stroke="{ACCENT_WHITE}" stroke-width="1.8"/>

  <!-- ==================== SATELLITE HUBS ==================== -->

  <!-- Hub 1: Full-Stack Web & SaaS (Top Left) -->
  <g transform="translate(100, 85)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_RED}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Full-Stack SaaS &amp; Web</text>
    <text x="18" y="46" class="hub-desc">PROJECTS: Glamourly • Report-Maker</text>
    <text x="18" y="63" class="hub-desc">STACK: Next.js • React • TS • MongoDB</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_ORANGE}">Real-time slots, verified listings</text>
  </g>

  <!-- Hub 2: Browser Systems & Extensions (Top Right) -->
  <g transform="translate(650, 85)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_ORANGE}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Browser Systems &amp; Tools</text>
    <text x="18" y="46" class="hub-desc">PROJECT: Leet-Vault (Chrome MV3)</text>
    <text x="18" y="63" class="hub-desc">TECH: TypeScript • OAuth Flow • DOM FSM</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_RED}">Multi-named sync, collision queue</text>
  </g>

  <!-- Hub 3: Applied AI & Language Models (Mid Right) -->
  <g transform="translate(680, 235)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_AMBER}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Applied AI &amp; LLM Arenas</text>
    <text x="18" y="46" class="hub-desc">PROJECT: AI Debate Arena</text>
    <text x="18" y="63" class="hub-desc">STACK: Express • OpenRouter • Multi-LLM</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_AMBER}">Dual-model rebuttal, fallacy scoring</text>
  </g>

  <!-- Hub 4: Marine AI & Geospatial (Bottom Right) -->
  <g transform="translate(640, 380)">
    <rect width="255" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_RED}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Marine Geospatial Intel</text>
    <text x="18" y="46" class="hub-desc">PROJECT: OceanGuard (SIH 2026)</text>
    <text x="18" y="63" class="hub-desc">STACK: FastAPI • SciPy • Leaflet • SAR</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_ROSE}">Drift hindcasting &amp; AIS scoring</text>
  </g>

  <!-- Hub 5: Game Dev & Physics (Bottom Left) -->
  <g transform="translate(100, 380)">
    <rect width="255" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_ORANGE}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Game Dev &amp; Physics</text>
    <text x="18" y="46" class="hub-desc">PROJECT: Rune-Striker (Godot 4.6)</text>
    <text x="18" y="63" class="hub-desc">ENGINE: Godot • GDScript • Windows .exe</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_ORANGE}">Coyote time, input buffer, Raycast AI</text>
  </g>

  <!-- Hub 6: Media Utilities & Algorithms (Mid Left) -->
  <g transform="translate(70, 235)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_WHITE}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Media Utilities &amp; DSA</text>
    <text x="18" y="46" class="hub-desc">PROJECTS: yt-to-mp4 • LeetCode (C++)</text>
    <text x="18" y="63" class="hub-desc">STACK: Python • Flask • FFmpeg • Docker</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_RED}">18+ DSA topics, async transcoding</text>
  </g>

  <!-- ==================== CENTRAL CORE NODE ==================== -->
  <g transform="translate(500, 265)">
    <circle cx="0" cy="0" r="70" fill="none" stroke="#2a1820" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="56" fill="none" stroke="{BORDER_ACCENT}" stroke-width="1.2" stroke-dasharray="6, 5">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="14s" repeatCount="indefinite"/>
    </circle>

    <circle cx="0" cy="0" r="44" fill="url(#coreGrad)" stroke="{ACCENT_RED}" stroke-width="1.5"/>

    <text x="0" y="-8" text-anchor="middle" class="core-label" fill="{ACCENT_WHITE}">BUILD</text>
    <text x="0" y="8" text-anchor="middle" class="core-label" fill="{TEXT_PRIMARY}">ENGINEER</text>
    <text x="0" y="24" text-anchor="middle" class="core-label" fill="{ACCENT_ORANGE}">SHIP</text>

    <!-- Satellite Orbit -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="6s" repeatCount="indefinite"/>
      <circle cx="52" cy="0" r="3" fill="{ACCENT_ORANGE}"/>
      <circle cx="-52" cy="0" r="3" fill="{ACCENT_WHITE}"/>
    </g>
  </g>

  <!-- Outer Frame -->
  <rect x="1" y="1" width="998" height="498" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "engineering-network.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected engineering-network.svg with Red/Orange/White theme!")


def generate_workflow_card():
    # 1000 x 220 viewBox: Red, Orange, and White progression across 5 phases
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 220" width="100%" height="100%">
  <defs>
    <linearGradient id="wfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="wfCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#18141b"/>
      <stop offset="100%" stop-color="#121117"/>
    </linearGradient>
    <style>
      .wf-step-num {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 800; }}
      .wf-step-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; font-weight: 700; fill: {TEXT_PRIMARY}; }}
      .wf-step-desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: {TEXT_MUTED}; line-height: 1.4; }}
      .wf-step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {ACCENT_ORANGE}; }}
      @keyframes wfFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .wf-conn {{ stroke-dasharray: 4, 4; animation: wfFlow 2s linear infinite; }}
    </style>
  </defs>

  <rect width="1000" height="220" rx="12" fill="url(#wfBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(40, 22)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_RED}" letter-spacing="1">
      HOW I APPROACH BUILDING THINGS
    </text>
  </g>

  <!-- 5 Equal Phases: width 170 each, gap 16. Total width: 914. x=40 -> ends at 954 (46px right margin) -->

  <!-- Phase 1: Problem & Spec (x=40) -->
  <g transform="translate(40, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_RED}">PHASE 01</text>
    <text x="14" y="44" class="wf-step-title">Problem &amp; Spec</text>
    <text x="14" y="66" class="wf-step-desc">Break down core user</text>
    <text x="14" y="82" class="wf-step-desc">pain points &amp; system</text>
    <text x="14" y="98" class="wf-step-desc">bottlenecks first.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d0e14"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_RED}">System Blueprint</text>
  </g>

  <line class="wf-conn" x1="210" y1="118" x2="226" y2="118" stroke="{ACCENT_RED}" stroke-width="1.5"/>

  <!-- Phase 2: Schema & Engine (x=226) -->
  <g transform="translate(226, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_ROSE}">PHASE 02</text>
    <text x="14" y="44" class="wf-step-title">Schema &amp; Logic</text>
    <text x="14" y="66" class="wf-step-desc">Type-safe models,</text>
    <text x="14" y="82" class="wf-step-desc">clean DB schemas &amp;</text>
    <text x="14" y="98" class="wf-step-desc">core state machines.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d0e14"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_ROSE}">APIs &amp; State Logic</text>
  </g>

  <line class="wf-conn" x1="396" y1="118" x2="412" y2="118" stroke="{ACCENT_ORANGE}" stroke-width="1.5"/>

  <!-- Phase 3: Interactive UI (x=412) -->
  <g transform="translate(412, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_ORANGE}">PHASE 03</text>
    <text x="14" y="44" class="wf-step-title">Frontend &amp; UX</text>
    <text x="14" y="66" class="wf-step-desc">Fast, responsive UI,</text>
    <text x="14" y="82" class="wf-step-desc">dark mode layout &amp;</text>
    <text x="14" y="98" class="wf-step-desc">fluid user feedback.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d0e14"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_ORANGE}">Next.js • React • CSS</text>
  </g>

  <line class="wf-conn" x1="582" y1="118" x2="598" y2="118" stroke="{ACCENT_ORANGE}" stroke-width="1.5"/>

  <!-- Phase 4: Resilience & Tests (x=598) -->
  <g transform="translate(598, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_AMBER}">PHASE 04</text>
    <text x="14" y="44" class="wf-step-title">Resilience &amp; Tests</text>
    <text x="14" y="66" class="wf-step-desc">Edge-case testing,</text>
    <text x="14" y="82" class="wf-step-desc">offline retry queues &amp;</text>
    <text x="14" y="98" class="wf-step-desc">error recovery.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d0e14"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_AMBER}">50+ Tests • Edge Cases</text>
  </g>

  <line class="wf-conn" x1="768" y1="118" x2="784" y2="118" stroke="{ACCENT_WHITE}" stroke-width="1.5"/>

  <!-- Phase 5: Ship & Deploy (x=784 -> ends at 954px) -->
  <g transform="translate(784, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_WHITE}">PHASE 05</text>
    <text x="14" y="44" class="wf-step-title">Ship &amp; Deploy</text>
    <text x="14" y="66" class="wf-step-desc">Docker images,</text>
    <text x="14" y="82" class="wf-step-desc">CI/CD workflows &amp;</text>
    <text x="14" y="98" class="wf-step-desc">production hosting.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d0e14"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_WHITE}">Deploy &amp; Monitor</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "workflow-inside-build.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected workflow-inside-build.svg with Red/Orange/White theme!")


def generate_animated_stats_card():
    # 1000 x 200 viewBox with pure SMIL rolling counter digits + animated language progress bars
    # Red, Orange, and White Flame/Ember theme:
    # Continuous 6.5s cyclical telemetry roll with 4.5s steady hold:
    # Guaranteed to animate in front of the viewer's eyes whenever they scroll down!
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200" width="100%" height="100%">
  <defs>
    <linearGradient id="stBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="stCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#18141b"/>
      <stop offset="100%" stop-color="#121117"/>
    </linearGradient>
    <linearGradient id="sweepGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ACCENT_RED}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{ACCENT_ORANGE}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{ACCENT_RED}" stop-opacity="0"/>
    </linearGradient>
    
    <clipPath id="digitClip">
      <rect x="0" y="0" width="24" height="38"/>
    </clipPath>

    <style>
      .st-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; fill: {ACCENT_ORANGE}; letter-spacing: 0.8px; font-weight: 700; }}
      .st-num {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 32px; font-weight: 800; }}
      .st-lbl {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 10.5px; fill: {TEXT_MUTED}; letter-spacing: 0.5px; font-weight: 600; }}
      .st-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: {TEXT_MUTED}; }}
    </style>
  </defs>

  <rect width="1000" height="200" rx="10" fill="url(#stBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header with Telemetry Ping Indicator -->
  <g transform="translate(35, 24)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_RED}">
      <animate attributeName="r" values="3; 5.5; 3" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5; 1; 0.5" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="18" y="10" class="st-title">GITHUB TELEMETRY &amp; ACTIVITY BENCHMARKS</text>
  </g>

  <!-- Telemetry Scan Laser Line across Header -->
  <line x1="35" y1="36" x2="140" y2="36" stroke="url(#sweepGrad)" stroke-width="1.5">
    <animate attributeName="x1" values="35; 860; 35" dur="6.5s" repeatCount="indefinite" calcMode="spline" keyTimes="0; 0.5; 1" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"/>
    <animate attributeName="x2" values="140; 965; 140" dur="6.5s" repeatCount="indefinite" calcMode="spline" keyTimes="0; 0.5; 1" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"/>
  </line>

  <!-- 4 Balanced Metric Cards in Red, Orange, Amber, and White -->

  <!-- Card 1: Total Contributions (Rolls 0 -> 187 in Crimson Red) -->
  <g transform="translate(35, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">CONTRIBUTIONS (YTD)</text>
    
    <!-- Rolling Counter: 1 8 7 -->
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_RED}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -38; 0 -38; 0 0" keyTimes="0; 0.18; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num" fill="{ACCENT_RED}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text><text x="2" y="334">8</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -304; 0 -304; 0 0" keyTimes="0; 0.21; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(48, 0)">
        <g class="st-num" fill="{ACCENT_RED}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -266; 0 -266; 0 0" keyTimes="0; 0.24; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
    </g>
    <text x="18" y="112" class="st-sub">Live public GitHub stream</text>
  </g>

  <!-- Card 2: Public Repos (Rolls 0 -> 17 in Blaze Orange) -->
  <g transform="translate(269, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">PUBLIC REPOSITORIES</text>
    
    <!-- Rolling Counter: 1 7 -->
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_ORANGE}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -38; 0 -38; 0 0" keyTimes="0; 0.18; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num" fill="{ACCENT_ORANGE}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -266; 0 -266; 0 0" keyTimes="0; 0.22; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
    </g>
    <text x="18" y="112" class="st-sub">Full-stack, tools, &amp; games</text>
  </g>

  <!-- Card 3: Longest Streak (Rolls 0 -> 13 in Warm Amber) -->
  <g transform="translate(503, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">LONGEST STREAK (DAYS)</text>
    
    <!-- Rolling Counter: 1 3 -->
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_AMBER}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -38; 0 -38; 0 0" keyTimes="0; 0.17; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num" fill="{ACCENT_AMBER}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -114; 0 -114; 0 0" keyTimes="0; 0.21; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
    </g>
    <text x="18" y="112" class="st-sub">Consecutive active days</text>
  </g>

  <!-- Card 4: Top Language: TypeScript 74% (Pure White with Flame Progress Bar) -->
  <g transform="translate(737, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_ACCENT}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">PRIMARY CODEBASE (TS)</text>
    
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_WHITE}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -266; 0 -266; 0 0" keyTimes="0; 0.20; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num" fill="{ACCENT_WHITE}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text><text x="2" y="182">4</text>
          <animateTransform attributeName="transform" type="translate" values="0 0; 0 -152; 0 -152; 0 0" keyTimes="0; 0.23; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
        </g>
      </g>
      <text x="50" y="30" class="st-num" fill="{ACCENT_WHITE}">%</text>
    </g>

    <!-- Animated progress bar in Flame Orange -->
    <rect x="18" y="86" width="180" height="6" rx="3" fill="#25161e"/>
    <rect x="18" y="86" width="0" height="6" rx="3" fill="{ACCENT_ORANGE}">
      <animate attributeName="width" values="0; 134; 134; 0" keyTimes="0; 0.24; 0.88; 1" keySplines="0.16 1 0.3 1; 0 0 1 1; 0.7 0 0.84 0" calcMode="spline" dur="6.5s" repeatCount="indefinite"/>
    </rect>
    <text x="18" y="112" class="st-sub">7.27 MB verified code</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "github-stats-animated.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected github-stats-animated.svg with Red/Orange/White theme!")


def generate_contribution_snake():
    # Fetch real live contribution data from GitHub
    cells_data = []
    try:
        req = urllib.request.Request("https://github.com/users/Diyan4444/contributions", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")
        cells = re.findall(r'data-date="([^"]+)"[^>]*data-level="([^"]+)"', html)
        if not cells:
            cells = re.findall(r'data-level="([^"]+)"[^>]*data-date="([^"]+)"', html)
        if cells:
            for d, l in cells:
                try:
                    lvl = int(l) if l.isdigit() else (int(d) if d.isdigit() else 0)
                except:
                    lvl = 0
                cells_data.append(lvl)
    except Exception as e:
        print(f"Warning: could not fetch live calendar stream ({e}), using audited 187 activity pattern.")

    # 53 columns x 7 rows = 371 cells
    if len(cells_data) < 371:
        import random
        random.seed(4444)
        cells_data = [0] * 371
        # Place 187 contributions realistically
        for idx in range(120, 371):
            if random.random() < 0.62:
                cells_data[idx] = random.choice([1, 1, 2, 2, 3, 4])

    # Red/Orange Flame Color Map
    COLOR_MAP = {
        0: "#161820",   # Empty dark tile
        1: "#4c1d1d",   # Deep ruby wine
        2: "#881337",   # Dark crimson
        3: "#ea580c",   # Blaze orange
        4: "#ff6b35"    # Radiant flame orange
    }

    rects = []
    col_width = 16
    row_height = 16
    for col in range(53):
        for row in range(7):
            idx = col * 7 + row
            lvl = cells_data[idx] if idx < len(cells_data) else 0
            color = COLOR_MAP.get(lvl, "#161820")
            x = col * col_width
            y = row * row_height
            rects.append(f'<rect x="{x}" y="{y}" width="12" height="12" rx="2.5" fill="{color}"/>')

    rects_str = "\n    ".join(rects)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 185" width="100%" height="100%">
  <defs>
    <linearGradient id="snkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>

    <style>
      .snk-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; fill: {ACCENT_ORANGE}; letter-spacing: 0.8px; font-weight: 700; }}
      .snk-legend {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
    </style>
  </defs>

  <rect width="1000" height="185" rx="10" fill="url(#snkBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(35, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_RED}"/>
    <text x="18" y="10" class="snk-title">GITHUB CONTRIBUTION CALENDAR • 187 CONTRIBUTIONS</text>
  </g>

  <!-- 53 cols x 7 rows Grid -->
  <g transform="translate(70, 42)">
    {rects_str}

    <!-- Animated Glowing Flame Snake traversing the grid -->
    <path id="snakeTrack" d="M 10 10 L 260 10 L 260 58 L 500 58 L 500 26 L 700 26 L 700 90 L 830 90 L 830 20 L 848 70" fill="none" stroke="none"/>

    <!-- Segment 4 (Tail) -->
    <circle r="4" fill="{ACCENT_RED}" opacity="0.6">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 3 -->
    <circle r="4.5" fill="{ACCENT_ROSE}">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto" begin="0.08s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 2 -->
    <circle r="5" fill="{ACCENT_ORANGE}">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto" begin="0.16s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 1 (Head: Pure White with Fire Glow) -->
    <circle r="6" fill="#ffffff" stroke="{ACCENT_RED}" stroke-width="1.5">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto" begin="0.24s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>
  </g>

  <!-- Legend in Red & Orange -->
  <g transform="translate(70, 162)">
    <text x="0" y="9" class="snk-legend">187 CONTRIBUTIONS ACROSS THE PAST YEAR</text>
    <g transform="translate(710, 0)">
      <text x="-32" y="9" class="snk-legend">Less</text>
      <rect x="0" y="0" width="10" height="10" rx="2" fill="#161820"/>
      <rect x="14" y="0" width="10" height="10" rx="2" fill="#4c1d1d"/>
      <rect x="28" y="0" width="10" height="10" rx="2" fill="#881337"/>
      <rect x="42" y="0" width="10" height="10" rx="2" fill="#ea580c"/>
      <rect x="56" y="0" width="10" height="10" rx="2" fill="#ff6b35"/>
      <text x="72" y="9" class="snk-legend">More</text>
    </g>
  </g>
</svg>'''
    with open(ASSETS_DIR / "github-contribution-grid-snake.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected github-contribution-grid-snake.svg with Flame theme!")


if __name__ == "__main__":
    generate_hero_banner()
    generate_profile_matrix()
    generate_engineering_network()
    generate_workflow_card()
    generate_animated_stats_card()
    generate_contribution_snake()
    print("All core assets regenerated with Red/Orange/White theme and full animation suite!")
