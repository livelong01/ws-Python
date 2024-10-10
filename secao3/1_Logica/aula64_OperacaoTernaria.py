"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# print('Valor' if True else 'Outro valor') #Valor
# print('Valor' if False else 'Outro valor') #Outro valor

# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)

digito = 10
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito >= 9 else digito
print(novo_digito)

'''Recapitulando: 
<valor se verdadeiro> if <condicao> else <valor se falso>
'''
print('valor' if False else 'outro valor' if False else 'fim')

'''
da pra fazer infinitamente, mesmo nao sendo recomendado,
falta de legibilidade! 
Funciona igual: 
print('valor se verdadeiro de 1ª' if False else 'valor se a 2ª cond for verdadeira' if False else 'valor se todas forem falsas.')
'''