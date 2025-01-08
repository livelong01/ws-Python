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
