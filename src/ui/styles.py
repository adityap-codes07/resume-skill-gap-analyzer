import streamlit as st

CSS = """
<style>

/* =====================================================
   🎨 THEME VARIABLES
   Centralized color configuration
   ===================================================== */
:root {
    --bg-900: #0f172a;
    --bg-800: #1e293b;
    --primary: #6366f1;
    --accent: #a855f7;
    --muted: #94a3b8;
    --text: #f8fafc;
    --card-bg: rgba(15, 23, 42, 0.6);
    --input-bg: rgba(15, 23, 42, 0.55);
}


/* =====================================================
   🧱 BASE STYLING
   ===================================================== */

/* Import clean modern font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

* {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

/* Hide default Streamlit menu & footer */
#MainMenu,
header,
footer {
    visibility: hidden;
}

/* Main app background */
.stApp {
    background: linear-gradient(180deg, var(--bg-900), var(--bg-800));
    color: var(--text);
}

/* Content container width */
.block-container {
    padding: 2rem;
    max-width: 1200px;
}


/* =====================================================
   🔘 BUTTONS
   ===================================================== */

.stButton > button {
    background: var(--primary);
    color: #ffffff;
    border: none;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    border-radius: 10px;
}


/* =====================================================
   📝 INPUT FIELDS
   ===================================================== */

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: var(--input-bg);
    border: 1px solid rgba(100, 116, 139, 0.25);
    border-radius: 8px;
    color: var(--text);
    padding: 0.6rem;
    font-size: 0.95rem;
}


/* =====================================================
   📊 DATAFRAME CONTAINER
   ===================================================== */

div[data-testid="stDataFrame"] {
    background: var(--card-bg);
    border-radius: 10px;
    padding: 0.75rem;
}


/* =====================================================
   📦 METRIC CARDS
   ===================================================== */

.metric-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(100, 116, 139, 0.12);
    border-radius: 12px;
    padding: 1.25rem;
    text-align: center;
}


/* =====================================================
   🏷 SKILL & GAP BADGES
   ===================================================== */

.skill-badge,
.gap-badge {
    display: inline-block;
    padding: 0.35rem 0.75rem;
    border-radius: 16px;
    font-size: 0.85rem;
    font-weight: 500;
    margin: 0.2rem;
}

/* Matched Skills */
.skill-badge {
    background: rgba(99, 102, 241, 0.12);
    color: var(--primary);
    border: 1px solid rgba(99, 102, 241, 0.18);
}

/* Missing Skills */
.gap-badge {
    background: rgba(239, 68, 68, 0.10);
    color: #ef4444;
    border: 1px solid rgba(239, 68, 68, 0.18);
}


/* =====================================================
   🚀 HERO SECTION
   ===================================================== */

.hero-title {
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    color: var(--text);
}

.hero-sub {
    color: var(--muted);
    margin: 0;
    font-size: 1rem;
    line-height: 1.5;
    max-width: 900px;
}


/* =====================================================
   📐 METRICS GRID LAYOUT
   ===================================================== */

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin: 1.25rem 0;
}

</style>
"""

def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)