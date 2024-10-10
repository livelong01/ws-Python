# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
abreviacao = ['BA', 'SP', 'MG', 'RJ']


# def decorador(func):
#     def interna(*args,**kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return interna


# @decorador
def zipper(lista_1, lista_2):
    lista_junta = [(lista1, lista2) for lista1, lista2 in zip(lista_1, lista_2)] #listcomprehension
    # for lista1, lista2 in zip(lista_1, lista_2):
    #     lista_junta.append((lista1, lista2)) 
    return lista_junta
   
print(zipper(cidades, abreviacao))


#RESPOSTA DO PROFESSOR!

# def zipper( lista1, lista2):
#    internvalo_maximo = min(len(lista1), len(lista2)) # escolhe o menor entre duas
#    return [
#        (lista1[i], lista2[i]) for i in range(internvalo_maximo)
#    ]
# print(zipper(cidades, abreviacao))
print(list(zip(cidades, abreviacao))) # outra forma usando zip!

from itertools import zip_longest

print(list(zip_longest(cidades, abreviacao, fillvalue= 'Sem cidade')))
#[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'), (None, 'RJ')]

'''#Fillvalue = substitui o valor NoNE POR o q vc quiser.
ELA VAI PELA LISTA MAIS LONGA!
'''






