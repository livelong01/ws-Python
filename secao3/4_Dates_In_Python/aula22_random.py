# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
# import time

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
# r_range = random.randrange(10, 20, 2) #pula de 2 em 2, sempre par.
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# r_int = random.randint(10, 20) #10-20 SAO INCLUSOS!
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)  # embaralhar uma lista
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# k = tamanho do sample (trecho da lista)
novos_nomes = random.sample(nomes, k=2)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)  # choices pode reperir o msm valor
# ex: ['Joana', 'Joana', 'Joana'] ou ['Helena', 'Helena', 'Joana']

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))  # pega um nome da lista sorteando.
# bom pra usar em sorteios.
