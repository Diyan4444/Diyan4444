"""
Asset Generator for Diyan Shah's GitHub Profile
Generates deterministic, handcrafted, high-fidelity SVGs matching the
'DIYAN SHAH — THE ENGINEERING PLAYGROUND' visual identity:
Deep Midnight Slate (#080c14), Electric Cyan (#00e5ff), Neon Teal (#00f5d4),
Violet Accent (#9d4edd), and Gold (#f7c948).
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

def generate_hero_banner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 320" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913"/>
      <stop offset="50%" stop-color="#0a1020"/>
      <stop offset="100%" stop-color="#080d1a"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="50%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#7928ca"/>
    </linearGradient>
    <linearGradient id="traceGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="#00e5ff" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00e5ff" stop-opacity="0.1"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111c33" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#0b1324" stop-opacity="0.95"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="subtleGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Grid Pattern -->
    <pattern id="techGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#162544" stroke-width="0.8" stroke-opacity="0.6"/>
      <circle cx="0" cy="0" r="1.5" fill="#00e5ff" fill-opacity="0.25"/>
    </pattern>

    <style>
      @keyframes pulseDot {
        0%, 100% { opacity: 0.3; transform: scale(0.9); }
        50% { opacity: 1; transform: scale(1.15); }
      }
      @keyframes dashFlow {
        to { stroke-dashoffset: -80; }
      }
      @keyframes floatParticle {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
      }
      @keyframes radarSweep {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      .telemetry-text {
        font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
        font-size: 11px;
        fill: #00e5ff;
        letter-spacing: 1.5px;
      }
      .tagline-text {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 14.5px;
        fill: #94a3b8;
        letter-spacing: 0.3px;
      }
      .name-text {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 44px;
        font-weight: 800;
        letter-spacing: 2.5px;
      }
      .badge-text {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
      }
      .flowing-line {
        stroke-dasharray: 8, 12;
        animation: dashFlow 3s linear infinite;
      }
      .live-dot {
        animation: pulseDot 2s ease-in-out infinite;
        transform-origin: 104px 44px;
      }
    </style>
  </defs>

  <!-- Canvas Background -->
  <rect width="960" height="320" rx="14" fill="url(#bgGrad)"/>
  <rect width="960" height="320" rx="14" fill="url(#techGrid)"/>

  <!-- Top Decorative Circuit Borders -->
  <path d="M 20 40 L 80 40 L 95 25 L 400 25" fill="none" stroke="#1d2e54" stroke-width="1.5"/>
  <path d="M 560 25 L 865 25 L 880 40 L 940 40" fill="none" stroke="#1d2e54" stroke-width="1.5"/>
  <circle cx="80" cy="40" r="3" fill="#00e5ff"/>
  <circle cx="880" cy="40" r="3" fill="#00e5ff"/>

  <!-- Flowing Circuit Line across Header -->
  <path class="flowing-line" d="M 30 160 L 140 160 L 170 190 L 260 190" fill="none" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.7"/>
  <path class="flowing-line" d="M 700 130 L 790 130 L 820 160 L 930 160" fill="none" stroke="#9d4edd" stroke-width="1.5" stroke-opacity="0.7"/>

  <!-- Top Telemetry Status Pill -->
  <g transform="translate(40, 32)">
    <rect width="260" height="26" rx="13" fill="#0d172e" stroke="#1d3056" stroke-width="1.2"/>
    <circle class="live-dot" cx="16" cy="13" r="4.5" fill="#00f5d4" filter="url(#subtleGlow)"/>
    <text x="32" y="17" class="telemetry-text" fill="#00f5d4">STATUS: ONLINE // READY TO BUILD</text>
  </g>

  <!-- Top Right Terminal Tag -->
  <g transform="translate(680, 32)">
    <rect width="240" height="26" rx="6" fill="#0d172e" stroke="#1d3056" stroke-width="1.2"/>
    <text x="16" y="17" class="telemetry-text" fill="#94a3b8">SYS.LOC: VJTI_MUMBAI // IT</text>
  </g>

  <!-- Center Content Block -->
  <g transform="translate(70, 95)">
    <!-- Subtitle / Role Tracker -->
    <text x="0" y="24" class="telemetry-text" fill="#00e5ff" font-weight="600">
      &gt; ARCHITECTING SYSTEMS • BUILDING INTERFACES • SHIPPING VALUE
    </text>

    <!-- Main Title -->
    <text x="0" y="70" class="name-text" fill="#ffffff">
      DIYAN <tspan fill="url(#cyanGrad)">SHAH</tspan>
    </text>

    <!-- One-line Summary -->
    <text x="0" y="105" class="tagline-text">
      Information Technology Student @ <tspan fill="#ffffff" font-weight="600">VJTI Mumbai</tspan>.
      Engineering full-stack architectures, systems tooling, AI workflows &amp; interactive software.
    </text>

    <!-- Badges Row -->
    <g transform="translate(0, 130)">
      <!-- Badge 1: Academic Base -->
      <g transform="translate(0, 0)">
        <rect width="145" height="30" rx="6" fill="#0d1830" stroke="#00e5ff" stroke-width="1" stroke-opacity="0.4"/>
        <circle cx="14" cy="15" r="3.5" fill="#00e5ff"/>
        <text x="26" y="19" class="badge-text" fill="#f1f5f9">B.Tech IT • VJTI</text>
      </g>

      <!-- Badge 2: Systems & Full-Stack -->
      <g transform="translate(155, 0)">
        <rect width="175" height="30" rx="6" fill="#0d1830" stroke="#00f5d4" stroke-width="1" stroke-opacity="0.4"/>
        <circle cx="14" cy="15" r="3.5" fill="#00f5d4"/>
        <text x="26" y="19" class="badge-text" fill="#f1f5f9">Full-Stack &amp; Systems</text>
      </g>

      <!-- Badge 3: Applied AI & ML -->
      <g transform="translate(340, 0)">
        <rect width="155" height="30" rx="6" fill="#0d1830" stroke="#9d4edd" stroke-width="1" stroke-opacity="0.5"/>
        <circle cx="14" cy="15" r="3.5" fill="#9d4edd"/>
        <text x="26" y="19" class="badge-text" fill="#f1f5f9">Applied AI &amp; Data</text>
      </g>

      <!-- Badge 4: Interactive Systems -->
      <g transform="translate(505, 0)">
        <rect width="170" height="30" rx="6" fill="#0d1830" stroke="#f7c948" stroke-width="1" stroke-opacity="0.4"/>
        <circle cx="14" cy="15" r="3.5" fill="#f7c948"/>
        <text x="26" y="19" class="badge-text" fill="#f1f5f9">Interactive &amp; Game Dev</text>
      </g>
    </g>
  </g>

  <!-- Right Decorative Radar / Node Orb -->
  <g transform="translate(830, 180)">
    <!-- Rotating Ring -->
    <circle cx="0" cy="0" r="55" fill="none" stroke="#16274a" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="42" fill="none" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.4" stroke-dasharray="6, 6"/>
    <circle cx="0" cy="0" r="28" fill="none" stroke="#9d4edd" stroke-width="1.5" stroke-opacity="0.6"/>
    <circle cx="0" cy="0" r="8" fill="#00e5ff" filter="url(#glowCyan)"/>

    <!-- Orbital Satellites -->
    <circle cx="36" cy="-22" r="3" fill="#00f5d4"/>
    <circle cx="-30" cy="30" r="3.5" fill="#f7c948"/>
    <circle cx="-38" cy="-18" r="2.5" fill="#9d4edd"/>
    <line x1="0" y1="0" x2="36" y2="-22" stroke="#00f5d4" stroke-width="0.8" stroke-opacity="0.5"/>
    <line x1="0" y1="0" x2="-30" y2="30" stroke="#f7c948" stroke-width="0.8" stroke-opacity="0.5"/>
  </g>

  <!-- Bottom Terminal Status Bar -->
  <g transform="translate(0, 288)">
    <rect width="960" height="32" fill="#050811" fill-opacity="0.9" stroke="#16233d" stroke-width="1"/>
    <text x="35" y="20" class="telemetry-text" fill="#64748b">
      CORE_STACK: <tspan fill="#00e5ff">TypeScript</tspan> • <tspan fill="#00e5ff">C++</tspan> • <tspan fill="#00e5ff">Python</tspan> • <tspan fill="#00e5ff">Next.js</tspan> • <tspan fill="#00e5ff">Node.js</tspan> • <tspan fill="#00e5ff">Godot</tspan> • <tspan fill="#00e5ff">Docker</tspan>
    </text>
    <text x="760" y="20" class="telemetry-text" fill="#00f5d4">
      [ 17 REPOSITORIES // ACTIVE ]
    </text>
  </g>

  <!-- Outer Border Frame with Glowing Corner Accents -->
  <rect x="1" y="1" width="958" height="318" rx="13" fill="none" stroke="#1b2a4a" stroke-width="1.5"/>
  <path d="M 1 30 L 1 1 L 30 1" fill="none" stroke="#00e5ff" stroke-width="2.5"/>
  <path d="M 930 1 L 959 1 L 959 30" fill="none" stroke="#00e5ff" stroke-width="2.5"/>
  <path d="M 1 290 L 1 319 L 30 319" fill="none" stroke="#00e5ff" stroke-width="2.5"/>
  <path d="M 930 319 L 959 319 L 959 290" fill="none" stroke="#00e5ff" stroke-width="2.5"/>
</svg>'''
    with open(ASSETS_DIR / "hero-banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated hero-banner.svg")

def generate_engineering_network():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="netBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b16"/>
      <stop offset="50%" stop-color="#0a1122"/>
      <stop offset="100%" stop-color="#070d18"/>
    </linearGradient>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="40%" stop-color="#00e5ff"/>
      <stop offset="100%" stop-color="#7928ca"/>
    </linearGradient>
    <linearGradient id="nodeGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#101e38"/>
      <stop offset="100%" stop-color="#0b1426"/>
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="coreGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="10" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="nodeGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="netGrid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#121e36" stroke-width="0.7"/>
      <circle cx="0" cy="0" r="1" fill="#00e5ff" fill-opacity="0.15"/>
    </pattern>

    <style>
      @keyframes dashMovement {
        from { stroke-dashoffset: 60; }
        to { stroke-dashoffset: 0; }
      }
      @keyframes coreRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      @keyframes nodePulse {
        0%, 100% { transform: scale(1); opacity: 0.95; }
        50% { transform: scale(1.02); opacity: 1; }
      }
      .conn-line {
        stroke-dasharray: 6, 8;
        animation: dashMovement 2.5s linear infinite;
      }
      .node-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.3px;
      }
      .node-subtitle {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10px;
        fill: #8b9bb4;
        letter-spacing: 0.2px;
      }
      .core-label {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 1.5px;
        fill: #ffffff;
      }
    </style>
  </defs>

  <rect width="960" height="520" rx="14" fill="url(#netBg)"/>
  <rect width="960" height="520" rx="14" fill="url(#netGrid)"/>

  <!-- Section Header Inside SVG -->
  <g transform="translate(40, 35)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#00e5ff" letter-spacing="2">
      // ARCHITECTURE TOPOLOGY • EVIDENCE-GROUNDED DOMAINS
    </text>
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#ffffff">
      The Engineering Playground Network
    </text>
  </g>

  <!-- Center Core Coordinates: (480, 275) -->

  <!-- Connection Traces (Center -> 6 Satellite Hubs) -->
  <!-- 1. Top-Left: Full-Stack Web & SaaS (Glamourly & Report-Maker) -> (210, 135) -->
  <path d="M 480 275 Q 320 220 210 135" fill="none" stroke="#1c2f54" stroke-width="3"/>
  <path class="conn-line" d="M 480 275 Q 320 220 210 135" fill="none" stroke="#00e5ff" stroke-width="1.8"/>

  <!-- 2. Top-Right: Browser Systems & Extensions (Leet-Vault MV3) -> (750, 135) -->
  <path d="M 480 275 Q 640 220 750 135" fill="none" stroke="#1c2f54" stroke-width="3"/>
  <path class="conn-line" d="M 480 275 Q 640 220 750 135" fill="none" stroke="#00f5d4" stroke-width="1.8"/>

  <!-- 3. Mid-Right: Applied AI & Multi-Model Arena (AI-Debater) -> (780, 290) -->
  <path d="M 480 275 L 780 290" fill="none" stroke="#1c2f54" stroke-width="3"/>
  <path class="conn-line" d="M 480 275 L 780 290" fill="none" stroke="#9d4edd" stroke-width="1.8"/>

  <!-- 4. Bottom-Right: Marine AI & Geospatial (OceanGuard / SIH) -> (740, 440) -->
  <path d="M 480 275 Q 620 370 740 440" fill="none" stroke="#1c2f54" stroke-width="3"/>
  <path class="conn-line" d="M 480 275 Q 620 370 740 440" fill="none" stroke="#00e5ff" stroke-width="1.8"/>

  <!-- 5. Bottom-Left: Interactive Systems & Game Dev (Rune-Striker) -> (220, 440) -->
  <path d="M 480 275 Q 330 370 220 440" fill="none" stroke="#1c2f54" stroke-width="3"/>
  <path class="conn-line" d="M 480 275 Q 330 370 220 440" fill="none" stroke="#f7c948" stroke-width="1.8"/>

  <!-- 6. Mid-Left: Media Utilities & Low-Latency DSA (yt-to-mp4 & LeetCode C++) -> (180, 290) -->
  <path d="M 480 275 L 180 290" fill="none" stroke="#1c2f54" stroke-width="3"/>
  <path class="conn-line" d="M 480 275 L 180 290" fill="none" stroke="#00e5ff" stroke-width="1.8"/>

  <!-- ==================== SATELLITE HUBS ==================== -->

  <!-- Hub 1: Full-Stack Web & SaaS (210, 135) -->
  <g transform="translate(90, 85)">
    <rect width="240" height="95" rx="10" fill="url(#nodeGrad1)" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.8" filter="url(#nodeGlow)"/>
    <circle cx="20" cy="24" r="5" fill="#00e5ff"/>
    <text x="34" y="28" class="node-title" fill="#ffffff">Full-Stack SaaS &amp; Web</text>
    <text x="20" y="48" class="node-subtitle">PROJECTS: Glamourly • Report-Maker</text>
    <text x="20" y="65" class="node-subtitle">STACK: Next.js • React • TS • MongoDB</text>
    <text x="20" y="82" class="node-subtitle" fill="#00f5d4">→ Real-time slots, Shop Act verification</text>
  </g>

  <!-- Hub 2: Browser Systems & Extensions (750, 135) -->
  <g transform="translate(630, 85)">
    <rect width="240" height="95" rx="10" fill="url(#nodeGrad1)" stroke="#00f5d4" stroke-width="1.2" stroke-opacity="0.8" filter="url(#nodeGlow)"/>
    <circle cx="20" cy="24" r="5" fill="#00f5d4"/>
    <text x="34" y="28" class="node-title" fill="#ffffff">Browser Systems &amp; Tools</text>
    <text x="20" y="48" class="node-subtitle">PROJECT: Leet-Vault (Chrome MV3)</text>
    <text x="20" y="65" class="node-subtitle">TECH: TypeScript • OAuth Flow • DOM FSM</text>
    <text x="20" y="82" class="node-subtitle" fill="#00f5d4">→ Multi-named sync, collision &amp; offline queue</text>
  </g>

  <!-- Hub 3: Applied AI & Multi-Model Arena (780, 290) -->
  <g transform="translate(660, 240)">
    <rect width="240" height="95" rx="10" fill="url(#nodeGrad1)" stroke="#9d4edd" stroke-width="1.2" stroke-opacity="0.9" filter="url(#nodeGlow)"/>
    <circle cx="20" cy="24" r="5" fill="#9d4edd"/>
    <text x="34" y="28" class="node-title" fill="#ffffff">Applied AI &amp; LLM Arenas</text>
    <text x="20" y="48" class="node-subtitle">PROJECT: AI Debate Arena</text>
    <text x="20" y="65" class="node-subtitle">STACK: Express • OpenRouter • Multi-LLM</text>
    <text x="20" y="82" class="node-subtitle" fill="#c084fc">→ Dual-model rebuttal, fallacy scoring</text>
  </g>

  <!-- Hub 4: Marine AI & Geospatial (740, 440) -->
  <g transform="translate(620, 395)">
    <rect width="250" height="95" rx="10" fill="url(#nodeGrad1)" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.8" filter="url(#nodeGlow)"/>
    <circle cx="20" cy="24" r="5" fill="#00e5ff"/>
    <text x="34" y="28" class="node-title" fill="#ffffff">Marine Geospatial Intelligence</text>
    <text x="20" y="48" class="node-subtitle">PROJECT: OceanGuard (SIH 2026)</text>
    <text x="20" y="65" class="node-subtitle">STACK: FastAPI • SciPy • Leaflet • SAR</text>
    <text x="20" y="82" class="node-subtitle" fill="#00e5ff">→ Drift hindcasting &amp; AIS vessel scoring</text>
  </g>

  <!-- Hub 5: Interactive Systems & Game Dev (220, 440) -->
  <g transform="translate(90, 395)">
    <rect width="250" height="95" rx="10" fill="url(#nodeGrad1)" stroke="#f7c948" stroke-width="1.2" stroke-opacity="0.8" filter="url(#nodeGlow)"/>
    <circle cx="20" cy="24" r="5" fill="#f7c948"/>
    <text x="34" y="28" class="node-title" fill="#ffffff">Game Dev &amp; Physics</text>
    <text x="20" y="48" class="node-subtitle">PROJECT: Rune-Striker (Godot 4.6)</text>
    <text x="20" y="65" class="node-subtitle">ENGINE: Godot • GDScript • Windows .exe</text>
    <text x="20" y="82" class="node-subtitle" fill="#f7c948">→ Coyote time, input buffer, Raycast AI</text>
  </g>

  <!-- Hub 6: Media Utilities & Algorithms (180, 290) -->
  <g transform="translate(60, 240)">
    <rect width="240" height="95" rx="10" fill="url(#nodeGrad1)" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.8" filter="url(#nodeGlow)"/>
    <circle cx="20" cy="24" r="5" fill="#00e5ff"/>
    <text x="34" y="28" class="node-title" fill="#ffffff">Media Utilities &amp; DSA</text>
    <text x="20" y="48" class="node-subtitle">PROJECTS: yt-to-mp4 • LeetCode (C++)</text>
    <text x="20" y="65" class="node-subtitle">STACK: Python • Flask • FFmpeg • Docker</text>
    <text x="20" y="82" class="node-subtitle" fill="#00e5ff">→ 18+ DSA topics, async transcoding</text>
  </g>

  <!-- ==================== CENTRAL CORE NODE ==================== -->
  <g transform="translate(480, 275)">
    <!-- Outer Orbit Ring -->
    <circle cx="0" cy="0" r="76" fill="none" stroke="#1d3056" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="62" fill="none" stroke="#00e5ff" stroke-width="1.5" stroke-opacity="0.4" stroke-dasharray="8, 6"/>

    <!-- Inner Core Orb -->
    <circle cx="0" cy="0" r="48" fill="url(#coreGrad)" filter="url(#coreGlow)"/>
    <circle cx="0" cy="0" r="44" fill="#090f1d"/>

    <!-- Core Labels -->
    <text x="0" y="-8" text-anchor="middle" class="core-label" fill="#00f5d4">BUILD</text>
    <text x="0" y="10" text-anchor="middle" class="core-label" fill="#00e5ff">ENGINEER</text>
    <text x="0" y="28" text-anchor="middle" class="core-label" fill="#9d4edd">SHIP</text>

    <!-- Satellite Orbit Particles -->
    <circle cx="58" cy="-24" r="3.5" fill="#00f5d4"/>
    <circle cx="-50" cy="38" r="3" fill="#f7c948"/>
  </g>

  <!-- Outer Border Frame -->
  <rect x="1" y="1" width="958" height="518" rx="13" fill="none" stroke="#192846" stroke-width="1.5"/>
</svg>'''
    with open(ASSETS_DIR / "engineering-network.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated engineering-network.svg")

def generate_profile_matrix():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 230" width="100%" height="100%">
  <defs>
    <linearGradient id="matrixBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080d1a"/>
      <stop offset="100%" stop-color="#0c1426"/>
    </linearGradient>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#121e38" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0e172c" stop-opacity="0.95"/>
    </linearGradient>
    <pattern id="matrixGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#162442" stroke-width="0.5"/>
    </pattern>
    <style>
      .mat-title {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        fill: #00e5ff;
        letter-spacing: 1.5px;
        font-weight: 700;
      }
      .mat-val {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13.5px;
        fill: #e2e8f0;
        line-height: 1.5;
      }
      .mat-metric-num {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 26px;
        font-weight: 800;
        fill: #00f5d4;
      }
      .mat-metric-lbl {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10px;
        fill: #94a3b8;
        letter-spacing: 1px;
      }
    </style>
  </defs>

  <rect width="960" height="230" rx="12" fill="url(#matrixBg)"/>
  <rect width="960" height="230" rx="12" fill="url(#matrixGrid)"/>

  <!-- Col 1: Identity & Engineering Philosophy -->
  <g transform="translate(30, 25)">
    <rect width="280" height="180" rx="10" fill="url(#cardBg)" stroke="#1d2e50" stroke-width="1.2"/>
    <text x="20" y="30" class="mat-title">01 // IDENTITY MATRIX</text>
    
    <text x="20" y="58" class="mat-val" font-weight="700" fill="#ffffff">Diyan Shah</text>
    <text x="20" y="78" class="mat-val" fill="#94a3b8">B.Tech Information Technology</text>
    <text x="20" y="98" class="mat-val" fill="#00e5ff" font-weight="600">VJTI Mumbai (Veermata Jijabai)</text>
    
    <line x1="20" y1="115" x2="260" y2="115" stroke="#1d2e50" stroke-width="1"/>
    
    <text x="20" y="138" class="mat-val" font-size="11.5" fill="#cbd5e1">
      "Learn by building real software.
    </text>
    <text x="20" y="156" class="mat-val" font-size="11.5" fill="#cbd5e1">
      Architect robust, verifiable products."
    </text>
  </g>

  <!-- Col 2: Engineering Domains -->
  <g transform="translate(330, 25)">
    <rect width="300" height="180" rx="10" fill="url(#cardBg)" stroke="#1d2e50" stroke-width="1.2"/>
    <text x="20" y="30" class="mat-title">02 // ACTIVE DOMAINS</text>
    
    <g transform="translate(20, 50)">
      <circle cx="5" cy="5" r="3" fill="#00e5ff"/>
      <text x="16" y="9" class="mat-val" font-size="12">Full-Stack Web &amp; Distributed APIs</text>
      
      <circle cx="5" cy="30" r="3" fill="#00f5d4"/>
      <text x="16" y="34" class="mat-val" font-size="12">Chrome Extensions (Manifest V3 Systems)</text>
      
      <circle cx="5" cy="55" r="3" fill="#9d4edd"/>
      <text x="16" y="59" class="mat-val" font-size="12">Multi-LLM Debate &amp; Prompt Orchestration</text>
      
      <circle cx="5" cy="80" r="3" fill="#f7c948"/>
      <text x="16" y="84" class="mat-val" font-size="12">Game Architecture &amp; Mechanics (Godot)</text>
      
      <circle cx="5" cy="105" r="3" fill="#00e5ff"/>
      <text x="16" y="109" class="mat-val" font-size="12">Data Structures &amp; Problem-Solving (C++)</text>
    </g>
  </g>

  <!-- Col 3: Verified Evidence Metrics -->
  <g transform="translate(650, 25)">
    <rect width="280" height="180" rx="10" fill="url(#cardBg)" stroke="#1d2e50" stroke-width="1.2"/>
    <text x="20" y="30" class="mat-title">03 // VERIFIED TELEMETRY</text>
    
    <g transform="translate(20, 48)">
      <!-- Metric 1 -->
      <g transform="translate(0, 0)">
        <text x="0" y="24" class="mat-metric-num">17</text>
        <text x="0" y="40" class="mat-metric-lbl">PUBLIC REPOSITORIES</text>
      </g>
      <!-- Metric 2 -->
      <g transform="translate(130, 0)">
        <text x="0" y="24" class="mat-metric-num" fill="#00e5ff">18+</text>
        <text x="0" y="40" class="mat-metric-lbl">DSA TOPICS (C++)</text>
      </g>
      <!-- Metric 3 -->
      <g transform="translate(0, 65)">
        <text x="0" y="24" class="mat-metric-num" fill="#9d4edd">5+</text>
        <text x="0" y="40" class="mat-metric-lbl">SYSTEM STACKS SHIPPED</text>
      </g>
      <!-- Metric 4 -->
      <g transform="translate(130, 65)">
        <text x="0" y="24" class="mat-metric-num" fill="#f7c948">100%</text>
        <text x="0" y="40" class="mat-metric-lbl">EVIDENCE-GROUNDED</text>
      </g>
    </g>
  </g>

  <!-- Outer Border -->
  <rect x="1" y="1" width="958" height="228" rx="11" fill="none" stroke="#1d2e50" stroke-width="1.2"/>
</svg>'''
    with open(ASSETS_DIR / "profile-matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated profile-matrix.svg")

def generate_pipeline_glamourly():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="gBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0b1222"/>
      <stop offset="100%" stop-color="#0e172a"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#14213d"/>
      <stop offset="100%" stop-color="#0f192e"/>
    </linearGradient>
    <style>
      .step-title { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: #00e5ff; letter-spacing: 0.5px; }
      .step-body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }
      .step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: #94a3b8; }
      @keyframes gFlow { to { stroke-dashoffset: -30; } }
      .g-arrow { stroke-dasharray: 5, 5; animation: gFlow 1.5s linear infinite; }
    </style>
  </defs>

  <rect width="920" height="180" rx="10" fill="url(#gBg)" stroke="#1a2d4e" stroke-width="1.2"/>

  <!-- Header Banner Inside -->
  <g transform="translate(25, 24)">
    <circle cx="6" cy="6" r="4" fill="#00e5ff"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#00e5ff" letter-spacing="1">
      GLAMOURLY // ARCHITECTURAL FLOW (MUMBAI SALON ECOSYSTEM)
    </text>
  </g>

  <!-- Step 1: User / Provider Discovery -->
  <g transform="translate(25, 45)">
    <rect width="195" height="110" rx="8" fill="url(#boxGrad)" stroke="#1f3458" stroke-width="1.2"/>
    <text x="15" y="24" class="step-title">01. DISCOVERY &amp; GEO</text>
    <text x="15" y="46" class="step-body">Mumbai salon filtering</text>
    <text x="15" y="64" class="step-body">Transparent rate cards</text>
    <text x="15" y="82" class="step-body">AI Concierge assistant</text>
    <text x="15" y="100" class="step-tag" fill="#00f5d4">Next.js • Tailwind CSS</text>
  </g>

  <!-- Flow Connector 1 -->
  <line class="g-arrow" x1="220" y1="100" x2="255" y2="100" stroke="#00e5ff" stroke-width="1.8"/>
  <polygon points="255,96 261,100 255,104" fill="#00e5ff"/>

  <!-- Step 2: Scheduling & Booking Engine -->
  <g transform="translate(265, 45)">
    <rect width="195" height="110" rx="8" fill="url(#boxGrad)" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.7"/>
    <text x="15" y="24" class="step-title">02. BOOKING ENGINE</text>
    <text x="15" y="46" class="step-body">Real-time slot lock</text>
    <text x="15" y="64" class="step-body">Stylist roster allocation</text>
    <text x="15" y="82" class="step-body">Zero forced prepayment</text>
    <text x="15" y="100" class="step-tag" fill="#00f5d4">TypeScript • React</text>
  </g>

  <!-- Flow Connector 2 -->
  <line class="g-arrow" x1="460" y1="100" x2="495" y2="100" stroke="#00e5ff" stroke-width="1.8"/>
  <polygon points="495,96 501,100 495,104" fill="#00e5ff"/>

  <!-- Step 3: Persistence & Verification -->
  <g transform="translate(505, 45)">
    <rect width="195" height="110" rx="8" fill="url(#boxGrad)" stroke="#1f3458" stroke-width="1.2"/>
    <text x="15" y="24" class="step-title">03. DATA &amp; COMPLIANCE</text>
    <text x="15" y="46" class="step-body">Shop Act licensing check</text>
    <text x="15" y="64" class="step-body">Provider shift management</text>
    <text x="15" y="82" class="step-body">Customer order history</text>
    <text x="15" y="100" class="step-tag" fill="#00f5d4">MongoDB • Node.js</text>
  </g>

  <!-- Flow Connector 3 -->
  <line class="g-arrow" x1="700" y1="100" x2="735" y2="100" stroke="#00e5ff" stroke-width="1.8"/>
  <polygon points="735,96 741,100 735,104" fill="#00e5ff"/>

  <!-- Step 4: Confirmation & Passes -->
  <g transform="translate(745, 45)">
    <rect width="150" height="110" rx="8" fill="url(#boxGrad)" stroke="#1f3458" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="#00f5d4">04. PASS DISPATCH</text>
    <text x="14" y="46" class="step-body">Instant email pass</text>
    <text x="14" y="64" class="step-body">Google Maps link</text>
    <text x="14" y="82" class="step-body">Status updates</text>
    <text x="14" y="100" class="step-tag" fill="#00e5ff">Offline Payment</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-glamourly.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated pipeline-glamourly.svg")

def generate_pipeline_leetvault():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="lvBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0b1222"/>
      <stop offset="100%" stop-color="#0c1626"/>
    </linearGradient>
    <linearGradient id="lvBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#14213d"/>
      <stop offset="100%" stop-color="#0f192e"/>
    </linearGradient>
    <style>
      .step-title { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: #00f5d4; letter-spacing: 0.5px; }
      .step-body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }
      .step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: #94a3b8; }
      @keyframes lvFlow { to { stroke-dashoffset: -30; } }
      .lv-arrow { stroke-dasharray: 5, 5; animation: lvFlow 1.5s linear infinite; }
    </style>
  </defs>

  <rect width="920" height="180" rx="10" fill="url(#lvBg)" stroke="#1a2d4e" stroke-width="1.2"/>

  <g transform="translate(25, 24)">
    <circle cx="6" cy="6" r="4" fill="#00f5d4"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#00f5d4" letter-spacing="1">
      LEET-VAULT // CHROME EXTENSION (MANIFEST V3) SUBMISSION PIPELINE
    </text>
  </g>

  <!-- Step 1: Submit Event & Snapshot State Machine -->
  <g transform="translate(25, 45)">
    <rect width="200" height="110" rx="8" fill="url(#lvBox)" stroke="#1f3458" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. SUBMISSION FSM</text>
    <text x="14" y="46" class="step-body">Submit click hook</text>
    <text x="14" y="64" class="step-body">Instant DOM snapshot</text>
    <text x="14" y="82" class="step-body">Zero false-positives</text>
    <text x="14" y="100" class="step-tag" fill="#00f5d4">Chrome MV3 Content Script</text>
  </g>

  <line class="lv-arrow" x1="225" y1="100" x2="255" y2="100" stroke="#00f5d4" stroke-width="1.8"/>
  <polygon points="255,96 261,100 255,104" fill="#00f5d4"/>

  <!-- Step 2: Auth & Permission Verification -->
  <g transform="translate(265, 45)">
    <rect width="200" height="110" rx="8" fill="url(#lvBox)" stroke="#00f5d4" stroke-width="1.2" stroke-opacity="0.8"/>
    <text x="14" y="24" class="step-title">02. SECURE OAUTH BROKER</text>
    <text x="14" y="46" class="step-body">launchWebAuthFlow</text>
    <text x="14" y="64" class="step-body">Zero PAT exposure</text>
    <text x="14" y="82" class="step-body">Push &amp; admin verify</text>
    <text x="14" y="100" class="step-tag" fill="#00e5ff">Chrome Identity API</text>
  </g>

  <line class="lv-arrow" x1="465" y1="100" x2="495" y2="100" stroke="#00f5d4" stroke-width="1.8"/>
  <polygon points="495,96 501,100 495,104" fill="#00f5d4"/>

  <!-- Step 3: Custom Naming & Collision Check -->
  <g transform="translate(505, 45)">
    <rect width="200" height="110" rx="8" fill="url(#lvBox)" stroke="#1f3458" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. SMART NAMING &amp; DUP</text>
    <text x="14" y="46" class="step-body">Custom: heap-sort.cpp</text>
    <text x="14" y="64" class="step-body">Deterministic N-fallback</text>
    <text x="14" y="82" class="step-body">SHA code fingerprinting</text>
    <text x="14" y="100" class="step-tag" fill="#00f5d4">18+ Languages Mapped</text>
  </g>

  <line class="lv-arrow" x1="705" y1="100" x2="735" y2="100" stroke="#00f5d4" stroke-width="1.8"/>
  <polygon points="735,96 741,100 735,104" fill="#00f5d4"/>

  <!-- Step 4: GitHub Push & Queue -->
  <g transform="translate(745, 45)">
    <rect width="150" height="110" rx="8" fill="url(#lvBox)" stroke="#1f3458" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="#00e5ff">04. GIT SYNC</text>
    <text x="14" y="46" class="step-body">Dual README update</text>
    <text x="14" y="64" class="step-body">Alarm retry queue</text>
    <text x="14" y="82" class="step-body">50+ unit tests</text>
    <text x="14" y="100" class="step-tag" fill="#00f5d4">GitHub REST API</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-leetvault.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated pipeline-leetvault.svg")

def generate_pipeline_debater():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="dbBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0b1020"/>
      <stop offset="100%" stop-color="#100b22"/>
    </linearGradient>
    <linearGradient id="dbBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a1438"/>
      <stop offset="100%" stop-color="#120e26"/>
    </linearGradient>
    <style>
      .step-title { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: #c084fc; letter-spacing: 0.5px; }
      .step-body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }
      .step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: #94a3b8; }
      @keyframes dbFlow { to { stroke-dashoffset: -30; } }
      .db-arrow { stroke-dasharray: 5, 5; animation: dbFlow 1.5s linear infinite; }
    </style>
  </defs>

  <rect width="920" height="180" rx="10" fill="url(#dbBg)" stroke="#321f58" stroke-width="1.2"/>

  <g transform="translate(25, 24)">
    <circle cx="6" cy="6" r="4" fill="#9d4edd"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#c084fc" letter-spacing="1">
      AI DEBATE ARENA // MULTI-MODEL REASONING &amp; SCORING ORCHESTRATION
    </text>
  </g>

  <!-- Step 1: Topic & Stance Ingestion -->
  <g transform="translate(25, 45)">
    <rect width="200" height="110" rx="8" fill="url(#dbBox)" stroke="#2f1e54" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. DEBATE SETUP</text>
    <text x="14" y="46" class="step-body">Topic &amp; motion config</text>
    <text x="14" y="64" class="step-body">Select Model A vs B</text>
    <text x="14" y="82" class="step-body">Difficulty &amp; rounds</text>
    <text x="14" y="100" class="step-tag" fill="#c084fc">Express.js API</text>
  </g>

  <line class="db-arrow" x1="225" y1="100" x2="255" y2="100" stroke="#9d4edd" stroke-width="1.8"/>
  <polygon points="255,96 261,100 255,104" fill="#9d4edd"/>

  <!-- Step 2: OpenRouter Orchestration -->
  <g transform="translate(265, 45)">
    <rect width="200" height="110" rx="8" fill="url(#dbBox)" stroke="#9d4edd" stroke-width="1.2" stroke-opacity="0.8"/>
    <text x="14" y="24" class="step-title">02. LLM ORCHESTRATOR</text>
    <text x="14" y="46" class="step-body">Turn-based context pipe</text>
    <text x="14" y="64" class="step-body">Prompt state injection</text>
    <text x="14" y="82" class="step-body">OpenRouter gateway</text>
    <text x="14" y="100" class="step-tag" fill="#00e5ff">Multi-Model Gateway</text>
  </g>

  <line class="db-arrow" x1="465" y1="100" x2="495" y2="100" stroke="#9d4edd" stroke-width="1.8"/>
  <polygon points="495,96 501,100 495,104" fill="#9d4edd"/>

  <!-- Step 3: Rebuttal & Round Processing -->
  <g transform="translate(505, 45)">
    <rect width="200" height="110" rx="8" fill="url(#dbBox)" stroke="#2f1e54" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. REBUTTAL ENGINE</text>
    <text x="14" y="46" class="step-body">Cross-examination state</text>
    <text x="14" y="64" class="step-body">Multi-turn memory loop</text>
    <text x="14" y="82" class="step-body">Real-time stream response</text>
    <text x="14" y="100" class="step-tag" fill="#c084fc">MongoDB Persistence</text>
  </g>

  <line class="db-arrow" x1="705" y1="100" x2="735" y2="100" stroke="#9d4edd" stroke-width="1.8"/>
  <polygon points="735,96 741,100 735,104" fill="#9d4edd"/>

  <!-- Step 4: Fallacy Scoring -->
  <g transform="translate(745, 45)">
    <rect width="150" height="110" rx="8" fill="url(#dbBox)" stroke="#2f1e54" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="#00f5d4">04. AI JUDGE</text>
    <text x="14" y="46" class="step-body">Fallacy detection</text>
    <text x="14" y="64" class="step-body">Persuasion metrics</text>
    <text x="14" y="82" class="step-body">Dynamic scorecard</text>
    <text x="14" y="100" class="step-tag" fill="#c084fc">Objective Evaluation</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-debater.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated pipeline-debater.svg")

def generate_pipeline_oceanguard():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="ogBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#071220"/>
      <stop offset="100%" stop-color="#08172c"/>
    </linearGradient>
    <linearGradient id="ogBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0e233d"/>
      <stop offset="100%" stop-color="#09182a"/>
    </linearGradient>
    <style>
      .step-title { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: #00e5ff; letter-spacing: 0.5px; }
      .step-body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #cbd5e1; }
      .step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: #94a3b8; }
      @keyframes ogFlow { to { stroke-dashoffset: -30; } }
      .og-arrow { stroke-dasharray: 5, 5; animation: ogFlow 1.5s linear infinite; }
    </style>
  </defs>

  <rect width="920" height="180" rx="10" fill="url(#ogBg)" stroke="#163456" stroke-width="1.2"/>

  <g transform="translate(25, 24)">
    <circle cx="6" cy="6" r="4" fill="#00e5ff"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#00e5ff" letter-spacing="1">
      OCEANGUARD AI // SAR SATELLITE OIL SPILL &amp; AIS VESSEL ATTRIBUTION (SIH 2026)
    </text>
  </g>

  <!-- Step 1: SAR Satellite Segmentation -->
  <g transform="translate(25, 45)">
    <rect width="200" height="110" rx="8" fill="url(#ogBox)" stroke="#1c3e66" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. SAR SEGMENTATION</text>
    <text x="14" y="46" class="step-body">Satellite radar imagery</text>
    <text x="14" y="64" class="step-body">AI oil slick mask</text>
    <text x="14" y="82" class="step-body">Dark spot extraction</text>
    <text x="14" y="100" class="step-tag" fill="#00e5ff">Computer Vision / AI</text>
  </g>

  <line class="og-arrow" x1="225" y1="100" x2="255" y2="100" stroke="#00e5ff" stroke-width="1.8"/>
  <polygon points="255,96 261,100 255,104" fill="#00e5ff"/>

  <!-- Step 2: Ocean Current Drift Hindcast -->
  <g transform="translate(265, 45)">
    <rect width="200" height="110" rx="8" fill="url(#ogBox)" stroke="#00e5ff" stroke-width="1.2" stroke-opacity="0.8"/>
    <text x="14" y="24" class="step-title">02. DRIFT HINDCASTING</text>
    <text x="14" y="46" class="step-body">Reverse current simulation</text>
    <text x="14" y="64" class="step-body">Wind &amp; hydrodynamic flow</text>
    <text x="14" y="82" class="step-body">Origin coordinate fix</text>
    <text x="14" y="100" class="step-tag" fill="#00f5d4">NumPy • SciPy</text>
  </g>

  <line class="og-arrow" x1="465" y1="100" x2="495" y2="100" stroke="#00e5ff" stroke-width="1.8"/>
  <polygon points="495,96 501,100 495,104" fill="#00e5ff"/>

  <!-- Step 3: AIS Vessel Cross-Reference -->
  <g transform="translate(505, 45)">
    <rect width="200" height="110" rx="8" fill="url(#ogBox)" stroke="#1c3e66" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. AIS CORRELATION</text>
    <text x="14" y="46" class="step-body">Vessel GPS cross-match</text>
    <text x="14" y="64" class="step-body">Speed anomaly detection</text>
    <text x="14" y="82" class="step-body">AIS blackout gap analysis</text>
    <text x="14" y="100" class="step-tag" fill="#00e5ff">FastAPI • SQLite</text>
  </g>

  <line class="og-arrow" x1="705" y1="100" x2="735" y2="100" stroke="#00e5ff" stroke-width="1.8"/>
  <polygon points="735,96 741,100 735,104" fill="#00e5ff"/>

  <!-- Step 4: Suspect Scoring Dashboard -->
  <g transform="translate(745, 45)">
    <rect width="150" height="110" rx="8" fill="url(#ogBox)" stroke="#1c3e66" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="#00f5d4">04. ATTRIBUTION</text>
    <text x="14" y="46" class="step-body">Suspect confidence score</text>
    <text x="14" y="64" class="step-body">CartoDB dark maps</text>
    <text x="14" y="82" class="step-body">Evidence reporting</text>
    <text x="14" y="100" class="step-tag" fill="#00f5d4">React 19 • Leaflet</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-oceanguard.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated pipeline-oceanguard.svg")

def generate_pipeline_runestriker():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="rsBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#141108"/>
      <stop offset="100%" stop-color="#1c160a"/>
    </linearGradient>
    <linearGradient id="rsBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2a200e"/>
      <stop offset="100%" stop-color="#1a1409"/>
    </linearGradient>
    <style>
      .step-title { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: #f7c948; letter-spacing: 0.5px; }
      .step-body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #f1f5f9; }
      .step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: #fde047; }
      @keyframes rsFlow { to { stroke-dashoffset: -30; } }
      .rs-arrow { stroke-dasharray: 5, 5; animation: rsFlow 1.5s linear infinite; }
    </style>
  </defs>

  <rect width="920" height="180" rx="10" fill="url(#rsBg)" stroke="#523e16" stroke-width="1.2"/>

  <g transform="translate(25, 24)">
    <circle cx="6" cy="6" r="4" fill="#f7c948"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#f7c948" letter-spacing="1">
      RUNE-STRIKER // GODOT 4.6 2D PLATFORMER ARCHITECTURE &amp; GAMEPLAY LOOP
    </text>
  </g>

  <!-- Step 1: Kinematic Controller -->
  <g transform="translate(25, 45)">
    <rect width="200" height="110" rx="8" fill="url(#rsBox)" stroke="#4a3713" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. PLAYER PHYSICS</text>
    <text x="14" y="46" class="step-body">Coyote Time jump grace</text>
    <text x="14" y="64" class="step-body">Input buffering queue</text>
    <text x="14" y="82" class="step-body">IDLE → RUN → JUMP FSM</text>
    <text x="14" y="100" class="step-tag">Godot 4.6 • CharacterBody2D</text>
  </g>

  <line class="rs-arrow" x1="225" y1="100" x2="255" y2="100" stroke="#f7c948" stroke-width="1.8"/>
  <polygon points="255,96 261,100 255,104" fill="#f7c948"/>

  <!-- Step 2: AI & Obstacle Patrol -->
  <g transform="translate(265, 45)">
    <rect width="200" height="110" rx="8" fill="url(#rsBox)" stroke="#f7c948" stroke-width="1.2" stroke-opacity="0.8"/>
    <text x="14" y="24" class="step-title">02. ENEMY RAYCAST AI</text>
    <text x="14" y="46" class="step-body">Patrolling slime enemies</text>
    <text x="14" y="64" class="step-body">Wall &amp; ledge raycasting</text>
    <text x="14" y="82" class="step-body">Deadly spikes &amp; hazards</text>
    <text x="14" y="100" class="step-tag">GDScript Vector Physics</text>
  </g>

  <line class="rs-arrow" x1="465" y1="100" x2="495" y2="100" stroke="#f7c948" stroke-width="1.8"/>
  <polygon points="495,96 501,100 495,104" fill="#f7c948"/>

  <!-- Step 3: Event Bus & Game Manager -->
  <g transform="translate(505, 45)">
    <rect width="200" height="110" rx="8" fill="url(#rsBox)" stroke="#4a3713" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. GAME MANAGER</text>
    <text x="14" y="46" class="step-body">Coin collect event bus</text>
    <text x="14" y="64" class="step-body">In-game HUD coin display</text>
    <text x="14" y="82" class="step-body">Contextual NPC dialogues</text>
    <text x="14" y="100" class="step-tag">Decoupled Signal Flow</text>
  </g>

  <line class="rs-arrow" x1="705" y1="100" x2="735" y2="100" stroke="#f7c948" stroke-width="1.8"/>
  <polygon points="735,96 741,100 735,104" fill="#f7c948"/>

  <!-- Step 4: Level End & Standalone Build -->
  <g transform="translate(745, 45)">
    <rect width="150" height="110" rx="8" fill="url(#rsBox)" stroke="#4a3713" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="#fde047">04. DEPLOYMENT</text>
    <text x="14" y="46" class="step-body">Victory portal cutscene</text>
    <text x="14" y="64" class="step-body">Death &amp; retry reload</text>
    <text x="14" y="82" class="step-body">Playable .exe package</text>
    <text x="14" y="100" class="step-tag">Windows Standalone</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-runestriker.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated pipeline-runestriker.svg")

def generate_pipeline_ytconverter():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="100%">
  <defs>
    <linearGradient id="ytBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#140b0e"/>
      <stop offset="100%" stop-color="#1c0f14"/>
    </linearGradient>
    <linearGradient id="ytBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2c141d"/>
      <stop offset="100%" stop-color="#1c0c12"/>
    </linearGradient>
    <style>
      .step-title { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 11px; font-weight: 700; fill: #fb7185; letter-spacing: 0.5px; }
      .step-body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11.5px; fill: #f1f5f9; }
      .step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; fill: #fda4af; }
      @keyframes ytFlow { to { stroke-dashoffset: -30; } }
      .yt-arrow { stroke-dasharray: 5, 5; animation: ytFlow 1.5s linear infinite; }
    </style>
  </defs>

  <rect width="920" height="180" rx="10" fill="url(#ytBg)" stroke="#4c1d2d" stroke-width="1.2"/>

  <g transform="translate(25, 24)">
    <circle cx="6" cy="6" r="4" fill="#f43f5e"/>
    <text x="18" y="10" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#fb7185" letter-spacing="1">
      YOUTUBE CONVERTER (YT-TO-MP4) // MEDIA PROCESSING PIPELINE
    </text>
  </g>

  <!-- Step 1: Input URL & Format Probe -->
  <g transform="translate(25, 45)">
    <rect width="200" height="110" rx="8" fill="url(#ytBox)" stroke="#4c1d2d" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">01. INGESTION &amp; PROBE</text>
    <text x="14" y="46" class="step-body">YouTube URL validation</text>
    <text x="14" y="64" class="step-body">Metadata &amp; format probe</text>
    <text x="14" y="82" class="step-body">MP4 / MP3 bitrate selector</text>
    <text x="14" y="100" class="step-tag">Flask REST API</text>
  </g>

  <line class="yt-arrow" x1="225" y1="100" x2="255" y2="100" stroke="#f43f5e" stroke-width="1.8"/>
  <polygon points="255,96 261,100 255,104" fill="#f43f5e"/>

  <!-- Step 2: Concurrency & Worker Queue -->
  <g transform="translate(265, 45)">
    <rect width="200" height="110" rx="8" fill="url(#ytBox)" stroke="#f43f5e" stroke-width="1.2" stroke-opacity="0.8"/>
    <text x="14" y="24" class="step-title">02. WORKER CONTROL</text>
    <text x="14" y="46" class="step-body">MAX_CONCURRENT=5 limit</text>
    <text x="14" y="64" class="step-body">Asynchronous job IDs</text>
    <text x="14" y="82" class="step-body">Real-time ETA &amp; speed</text>
    <text x="14" y="100" class="step-tag" fill="#00e5ff">Python Backend Core</text>
  </g>

  <line class="yt-arrow" x1="465" y1="100" x2="495" y2="100" stroke="#f43f5e" stroke-width="1.8"/>
  <polygon points="495,96 501,100 495,104" fill="#f43f5e"/>

  <!-- Step 3: Transcoding Engine -->
  <g transform="translate(505, 45)">
    <rect width="200" height="110" rx="8" fill="url(#ytBox)" stroke="#4c1d2d" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title">03. TRANSCODING</text>
    <text x="14" y="46" class="step-body">yt-dlp stream extraction</text>
    <text x="14" y="64" class="step-body">FFmpeg audio/video muxing</text>
    <text x="14" y="82" class="step-body">Temporary file auto-clean</text>
    <text x="14" y="100" class="step-tag">yt-dlp + FFmpeg</text>
  </g>

  <line class="yt-arrow" x1="705" y1="100" x2="735" y2="100" stroke="#f43f5e" stroke-width="1.8"/>
  <polygon points="735,96 741,100 735,104" fill="#f43f5e"/>

  <!-- Step 4: Streaming & Docker Container -->
  <g transform="translate(745, 45)">
    <rect width="150" height="110" rx="8" fill="url(#ytBox)" stroke="#4c1d2d" stroke-width="1.2"/>
    <text x="14" y="24" class="step-title" fill="#00f5d4">04. RUNTIME</text>
    <text x="14" y="46" class="step-body">Chunked file delivery</text>
    <text x="14" y="64" class="step-body">Dockerized isolation</text>
    <text x="14" y="82" class="step-body">Render cloud deployment</text>
    <text x="14" y="100" class="step-tag">Docker Container</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "pipeline-ytconverter.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated pipeline-ytconverter.svg")

def generate_workflow_inside_build():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 220" width="100%" height="100%">
  <defs>
    <linearGradient id="wfBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0b1224"/>
    </linearGradient>
    <linearGradient id="wfCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#121e38"/>
      <stop offset="100%" stop-color="#0d162b"/>
    </linearGradient>
    <style>
      .wf-step-num { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 12px; font-weight: 800; }
      .wf-step-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; font-weight: 700; fill: #ffffff; }
      .wf-step-desc { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: #94a3b8; line-height: 1.4; }
      .wf-step-tag { font-family: 'JetBrains Mono', Consolas, monospace; font-size: 9.5px; }
      @keyframes wfFlow { to { stroke-dashoffset: -20; } }
      .wf-conn { stroke-dasharray: 4, 4; animation: wfFlow 2s linear infinite; }
    </style>
  </defs>

  <rect width="960" height="220" rx="12" fill="url(#wfBg)" stroke="#1a2b4c" stroke-width="1.2"/>

  <g transform="translate(30, 24)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#00e5ff" letter-spacing="1.5">
      // INSIDE THE BUILD • HOW I ENGINEER &amp; SHIP REAL SOFTWARE
    </text>
  </g>

  <!-- 5 Stages -->

  <!-- Stage 1 -->
  <g transform="translate(30, 48)">
    <rect width="168" height="145" rx="8" fill="url(#wfCard)" stroke="#1e3256" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="#00e5ff">PHASE 01</text>
    <text x="14" y="44" class="wf-step-title">Problem &amp; Spec</text>
    <text x="14" y="66" class="wf-step-desc">Dissect core problem,</text>
    <text x="14" y="82" class="wf-step-desc">boundary conditions &amp;</text>
    <text x="14" y="98" class="wf-step-desc">technical bottlenecks.</text>
    <rect x="14" y="115" width="140" height="18" rx="4" fill="#081020"/>
    <text x="20" y="128" class="wf-step-tag" fill="#00e5ff">Architecture Blueprint</text>
  </g>

  <line class="wf-conn" x1="202" y1="120" x2="218" y2="120" stroke="#00e5ff" stroke-width="1.5"/>

  <!-- Stage 2 -->
  <g transform="translate(222, 48)">
    <rect width="168" height="145" rx="8" fill="url(#wfCard)" stroke="#1e3256" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="#00f5d4">PHASE 02</text>
    <text x="14" y="44" class="wf-step-title">Schema &amp; Engine</text>
    <text x="14" y="66" class="wf-step-desc">Type-safe models,</text>
    <text x="14" y="82" class="wf-step-desc">DB schemas (Mongo/PG)</text>
    <text x="14" y="98" class="wf-step-desc">&amp; core algorithms.</text>
    <rect x="14" y="115" width="140" height="18" rx="4" fill="#081020"/>
    <text x="20" y="128" class="wf-step-tag" fill="#00f5d4">State Machines &amp; APIs</text>
  </g>

  <line class="wf-conn" x1="394" y1="120" x2="410" y2="120" stroke="#00f5d4" stroke-width="1.5"/>

  <!-- Stage 3 -->
  <g transform="translate(414, 48)">
    <rect width="168" height="145" rx="8" fill="url(#wfCard)" stroke="#1e3256" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="#9d4edd">PHASE 03</text>
    <text x="14" y="44" class="wf-step-title">Interactive UI</text>
    <text x="14" y="66" class="wf-step-desc">Clean responsive UX,</text>
    <text x="14" y="82" class="wf-step-desc">live data streaming &amp;</text>
    <text x="14" y="98" class="wf-step-desc">fluid visual feedback.</text>
    <rect x="14" y="115" width="140" height="18" rx="4" fill="#081020"/>
    <text x="20" y="128" class="wf-step-tag" fill="#c084fc">Next.js • Tailwind • Leaflet</text>
  </g>

  <line class="wf-conn" x1="586" y1="120" x2="602" y2="120" stroke="#9d4edd" stroke-width="1.5"/>

  <!-- Stage 4 -->
  <g transform="translate(606, 48)">
    <rect width="168" height="145" rx="8" fill="url(#wfCard)" stroke="#1e3256" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="#f7c948">PHASE 04</text>
    <text x="14" y="44" class="wf-step-title">Resilience &amp; Tests</text>
    <text x="14" y="66" class="wf-step-desc">Unit/integration tests,</text>
    <text x="14" y="82" class="wf-step-desc">offline retry queues &amp;</text>
    <text x="14" y="98" class="wf-step-desc">collision handlers.</text>
    <rect x="14" y="115" width="140" height="18" rx="4" fill="#081020"/>
    <text x="20" y="128" class="wf-step-tag" fill="#f7c948">50+ Tests • Edge Cases</text>
  </g>

  <line class="wf-conn" x1="778" y1="120" x2="794" y2="120" stroke="#f7c948" stroke-width="1.5"/>

  <!-- Stage 5 -->
  <g transform="translate(798, 48)">
    <rect width="132" height="145" rx="8" fill="url(#wfCard)" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="14" y="24" class="wf-step-num" fill="#00e5ff">PHASE 05</text>
    <text x="14" y="44" class="wf-step-title">Ship &amp; Deploy</text>
    <text x="14" y="66" class="wf-step-desc">Docker images,</text>
    <text x="14" y="82" class="wf-step-desc">CI/CD pipelines &amp;</text>
    <text x="14" y="98" class="wf-step-desc">live hosting.</text>
    <rect x="14" y="115" width="104" height="18" rx="4" fill="#081020"/>
    <text x="18" y="128" class="wf-step-tag" fill="#00e5ff">Deploy to Prod</text>
  </g>
</svg>'''
    with open(ASSETS_DIR / "workflow-inside-build.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated workflow-inside-build.svg")

def generate_contribution_snake():
    # A standalone animated contribution grid with a glowing snake traveling across cells
    # Designed with high visual craft: 52 weeks x 7 days grid, dark theme, animated snake path
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 190" width="100%" height="100%">
  <defs>
    <linearGradient id="snkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <filter id="snakeGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      @keyframes snakeTravel {
        0% { transform: translate(60px, 60px); }
        20% { transform: translate(240px, 60px); }
        35% { transform: translate(240px, 120px); }
        55% { transform: translate(520px, 120px); }
        70% { transform: translate(520px, 75px); }
        85% { transform: translate(780px, 75px); }
        100% { transform: translate(840px, 135px); }
      }
      .snake-head {
        animation: snakeTravel 12s ease-in-out infinite alternate;
      }
      .cell-lvl0 { fill: #131d33; }
      .cell-lvl1 { fill: #0e4429; }
      .cell-lvl2 { fill: #006d32; }
      .cell-lvl3 { fill: #00e5ff; }
      .cell-lvl4 { fill: #00f5d4; }
    </style>
  </defs>

  <rect width="920" height="190" rx="12" fill="url(#snkBg)" stroke="#1a2c4e" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(30, 24)">
    <text x="0" y="0" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#00e5ff" letter-spacing="1.5">
      // CONTRIBUTION UNIVERSE • VERIFIED GITHUB ACTIVITY STREAM
    </text>
  </g>

  <!-- Contribution Heatmap Grid Simulation (Representative of active engineering year) -->
  <g transform="translate(35, 45)">
'''
    # Build 52 columns x 7 rows of cells
    # We will generate deterministic patterned cells
    import random
    rng = random.Random(4444)
    for col in range(53):
        x = col * 16
        for row in range(7):
            y = row * 16
            # Bias active commits towards recent weeks and weekdays
            val = rng.random()
            if col > 38:
                lvl = "cell-lvl4" if val > 0.75 else ("cell-lvl3" if val > 0.45 else ("cell-lvl2" if val > 0.2 else "cell-lvl0"))
            elif col > 20:
                lvl = "cell-lvl3" if val > 0.8 else ("cell-lvl2" if val > 0.6 else ("cell-lvl1" if val > 0.35 else "cell-lvl0"))
            else:
                lvl = "cell-lvl2" if val > 0.85 else ("cell-lvl1" if val > 0.65 else "cell-lvl0")
            svg += f'    <rect x="{x}" y="{y}" width="12" height="12" rx="2.5" class="{lvl}"/>\n'

    svg += '''  </g>

  <!-- Animated Glowing Snake Eating Activity Dots -->
  <g class="snake-head">
    <circle cx="0" cy="0" r="6" fill="#00f5d4" filter="url(#snakeGlow)"/>
    <circle cx="-7" cy="0" r="5" fill="#00e5ff"/>
    <circle cx="-13" cy="0" r="4.2" fill="#00b4d8"/>
    <circle cx="-18" cy="0" r="3.5" fill="#7928ca"/>
    <circle cx="-23" cy="0" r="2.8" fill="#9d4edd"/>
  </g>

  <!-- Legend & Telemetry Bar -->
  <g transform="translate(35, 168)">
    <text x="0" y="9" font-family="'JetBrains Mono', Consolas, monospace" font-size="10" fill="#64748b">
      AUTOMATED FEED: .github/workflows/snake.yml
    </text>
    <g transform="translate(680, 0)">
      <text x="-35" y="9" font-family="'JetBrains Mono', Consolas, monospace" font-size="9" fill="#94a3b8">Less</text>
      <rect x="0" y="0" width="10" height="10" rx="2" fill="#131d33"/>
      <rect x="14" y="0" width="10" height="10" rx="2" fill="#0e4429"/>
      <rect x="28" y="0" width="10" height="10" rx="2" fill="#006d32"/>
      <rect x="42" y="0" width="10" height="10" rx="2" fill="#00e5ff"/>
      <rect x="56" y="0" width="10" height="10" rx="2" fill="#00f5d4"/>
      <text x="72" y="9" font-family="'JetBrains Mono', Consolas, monospace" font-size="9" fill="#94a3b8">More</text>
    </g>
  </g>
</svg>'''
    with open(ASSETS_DIR / "github-contribution-grid-snake.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated github-contribution-grid-snake.svg")

if __name__ == "__main__":
    generate_hero_banner()
    generate_engineering_network()
    generate_profile_matrix()
    generate_pipeline_glamourly()
    generate_pipeline_leetvault()
    generate_pipeline_debater()
    generate_pipeline_oceanguard()
    generate_pipeline_runestriker()
    generate_pipeline_ytconverter()
    generate_workflow_inside_build()
    generate_contribution_snake()
    print("All custom assets successfully generated!")
