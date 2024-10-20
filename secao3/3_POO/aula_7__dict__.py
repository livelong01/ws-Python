# __dict__ e vars para atributos de instancia

class Pessoa:
    ano_atual = 2024 #ATRIBUTO

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #USA O ATRIBUTO COMO REFERENCIA


p1 =  Pessoa('Jonathan', 33)
# p1.nome = 'Eita'
print(p1.nome)
# del p1.nome #apaga
# print(p1.nome)
print(p1.idade)
#-------------------
dados = {'nome' : 'Jonathan', 'idade' : 35}
p1 = Pessoa(**dados) #fazendo assim vc envia as informacoes para o objeto.

#---------------
#onde fica salvo os dados da instancia? para descobrir
#basta usar __dict__ no p1.

# print(p1.__dict__)
#ou
print(vars(p1))

#tmb pode criar atributos dentro do dict
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.outra )
# print(vars(p1))

# print(vars(p1))