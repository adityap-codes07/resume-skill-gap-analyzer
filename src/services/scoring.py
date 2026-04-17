from typing import Dict, Any, List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from src.constants import TECH_SKILLS, COMMUNICATION_SKILLS, SOFT_SKILLS, EXPERIENCE_KEYWORDS, WEIGHTS
from src.utils.text import clean_text, extract_skills, extract_years_of_experience


def technical_matching(job_text: str, resume_text: str):
    job_skills = extract_skills(job_text, TECH_SKILLS)
    resume_skills = extract_skills(resume_text, TECH_SKILLS)

    if not job_skills:
        # No tech skills required in JD → full marks
        return 100.0, job_skills, resume_skills

    skill_match = len(set(job_skills) & set(resume_skills)) / len(job_skills)

    # Only use TF-IDF as a bonus when job skills is detailed enough (4+ words)
    if len(job_skills) >= 5:
        vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 3), max_features=500)
        tfidf = vectorizer.fit_transform([job_text, resume_text])
        tfidf_score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        final_score = (tfidf_score * 0.4 + skill_match * 0.6) * 100
    else:
        final_score = skill_match * 100

    return final_score, job_skills, resume_skills


def run_analysis(job_description: str, resume_text: str) -> Dict[str, Any]:
    job_clean = clean_text(job_description)  # from src.utils.text file
    resume_clean = clean_text(resume_text)

    tech_score, job_skills, resume_skills = technical_matching(job_clean, resume_clean)
    matched_skills = list(set(job_skills) & set(resume_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    jd_comm_skills = extract_skills(job_clean, COMMUNICATION_SKILLS)
    if jd_comm_skills:
        comm_found = extract_skills(resume_clean, COMMUNICATION_SKILLS)
        comm_score = min((len(set(comm_found) & set(jd_comm_skills)) / len(jd_comm_skills)) * 100, 100)
    else:
        comm_score = 100.0  # JD doesn't require communication skills → full marks

    jd_soft_skills = extract_skills(job_clean, SOFT_SKILLS)
    if jd_soft_skills:
        soft_found = extract_skills(resume_clean, SOFT_SKILLS)
        soft_score = min((len(set(soft_found) & set(jd_soft_skills)) / len(jd_soft_skills)) * 100, 100)
    else:
        soft_score = 100.0  # JD doesn't require soft skills → full marks

    jd_exp_keywords = extract_skills(job_clean, EXPERIENCE_KEYWORDS)
    years_exp = extract_years_of_experience(resume_clean)
    if jd_exp_keywords:
        exp_found = extract_skills(resume_clean, EXPERIENCE_KEYWORDS)
        exp_score = min((len(set(exp_found) & set(jd_exp_keywords)) / len(jd_exp_keywords)) * 100 + (years_exp * 5),
                        100)
    else:
        exp_score = 100.0 if years_exp > 0 else 50.0  # No exp required → generous default

    final_score = (
        tech_score * WEIGHTS["technical"] +
        comm_score * WEIGHTS["communication"] +
        soft_score * WEIGHTS["soft_skills"] +
        exp_score * WEIGHTS["experience"]
    )

    if final_score >= 80:
        fit_level, fit_color = "Excellent", "#22c55e"
    elif final_score >= 65:
        fit_level, fit_color = "Good", "#eab308"
    elif final_score >= 50:
        fit_level, fit_color = "Moderate", "#f97316"
    else:
        fit_level, fit_color = "Needs Improvement", "#ef4444"

    return {
        "tech_score": tech_score,
        "comm_score": comm_score,
        "soft_score": soft_score,
        "exp_score": exp_score,
        "final_score": final_score,
        "fit_level": fit_level,
        "fit_color": fit_color,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "job_skills": job_skills,
        "resume_skills": resume_skills,
        "years_exp": years_exp,
        "jd_comm_required": len(extract_skills(job_clean, COMMUNICATION_SKILLS)) > 0,
        "jd_soft_required": len(extract_skills(job_clean, SOFT_SKILLS)) > 0,
        "jd_exp_required": len(extract_skills(job_clean, EXPERIENCE_KEYWORDS)) > 0,
    }


def build_breakdown_df(result: Dict[str, Any]) -> pd.DataFrame:
    tech = result["tech_score"]
    comm = result["comm_score"]
    soft = result["soft_score"]
    exp = result["exp_score"]

    return pd.DataFrame({
        "Category": ["Technical Skills", "Communication", "Soft Skills", "Experience"],
        "Score": [f"{tech:.1f}%", f"{comm:.1f}%", f"{soft:.1f}%", f"{exp:.1f}%"],
        "Weight": ["45%", "20%", "20%", "15%"],
        "Impact": [
            f"{tech * WEIGHTS['technical']:.1f}",
            f"{comm * WEIGHTS['communication']:.1f}",
            f"{soft * WEIGHTS['soft_skills']:.1f}",
            f"{exp * WEIGHTS['experience']:.1f}",
        ],
    })


def build_recommendations(result: Dict[str, Any]) -> List[Dict[str, str]]:
    recs = []
    tech_score = result["tech_score"]
    comm_score = result["comm_score"]
    soft_score = result["soft_score"]
    exp_score = result["exp_score"]
    missing_skills = result["missing_skills"]

    if tech_score < 70:
        recs.append({
            "priority": "🔴 High",
            "category": "Technical Skills",
            "action": f"Acquire {len(missing_skills)} missing technical skills: {', '.join(missing_skills[:5])}{'...' if len(missing_skills) > 5 else ''}",
            "impact": "Will increase overall score by ~15-20 points",
        })

    if comm_score < 60 and result.get("jd_comm_required"):
        recs.append({
            "priority": "🟡 Medium",
            "category": "Communication",
            "action": "Add examples of presentations, documentation, and stakeholder interactions to resume",
            "impact": "Will improve overall score by ~8-12 points",
        })

    if soft_score < 60 and result.get("jd_soft_required"):
        recs.append({
            "priority": "🟡 Medium",
            "category": "Soft Skills",
            "action": "Highlight leadership, teamwork, and problem-solving achievements with quantifiable results",
            "impact": "Will improve overall score by ~8-12 points",
        })

    if exp_score < 50 and result.get("jd_exp_required"):
        recs.append({
            "priority": "🟠 Medium-High",
            "category": "Experience",
            "action": "Add more project details/internships; quantify achievements (e.g., 'increased efficiency by 30%')",
            "impact": "Will improve overall score by ~6-10 points",
        })

    return recs