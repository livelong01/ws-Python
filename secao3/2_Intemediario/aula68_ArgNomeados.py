"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
'''
Quando vc n da valor, caso x, y vazios, esses argumentos se indentificam, como
arumentos posicionais, pois dependem dos valores dados ao ser chamados. 
'''
def soma(x, y, z):
    #definicao da funcao 
    print(f'{x=} {y=} {z=}', '|', 'x + y + z= ', x + y+ z)

# soma(1, 2) # x=1  y=2 | x + y =  3 
# soma(2, 1) # x=2  y=1 | x + y =  3 (INVERTEU)

'''
Usando os parametros nomeados, voce pode adc os parametros na ordem que vc
quiser!
EXEMPLO: 
'''
# soma(y = 2, x = 1) # x=1  y=2 | x + y =  3 |Agora corrigiu!
soma(y = 2, z= 3, x = 1) 
soma(1 , 2 , 3) # x=1 y=2 z=3 | x + y + z=  6
soma
soma( 1, y = 2 , z = 5) # mesma coisa que: Se nomrar um argumento, os seguintes precisarao ser nomeados tmb.
print( 1, 2, 3, sep = '-') #chamar o sep, é nomear a variavel q vc quer dar valor.

