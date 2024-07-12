def get_position(element):
    if hasattr(element, 'x0') and hasattr(element, 'y0') and hasattr(element, 'x1') and hasattr(element, 'y1'):
        return {
            'x0': element.x0,
            'y0': element.y0,
            'x1': element.x1,
            'y1': element.y1
        }
    return None