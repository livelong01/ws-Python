# https://www.youtube.com/watch?v=4kPRm8D8Vx0
# 4 Automações com Python que Vão SALVAR Seu Tempo no Trabalho

# 2 - AUTOMACAO DE ARQUIVOS:
import os

'''
def organizar_arquivos():
    pasta_origem = 'C://Users/jonat/Downloads'
    pasta_destino = 'C://Users/jonat/Downloads/pdfs'
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    arquivos_pasta_atual = os.listdir(pasta_origem)

    for arquivo in arquivos_pasta_atual:
        if ".pdf" in arquivo:
            os.rename(arquivo, f'{pasta_destino}/{arquivo}')
        print(arquivo)
    print('Arquivos organizados com sucesso!')


organizar_arquivos()
'''

# OUTRA FORMA MAIS EFICIENTE!


def organizar_arquivos():
    pasta_origem = 'C://Users/jonat/Downloads'
    pasta_destino = 'C://Users/jonat/Downloads/IMG'

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    arquivos_pasta_origem = os.listdir(pasta_origem)

    for arquivo in arquivos_pasta_origem:
        if arquivo.endswith(".png"):
            caminho_origem = os.path.join(pasta_origem, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)
            os.rename(caminho_origem, caminho_destino)

    print('Arquivos organizados com sucesso!')


organizar_arquivos()
