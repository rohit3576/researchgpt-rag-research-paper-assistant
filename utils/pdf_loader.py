import PyPDF2
from typing import Union
import re


def clean_text(text: str) -> str:
    """
    Cleans extracted PDF text by fixing line breaks and spacing.
    """
    text = re.sub(r"-\n", "", text)      # Fix hyphenated line breaks
    text = re.sub(r"\n", " ", text)      # Remove newlines
    text = re.sub(r"\s+", " ", text)     # Normalize spaces
    return text.strip()


def extract_text_from_pdf(pdf_path: Union[str, bytes]) -> str:
    """
    Extracts and cleans text from a PDF file.

    Args:
        pdf_path (str or bytes): Path to PDF file

    Returns:
        str: Cleaned extracted text
    """
    raw_text = ""

    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    raw_text += page_text + "\n"

    except Exception as e:
        print(f"[ERROR] Failed to read PDF: {e}")

    return clean_text(raw_text)


# ---------------- TEST BLOCK ----------------
if __name__ == "__main__":
    sample_pdf = "sample.pdf"  # put any test PDF in project root
    extracted_text = extract_text_from_pdf(sample_pdf)

    print("✅ Extracted Text Preview:\n")
    print(extracted_text[:1000])
