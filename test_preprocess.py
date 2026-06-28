from utils.parser import extract_text_from_pdf
from utils.preprocess import preprocess_text

pdf_path = "resumes/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

clean_text = preprocess_text(text)

print("=" * 50)
print("Original Resume Text")
print("=" * 50)
print(text)

print("\n")

print("=" * 50)
print("Cleaned Resume Text")
print("=" * 50)
print(clean_text)