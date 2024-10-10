"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('joao')

lista_enumerada = enumerate(lista)
print(next(lista_enumerada)) #nao consigo ver se der print sem o next. (o next mostra o primeiro e assim por diante se vc repetir os prints.)
print(next(lista_enumerada)) #nao consigo ver se der print sem o next. (o next mostra o primeiro e assim por diante se vc repetir os prints.)
print(next(lista_enumerada)) #nao consigo ver se der print sem o next. (o next mostra o primeiro e assim por diante se vc repetir os prints.)
print(next(lista_enumerada)) #nao consigo ver se der print sem o next. (o next mostra o primeiro e assim por diante se vc repetir os prints.)

# o melhor jeito é: 

for item in lista_enumerada:
    print(item)
'''
(0, 'Maria')
(1, 'Helena')
(2, 'Luiz')
(3, 'joao')
    '''
'''
Apos o uso da lista, se eu fizer um novo for abaixo, nada acontecera
pois ja usei a lista. E o enumerate entende q n ha mais nada que mostrar
ja foi "consumida a lista e por isso nada aparece.
'''
# for item in lista_enumerada:
#     print(item)

'''
Nada acontece aqui ... Foram consumidas no for acima!
Uma forma de CONTORNAR isso é vc não por o "ENUMERATE" em
uma variavel e sim diretamente no FOR. EXEMPLO: 
'''
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)

''' RESULTADO: FUNCIONA!
(0, 'Maria')
(1, 'Helena')
(2, 'Luiz')
(3, 'joao')
(0, 'Maria')
(1, 'Helena')
(2, 'Luiz')
(3, 'joao')
(0, 'Maria')
(1, 'Helena')
(2, 'Luiz')
(3, 'joao')
(0, 'Maria')
(1, 'Helena')
(2, 'Luiz')
(3, 'joao')
'''

lista_enumerada = list(enumerate(lista))
print(lista_enumerada) #Uma forma de dar print é transf. o enumarate em lista/tupla.
#Resultado: [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'joao')]

for item in enumerate(lista):
    indice, nome = item #deu nome as variaveis dentro da lista.
    print(indice, nome) # mandou mostrar separadamente.
    '''Resultado: 
    0 Maria
    1 Helena
    2 Luiz
    3 joao
    '''

#Uma maneira do python facilitar o uso e simplificar o codg é usar os 
#nomes das variaveis dentro do for, dai ele usa como se fosse for em for.
#EXEMPLO: 
print('---------------')
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice]) #faz a mesma coisa, mas com o codg mais limpo.

#é a msm coisa que um FOR DENTRO DE OUTRO FOR: EXEMPLO: 
# for tupla_enumerada in enumerate(lista):
#     print('For da tupla:')
#     for valor in tupla_enumerada: 
#         print(f'\t{valor}') #\t é TAB. 
''' RESULTADO: 
        For da tupla:
        0
        Maria
        For da tupla:
        1
        Helena
        For da tupla:
        2
        Luiz
        For da tupla:
        3
        joao  

        Nao fica igual, mas o resultkado é parecido.       
'''

