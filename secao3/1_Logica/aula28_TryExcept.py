"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
# print(123)
# print(456)
# int("a")

numero_str = input("Vou dobrar o numero digitado: ")

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print("Isso nao é um número")

try:
    print("alou!")
    numero_float = float(numero_str)
    print("FLOAT", numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print("Isso nao é um numero")

'''
A grande diferença do if/else e do try/except é que
o try tenta rodar o codigo e qd há um erro ele executa
o codigo ate o momento onde o erro ocorreu. 
Ao contrario do if else, que verifica o erro no inicio
e se encontrar nem executa parte alguma do codigo.
O try te ajuda a identificar o local do erro e com isso
corrigi-lo de forma mais EFICAZ!
'''