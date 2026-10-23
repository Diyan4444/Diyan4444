from pathlib import Path

p = Path("preview/index.html")
text = p.read_text(encoding="utf-8")
t_norm = text.replace("\r\n", "\n")

target = '<img src="../assets/contribution-graph.svg" alt="Diyan\'s 2-Month GitHub Contribution Graph" />\n      </div>'
replacement = '<img src="../assets/contribution-graph.svg" alt="Diyan\'s 2-Month GitHub Contribution Graph" />\n      </div>\n      <div class="hero-card" style="margin-top: 20px;">\n        <img src="../assets/github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Grid" />\n      </div>'

if target in t_norm:
    t_norm = t_norm.replace(target, replacement, 1)
    p.write_text(t_norm, encoding="utf-8")
    print("Updated preview/index.html with both graph and snake!")
else:
    print("Target not found in preview/index.html")
