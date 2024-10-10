# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'c1' : 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# d2 = d1 # para itens mutaveis ele apenas aponta para d1 (n copia!)

# d2 ['c1'] = 1000
# print(d1) # D1 MUDOU! {'c1': 1000, 'c2': 2}

'''
Se vc quiser copiar de verdade, nao apenas
apontar. Tem que usar .copy()
'''

d2 = d1.copy()
d2 ['c1'] = 1100

# print(d1) #{'c1': 1, 'c2': 2} #porem isso é uma copia rasa e traz problemas.
# print(d2)#{'c1': 1100, 'c2': 2} Altera apenas em 1!

# '''
# Ele copia apenas os itens imutaveis, porem se tiver uma lista (um subnivel), 
# ele n copia, apenas aponta! Por isso se chama "copia rasa" (Shallow copy)
# '''
# d2['l1'][1] = 999 #Alterando a lista, no indice 1. apenas de d2.........

# print(d1) #{'c1': 1, 'c2': 2, 'l1': [0, 999, 2]}
# print(d2) #{'c1': 1100, 'c2': 2, 'l1': [0, 999, 2]} 

'''
Ambas as listas foram alteradas, a copia n funciona bem pra subniveis.
PARA solucionar isso, basta usar o "import copy" e usar o deepcopy
'''
d2 = copy.deepcopy(d1) #DEEPCOPY acessa a todos SUBNIVEIS.
d2['l1'][1] = 999 


print(d1) #{'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
print(d2) #{'c1': 1, 'c2': 2, 'l1': [0, 999, 2]} #  Agora so uma foi alterada.

