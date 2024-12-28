'''
Crie um script que:

Use os.walk para percorrer uma estrutura de diretórios especificada.
Conte e exiba a quantidade total de arquivos encontrados.
Mostre apenas os arquivos com a extensão .txt e seus respectivos caminhos
completos.
Teste com um diretório de exemplo que contenha subdiretórios e arquivos.
'''
import os

caminho = os.path.join('\\temp', 'ws-Python', 'treino')
print(caminho)
count = 0
for root, dirs, files in os.walk(caminho):
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        caminho, extensao = os.path.splitext(caminho_completo_arquivo)
        if extensao == '.txt':
            count += 1
            print('     ', count, 'Files: ', caminho_completo_arquivo)
print('Total txt files: ', count)
