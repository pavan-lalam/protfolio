import streamlit as st
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="L. Pavan Kumar | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Modern & Colorful Design ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&display=swap');
    
    /* CSS Variables for easy theming */
    :root {
        --primary: #4f46e5;
        --primary-dark: #4338ca;
        --secondary: #06b6d4;
        --accent: #f97316;
        --bg-light: #f9fafb;
        --card-bg: #ffffff;
        --text-dark: #111827;
        --text-muted: #6b7280;
        --border-radius: 1rem;
    }
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Gradient Header with animation */
    .main-header {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 50%, #f97316 100%);
        border-radius: var(--border-radius);
        margin-bottom: 2.5rem;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);
        animation: fadeInDown 0.6s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main-header h1 {
        font-size: 2.8rem;
        margin-bottom: 0;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 2rem 0 1.2rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--primary);
        display: inline-block;
        color: var(--text-dark);
    }
    
    /* Card styling */
    .card {
        background-color: var(--card-bg);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        box-shadow: 0 4px 6px -2px rgba(0,0,0,0.05), 0 10px 15px -3px rgba(0,0,0,0.1);
        margin-bottom: 1.2rem;
        transition: all 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.02);
        border-color: rgba(79,70,229,0.2);
    }
    
    /* Skill badges */
    .skill-badge {
        background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
        color: var(--primary-dark);
        padding: 0.3rem 1rem;
        border-radius: 2rem;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin: 0.25rem 0.4rem;
        transition: all 0.2s;
    }
    
    .skill-badge:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #c7d2fe 0%, #a5b4fc 100%);
    }
    
    /* Publication item */
    .pub-item {
        padding: 1rem;
        border-left: 4px solid var(--primary);
        background-color: #fefefe;
        margin-bottom: 1rem;
        border-radius: 0.75rem;
        transition: all 0.2s;
    }
    
    .pub-item:hover {
        background-color: #f5f3ff;
        border-left-color: var(--accent);
    }
    
    /* Metrics styling */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%);
        border-radius: 1rem;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
    }
    
    /* Footer */
    footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        color: var(--text-muted);
        font-size: 0.85rem;
        border-top: 1px solid #e5e7eb;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        .section-title {
            font-size: 1.5rem;
        }
        .card {
            padding: 1rem;
        }
    }
    
    /* Custom button style (optional) */
    .stButton button {
        background-color: var(--primary);
        color: white;
        border-radius: 2rem;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton button:hover {
        background-color: var(--primary-dark);
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    st.markdown("""
    <div class="main-header">
        <h1>⚡ L. Pavan Kumar</h1>
        <p>Electronics & Communication Engineer | IoT & AI/ML Researcher</p>
        <p>📍 Chennai, India | 📧 pavan.kumar@amrita.edu | 🔗 linkedin.com/in/lpavankumar</p>
    </div>
    """, unsafe_allow_html=True)

# --- Metrics Row with Colorful Cards ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card">📚 <strong style="font-size:1.8rem;">5</strong><br/>Publications</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card">🚀 <strong style="font-size:1.8rem;">5+</strong><br/>Projects</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card">💼 <strong style="font-size:1.8rem;">1</strong><br/>Internship</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card">🎓 <strong style="font-size:1.8rem;">8.39</strong><br/>CGPA</div>', unsafe_allow_html=True)

st.markdown("---")

# --- About Me ---
st.markdown('<h2 class="section-title">👋 About Me</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    Passionate Electronics and Communication Engineering undergraduate with strong expertise in <strong>Embedded Systems, IoT, and Machine Learning</strong>. 
    Proven research record with publications in <strong>IEEE Access, Results in Engineering</strong>, and top conferences. 
    I enjoy building intelligent systems that bridge hardware and software — from FreeRTOS-based automation to explainable AI for energy forecasting.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Education Section ---
st.markdown('<h2 class="section-title">🎓 Education</h2>', unsafe_allow_html=True)

edu_data = [
    {
        "degree": "B.Tech in Electronics and Communication Engineering",
        "institution": "Amrita Vishwa Vidyapeetham, Chennai",
        "duration": "2023 - Present",
        "score": "CGPA: 8.39/10"
    },
    {
        "degree": "Intermediate (M.P.C)",
        "institution": "Dalton Junior College, Visakhapatnam",
        "duration": "2021 - 2023",
        "score": "Percentage: 95.2%"
    },
    {
        "degree": "CBSE Secondary Education",
        "institution": "Narayana High School, Visakhapatnam",
        "duration": "2021",
        "score": "Percentage: 63.4%"
    }
]

for edu in edu_data:
    st.markdown(f"""
    <div class="card">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; align-items: baseline;">
            <div>
                <strong style="font-size:1.1rem;">{edu['degree']}</strong><br/>
                <span style="color: #4b5563;">{edu['institution']}</span>
            </div>
            <div style="text-align: right;">
                <em>{edu['duration']}</em><br/>
                {edu['score']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Skills Section ---
st.markdown('<h2 class="section-title">🧠 Skills & Tools</h2>', unsafe_allow_html=True)

col_skill1, col_skill2 = st.columns(2)

with col_skill1:
    st.markdown("**💻 Technical & Programming**")
    tech_skills = ["IoT Systems", "Energy Management", "Embedded Systems", "UAV Networks", "Audio Visualization", "AI & ML", "Python", "MATLAB", "C"]
    for skill in tech_skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    st.markdown("")
    st.markdown("**🛠️ Software Tools**")
    tools = ["Arduino IDE", "MATLAB", "Keil", "Vivado", "Scikit-learn", "XGBoost", "BERT"]
    for tool in tools:
        st.markdown(f'<span class="skill-badge">{tool}</span>', unsafe_allow_html=True)

with col_skill2:
    st.markdown("**🚀 Professional & Soft**")
    prof_skills = ["Project Management", "Leadership", "Critical Thinking", "Effective Communication", "Time Management"]
    for ps in prof_skills:
        st.markdown(f'<span class="skill-badge">{ps}</span>', unsafe_allow_html=True)
    st.markdown("")
    st.markdown("**🌐 Languages**")
    langs = ["English (Professional)", "Telugu (Native)"]
    for lang in langs:
        st.markdown(f'<span class="skill-badge">{lang}</span>', unsafe_allow_html=True)

st.markdown("---")

# --- Work Experience ---
st.markdown('<h2 class="section-title">💼 Work Experience</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div style="font-weight:700; font-size:1.2rem;">Machine Learning Intern</div>
    <div style="color: #4b5563; margin-bottom: 8px;">ShadowFox | July 2025</div>
    <ul style="margin-top: 8px; margin-bottom: 0;">
        <li>Developed ML models for housing price & loan approval prediction using Scikit-learn and XGBoost.</li>
        <li>Implemented BERT-based NLP sentiment analysis for customer feedback classification.</li>
        <li>Optimized model hyperparameters achieving 15% improvement in prediction accuracy.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Projects Section ---
st.markdown('<h2 class="section-title">📌 Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "Autonomous Multi-Zone Smart Irrigation System",
        "tech": "FreeRTOS, Sensors, Priority Scheduling",
        "desc": "Multi-sensor fusion (soil moisture, temp, humidity) with priority-based water scheduling on FreeRTOS. Reduced water consumption by 30%."
    },
    {
        "title": "Smart Anomaly Detection for Li-ion Battery Packs",
        "tech": "ESP32, Machine Learning, IoT Analytics",
        "desc": "Real-time monitoring of voltage, current, temperature with ML-based anomaly detection (Isolation Forest) for early fault prediction."
    },
    {
        "title": "AI-Powered IoT AC Power Consumption Analysis",
        "tech": "IoT, LSTM, XGBoost, Cloud Dashboard",
        "desc": "End-to-end system for predicting household AC power consumption with explainable AI (SHAP/LIME) and real-time monitoring."
    },
    {
        "title": "Real-Time Alcohol Detection & Engine Immobilization",
        "tech": "GPS, MQ-3 Sensor, Arduino, Safety System",
        "desc": "Built vehicle safety system that detects alcohol and triggers engine immobilization with GPS location alert."
    },
    {
        "title": "Interactive Smart Audio Visualizer",
        "tech": "DSP, 3D Visualization, Real-time Equalization",
        "desc": "Real-time audio spectrum visualization with 3D effects and frequency equalization using embedded processing."
    }
]

# Display projects in two columns
for i in range(0, len(projects), 2):
    cols = st.columns(2)
    for idx, col in enumerate(cols):
        if i+idx < len(projects):
            proj = projects[i+idx]
            with col:
                st.markdown(f"""
                <div class="card">
                    <div style="font-weight:700; font-size:1.1rem; margin-bottom:0.5rem;">{proj['title']}</div>
                    <div style="font-size:0.8rem; color:#4b5563; margin-bottom:8px;">🔧 {proj['tech']}</div>
                    <p style="margin-bottom:0;">{proj['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")

# --- Publications Section ---
st.markdown('<h2 class="section-title">📄 Publications</h2>', unsafe_allow_html=True)

publications = [
    {
        "authors": "Devanathan, B. et al.",
        "year": "2025",
        "title": "Explainable AI Framework Using XGBoost With SHAP and LIME for Multi-Scale Household Energy Forecasting.",
        "journal": "IEEE Access, vol. 13, pp. 149750-149764",
        "doi": "10.1109/ACCESS.2025.3602673"
    },
    {
        "authors": "Ravishankar, Simhadri et al.",
        "year": "2025",
        "title": "Performance Analysis of IRS-Equipped UAV NOMA System with Two-Cell Coordination.",
        "journal": "2025 IEEE Wireless Antenna and Microwave Symposium (WAMS), pp. 1-5",
        "doi": "10.1109/WAMS64402.2025.11158900"
    },
    {
        "authors": "Varshitha, K. Jnana, L. Pavan Kumar, B. Devanathan, et al.",
        "year": "2025",
        "title": "VLSI-Based Multi-Zone Smart Home Controller with FSM-Driven Automation Using Round-Robin Arbitration and Power Optimization.",
        "journal": "2025 IEEE PES GTD Asia, pp. 83-87",
        "doi": "10.1109/GTDAsia60461.2025.11313263"
    },
    {
        "authors": "Varshitha, K. Jnana, L. Pavan Kumar, Pavan Manellore, et al.",
        "year": "2025",
        "title": "Explainable AI-Enhanced Energy Forecasting Using LightGBM with SHAP and LIME Interpretability.",
        "journal": "2025 IEEE PES GTD Asia, pp. 369-373",
        "doi": "10.1109/GTDAsia60461.2025.11313274"
    },
    {
        "authors": "Devanathan, B. et al.",
        "year": "2026",
        "title": "AI-Based Energy Consumption Forecasting in Smart Homes Using Multi-Algorithm Analysis Across Temporal Resolutions.",
        "journal": "Results in Engineering, vol. 29, p. 109272",
        "doi": "10.1016/j.rineng.2026.109272"
    }
]

for pub in publications:
    doi_link = f"https://doi.org/{pub['doi']}"
    st.markdown(f"""
    <div class="pub-item">
        <strong>{pub['title']}</strong><br/>
        {pub['authors']} ({pub['year']}). <em>{pub['journal']}</em><br/>
        <a href="{doi_link}" target="_blank" style="color: #4f46e5; text-decoration: none;">DOI: {pub['doi']}</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Contact Section ---
st.markdown('<h2 class="section-title">📫 Connect with Me</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        ✉️ **Email**<br/>
        pavan.kumar@amrita.edu
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card" style="text-align:center;">
        💼 **LinkedIn**<br/>
        [linkedin.com/in/lpavankumar](https://linkedin.com/in/lpavankumar)
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        🐙 **GitHub**<br/>
        [github.com/lpavankumar](https://github.com/lpavankumar)
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg, #f3f4f6 0%, #ffffff 100%); padding:1.5rem; border-radius:1rem; margin-top:1rem; text-align:center;">
    🌟 Open to research collaborations and ML/IoT engineering opportunities. Feel free to reach out!
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<footer>
    Built with ❤️ using Streamlit | Last updated: April 2026 | Data based on latest resume
</footer>
""", unsafe_allow_html=True)
