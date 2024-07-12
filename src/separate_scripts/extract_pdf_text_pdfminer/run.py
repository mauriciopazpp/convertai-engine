import argparse
from modules.extractAndProcessPage import extract_and_process_pages  # type: ignore

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process PDF pages.')
    parser.add_argument('--pdf_path', type=str, required=True, help='Path to the PDF file.')
    parser.add_argument('--start_page', type=int, required=True, help='Page number to start processing from.')
    parser.add_argument('--end_page', type=int, help='Page number to end processing at.')
    parser.add_argument('--page_height', type=float, default=29.7, help='Height of the page in cm.')
    parser.add_argument('--header', type=float, default=1.76, help='Header margin in cm.')
    parser.add_argument('--footer', type=float, default=1.76, help='Footer margin in cm.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode to print the pages dictionary.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    pages = extract_and_process_pages(
        pdf_path=args.pdf_path,
        start_page=args.start_page,
        end_page=args.end_page,
        page_height_cm=args.page_height,
        header_margin_cm=args.header,
        footer_margin_cm=args.footer
    )

    if args.debug:
        for key, value in pages.items():
            print(f'{key}: {value},')

if __name__ == "__main__":
    main()
