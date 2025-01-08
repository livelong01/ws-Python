'''Crie um script que:

Leia um arquivo JSON contendo uma lista de produtos com nome, preco e 
quantidade.
Calcule o valor total de cada produto (preco * quantidade).
Adicione um novo campo valor_total para cada produto.
Salve os dados atualizados em um novo arquivo JSON.
Dica: Utilize json.load para ler o arquivo e json.dump para salvar os dados 
atualizados.

Boa sorte! 🚀~
'''
import os
import json
NOME_ARQUIVO = 'produtos.json'
CAMINHO_ABS_ARQUIVO = os.path.abspath(  # retorna caminho desde raiz "c:"
    os.path.join(  # vai unir dois textos/caminho
        # __file__ é o caminho ate o arquivo que estamos editando
        # dirname seleciona apenas o diretorio e ignora o nome do arquivo
        os.path.dirname(__file__), NOME_ARQUIVO))

with open(CAMINHO_ABS_ARQUIVO, 'r') as arquivo:
    produtos_json = json.load(arquivo)
    print(produtos_json)


for produto in produtos_json:
    total = produto['preco']*produto['quantidade']
    produto['valor_total'] = total
    print(produto)


NOME_ARQUIVO2_ATUALIZADO = 'produtos_atualizados.json'
CAMINHO_ABS_ARQUIVO_ATUALIZADO = os.path.abspath(  # retorna caminho desde
    # raiz "c:"
    os.path.join(  # vai unir dois textos/caminho
        # __file__ é o caminho ate o arquivo que estamos editando
        # dirname seleciona apenas o diretorio e ignora o nome do arquivo
        os.path.dirname(__file__), NOME_ARQUIVO2_ATUALIZADO))

with open(CAMINHO_ABS_ARQUIVO_ATUALIZADO, 'w') as arquivo:
    json.dump(produtos_json, arquivo, ensure_ascii=False, indent=2)
