'''
Crie uma classe chamada ContaBancaria com um atributo privado __saldo. 
Implemente métodos getter e setter para esse atributo utilizando a função property. 
O setter deve garantir que o saldo nunca seja negativo.

Instruções:

O método getter deve retornar o valor atual do saldo.
O método setter deve permitir alterar o saldo, mas se o valor fornecido for negativo, deve exibir uma mensagem de erro e não alterar o saldo.
Teste o comportamento da classe, criando uma conta e tentando definir valores válidos e inválidos para o saldo.
'''

class ContaBancaria:
    def __init__(self, saldo = 0):
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if  valor < 0:
            raise ValueError('Valores negativos não sao aceitos.')
        self._saldo = valor

conta = ContaBancaria(100)
print(conta.saldo)  # Deve mostrar 100

conta.saldo = 200
print(conta.saldo)  # Deve mostrar 200

# conta.saldo = -50  # Deve exibir mensagem de erro

################################## EXERCICIO 2 #########################################

'''
Crie uma classe chamada Termometro com um atributo privado __temperatura representando a temperatura em Celsius. 
Implemente métodos getter e setter para esse atributo, onde o setter converte Fahrenheit para Celsius ao definir a temperatura.

Instruções:

O método getter deve retornar a temperatura atual em Celsius.
O método setter deve aceitar a temperatura em Fahrenheit, convertê-la para Celsius e armazená-la.
Teste a classe convertendo algumas temperaturas.
Fórmula de conversão de Fahrenheit para Celsius:
'''

class Termometer:
    def __init__(self, temperatura_c = 0):
        self._temperatura_c =  temperatura_c
    
    @property
    def temperatura_c(self):
        return self._temperatura_c
    
    @temperatura_c.setter
    def temperatura_c(self, valor):
        self._temperatura_c = (valor - 32) * 5/9

termometer = Termometer() #CONSTUTOR. #ele inicializa sem valor, ja que n precisa por valor inicial.
termometer.temperatura_c = 98.6
print(f"Temperatura em Celsius: {termometer.temperatura_c:.2f}°C")
termometer.temperatura_c = 80
print(f"Temperatura em Celsius: {termometer.temperatura_c:.2f}°C")

