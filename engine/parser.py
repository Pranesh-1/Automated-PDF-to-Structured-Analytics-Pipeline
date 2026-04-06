import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts raw text from a PDF file using PyMuPDF."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        raise
        
    return text.strip()

if __name__ == "__main__":
    # Test extraction
    test_pdf = "sample.pdf" # Placeholder for testing
    if os.path.exists(test_pdf):
        print(extract_text_from_pdf(test_pdf))
