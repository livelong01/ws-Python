'''
args - Argumentos nao nomeados
* - * (empacotamento e desempacotamento)
###Lembre-te de desempacotamento.
'''

# x , y, *resto = 1, 2 , 3, 4
# print( x, y, resto)

# def soma( x, y):
#     return x + y

def soma(*args): #*args é utilizado para passar muitos argumentos Nao nomeados.
    # args = list(args)
    # print(args, type(args))
    total = 0
    for numero in args:
        total += numero 
    return total

soma_1_2_3 = soma (1,2,3)
print(soma_1_2_3)
soma_4_5_6 = soma (4,5,6)
print(soma_4_5_6)

#EXISTE UMA FUNCAO Q JA FAZ ISSO: 
print(sum((4,5,6))) # pra funcionar tem q por entre parenteses ( como uma tupla ou lista. (colchetes))
#outra forma é por os numeros numa variavle ( que da no mesmo de criar uma tupla/lista)
numeros = 4,5,6
print(sum(numeros))

#entretanto, na nossa funcao criada:
# print(soma(numeros)) # dá erro.
# isso acontece, pq ele empacota o q ja foi empacotado! 
# COMO CORRIGIR ISSO?!
print(soma(*numeros)) # o '*' desempacota e assim se torna apenas uma tupla.
#OUTRO EXEMPLO: 
print(numeros) # (4, 5, 6) empacotado
print(*numeros) # 4 5 6 desempacotado
