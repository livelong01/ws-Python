# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [3,1,3,7,0,8,6,4,3267,5,7,75,265]
# lista.sort(reverse=True) #ele altera direto na lista.
#com o reverse true ele inverte do maior para menor.
# lista.sort() # ele n consegue ordenar DICT.

'''
Para resolver o problema de ordenacao em dict
vc passa para o python uma funcao (lambda), que 
ordena da forma q vc quer, uma funcao pequena 
de uma linha.
'''
# def ordena(item):
#     return item['sobrenome'] # vai ordenar pela chave nome, ex: ana, bruno, carvalho...etc

# lista.sort(key=ordena) # a ky vc passa a funcao, que vc quer usar.
#uma maneira de fazr isso, sem criar uma funcao... é usando a lambda.

# lista.sort(key=lambda item: item['nome'])

# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()

# l1 = sorted(lista, key=lambda item: item['nome']) #faz uma COPIA e ordena, diferente do sort q só ordena sua propria lista.
# l2 = sorted(lista, key=lambda item: item['sobrenome'])# ele faz uma ordenacao RASA, ou seja, n entra dentro de lista dentro de lista.

# exibir(l1)
# exibir(l2)

'''
No caso, tem q por key = lambda (para indicar q é a funcao, item (a variavel recebida), item['nome'], o que vai retornar.)
'''

# for item in lista:
#     print(item)

nomeros = [
    {'x': 1, 'y': 1},
    {'x': 3, 'y': 7},
    {'x': 2, 'y': 9},
    {'x': 7, 'y': 9},
    {'x': 4, 'y': 6},
]

nomeros.sort(key = lambda number:number['x'])

for x in nomeros:
    print(x)