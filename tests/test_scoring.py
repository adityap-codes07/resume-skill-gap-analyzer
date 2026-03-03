import pytest

from src.services.scoring import run_analysis, build_recommendations


JOB = """
We are hiring a Python developer with experience in Flask, SQL, Git, Docker, and AWS.
Must have good communication, documentation, teamwork, and leadership.
"""

RESUME_STRONG = """
Aditya is a Python developer. Built APIs using Flask and FastAPI.
Worked with SQL databases (PostgreSQL), used Git/GitHub daily and Docker for deployments.
Deployed services on AWS. Strong communication and documentation skills.
Teamwork and leadership demonstrated in multiple projects.
3 years of experience.
"""

RESUME_WEAK = """
I am a fresher looking for a software job.
I have basic knowledge of programming.
No major projects.
"""


def test_run_analysis_returns_expected_keys():
    result = run_analysis(JOB, RESUME_STRONG)
    expected_keys = {
        "tech_score", "comm_score", "soft_score", "exp_score",
        "final_score", "fit_level", "fit_color",
        "matched_skills", "missing_skills",
        "job_skills", "resume_skills", "years_exp"
    }
    assert expected_keys.issubset(result.keys())


def test_scores_are_in_valid_range():
    result = run_analysis(JOB, RESUME_STRONG)
    for k in ["tech_score", "comm_score", "soft_score", "exp_score", "final_score"]:
        assert 0 <= result[k] <= 100


def test_strong_resume_has_higher_score_than_weak_resume():
    strong = run_analysis(JOB, RESUME_STRONG)
    weak = run_analysis(JOB, RESUME_WEAK)
    assert strong["final_score"] > weak["final_score"]


def test_matched_and_missing_skills_are_disjoint():
    result = run_analysis(JOB, RESUME_STRONG)
    assert set(result["matched_skills"]).isdisjoint(set(result["missing_skills"]))


def test_fit_level_is_valid_label():
    result = run_analysis(JOB, RESUME_STRONG)
    assert result["fit_level"] in {"Excellent", "Good", "Moderate", "Needs Improvement"}


def test_recommendations_generated_for_weak_resume():
    result = run_analysis(JOB, RESUME_WEAK)
    recs = build_recommendations(result)

    # Weak resume should generally trigger at least one recommendation
    assert isinstance(recs, list)
    assert len(recs) >= 1

    # Recommendation item structure sanity check
    for r in recs:
        assert "priority" in r
        assert "category" in r
        assert "action" in r
        assert "impact" in r


def test_no_crash_when_job_description_empty_skills():
    job = "This role involves general responsibilities."
    resume = "I have worked on projects and communication."
    result = run_analysis(job, resume)
    assert 0 <= result["tech_score"] <= 100