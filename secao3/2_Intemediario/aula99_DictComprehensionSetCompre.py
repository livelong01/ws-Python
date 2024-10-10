#Dictionary Comprehension e set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritorio',
}

# print(produto.items())

# for chave, valor in produto.items():
#     print(chave, valor)

dc ={
    chave: valor.upper()
    if isinstance(valor, str) else valor #isinstance é um verificador, se for STR ele retorna verdadeiro. 
    # if isinstance(valor, (float, int)) else valor.upper #isinstance pode receber tupla de valores ex: int e float
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
# dc = { #TRANSFORMAR LISTA EM DICT. SÓ FUNCIONA SE A LISTA TIVER AS CARACTERISTICAS DE UM DICT
#     chave: valor 
#     for chave, valor in lista
# }
# print(dc)


##OU 

# print(dict(lista)) # usando o conversor dict ..

#---------------agora set conprehension-------------

s1 = {2 ** i for i in range(10)} #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# s2 = set(range(10)) # da no mesmo q no de cima. {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1)

#da pra usar o conjuto tmb, ele eleva o 2 para cada i no for no range (10)