import pytest

from src.utils.text import clean_text, extract_skills, extract_years_of_experience


def test_clean_text_lowercase_and_strip():
    raw = "  Hello WORLD  "
    assert clean_text(raw) == "hello world"


def test_clean_text_removes_special_chars_keeps_plus_hash_dot():
    raw = "C++ & Python!! #NLP... (2024)"
    # keeps: c++, python, #nlp..., 2024
    out = clean_text(raw)
    assert "c++" in out
    assert "python" in out
    assert "#nlp..." in out
    assert "2024" in out
    assert "&" not in out
    assert "!" not in out
    assert "(" not in out
    assert ")" not in out


def test_extract_skills_basic_word_boundary():
    text = "I have experience with Python and FastAPI. Also used SQL."
    skills = {"python", "fastapi", "sql", "java"}
    found = extract_skills(text, skills)
    assert set(found) == {"python", "fastapi", "sql"}


def test_extract_skills_word_boundary_prevents_substring_match():
    # "react" should not match "reaction"
    text = "We studied reaction kinetics."
    skills = {"react"}
    found = extract_skills(text, skills)
    assert found == []


@pytest.mark.parametrize(
    "text, expected",
    [
        ("I have 3 years of experience in software.", 3),
        ("Experience: 5 years in data science", 5),
        ("Worked for 2 yrs as an intern", 2),
        ("No experience mentioned", 0),
    ],
)
def test_extract_years_of_experience_patterns(text, expected):
    assert extract_years_of_experience(text) == expected


def test_extract_years_of_experience_returns_max():
    text = "I have 2 years of experience, earlier 1 yrs internship, total 4 years of experience."
    assert extract_years_of_experience(text) == 4