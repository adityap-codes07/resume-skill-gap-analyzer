import streamlit as st
from datetime import datetime
import base64
from pathlib import Path

def get_base64_img(img_path):
    img_bytes = Path(img_path).read_bytes()
    return base64.b64encode(img_bytes).decode()

component_dir = Path(__file__).parent.resolve()
project_root = component_dir.parent.parent.resolve()
logo_absolute_path = project_root / "Skill_Bridge_Logo.png"

try:
    logo_base64 = get_base64_img(str(logo_absolute_path))
except FileNotFoundError:
    logo_base64 = None
    st.warning(f"Logo file not found at the constructed path:\n`{logo_absolute_path}`")
    print(f"Error: Could not find image at path: {logo_absolute_path}")


def hero():
    """Display hero section with logo and title"""
    gradient = "linear-gradient(90deg, rgba(99,102,241,0.08), rgba(168,85,247,0.06))"

    logo_html = ""
    if logo_base64:
        logo_html = f'''
<div style="background: {gradient}; border-radius: 50%; padding: 10px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-right: 25px;">
    <img src="data:image/png;base64,{logo_base64}" style="width: 96px; height: auto;">
</div>'''

    st.markdown(
        f"""
<div style="background: {gradient}; padding: 3rem 2rem; border-radius: 14px; text-align:center; margin-bottom:1.5rem;">
    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
        {logo_html}
        <h1 style="margin: 0; font-size: 2.8rem; line-height: 1.2; color: white; text-align: left;">
            ML-Based Resume Analyzer with <br>TF-IDF & Similarity Matching
        </h1>
    </div>
    <p style="max-width: 800px; margin: 0 auto; opacity: 0.8; font-size: 1.1rem; color: #e0e0e0;">
        Advanced ATS simulation with multi-dimensional analysis, real-time skill gap detection, 
        and actionable career insights powered by enterprise-grade NLP algorithms.
    </p>
</div>
""",
        unsafe_allow_html=True
    )

def section_header(title: str, emoji: str):
    st.markdown(
        f"""
        <div style="margin:1.75rem 0 1rem 0; padding:.75rem 1rem;
                    background: rgba(99, 102, 241, 0.10); border-left:4px solid #6366f1; border-radius:8px;">
            <h2 style="color:#e2e8f0; margin:0; font-size:1.25rem; font-weight:600;">{emoji} {title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

def metrics_cards(result):
    fit_color = result["fit_color"]
    final_score = result["final_score"]
    tech_score = result["tech_score"]
    fit_level = result["fit_level"]
    matched_skills = result["matched_skills"]

    st.markdown(
        f"""
        <div class="metrics-grid">
            <div class="metric-card">
                <div style="font-size:2.4rem; font-weight:700; color:{fit_color};">{final_score:.1f}</div>
                <div style="color:var(--muted); font-size:0.9rem; letter-spacing:1px; margin-top:0.25rem;">Overall ATS Score</div>
            </div>
            <div class="metric-card">
                <div style="font-size:2.4rem; font-weight:700; color:#60a5fa;">{tech_score:.1f}%</div>
                <div style="color:var(--muted); font-size:0.9rem; letter-spacing:1px; margin-top:0.25rem;">Technical Match</div>
            </div>
            <div class="metric-card">
                <div style="font-size:1.6rem; font-weight:700; color:{fit_color};">{fit_level}</div>
                <div style="color:var(--muted); font-size:0.9rem; letter-spacing:1px; margin-top:0.25rem;">Candidate Fit</div>
            </div>
            <div class="metric-card">
                <div style="font-size:2.4rem; font-weight:700; color:var(--accent);">{len(matched_skills)}</div>
                <div style="color:var(--muted); font-size:0.9rem; letter-spacing:1px; margin-top:0.25rem;">Skills Matched</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def skills_block(result):
    matched = result["matched_skills"]
    missing = result["missing_skills"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**✅ Matched Skills**")
        if matched:
            st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in matched[:15]]), unsafe_allow_html=True)
        else:
            st.info("No direct skill matches detected.")

    with col2:
        st.markdown("**⚠️ Missing Skills (Top Priority)**")
        if missing:
            st.markdown("".join([f'<span class="gap-badge">{s}</span>' for s in missing[:15]]), unsafe_allow_html=True)
        else:
            st.success("All key skills covered!")

def footer(candidate_name: str):
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align:center; padding:0.8rem; border-radius:10px;
                    background: rgba(15,23,42,0.35); border:1px solid rgba(100,116,139,0.12);">
            <p style="color:var(--muted); margin:0; font-size:0.9rem;">
                Analysis completed on {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}
                {'for ' + candidate_name if candidate_name else ''} | Powered by ML & NLP
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )