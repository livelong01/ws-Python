"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
'''
x minusculo gera um hexad minusculo e o X o contrario.
'''
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500,1500)) 
# se vc por %08 o numero vai ter 8 casas a frente do hexadecimal.