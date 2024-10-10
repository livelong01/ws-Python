# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
def print_inter(iterator):
    print(*list(iterator), sep='\n') #usa o list, pq o resultado de combinatiosn é um iterator
    print()

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
pessoas = ['Joao', 'Joana', 'Luiz', 'leticia']

camisas = [
    ['preta', 'branca'], 
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodao', 'poliester']
]

#combinacao: /SEM REPETICOES.
print_inter(combinations(pessoas, 2)) # nomes em grupos de 2 
print_inter(combinations(pessoas, 3)) # nomes em grupos de 3 

#permutacao: /COM REPETICOES
print_inter(permutations(pessoas, 2)) #nomes em grupos de 2
print_inter(permutations(pessoas, 3)) #nomes em grupos de 3

#PRODUTO: /PLANO CARTESIANO
print_inter(product(*camisas)) 
''' COMBINA AS DUAS LISTAS UMA DENTOR DA OUTRA.
('preta', 'p')
('preta', 'm')
('branca', 'p')
('branca', 'm')
'''


