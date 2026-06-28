import os

from utils.parser import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity


def process_resume(resume_path, job_description):

    resume_text = extract_text_from_pdf(resume_path)

    clean_resume = preprocess_text(resume_text)

    skills = extract_skills(clean_resume)

    score = calculate_similarity(
        clean_resume,
        job_description
    )

    return {

        "Candidate": os.path.basename(resume_path),

        "ATS Score": score,

        "Skills": skills

    }