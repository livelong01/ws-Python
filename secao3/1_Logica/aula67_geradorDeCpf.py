import random
import sys

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    cpf_padrao = nove_digitos

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

    cpf_gerado = f'{cpf_padrao_1[:3]}.{cpf_padrao_1[3:6]}.{cpf_padrao_1[6:]}-{novo_digito}{novo_digito_2}'
    print(cpf_gerado)