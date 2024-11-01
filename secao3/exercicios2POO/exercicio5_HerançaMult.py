'''
1. Exercício Fácil com Herança Múltipla
Crie um sistema que simule veículos aéreos e terrestres.

Crie uma classe Veiculo com um método mover(), que exiba uma mensagem genérica de movimento.
Crie as classes Terrestre e Aereo, ambas herdam de Veiculo, e implementam mover() 
para exibir uma mensagem sobre como se movem (por exemplo, rodando ou voando).
Crie uma classe CarroVoador que herda de Terrestre e Aereo. Ele deve ter o método mover() 
que exibe uma mensagem sobre como um carro voador se move, combinando as habilidades de Terrestre e Aereo.
Objetivo: Implementar herança múltipla e criar uma funcionalidade única para a classe CarroVoador.

'''

# class Veiculo:
#     def __init__(self, nome):
#         self._nome = nome

#     def mover(self):
#         msg = f' O {self._nome} está se movendo.' 
#         print(msg)

# class Terrestre(Veiculo):
#     def mover(self):
#         msg = f'O {self._nome} está rodando.'
#         print(msg)


# class Aereo(Veiculo):
#     def mover(self):
#         msg = f'O {self._nome} está voando.'
#         print(msg)

# class CarroVoador(Aereo, Terrestre):
#     def mover(self, local):
#         if local == 'terra':
#             Terrestre(self._nome).mover()
#         else:
#             Aereo(self._nome).mover()



        

# carro = Terrestre('Carro')
# carro.mover()
# aviao = Aereo('Aviao')
# aviao.mover()
# carro_voador = CarroVoador('Carro Voador')
# carro_voador.mover('terra')
# carro_voador.mover('Ar')

#=============================================================================
'''
2. Exercício Médio com Herança Múltipla e Composição
Crie um sistema de monitoramento de animais.

Crie uma classe Animal com um método emitir_som(), que será genérico (por exemplo, uma mensagem básica).
Crie as classes Mamifero e Ave que herdam de Animal. Cada um deve implementar seu próprio emitir_som(), 
com sons específicos (exemplo: mamífero ruge, ave canta).
Crie uma classe PassaroEstranho que herda de Mamifero e Ave, e em emitir_som(), faça com que combine sons dos dois.
Crie uma classe Habitat que possui uma composição com Animal e um método descrever_habitat() 
que descreve o ambiente do animal, usando o método emitir_som().
Objetivo: Demonstrar o uso de herança múltipla e composição para criar uma interação entre classes.
'''

# class Animal:
#     def emitir_som(self):
#         print('O animal faz um som')

# class Mamifero(Animal):
#     def emitir_som(self):
#         print('O mamifero Ruge')

# class Ave(Animal):
#     def emitir_som(self):
#         print('A ave Canta')

# class PassaroEstranho(Ave, Mamifero):
#     def emitir_som(self):
#         print('O passaro Estranho Ruge e Canta.')

# class Habitat:
#     def __init__(self, animal):
#         self.animal = animal

#     def descrever_habitat(self):
#         print("Este é o habitat do animal:")
#         self.animal.emitir_som()
        
# passaro_estranho =PassaroEstranho()
# habitat = Habitat(passaro_estranho)
# habitat.descrever_habitat() # == PassaroEstranho().emitir_som() COMPOSICAO.

#===================================================================================================================================

'''
3. Exercício Difícil com Herança Múltipla, Composição e Getters e Setters
Crie um sistema de gerenciamento de funcionários para uma empresa que possui diferentes tipos de profissionais.

Crie uma classe Pessoa com atributos nome, idade, e métodos getters e setters para controlar o acesso a esses atributos.
Crie duas classes Engenheiro e Designer, ambas herdam de Pessoa, com um método trabalhar(). 
Cada classe deve implementar trabalhar() de forma única.
Crie uma classe Gerente que herda de Engenheiro e Designer, e que também possui um método liderar_projeto(). 
Use setters e getters na classe Gerente para controlar atributos de gerenciamento, como o número de projetos gerenciados.
Por fim, crie uma classe Departamento que contém uma lista de Pessoa (composição). 
Implemente um método adicionar_funcionario() para adicionar pessoas ao departamento e 
um mostrar_funcionarios() para listar os funcionários e suas funções.
Objetivo: Desenvolver um sistema que utilize herança múltipla, composição, 
getters e setters para criar e gerenciar uma hierarquia complexa de funcionários.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

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

class Engenheiro(Pessoa):
    def trabalhar(self):
        print(f'O {self._nome} trabalha nas obras')

class Desinger(Pessoa):
    def trabalhar(self):
        print(f'O {self._nome} trabalha no FIM das obras')

class Gerente(Engenheiro, Desinger):

    def __init__(self, nome, idade, projetos):
        super().__init__(nome, idade)
        self._projetos = projetos

    @property
    def projetos(self):
        return self._projetos
    @projetos.setter
    def projetos(self, numero):
        self._projetos = numero

    def liderar_projeto(self):
        print(f'{self._nome} é o gerente do projeto e lidera {self._projetos} projetos! UAu!')

class Departamento:
    def __init__(self):
        self.pessoal = []
    
    def adicionar_funcionario(self, pessoa):
        self.pessoal.append(pessoa)
    
    def mostrar_funcionarios(self):
            for funcionario in self.pessoal:
                print(f"Funcionário: {funcionario._nome} - Função: {type(funcionario).__name__}")

jonathan = Engenheiro('Jonathan', 33)
jonathan.idade = 36
tatiane = Desinger('Tatiane', 29)
tatiane.nome = 'Tatiana'
Luna = Gerente('Luna', 0, 5)
Luna.projetos = 6
Luna.liderar_projeto()

departamento = Departamento()
departamento.adicionar_funcionario(jonathan)
departamento.adicionar_funcionario(tatiane)
departamento.adicionar_funcionario(Luna)
print(jonathan.nome)
tatiane.trabalhar()
jonathan.trabalhar()

departamento.mostrar_funcionarios()








    
