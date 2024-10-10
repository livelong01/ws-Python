def soma( x, y):
    return x + y

def multiplica ( x, y):
    return x * y

def criar_funcao(funcao, *args):
    def primeiro_argumento(x):
        return funcao (x, *args)
    return primeiro_argumento

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
print(criar_funcao(soma, 5)(10)) # pode fazer assim TAMBEM!