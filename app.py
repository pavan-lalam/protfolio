import streamlit as st
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="L. Pavan Kumar | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Modern Styling ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 1rem;
        margin-bottom: 2rem;
        color: white;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }
    
    .card {
        background-color: #ffffff;
        border-radius: 1rem;
        padding: 1.25rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        border: 1px solid #eef2f6;
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.1);
    }
    
    .skill-badge {
        background-color: #f0f2f6;
        padding: 0.3rem 0.8rem;
        border-radius: 2rem;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.2rem 0.3rem;
        color: #1e293b;
    }
    
    .pub-item {
        padding: 0.75rem;
        border-left: 4px solid #667eea;
        background-color: #fafcff;
        margin-bottom: 0.75rem;
        border-radius: 0.5rem;
    }
    
    .project-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #1e293b;
    }
    
    .experience-title {
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.2rem;
    }
    
    .institution {
        font-weight: 500;
        color: #475569;
    }
    
    hr {
        margin: 1rem 0;
    }
    
    footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: #64748b;
        font-size: 0.8rem;
        border-top: 1px solid #e2e8f0;
    }
    
    @media (max-width: 768px) {
        .section-title {
            font-size: 1.6rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='margin-bottom:0;'>⚡ L. Pavan Kumar</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:1.2rem; margin-top:-0.5rem;'>Electronics & Communication Engineer | IoT & AI/ML Enthusiast</p>", unsafe_allow_html=True)
        st.markdown("<p>📍 Chennai, India | 📧 pavan.kumar@amrita.edu | 🔗 linkedin.com/in/lpavankumar</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Metrics Row ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📚 Publications", "5")
with col2:
    st.metric("🚀 Projects", "5+")
with col3:
    st.metric("💼 Experience", "1 Internship")
with col4:
    st.metric("🎓 CGPA", "8.39/10")

st.markdown("---")

# --- About & Quick Summary ---
st.markdown('<h2 class="section-title">👋 About Me</h2>', unsafe_allow_html=True)
st.markdown("""
Passionate Electronics and Communication Engineering undergraduate with strong expertise in **Embedded Systems, IoT, and Machine Learning**. 
Proven research record with publications in IEEE Access, Results in Engineering, and top conferences. 
I enjoy building intelligent systems that bridge hardware and software — from FreeRTOS-based automation to explainable AI for energy forecasting.
""")

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
    with st.container():
        st.markdown(f"""
        <div class="card">
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div><strong style="font-size:1.1rem;">{edu['degree']}</strong><br><span class="institution">{edu['institution']}</span></div>
                <div><em>{edu['duration']}</em><br>{edu['score']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Skills Section (with columns) ---
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
    <div class="experience-title">Machine Learning Intern</div>
    <div><strong>ShadowFox</strong> | July 2025</div>
    <ul style="margin-top: 8px; margin-bottom: 0;">
        <li>Developed ML models for housing price & loan approval prediction using Scikit-learn and XGBoost.</li>
        <li>Implemented BERT-based NLP sentiment analysis for customer feedback classification.</li>
        <li>Optimized model hyperparameters achieving 15% improvement in prediction accuracy.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Projects Section (Grid using columns) ---
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
                    <div class="project-title">{proj['title']}</div>
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
        <strong>{pub['title']}</strong><br>
        {pub['authors']} ({pub['year']}). <em>{pub['journal']}</em><br>
        <a href="{doi_link}" target="_blank">DOI: {pub['doi']}</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Contact & Social ---
st.markdown('<h2 class="section-title">📫 Connect with Me</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**✉️ Email**  \npavan.kumar@amrita.edu")
with col2:
    st.markdown("**💼 LinkedIn**  \n[linkedin.com/in/lpavankumar](https://linkedin.com/in/lpavankumar)")
with col3:
    st.markdown("**🐙 GitHub**  \n[github.com/lpavankumar](https://github.com/lpavankumar)")

st.markdown("""
<div style="background-color:#f8fafc; padding:1rem; border-radius:1rem; margin-top:1rem;">
    <p style="margin-bottom:0;">🌟 Open to research collaborations and ML/IoT engineering opportunities. Feel free to reach out!</p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<footer>
    Built with ❤️ using Streamlit | Last updated: April 2026 | Data based on latest resume
</footer>
""", unsafe_allow_html=True)
