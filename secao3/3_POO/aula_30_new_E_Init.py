# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe


class A:
    def __new__(cls, *args, **kwargs): # usou args e kwargs pra poder por qts argumentos quiser no INIT
        print('Antes de criar a instancia')
        # return super().__new__(cls) #O codigo volta a funcionar
        instancia = super().__new__(cls) # A partir desse momento é que se cria a instnacia e o init pode ser usado
        print('Depois')
        instancia.x = 121
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'
    
a = A(1) #é a msm coisa que: (por de baixo dos panos)
# a = object.__new__(A)
# a.__init__()
print(a)
print(a.x)