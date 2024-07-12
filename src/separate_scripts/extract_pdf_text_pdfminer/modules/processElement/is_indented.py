from pdfminer.layout import LTTextBox, LTTextBoxHorizontal, LTTextLine, LTTextLineHorizontal

def is_indented(element, page_width, indent_threshold=0.05):
    if isinstance(element, (LTTextBox, LTTextBoxHorizontal, LTTextLine, LTTextLineHorizontal)):
        x0, _, _, _ = element.bbox
        return x0 > page_width * indent_threshold
    return False
