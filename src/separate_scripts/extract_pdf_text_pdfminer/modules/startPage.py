import sys

def parse_start_page_argument():
    start_page = 1
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.startswith("start_page="):
            try:
                start_page = int(arg.split("=")[1])
            except ValueError:
                print("Valor de página inicial inválido. Usando a página 1 como padrão.")
    return start_page
