# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(a, b, /, x, y):
    print(a + y + x + b)

# soma(1,2)
# soma(y = 1, x = 2) #nao consegue passar funcao nomeada, 
# a barra la em cima bloqueia chamada de funcao nomeada,
# para que seja sempre compativel e n de erro no futuro.

soma(1 ,2 , 3, y = 3) #argumentos DEPOIS da barra, podem ser noemado, so os ANTES que nao.


def soma2(a, b, *args):
    print(args)
    print(a+b)

soma2(1,2, 'qualquer', 'coisa')
'''
O que for usado (A,B) vao ser somados, o restante vai pra uma tupla como no exemplo acima.
O args suga todos os argumentos que nao foram uteis e junta eles em uma tupla.
resposta: 

('qualquer', 'coisa')
3
'''

def soma3(a, b, *, c):
    print(a+b + c )

# soma3(1,2, 3) #DA ERRO, pq tudo dps do asteristico TEM que ser POSICIONAL, ou seja, 
# tem que ser chamado com nome! exemplo: LIMITA A QTD de argumentos e n suga o q n foi usado.
soma3(1,2, c = 3)
# 6

soma3(1,b = 2, c = 3) # entretanto se eu chamar o 'b', funciona e n era o que queriamos.

# pra funcionar com apenas o c precisando ser chamado, temos q por o limitador novamente.


def soma4(a, b, /, *, c):
    print(a + b + c )

# soma4(1, b= 2, c= 3) #erro: TypeError: soma4() got some positional-only arguments passed as keyword arguments: 'b'

soma4(1,2, c= 3) # assim funciona! E VC OBRIGA O 'C' A SER CHAMADO!
#---------------------------------------------

def soma5(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c )

soma5(1,2, c = 3, nome = 'teste')
# assim ele aceita todos os argumentos 'nomeados'  e SUGA para o kwargs
