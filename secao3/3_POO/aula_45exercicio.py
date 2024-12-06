"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

# from abc import ABC, abstractmethod

# class Conta(ABC):
#     def __init__(self, agencia, n_conta, saldo = 0):
#         self.agencia = agencia
#         self.n_conta = n_conta
#         self.saldo = saldo

#     @abstractmethod
#     def sacar(self, valor):
#         raise NotImplementedError('O metodo sacar precisa ser implementado!')
    
#     @abstractmethod
#     def saldo_atual(self):
#         raise NotImplementedError('O metodo saldo precisa ser implementado!')

# class Conta_corrente(Conta):
#     def __init__(self, agencia, n_conta, limite, saldo=0):
#         super().__init__(agencia, n_conta, saldo)
#         self.limite = limite

#     def sacar(self, valor):

#         total = self.saldo + self.limite
#         if valor > total:
#             print('Valor do saque excede o limite de crédito')
#         else:
#             self.saldo -= valor

#     def deposito(self, valor):
#         self.saldo += valor
#         print('Deposito realizado com sucesso.')
    
#     def saldo_atual(self):
#         print(f' Seu saldo atual é R$ {self.saldo}') 

# class Conta_poupanca(Conta):

#     def sacar(self, valor):

#         if valor > self.saldo:
#             print(f'Saldo insuficiente.')
#         else:
#             self.saldo -= valor
#             print('Saque efetuado com sucesso.')

#     def deposito(self, valor):
#         self.saldo += valor
#         print('Deposito realizado com sucesso.')

#     def saldo_atual(self):
#         print(f'Seu saldo atual é R$ {self.saldo}')

# #==================================================================================    
# class Pessoa(ABC):
#     def __init__(self, nome, idade):
#         self._nome = nome
#         self._idade = idade

#     @property
#     @abstractmethod    
#     def nome(self):
#         raise NotImplementedError('O metodo nome precisa ser implementado!')
    
#     @property
#     @abstractmethod 
#     def idade(self):
#         raise NotImplementedError('O metodo idade precisa ser implementado!')

# class Cliente(Pessoa):
#     def __init__(self, nome, idade):
#         super().__init__(nome, idade)
#         self._conta = []

#     @property
#     def nome(self):
#         return self._nome
    
#     @nome.setter
#     def nome(self, nome):
#         self._nome = nome

#     @property
#     def idade(self):
#         return self._idade
    
#     @idade.setter
#     def idade(self, idade ):
#         self._idade = idade
    
#     def inserir_contas(self, *conta):
#         self._conta += conta
    
#     def listar_contas(self):
#         for conta in self._conta:
#             print(f'Tipo de conta: {conta.__class__.__name__} \n',
#                    f'Agencia: {conta.agencia}\n',
#                    f'Número da conta: {conta.n_conta} \n',
#                    f'Saldo: {conta.saldo}' )
#             print()
#     def CC(self):
#         for conta in self._conta:
#             if conta.__class__.__name__ == 'Conta_corrente':
#                 return conta

#     def CP(self):
#         for conta in self._conta:
#             if conta.__class__.__name__ == 'Conta_poupanca':
#                 return conta
    
# #==================================================================================  

# class Banco:
#     def __init__(self, agencias = [] ):
#         self.clientes = []
#         self.contas = []
#         self.agencias = agencias
    
#     def inserir_clientes(self, *cliente):
#         self.clientes += cliente
    
#     def inserir_contas(self, *conta):
#         self.contas += conta
    
#     def autenticar(self, agencia, cliente, conta):
#         if agencia in self.agencias:
#             print('Agencia está OK')
#             if cliente in self.clientes:
#                 print('Cliente está OK')
#                 if conta in self.contas:
#                     print('Conta está OK')
#                     print('Saque permitido')
#                     return True
#                 else:
#                     print('Conta inexistente')
#             else:
#                 print('Cliente inexistente')
#         else: 
#             print('agencia Inexistente')
        

    
        

# '''
# * Checar se a agência é daquele banco
# * Checar se o cliente é daquele banco
# * Checar se a conta é daquele banco 
# '''


