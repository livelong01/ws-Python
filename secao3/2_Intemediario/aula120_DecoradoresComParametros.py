#Decoradores com parametros:
def fabrica_de_decoradores(a=None,b=None,c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Paramentros do decorador, ', a,b,c)
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

# def blablabla(a, b, c):
#     print(a,b,c)
#     return decoradora

# '''
# fazendo desse jeito, com o @funcao(paramentros,c,d) vc executa a funcao e de bonus decora a funcao que vc queria. 2 em 1!
# '''
# @blablabla(1,2,3)



@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    print(soma.__name__)
    return x + y


multiplica = fabrica_de_decoradores()(lambda x, y: x * y) # cria funcao com uma decoradora.

dez_mais_cinco = soma (10, 5)
dez_vezes_cinco = multiplica(10,5)
print(dez_mais_cinco)
print(dez_vezes_cinco)