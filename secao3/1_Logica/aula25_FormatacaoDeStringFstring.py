"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
''' ATENCAO!!!!!
Voce pode fazer repeticao de caracteres,
mas nao pode dar espaço e deve estar colado com o
":" e o ">" como no caso acima!
'''
x = "h"
print(f'{variavel:-<10}.')
print(f'{variavel:{x}^20}.') # ^ centraliza (dá para usar uma variavel na repeticao)
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')