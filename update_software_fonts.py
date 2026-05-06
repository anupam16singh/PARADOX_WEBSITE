import re

with open('index.html.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<h2 style="font-size: clamp(40px, 4vw, 56px); font-weight: 400; margin-bottom: 64px; max-width: 900px;">The Paradox AIS Software Suite</h2>', 
                          '<h2 style="font-family: var(--display); font-size: clamp(40px, 4vw, 56px); font-weight: 500; margin-bottom: 64px; max-width: 900px; letter-spacing: -0.02em;">The Paradox AIS Software Suite</h2>')

content = content.replace('<h3 style="font-size: 24px; font-weight: 500; margin-bottom: 24px; color: #fff;">', 
                          '<h3 style="font-family: var(--display); font-size: 28px; font-weight: 600; margin-bottom: 24px; color: #fff; letter-spacing: -0.01em;">')

with open('index.html.html', 'w', encoding='utf-8') as f:
    f.write(content)