# #==================================================================================
# n = Conta_corrente('123', '0036', 1000)
# p = Conta_poupanca('123', '0012')

# p.deposito(500)
# p.sacar(0)
# p.saldo_atual()
# n.deposito(500)
# # n.sacar(1200)
# n.saldo_atual()

# joao = Cliente('Joao', 28)
# joao.inserir_contas(n, p)
# joao.listar_contas()
# joao.CP().sacar(109)


# bradesco = Banco(['123'])

# bradesco.inserir_clientes(joao)
# bradesco.inserir_contas(n, p)
# # bradesco.autenticar('123', joao, n)

# if bradesco.autenticar('123', joao, n):
#     for conta in joao._conta:
#         if conta.__class__.__name__ == 'Conta_corrente':
#             conta.sacar(100)
#             conta.saldo_atual()

# p.saldo_atual()



#000000000000000000000000 CHAT GPT METODO ===================================

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, banco, cliente, agencia, n_conta, saldo=0):
        self._banco = banco
        self._cliente = cliente
        self.agencia = agencia
        self.n_conta = n_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        raise NotImplementedError("O método sacar precisa ser implementado!")
    
    def autenticar(self):
        return self._banco.autenticar(self.agencia, self._cliente, self)
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")

    def saldo_atual(self):
        print(f"Seu saldo atual é R${self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, banco, cliente, agencia, n_conta, limite=1000, saldo=0):
        super().__init__(banco, cliente, agencia, n_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if not self.autenticar():
            print("Autenticação falhou. Saque não permitido.")
            return
        
        total = self.saldo + self.limite
        if valor > total:
            print("Saldo insuficiente (incluindo limite).")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not self.autenticar():
            print("Autenticação falhou. Saque não permitido.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

#==================================================================================    

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    @abstractmethod    
    def nome(self):
        raise NotImplementedError("O método nome precisa ser implementado!")
    
    @property
    @abstractmethod 
    def idade(self):
        raise NotImplementedError("O método idade precisa ser implementado!")

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._contas = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
    
    def inserir_contas(self, *conta):
        self._contas += conta
    
    def listar_contas(self):
        for conta in self._contas:
            print(f"Tipo de conta: {conta.__class__.__name__} \n",
                  f"Agência: {conta.agencia}\n",
                  f"Número da conta: {conta.n_conta}\n",
                  f"Saldo: R${conta.saldo}")
            print()

    def get_conta_corrente(self):
        for conta in self._contas:
            if isinstance(conta, ContaCorrente):
                return conta

    def get_conta_poupanca(self):
        for conta in self._contas:
            if isinstance(conta, ContaPoupanca):
                return conta

#==================================================================================  

class Banco:
    def __init__(self, agencias=None):
        if agencias is None:
            agencias = []
        self._clientes = []
        self._contas = []
        self._agencias = agencias
    
    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)
    
    def inserir_conta(self, conta):
        self._contas.append(conta)
    
    def autenticar(self, agencia, cliente, conta):
        if agencia not in self._agencias:
            print("Agência inexistente.")
            return False
        if cliente not in self._clientes:
            print("Cliente não encontrado.")
            return False
        if conta not in self._contas:
            print("Conta não encontrada.")
            return False
        print("Autenticação bem-sucedida.")
        return True

#==================================================================================

# Criando o banco
bradesco = Banco(["123"])

# Criando cliente
joao = Cliente("João", 30)

# Criando contas para o cliente
conta_corrente = ContaCorrente(bradesco, joao, "123", "001", limite=500, saldo=1000)
conta_poupanca = ContaPoupanca(bradesco, joao, "123", "002", saldo=2000)

# Associando contas ao cliente e adicionando ao banco
joao.inserir_contas(conta_corrente, conta_poupanca)
bradesco.inserir_cliente(joao)
bradesco.inserir_conta(conta_corrente)
bradesco.inserir_conta(conta_poupanca)

# Operações bancárias
print("\n--- Conta Corrente ---")
joao.get_conta_corrente().sacar(1200)
joao.get_conta_corrente().saldo_atual()

print("\n--- Conta Poupança ---")
joao.get_conta_poupanca().sacar(3000)
joao.get_conta_poupanca().saldo_atual()
