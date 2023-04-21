# Para formatar string e ter texto com numeros decimais etc.
nome = 'Jonathan Alonso'
altura = 1.78
peso = 75.6
imc = peso / (altura**2)

print(nome, ' tem ', altura,
       ' de altura, pesa ', peso, 
       'quilos e seu IMC é ',imc)

print()
##OUTRA FORMA DE FORMATAR

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc: .2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print()

# PODE USAR A VIRGULA PARA FORMATAR DINHEIRO
salario = 18000.56
linha_1 = f'eu recebo {salario: ,.2f} reais'
print(linha_1)


