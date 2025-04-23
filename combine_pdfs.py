import PyPDF2
import os
from scrape_lobby_pdf import setup_folders

# Note: This can take some time!

def combine_pdfs(pdf_dir, output_path):
    merger = PyPDF2.PdfFileMerger()
    
    # Get list of PDF files in the directory
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    
    # Sort the PDF files to ensure they are merged in the correct order
    pdf_files.sort()
    
    # Merge PDFs
    for pdf_file in pdf_files:
        with open(os.path.join(pdf_dir, pdf_file), 'rb') as f:
            merger.append(f)
    
    # Write merged PDF to output file
    with open(output_path, 'wb') as f:
        merger.write(f)

# Parameters
data_dir = '/home/will/Datasets/' # should exist already on your computer
data_path = setup_folders(data_dir)
print(f"Location of scraped PDFs: {data_path}")

# Example usage:
pdf_directory = data_path
output_pdf_path = data_path + 'combined.pdf'

combine_pdfs(pdf_directory, output_pdf_path)