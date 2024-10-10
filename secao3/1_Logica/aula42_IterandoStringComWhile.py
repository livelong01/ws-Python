frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'.lower()

# ver qual letra mais se repetiu. 
##############ESSA FOI A MINHA VERSAO###########
# i = 0
# letra = ''
# while i < len(frase):

#     if frase[i] not in letra:
#         letra += frase[i]
#     i += 1

# j = 0
# x = 0

# while j < len(letra):

#     if frase.count(letra[j]) > x:
#         x = frase.count(letra[j])
#         maior = letra[j]
#     j += 1

# print (f'O {maior=} aparece {x} vezes')

###########VERSAO DO PROFESSOR ###########

i= 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)
    
    if apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_que_apareceu_mais_vezes = letra_atual
    
    i += 1

print('A letra que apareceu mais vezes foi o "' 
      f'{letra_que_apareceu_mais_vezes}" que apareceu '
      f'{apareceu_mais_vezes} x')

    





