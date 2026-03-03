import re
from typing import Iterable, List, Set

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s.#+]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_skills(text: str, skill_set: Iterable[str]) -> List[str]:
    text_lower = text.lower()
    found: Set[str] = set()

    for skill in skill_set:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text_lower):
            found.add(skill)

    return list(found)

def extract_years_of_experience(text: str) -> int:
    patterns = [
        r"(\d+)\+?\s*years?\s+(?:of\s+)?experience",
        r"experience\s*:?\s*(\d+)\+?\s*years?",
        r"(\d+)\+?\s*yrs?"
    ]

    years = []
    for p in patterns:
        matches = re.findall(p, text.lower())
        years.extend([int(m) for m in matches])

    return max(years) if years else 0