from pdfminer.high_level import extract_pages # type: ignore

def extract_and_process_pages(pdf_path, start_at_page, process_page):
    page_num = 1
    for page_layout in extract_pages(pdf_path):
        if page_num >= start_at_page:
            process_page(page_num, page_layout)
        page_num += 1
