
l1= [1,2,3,4,5,6,6,7,8,9,10,1,2,56]
l2= [3,6,87,9,0,7,5,42,3,1,12]
'''Escreva uma função unir_listas(lista1, lista2) que recebe duas listas e retorna uma nova lista que contém todos os elementos únicos presentes em ambas as listas.
'''
# lista1 = [3, 1, 4, 5, 2]
# lista2 = [6, 5, 4, 8, 7]
# def unir_listas(lista1, lista2):
#     lista3 = list(set(lista1) | set(lista2)) #uniao
#     return lista3

# print(unir_listas(lista1,lista2))


'''União Simples de Listas:União com Elementos Repetidos: Crie uma função unir_com_repeticao(lista1, lista2) que une duas listas, permitindo que elementos repetidos sejam incluídos. Retorne a nova lista.'''

# def unir_com_repeticao(lista1, lista2):
#     lista3 = lista1 + lista2
#     return lista3

# print(unir_com_repeticao(l1, l2))

'''União e Ordenação: Implemente uma função unir_e_ordenar(lista1, lista2) que une duas listas, remove elementos duplicados e retorna uma lista ordenada.
'''

# def unir_e_ordenar(lista1, lista2):
#     # Usar set para unir as listas e remover duplicados
#     lista_unida = set(lista1) | set(lista2)
#     # Ordenar a lista resultante
#     lista_ordenada = sorted(lista_unida)
#     return lista_ordenada

# # Teste da função
# lista1 = [3, 1, 4, 5, 2]
# lista2 = [6, 5, 4, 8, 7]
# resultado = unir_e_ordenar(lista1, lista2)
# print(resultado)

'''
União de Listas de Números: Escreva uma função unir_numeros(lista1, lista2) que aceita duas listas de números e retorna uma lista contendo a união dos números que são maiores que 10.
'''
# lista1 = [5, 12, 7, 20, 11]
# lista2 = [15, 8, 20, 25, 5]
# def unir_numeros(lista1, lista2):
#     lista3 = list(set(lista1) | set(lista2))
#     return [valor for valor in lista3 
#             if valor > 10]

# print(unir_numeros(lista1, lista2))

'''União de Listas de Strings: Crie uma função unir_strings(lista1, lista2) 
    que aceita duas listas de strings e retorna uma lista que contém somente as strings que têm mais de 5 caracteres.
'''
# lista1 = ["casa", "automovel", "gato",'sol', "bicicleta"]
# lista2 = ["elefante", "sol", "computador",'gato', "caneta"]
# def unir_strings(lista1, lista2):
#     lista3 = lista1 + lista2
#     return [string for string in lista3
#             if len(string)>5]

# print(unir_strings(lista1, lista2))

'''Interseção antes da União: Escreva uma função unir_com_interseccao(lista1, lista2) 
que une duas listas, mas antes de unir, imprime os elementos que estão presentes em ambas as listas (interseção).
'''
# def unir_com_interseccao(lista1, lista2):
#     lista3 = set(lista1) & set(lista2)
#     print("Elementos em ambas as listas (interseção):", list(lista3)) 

#     lista4 = list(set(lista1) | set(lista2))
#     return lista4
# print(unir_com_interseccao(lista1, lista2))



'''União com Filtragem: Implemente uma função unir_filtrando(lista1, lista2, filtro)
 que une duas listas e filtra os elementos que não atendem a uma condição definida pela função filtro.
'''
# def unir_filtrando(lista1, lista2, filtro):
#     lista3 = lista1 + lista2
#     return [valor 
#             for valor in lista3
#             if valor > filtro]
# print(unir_filtrando(l1, l2, 10))


'''União de Listas em um Dicionário: Crie uma função unir_em_dicionario(lista1, lista2) que aceita duas listas e retorna um dicionário onde cada elemento da lista1 é uma chave e os elementos da lista2 são os valores correspondentes.
'''


'''Contagem de Elementos:Escreva uma função contar_elementos_unidos(lista1, lista2) que une duas listas e retorna um dicionário com a contagem de cada elemento na lista unida.
'''

'''União de Múltiplas Listas: Implemente uma função unir_multiplas(*listas) que aceita um número variável de listas e retorna a união de todas elas, garantindo que não haja elementos duplicados.'''


