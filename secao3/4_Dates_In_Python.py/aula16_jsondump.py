# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
# from pprint import pprint  # PREATY PRINT (PRINT BONITO)
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


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
movie: Movie = json.loads(string_json)  # CARREGA OS DADOS DE JSON PARA PYTHON
# pprint(movie, width=40)
# print(type(movie))
# print(movie['title'])
# print(movie['characters'][0])
# print(movie['characters'][0])
# apos fazer a funcao e dizer que o movie é do tipo Movie,
# print(movie['year'] + 10)

# vc consegue selecionar coisas no dict, por ex: budget, characteres, etc.

# carrega os dados de python para json
# print(json.dumps(movie, ensure_ascii=False, indent=2))  # corrige os acentos
json_string = json.dumps(movie, ensure_ascii=False, indent=2)
print(json_string)
