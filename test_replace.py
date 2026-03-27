import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace spans without attributes
content = re.sub(r'<span>([↗↓▶✉✈↑])</span>', r'<span aria-hidden="true">\1</span>', content)

# Replace spans with class="btn-icon"
content = re.sub(r'<span class="btn-icon">([↗↓✈])</span>', r'<span class="btn-icon" aria-hidden="true">\1</span>', content)

# Replace span with class="lang-divider"
content = re.sub(r'<span class="lang-divider">\|</span>', r'<span class="lang-divider" aria-hidden="true">|</span>', content)

with open('index.html', 'w') as f:
    f.write(content)
