import pdfplumber
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
import os

def create_half_pdf(input_pdf_path, output_pdf_path):
    """
    Extract text from PDF and create a new PDF with half the text content.
    """
    print(f"Reading PDF: {input_pdf_path}")
    
    # Extract all text from the PDF
    all_text = []
    with pdfplumber.open(input_pdf_path) as pdf:
        print(f"Total pages in original PDF: {len(pdf.pages)}")
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                all_text.append(text)
                print(f"Extracted text from page {page_num}")
    
    # Combine all text
    full_text = "\n\n".join(all_text)
    total_chars = len(full_text)
    print(f"\nTotal characters extracted: {total_chars}")
    
    # Get first half of the text
    half_point = total_chars // 2
    half_text = full_text[:half_point]
    print(f"Half text characters: {len(half_text)}")
    
    # Create new PDF with the half text
    print(f"\nCreating new PDF: {output_pdf_path}")
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='Justify',
        parent=styles['BodyText'],
        alignment=TA_JUSTIFY,
        fontSize=10,
        leading=14
    ))
    
    # Split text into paragraphs and add to document
    paragraphs = half_text.split('\n\n')
    
    for para_text in paragraphs:
        if para_text.strip():
            # Clean up the text
            para_text = para_text.strip().replace('\n', ' ')
            # Create paragraph
            para = Paragraph(para_text, styles['Justify'])
            elements.append(para)
            elements.append(Spacer(1, 0.2*inch))
    
    # Build PDF
    doc.build(elements)
    print(f"\n✅ Successfully created PDF with half the text!")
    print(f"Output file: {output_pdf_path}")

if __name__ == "__main__":
    input_pdf = r"C:\Users\USER\Desktop\Cog Culture\uploads\db6c40f9-8b18-4fde-b4c1-9a404cb6c5e7_Assessment_Reference_Market_Report.pdf"
    output_pdf = r"C:\Users\USER\Desktop\Cog Culture\uploads\Half_Market_Report.pdf"
    
    if os.path.exists(input_pdf):
        create_half_pdf(input_pdf, output_pdf)
    else:
        print(f"❌ Error: Input file not found: {input_pdf}")
