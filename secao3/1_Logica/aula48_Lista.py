"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#         +01234
#         -54321

string = 'ABCDE' # CARACTERES (len)
# lista = list('') # jeito antigo!
# print(lista, type(lista))
# print(bool(lista)) # false qd vazia e true qd cheia.

##############  INDICE  ##############
#----------0----1------2--------3-----4--------itens
#--------'-5'-'-4'---'-3'-----'-2'--'-1'--------itens
lista = ['ola', 2, 'falcaooo', 1.8, ['a']] #Nova forma, mais compacta.

print(lista[2].upper(), type(lista[2]))
lista[2]= 56 #pode subs por qqt tipo.
print(lista)
