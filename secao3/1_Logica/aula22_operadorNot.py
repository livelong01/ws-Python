# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

'''
No caso abaixo, quando tentei por apenas not bool("0"),
para inverter e enganar o codigo, para ele dizer que
eu n tinha digitado nada, nao funcionou, pq "0" em Srt
É CONSIDERADO VERDADEIRO. Entao tive que transformar
em "int" antes de passar para boolean e assim ele aceitar
como false e assim enganar o codigo, que transformou
com o not em verdadeiro e disse que n digitei nada 
xD kkk

'''

if not bool(int(senha)):
    print('voce nao digitou nada')
else: 
    print(senha)

'''

O not <<inverte>>, usa bolean, ou seja, senha com nenhum
argumento é false, porem o not a torna verdadeira 
e faz com que a condicao do if seja true e por isso
ele faz o print do texto.
'''

# usuario = 'carlos'
# password = '12345'
 
 
# nome = input('Digite seu usuario: ')
# senha = input('Digite a sua senha: ')
 
 
 
# if nome == usuario and senha == password:
#     print('Seja bem vindo ao sistema')
# elif not nome:
#     print('Digite seu usuario')
# elif not senha:
#     print('Digite sua senha')
# elif nome != usuario:
#     print('Usuario incorreto, por favor tente novamente')
# else:
#     print('Senha incorreta, por favor tente novamente')