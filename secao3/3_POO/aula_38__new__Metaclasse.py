'''
A metaclass ela cria uma instancia que é classe Pessoa,
depois pessoa cria uma instancia, que é objeto, nesse caso
p1.
Nao tem nada a ver com herança, é instancia!
'''
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


class Pessoa(metaclass = Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome) -> None:
        print('Meu INIT')
        self.nome = nome
    
    # def falar(self):
    #     print('falando...')

p1 = Pessoa('Luiz')
print(p1.attr) # se vc criar um atrb na metaclasse, todas as classes instnaciadas
# por ela tambem terao esse atributo, assim vc pode personalizar sua metaclass.
print(Pessoa.attr)
print(p1)
