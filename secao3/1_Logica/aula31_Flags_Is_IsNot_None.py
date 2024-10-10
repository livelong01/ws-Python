'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou nao é (tipo, valor, identidade)
id = Identidade
'''

# v1 = "a"
# v2 = "b"
# print(id(v1))
# print(id(v2))

condicao = False


# if condicao:
#     passou_no_if = True 
#     '''
#     O problema de deixar a criacao da variavel
#     dentro do if, é que ela for falsa e n for criada
#     vai dar erro no print a seguir. Pq ela n vai existir!
#     '''
#     print("faça algo")
# else:
#     print("nao faça algo")

# print(passou_no_if)

passou_no_if = None
if condicao:
    passou_no_if = True
    print("faça algo")
else:
    print("nao faça algo")

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

'''
Verificar se algo é "ALGUMA COISA" ou nao.
vc pode usar o "is" e "is not", respectivamente.
EXEMPLO: 
'''
numero = 34
print(numero is not 34) #false
print(numero is 34) #true