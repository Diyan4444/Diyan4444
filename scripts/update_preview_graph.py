from pathlib import Path

p = Path("preview/index.html")
text = p.read_text(encoding="utf-8")
t_norm = text.replace("\r\n", "\n")

old_sec = """    <!-- Contribution Universe -->
    <section id="contributions" style="margin-top: 48px;" class="viewport-reveal">
      <div class="section-tag">ACTIVITY CALENDAR</div>
      <h2 class="section-title">GitHub Contribution Universe</h2>
      <div class="hero-card" style="margin-top: 14px;">
        <img src="../assets/contribution-graph.svg" alt="GitHub Contribution Graph" />
      </div>
      <div class="hero-card" style="margin-top: 20px;">
        <img src="../assets/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Grid" />
      </div>
    </section>"""

new_sec = """    <!-- Contribution Universe -->
    <section id="contributions" style="margin-top: 48px;" class="viewport-reveal">
      <div class="section-tag">ACTIVITY TELEMETRY</div>
      <h2 class="section-title">2-Month Contribution Graph</h2>
      <div class="hero-card" style="margin-top: 14px;">
        <img src="../assets/contribution-graph.svg" alt="Diyan's 2-Month GitHub Contribution Graph" />
      </div>
    </section>"""

if old_sec in t_norm:
    t_norm = t_norm.replace(old_sec, new_sec, 1)
    p.write_text(t_norm, encoding="utf-8")
    print("Updated preview/index.html successfully without snake!")
else:
    print("Could not match old section in preview/index.html")
