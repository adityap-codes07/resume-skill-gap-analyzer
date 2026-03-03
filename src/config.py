import streamlit as st

def set_page() -> None:
    st.set_page_config(
        page_title="ML & TF-IDF Resume Similarity and Skill Gap Analyzer",
        layout="wide",
        initial_sidebar_state="collapsed",
    )