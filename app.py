import streamlit as st

st.set_page_config(
    page_title="Lalam Pavan Kumar | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Syne', sans-serif; background-color: #0a0a0f; color: #e8e6f0; }
.stApp { background: #0a0a0f; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

.hero {
    min-height: 100vh; display: flex; flex-direction: column;
    justify-content: center; align-items: flex-start;
    padding: 6rem 8vw 4rem; position: relative; overflow: hidden;
}
.hero::before {
    content: ""; position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 70% 40%, rgba(99,60,255,0.18) 0%, transparent 65%),
        radial-gradient(ellipse 50% 40% at 10% 80%, rgba(0,200,180,0.10) 0%, transparent 60%);
    pointer-events: none;
}
.hero-tag {
    font-family: 'Space Mono', monospace; font-size: 0.78rem; letter-spacing: 0.22em;
    color: #7b5ef8; text-transform: uppercase; margin-bottom: 1.4rem;
    border: 1px solid rgba(123,94,248,0.35); display: inline-block;
    padding: 0.3rem 0.9rem; border-radius: 2px;
}
.hero-name {
    font-size: clamp(3rem, 7vw, 6rem); font-weight: 800; line-height: 1.02;
    letter-spacing: -0.03em; margin-bottom: 0.4rem;
    background: linear-gradient(135deg, #ffffff 30%, #a78bfa 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-role { font-size: clamp(1.1rem, 2.5vw, 1.6rem); font-weight: 600; color: #00c4b0; margin-bottom: 1.6rem; letter-spacing: 0.04em; }
.hero-summary { max-width: 640px; font-size: 1.05rem; color: #b0adc8; line-height: 1.75; margin-bottom: 2.4rem; }
.hero-links { display: flex; gap: 1rem; flex-wrap: wrap; }
.hero-btn {
    font-family: 'Space Mono', monospace; font-size: 0.8rem;
    padding: 0.65rem 1.4rem; border-radius: 3px; text-decoration: none !important;
    letter-spacing: 0.08em; display: inline-block;
}
.hero-btn.primary { background: #7b5ef8; color: #fff !important; border: 1px solid #7b5ef8; }
.hero-btn.secondary { background: transparent; color: #e8e6f0 !important; border: 1px solid rgba(232,230,240,0.3); }

.section { padding: 5rem 8vw; border-top: 1px solid rgba(255,255,255,0.06); }
.section-label { font-family: 'Space Mono', monospace; font-size: 0.72rem; letter-spacing: 0.25em; color: #7b5ef8; text-transform: uppercase; margin-bottom: 0.5rem; }
.section-title { font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 800; letter-spacing: -0.02em; margin-bottom: 2.8rem; line-height: 1.1; }

.card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px; padding: 1.8rem; margin-bottom: 1.2rem;
    position: relative; overflow: hidden;
}
.card::before {
    content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #7b5ef8, #00c4b0);
}
.card-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.4rem; color: #fff; }
.card-sub { font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #7b5ef8; margin-bottom: 0.8rem; letter-spacing: 0.05em; }
.card-body { font-size: 0.93rem; color: #b0adc8; line-height: 1.65; }

.skill-grid { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.4rem; }
.pill { font-family: 'Space Mono', monospace; font-size: 0.72rem; padding: 0.35rem 0.85rem; border-radius: 100px; letter-spacing: 0.06em; border: 1px solid; }
.pill.tech   { background: rgba(123,94,248,0.12); color: #a78bfa; border-color: rgba(123,94,248,0.35); }
.pill.lang   { background: rgba(0,196,176,0.10); color: #2dd4bf; border-color: rgba(0,196,176,0.3); }
.pill.tool   { background: rgba(244,164,44,0.10); color: #fbbf24; border-color: rgba(244,164,44,0.3); }
.pill.soft   { background: rgba(236,72,153,0.10); color: #f472b6; border-color: rgba(236,72,153,0.3); }

.pub { padding: 1.4rem 1.8rem; border-left: 3px solid #7b5ef8; background: rgba(123,94,248,0.06); border-radius: 0 6px 6px 0; margin-bottom: 1rem; }
.pub-title { font-size: 0.95rem; font-weight: 600; color: #e8e6f0; margin-bottom: 0.4rem; }
.pub-meta  { font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #7b5ef8; }

.stat-strip { display:flex; gap:2rem; flex-wrap:wrap; margin-bottom:3rem; }
.stat-num { font-size:2.4rem; font-weight:800; color:#7b5ef8; line-height:1; }
.stat-lbl { font-family:'Space Mono',monospace; font-size:0.7rem; letter-spacing:0.12em; color:#6b6890; text-transform:uppercase; margin-top:0.2rem; }

.contact-grid { display: flex; gap: 1rem; flex-wrap: wrap; }
.contact-item { flex: 1; min-width: 220px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 1.4rem 1.8rem; text-decoration: none !important; display: block; }
.contact-label { font-family:'Space Mono',monospace; font-size:0.65rem; letter-spacing:0.2em; color:#7b5ef8; text-transform:uppercase; margin-bottom:0.3rem; }
.contact-value { font-size:0.95rem; color:#e8e6f0; font-weight:600; }

.footer { padding: 2rem 8vw; border-top: 1px solid rgba(255,255,255,0.06); font-family: 'Space Mono', monospace; font-size: 0.72rem; color: #4a4768; text-align: center; }

.nav { position: fixed; top: 0; left: 0; right: 0; z-index: 999; display: flex; align-items: center; justify-content: space-between; padding: 1.1rem 8vw; background: rgba(10,10,15,0.82); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(255,255,255,0.06); }
.nav-logo { font-weight:800; letter-spacing:-0.02em; font-size:1.05rem; }
.nav-links { display:flex; gap:1.8rem; }
.nav-link { font-family:'Space Mono',monospace; font-size:0.72rem; color:#b0adc8; text-decoration:none; letter-spacing:0.1em; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<nav class="nav">
  <div class="nav-logo">LPK<span style="color:#7b5ef8;">.</span></div>
  <div class="nav-links">
    <a class="nav-link" href="#about">ABOUT</a>
    <a class="nav-link" href="#skills">SKILLS</a>
    <a class="nav-link" href="#projects">PROJECTS</a>
    <a class="nav-link" href="#publications">PUBLICATIONS</a>
    <a class="nav-link" href="#contact">CONTACT</a>
  </div>
</nav>

<section class="hero" id="about">
  <div class="hero-tag">⚡ ECE Engineer &amp; Researcher</div>
  <h1 class="hero-name">Lalam Pavan<br>Kumar</h1>
  <div class="hero-role">Embedded Systems · IoT · AI/ML · Wireless Comms</div>
  <p class="hero-summary">
    Motivated Electronics &amp; Communication Engineering student building hardware-software
    integrated solutions for real-time monitoring, automation, and intelligent energy management.
    Published researcher with 5 IEEE &amp; Elsevier papers.
  </p>
  <div class="hero-links">
    <a class="hero-btn primary"  href="https://github.com/LalamPavanKumar" target="_blank">GitHub</a>
    <a class="hero-btn secondary" href="https://linkedin.com/in/LalamPavanKumar" target="_blank">LinkedIn</a>
    <a class="hero-btn secondary" href="mailto:lalampavan6@gmail.com">Email Me</a>
  </div>
</section>

<div class="section">
  <div class="stat-strip">
    <div class="stat"><div class="stat-num">8.39</div><div class="stat-lbl">CGPA / 10</div></div>
    <div class="stat"><div class="stat-num">5</div><div class="stat-lbl">IEEE &amp; Elsevier Papers</div></div>
    <div class="stat"><div class="stat-num">5+</div><div class="stat-lbl">IoT / ML Projects</div></div>
    <div class="stat"><div class="stat-num">95.2%</div><div class="stat-lbl">Intermediate Score</div></div>
  </div>
</div>

<div class="section" id="education">
  <div class="section-label">01 / Education</div>
  <h2 class="section-title">Academic Background</h2>
  <div class="card">
    <div class="card-title">B.Tech — Electronics and Communication Engineering</div>
    <div class="card-sub">Amrita Vishwa Vidyapeetham, Chennai &nbsp;·&nbsp; 2023 – Present &nbsp;·&nbsp; CGPA: 8.39/10</div>
    <div class="card-body">Focused on embedded systems, wireless communication, VLSI design, and intelligent IoT applications.</div>
  </div>
  <div class="card">
    <div class="card-title">Intermediate (M.P.C)</div>
    <div class="card-sub">Dalton Junior College, Visakhapatnam &nbsp;·&nbsp; 2021 – 2023 &nbsp;·&nbsp; 95.2%</div>
    <div class="card-body">Mathematics, Physics, Chemistry — built the analytical foundation for engineering.</div>
  </div>
  <div class="card">
    <div class="card-title">CBSE Secondary Education</div>
    <div class="card-sub">Narayana High School, Visakhapatnam &nbsp;·&nbsp; 2021 &nbsp;·&nbsp; 63.4%</div>
  </div>
</div>

<div class="section" id="skills">
  <div class="section-label">02 / Skills</div>
  <h2 class="section-title">Technical Arsenal</h2>
  <p style="font-family:'Space Mono',monospace;font-size:0.72rem;letter-spacing:0.15em;color:#7b5ef8;text-transform:uppercase;margin-bottom:0.6rem;">Technical</p>
  <div class="skill-grid">
    <span class="pill tech">IoT Systems</span><span class="pill tech">Embedded Systems</span>
    <span class="pill tech">Energy Management</span><span class="pill tech">UAV Networks</span>
    <span class="pill tech">Audio Visualization</span><span class="pill tech">AI &amp; ML</span>
  </div>
  <p style="font-family:'Space Mono',monospace;font-size:0.72rem;letter-spacing:0.15em;color:#00c4b0;text-transform:uppercase;margin-bottom:0.6rem;">Programming</p>
  <div class="skill-grid">
    <span class="pill lang">Python</span><span class="pill lang">MATLAB</span><span class="pill lang">C</span>
  </div>
  <p style="font-family:'Space Mono',monospace;font-size:0.72rem;letter-spacing:0.15em;color:#fbbf24;text-transform:uppercase;margin-bottom:0.6rem;">Software Tools</p>
  <div class="skill-grid">
    <span class="pill tool">Arduino IDE</span><span class="pill tool">MATLAB</span>
    <span class="pill tool">Keil</span><span class="pill tool">Vivado</span>
  </div>
  <p style="font-family:'Space Mono',monospace;font-size:0.72rem;letter-spacing:0.15em;color:#f472b6;text-transform:uppercase;margin-bottom:0.6rem;">Professional</p>
  <div class="skill-grid">
    <span class="pill soft">Project Management</span><span class="pill soft">Leadership</span>
    <span class="pill soft">Critical Thinking</span><span class="pill soft">Communication</span>
    <span class="pill soft">Time Management</span>
  </div>
</div>

<div class="section" id="experience">
  <div class="section-label">03 / Experience</div>
  <h2 class="section-title">Work Experience</h2>
  <div class="card">
    <div class="card-title">Machine Learning Intern</div>
    <div class="card-sub">ShadowFox &nbsp;·&nbsp; July 2025</div>
    <div class="card-body">
      Developed ML models for housing price prediction and loan approval using Scikit-learn and XGBoost.
      Implemented BERT-based NLP pipeline for sentiment analysis.
    </div>
  </div>
</div>

<div class="section" id="projects">
  <div class="section-label">04 / Projects</div>
  <h2 class="section-title">Featured Projects</h2>
  <div class="card">
    <div class="card-title">Autonomous Multi-Zone Smart Irrigation System</div>
    <div class="card-sub">FreeRTOS · Multi-Sensor Fusion · Priority Scheduling</div>
    <div class="card-body">Real-time irrigation control with multi-sensor fusion and priority-based task scheduling on FreeRTOS for efficient agricultural water management.</div>
  </div>
  <div class="card">
    <div class="card-title">Smart Anomaly Detection for Li-Ion Battery Packs</div>
    <div class="card-sub">ESP32 · Machine Learning · IoT</div>
    <div class="card-body">ML-powered system deployed on ESP32 to detect anomalies in lithium-ion battery behaviour, enabling proactive maintenance and safety monitoring.</div>
  </div>
  <div class="card">
    <div class="card-title">AI-Powered IoT AC Power Consumption Analysis</div>
    <div class="card-sub">AI · IoT · Energy Prediction</div>
    <div class="card-body">End-to-end IoT system for real-time AC power monitoring and AI-driven consumption prediction to optimize home energy usage.</div>
  </div>
  <div class="card">
    <div class="card-title">Real-Time Alcohol Detection &amp; Engine Immobilization</div>
    <div class="card-sub">GPS · Road Safety · Embedded Systems</div>
    <div class="card-body">Safety-critical embedded system that detects driver alcohol levels and automatically immobilizes the engine, with GPS location logging.</div>
  </div>
  <div class="card">
    <div class="card-title">Interactive Smart Audio Visualizer</div>
    <div class="card-sub">Real-Time DSP · 3D Visualization · Equalization</div>
    <div class="card-body">Real-time audio processing system with dynamic equalization and immersive 3D visualization for interactive sound exploration.</div>
  </div>
</div>

<div class="section" id="publications">
  <div class="section-label">05 / Research</div>
  <h2 class="section-title">Publications</h2>
  <div class="pub">
    <div class="pub-title">Explainable AI Framework Using XGBoost With SHAP and LIME for Multi-Scale Household Energy Forecasting</div>
    <div class="pub-meta">IEEE Access, vol. 13, pp. 149750–149764 · 2025 · DOI: 10.1109/ACCESS.2025.3602673</div>
  </div>
  <div class="pub">
    <div class="pub-title">Performance Analysis of IRS-Equipped UAV NOMA System with Two-Cell Coordination</div>
    <div class="pub-meta">IEEE WAMS 2025, pp. 1–5 · DOI: 10.1109/WAMS64402.2025.11158900</div>
  </div>
  <div class="pub">
    <div class="pub-title">VLSI-Based Multi-Zone Smart Home Controller with FSM-Driven Automation Using Round-Robin Arbitration and Power Optimization</div>
    <div class="pub-meta">IEEE PES GTD Asia 2025, pp. 83–87 · DOI: 10.1109/GTDAsia60461.2025.11313263</div>
  </div>
  <div class="pub">
    <div class="pub-title">Explainable AI-Enhanced Energy Forecasting Using LightGBM with SHAP and LIME Interpretability</div>
    <div class="pub-meta">IEEE PES GTD Asia 2025, pp. 369–373 · DOI: 10.1109/GTDAsia60461.2025.11313274</div>
  </div>
  <div class="pub">
    <div class="pub-title">AI-Based Energy Consumption Forecasting in Smart Homes Using Multi-Algorithm Analysis Across Temporal Resolutions</div>
    <div class="pub-meta">Results in Engineering, vol. 29, p. 109272 · 2026 · DOI: 10.1016/j.rineng.2026.109272</div>
  </div>
</div>

<div class="section" id="contact">
  <div class="section-label">06 / Contact</div>
  <h2 class="section-title">Get In Touch</h2>
  <div class="contact-grid">
    <a class="contact-item" href="mailto:lalampavan6@gmail.com">
      <div class="contact-label">Email</div><div class="contact-value">lalampavan6@gmail.com</div>
    </a>
    <a class="contact-item" href="tel:+919000508271">
      <div class="contact-label">Phone</div><div class="contact-value">+91 9000508271</div>
    </a>
    <a class="contact-item" href="https://github.com/LalamPavanKumar" target="_blank">
      <div class="contact-label">GitHub</div><div class="contact-value">LalamPavanKumar</div>
    </a>
    <a class="contact-item" href="https://linkedin.com/in/LalamPavanKumar" target="_blank">
      <div class="contact-label">LinkedIn</div><div class="contact-value">LalamPavanKumar</div>
    </a>
  </div>
</div>

<div class="footer">© 2025 Lalam Pavan Kumar · Built with Streamlit · Chennai, India</div>
""", unsafe_allow_html=True)
