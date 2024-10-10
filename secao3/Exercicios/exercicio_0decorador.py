def fabrica_de_decoradores(a=0,b=0,c=0):
    def fabrica_de_funcoes(func):

        def aninhada(*args, **kwargs):
            res = func(*args, **kwargs)
            return res + a + b + c
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,3,4)
def soma(x,y):
    return x + y


dez_mais_cinco = soma(10, 5)

print(dez_mais_cinco)
