# json.dump e json.load com arquivos.
import json
import os

NOME_ARQUIVO = 'aula17.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(  # retorna caminho desde raiz "c:"
    os.path.join(  # vai unir dois textos/caminho
        # __file__ é o caminho ate o arquivo que estamos editando
        # dirname seleciona apenas o diretorio e ignora o nome do arquivo
        os.path.dirname(__file__), NOME_ARQUIVO)
)
# print(os.path.dirname(__file__))
# print(os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))

string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''
# vou converter a string em dict to pythhon usando o LOADS.
print(json.loads(string_json))
# agora vou copiar o resultado do prompt
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)


'''
Resumo da Aula: json.dump e json.load com Arquivos
O módulo json do Python é utilizado para trabalhar com arquivos e dados no
formato JSON (JavaScript Object Notation).
Ele permite a conversão entre objetos Python e JSON, um formato amplamente
usado para troca de dados entre sistemas.

Pontos Importantes
json.dumps e json.loads:

json.dumps: Converte um objeto Python (ex.: dict) em uma string JSON.
json.loads: Converte uma string JSON em um objeto Python.
Exemplo:

python
Copiar código
import json

string_json = '{"nome": "Jonathan", "idade": 30}'
dados = json.loads(string_json)
print(dados["nome"])  # Saída: Jonathan
json.dump e json.load:

json.dump: Salva um objeto Python em um arquivo no formato JSON.
json.load: Carrega dados de um arquivo JSON para um objeto Python.
Exemplo:

python
Copiar código
filme = {"nome": "Matrix", "ano": 1999, "genero": "Ficção"}
with open('filme.json', 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)
Trabalhando com caminhos absolutos:

os.path.abspath: Obtém o caminho absoluto.
os.path.dirname(__file__): Retorna o diretório do arquivo atual.
Esses métodos são úteis para garantir que o código funcione em diferentes
sistemas operacionais.

Formato JSON:

Baseado em pares chave-valor (key-value).
Pode conter objetos ({}), listas ([]), números, strings, booleanos e null
(equivalente a None em Python).
Exemplo de Uso Comum
Salvar configurações de um aplicativo:

python
Copiar código
configuracao = {"volume": 70, "tema": "escuro", "notificacoes": True}
with open('config.json', 'w') as arquivo:
    json.dump(configuracao, arquivo, indent=4)
Carregar e processar dados de uma API:

python
Copiar código
import requests

resposta = requests.get('https://api.exemplo.com/dados')
dados = json.loads(resposta.text)
print(dados["nome"])
Exportar resultados de análises para JSON:

python
Copiar código
resultados = {"media": 89.5, "desvio_padrao": 4.3}
with open('resultados.json', 'w') as arquivo:
    json.dump(resultados, arquivo, indent=2)
'''
