from modules.startPage import parse_start_page_argument  # type: ignore
from modules.extractAndProcessPage import extract_and_process_pages  # type: ignore

def process_page(page_num, page_layout):
    print(f"\n#### Processando página {page_num} ####\n")
    for element in page_layout:
        print(element)

def main():
    pdf_path = "input/meupdf.pdf"
    start_page = parse_start_page_argument()
    extract_and_process_pages(pdf_path, start_page, process_page)

if __name__ == "__main__":
    main()
