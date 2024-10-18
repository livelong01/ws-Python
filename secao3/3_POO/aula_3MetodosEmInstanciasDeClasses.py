#Metodos em instnacias de Classes Python-
#Hard Coded - algo que foi escrito diretamente no codigo base.
#A classe é o MOLDE(sem dados) 
#E a instancia da classe pode gerar varias instnacias.
#Na classe o self é a propria instnacia.

class Carro:
    def __init__(self, nome):
        # self.nome = 'fusca' #Hard Coded (NAO QUEREMOS ISSO.)
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

# string = 'jon'
# print(string.upper())

fusca = Carro('fusca')
# fusca.nome = 'Fusca'
print(fusca.nome)
fusca.acelerar()


celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()