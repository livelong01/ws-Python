'''Crie um script que:

Copie arquivos de uma pasta para outra, mantendo a estrutura de pastas.
Exiba os arquivos copiados com seus caminhos completos.
Adicione uma verificação para não copiar arquivos maiores que 5 MB.
💡 Dica: Use os.stat para verificar o tamanho do arquivo antes de copiá-lo.
'''

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join('\\temp', 'ws-Python', 'treino')
NOVA_PASTA = os.path.join('\\temp', 'ws-Python', 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL,
                                                           NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_)
        if os.stat(caminho_arquivo).st_size < 1000000:  # 1MB
            print(caminho_novo_arquivo)
            shutil.copy(caminho_arquivo, caminho_novo_arquivo)
