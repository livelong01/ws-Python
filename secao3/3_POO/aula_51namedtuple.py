# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple

from typing import NamedTuple
# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR PADRAO', 'NAIPE PADRAO'])
# as_espadas = Carta('A', '♠')
# as_copas = Carta(naipe='♥')

# print(as_espadas._asdict())  # converte em dicionario, muito util!

# print(as_espadas)
# print(as_espadas.naipe)
# print(as_espadas[0])
# print(as_espadas.valor)  # consegue ver os fields
# print(as_espadas._field_defaults)  # os defaults
# print(as_copas)  # os defaults
# print(as_copas._field_defaults)  # os defaults

# for valor in as_espadas:
#     print(valor)

# usando uma classe no lugar de tuple:


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


as_espadas = Carta('A', '♠')
as_copas = Carta(naipe='♥')
print(as_copas)
print(as_espadas)  # tudo funciona perfeitamente. (Tanto class, qt tupla!)

# Definindo uma namedtuple para


class Cartas(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Lista de valores e naipes
valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['♠', '♥', '♦', '♣']

# Criando um baralho
baralho = [Carta(valor, naipe) for valor in valores for naipe in naipes]

# Exibindo algumas cartas
for carta in baralho[:5]:  # Primeiras 5 cartas
    print(carta)
