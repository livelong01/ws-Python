# PyPDF2 manipular arquivos PDF
# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# https://pypdf.readthedocs.io/en/latest/
# Ative seu ambiente virtual
# pip install pypdf2
# pip install --upgrade pypdf2


# from PyPDF2 import PdfReader, PdfWriter
# import os

# # Get the absolute path of the current script
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Construct the full path to the PDF file
# pdf_path_original = os.path.join(current_dir, "exemplo.pdf")
# pdf_path_modificado = os.path.join(current_dir, "encrypted-pdf.pdf")
# pdf_path_dec = os.path.join(current_dir, "decrypted-pdf.pdf")

# # Use the constructed path to read the PDF
# reader = PdfReader(pdf_path)
# writer = PdfWriter()

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Add a password to the new PDF
# writer.encrypt("my-secret-password")

# # Save the new PDF to a file
# with open(pdf_path_end, "wb") as f:
#     writer.write(f)


# ------------------------------------------

# reader = PdfReader(pdf_path_end)
# writer = PdfWriter()

# if reader.is_encrypted:
#     reader.decrypt("my-secret-password")

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Save the new PDF to a file
# with open(pdf_path_dec, "wb") as f:
#     writer.write(f)


# ----------------------------------------------------------- AULA
# from PIL import Image
# from io import BytesIO
# from pathlib import Path

# PASTA_RAIZ = Path(__file__).parent
# # PASTA_ORIGINAIS = Path("pdfs_originais")
# PASTA_ORIGINAIS = PASTA_RAIZ / "pdfs_originais"
# PASTA_MODIFICADOS = PASTA_RAIZ / "pdfs_modificados"
# # PASTA_MODIFICADOS = Path("pdfs_modificados")


# RELATORIO_BACEN = PASTA_ORIGINAIS / "R20250404.pdf"

# PASTA_ORIGINAIS.mkdir(exist_ok=True)

# reader = PdfReader(RELATORIO_BACEN)

# # print(f"Total de páginas: {len(reader.pages)}")

# # for page in reader.pages:
# #     print(page)

# page = reader.pages[0]
# count = 0

# for image_file_object in page.images:
#     image_bytes = image_file_object.data
#     img = Image.open(BytesIO(image_bytes))
#     img = img.convert("RGBA")  # ou "RGB" se não quiser transparência
#     with open(f"{count}_{image_file_object.name}", "wb") as fp:
#         img.save(fp, format="PNG")
#     count += 1


# # ----------------------------------------------------------- AULA final

from pathlib import Path

from pypdf import PdfReader, PdfWriter


PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAL = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'PDFS'

RELATORIO_BACEN = PASTA_ORIGINAL / 'R20250404.pdf'

PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagens = page0.images
# print(imagens)
# print(len(imagens))

# print(page0.extract_text())

# for count, image_file_object in enumerate(imagens):  # Percorre as imagens
#     caminho_arquivo = PASTA_NOVA / \
#         (str(count) + image_file_object.name)  # Cria o caminho do arquivo
#     with open(caminho_arquivo, "wb") as fp:
#         fp.write(image_file_object.data)  # Salva a imagem

writer = PdfWriter()
writer.add_page(page0)

# with open(PASTA_NOVA / 'pagina0.pdf', "wb") as fp:
#     writer.write(fp)  # Salva a página em um novo a arquivo PDF

# JUNTAR TODAS AS PAGINAS EM 1 ARQUIVO PDF
# pages = reader.pages
# writer = PdfWriter()  # Cria um novo objeto PdfWriter

# with open(PASTA_NOVA / 'NOVO.pdf', "wb") as fp:
#     for page in pages:  # Percorre todas as páginas
#         writer.add_page(page)      # Adiciona a página ao objeto PdfWriter

#     writer.write(fp)    # Salva o arquivo PDF com todas as páginas

# CADA PAGINA EM UM ARQUIVO PDF.

# pages = reader.pages


# for i, page in enumerate(pages):  # Percorre todas as páginas
#     writer = PdfWriter()
#     with open(PASTA_NOVA / f'{i}-NOVO.pdf', "wb") as fp:
#         writer.add_page(page)      # Adiciona a página ao objeto PdfWriter
#         writer.write(fp)

files = [  # A ordem dos arquivos é importante,
    # pois eles serão unidos na ordem em que estão
    PASTA_NOVA / '0-NOVO.pdf',
    PASTA_NOVA / '1-NOVO.pdf',
    PASTA_NOVA / 'copy.pdf',
    PASTA_NOVA / 'pagina0.pdf',
    PASTA_NOVA / 'MERGER.pdf',
]


merger = PdfWriter()
for file in files:
    merger.append(file)

with open(PASTA_NOVA / 'TUDO_JUNTO.pdf', "wb") as fp:
    merger.write(fp)
