import codecs

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ParadoxAIS | The Geopolitical Decision Engine</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #000000;
      --surface: #0a0a0a;
      --surface-2: #141414;
      --text: #ffffff;
      --muted: #888888;
      --faint: #444444;
      --line: rgba(255, 255, 255, 0.1);
      --line-strong: rgba(255, 255, 255, 0.2);
      --accent: #4ade80; /* A crisp, tactical green/cyan */
      --sans: 'Inter', -apple-system, sans-serif;
      --mono: 'JetBrains Mono', Consolas, monospace;
      --ease: cubic-bezier(.22, 1, .36, 1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html { scroll-behavior: smooth; background: var(--bg); }

    body {
      min-height: 100vh;
      background: var(--bg);
      color: var(--text);
      font-family: var(--sans);
      font-size: 16px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    a { color: inherit; text-decoration: none; }

    .container {
      width: min(1400px, calc(100% - 48px));
      margin-inline: auto;
    }

    /* NAVIGATION */
    .nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 50;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--line);
    }
    .nav-inner {
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand {
      font-weight: 600;
      font-size: 16px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }
    .nav-links {
      display: flex;
      gap: 32px;
      font-size: 13px;
      font-weight: 500;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--muted);
    }
    .nav-links a { transition: color 0.2s; }
    .nav-links a:hover { color: var(--text); }

    /* HERO SECTION with VIDEO BG */
    .hero {
      position: relative;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      overflow: hidden;
    }
    .hero-video-wrapper {
      position: absolute;
      inset: 0;
      z-index: 0;
    }
    .hero-video-wrapper video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.4;
    }
    .hero-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,1) 100%);
      z-index: 1;
    }
    .hero-content {
      position: relative;
      z-index: 2;
      max-width: 900px;
      padding: 0 24px;
    }
    .hero-label {
      font-family: var(--mono);
      font-size: 12px;
      letter-spacing: 0.2em;
      color: var(--muted);
      margin-bottom: 24px;
      display: block;
      text-transform: uppercase;
    }
    .hero h1 {
      font-size: clamp(64px, 8vw, 130px);
      font-weight: 500;
      line-height: 0.9;
      letter-spacing: -0.04em;
      margin-bottom: 32px;
    }
    .hero p {
      font-size: clamp(20px, 2vw, 28px);
      font-weight: 300;
      color: var(--muted);
      max-width: 700px;
      margin: 0 auto;
    }
    .scroll-indicator {
      position: absolute;
      bottom: 40px;
      left: 50%;
      transform: translateX(-50%);
      font-family: var(--mono);
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--muted);
      z-index: 2;
    }

    /* MASSIVE TYPOGRAPHY SECTION */
    .statement {
      padding: 160px 0;
      border-bottom: 1px solid var(--line);
    }
    .statement h2 {
      font-size: clamp(40px, 5vw, 72px);
      font-weight: 400;
      line-height: 1.1;
      letter-spacing: -0.02em;
      max-width: 1100px;
    }
    .statement h2 span {
      color: var(--muted);
    }

    /* STICKY SCROLL SECTION */
    .sticky-story {
      position: relative;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
    }
    .sticky-container {
      display: flex;
      align-items: flex-start;
      max-width: 1400px;
      margin: 0 auto;
    }
    .sticky-visual {
      position: sticky;
      top: 64px;
      width: 50%;
      height: calc(100vh - 64px);
      padding: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .visual-media {
      width: 100%;
      height: 80%;
      object-fit: cover;
      border: 1px solid var(--line-strong);
      /* Add a glowing effect for the system feel */
      box-shadow: 0 0 60px rgba(74, 222, 128, 0.05);
    }
    .sticky-content {
      width: 50%;
      padding: 0 60px 200px;
    }
    .story-step {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .story-step .step-num {
      font-family: var(--mono);
      font-size: 14px;
      color: var(--accent);
      margin-bottom: 24px;
      letter-spacing: 0.1em;
    }
    .story-step h3 {
      font-size: 48px;
      font-weight: 500;
      line-height: 1.1;
      letter-spacing: -0.02em;
      margin-bottom: 24px;
    }
    .story-step p {
      font-size: 22px;
      color: var(--muted);
      font-weight: 300;
      line-height: 1.5;
    }

    /* ARCHITECTURE GRID (From previous iteration but styled for Palantir-vibe) */
    .architecture {
      padding: 160px 0;
      background: var(--bg);
    }
    .arch-header {
      margin-bottom: 80px;
      max-width: 800px;
    }
    .arch-header h2 {
      font-size: clamp(40px, 4vw, 56px);
      font-weight: 500;
      letter-spacing: -0.02em;
      margin-bottom: 24px;
    }
    .arch-grid {
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 1px;
      background: var(--line-strong);
      border: 1px solid var(--line-strong);
    }
    .arch-sidebar {
      background: var(--surface);
      padding: 40px;
    }
    .arch-main {
      background: var(--surface);
      padding: 40px;
      display: flex;
      flex-direction: column;
      gap: 40px;
    }
    .k-mono {
      font-family: var(--mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: var(--muted);
      margin-bottom: 16px;
    }
    .tech-list {
      list-style: none;
      display: grid;
      gap: 12px;
    }
    .tech-list li {
      border: 1px solid var(--line);
      padding: 12px 16px;
      font-family: var(--mono);
      font-size: 12px;
      background: rgba(255,255,255,0.02);
    }
    .vs-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
      margin-top: 24px;
    }
    .vs-table th, .vs-table td {
      padding: 16px;
      text-align: left;
      border-bottom: 1px solid var(--line);
    }
    .vs-table th {
      font-weight: 500;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    /* TERMINAL */
    .terminal {
      background: #000;
      border: 1px solid var(--line-strong);
      padding: 32px;
      font-family: var(--mono);
      font-size: 13px;
      line-height: 1.8;
      color: var(--muted);
    }
    .terminal .prompt { color: var(--accent); }
    .terminal .highlight { color: #fff; font-weight: 500; }

    /* FULL BLEED IMAGE PREVIEW */
    .system-preview {
      padding: 120px 0;
      background: var(--surface-2);
      border-top: 1px solid var(--line);
      text-align: center;
    }
    .preview-wrapper {
      max-width: 1400px;
      margin: 60px auto 0;
      border: 1px solid var(--line-strong);
      box-shadow: 0 40px 100px rgba(0,0,0,0.5);
    }
    .preview-wrapper img {
      width: 100%;
      display: block;
    }

    /* FOOTER */
    .footer {
      padding: 60px 0;
      border-top: 1px solid var(--line);
      font-family: var(--mono);
      font-size: 12px;
      color: var(--muted);
    }
    .footer-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    @media (max-width: 1024px) {
      .sticky-container { flex-direction: column; }
      .sticky-visual {
        position: relative;
        width: 100%;
        height: 60vh;
        top: 0;
        padding: 24px;
      }
      .sticky-content { width: 100%; padding: 40px 24px; }
      .story-step { min-height: auto; padding: 60px 0; }
      .arch-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <nav class="nav">
    <div class="container nav-inner">
      <a class="brand" href="#top">ParadoxAIS</a>
      <div class="nav-links">
        <a href="#overview">Overview</a>
        <a href="#how-it-works">Architecture</a>
        <a href="#comparison">Gotham vs AIS</a>
        <a href="documentation.html">Docs & Cases</a>
      </div>
    </div>
  </nav>

  <main id="top">
    <!-- HERO SECTION -->
    <section class="hero">
      <div class="hero-video-wrapper">
        <!-- Placeholder Video 1 (Full Bleed Background) -->
        <video autoplay muted loop playsinline>
          <source src="https://cdn.pixabay.com/video/2021/08/04/83866-584745814_large.mp4" type="video/mp4">
        </video>
        <div class="hero-overlay"></div>
      </div>
      <div class="hero-content">
        <span class="hero-label">The Geopolitical Decision Engine</span>
        <h1>PARADOX AIS</h1>
        <p>The operating system for autonomous strategic intelligence. Moving beyond data integration into causal simulation.</p>
      </div>
      <div class="scroll-indicator">Scroll to Explore</div>
    </section>

    <!-- THE PROBLEM STATEMENT -->
    <section id="overview" class="statement">
      <div class="container">
        <h2>
          Most intelligence platforms tell you what is happening. <br>
          <span>ParadoxAIS tells you what will happen next.</span>
        </h2>
      </div>
    </section>

    <!-- STICKY SCROLL: HOW IT WORKS -->
    <section id="how-it-works" class="sticky-story">
      <div class="sticky-container">
        
        <div class="sticky-visual">
          <!-- Placeholder Video 2 (System Demo Placeholder) -->
          <!-- NOTE TO USER: Replace the src below with your system demo video -->
          <video autoplay muted loop playsinline class="visual-media" style="background: #000;">
            <source src="https://cdn.pixabay.com/video/2020/05/18/39511-423588721_large.mp4" type="video/mp4">
          </video>
        </div>

        <div class="sticky-content">
          <div class="story-step">
            <div class="step-num">01 // MONITOR</div>
            <h3>Global Signal Ingestion</h3>
            <p>ParadoxAIS observes a global live-feed of geopolitical signals—from natural disasters to troop movements and economic shifts—updated every 45 seconds to ensure operational superiority.</p>
          </div>
          
          <div class="story-step">
            <div class="step-num">02 // TRIGGER</div>
            <h3>Scenario Activation</h3>
            <p>When tension nodes are detected, the system does not wait for a human operator. It instantly initiates thousands of parallel "What-If" scenarios targeting specific regional and economic flashpoints.</p>
          </div>
          
          <div class="story-step">
            <div class="step-num">03 // SIMULATE</div>
            <h3>Monte Carlo Execution</h3>
            <p>Using the v4 Causal Engine and the Atlas Graph knowledge base, Paradox runs 1,000+ simulations in seconds, modeling multi-agent utility functions to eliminate traditional defensive bias.</p>
          </div>

          <div class="story-step">
            <div class="step-num">04 // EXECUTE</div>
            <h3>Decision Supremacy</h3>
            <p>The output is not just an alert. It is a mathematically sound Strategic Briefing providing exact probabilities, causal narratives, and a step-by-step Action Plan based on Reward - Risk * Uncertainty.</p>
          </div>
        </div>

      </div>
    </section>

    <!-- ARCHITECTURE & COMPARISON GRID -->
    <section id="comparison" class="architecture">
      <div class="container">
        <div class="arch-header">
          <div class="k-mono" style="color: var(--accent);">System Architecture</div>
          <h2>Designed for consequence.</h2>
          <p style="color: var(--muted); font-size: 20px;">While legacy systems (like Palantir Gotham) rely on object-relational mapping for human analysts, ParadoxAIS creates a new category of autonomous strategic intelligence.</p>
        </div>

        <div class="arch-grid">
          <!-- SIDEBAR -->
          <div class="arch-sidebar">
            <div class="k-mono">Core Tech Stack</div>
            <ul class="tech-list">
              <li style="border-left: 2px solid var(--accent); color: #fff;">Atlas Graph Knowledge Base</li>
              <li>Causal Engine v4</li>
              <li>Monte Carlo Execution</li>
              <li>Multi-Agent Adversarial Logic</li>
            </ul>
          </div>
          
          <!-- MAIN AREA -->
          <div class="arch-main">
            <div>
              <div class="k-mono">Comparative Architecture</div>
              <table class="vs-table">
                <thead>
                  <tr>
                    <th>Vector</th>
                    <th>Legacy Systems (Gotham)</th>
                    <th style="color: var(--accent);">ParadoxAIS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="color: #fff;">Primary Goal</td>
                    <td>Data Integration & Analysis</td>
                    <td style="color: #fff; font-weight: 500;">Simulation & Decision Support</td>
                  </tr>
                  <tr>
                    <td style="color: #fff;">Output</td>
                    <td>"What is the situation?"</td>
                    <td style="color: #fff; font-weight: 500;">"What happens next?"</td>
                  </tr>
                  <tr>
                    <td style="color: #fff;">Core Tech</td>
                    <td>Object-relational mapping</td>
                    <td style="color: #fff; font-weight: 500;">Monte Carlo + Causal Engine</td>
                  </tr>
                  <tr>
                    <td style="color: #fff;">Decision Bias</td>
                    <td>Relies on human operator</td>
                    <td style="color: #fff; font-weight: 500;">Algorithmic diversity penalty</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- TERMINAL / LOGS -->
            <div class="terminal">
              <div class="k-mono" style="margin-bottom: 12px; color: var(--faint);">v4.Engine.Execution_Log</div>
              <div>
                <span class="prompt">[04:22:18 UTC]</span> > Initializing ParadoxAIS Core... [OK]<br>
                <span class="prompt">[04:22:19 UTC]</span> > Connecting to Atlas Graph... [OK]<br>
                <span class="prompt">[04:22:20 UTC]</span> > <span class="highlight">DETECTED TENSION:</span> Taiwan Strait Node.<br>
                <span class="prompt">[04:22:21 UTC]</span> > Running 1,000+ Monte Carlo pathways...<br>
                <span style="color: var(--faint);">[04:22:23 UTC]</span> > ... calculating multi-agent utility functions ...<br>
                <span class="prompt">[04:22:25 UTC]</span> > <span class="highlight">OUTPUT: 82% PROBABILITY OF ESCALATION.</span><br>
                <span class="prompt">[04:22:25 UTC]</span> > ? Action: [Hedge energy exposure] [Initiate backchannel].
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- FULL SCREEN PREVIEW -->
    <section class="system-preview">
      <div class="container">
        <div class="k-mono">Command Center Interface</div>
        <h2 style="font-size: 40px; margin-top: 16px;">The Operator Dashboard</h2>
        
        <div class="preview-wrapper">
          <!-- User provided Dashboard Image -->
          <img src="system-dashboard.png" alt="Paradox AIS Dashboard Interface">
        </div>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="container footer-inner">
      <span>PARADOX LAB // 2026</span>
      <div class="footer-links" style="display: flex; gap: 24px;">
        <a href="#overview">Overview</a>
        <a href="#how-it-works">Architecture</a>
        <a href="documentation.html">Docs & Cases</a>
      </div>
    </div>
  </footer>

</body>
</html>"""

with codecs.open("index.html.html", "w", "utf-8") as f:
    f.write(html_content)
