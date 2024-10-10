# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena',1 ,2 ,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, c , *_, ap,  u = lista # u = ultimo
print(a, c) #Maria 1
print(a, u, ap) #Maria Eduarda 3 #qualquer ordem tmb!
print(ap) # ap = antipenultimo R: 3

for nome in lista:
    print(nome, end = ' ') #Maria Helena 1 2 3 Eduarda

print(lista) #['Maria', 'Helena', 1, 2, 3, 'Eduarda']
print(*lista) #Maria Helena 1 2 3 Eduarda

'''
fazendo com * voce tem o mesmo efeito do for
só que sem PULAR  a linha, por isso ele pos end = ' ' espaço
'''
print(*string)# A B C D separa por espaço, mas pode modificar.
print(*tupla) #Python é legal
