"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero_01 = 0.1
numero_02 = 0.7
numero_03 = numero_01 + numero_02 # 0.79999 imprecisao!
print(numero_03)
print(f'{numero_03:.2f}')

'''
3 maneiras de formatar e corrigir o problema da imprecisao:
1) Usando o format:
'''
print(f'{numero_03:.2f}') #0.80 #resultado é em STRING

#2) USANDO O ROUND.
print(type(round(numero_03, 3)))  #0.8 retorna FLOAT!

#3)usando modulo de decimal.
#Nesse caso, vc tem q por em forma de string, entre ''
#assim ele converte corretamente.
import decimal

numero_01 = decimal.Decimal('0.1')
numero_02 = decimal.Decimal('0.7')
numero_03 = numero_01 + numero_02  
print(numero_03) ##0.8