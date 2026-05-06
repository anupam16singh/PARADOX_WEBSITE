import re

with open('index.html.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the <head> section (which contains the new CSS) from index.html.html
head_match = re.search(r'<head>.*?</head>', index_content, re.DOTALL)
new_head = head_match.group(0)

# The HTML for documentation.html styled like Gotham
html_content = f"""<!DOCTYPE html>
<html lang="en">
{new_head}
<body>

  <nav class="nav">
    <div class="container nav-inner">
      <a class="brand" href="index.html.html">ParadoxAI Lab</a>
      <div class="nav-links">
        <a href="index.html.html#overview">Overview</a>
        <a href="index.html.html#how-it-works">Architecture</a>
        <a href="paradox-explained.html">Explained</a>
        <a href="documentation.html" style="color: var(--text);">Docs & Cases</a>
      </div>
    </div>
  </nav>

  <main id="top" style="padding-top: 100px;">
    <!-- HERO / METRICS -->
    <section class="hero" style="height: auto; min-height: 60vh; padding-bottom: 60px; background: none;">
      <div class="container hero-content" style="max-width: 1200px; text-align: left; padding: 0;">
        <div class="k-mono" style="color: var(--accent); margin-bottom: 24px;">System Validation / v4 Engine</div>
        <h1 style="font-size: clamp(48px, 6vw, 90px); text-align: left; margin-bottom: 24px;">Verified Precision.</h1>
        <p style="max-width: 800px; margin: 0; text-align: left; font-size: 22px;">Operating beyond heuristic bias. The Paradox AIS v4 engine utilizes over 1,000+ Monte Carlo simulations to calculate causal outcomes with rigorous accuracy.</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1px; background: var(--line-strong); border: 1px solid var(--line-strong); margin-top: 64px;">
          <div style="background: var(--surface); padding: 40px;">
            <div class="k-mono">Validation Accuracy</div>
            <div style="font-size: 56px; font-weight: 300; color: var(--accent); line-height: 1; margin-bottom: 16px;">75.73%</div>
            <p style="color: var(--muted); font-size: 15px; margin: 0;">Overall accuracy across 103 historical geopolitical event nodes.</p>
          </div>
          <div style="background: var(--surface); padding: 40px;">
            <div class="k-mono">Scenario Matches</div>
            <div style="font-size: 56px; font-weight: 300; color: #fff; line-height: 1; margin-bottom: 16px;">78 / 103</div>
            <p style="color: var(--muted); font-size: 15px; margin: 0;">Correctly predicted escalation vs. de-escalation actions.</p>
          </div>
          <div style="background: var(--surface); padding: 40px;">
            <div class="k-mono">Avg Confidence</div>
            <div style="font-size: 56px; font-weight: 300; color: #fff; line-height: 1; margin-bottom: 16px;">78.0%</div>
            <p style="color: var(--muted); font-size: 15px; margin: 0;">Stable average model confidence across full backtest.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CASE STUDIES -->
    <section id="case-studies" style="padding: 100px 0; border-top: 1px solid var(--line);">
      <div class="container">
        <div class="k-mono" style="color: var(--accent); margin-bottom: 24px;">Case Studies</div>
        <h2 style="font-size: 48px; font-weight: 400; margin-bottom: 60px;">Historical & Active Modeling.</h2>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1px; background: var(--line-strong); border: 1px solid var(--line-strong);">
          
          <article style="background: var(--surface); padding: 40px; display: flex; flex-direction: column;">
            <div class="k-mono" style="color: var(--muted);">Historical / Aramco Attack (2019)</div>
            <h3 style="font-size: 28px; font-weight: 500; margin: 24px 0 16px; line-height: 1.2;">Drone Strike on Infrastructure</h3>
            <p style="color: #fff; margin-bottom: 16px; font-size: 15px;"><strong>Context:</strong> Asymmetric strike on global energy infrastructure.</p>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6;"><strong>AIS Value Proposition:</strong> While traditional heuristic systems flagged "High Alert" and assumed retaliatory escalation, ParadoxAIS modeled the impact on supply chains and regional stability, assigning a <strong>78% probability to a neutral (non-escalatory) outcome</strong>. This matched the actual geopolitical response.</p>
            <div style="margin-top: auto; padding-top: 32px; border-top: 1px solid var(--line); font-family: var(--mono); font-size: 12px; color: var(--muted);">
              <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Neutral Probability</span><strong style="color: var(--accent);">78%</strong></div>
              <div style="display: flex; justify-content: space-between;"><span>Validation Status</span><strong style="color: #fff;">MATCH</strong></div>
            </div>
          </article>

          <article style="background: var(--surface); padding: 40px; display: flex; flex-direction: column;">
            <div class="k-mono" style="color: var(--muted);">Retrospective Simulation</div>
            <h3 style="font-size: 28px; font-weight: 500; margin: 24px 0 16px; line-height: 1.2;">The Gulf War (1990-1991)</h3>
            <p style="color: #fff; margin-bottom: 16px; font-size: 15px;"><strong>Context:</strong> Iraqi invasion of Kuwait and subsequent coalition intervention.</p>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6;"><strong>AIS Value Proposition:</strong> In a retrospective modeling, Paradox AIS ingests historical troop buildup data, diplomatic cables, and commodity fluctuations. The <em>Pulse Detection Pipeline</em> successfully identifies the latent signal of invasion intent, generating a high-confidence early warning alert 14 days before kinetic action.</p>
            <div style="margin-top: auto; padding-top: 32px; border-top: 1px solid var(--line); font-family: var(--mono); font-size: 12px; color: var(--muted);">
              <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Armor Mobilization Detection</span><strong style="color: var(--accent);">T-14 Days</strong></div>
              <div style="display: flex; justify-content: space-between;"><span>Coalition Logistics</span><strong style="color: #fff;">Simulated</strong></div>
            </div>
          </article>

          <article style="background: var(--surface); padding: 40px; display: flex; flex-direction: column;">
            <div class="k-mono" style="color: var(--muted);">Active Theater</div>
            <h3 style="font-size: 28px; font-weight: 500; margin: 24px 0 16px; line-height: 1.2;">US-Iran Strategic Escalation</h3>
            <p style="color: #fff; margin-bottom: 16px; font-size: 15px;"><strong>Context:</strong> Asymmetric engagements, Strait of Hormuz maritime security, and proxy network dynamics.</p>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6;"><strong>AIS Value Proposition:</strong> Operating as a forward-looking causal engine, AIS maps the <em>Atlas Graph</em> of regional proxy funding and maritime capabilities. By applying multi-agent utility functions, the system simulates realistic Iranian escalation ladders in response to US policy shifts.</p>
            <div style="margin-top: auto; padding-top: 32px; border-top: 1px solid var(--line); font-family: var(--mono); font-size: 12px; color: var(--muted);">
              <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Strait Chokepoint Risk</span><strong style="color: var(--accent);">Continuous</strong></div>
              <div style="display: flex; justify-content: space-between;"><span>Proxy Escalation Vectors</span><strong style="color: #fff;">Mapped</strong></div>
            </div>
          </article>

        </div>
      </div>
    </section>

    <!-- DOCUMENTATION LINKS -->
    <section id="docs" style="padding: 100px 0 160px; border-top: 1px solid var(--line);">
      <div class="container">
        <div class="k-mono" style="color: var(--accent); margin-bottom: 24px;">Technical Integration</div>
        <h2 style="font-size: 48px; font-weight: 400; margin-bottom: 60px;">System Documentation.</h2>
        
        <div style="display: grid; gap: 16px;">
          <!-- Doc Items -->
          <a href="AIS_Product_Brief.md" target="_blank" style="display: flex; align-items: center; justify-content: space-between; padding: 24px 32px; background: var(--surface); border: 1px solid var(--line-strong); transition: border-color 0.2s;">
            <div>
              <div class="k-mono" style="color: var(--muted);">DOC-BRIEF</div>
              <h3 style="font-size: 20px; font-weight: 400; color: #fff;">AIS Product Brief: The Geopolitical Decision Engine</h3>
            </div>
            <div class="k-mono" style="color: var(--accent);">Markdown</div>
          </a>

          <a href="AIS_System_Review_v4.md" target="_blank" style="display: flex; align-items: center; justify-content: space-between; padding: 24px 32px; background: var(--surface); border: 1px solid var(--line-strong); transition: border-color 0.2s;">
            <div>
              <div class="k-mono" style="color: var(--muted);">DOC-REVIEW</div>
              <h3 style="font-size: 20px; font-weight: 400; color: #fff;">AIS System Review v4</h3>
            </div>
            <div class="k-mono" style="color: var(--accent);">Markdown</div>
          </a>

          <a href="AIS_Whitepaper_v1.pdf" target="_blank" style="display: flex; align-items: center; justify-content: space-between; padding: 24px 32px; background: var(--surface); border: 1px solid var(--line-strong); transition: border-color 0.2s;">
            <div>
              <div class="k-mono" style="color: var(--muted);">DOC-PAPER</div>
              <h3 style="font-size: 20px; font-weight: 400; color: #fff;">Paradox AIS Whitepaper v1</h3>
            </div>
            <div class="k-mono" style="color: var(--accent);">PDF</div>
          </a>

          <a href="AIS_v4_Validation_Report.md" target="_blank" style="display: flex; align-items: center; justify-content: space-between; padding: 24px 32px; background: var(--surface); border: 1px solid var(--line-strong); transition: border-color 0.2s;">
            <div>
              <div class="k-mono" style="color: var(--muted);">DOC-VALIDATION</div>
              <h3 style="font-size: 20px; font-weight: 400; color: #fff;">v4 Batch Validation Report</h3>
            </div>
            <div class="k-mono" style="color: var(--accent);">Markdown</div>
          </a>

          <a href="AIS_v4_validation_dataset.json" target="_blank" style="display: flex; align-items: center; justify-content: space-between; padding: 24px 32px; background: var(--surface); border: 1px solid var(--line-strong); transition: border-color 0.2s;">
            <div>
              <div class="k-mono" style="color: var(--muted);">DATA-JSON</div>
              <h3 style="font-size: 20px; font-weight: 400; color: #fff;">v4 Validation Dataset (103 Nodes)</h3>
            </div>
            <div class="k-mono" style="color: var(--accent);">JSON</div>
          </a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-inner">
      <span>ParadoxAI Lab // 2026</span>
      <div class="footer-links" style="display: flex; gap: 24px;">
        <a href="index.html.html#overview">Overview</a>
        <a href="index.html.html#how-it-works">Architecture</a>
        <a href="paradox-explained.html">Explained</a>
        <a href="documentation.html">Docs & Cases</a>
      </div>
    </div>
  </footer>

</body>
</html>"""

with open('documentation.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
