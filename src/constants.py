import json, os

TECH_SKILLS = {
    "python", "java", "javascript", "c", "c#", "c++", "ruby", "go", "rust", "swift", "kotlin", "r", "shell",
    "html", "css", "react", "angular", "node.js", "express", "django", "flask", "fastapi", "spring boot", "next.js",
    "sql", "mysql", "postgresql", "mongodb", "oracle", "sql server", "elasticsearch", "neo4j", "sqlite",
    "aws", "azure", "docker", "kubernetes", "jenkins", "ci/cd", "git", "github", "gitlab",
    "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy", "tableau", "power bi", "data science", "statistics",
    "rest api", "graphql", "agile", "scrum", "linux", "unix", "windows", "networking", "security", "testing", "dart",
    "npm", "firebase"
}

COMMUNICATION_SKILLS = [
    "communication", "presentation", "documentation", "technical writing",
    "client interaction", "verbal", "written", "public speaking", "reporting", "collaboration"
]

SOFT_SKILLS = [
    "leadership", "teamwork", "problem solving", "analytical", "critical thinking",
    "time management", "adaptability", "creativity", "innovation", "mentoring",
    "strategic thinking", "decision making", "conflict resolution", "empathy"
]

EXPERIENCE_KEYWORDS = [
    "years", "experience", "worked", "developed", "led", "managed", "designed",
    "implemented", "built", "created", "delivered", "project", "internship",
    "contributed", "achieved", "improved", "optimized", "scaled"
]

_weights_path = os.path.join(os.path.dirname(__file__), "ml_weights.json")

if os.path.exists(_weights_path):
    with open(_weights_path) as f:
        WEIGHTS = json.load(f)
