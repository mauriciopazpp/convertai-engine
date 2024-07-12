from pdfminer.layout import LTTextBox, LTTextBoxHorizontal, LTTextLine, LTTextLineHorizontal

def get_text_alignment(element, page_width):
    x0, x1 = element.bbox[0], element.bbox[2]

    margin_of_error = 0.05 * page_width

    if abs(x0) < margin_of_error:  # very close to the left margin
        return "left"
    elif abs(x1 - page_width) < margin_of_error:  # very close to the right margin
        return "right"
    elif abs((x0 + x1) / 2 - page_width / 2) < margin_of_error:  # center of the element close to center of the page
        return "center"
    else:
        return "justified"
