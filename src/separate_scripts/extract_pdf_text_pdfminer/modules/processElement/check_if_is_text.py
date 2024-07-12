from pdfminer.layout import LTTextContainer

def check_if_is_text(element):
    return isinstance(element, LTTextContainer)
