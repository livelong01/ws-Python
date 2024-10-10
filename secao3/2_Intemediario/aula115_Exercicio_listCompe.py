# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy
from dados import produtos, exibir



novos_produtos = copy.deepcopy(produtos) # copia profunda do dicionario

novos_produtos = [
    {**produto, 'preco' : f"{produto['preco']*1.1:.2f}"}
    for produto in novos_produtos
]

novos_produtos.sort(key=lambda nome:nome['nome'])
# print(*produtos, sep='\n')
print()
# exibir(novos_produtos)
#----------------------------------------------------------------------------
print()

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda nome:nome['nome'], reverse=True)
# exibir(produtos_ordenados_por_nome)

#---------------------------------------------------------------------------
print()
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda preco:preco['preco'])
# exibir(produtos_ordenados_por_preco)

print(*produtos, sep='\n')
print(10*'-')
print(*novos_produtos, sep='\n')
print(10*'-')
print(*produtos_ordenados_por_nome, sep='\n')
print(10*'-')
print(*produtos_ordenados_por_preco, sep='\n')
# exibir(produtos)
# print(10*'-')
# exibir(novos_produtos)
# print(10*'-')
# exibir(produtos_ordenados_por_nome)
# print(10*'-')
# exibir(produtos_ordenados_por_preco)