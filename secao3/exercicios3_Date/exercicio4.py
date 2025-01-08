'''
Desafio
Crie um script que:

Apague todos os arquivos .jpg de uma pasta específica.
Mova os arquivos .pdf para uma nova pasta.
Renomeie a pasta para "Meus_pdfs".
Boa sorte! 🚀
'''
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join('\\temp', 'ws-Python', 'treino')
NOVA_PASTA = os.path.join('\\temp', 'ws-Python', 'NOVA_PASTA')
MEUS_PDFS = os.path.join('\\temp', 'ws-Python', 'Meu_pdf')


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for file_ in files:
        caminho_arquivo_1 = os.path.join(root, file_)
        caminho, extensao = os.path.splitext(caminho_arquivo_1)
        if extensao == '.jpg':
            print(caminho_arquivo_1)
            os.unlink(caminho_arquivo_1)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        _, extensao = os.path.splitext(caminho_arquivo)
        if extensao == '.pdf':
            # Criar o subdiretório correspondente em NOVA_PASTA
            subdiretorio = root.replace(PASTA_ORIGINAL, MEUS_PDFS)
            os.makedirs(subdiretorio, exist_ok=True)
            caminho_novo_arquivo = os.path.join(subdiretorio, file_)
            print(f"Movendo: {caminho_arquivo} -> {caminho_novo_arquivo}")
            # Move o arquivo
            shutil.move(caminho_arquivo, caminho_novo_arquivo)

print(f"Arquivos .pdf movidos para {MEUS_PDFS}")
