from pdfminer.layout import LTChar

def get_font_family(element):
    font_families = set()

    for obj in element:
        if isinstance(obj, LTChar):
            font_families.add(obj.fontname)
        elif hasattr(obj, '__iter__'):
            for sub_obj in obj:
                if isinstance(sub_obj, LTChar):
                    font_families.add(sub_obj.fontname)

    font_family = list(font_families)[0] if font_families else None
    return font_family
