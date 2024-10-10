'''
Exercicio
exiba os indices da lista
0 maria
1 helena
2 luiz 
'''


lista = ['Maria', 'Helena', 'Luiz']

lista.append('Jonathan')
indices = range(len(lista))

for indice in indices:
    print(indice ,lista[indice])
