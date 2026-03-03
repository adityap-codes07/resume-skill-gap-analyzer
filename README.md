# 🚀 Resume Skill Gap Analyzer

An advanced ATS-style Resume Analysis platform powered by TF-IDF, Cosine Similarity, and multi-dimensional skill evaluation.

---

## 📌 Overview

Resume Skill Gap Analyzer is an advanced ATS-like Resume Analysis Tool which analyzes a Resume on parameters such as:

- Technical Skill Matching (Utilizing Techniques such as TF-IDF and Skill Overlap)
- Communication Skills
- Soft Skills
- Experience and Work Impact

It provides features such as:

- 📊 Overall Resume Fit Score (0-100)
- 🎯 Skill Gap Detection
- 📈 Resume Score Breakdown (Utilizing Gauge Charts)
- 💡 Resume Optimization Insights

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn (TF-IDF & Cosine Similarity)
- Pandas
- Plotly

---

## 📂 Project Structure


```text
resume-skill-gap-analyzer/
│
├── .streamlit/
│   └── config.toml
│
├── src/
│   ├── services/
│   │   ├── __init__.py
│   │   └── scoring.py
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── charts.py
│   │   ├── components.py
│   │   └── styles.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── constants.py
│
├── tests/
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt

```
---

## 🚀 Installation

1. Clone the repository:

git clone <your-repo-url>


2. Navigate to project folder:

cd ResumeSkillGapAnalyzer


3. Install dependencies:

pip install -r requirements.txt


4. Run the app:

streamlit run app.py


---

## 🎯 Features

- Advanced TF-IDF Similarity Scoring
- Multi Category Weighted Evaluation
- Industry Style Dashboard UI
- Real Time Skill Gap Identification
- Resume Improvement Suggestions

---

## 📈 Future Improvements

- PDF Resume Upload Support
- Job Role Based Skill Templates
- AI Resume Rewrite Suggestions
- Model Optimization & Caching

---

## 👤 Author

Aditya Prakash  
CSBS Undergraduate | ML & Data Enthusiast