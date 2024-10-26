# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def __del__(self):
        print('APAGANDO', self.nome)  
    

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO', self.rua, self.numero)


       

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 5785)
##################
endereco_externo = Endereco('Av. saudade', 48545)
cliente1.inserir_endereco_externo(endereco_externo)

# print(cliente1.enderecos[0].rua)
# print(cliente1.enderecos[1].rua)
cliente1.listar_enderecos()

#VOU APAGAR A MARIA 
del cliente1 


print('##########Aqui termina meu codigo##########')

#A COMPOSICAO mescla os codigos das duas classes. 
'''
Como no exemplo acima, quando se apaga a maria, o endereco ligado a ela
fica sem onde apontar e por isso é apagado JUNTO. 
Isso acontece, pq na composicao o OBJETO é criado dentro da Classe. ´Como acontece
nesse trecho: 
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

O objeto Endereco(rua, numero) foi criado dentro da classe CLIENTE.
e isso os liga pra sempre.

CHATGPT: 
A composição é uma relação onde uma classe depende totalmente de 
outra para existir. Ou seja, uma classe contém outra como parte essencial, 
e se a classe "principal" for destruída, os objetos contidos também serão.
É uma dependência mais forte que a agregação.

'''