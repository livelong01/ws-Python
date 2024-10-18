# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# string = 'luiz' #str
# print(string.upper())
# print(isinstance(string, str)) #str é uma classe.

# CriarBaseDeDados, por converncao se usa pascal case para criar nome de CLASSE.

class Pessoa:
    ...  #atributos -  dados dentro da classe.
         #metodos - algo que faça uma acao dentro da classe.
 
p1 = Pessoa() #criando um novo objeto/instancia.
p1.nome = 'Luiz'
p1.sobrenome = 'Otavio'

p2 = Pessoa()
p2.nome = 'Jonathan'
p2.sobrenome = 'Marques'

print(p1.nome) # atributos, nao se usa parenteses.
print(p1.sobrenome)  

print(p2.nome) 
print(p2.sobrenome)