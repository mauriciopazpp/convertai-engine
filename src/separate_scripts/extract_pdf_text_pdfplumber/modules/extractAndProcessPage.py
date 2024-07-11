import pdfplumber

def extract_and_process_pages(pdf_path, start_at_page, process_page):
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            if page_num >= start_at_page:
                process_page(page_num, page)
