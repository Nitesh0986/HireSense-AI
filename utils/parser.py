import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF resume.

    Parameters:
        pdf_path (str): Path of PDF

    Returns:
        str: Extracted text
    """

    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            text += page.get_text()

        document.close()

        return text

    except Exception as e:
        print("Error:", e)
        return ""