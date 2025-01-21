# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr
random = secrets.SystemRandom()

# todas as letras, todos os numeros, todas as pontuacoes
# CRIADOR DE SENHAS FORTES
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=15)))


print(secrets.randbelow(100))
print(secrets.choice([10, 11, 100]))  # alearorio entre esses numeros


# ??????????????????ULTIMA AULA?????????????????????
# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)  # NAO FAZ NADA!

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)  # pula de 2 em 2, sempre par.
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)  # 10-20 SAO INCLUSOS!
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)  # embaralhar uma lista
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# k = tamanho do sample (trecho da lista)
novos_nomes = random.sample(nomes, k=2)
print(nomes)
print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)  # choices pode reperir o msm valor
# ex: ['Joana', 'Joana', 'Joana'] ou ['Helena', 'Helena', 'Joana']

# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nomes))  # pega um nome da lista sorteando.
# bom pra usar em sorteios.
