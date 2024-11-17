'''
Exercício 1: Decorador de Classe - Logger de Métodos
Crie um decorador de classe que registra cada chamada 
de método da classe, exibindo o nome do método e os 
argumentos com os quais ele foi chamado.
'''

# def log_methods(cls):
#     # Itera sobre todos os atributos da classe
#     for attr_name, attr_value in cls.__dict__.items():
#         if callable(attr_value):  # Se o atributo for um método
#             original_method = attr_value

#             def wrapper(*args, **kwargs):
#                 print(f"Chamando {attr_name} com argumentos {args} e {kwargs}")
#                 return original_method(*args, **kwargs)

#             setattr(cls, attr_name, wrapper)
#     return cls

# @log_methods
# class MinhaClasse:
#     def metodo_1(self, x):
#         return x * 2

#     def metodo_2(self, y):
#         return y + 3

# # Teste
# obj = MinhaClasse()
# print(obj.metodo_1(5))
# print(obj.metodo_2(7))

'''
Exercício 2: Decorador de Classe - Adicionar Propriedade
Escreva um decorador de classe que adicione uma 
propriedade chamada descricao a todas as instâncias 
da classe. Essa propriedade deve ser gerada com base 
nos atributos da classe.
'''

# def add_descricao(cls):
#     @property
#     def descricao(self):
#         return f"{self.__class__.__name__}: {self.nome}, {self.idade} anos"
#     cls.descricao = descricao # subs a antiga funcao com a nova descricao.
#     return cls

# @add_descricao
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# @add_descricao
# class Estudante:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# # Teste
# pessoa = Pessoa("Jonathan", 30)
# print(pessoa.descricao)
# estudante = Estudante("Luna", 0)
# print(estudante.descricao)

'''
Exercício 3: Adicionar __repr__ Fora da Classe
Crie uma função __repr__ fora da classe e
 adicione-a à classe dinamicamente.
'''
def repr_function(self): #funcao criada fora da classe
    return f"{self.__class__.__name__}(nome={self.nome}, idade={self.idade})"

# Adicionando a função __repr__ à classe Animal
def adc_repr(cls):
    cls.__repr__ = repr_function  #REPASSA PRA CLASSE
    return cls

@adc_repr #DECORA A CLASSE COM A FUNCAO QUE ADC REPR
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Teste
animal = Animal("Muchacho", 4)
# print(repr(animal)) #nao precisa do repr
print(animal) #agora ele tem uma representacao em string

