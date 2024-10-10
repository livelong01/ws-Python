# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('I will docorate you')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'Your result was {resultado}')
        print('ok now you have been decorated')
        return resultado
    return interna
#A FUNCAO ACIMA, É A FUNCAO DECORADORA!

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param must be a string")



inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)