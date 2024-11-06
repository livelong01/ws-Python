'''
Crie uma classe base chamada Animal com um método falar() 
que não faz nada (utilize pass ou raise NotImplementedError). 
Depois, crie duas subclasses chamadas Cachorro e Gato, 
cada uma implementando o método falar() para retornar 
uma frase que o respectivo animal "diria" (por exemplo, 
"Au au" para Cachorro e "Miau" para Gato).

No final, crie uma função que recebe uma lista de objetos Animal e 
chama o método falar() para cada um deles.
'''
from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#     def falar():
#         raise NotImplementedError

# class Cachorro(Animal):
    
#     def falar(self):
#         print('Au Au!')

# class Gato(Animal):

#     def falar(self):
#         print('Miauuu!')  

# def sons_de_animais(animais:Animal):  
#     for animal in animais:
#         animal.falar()

# muchacho = Gato()
# pretinha = Cachorro()
# animais = [muchacho, pretinha] #crie a lista antes
# sons_de_animais(animais)

#################### EXERCICIO 2 ###################

'''
Crie uma classe Forma com um método area() abstrato 
(use raise NotImplementedError). Depois, crie duas subclasses: 
Quadrado e Círculo.

Cada subclasse deve implementar o método area() de acordo com a 
fórmula apropriada:

Área do quadrado: lado^2
Área do círculo: π * raio^2
No final, crie uma função que receba uma lista de objetos Forma e 
retorne a área total de todas as formas da lista.
'''
import math
class Forma(ABC):
    @abstractmethod
    def area():
        raise NotImplementedError

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)
    

def soma_area(formas):
    total_area = 0
    for forma in formas:
        total_area += forma.area()
    return total_area

q1 = Quadrado(4)
c1 = Circulo(3)
q2 = Quadrado(2)
areas_lista = [q1, q2, c1]
print(soma_area(areas_lista))