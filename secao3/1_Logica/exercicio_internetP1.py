'''
Faça um Programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
 e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

tamanho_pintado = input('Qual o tamanho da area a ser pintada? ')
#1 litro - > 6 metros 
# lata de 18L e 3,6 L (80, 25 R$)
litros_necessarios = int(tamanho_pintado)/6 
lata_litros = 18
galao_litro = 3.6
preco_lata = 80
preco_galao = 25

resultado_lata = (litros_necessarios // lata_litros) + 1
resultado_galao = (litros_necessarios // galao_litro) + 1
resto_lata = litros_necessarios % lata_litros

resto_galao = (resto_lata // galao_litro) + 1




print(resultado_lata* 80 )
print(resultado_galao * 25 )
print(f'{(resultado_lata-1)} latas + {resto_galao} galoes, total R${(resultado_lata-1)* 80 + resto_galao*25}')




# if litros_necessarios // 18 
# print(f'Comprando apenas latas de 18 litros, voce precisará de {litros_necessarios}.')
