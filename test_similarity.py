from utils.parser import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.similarity import calculate_similarity

# Resume
resume = extract_text_from_pdf("resumes/sample_resume.pdf")

resume = preprocess_text(resume)

# Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:

    job = file.read()

job = preprocess_text(job)

score = calculate_similarity(resume, job)

print("=" * 50)
print("ATS MATCH SCORE")
print("=" * 50)

print(f"\nResume Match : {score}%")