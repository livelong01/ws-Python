'''
Retorno de valores das funcoes (Return)
'''

# variavel = print('Luiz') #Luiz
# print(variavel)# None é o return da funcao

# def soma(x, y):
#     print(x+y)
    

# variavel = soma(1 ,2) 
# variavel = int ('1')
# print(variavel)

'''
Existem dois tipos de funcoes: 
1) Aquelas que servem apenas para executar
funcoes. Ex; print, etc.
2) Aquelas que retornam algum valor. Ex: int()
'''
# def soma(x, y):
#     print('Olha')
#     print('Isso') # antes do return executa
#     print('Aqui')
#     return x + y
#     print(x+y) # nunca processa nada dps do return
# #antes era print(x+y e n funcionou. Retornava None.)

   
# soma1 = soma(2,2)
# soma2 = soma(3,3)

# print(soma1 + soma2) # da erro, pq None + None é erro. 
# por isso nesse caso, a funcao deve retornar algo. 
#Para que se possa atribuir o return a uma variavel.


def soma(x, y):
    if x > 10:
        return 10, 20
    return x + y # n preciso colocar o else, pq ao chegar no 1ª return, a funcao termina.

soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma1)
print(soma2)
print(soma(11, 2))