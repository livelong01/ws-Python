# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# def divide(n, d):
#     try :
#         return n/d
#     except ZeroDivisionError:
#         print('........')
#         raise #relança o erro. redundante as vezes.

# print(divide(8, 0))
def nao_aceito_zero(x):
    if x == 0:
        raise ZeroDivisionError ('Voce esta tentando dividir por zero')
    return True

def deve_ser_int_ou_float(x):
    tipo_x = type(x)
    if not isinstance(x, (float, int)):
        raise TypeError(
            f'"{x}"deve ser int ou float.'
            f' "{tipo_x.__name__}" enviado.')
    

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n/d


print(divide(8, 'a'))

'''
RAISE :
serve pra vc modificar os erros existentes e chamar eles alterando a
mensagens PADRAO que eles tem. Com isso vc pode personalizar e mostrar
a msg que vc quiser. Isso ajuda o VC do futuro ou pessoas que irao
usar o seu codigo.
'''


