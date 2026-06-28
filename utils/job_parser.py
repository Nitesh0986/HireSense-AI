from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills


def extract_job_skills(job_file):

    with open(job_file, "r", encoding="utf-8") as file:

        text = file.read()

    clean_text = preprocess_text(text)

    skills = extract_skills(clean_text)

    return clean_text, skills