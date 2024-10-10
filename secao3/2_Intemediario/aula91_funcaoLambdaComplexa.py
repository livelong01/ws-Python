def executa (funcao, *args):
    return funcao(*args)



# def soma(x,y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# print(
#     executa(
#         lambda x, y : x + y, # funcao recebida pelo executa
#         2,3 #5 # argumentos recebidos pelo executa.
#     ),
#     executa(soma, 2, 3), #5
#     soma(2,3)# 5
# )

#AGORA A CRIAR MULTIPLICADO, MAIS DIFICIL
# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m : lambda n : n * m ,
    2 # tenho q dar o valor de m = 2 (multiplicador)
)

print(duplica(10)) # aqui damos o valor de "n", DAí 10 x 2 = 20!

print(
    executa(
        lambda *args: sum(args), #outra forma de fazer a funcao labda (mais facil de ver e entender.)
        1,2,3,4,5,6,7
    )
)