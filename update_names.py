import re

with open('index.html.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title
content = re.sub(r'<title>.*?</title>', '<title>ParadoxAI Lab | Paradox AIS</title>', content)

# Update Brand in Nav
content = re.sub(r'<a class="brand" href="#top">ParadoxAIS</a>', '<a class="brand" href="#top">ParadoxAI Lab</a>', content)

# Update Footer
content = re.sub(r'<span>PARADOX LAB // 2026</span>', '<span>ParadoxAI Lab // 2026</span>', content)

# Update the Problem Statement section to be a more complete Platform Intro
intro_replacement = """    <!-- THE PLATFORM INTRO -->
    <section id="overview" class="statement" style="padding: 160px 0; border-bottom: 1px solid var(--line); text-align: center;">
      <div class="container">
        <div style="font-family: var(--mono); font-size: 14px; letter-spacing: 0.2em; color: var(--accent); margin-bottom: 32px; text-transform: uppercase;">A ParadoxAI Lab Platform</div>
        <h2 style="font-size: clamp(32px, 5vw, 64px); font-weight: 400; line-height: 1.2; max-width: 1100px; margin: 0 auto;">
          Most intelligence platforms tell you what is happening. <br>
          <span style="color: var(--muted);">Paradox AIS tells you what will happen next.</span>
        </h2>
        <p style="color: var(--muted); font-size: 22px; max-width: 800px; margin: 40px auto 0; line-height: 1.6; font-weight: 300;">
          Designed by ParadoxAI Lab, Paradox AIS is the first commercially available operating system capable of executing autonomous causal simulations for defense and global enterprise.
        </p>
      </div>
    </section>"""

content = re.sub(r'<!-- THE PROBLEM STATEMENT -->.*?</section>', intro_replacement, content, flags=re.DOTALL)

with open('index.html.html', 'w', encoding='utf-8') as f:
    f.write(content)
