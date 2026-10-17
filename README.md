<!-- ================================================================= -->
<!--                DIYAN SHAH — THE ENGINEERING PLAYGROUND            -->
<!-- ================================================================= -->

<div align="center">
  <a href="https://github.com/Diyan4444">
    <img src="assets/hero-banner.svg" width="100%" alt="Diyan Shah — The Engineering Playground Hero Banner" />
  </a>
</div>

<br>

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Diyan4444-22c55e?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=16202c)](https://github.com/Diyan4444)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diyan_Shah-39d353?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=16202c)](https://www.linkedin.com/in/diyan-shah-14b4993a9/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Diyan4444-f59e0b?style=for-the-badge&logo=leetcode&logoColor=ffffff&labelColor=16202c)](https://leetcode.com/u/diddy4/)
[![Email](https://img.shields.io/badge/Email-diyanshah2301%40gmail.com-38bdf8?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=16202c)](mailto:diyanshah2301@gmail.com)

</div>

<br>

---

## ⚡ About Me

I'm **Diyan Shah**, an **Information Technology Sophomore at VJTI Mumbai (Veermata Jijabai Technological Institute)**. 

I love engineering software by building real systems from the ground up. Instead of just following tutorials, I learn by shipping: from full-stack platforms and production Chrome extensions (Manifest V3) to multi-model LLM debate engines, satellite radar geospatial pipelines, and 2D games in Godot.

```text
  [ Core Stack ]   TypeScript • C++ • Python • Next.js • Node.js • Godot • Docker • MongoDB
  [ Education  ]   Information Technology Sophomore — VJTI Mumbai
  [ Focus Area ]   Full-Stack Systems • Browser Tools • Applied AI • Algorithmic Problem Solving
  [ Philosophy ]   "Learn by shipping real software. Deep dives over surface tutorials."
```

---

## 🌐 Project Architecture & Domains

The diagram below shows how my core foundation connects across different technical domains and projects.

<div align="center">
  <img src="assets/engineering-network.svg" width="100%" alt="Project Network Architecture" />
</div>

<br>

### 📡 Network Node Breakdown

1. **Full-Stack SaaS & Web Platforms**  
   * **[Glamourly](https://github.com/Diyan4444/Glamourly)**: Curated salon discovery and real-time appointment booking engine handcrafted for Mumbai with Next.js, React, TypeScript, and MongoDB. Features zero forced prepayments and Shop Act verification.
   * **[Report-Maker](https://github.com/Diyan4444/Report-Maker)**: Internal corporate intelligence platform tracking company profiles, relationship graphs, and automated PDF/Excel reports with PostgreSQL (Prisma), Redis, and Docker.
   * **[RentWheels](https://github.com/Diyan4444/RentWheels)**: Responsive vehicle rental platform deployed live at [wheel-rent.netlify.app](https://wheel-rent.netlify.app/).

2. **Browser Systems & Tooling**  
   * **[Leet-Vault](https://github.com/Diyan4444/Leet-Vault)**: Chrome Extension (Manifest V3) engineered with a strict DOM snapshot state machine, serverless OAuth broker, 18+ language mappings, collision resolution, and offline alarm retry queues backed by 50+ unit/integration tests.

3. **Applied AI & LLM Sparring**  
   * **[AI Debate Arena](https://github.com/Diyan4444/AI-Debater)**: Turn-based debate platform comparing how different language models argue and respond to topics using Express.js, MongoDB, and OpenRouter API, featuring real-time argument streaming and automated fallacy judging.

4. **Geospatial & Marine Intelligence**  
   * **[OceanGuard AI](https://github.com/Diyan4444/OceanGuard)**: Smart India Hackathon 2026 project combining SAR satellite radar imagery segmentation, ocean current hydrodynamic drift hindcasting, and AIS vessel cross-matching with FastAPI, SciPy, React 19, and Leaflet.

5. **Interactive Systems & Game Development**  
   * **[Rune-Striker](https://github.com/Diyan4444/Rune-Striker)**: Handcrafted 2D retro action-platformer in Godot 4.6 (GDScript) with Coyote Time jump forgiveness, input buffering, slime raycast patrol AI, decoupled coin event bus, and a standalone Windows `.exe` build.

6. **Media Utilities & High-Throughput DSA**  
   * **[YouTube Converter (yt-to-mp4)](https://github.com/Diyan4444/yt-to-mp4)**: Media extraction utility built with Flask, yt-dlp, FFmpeg, and Docker with concurrency throttling and temp-file auto-cleanup.
   * **[LeetCode Practice (C++)](https://github.com/Diyan4444/LeetCode)**: Algorithmic solutions categorized across 18+ topics including Dynamic Programming, Graphs, Heaps, Trees, and Trie structures in C++.

---

## 🎛️ Developer Console HUD

<div align="center">
  <img src="assets/profile-matrix.svg" width="100%" alt="Diyan Shah Identity & Telemetry HUD Matrix" />
</div>

---

## 🚀 Featured Projects

A closer look at some of the primary projects I've built, how they work under the hood, and the problems they solve.

<br>

### 1. 💇 Glamourly — Mumbai Salon Discovery & Direct Booking Platform
> **Repository:** [`Diyan4444/Glamourly`](https://github.com/Diyan4444/Glamourly)

* **Problem Solved:** Most salon booking portals enforce upfront online prepayments, lack verified licenses, or obscure true treatment pricing.
* **Architecture & Capabilities:**
  * **Geospatial Discovery:** Filter verified beauty studios across Mumbai (Bandra, Juhu, Worli, Colaba, Andheri) by real distance, rating, and explicit treatment rate cards.
  * **Zero Prepayments:** Direct offline reservations where customers pay strictly after service completion.
  * **Provider Control Dashboard:** Salon owners configure branch operating hours, manage stylist shift allocations, declare break periods, and verify statutory Shop Act and trade licenses.
  * **AI Concierge:** Embedded smart salon assistant delivering personalized treatment recommendations based on user preferences.
* **Stack:** `Next.js` • `React` • `TypeScript` • `Tailwind CSS` • `Node.js` • `MongoDB Atlas`

---

### 2. ⚡ Leet-Vault — Chrome Extension (Manifest V3) Solution Sync
> **Repository:** [`Diyan4444/Leet-Vault`](https://github.com/Diyan4444/Leet-Vault) • **Test Suite:** 50+ Unit/Integration Tests

* **Problem Solved:** Existing LeetCode sync extensions blindly overwrite previous solutions, leak personal access tokens (PATs), trigger false-positive commits on page navigation, or crash on network drops.
* **Architecture & Capabilities:**
  * **User-Named Multi-Solution Architecture:** Enables unlimited named solutions per problem (`0912-sort-an-array/heap-sort.cpp`, `merge-sort.cpp`) with deterministic `solution-N.cpp` fallback.
  * **Submit-Only Snapshot State Machine:** Hooks exclusively into user **Submit** actions, capturing an immediate code snapshot to eliminate SPA false positives.
  * **Production OAuth Broker:** Implements `chrome.identity.launchWebAuthFlow` with zero client secrets embedded in the extension bundle and authoritative write-permission verification.
  * **Collision & Duplicate Protection:** Generates SHA code fingerprints to prevent duplicate commits and offers explicit overwrite vs. versioning prompts.
  * **Offline Alarm Queue:** Catches GitHub API rate limits and network drops in a persistent queue with automatic alarm-based retry cycles.
* **Stack:** `TypeScript` • `Chrome Extensions API (MV3)` • `Chrome Identity API` • `GitHub REST API` • `Vite` • `Vitest`

---

### 3. 🤖 AI Debate Arena — Multi-Model Argumentation & Scoring Engine
> **Repository:** [`Diyan4444/AI-Debater`](https://github.com/Diyan4444/AI-Debater)

* **Problem Solved:** Evaluating and comparing how different LLMs reason, handle rebuttals, and maintain logical integrity when debating contentious motions.
* **Architecture & Capabilities:**
  * **Turn-Based Debate Orchestration:** Configures topics, stances, difficulty parameters, and round counts between two distinct language models.
  * **OpenRouter Gateway Integration:** Unified API interface querying competing LLMs under structured system prompts.
  * **Dynamic Scoring & Fact-Checking:** Automated scoring layer evaluating counterarguments for logical consistency, fallacies, persuasiveness, and clarity.
* **Stack:** `Node.js` • `Express.js API` • `MongoDB` • `OpenRouter API` • `JavaScript (ES6+)`

---

### 4. 🛰️ OceanGuard AI — SAR Satellite Oil Spill & AIS Vessel Attribution
> **Repository:** [`Diyan4444/OceanGuard`](https://github.com/Diyan4444/OceanGuard) • Built for Smart India Hackathon 2026 (Problem SIH26143)

* **Problem Solved:** Identifying illegal marine oil dumping from space, accounting for ocean surface drift, and legally holding responsible maritime vessels accountable.
* **Architecture & Capabilities:**
  * **SAR Satellite Segmentation:** Extracts dark slicks from Synthetic Aperture Radar (SAR) imagery via computer vision segmentation models.
  * **Hydrodynamic Drift Hindcasting:** Simulates ocean currents and wind vectors backward in time to calculate the exact spill origin coordinates.
  * **AIS Telemetry Cross-Referencing:** Cross-references global AIS vessel tracks with the calculated origin coordinates and timestamps.
  * **Suspect Anomaly Scoring:** Evaluates candidate ships on proximity, speed anomalies, and deliberate AIS transmitter blackouts.
* **Stack:** `Python` • `FastAPI` • `NumPy` • `SciPy` • `React 19` • `Vite` • `Leaflet` • `CartoDB Dark Tiles` • `SQLite`

---

### 5. ⚔️ Rune-Striker — 2D Retro Action-Platformer
> **Repository:** [`Diyan4444/Rune-Striker`](https://github.com/Diyan4444/Rune-Striker)

* **Problem Solved:** Designing responsive, forgiving 2D kinematic platforming mechanics and autonomous enemy patrol AI without bloated engine overhead.
* **Architecture & Capabilities:**
  * **Precision Movement & Coyote Time:** Implements jump forgiveness (Coyote Time) and input buffering to prevent missed inputs at platform ledges.
  * **Character Kinematic FSM:** Smooth state transitions between `IDLE`, `RUN`, and `JUMP` with direction facing logic.
  * **Raycast Enemy Patrols:** Slimes patrol platforms autonomously, using horizontal and downward ledge raycasts to detect barriers and turnaround points.
  * **Decoupled Game Manager Event Bus:** Coin collection and HUD counter updates communicated via Godot signals.
  * **Release Packaging:** Exported as an optimized, standalone Windows `.exe` binary.
* **Stack:** `Godot 4.6` • `GDScript` • `2D Vector Physics` • `Raycast Collision AI` • `Windows Executable`

---

### 6. 🎬 YouTube Converter (`yt-to-mp4`) — Media Transcoding Service
> **Repository:** [`Diyan4444/yt-to-mp4`](https://github.com/Diyan4444/yt-to-mp4)

* **Problem Solved:** Lightweight, containerized web service for high-quality audio and video transcoding without third-party ad injection.
* **Architecture & Capabilities:**
  * **Format & Quality Probing:** Fetches available container formats, resolutions, and audio bitrates dynamically.
  * **Worker Concurrency Throttling:** Strict queue management (`MAX_CONCURRENT_DOWNLOADS=5`) prevents CPU exhaustion during FFmpeg transcode jobs.
  * **Real-Time Progress Streaming:** API polling for download percentages, byte rates, and estimated completion times.
  * **Automated Ephemeral Cleanup:** Temporary scratch files automatically purged post-transcoding to maintain disk health.
* **Stack:** `Python` • `Flask` • `yt-dlp` • `FFmpeg` • `Docker` • `Render Config`

---

## 🛠️ How I Build Software

How I take an idea from initial specification to a deployed, working build:

<div align="center">
  <img src="assets/workflow-inside-build.svg" width="100%" alt="How I Build Software" />
</div>

<br>

| Phase | Methodology & Actions | Verifiable Evidence |
| :--- | :--- | :--- |
| **01. Problem & Architecture** | Dissect user pain points, define boundary conditions, and draft system contracts before writing code. | Leet-Vault submission state machine specification; Glamourly Shop Act flow. |
| **02. Schema & Engine Design** | Design type-safe data models, relational/document schemas, and state machines with zero data corruption. | MongoDB Atlas clusters, PostgreSQL Prisma schemas, Godot kinematic FSMs. |
| **03. UI & Interactive Experience** | Develop responsive, dark-mode native interfaces with real-time feedback and clean typography. | React 19, Next.js App Router, Tailwind CSS, Leaflet geospatial maps. |
| **04. Testing & Edge-Case Resilience** | Implement deterministic error queues, duplicate code detection, and exhaustive unit suites. | 50+ unit and integration tests in Leet-Vault; Coyote jump buffering in Rune-Striker. |
| **05. Containerization & Deployment** | Package binaries, Docker containers, and CI/CD pipelines for production stability. | Dockerfiles, Render configurations, Netlify live deployments, Standalone `.exe`. |

---

## 💻 Skills & Technologies

Technologies I actively work with and have shipped projects using:

<table>
  <tr>
    <td width="33%" valign="top">
      <h4>⚡ Languages</h4>
      <ul>
        <li><b>TypeScript</b> (Glamourly, Leet-Vault, Report-Maker)</li>
        <li><b>JavaScript [ES6+]</b> (AI-Debater, RentWheels)</li>
        <li><b>C++ [STL / DSA]</b> (LeetCode, Shorties, OSTLAB)</li>
        <li><b>Python</b> (OceanGuard, yt-to-mp4)</li>
        <li><b>GDScript</b> (Rune-Striker Engine)</li>
        <li><b>SQL / PLpgSQL</b> (PostgreSQL / Prisma)</li>
        <li><b>HTML5 & CSS3</b> (Modern responsive semantic layouts)</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h4>🌐 Frontend & UI</h4>
      <ul>
        <li><b>Next.js (App Router)</b></li>
        <li><b>React & React 19</b></li>
        <li><b>Tailwind CSS</b></li>
        <li><b>Vite & Bundlers</b></li>
        <li><b>Leaflet.js & CartoDB Maps</b></li>
        <li><b>Recharts Data Visualization</b></li>
        <li><b>Responsive / Dark Mode Systems</b></li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h4>⚙️ Backend & Systems</h4>
      <ul>
        <li><b>Node.js & Express.js</b></li>
        <li><b>FastAPI (Python)</b></li>
        <li><b>Flask REST APIs</b></li>
        <li><b>Chrome Extension MV3 Architecture</b></li>
        <li><b>Chrome Identity API & OAuth Brokers</b></li>
        <li><b>OpenRouter Multi-LLM Gateway</b></li>
        <li><b>FFmpeg & yt-dlp Transcoding</b></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <h4>🗄️ Databases & Storage</h4>
      <ul>
        <li><b>MongoDB Atlas</b> (Document Store)</li>
        <li><b>PostgreSQL & Prisma ORM</b></li>
        <li><b>Redis</b> (Cache & Sessions)</li>
        <li><b>SQLite</b> (Zero-config local DB)</li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h4>🛠️ DevOps & Environments</h4>
      <ul>
        <li><b>Docker & Containerization</b></li>
        <li><b>Git & GitHub Actions</b></li>
        <li><b>Linux Command Line & Bash</b></li>
        <li><b>VS Code & Android Studio</b></li>
        <li><b>Netlify & Render Deployments</b></li>
      </ul>
    </td>
    <td width="33%" valign="top">
      <h4>🔭 Active Learning & Research</h4>
      <ul>
        <li><b>Computer Vision</b> (OpenCV workshops)</li>
        <li><b>Multi-Agent LLM Orchestration</b></li>
        <li><b>SAR Satellite Hydrodynamics</b></li>
        <li><b>Advanced Competitive DSA (C++)</b></li>
      </ul>
    </td>
  </tr>
</table>

---

## 📊 GitHub Stats & Activity

A snapshot of my development activity across 17 public repositories with live counters:

<div align="center">
  <img src="assets/github-stats-animated.svg" width="100%" alt="Live Telemetry & Activity Benchmarks" />
</div>

<br>

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Diyan4444&show_icons=true&theme=tokyonight&bg_color=0c1017&border_color=202c3c&title_color=39d353&text_color=94a3b8&icon_color=22c55e&hide_border=false" width="48%" alt="Diyan's GitHub Stats" />
  &nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Diyan4444&layout=compact&theme=tokyonight&bg_color=0c1017&border_color=202c3c&title_color=39d353&text_color=94a3b8&icon_color=22c55e&hide_border=false" width="48%" alt="Top Languages Used" />
</div>

<br>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=Diyan4444&theme=tokyonight&background=0c1017&border=202c3c&stroke=39d353&ring=22c55e&fire=f59e0b&currStreakLabel=39d353" width="97%" alt="Contribution Streak" />
</div>

<br>

### 📋 Activity Overview

| Metric Dimension | Audited Value | Primary Data Source |
| :--- | :--- | :--- |
| **Public Repositories** | **17 Repositories** | GitHub REST API (`/users/Diyan4444`) |
| **Contributions (YTD)** | **187 Contributions** | GitHub Public Contributions Stream |
| **Dominant Languages** | **TypeScript (74%), JavaScript (12%), C++ (5%), Python (4%)** | GitHub Languages Byte Counts |
| **Algorithmic Topics** | **18+ DSA Directories (C++)** | [`Diyan4444/LeetCode`](https://github.com/Diyan4444/LeetCode) |
| **Shipped System Stacks** | **6 Production Architectures** | Full-stack, Extensions, Games, AI, Media, Corporate Intel |
| **Hackathon Work** | **Smart India Hackathon 2026** | Problem Statement SIH26143 (`OceanGuard AI`) |

---

## 🟩 Contribution Calendar

A visual calendar of my GitHub contributions over the past year:

<div align="center">
  <img src="assets/github-contribution-grid-snake.svg" width="100%" alt="Diyan Shah Contribution Snake Animation" />
</div>

---

## 🧭 My Journey & What's Next

```text
[ FOUNDATIONS ]  ───────►  [ SYSTEMS & FULL-STACK ]  ───────►  [ ADVANCED DOMAINS ]  ───────►  [ FUTURE AMBITIONS ]
 • VJTI IT Degree           • Next.js / TypeScript Web         • Chrome MV3 Extensions          • Distributed Systems
 • C++ STL & Data Structs   • REST APIs & MongoDB / PG         • Multi-Model LLM Orchestration  • High-Throughput Engines
 • Algorithmic Rigor        • Docker Containerization          • Godot Kinematic Physics        • Intelligent Cloud Platforms
```

* **Where I've spent time:** Building complete products from start to finish—salon booking platforms, browser extensions, 2D game mechanics, and media processing tools.
* **What I'm exploring now:** Multi-agent LLM systems, computer vision with OpenCV, and scalable backend design.
* **What I want to build:** High-throughput distributed systems and developer tools that make developers' lives easier.

---

## 📬 Get in Touch

I'm always keen to chat about software engineering, developer tooling, or discuss internship and collaboration opportunities.

<div align="center">

<a href="mailto:diyanshah2301@gmail.com">
  <img src="https://img.shields.io/badge/Email-diyanshah2301%40gmail.com-38bdf8?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=16202c" alt="Send Email" />
</a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/diyan-shah-14b4993a9/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Connect%20with%20Diyan-39d353?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=16202c" alt="Connect on LinkedIn" />
</a>
&nbsp;&nbsp;
<a href="https://github.com/Diyan4444" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-Follow%20%40Diyan4444-22c55e?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=16202c" alt="Follow on GitHub" />
</a>
&nbsp;&nbsp;
<a href="https://leetcode.com/u/diddy4/" target="_blank">
  <img src="https://img.shields.io/badge/LeetCode-Diyan4444-f59e0b?style=for-the-badge&logo=leetcode&logoColor=ffffff&labelColor=16202c" alt="View LeetCode Profile" />
</a>

</div>

<!-- ================================================================= -->
<!--                        END OF PORTFOLIO                           -->
<!-- ================================================================= -->
