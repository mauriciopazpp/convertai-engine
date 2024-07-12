from pdfminer.layout import LTChar, LTTextBox, LTTextLine

def get_text_with_styles(element):
    text_styles = []
    if isinstance(element, (LTTextBox, LTTextLine)):
        for line in element:
            if hasattr(line, '__iter__'):
                for char in line:
                    if isinstance(char, LTChar):
                        fontname = char.fontname.lower()
                        text_styles.append({
                            'text': char.get_text(),
                            'bold': 'bold' in fontname,
                            'italic': 'italic' in fontname or 'oblique' in fontname,
                            'font_family': fontname,
                            'font_size': char.size
                        })
    elif isinstance(element, LTChar):
        fontname = element.fontname.lower()
        text_styles.append({
            'text': element.get_text(),
            'bold': 'bold' in fontname,
            'italic': 'italic' in fontname or 'oblique' in fontname,
            'font_family': fontname,
            'font_size': element.size
        })
    return text_styles
