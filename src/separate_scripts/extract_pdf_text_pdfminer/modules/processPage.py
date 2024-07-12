from modules.processElement.processElement import process_element # type: ignore

def process_page(pages, page_layout, page_number, page_height_pt, header_margin_cm, footer_margin_cm, page_width):
    for element in page_layout:
        process_element(pages, page_number, element, page_height_pt, header_margin_cm, footer_margin_cm, page_width)
