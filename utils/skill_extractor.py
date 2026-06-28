import re

SKILLS_DATABASE = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "express",
    "flask",
    "django",
    "tensorflow",
    "keras",
    "pytorch",
    "machine learning",
    "deep learning",
    "nlp",
    "streamlit",
    "git",
    "github",
    "docker",
    "linux",
    "numpy",
    "pandas",
    "opencv",
    "matplotlib",
    "seaborn",
    "fastapi",
    "redis"
]

def extract_skills(text):
    """
    Extract technical skills from any text.
    Works for resumes and job descriptions.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DATABASE:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))