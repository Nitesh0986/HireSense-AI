from utils.parser import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills

pdf_path = "resumes/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

clean_text = preprocess_text(text)

skills = extract_skills(clean_text)

print("=" * 50)
print("Detected Skills")
print("=" * 50)

for skill in skills:
    print("✔", skill)