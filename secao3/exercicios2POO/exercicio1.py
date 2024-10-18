class Carro:
    def __init__(self, marca, modelo, ano, velocidade = 0):
         self.marca = marca
         self.modelo = modelo
         self.ano = ano
         self.velocidade = velocidade
    
    def acelerar(self):
        print(f'Acelerando para {self.velocidade + 5} km/h')
        self.velocidade += 5
    def frear(self):
        if self.velocidade != 0:
            self.velocidade -= 5
            print(f'Freando para {self.velocidade} km/h')
        else:
            print('O carro está parado')
        
        
    def informacoes(self):
        print(f'A marca do carro é {self.marca}\n, o modelo é {self.modelo}\n, o ano é {self.ano}\n a velocidade atual é {self.velocidade}km/h')


clio = Carro('renault', 'clio', 2000)
clio.informacoes()
clio.acelerar()
clio.acelerar()
clio.acelerar()
clio.frear()
clio.frear()
clio.frear()
clio.frear()
clio.informacoes()