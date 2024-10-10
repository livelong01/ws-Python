"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""


# def escopo (): # isso n executa, só se for chamada.
#     x = 1
#     print(x)
# escopo() # como nesse caso.

'''
Entretanto se vc definir o x antes da funcao, ela pode ser usada pela funcao.
exemplo: '''
# x = 1
# def escopo():
#     x = 10 # ESSE X n é igual ao outro x de cima... Aqui ele fica protegido.
#     def outra_funcao():
#         x = 11
#         y = 2
#         print(x, y)
#     outra_funcao()
#     print(x)

# print(x)
# escopo()
# print(x) # resposta 1. O x fora da funcao é 1 ainda.
# posso acessar a outra funcao dentro da funcao escopo, fora n consegue.

''' Resultado: 
1 # x = 1 lado de fora.
11 2 x = 11, x mais interno, com valor de 11.
10  , x intermediario com valor 10.
1 # x mais externo com valor 1 novamente.
'''

x = 1
def escopo():
    # global x # agora o x tera o valor de 10, pq ele é global nessa parte.
    x = 10 
    def outra_funcao():
        x = 11 # ele muda pra 11 enquanto em "outra_funcao" e dps volta a ser 10.
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x) # aqui ele será 1, primeira coisa a ser executada.
escopo() #apos usar a funcao, o x muda pra 10 pra sempre.
print(x) # aqui o valor dele do lado de fora é 10.
'''
1 # fora da funcao 
11 2
10
10
'''