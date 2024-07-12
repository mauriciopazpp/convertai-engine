# Extract Elements from PDF

Este script permite extrair e processar elementos de um arquivo PDF, começando a partir de uma página específica.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca `pdfminer.six`

## Instalação

1. Instale a biblioteca `pdfminer.six` utilizando pip:

```sh
pip install pdfminer.six

2. Coloque o pdf na mesma pasta, altere o nome da variavel, e use o comando para executar

#python extract_elements_from_pdf.py start_page=1

# python run.py --start_page=56 --page_height=29.7 --header=1.76 --footer=1.76 --debug

# python run.py --pdf_path="input/arte-da-guerra.pdf" --start_page=56 --page_height=29.7 --header=1.76 --footer=1.76 --debug

python run.py \
    --pdf_path="files/input/arte-da-guerra.pdf" \
    --start_page=56 \
    --page_height=29.7 \
    --header=1.76 \
    --footer=1.76 \
    --debug \
    > files/output/output.txt
