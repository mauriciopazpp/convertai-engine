from pdfminer.layout import LTChar, LTRect

def get_font_size(element):
    font_sizes = []

    if isinstance(element, LTChar):
        font_sizes.append(element.size)
    elif hasattr(element, '__iter__'):
        for obj in element:
            if isinstance(obj, LTChar):
                font_sizes.append(obj.size)
            elif hasattr(obj, '__iter__'):
                for sub_obj in obj:
                    if isinstance(sub_obj, LTChar):
                        font_sizes.append(sub_obj.size)

    if font_sizes:
        return max(font_sizes)
        #return round(max(font_sizes))
    return None
