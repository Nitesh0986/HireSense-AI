from utils.parser import extract_text_from_pdf

pdf_path = "resumes/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("=" * 50)
print("Extracted Resume Text")
print("=" * 50)

print(text)