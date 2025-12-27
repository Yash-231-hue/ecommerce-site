import os
from pdf2docx import Converter

def perform_conversion(pdf_path):
    """
    Uses the pdf2docx library to convert PDF to Word while 
    preserving layout, images, and tables.
    """
    # Define the output path (e.g., media/resume.pdf -> media/resume.docx)
    docx_path = pdf_path.replace(".pdf", ".docx")
    
    try:
        # 1. Initialize the Converter with the PDF file path
        cv = Converter(pdf_path)
        
        # 2. Convert the PDF to Word
        # start=0, end=None means convert all pages
        cv.convert(docx_path, start=0, end=None)
        
        # 3. Close the converter to release the file
        cv.close()
        
        # Return the path to the newly created .docx file
        return docx_path
        
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None