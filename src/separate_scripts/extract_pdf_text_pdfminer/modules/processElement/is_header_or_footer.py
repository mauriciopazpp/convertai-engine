from modules.processElement.cm_to_pt import cm_to_pt # type: ignore

def is_header_or_footer(position, page_height_cm, header_margin_cm, footer_margin_cm):
    page_height_pt = cm_to_pt(page_height_cm)
    header_margin_pt = cm_to_pt(header_margin_cm)
    footer_margin_pt = cm_to_pt(footer_margin_cm)
    y0 = position['y0']
    y1 = position['y1']
    on_header = y1 > (page_height_pt - header_margin_pt)
    on_footer = y0 < footer_margin_pt
    return on_header, on_footer
