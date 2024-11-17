def meu_repr(self):
            class_name = self.__class__.__name__ 
            class_dict = self.__dict__ 
            class_repr = f'{class_name}({class_dict})' 
            return class_repr 

def adicionar_repr(cls):  
        cls.__repr__ = meu_repr #substitui a antiga funcao, com o repr adc.
        return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Voce esta em casa!' # AQUI VC pode criar if, etc. E ISSO VAI SER USADO NA CLASSE.
        return resultado
    return interno

@adicionar_repr 
class Time: 
    def __init__(self, nome):
        self.nome = nome 
    
@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    @meu_planeta #decoracao da funcao "meu planeta"
    def falar_nome(self):
        return f'O planeta é {self.nome}'
    

brasil = Time('Brasil')
portugal =Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(portugal)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())