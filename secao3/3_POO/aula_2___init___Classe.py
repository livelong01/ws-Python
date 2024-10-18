class Pessoa:
    def __init__(self, nome, sobrenome): #criacao de metodo (MESMO JEITO QUE FUNCAO, mas como ta dentro da classe, se chama METODO.)
        self.nome = nome
        self.sobrenome = sobrenome 


p1 = Pessoa('Jonathan', 'Marques') #criando um novo objeto/instancia.
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otavio'

p2 = Pessoa('Luiz', 'Otavio')
# p2.nome = 'Jonathan'
# p2.sobrenome = 'Marques'

print(p1.nome) # atributos, nao se usa parenteses.
print(p1.sobrenome)  

print(p2.nome) 
print(p2.sobrenome)