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

[![GitHub](https://img.shields.io/badge/GitHub-Diyan4444-ef4444?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=171922)](https://github.com/Diyan4444)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diyan_Shah-f97316?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=171922)](https://www.linkedin.com/in/diyan-shah-14b4993a9/)
[![LeetCode](https://img.shields.io/badge/LeetCode-diddy4-ff6b35?style=for-the-badge&logo=leetcode&logoColor=ffffff&labelColor=171922)](https://leetcode.com/u/diddy4/)
[![Email](https://img.shields.io/badge/Email-diyanshah2301%40gmail.com-ff3355?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=171922)](mailto:diyanshah2301@gmail.com)

</div>

<br>

---

## ⚡ About Me

I'm **Diyan Shah**, an **Information Technology Sophomore at VJTI Mumbai (Veermata Jijabai Technological Institute)**. 

I love engineering software by building real systems from the ground up. Instead of just following tutorials, I learn by shipping: from full-stack platforms and production Chrome extensions (Manifest V3) to multi-model LLM debate engines, satellite radar geospatial pipelines, and 2D games in Godot.

```text
  [ Core Stack ]   C++ • Python • Next.js • Node.js • Godot • Docker • MongoDB • TypeScript 
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



---

## 🎛️ Developer Console HUD

<div align="center">
  <img src="assets/profile-matrix.svg" width="100%" alt="Diyan Shah Identity & Telemetry HUD Matrix" />
</div>

---

## 🚀 Featured Projects

A closer look at some of the primary projects I've built, how they work under the hood, and the problems they solve.

<br>

### 1. 🛰️ OceanGuard AI — SAR Satellite Oil Spill & AIS Vessel Attribution
> **Repository:** [`Diyan4444/OceanGuard`](https://github.com/Diyan4444/OceanGuard) • Built for Smart India Hackathon 2026 (Problem SIH26143)

* **Problem Solved:** Identifying illegal marine oil dumping from space, accounting for ocean surface drift, and legally holding responsible maritime vessels accountable.
* **Architecture & Capabilities:**
  * **SAR Satellite Segmentation:** Extracts dark slicks from Synthetic Aperture Radar (SAR) imagery via computer vision segmentation models.
  * **Hydrodynamic Drift Hindcasting:** Simulates ocean currents and wind vectors backward in time to calculate the exact spill origin coordinates.
  * **AIS Telemetry Cross-Referencing:** Cross-references global AIS vessel tracks with the calculated origin coordinates and timestamps.
  * **Suspect Anomaly Scoring:** Evaluates candidate ships on proximity, speed anomalies, and deliberate AIS transmitter blackouts.
* **Stack:** `Python` • `FastAPI` • `NumPy` • `SciPy` • `React 19` • `Vite` • `Leaflet` • `CartoDB Dark Tiles` • `SQLite`

---

### 2. ⚔️ Rune-Striker — 2D Retro Action-Platformer
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

### 3. 🎬 YouTube Converter (`yt-to-mp4`) — Media Transcoding Service
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
        <li><b>AI/ML</b></li>
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
  <img src="https://github-readme-stats.vercel.app/api?username=Diyan4444&show_icons=true&theme=radical&bg_color=0a0b0e&border_color=331c22&title_color=ff3355&text_color=cbd5e1&icon_color=ff6b35&hide_border=false" width="48%" alt="Diyan's GitHub Stats" />
  &nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Diyan4444&layout=compact&theme=radical&bg_color=0a0b0e&border_color=331c22&title_color=ff3355&text_color=cbd5e1&icon_color=ff6b35&hide_border=false" width="48%" alt="Top Languages Used" />
</div>

<br>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=Diyan4444&theme=radical&background=0a0b0e&border=331c22&stroke=ff3355&ring=ff6b35&fire=ff3355&currStreakLabel=ff6b35" width="97%" alt="Contribution Streak" />
</div>

<br>

---

## 🟩 Contribution Calendar

A visual calendar of my GitHub contributions over the past year:

<div align="center">
  <img src="assets/github-contribution-grid-snake.svg" width="100%" alt="Diyan Shah Contribution Snake Animation" />
</div>

---

## 🧭 My Journey & What's Next

* **Where I've spent time:** Building complete products from start to finish—salon booking platforms, browser extensions, 2D game mechanics, and media processing tools.
* **What I'm exploring now:** AI/ML, computer vision with OpenCV, and scalable backend design.
* **What I want to build:** High-throughput distributed systems and developer tools that make developers' lives easier.

---

## 📬 Get in Touch

<div align="center">

<a href="mailto:diyanshah2301@gmail.com">
  <img src="https://img.shields.io/badge/Email-diyanshah2301%40gmail.com-ff3355?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=171922" alt="Send Email" />
</a>
&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/diyan-shah-14b4993a9/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Connect%20with%20Diyan-f97316?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=171922" alt="Connect on LinkedIn" />
</a>
&nbsp;&nbsp;
<a href="https://github.com/Diyan4444" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-Follow%20%40Diyan4444-ef4444?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=171922" alt="Follow on GitHub" />
</a>
&nbsp;&nbsp;
<a href="https://leetcode.com/u/diddy4/" target="_blank">
  <img src="https://img.shields.io/badge/LeetCode-diddy4-ff6b35?style=for-the-badge&logo=leetcode&logoColor=ffffff&labelColor=171922" alt="View LeetCode Profile" />
</a>

</div>

<!-- ================================================================= -->
<!--                        END OF PORTFOLIO                           -->
<!-- ================================================================= -->
