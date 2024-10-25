# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial




class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__privated = 'Isso é private'

    def metodo_publico(self):
        print(self.__privated)
        self.__metodo_private()
        return 'metodo publico'
    
    def _metodo_protegido(self): # uso interno da classe.
        return '_metodo_protected'

    def __metodo_private(self): # uso interno da classe.
        print('__metodo private')
        return '_metodo_private'
    

f = Foo()
# print(f.public)
print(f.metodo_publico())
# print(f._protected)
# print(f.__metodo_private) # n consegue acessar
print(f._Foo__metodo_private()) #consegue acessar, mas n se deve fazer isso!