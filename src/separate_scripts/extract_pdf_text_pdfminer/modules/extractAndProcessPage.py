from pdfminer.high_level import extract_pages  # type: ignore
from modules.processPage import process_page

def extract_and_process_pages(pdf_path, start_page, end_page=None, page_height_cm=29.7, header_margin_cm=1.76, footer_margin_cm=1.76):
    pages = {}
    page_number = 0
    for page_layout in extract_pages(pdf_path):
        if page_number >= start_page - 1 and (end_page is None or page_number <= end_page - 1):
            pages[page_number + 1] = {'page_number': page_number + 1, 'elements': []}
            page_width = page_layout.width
            process_page(pages, page_layout, page_number + 1, page_height_cm, header_margin_cm, footer_margin_cm, page_width)
        page_number += 1
    return pages
