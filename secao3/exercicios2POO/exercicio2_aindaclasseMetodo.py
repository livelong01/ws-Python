'''
Exercício 2: Criando uma classe ContaBancaria
Crie uma classe chamada ContaBancaria com os seguintes atributos:

titular (string)
saldo (float, valor inicial 0)
A classe deve ter os seguintes métodos:

depositar(valor): adiciona o valor ao saldo.
sacar(valor): subtrai o valor do saldo, se houver saldo suficiente. Caso contrário, imprime "Saldo insuficiente".
consultar_saldo(): imprime o saldo atual.
Crie uma instância da classe e faça operações de depósito, saque e consulta de saldo.
'''

class ContaBancaria:
    def __init__(self, titular):
        self.titular =  titular
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor
    def consultar_saldo(self):
        print(f'Senhor {self.titular} \n seu Saldo atual é de:\n {self.saldo}')



nome_conta = input("Digite o nome do Titular da conta criada: ")
conta1 = ContaBancaria(nome_conta)

while True:
    conta1.depositar(float(input('Valor a depositar:  ')))
    conta1.sacar(float(input('Valor a sacar:  ')))
    conta1.consultar_saldo()
    

