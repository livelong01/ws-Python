"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

==========================
lista_soma = [2,4,6,8]
"""
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

#USANDO O ZIP E LIST COMPREHENSION 
def sumlist(lista1, lista2):
    resultado = [ valor1 + valor2 
                 for valor1, valor2 in zip(lista1, lista2)]
    return resultado

print(sumlist(lista_a, lista_b))

#USANDO O ZIP_LONGEST E LIST COMPREHENSION 
from itertools import zip_longest

def sumlist2(lista1, lista2):
    resultado = [ valor1 + valor2 
                 for valor1, valor2 in zip_longest(lista1, lista2, fillvalue = 0)]
    return resultado

print(sumlist2(lista_a, lista_b))

#USANDO FORÇA BRUTA! MIN , len e for.

def sumlist3(lista1, lista2):
    resultado = []
    menor = min(len(lista1), len(lista2))
    for indice in range(menor):
        resultado.append(lista1[indice] + lista2[indice])
    return resultado

print(sumlist3(lista_a, lista_b))

