from pathlib import Path

p = Path("preview/index.html")
text = p.read_text(encoding="utf-8")
t_norm = text.replace("\r\n", "\n")

target = '<img src="../assets/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Grid" />'
replacement = '<img src="../assets/contribution-graph.svg" alt="GitHub Contribution Graph" />\n      </div>\n      <div class="hero-card" style="margin-top: 20px;">\n        <img src="../assets/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Grid" />'

if target in t_norm:
    t_norm = t_norm.replace(target, replacement, 1)
    p.write_text(t_norm, encoding="utf-8")
    print("Updated preview/index.html successfully!")
else:
    print("Target not found in preview/index.html")
