"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('luiz') #___iter___

# print(next(texto))# print(texto.__next__()) # l
# print(next(texto))# print(texto.__next__()) # u
# print(next(texto))# print(texto.__next__()) # i
# print(next(texto))# print(texto.__next__()) # z
# print(next(texto))# print(texto.__next__()) # error StopIteration

'''
Isso é vc criando um metodo, vc diz para o python
que quer iterar a palavra luiz, e qd usa o NEXT
cada vez ele vai pra outra letra seguinte.
'''
#for letra in texto ( como o for funciona );
texto = 'Jonathan' # iteravel
# iterador = iter(texto) # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

#ISSO QUE FOI FEITO ACIMA É A MSM COISA QUE:

for letra in texto:
    print(letra)