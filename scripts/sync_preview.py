from pathlib import Path

p = Path("preview/index.html")
text = p.read_text(encoding="utf-8")

old_p3_head = "<!-- 3. AI Debate Arena -->"
old_p3_tail = "</article>"

# Let's find index of AI Debate Arena
idx3 = text.find(old_p3_head)
idx3_end = text.find(old_p3_tail, idx3) + len(old_p3_tail)

new_p3 = """<!-- 3. RentWheels -->
        <article class="project-card viewport-reveal">
          <div class="project-header">
            <div>
              <h3 class="project-name">RentWheels — Multi-Category Vehicle Rental Marketplace</h3>
            </div>
            <a href="https://github.com/Diyan4444/RentWheels" target="_blank" class="project-repo-link">View Repo &#8599;</a>
          </div>
          <p class="project-desc">
            Multi-tier vehicle rental marketplace platform bringing multiple vehicle categories together in one unified interface. Features dynamic category filtering across bikes, scooters, sedans, electric trucks, and passenger buses, with an interactive reservation cart and responsive dark UI.
          </p>
          <div class="tech-tags">
            <span class="tech-tag">JavaScript (ES6+)</span>
            <span class="tech-tag">HTML5</span>
            <span class="tech-tag">CSS3</span>
            <span class="tech-tag">Responsive UI</span>
            <span class="tech-tag">Netlify</span>
          </div>
        </article>"""

text = text[:idx3] + new_p3 + text[idx3_end:]

old_p5_head = "<!-- 5. Rune-Striker -->"
idx5 = text.find(old_p5_head)
idx5_end = text.find(old_p3_tail, idx5) + len(old_p3_tail)

# Also update project 5 (YouTube Converter) number to 5 if needed, and add Well-Whisperer as 6
old_yt = "<!-- 6. YouTube Converter -->"
new_yt = "<!-- 5. YouTube Converter -->"
text = text.replace(old_yt, new_yt)

new_p6 = """<!-- 6. Well-Whisperer -->
        <article class="project-card viewport-reveal">
          <div class="project-header">
            <div>
              <h3 class="project-name">Well-Whisperer — Predictive Well Telemetry &amp; Oilfield Analytics</h3>
            </div>
            <a href="https://github.com/Diyan4444/Well-Whisperer" target="_blank" class="project-repo-link">View Repo &#8599;</a>
          </div>
          <p class="project-desc">
            Predictive well telemetry and benchmarking platform engineered for Smart India Hackathon 2026 (PS 121 — Oil India Limited). Features live sensor anomaly monitoring, threshold-based predictive maintenance alerts, and automated synthetic benchmark comparison.
          </p>
          <div class="tech-tags">
            <span class="tech-tag">React 19</span>
            <span class="tech-tag">TypeScript</span>
            <span class="tech-tag">FastAPI (Python 3.12)</span>
            <span class="tech-tag">Supabase (PostgreSQL)</span>
            <span class="tech-tag">Vite</span>
          </div>
        </article>"""

text = text[:idx5] + text[idx5_end:]

# Now place new_p6 after YouTube converter
yt_end = text.find("</article>", text.find("<!-- 5. YouTube Converter -->")) + len("</article>")
text = text[:yt_end] + "\n\n        " + new_p6 + text[yt_end:]

p.write_text(text, encoding="utf-8")
print("Successfully synced preview/index.html with the 6 permitted projects!")
