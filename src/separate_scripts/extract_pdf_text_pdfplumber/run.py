from modules.startPage import parse_start_page_argument  # type: ignore
from modules.extractAndProcessPage import extract_and_process_pages  # type: ignore

def process_page(page_num, page):
    print(f"\n#### Processando página {page_num} ####\n")
    text = page.extract_text()
    if text:
        print(text)

def main():
    pdf_path = "input/exemplo_2.pdf"
    start_page = parse_start_page_argument()
    extract_and_process_pages(pdf_path, start_page, process_page)

if __name__ == "__main__":
    main()
