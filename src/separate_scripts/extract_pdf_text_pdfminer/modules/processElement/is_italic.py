def is_italic(element):
    italic = False
    for line in element:
        if hasattr(line, 'fontname'):
            fontname = line.fontname.lower()
            if 'italic' in fontname or 'oblique' in fontname:
                return True
        if hasattr(line, '__iter__'):  # Verifica se line é iterável
            for char in line:
                if hasattr(char, 'fontname'):
                    fontname = char.fontname.lower()
                    if 'italic' in fontname or 'oblique' in fontname:
                        return True
    return italic
