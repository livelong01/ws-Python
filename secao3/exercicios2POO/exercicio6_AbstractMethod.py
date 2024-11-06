'''
Crie uma classe abstrata chamada FormaGeometrica com os seguintes 
métodos abstratos:
calcular_area: que deve retornar a área da forma geométrica.
calcular_perimetro: que deve retornar o perímetro da forma geométrica.
Em seguida, crie duas subclasses:
Circulo, que tem um atributo raio. Implemente os métodos para 
calcular a área e o perímetro de um círculo.
Retangulo, que tem atributos largura e altura. Implemente
os métodos para calcular a área e o perímetro de um retângulo.
Instancie ambas as classes e chame os métodos para verificar os resultados.
'''
from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self): ...
    @abstractmethod
    def calcular_perimetro(self): ...

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return (self.raio**2 * math.pi)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(FormaGeometrica):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def calcular_area(self):
        return (self.altura * self.largura)
    
    def calcular_perimetro(self):
        return 2*self.largura + 2*self.altura
    

c1 = Circulo(3)
c2 = Circulo(5)
r1 = Retangulo(4, 6)

# print(c1.calcular_area())
# print(c1.calcular_perimetro())

# print(c2.calcular_area())
# print(c2.calcular_perimetro())

# print(r1.calcular_area())
# print(r1.calcular_perimetro())

'''
Exercício 2: Sistema de Pagamento
Crie uma classe abstrata MetodoPagamento com um método abstrato processar_pagamento.
Crie as subclasses:
CartaoCredito, que pede número do cartão, data de validade e código de segurança.
BoletoBancario, que pede o código do boleto.
Implemente o método processar_pagamento para cada um, simulando uma mensagem diferente para cada tipo de pagamento.
Instancie cada uma das classes e chame processar_pagamento.
'''
# class MetodoPagamento(ABC):
#     @abstractmethod
#     def processar_pagamento(self):
#         pass

# class CartaoCredito(MetodoPagamento):
#     def __init__(self, card_number, valid, security_code):
#         self.card = card_number
#         self.valid = valid
#         self.security = security_code

#     def processar_pagamento(self):
#         return print('Pagamento com cartão Aprovado ✔')

# class BoletoBancario(MetodoPagamento):
#     def __init__(self, bill_code):
#         self.bill_code = bill_code
    
#     def processar_pagamento(self):
#         return print('Pagamento do Boleto Aprovado ✔')

# cartao1 = CartaoCredito(112, "12/09", 123)
# boleto1 = BoletoBancario(112459498489423)

# cartao1.processar_pagamento()
# boleto1.processar_pagamento()

  # ############# chat gpt: 

# Classe abstrata MetodoPagamento
class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

# Subclasse CartaoCredito
class CartaoCredito(MetodoPagamento):
    def __init__(self, numero_cartao, validade, codigo_seguranca):
        self.numero_cartao = numero_cartao
        self.validade = validade
        self.codigo_seguranca = codigo_seguranca

    def processar_pagamento(self, valor):
        # Simulação do processo de pagamento com cartão de crédito
        return f"Pagamento de {valor} processado com sucesso no cartão de crédito {self.numero_cartao}."

# Subclasse BoletoBancario
class BoletoBancario(MetodoPagamento):
    def __init__(self, codigo_boleto):
        self.codigo_boleto = codigo_boleto

    def processar_pagamento(self, valor):
        # Simulação do processo de pagamento com boleto bancário
        return f"Pagamento de {valor} processado com sucesso com o boleto bancário {self.codigo_boleto}."

# Testando as classes
cartao = CartaoCredito(numero_cartao="1234-5678-9012-3456", validade="12/25", codigo_seguranca="123")
boleto = BoletoBancario(codigo_boleto="987654321")

print(cartao.processar_pagamento(150.75))
print(boleto.processar_pagamento(150.75))      
