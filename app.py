import streamlit as st

from src.config import set_page
from src.ui.styles import inject_css
from src.ui.components import hero, section_header, metrics_cards, skills_block, footer
from src.ui.charts import render_gauges
from src.services.scoring import run_analysis, build_breakdown_df, build_recommendations


def main():
    set_page()
    inject_css()
    hero()

    # ===== INPUT SECTION =====
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        section_header("Job Requirements", "📋")
        job_role = st.text_input("Position Title", placeholder="e.g., Senior Software Engineer")
        job_description = st.text_area(
            "Complete Job Description",
            height=300,
            placeholder="Paste the full job description including required skills, responsibilities, qualifications, and experience..."
        )

    with col2:
        section_header("Candidate Profile", "👤")
        candidate_name = st.text_input("Candidate Name (Optional)", placeholder="John Doe")
        resume_text = st.text_area(
            "Complete Resume Content",
            height=300,
            placeholder="Paste your entire resume including professional summary, work experience, education, skills, projects, and achievements..."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ===== RUN ANALYSIS =====
    if st.button("🔬 Run Advanced Analysis", use_container_width=True):
        if not job_description or not resume_text:
            st.error("⚠️ Please provide both job description and resume content.")
            return

        with st.spinner("🔄 Applying TF-IDF and similarity models..."):
            result = run_analysis(job_description, resume_text)

        # ===== RESULTS =====
        st.markdown("<br>", unsafe_allow_html=True)
        section_header("Analysis Results", "📊")
        metrics_cards(result)

        section_header("Detailed Scoring Breakdown", "📈")
        render_gauges(result)

        section_header("Category Breakdown", "📋")
        df = build_breakdown_df(result)
        st.dataframe(df, use_container_width=True, hide_index=True)

        section_header("Skills Intelligence", "🎯")
        skills_block(result)

        section_header("ATS Optimization Insights", "💡")
        recs = build_recommendations(result)
        if result["final_score"] >= 80:
            st.success("🎉 **Outstanding Match!** Your resume is highly competitive for this role. Consider applying immediately.")
        elif recs:
            for r in recs:
                st.warning(f"**{r['priority']} - {r['category']}**  \n📌 {r['action']}  \n💫 *{r['impact']}*")
        else:
            st.info("✨ Your resume is well-aligned with the job requirements. Minor optimizations may further enhance your chances.")

        footer(candidate_name)


if __name__ == "__main__":
    main()