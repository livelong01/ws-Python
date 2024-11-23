from typing import Any


def meru_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__ (msc, Pessoa, bases, dct):
        print('MetaClass NEW')
        cls = super().__new__(msc, Pessoa, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meru_repr

        if 'falar' not in cls.__dict__ or \
            not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente Falar!')
        return cls
    def __call__(cls, *args ,**kwargs):
        instancia = super().__call__(*args, **kwargs)
        print(instancia.__dict__)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o atrt nome')    

        return instancia


class Pessoa(metaclass = Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome) -> None:
        print('Meu INIT')
        # self.nome = nome
    
    def falar(self):
        print('falando...')

p1 = Pessoa('Luiz')
print(p1.attr) # se vc criar um atrb na metaclasse, todas as classes instnaciadas
# por ela tambem terao esse atributo, assim vc pode personalizar sua metaclass.
print(Pessoa.attr)
print(p1)