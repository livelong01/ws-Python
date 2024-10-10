"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf_padrao = "746.824.890-70"

cpf_padrao_1 = cpf_padrao[:11]
calculo_cpf_1 = 0
decrescente_1 = 10
for digito in cpf_padrao_1:
    if digito.isdigit():
        calculo_cpf_1 += int(digito) * decrescente_1
        decrescente_1 -= 1
calculo_cpf_1 = (calculo_cpf_1 * 10) % 11

novo_digito = calculo_cpf_1 if calculo_cpf_1 < 9 else 0


cpf_padrao_2 = cpf_padrao_1 + str(novo_digito)
calculo_cpf_2 = 0
decrescente_2 = 11
for digito in cpf_padrao_2:
    if digito.isdigit():
        calculo_cpf_2 += int(digito) * decrescente_2
        decrescente_2 -= 1

calculo_cpf_2 = (calculo_cpf_2 * 10) % 11

novo_digito_2 = calculo_cpf_2 if calculo_cpf_2 < 9 else 0

cpf_gerado = f'{cpf_padrao_1}-{novo_digito}{novo_digito_2}'

if cpf_gerado == cpf_padrao:
    print(f'O cpf {cpf_padrao} é valido!')
else: 
    print(f'O cpf é invalido!')


