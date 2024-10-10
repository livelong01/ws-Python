'''
tipo tupla - uma lista IMUTAVEL!
'''

_,_, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)

'''
Se vc n for mudar a lista, nao precisar altera-la, basta vc 
criar uma tupla, ela é mais eficiente, que a lista.
'''
nomes = 'Maria', 'Helena', 'Luiz' #tupla, n usa colchetes
# nomes[1] = 'jorge'
print(nomes) #ERRO: 'tuple' object does not support item assignment
#TUPLAS SAO IMUTAVEIS, POR ISSO N DA PRA USAR ISSO.
print(nomes[-1]) # para visualizacao funciona igual a lista.

#Normalmente, para criar tuplas, se usa (PARENTESES). EX:

nomes = ('Maria', 'joao', 'jorge') #tupla criada!
#pode converter a lista em tupla::
nome1 = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nome1)
nomes = list(nomes) # pode converter tupla para lista tmb.