import pdfplumber
import os

class PDFProcessor:
    """Extract text from PDF files"""
    
    @staticmethod
    def extract_text(pdf_path):
        """
        Extract text from a PDF file
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
        """
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n\n"
            
            # Clean up the text
            text = text.strip()
            
            if not text:
                raise ValueError("No text could be extracted from the PDF")
            
            return text
            
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    @staticmethod
    def validate_pdf(file):
        """
        Validate that the uploaded file is a valid PDF
        
        Args:
            file: FileStorage object from Flask
            
        Returns:
            bool: True if valid, raises exception otherwise
        """
        if not file:
            raise ValueError("No file provided")
        
        if file.filename == '':
            raise ValueError("No file selected")
        
        if not file.filename.lower().endswith('.pdf'):
            raise ValueError("File must be a PDF")
        
        return True
