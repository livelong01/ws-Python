"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""
# def texto(x, y, sep= '-'):
#     print(x,sep,y, sep= '')

# texto('Eu te', 'amo')

'''
Assim como ao chamaar a funcao, se vc der um valor padrao ao parametro, 
os seguintes precisarao ter valores padrao tmb.
ex CERTO: def soma(x, y= None, z = None)-> OK
ex ERRADO: def soma(x, y= None, z)-> ERROR
'''
def soma(x, y, z = None): # por o valor padrao de z = 0. Daí n dá mais erro e vc n é OBRIGADO  a usar z.
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(7 , 8, 0) # x=7 y=8 15 | Como z = 0, falsy, ele entra direto no ELSE e n executa o cod certo.

'''
Agora usando o com o valor padrao "NONE" voce pode fazer o if com is not None
e saber se a pessoa pois "zero" no valor de z. Resultado : "x=7 y=8 z=0 15"
'''
