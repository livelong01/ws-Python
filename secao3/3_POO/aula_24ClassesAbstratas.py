# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.
from abc import ABC, ABCMeta, abstractmethod

# class Log(metaclass=ABCMeta): # TANTO ESSA
#     ...

'''
Para uma classe ser ABSTRATA, ela precisa de duas coisas:
1) herdar de ABC OU ABCMETA
2) Ter pelo menos UMA classe Abstrata em seu escopo

ou seja, uma classe sem corpo, com "..." apos sua chamada.
e com o @abstractmethod EM CIMA.

'''

class Log(ABC): #QUANTO ESSA SAO DUAS FORMAS DE TRANSF. UMA CLASSE EM ABSTRACT
   
    @abstractmethod
    def _log(self, msg): ... #metodo abstrato.
        
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        self._log(f'Sucess: {msg}')

class LogPrintMixin(Log): 
    def _log(self, msg): #para usa o metodo, vc obrigatoriamente tem que implementa-lo em toda subclasse que for usar
        print(f'{msg} ({self.__class__.__name__})') #SENAO DA ERRO.

# l = Log() # agora n consegue mais instanciar ela. dá erro: TypeError: Can't instantiate abstract class Log with abstract method _log
 # agora so pode INSTANCIAR as filhas dela. LogPrintMixin, que HERDAM dela.
l = LogPrintMixin()
l.log_error('oi')