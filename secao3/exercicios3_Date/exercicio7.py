'''
🎯 Desafio
Crie um script que:
✅ Compacte apenas arquivos .txt dentro de um diretório específico.
✅ Dê a opção ao usuário de listar ou descompactar os arquivos depois da compactação.
✅ Pergunte ao usuário o nome do ZIP a ser criado.

Dica: Utilize input() para coletar a escolha do usuário.
'''
# import os
# from pathlib import Path
# from zipfile import ZipFile

# CAMINHO_RAIZ = Path(
#     "C://Users//jonat//Dropbox//PC//Desktop//coisas_zip//compactar").parent
# CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'compactar'
# # CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'compactar.zip'
# CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'descompactar'

# nome_zip = input('Qual nome do arquivo zip?: ')
# nome_completo = nome_zip + ".zip"
# CAMINHO_COMPACTADO = CAMINHO_RAIZ / nome_completo

# with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
#     for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
#         for file in files:
#             caminho_arquivo = os.path.join(root, file)
#             caminho, extensao = os.path.splitext(caminho_arquivo)
#             if extensao == ".txt":
#                 print(file)
#                 # file dps da virgula
#                 zip.write(os.path.join(root, file), file)
#             # serve para eu por o arquivo sem o caminho das pastas completas.
#             # que é a forma padrao do zip.write.

# resposta = input(
#     'Gostaria de descompactar(d) ou apenas listar(l) os arquivos zipados ? ')
# print(resposta)
# if resposta == "d":
#     with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
#         print("extraido!")
#         zip.extractall(CAMINHO_DESCOMPACTADO)
# elif resposta == "l":
#     with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
#         for arquivo in zip.namelist():
#             print(arquivo)
# else:
#     print('Digite um valor válido!')

# VERSAO MELHORADA SUGERIDA POELO CHATGPT

import os
from pathlib import Path
from zipfile import ZipFile

# Definição de caminhos
CAMINHO_RAIZ = Path(
    "C://Users//jonat//Dropbox//PC//Desktop//coisas_zip//compactar").parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'compactar'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'descompactar'

# Pergunta ao usuário o nome do ZIP
nome_zip = input('Qual nome do arquivo zip?: ').strip()
nome_completo = f"{nome_zip}.zip"
CAMINHO_COMPACTADO = CAMINHO_RAIZ / nome_completo


def compactar_txt():
    """Compacta apenas arquivos .txt dentro do diretório especificado."""
    with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
        for root, _, files in os.walk(CAMINHO_ZIP_DIR):
            for file in files:
                caminho_arquivo = Path(root) / file
                if caminho_arquivo.suffix == ".txt":  # Melhor forma de verificar extensão
                    print(f"Compactando: {file}")
                    zip.write(caminho_arquivo, file)


def listar_arquivos():
    """Lista os arquivos dentro do ZIP."""
    with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
        print("\nArquivos no ZIP:")
        for arquivo in zip.namelist():
            print(arquivo)


def descompactar():
    """Extrai todos os arquivos do ZIP."""
    with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
        zip.extractall(CAMINHO_DESCOMPACTADO)
        print(f"Arquivos extraídos para {CAMINHO_DESCOMPACTADO}")


# Executa a compactação
compactar_txt()

# Pergunta ao usuário o que deseja fazer
resposta = input(
    '\nGostaria de descompactar (d) ou apenas listar (l) os arquivos zipados? ').strip().lower()

if resposta == "d":
    descompactar()
elif resposta == "l":
    listar_arquivos()
else:
    print("Opção inválida. Tente novamente.")


'''
Principais Melhorias
✅ Código modularizado – Criamos funções para compactar, listar e descompactar.
✅ Melhor verificação da extensão – Usamos .suffix do Path ao invés de os.path.splitext().
✅ Melhor manipulação de entradas do usuário – .strip().lower() evita problemas com espaços e letras maiúsculas.

Agora o código está mais legível, reutilizável e robusto! O que achou dessa versão? 😃🚀
'''
