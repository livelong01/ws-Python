caminho_arquivo = 'C:\\temp\\'
caminho_arquivo += 'CONFIGURAR GIT.txt'


with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    for linha in arquivo.readlines():
        print(linha, end= '')

        #FUNCIONOU!