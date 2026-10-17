"""
Asset Generator for Diyan Shah's GitHub Profile
Generates deterministic, handcrafted, high-fidelity SVGs matching the refined
Human Developer & Engineering Playground identity:
- Palette: Deep Charcoal (#0d1117), Forest Green (#12241a), Vibrant Lime (#39d353), Warm Amber (#f59e0b), Off-White (#f0f6fc), Muted Grey (#8b949e). Zero purple.
- Spacing: 1000px wide viewBoxes with generous margins, zero text clipping across any system font.
- Language: Natural developer tone. No robotic AI jargon or backslashes.
"""

from pathlib import Path
import urllib.request
import re

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# Shared Palette
BG_DARK = "#0d1117"
BG_SURFACE = "#121820"
BG_CARD = "#16202c"
BORDER_SUBTLE = "#212e3e"
BORDER_GREEN = "#234e32"
TEXT_PRIMARY = "#f0f6fc"
TEXT_MUTED = "#8b949e"
ACCENT_LIME = "#39d353"
ACCENT_GREEN = "#22c55e"
ACCENT_AMBER = "#f59e0b"
ACCENT_BLUE = "#38bdf8"

def generate_hero_banner():
    # 1000 x 300 viewBox - generous breathing room for all elements
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="50%" stop-color="{BG_SURFACE}"/>
      <stop offset="100%" stop-color="#0a0e14"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{TEXT_PRIMARY}"/>
      <stop offset="70%" stop-color="{TEXT_PRIMARY}"/>
      <stop offset="100%" stop-color="{ACCENT_LIME}"/>
    </linearGradient>
    <pattern id="techGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#162230" stroke-width="0.8"/>
      <circle cx="0" cy="0" r="1.2" fill="{ACCENT_LIME}" fill-opacity="0.15"/>
    </pattern>

    <style>
      .mono-pill {{
        font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
        font-size: 11px;
        fill: {ACCENT_LIME};
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

  <!-- Top Circuit Accent Line -->
  <path d="M 35 25 L 360 25 L 375 38 L 610 38 L 625 25 L 965 25" fill="none" stroke="#1c2b3e" stroke-width="1.2"/>
  <circle cx="360" cy="25" r="2.5" fill="{ACCENT_LIME}"/>
  <circle cx="625" cy="25" r="2.5" fill="{ACCENT_LIME}"/>

  <!-- Top Status Pill: ONLINE • READY TO BUILD (Width: 290px, generous padding) -->
  <g transform="translate(45, 24)">
    <rect width="290" height="28" rx="14" fill="#13241b" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <!-- Subtle contained pulsing dot, never flickers outside -->
    <circle cx="16" cy="14" r="4.5" fill="{ACCENT_LIME}">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <text x="32" y="18" class="mono-pill">ONLINE • READY TO BUILD</text>
  </g>

  <!-- Top Right Academic Tag (Width: 260px) -->
  <g transform="translate(695, 24)">
    <rect width="260" height="28" rx="6" fill="#141d28" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="18" y="18" class="mono-pill" fill="{TEXT_MUTED}">VJTI MUMBAI • IT SOPHOMORE</text>
  </g>

  <!-- Main Identity Content Block -->
  <g transform="translate(55, 76)">
    <!-- Subtitle / Mission -->
    <text x="0" y="20" class="mono-pill" fill="{ACCENT_LIME}">
      &gt; BUILDING SOFTWARE FROM FIRST PRINCIPLES
    </text>

    <!-- Main Title -->
    <text x="0" y="64" class="name-text" fill="url(#textGrad)">
      DIYAN SHAH
    </text>

    <!-- Exact Academic Description across two balanced lines with 400px+ room to spare -->
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
        <rect width="145" height="30" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_LIME}"/>
        <text x="26" y="19" class="badge-label">B.Tech IT • VJTI</text>
      </g>

      <!-- Badge 2: Full-Stack & Systems (width: 185, x: 155) -->
      <g transform="translate(155, 0)">
        <rect width="185" height="30" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_GREEN}"/>
        <text x="26" y="19" class="badge-label">Full Stack &amp; Systems</text>
      </g>

      <!-- Badge 3: Applied AI & Data (width: 175, x: 350) -->
      <g transform="translate(350, 0)">
        <rect width="175" height="30" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_BLUE}"/>
        <text x="26" y="19" class="badge-label">Applied AI &amp; Data</text>
      </g>

      <!-- Badge 4: Interactive & Game Dev (width: 220, x: 535) -> ends at 755px -->
      <g transform="translate(535, 0)">
        <rect width="220" height="30" rx="5" fill="#141f2c" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
        <circle cx="14" cy="15" r="3" fill="{ACCENT_AMBER}"/>
        <text x="26" y="19" class="badge-label">Interactive &amp; Game Dev</text>
      </g>
    </g>
  </g>

  <!-- Right Decorative Node Element (Centered at x=875, y=160) -->
  <g transform="translate(875, 160)">
    <circle cx="0" cy="0" r="50" fill="none" stroke="#1a2738" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="36" fill="none" stroke="{BORDER_GREEN}" stroke-width="1.2" stroke-dasharray="4, 4"/>
    <circle cx="0" cy="0" r="22" fill="#13241b" stroke="{ACCENT_GREEN}" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="6" fill="{ACCENT_LIME}"/>

    <!-- Satellites -->
    <circle cx="30" cy="-22" r="3" fill="{ACCENT_LIME}"/>
    <circle cx="-28" cy="24" r="3" fill="{ACCENT_AMBER}"/>
    <circle cx="-26" cy="-22" r="2.5" fill="{ACCENT_BLUE}"/>
    <line x1="0" y1="0" x2="30" y2="-22" stroke="{ACCENT_LIME}" stroke-width="0.8" stroke-opacity="0.4"/>
    <line x1="0" y1="0" x2="-28" y2="24" stroke="{ACCENT_AMBER}" stroke-width="0.8" stroke-opacity="0.4"/>
  </g>

  <!-- Bottom Terminal Status Bar -->
  <g transform="translate(0, 268)">
    <rect width="1000" height="32" fill="#0a0e14" stroke="#162230" stroke-width="1"/>
    <text x="35" y="20" class="mono-pill" fill="{TEXT_MUTED}">
      CORE TECH: <tspan fill="{TEXT_PRIMARY}">TypeScript</tspan> • <tspan fill="{TEXT_PRIMARY}">C++</tspan> • <tspan fill="{TEXT_PRIMARY}">Python</tspan> • <tspan fill="{TEXT_PRIMARY}">Next.js</tspan> • <tspan fill="{TEXT_PRIMARY}">Node.js</tspan> • <tspan fill="{TEXT_PRIMARY}">Godot</tspan> • <tspan fill="{TEXT_PRIMARY}">Docker</tspan>
    </text>

    <!-- Lower-Right Badge: width 240, centered text. Generous 40px margin from canvas edge! -->
    <g transform="translate(720, 4)">
      <rect width="240" height="24" rx="4" fill="#13241b" stroke="{BORDER_GREEN}" stroke-width="1"/>
      <text x="120" y="16" class="mono-pill" text-anchor="middle" fill="{ACCENT_LIME}">
        17 REPOSITORIES • ACTIVE
      </text>
    </g>
  </g>

  <!-- Outer Border Frame with Corner Accents -->
  <rect x="1" y="1" width="998" height="298" rx="11" fill="none" stroke="#1c293c" stroke-width="1.2"/>
  <path d="M 1 25 L 1 1 L 25 1" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
  <path d="M 975 1 L 999 1 L 999 25" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
  <path d="M 1 275 L 1 299 L 25 299" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
  <path d="M 975 299 L 999 299 L 999 275" fill="none" stroke="{ACCENT_LIME}" stroke-width="2"/>
