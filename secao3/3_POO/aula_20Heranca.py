# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:

    cpf = 'cpf Pessoa'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):  #por entre parenteses a outra classe, "EXTEND" a outra classe, ou seja, HERDA dela os atributos.
    def falar_nome_classe(self):
        print('Nem sai da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'

c1 = Cliente('Jonathan', 'Marques')
a1 = Aluno('Luna', 'Alonso')

print(c1.nome, c1.sobrenome)
c1.falar_nome_classe()
print(a1.nome, a1.sobrenome)
a1.falar_nome_classe()
print(a1.cpf)
print(c1.cpf)
# help(Cliente)

'''
Method resolution order:
 |      Cliente
 |      Pessoa
 |      builtins.object

 Primeiro o python entra em cliente, se ele encontrar o metodo la
 use de la mesmo. Caso n encontre ele segue para Pessoa se encontrar usa de la ,
 caso n encontre, ele vai pra builtins.object e encontra la.
 Essa ordem é importante para entender A HERANÇA.

 TENTE USAR NO MAX 3 LEVEIS "SEUS" excluindo o builtins.object. 
 Senao o codigo fica extremamente complexo E atrapalha outros desenvolvedores
 que forem usar seu codigo. DEBUGGER RUIM

'''