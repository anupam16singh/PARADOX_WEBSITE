import re

with open('paradox-explained.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title
content = re.sub(r'<title>.*?</title>', '<title>ParadoxAI Lab | Explained</title>', content)

# Update Brand in Nav
content = re.sub(r'<a href="index.html.html">ParadoxAIS</a>', '<a href="index.html.html">ParadoxAI Lab</a>', content)

with open('paradox-explained.html', 'w', encoding='utf-8') as f:
    f.write(content)