</svg>'''
    with open(ASSETS_DIR / "hero-banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected hero-banner.svg")

def generate_profile_matrix():
    # Developer Console HUD: Natural developer wording, zero backslashes, green/amber theme
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 220" width="100%" height="100%">
  <defs>
    <linearGradient id="hudBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="hudCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141e2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .hud-title {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        fill: {ACCENT_LIME};
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
        fill: {ACCENT_LIME};
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
    <rect width="290" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title">01 • ABOUT ME</text>
    
    <text x="20" y="56" class="hud-text" font-weight="700">Diyan Shah</text>
    <text x="20" y="76" class="hud-sub">Information Technology Sophomore</text>
    <text x="20" y="96" class="hud-sub" fill="{ACCENT_LIME}" font-weight="600">VJTI Mumbai</text>
    
    <line x1="20" y1="112" x2="270" y2="112" stroke="{BORDER_SUBTLE}" stroke-width="1"/>
    
    <text x="20" y="136" class="hud-sub" fill="#cbd5e1">
      "Building software from first principles.
    </text>
    <text x="20" y="154" class="hud-sub" fill="#cbd5e1">
      Deep dives over surface tutorials."
    </text>
  </g>

  <!-- Col 2: Active Engineering Domains (width: 320) -->
  <g transform="translate(340, 20)">
    <rect width="320" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title">02 • AREAS OF INTEREST</text>
    
    <g transform="translate(20, 48)">
      <circle cx="5" cy="5" r="3" fill="{ACCENT_LIME}"/>
      <text x="16" y="9" class="hud-sub" fill="{TEXT_PRIMARY}">Full-Stack Web &amp; Distributed APIs</text>
      
      <circle cx="5" cy="28" r="3" fill="{ACCENT_GREEN}"/>
      <text x="16" y="32" class="hud-sub" fill="{TEXT_PRIMARY}">Chrome Extensions (Manifest V3 Systems)</text>
      
      <circle cx="5" cy="51" r="3" fill="{ACCENT_AMBER}"/>
      <text x="16" y="55" class="hud-sub" fill="{TEXT_PRIMARY}">Multi-LLM Debate &amp; Prompt Orchestration</text>
      
      <circle cx="5" cy="74" r="3" fill="{ACCENT_BLUE}"/>
      <text x="16" y="78" class="hud-sub" fill="{TEXT_PRIMARY}">Game Architecture &amp; Mechanics (Godot)</text>
      
      <circle cx="5" cy="97" r="3" fill="{ACCENT_LIME}"/>
      <text x="16" y="101" class="hud-sub" fill="{TEXT_PRIMARY}">Data Structures &amp; Problem-Solving (C++)</text>
    </g>
  </g>

  <!-- Col 3: Key Metrics (width: 290) -->
  <g transform="translate(675, 20)">
    <rect width="290" height="180" rx="8" fill="url(#hudCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="20" y="28" class="hud-title">03 • AT A GLANCE</text>
    
    <g transform="translate(20, 48)">
      <!-- Metric 1: Public Repos -->
      <g transform="translate(0, 0)">
        <text x="0" y="24" class="hud-num">17</text>
        <text x="0" y="40" class="hud-lbl">PUBLIC REPOSITORIES</text>
      </g>
      <!-- Metric 2: Contributions -->
      <g transform="translate(135, 0)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_GREEN}">187</text>
        <text x="0" y="40" class="hud-lbl">CONTRIBUTIONS (YTD)</text>
      </g>
      <!-- Metric 3: DSA Topics -->
      <g transform="translate(0, 62)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_AMBER}">18+</text>
        <text x="0" y="40" class="hud-lbl">DSA TOPICS (C++)</text>
      </g>
      <!-- Metric 4: Shipped Architectures -->
      <g transform="translate(135, 62)">
        <text x="0" y="24" class="hud-num" fill="{ACCENT_BLUE}">6</text>
        <text x="0" y="40" class="hud-lbl">CORE ARCHITECTURES</text>
      </g>
    </g>
  </g>

  <!-- Outer Frame -->
  <rect x="1" y="1" width="998" height="218" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "profile-matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected profile-matrix.svg")

def generate_engineering_network():
    # 1000 x 500 viewBox
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 500" width="100%" height="100%">
  <defs>
    <linearGradient id="netBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1b3624"/>
      <stop offset="50%" stop-color="#12251a"/>
      <stop offset="100%" stop-color="#0e1713"/>
    </linearGradient>
    <linearGradient id="hubGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
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

  <rect width="1000" height="500" rx="12" fill="url(#netBg)"/>

  <!-- Section Header (Clean, zero backslashes) -->
  <g transform="translate(45, 32)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      PROJECT NETWORK &amp; CONNECTED DOMAINS
    </text>
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="{TEXT_PRIMARY}">
      What I Build &amp; How It Connects
    </text>
  </g>

  <!-- Central Core: (500, 265) -->

  <!-- Interconnect Lines -->
  <!-- Hub 1: Top-Left (230, 135) -->
  <path d="M 500 265 Q 340 215 230 135" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 340 215 230 135" fill="none" stroke="{ACCENT_LIME}" stroke-width="1.8"/>

  <!-- Hub 2: Top-Right (770, 135) -->
  <path d="M 500 265 Q 660 215 770 135" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 660 215 770 135" fill="none" stroke="{ACCENT_GREEN}" stroke-width="1.8"/>

  <!-- Hub 3: Mid-Right (800, 280) -->
  <path d="M 500 265 L 800 280" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 L 800 280" fill="none" stroke="{ACCENT_AMBER}" stroke-width="1.8"/>

  <!-- Hub 4: Bottom-Right (760, 420) -->
  <path d="M 500 265 Q 640 355 760 420" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 640 355 760 420" fill="none" stroke="{ACCENT_BLUE}" stroke-width="1.8"/>

  <!-- Hub 5: Bottom-Left (240, 420) -->
  <path d="M 500 265 Q 350 355 240 420" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 Q 350 355 240 420" fill="none" stroke="{ACCENT_AMBER}" stroke-width="1.8"/>

  <!-- Hub 6: Mid-Left (200, 280) -->
  <path d="M 500 265 L 200 280" fill="none" stroke="#1c2b3e" stroke-width="2.5"/>
  <path class="conn-trace" d="M 500 265 L 200 280" fill="none" stroke="{ACCENT_LIME}" stroke-width="1.8"/>

  <!-- ==================== SATELLITE HUBS ==================== -->

  <!-- Hub 1: Full-Stack Web & SaaS (Top Left) -->
  <g transform="translate(100, 85)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_LIME}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Full-Stack SaaS &amp; Web</text>
    <text x="18" y="46" class="hub-desc">PROJECTS: Glamourly • Report-Maker</text>
    <text x="18" y="63" class="hub-desc">STACK: Next.js • React • TS • MongoDB</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_GREEN}">Real-time slots, verified listings</text>
  </g>

  <!-- Hub 2: Browser Systems & Extensions (Top Right) -->
  <g transform="translate(650, 85)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_GREEN}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Browser Systems &amp; Tools</text>
    <text x="18" y="46" class="hub-desc">PROJECT: Leet-Vault (Chrome MV3)</text>
    <text x="18" y="63" class="hub-desc">TECH: TypeScript • OAuth Flow • DOM FSM</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_GREEN}">Multi-named sync, collision queue</text>
  </g>

  <!-- Hub 3: Applied AI & Language Models (Mid Right) -->
  <g transform="translate(680, 235)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_AMBER}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Applied AI &amp; LLM Arenas</text>
    <text x="18" y="46" class="hub-desc">PROJECT: AI Debate Arena</text>
    <text x="18" y="63" class="hub-desc">STACK: Express • OpenRouter • Multi-LLM</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_AMBER}">Dual-model rebuttal, fallacy scoring</text>
  </g>

  <!-- Hub 4: Marine AI & Geospatial (Bottom Right) -->
  <g transform="translate(640, 380)">
    <rect width="255" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_BLUE}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Marine Geospatial Intel</text>
    <text x="18" y="46" class="hub-desc">PROJECT: OceanGuard (SIH 2026)</text>
    <text x="18" y="63" class="hub-desc">STACK: FastAPI • SciPy • Leaflet • SAR</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_BLUE}">Drift hindcasting &amp; AIS scoring</text>
  </g>

  <!-- Hub 5: Game Dev & Physics (Bottom Left) -->
  <g transform="translate(100, 380)">
    <rect width="255" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_AMBER}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Game Dev &amp; Physics</text>
    <text x="18" y="46" class="hub-desc">PROJECT: Rune-Striker (Godot 4.6)</text>
    <text x="18" y="63" class="hub-desc">ENGINE: Godot • GDScript • Windows .exe</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_AMBER}">Coyote time, input buffer, Raycast AI</text>
  </g>

  <!-- Hub 6: Media Utilities & Algorithms (Mid Left) -->
  <g transform="translate(70, 235)">
    <rect width="250" height="92" rx="8" fill="url(#hubGrad)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <circle cx="18" cy="22" r="4.5" fill="{ACCENT_LIME}"/>
    <text x="32" y="26" class="hub-title" fill="{TEXT_PRIMARY}">Media Utilities &amp; DSA</text>
    <text x="18" y="46" class="hub-desc">PROJECTS: yt-to-mp4 • LeetCode (C++)</text>
    <text x="18" y="63" class="hub-desc">STACK: Python • Flask • FFmpeg • Docker</text>
    <text x="18" y="80" class="hub-desc" fill="{ACCENT_GREEN}">18+ DSA topics, async transcoding</text>
  </g>

  <!-- ==================== CENTRAL CORE NODE ==================== -->
  <g transform="translate(500, 265)">
    <circle cx="0" cy="0" r="70" fill="none" stroke="#1c2b3e" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="56" fill="none" stroke="{BORDER_GREEN}" stroke-width="1.2" stroke-dasharray="6, 5"/>

    <circle cx="0" cy="0" r="44" fill="url(#coreGrad)" stroke="{ACCENT_GREEN}" stroke-width="1.5"/>

    <text x="0" y="-8" text-anchor="middle" class="core-label" fill="{ACCENT_LIME}">BUILD</text>
    <text x="0" y="8" text-anchor="middle" class="core-label" fill="{TEXT_PRIMARY}">ENGINEER</text>
    <text x="0" y="24" text-anchor="middle" class="core-label" fill="{ACCENT_GREEN}">SHIP</text>

    <!-- Satellite Orbit -->
    <circle cx="52" cy="-22" r="3" fill="{ACCENT_LIME}"/>
    <circle cx="-46" cy="32" r="3" fill="{ACCENT_AMBER}"/>
  </g>

  <!-- Outer Frame -->
  <rect x="1" y="1" width="998" height="498" rx="11" fill="none" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "engineering-network.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected engineering-network.svg")

def generate_workflow_inside_build():
    # 1000 x 220 viewBox: 5 equal 170px phases, 16px gap, 46px margin on right!
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 220" width="100%" height="100%">
  <defs>
    <linearGradient id="wfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="wfCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    <style>
      .wf-step-num {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 800; }}
      .wf-step-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; font-weight: 700; fill: {TEXT_PRIMARY}; }}
      .wf-step-desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: {TEXT_MUTED}; line-height: 1.4; }}
      .wf-step-tag {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {ACCENT_LIME}; }}
      @keyframes wfFlow {{ to {{ stroke-dashoffset: -20; }} }}
      .wf-conn {{ stroke-dasharray: 4, 4; animation: wfFlow 2s linear infinite; }}
    </style>
  </defs>

  <rect width="1000" height="220" rx="12" fill="url(#wfBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <g transform="translate(40, 22)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="{ACCENT_LIME}" letter-spacing="1">
      HOW I APPROACH BUILDING THINGS
    </text>
  </g>

  <!-- 5 Equal Phases: width 170 each, gap 16. Total width: 5*170 + 4*16 = 914. x=40 -> ends at 954. Right margin: 46px! -->

  <!-- Phase 1: Problem & Spec (x=40) -->
  <g transform="translate(40, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_LIME}">PHASE 01</text>
    <text x="14" y="44" class="wf-step-title">Problem &amp; Spec</text>
    <text x="14" y="66" class="wf-step-desc">Break down core user</text>
    <text x="14" y="82" class="wf-step-desc">pain points &amp; system</text>
    <text x="14" y="98" class="wf-step-desc">bottlenecks first.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag">System Blueprint</text>
  </g>

  <line class="wf-conn" x1="210" y1="118" x2="226" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 2: Schema & Engine (x=226) -->
  <g transform="translate(226, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_GREEN}">PHASE 02</text>
    <text x="14" y="44" class="wf-step-title">Schema &amp; Logic</text>
    <text x="14" y="66" class="wf-step-desc">Type-safe models,</text>
    <text x="14" y="82" class="wf-step-desc">clean DB schemas &amp;</text>
    <text x="14" y="98" class="wf-step-desc">core state machines.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_GREEN}">APIs &amp; State Logic</text>
  </g>

  <line class="wf-conn" x1="396" y1="118" x2="412" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 3: Interactive UI (x=412) -->
  <g transform="translate(412, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_AMBER}">PHASE 03</text>
    <text x="14" y="44" class="wf-step-title">Frontend &amp; UX</text>
    <text x="14" y="66" class="wf-step-desc">Fast, responsive UI,</text>
    <text x="14" y="82" class="wf-step-desc">dark mode layout &amp;</text>
    <text x="14" y="98" class="wf-step-desc">fluid user feedback.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_AMBER}">Next.js • React • CSS</text>
  </g>

  <line class="wf-conn" x1="582" y1="118" x2="598" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 4: Resilience & Tests (x=598) -->
  <g transform="translate(598, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_BLUE}">PHASE 04</text>
    <text x="14" y="44" class="wf-step-title">Resilience &amp; Tests</text>
    <text x="14" y="66" class="wf-step-desc">Edge-case testing,</text>
    <text x="14" y="82" class="wf-step-desc">offline retry queues &amp;</text>
    <text x="14" y="98" class="wf-step-desc">error recovery.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_BLUE}">50+ Tests • Edge Cases</text>
  </g>

  <line class="wf-conn" x1="768" y1="118" x2="784" y2="118" stroke="{ACCENT_LIME}" stroke-width="1.5"/>

  <!-- Phase 5: Ship & Deploy (x=784 -> ends at 954px. Clean 46px margin on right!) -->
  <g transform="translate(784, 44)">
    <rect width="170" height="148" rx="8" fill="url(#wfCard)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="{ACCENT_LIME}">PHASE 05</text>
    <text x="14" y="44" class="wf-step-title">Ship &amp; Deploy</text>
    <text x="14" y="66" class="wf-step-desc">Docker images,</text>
    <text x="14" y="82" class="wf-step-desc">CI/CD workflows &amp;</text>
    <text x="14" y="98" class="wf-step-desc">production hosting.</text>
    <rect x="12" y="118" width="146" height="18" rx="4" fill="#0d141d"/>
    <text x="18" y="131" class="wf-step-tag" fill="{ACCENT_LIME}">Deploy &amp; Monitor</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "workflow-inside-build.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected workflow-inside-build.svg")

def generate_animated_stats_card():
    # 1000 x 200 viewBox with pure SMIL rolling counter digits + animated language progress bars
    # Numbers roll from 0 on load! Works 100% natively in GitHub camo image renderer without JS!
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 200" width="100%" height="100%">
  <defs>
    <linearGradient id="stBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>
    <linearGradient id="stCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f2a"/>
      <stop offset="100%" stop-color="#101720"/>
    </linearGradient>
    
    <clipPath id="digitClip">
      <rect x="0" y="0" width="24" height="38"/>
    </clipPath>

    <style>
      .st-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; fill: {ACCENT_LIME}; letter-spacing: 0.8px; font-weight: 700; }}
      .st-num {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 32px; font-weight: 800; fill: {ACCENT_LIME}; }}
      .st-lbl {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 10.5px; fill: {TEXT_MUTED}; letter-spacing: 0.5px; font-weight: 600; }}
      .st-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: {TEXT_MUTED}; }}
    </style>
  </defs>

  <rect width="1000" height="200" rx="10" fill="url(#stBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(35, 24)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" class="st-title">GITHUB TELEMETRY &amp; ACTIVITY BENCHMARKS</text>
  </g>

  <!-- 4 Balanced Metric Cards (width 218 each, gap 16. 35 + 4*218 + 3*16 = 35 + 872 + 48 = 955 -> ends with 45px right margin) -->

  <!-- Card 1: Total Contributions (Rolls 0 -> 187) -->
  <g transform="translate(35, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_GREEN}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">CONTRIBUTIONS (YTD)</text>
    
    <!-- Rolling Counter: 1 8 7 -->
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="68">1</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -38" dur="1s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text><text x="2" y="334">8</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -304" dur="1.3s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(48, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -266" dur="1.6s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
    </g>
    <text x="18" y="112" class="st-sub">Live public GitHub stream</text>
  </g>

  <!-- Card 2: Public Repos (Rolls 0 -> 17) -->
  <g transform="translate(269, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">PUBLIC REPOSITORIES</text>
    
    <!-- Rolling Counter: 1 7 -->
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="68">1</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -38" dur="0.9s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -266" dur="1.4s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
    </g>
    <text x="18" y="112" class="st-sub">Full-stack, tools, &amp; games</text>
  </g>

  <!-- Card 3: Longest Streak (Rolls 0 -> 13) -->
  <g transform="translate(503, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">LONGEST STREAK (DAYS)</text>
    
    <!-- Rolling Counter: 1 3 -->
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_AMBER}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -38" dur="0.8s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num" fill="{ACCENT_AMBER}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -114" dur="1.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
    </g>
    <text x="18" y="112" class="st-sub">Consecutive active days</text>
  </g>

  <!-- Card 4: Top Language: TypeScript 74% (Animated Progress Bar & Counter) -->
  <g transform="translate(737, 48)">
    <rect width="218" height="132" rx="8" fill="url(#stCard)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>
    <text x="18" y="26" class="st-lbl">PRIMARY CODEBASE (TS)</text>
    
    <g transform="translate(18, 40)">
      <g clip-path="url(#digitClip)" transform="translate(0, 0)">
        <g class="st-num" fill="{ACCENT_BLUE}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text>
          <text x="2" y="182">4</text><text x="2" y="220">5</text><text x="2" y="258">6</text><text x="2" y="296">7</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -266" dur="1.1s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <g clip-path="url(#digitClip)" transform="translate(24, 0)">
        <g class="st-num" fill="{ACCENT_BLUE}">
          <text x="2" y="30">0</text><text x="2" y="68">1</text><text x="2" y="106">2</text><text x="2" y="144">3</text><text x="2" y="182">4</text>
          <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -152" dur="1.4s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
        </g>
      </g>
      <text x="50" y="30" class="st-num" fill="{ACCENT_BLUE}">%</text>
    </g>

    <!-- Animated progress bar from width 0 to 140 -->
    <rect x="18" y="86" width="180" height="6" rx="3" fill="#162230"/>
    <rect x="18" y="86" width="0" height="6" rx="3" fill="{ACCENT_BLUE}">
      <animate attributeName="width" from="0" to="134" dur="1.5s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
    <text x="18" y="112" class="st-sub">7.27 MB verified code</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "github-stats-animated.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated perfected github-stats-animated.svg")

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
            cells = [(c[1], c[0]) for c in cells]
        cells_data = cells
    except Exception as e:
        print(f"Warning: could not fetch live contributions ({e})")

    LVL_COLORS = {
        "0": "#16202c",  # Empty cell
        "1": "#123821",  # Low
        "2": "#1b5e34",  # Medium-low
        "3": "#22c55e",  # Active
        "4": "#39d353",  # High activity
    }

    # 1000 x 185 viewBox, ZERO mention of yaml or workflows!
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 185" width="100%" height="100%">
  <defs>
    <linearGradient id="snkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_DARK}"/>
      <stop offset="100%" stop-color="{BG_SURFACE}"/>
    </linearGradient>

    <style>
      .snk-title {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; fill: {ACCENT_LIME}; letter-spacing: 0.8px; font-weight: 700; }}
      .snk-legend {{ font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: {TEXT_MUTED}; }}
    </style>
  </defs>

  <rect width="1000" height="185" rx="10" fill="url(#snkBg)" stroke="{BORDER_SUBTLE}" stroke-width="1.2"/>

  <!-- Header (Clean, zero mention of yaml/workflows) -->
  <g transform="translate(35, 22)">
    <circle cx="6" cy="6" r="4" fill="{ACCENT_LIME}"/>
    <text x="18" y="10" class="snk-title">GITHUB CONTRIBUTION UNIVERSE • VERIFIED CALENDAR STREAM</text>
  </g>

  <!-- 53 cols x 7 rows Grid -->
  <g transform="translate(70, 42)">
'''
    idx = 0
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
            idx += 1

    # Continuous snake path slithering through the grid eating commits
    snake_path = "M 10 10 L 260 10 L 260 58 L 500 58 L 500 26 L 700 26 L 700 90 L 830 90 L 830 20 L 848 70"

    svg += f'''
    <!-- Animated Glowing Snake traversing the grid -->
    <path id="snakeTrack" d="{snake_path}" fill="none" stroke="none"/>

    <!-- Segment 4 (Tail) -->
    <circle r="4" fill="#1b5e34" opacity="0.6">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 3 -->
    <circle r="4.5" fill="{ACCENT_GREEN}">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto" begin="0.08s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 2 -->
    <circle r="5" fill="{ACCENT_LIME}">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto" begin="0.16s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>

    <!-- Segment 1 (Head) with bright lime and glow -->
    <circle r="6" fill="#00ff88" stroke="#ffffff" stroke-width="1.2">
      <animateMotion dur="11s" repeatCount="indefinite" rotate="auto" begin="0.24s">
        <mpath href="#snakeTrack"/>
      </animateMotion>
    </circle>
  </g>

  <!-- Legend -->
  <g transform="translate(70, 162)">
    <text x="0" y="9" class="snk-legend">187 CONTRIBUTIONS ACROSS THE PAST YEAR</text>
    <g transform="translate(710, 0)">
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
    print("Generated perfected github-contribution-grid-snake.svg")

if __name__ == "__main__":
    generate_hero_banner()
    generate_profile_matrix()
    generate_engineering_network()
    generate_workflow_inside_build()
    generate_animated_stats_card()
    generate_contribution_snake()
    print("All core assets regenerated with 1000px generous viewBoxes!")
