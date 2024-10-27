'''
Exercício Proposto
Crie uma classe Livro (com o atributo titulo).👍
Crie uma classe Autor (com o atributo nome).👍
Crie uma classe Editora (com o atributo nome).👍
Faça a ligação entre Livro e Autor. 👍
Observação: Um autor pode escrever vários livros. 
Faça a ligação entre Livro e Editora.👍
Observação: Uma editora pode publicar vários livros.
Exiba o título do livro, o nome do autor e o nome da editora na tela.

'''

class Livro:
    def __init__(self, nome):
        self.nome = nome
        self._autor = None
        self._editora = None
    
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = valor
    
    @property
    def editora(self):
        return self._editora
    @editora.setter
    def editora(self, valor):
        self._editora = valor

class Autor: 
    def __init__(self, nome):
        self.nome = nome

class Editora:
    def __init__(self, nome):
        self.nome = nome

#'Rebecca Yarros'
#'George R.R. Martin'
game_of_thrones = Livro('Game of Thrones') #criar um objeto.
grrm = Autor('George R.R. Martin') #criar outro do autor
gcl = Editora('Grupo Companhia das Letras') # criar outro para editora
game_of_thrones.autor = grrm  #atribuir o objeto do autor ao init do livro
game_of_thrones.editora = gcl #atribuir o objeto da editora ao init do livro

print(game_of_thrones.nome,'/', game_of_thrones.autor.nome,'/', game_of_thrones.editora.nome) #agora tudo esta PRONTO!

sangue_fogo = Livro('Sangue & Fogo')
sangue_fogo.autor = grrm
suma = Editora('SUMA')
sangue_fogo.editora = suma

print(sangue_fogo.nome,'/', sangue_fogo.autor.nome,'/', sangue_fogo.editora.nome)

quarta_asa = Livro('Quarta Asa')
rebeca_yarros = Autor('Rebecca Yarros')
planeta_minotauro = Editora('Planeta Minotauro')
quarta_asa.autor = rebeca_yarros
quarta_asa.editora = planeta_minotauro

print(quarta_asa.nome,'/', quarta_asa.autor.nome,'/',  quarta_asa.editora.nome)





