from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal

def get_text(element):
    if isinstance(element, (LTTextBoxHorizontal, LTTextLineHorizontal)):
        return element.get_text()
    return None
