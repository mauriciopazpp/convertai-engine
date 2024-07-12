import os
from openai import OpenAI
from pdfminer.high_level import extract_pages # type: ignore
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal # type: ignore
from modules.startPage import parse_start_page_argument # type: ignore

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_page(page_num, page_layout):
    elements = []
    for element in page_layout:
        if isinstance(element, (LTTextBoxHorizontal, LTTextLineHorizontal)):
            text = element.get_text()
            bbox = element.bbox  # (x0, y0, x1, y1)
            elements.append({
                "text": text,
                "bbox": bbox
            })
    print(f"Processed page {page_num} with {len(elements)} elements")
    return {
        "page_num": page_num,
        "elements": elements
    }

def extract_pdf_content(pdf_path, start_page):
    pages_content = []
    for page_num, page_layout in enumerate(extract_pages(pdf_path), start=1):
        if page_num >= start_page:
            page_content = process_page(page_num, page_layout)
            pages_content.append(page_content)
            print(f"Extracted content from page {page_num}")
    return pages_content

def translate_content(pages_content):
    translated_pages = []
    for page_content in pages_content:
        content_to_translate = "".join([el["text"] for el in page_content["elements"]])
        print(f"Translating content from page {page_content['page_num']}")
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a translator. Translate the following text to Brazilian Portuguese."
            },
            {
                "role": "user",
                "content": content_to_translate
            }
        ])
        translated_text = response.choices[0].message.content
        translated_page = {
            "page_num": page_content["page_num"],
            "elements": []
        }
        text_parts = translated_text.split('\n')
        for i, element in enumerate(page_content["elements"]):
            translated_page["elements"].append({
                "text": text_parts[i] if i < len(text_parts) else "",
                "bbox": element["bbox"]
            })
        translated_pages.append(translated_page)
        print(f"Translated page {page_content['page_num']}")
    return translated_pages

def create_docx(translated_pages, output_path):
    from docx import Document # type: ignore
    from docx.shared import Pt # type: ignore
    from docx.enum.text import WD_ALIGN_PARAGRAPH # type: ignore

    doc = Document()
    for page in translated_pages:
        print(f"Creating DOCX content for page {page['page_num']}")
        for element in page["elements"]:
            paragraph = doc.add_paragraph(element["text"])

            if element["bbox"][0] > 100:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            if paragraph.runs:
                run = paragraph.runs[0]
                run.font.size = Pt(12)
        doc.add_page_break()
    doc.save(output_path)
    print(f"DOCX file saved to {output_path}")

def main():
    pdf_path = "input/La_revolution-1-15.pdf"
    start_page = parse_start_page_argument()
    pages_content = extract_pdf_content(pdf_path, start_page)
    print(f"Extracted content from {len(pages_content)} pages")
    translated_pages = translate_content(pages_content)
    print(f"Translated content from {len(translated_pages)} pages")
    create_docx(translated_pages, "output/translated_document.docx")

if __name__ == "__main__":
    main()
