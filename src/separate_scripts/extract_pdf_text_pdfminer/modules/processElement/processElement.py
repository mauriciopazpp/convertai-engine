###
# Um "elemento" eh estrutura ou objeto que representa
# uma parte do conteúdo de uma página. Pode ser um parágrafo,
# uma linha de texto, uma imagem, um título, ou qualquer outro componente
# que compõe a página.
##
from modules.processElement.get_position import get_position # type: ignore
from modules.processElement.get_text import get_text # type: ignore
from modules.processElement.is_header_or_footer import is_header_or_footer # type: ignore
from modules.processElement.get_font_size import get_font_size
from modules.processElement.get_font_family import get_font_family
from modules.processElement.get_text_with_styles import get_text_with_styles
from modules.processElement.check_if_is_text import check_if_is_text
from modules.processElement.get_text_alignment import get_text_alignment
#from modules.processElement.is_indented import is_indented

def process_element(pages, page_number, element, page_height_pt, header_margin_cm, footer_margin_cm, page_width):
    position = get_position(element)
    on_header, on_footer = is_header_or_footer(position, page_height_pt, header_margin_cm, footer_margin_cm)

    if check_if_is_text(element):
        text = get_text(element)
        text_with_styles = get_text_with_styles(element)
        #text_alignment = get_text_alignment(element, page_width)
        #indented = is_indented(element, page_width)
    else:
        text = None
        text_with_styles = None
        #text_alignment = None
        #indented = None

    element_info = {
        'text': text,
        'on_header': on_header,
        'on_footer': on_footer,
        'position': position,
        #'element': element,
        #'type_element': type(element).__name__,
        #'type_object': type(element),
        #'font_size': get_font_size(element),
        'text_with_styles': text_with_styles,
        #'alignment': text_alignment,
        'page_width': page_width,
        #'indented': indented
    }
    pages[page_number]['elements'].append(element_info)
