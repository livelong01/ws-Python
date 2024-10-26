
# class Carro:
#     def __init__(self, nome, motor, fabricante):
#         self.nome = nome
#         self.motor = motor
#         self.fabricante = fabricante
    
#     def exibir_carro(self):
#         print(self.nome, self.motor, self.fabricante)
        
# class Motor:
#     def __init__(self, nome):
#         self.nome = nome
#         self.carros = []
    
#     def inserir_carros(self, carro):
#         self.carros.append(carro)

#     def exibir_carros(self):
#         for carro in self.carros:
#             print(carro.nome, carro.motor, carro.fabricante)

# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome
#         self.carros = [] 

#     def inserir_carros(self, carro):
#         self.carros.append(carro)

# chevrolet = Fabricante('Chevrolet')
# ferrari = Fabricante('Ferrari')

# motor_v1 = Motor('V1')
# motor_v2 = Motor('V2')



# corsa = Carro('corsa',motor_v1.nome, chevrolet.nome)
# ferrari_488 = Carro('Ferrari 488', motor_v2.nome, ferrari.nome)
# onix = Carro('Onix', motor_v2.nome, chevrolet.nome)

# motor_v1.inserir_carros(corsa)
# motor_v2.inserir_carros(ferrari_488)
# motor_v2.inserir_carros(onix)

# chevrolet.inserir_carros(corsa)
# ferrari.inserir_carros(ferrari_488)
# chevrolet.inserir_carros(onix)

# corsa.exibir_carro()
# ferrari_488.exibir_carro()
# onix.exibir_carro()

# motor_v1.exibir_carros()
# motor_v2.exibir_carros()

###########  RESOLUCAO DO PROFESSOR  #############

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_v1 = Motor('V1')
fusca.fabricante = volkswagen
fusca.motor = motor_v1

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

fiat_uno = Carro('Uno')
volkswagen = Fabricante('Fiat')
motor_v1 = Motor('V1')
fiat_uno.fabricante = volkswagen
fiat_uno.motor = motor_v1

print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus_uno = Carro('Focus Titanium 2.0')
volkswagen = Fabricante('Ford')
motor_v2 = Motor('V2')
focus_uno.fabricante = volkswagen
focus_uno.motor = motor_v2

print(focus_uno.nome, focus_uno.fabricante.nome, focus_uno.motor.nome)

gol = Carro('Gol')
volkswagen = Fabricante('Volkswagen')
motor_v1 = Motor('V1')
gol.fabricante = volkswagen
gol.motor = motor_v1

print(gol.nome, gol.fabricante.nome, gol.motor.nome)