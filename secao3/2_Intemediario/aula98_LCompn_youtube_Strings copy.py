#STRING E LIST COMPREHENSION

string = 'Otavio Miranda'
numero_de_letras = 1
# nova_string = ''.join([letra for letra in string]) #Join junta as letras na lista sem espaçamento ''
nova_string2 = '.'.join(
    [string[indice:indice + numero_de_letras]# pega do string[0,3]
    for indice in range(0, len(string), numero_de_letras)]) #pula de 3 em 3 o indice, assim da certo. n repete numeros.


print(nova_string2) #O.t.a.v.i.o. .M.i.r.a.n.d.a
