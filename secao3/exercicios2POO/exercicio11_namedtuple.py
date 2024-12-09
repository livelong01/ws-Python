'''
Crie uma classe Pessoa utilizando NamedTuple com os atributos:

nome (tipo: str)
idade (tipo: int, valor padrão: 0)
cidade (tipo: str, valor padrão: "Desconhecida")
Depois:

Crie duas instâncias: uma com todos os valores preenchidos e outra usando 
os valores padrão.
Imprima os valores de cada campo das duas instâncias.
Converta a instância com valores preenchidos para um dicionário e exiba 
o resultado.

'''
from typing import NamedTuple


# class Pessoa(NamedTuple):
#     nome: str
#     idade: int = 0
#     cidade: str = 'Desconhecida'


# pessoa_desconhecida = Pessoa('Jorge')
# print(pessoa_desconhecida)

# pessoa_conhecida = Pessoa('Jonathan', 33, 'Espinho')
# print(pessoa_conhecida)

'''
Desafio Extra
Modifique o código para:

Exibir o valor de cada atributo individualmente para ambas as pessoas.
Converter a pessoa_conhecida em um dicionário usando _asdict().
Aqui está como ficaria:

python
Copiar código
# Exibindo atributos individuais
print(f"Nome: {pessoa_desconhecida.nome}, Idade: {pessoa_desconhecida.idade},
 Cidade: {pessoa_desconhecida.cidade}")
print(f"Nome: {pessoa_conhecida.nome}, Idade: {pessoa_conhecida.idade}, 
Cidade: {pessoa_conhecida.cidade}")

# Convertendo para dicionário
pessoa_dict = pessoa_conhecida._asdict()
print(pessoa_dict)  # {'nome': 'Jonathan', 'idade': 33, 'cidade': 'Espinho'}
Isso reforça o aprendizado e ainda mostra como a NamedTuple é prática! 🚀

'''


class Pessoa(NamedTuple):
    nome: str
    idade: int = 0
    cidade: str = 'Desconhecida'


pessoa_desconhecida = Pessoa('Jorge')
print(pessoa_desconhecida)

pessoa_conhecida = Pessoa('Jonathan', 33, 'Espinho')
print(pessoa_conhecida._asdict())

for valor in pessoa_conhecida:
    print(valor)

print(pessoa_conhecida.nome)
print(pessoa_conhecida.idade)
print(pessoa_conhecida.cidade)

print(pessoa_desconhecida.nome)
print(pessoa_desconhecida.idade)
print(pessoa_desconhecida.cidade)
