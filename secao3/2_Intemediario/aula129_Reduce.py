# REDUCE - faz a reducao de um iteravel em um valor
# reduce: redebe um ITERAVEL e transforma em um VALOR.

from functools import reduce

def print_inter(iterator):
    print(*list(iterator), sep= '\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 105},
    {'nome': 'Produto 4', 'preco': 69},
]

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

#usando o reduce para TOTAL:
total = reduce(
    funcao_do_reduce,
    produtos,
    0 #valor inicial, como se fosse o "total =0", que criamos abaixo.
)
print(total)
#usando LAMBDA (MAIS FACIL)
total_Lambda = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)
print(total_Lambda)


#exemplo total:

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum(p['preco'] for p in produtos))