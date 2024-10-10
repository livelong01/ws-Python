'''
se eu criar um modulo na pasta que quero importar
o modolo chamado: '__init__', exatamente assim.
eu faço com que o python seja enganado e ele 
faz com que a PASTA(PAGKAGE) seja tratado como
um MODULO. exemplo:::


'''

from aula112_package import soma, fala_oi


# print(aula112_package.dobra(5))
print(fala_oi())
print(soma(3, 2))