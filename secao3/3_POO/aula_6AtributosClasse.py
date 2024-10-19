#Atributos de Classe:
# ANO_ATUAL = 2024
class Pessoa:
    ano_atual = 2024 #ATRIBUTO

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #USA O ATRIBUTO COMO REFERENCIA
        # return self.ano_atual - self.idade #USA A INSTANCIA COMO REFERENCIA.



p1 =  Pessoa('Jonathan', 33)
p2 = Pessoa('Tatiane', 29)
# Pessoa.ano_atual = 1
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())