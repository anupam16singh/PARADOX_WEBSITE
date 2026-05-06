import re

with open('index.html.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new software section
software_section = """
    <!-- THE SOFTWARE APPLICATIONS -->
    <section id="software" style="padding: 160px 0; background: var(--surface-2); border-bottom: 1px solid var(--line);">
      <div class="container">
        <div class="k-mono" style="color: var(--accent); margin-bottom: 24px; font-family: var(--mono); font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase;">Core Applications</div>
        <h2 style="font-size: clamp(40px, 4vw, 56px); font-weight: 400; margin-bottom: 64px; max-width: 900px;">The Paradox AIS Software Suite</h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1px; background: var(--line-strong); border: 1px solid var(--line-strong);">
          
          <div style="background: var(--surface); padding: 48px; display: flex; flex-direction: column;">
            <div style="font-family: var(--mono); font-size: 10px; color: var(--faint); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.1em;">App 01</div>
            <h3 style="font-size: 24px; font-weight: 500; margin-bottom: 24px; color: #fff;">Pulse Detection Pipeline</h3>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6; margin-bottom: 40px;">
              The ingestion layer. It continuously pulls from global OSINT, commodity pipelines, and proprietary defense databases. Crucially, it ranks signals by strategic consequence, stripping away the noise that causes defensive bias.
            </p>
            <div style="margin-top: auto; border-top: 1px solid var(--line); padding-top: 24px; color: var(--accent); font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;">Real-Time OSINT Fusion</div>
          </div>

          <div style="background: var(--surface); padding: 48px; display: flex; flex-direction: column;">
            <div style="font-family: var(--mono); font-size: 10px; color: var(--faint); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.1em;">App 02</div>
            <h3 style="font-size: 24px; font-weight: 500; margin-bottom: 24px; color: #fff;">The Atlas Graph</h3>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6; margin-bottom: 40px;">
              A living knowledge base that maps the causal relationships of the world. Rather than just storing objects, Atlas understands how a shift in maritime logistics in the Strait of Hormuz causally affects European energy grids.
            </p>
            <div style="margin-top: auto; border-top: 1px solid var(--line); padding-top: 24px; color: var(--accent); font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;">Causal Knowledge Base</div>
          </div>

          <div style="background: var(--surface); padding: 48px; display: flex; flex-direction: column;">
            <div style="font-family: var(--mono); font-size: 10px; color: var(--faint); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.1em;">App 03</div>
            <h3 style="font-size: 24px; font-weight: 500; margin-bottom: 24px; color: #fff;">v4 Simulation Engine</h3>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6; margin-bottom: 40px;">
              The core differentiator. When a threat triggers, the engine runs 1,000+ Monte Carlo pathways in seconds. It models adversarial utility functions to find realistic futures instead of assuming worst-case scenarios.
            </p>
            <div style="margin-top: auto; border-top: 1px solid var(--line); padding-top: 24px; color: var(--accent); font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;">Monte Carlo Predictor</div>
          </div>

          <div style="background: var(--surface); padding: 48px; display: flex; flex-direction: column;">
            <div style="font-family: var(--mono); font-size: 10px; color: var(--faint); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.1em;">App 04</div>
            <h3 style="font-size: 24px; font-weight: 500; margin-bottom: 24px; color: #fff;">Strategic Briefing</h3>
            <p style="color: var(--muted); font-size: 15px; line-height: 1.6; margin-bottom: 40px;">
              Translating massive computational power into decision clarity. The system generates executive-ready narratives, exact probabilities, and a prioritized action plan scored dynamically by the Reward - Risk * Uncertainty matrix.
            </p>
            <div style="margin-top: auto; border-top: 1px solid var(--line); padding-top: 24px; color: var(--accent); font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;">Executive Output</div>
          </div>

        </div>
      </div>
    </section>
"""

# Insert before the ARCHITECTURE section
content = content.replace('    <!-- ARCHITECTURE & COMPARISON GRID -->', software_section + '\n    <!-- ARCHITECTURE & COMPARISON GRID -->')

with open('index.html.html', 'w', encoding='utf-8') as f:
    f.write(content)
