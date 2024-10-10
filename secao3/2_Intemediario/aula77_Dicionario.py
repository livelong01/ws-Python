# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = { #fORMA MAIS USADA PARA CRIAR DICT!
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# pessoa = dict(nome = 'Jonathan', sobrenome = 'Alonso') # FORMA MENOS USADA  de criar dict.
# print(pessoa, type(pessoa))
print(pessoa['nome']) # o vs code te da opcao do q vc quer acessar.
print()
for chave in pessoa:
    print(chave, pessoa[chave]) # sai bem organizado. Apesar de dict n ser iteravel.
''' RESULTADO DO FOR:
nome Luiz Otávio
sobrenome Miranda
idade 18
altura 1.8
endereços [{'rua': 'tal tal', 'número': 123}, {'rua': 'outra rua', 'número': 321}]
'''