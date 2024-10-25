# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

'''
Na agregação, uma classe contém outra como parte de sua composição, 
mas os objetos podem existir independentemente. 
É um tipo de associação mais forte, onde uma classe "tem" outra, 
mas essa relação não implica dependência total de existência entre elas.
'''
class Carrinho:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos): #* serve pra empacotar varios produtos ao msm tempo
        # for produto in produtos: 
        #     self._produtos.append(produto) pode usar assim ou:
        # self._produtos.extend(produtos) #OU AINDA:
        self._produtos += produtos
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()

p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20.00)
# print(p1.nome)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())

''' PASSO A PASSO: 
PRIMEIRO criamos um construtor do carrinho.  == > carrinho = Carrinho()
SEGUNDO: criamos um construtor para os produtos ==>  p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20.00)
TERCEIRO: inserimos os produtos p1, p2, na lista self._produtos do carrinho.
QUARTO: Agora podemos ter acesso atraves do self._produtos aos atributos da classe Produto. 
QUINTO: ao listar os produtos, chamamos produtos.nome, produto.preco, para listar os produtos do carrinho.
SEXTO: no total, usamos uma list comprehension que chama o p.preco, que é o preco de cada produto e soma o total dos precos.

Resumo, ao inserir os variaveis com construtores do PRODUTO na lista do carrinho, consegue-se ter acesso
aos atributos e funcoes da outra classe (Produto)


'''