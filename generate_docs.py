import re

with open('index.html.html', 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
style_content = style_match.group(0) if style_match else '<style></style>'

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ParadoxAI Lab - Documentation & Case Studies</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Serif:wght@400;500&display=swap" rel="stylesheet">
  {style_content}
  <style>
    @media (max-width: 980px) {{
      .hero-grid-stats {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <nav class="nav">
    <div class="container nav-inner">
      <a class="brand" href="index.html.html" aria-label="ParadoxAI Lab home">
        <i class="mark" aria-hidden="true"></i>
        <span>ParadoxAI Lab</span>
      </a>
      <div class="nav-links" aria-label="Primary navigation">
        <a href="index.html.html#capabilities">Capabilities</a>
        <a href="index.html.html#system">AIS</a>
        <a href="documentation.html">Docs & Cases</a>
        <a href="index.html.html#research">Research</a>
      </div>
    </div>
  </nav>

  <main id="top" style="padding-top: 120px;">
    <!-- HERO / METRICS -->
    <section class="hero" style="min-height: auto; padding-bottom: 40px; padding-top: 60px;">
      <div class="container hero-content reveal" style="max-width: 100%;">
        <div class="label">System Validation / v4 Engine</div>
        <h1 style="font-size: clamp(48px, 8vw, 112px);">Verified Precision.</h1>
        <p style="max-width: 800px;">Operating beyond heuristic bias. The Paradox AIS v4 engine utilizes over 1,000+ Monte Carlo simulations to calculate causal outcomes with rigorous accuracy.</p>
        
        <div class="hero-grid-stats case-grid reveal" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 64px;">
          <div class="intel-panel" style="background: rgba(255,255,255,0.015);">
            <div class="k">Validation Accuracy</div>
            <div class="v" style="font-size: 48px; color: var(--amber);">75.73%</div>
            <p>Overall accuracy across 103 historical geopolitical event nodes.</p>
          </div>
          <div class="intel-panel" style="background: rgba(255,255,255,0.015);">
            <div class="k">Scenario Matches</div>
            <div class="v" style="font-size: 48px; color: var(--ink);">78 / 103</div>
            <p>Correctly predicted escalation vs. de-escalation actions.</p>
          </div>
          <div class="intel-panel" style="background: rgba(255,255,255,0.015);">
            <div class="k">Avg Confidence</div>
            <div class="v" style="font-size: 48px; color: var(--ink);">78.0%</div>
            <p>Stable average model confidence across full backtest.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CASE STUDIES -->
    <section id="case-studies" style="padding-top: 60px;">
      <div class="container">
        <div class="section-head reveal">
          <div class="label">Case Studies</div>
          <h2>Historical & Active Modeling.</h2>
        </div>

        <div class="case-grid reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 24px;">
          
          <article class="intel-panel" style="padding: 36px; display: flex; flex-direction: column; background: rgba(255, 255, 255, 0.015);">
            <div class="k">Historical / Aramco Attack (2019)</div>
            <h3 class="v" style="font-size: 32px; margin-block: 18px 24px;">Drone Strike on Infrastructure</h3>
            <p style="margin-top: 0; color: var(--ink);"><strong>Context:</strong> Asymmetric strike on global energy infrastructure.</p>
            <p style="margin-top: 14px;"><strong>AIS Value Proposition:</strong> While traditional heuristic systems flagged "High Alert" and assumed retaliatory escalation, ParadoxAIS modeled the impact on supply chains and regional stability, assigning a <strong>78% probability to a neutral (non-escalatory) outcome</strong>. This matched the actual geopolitical response.</p>
            <div class="signal-list" style="margin-top: auto; padding-top: 32px;">
              <div><span>Neutral Outcome Probability</span><strong style="color: var(--amber);">78%</strong></div>
              <div><span>Validation Status</span><strong>? MATCH</strong></div>
            </div>
          </article>

          <article class="intel-panel" style="padding: 36px; display: flex; flex-direction: column; background: rgba(255, 255, 255, 0.015);">
            <div class="k">Retrospective Simulation</div>
            <h3 class="v" style="font-size: 32px; margin-block: 18px 24px;">The Gulf War (1990-1991)</h3>
            <p style="margin-top: 0; color: var(--ink);"><strong>Context:</strong> Iraqi invasion of Kuwait and subsequent coalition intervention.</p>
            <p style="margin-top: 14px;"><strong>AIS Value Proposition:</strong> In a retrospective modeling of the 1990 theater, Paradox AIS ingests historical troop buildup data, diplomatic cables, and commodity fluctuations. The <em>Pulse Detection Pipeline</em> successfully identifies the latent signal of invasion intent, generating a high-confidence early warning alert 14 days before kinetic action.</p>
            <div class="signal-list" style="margin-top: auto; padding-top: 32px;">
              <div><span>Armor Mobilization Detection</span><strong style="color: var(--amber);">T-14 Days</strong></div>
              <div><span>Coalition Logistics</span><strong>Simulated</strong></div>
            </div>
          </article>

          <article class="intel-panel" style="padding: 36px; display: flex; flex-direction: column; background: rgba(255, 255, 255, 0.015);">
            <div class="k">Active Theater</div>
            <h3 class="v" style="font-size: 32px; margin-block: 18px 24px;">US-Iran Strategic Escalation</h3>
            <p style="margin-top: 0; color: var(--ink);"><strong>Context:</strong> Asymmetric engagements, Strait of Hormuz maritime security, and proxy network dynamics.</p>
            <p style="margin-top: 14px;"><strong>AIS Value Proposition:</strong> Operating as a forward-looking causal engine, AIS maps the <em>Atlas Graph</em> of regional proxy funding and asymmetric maritime capabilities. By applying multi-agent utility functions, the system simulates realistic Iranian escalation ladders in response to US policy shifts.</p>
            <div class="signal-list" style="margin-top: auto; padding-top: 32px;">
              <div><span>Strait Chokepoint Risk</span><strong style="color: var(--amber);">Continuous</strong></div>
              <div><span>Proxy Escalation Vectors</span><strong>Mapped</strong></div>
            </div>
          </article>

        </div>
      </div>
    </section>

    <!-- DOCUMENTATION LINKS -->
    <section id="docs" style="padding-top: 80px; padding-bottom: 120px;">
      <div class="container">
        <div class="section-head reveal" style="margin-bottom: 42px;">
          <div class="label">Technical Integration</div>
          <h3 style="font-family: var(--serif); font-size: 36px; margin-top: 12px; font-weight: 400; letter-spacing: -0.02em;">System Documentation</h3>
        </div>
        <div class="papers-list reveal">
          <a class="paper" href="AIS_Product_Brief.md" target="_blank">
            <span class="meta">DOC-BRIEF</span>
            <h3>AIS Product Brief: The Geopolitical Decision Engine</h3>
            <span class="type">Markdown</span>
          </a>
          <a class="paper" href="AIS_System_Review_v4.md" target="_blank">
            <span class="meta">DOC-REVIEW</span>
            <h3>AIS System Review v4</h3>
            <span class="type">Markdown</span>
          </a>
          <a class="paper" href="AIS_Whitepaper_v1.pdf" target="_blank">
            <span class="meta">DOC-PAPER</span>
            <h3>Paradox AIS Whitepaper v1</h3>
            <span class="type">PDF</span>
          </a>
          <a class="paper" href="AIS_v4_Validation_Report.md" target="_blank">
            <span class="meta">DOC-VALIDATION</span>
            <h3>v4 Batch Validation Report</h3>
            <span class="type">Markdown</span>
          </a>
          <a class="paper" href="AIS_v4_validation_dataset.json" target="_blank">
            <span class="meta">DATA-JSON</span>
            <h3>v4 Validation Dataset (103 Nodes)</h3>
            <span class="type">JSON</span>
          </a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-inner">
      <span>ParadoxAI Lab / AIS</span>
      <div class="footer-links">
        <a href="index.html.html#capabilities">Capabilities</a>
        <a href="index.html.html#system">System</a>
        <a href="documentation.html">Docs & Cases</a>
      </div>
    </div>
  </footer>

  <script>
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }}
      }});
    }}, {{ threshold: 0.16 }});

    document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
  </script>
</body>
</html>'''

with open('documentation.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("documentation.html created successfully.")
