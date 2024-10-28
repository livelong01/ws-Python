# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    def quem_sou(self):
        print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C): # A ORDEM IMPORTA PARA O AUGORITIMO QUE VAI DAR A ORDEM
    ...

    # def quem_sou(self):
    #     print('D')

d = D()
d.quem_sou() #D
# comentando o metodo quem sou em D, quem ele ira atras agora? C OU B?
d.quem_sou() #B  || pq o B era o primeiro na herança multipla
# print(D.__mro__)
print(D.mro()) #ORDEM DE RESOLUCAO: D>B>C>A  (abaixo a ordem.)

#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
