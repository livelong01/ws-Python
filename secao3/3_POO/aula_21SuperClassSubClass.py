# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper() # ele ja faz automaticamente. a classe e o self abaixo.
#         # retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno
    
# string = MinhaString('Jonathan')
# print(string.upper())


class A:
    atributo_a = 'valor A'
    
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor B'    
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo) # repassa o atributo para o A. Só isso
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Ei, burlei o sistema!')

    def metodo(self):
        # super().metodo() # se deixar padrao, ele pega o super da classe atual. Mas vc pode por a classe acima e ele buscara pelo super da classe acima.
        super(B, self).metodo() # se deixar padrao, ele pega o super da classe atual. Mas vc pode por a classe acima e ele buscara pelo super da classe acima.
        print('C') # como nesse caso, pegando o super de B, vai buscar o A.

# print(C.mro()) # B #method Resolution Order ( pra saber a ordem de resolucao ) #<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>
# print(B.mro()) # A
# print(A.mro()) # Object
c = C('atributo', 'qualquer')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()