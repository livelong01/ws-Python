#filter é um filtro funcional.
def print_inter(iterator):
    print(*list(iterator), sep= '\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [ #COM LIST COMPREHENSION
#     produto
#     for produto in produtos
#     if produto['preco'] > 10
# ]

#outra forma! COM FUNCOES ORIGINAIS DO PYTHON (filter)
# novos_produtos = filter(
#     lambda p: p['preco'] > 10,
#     produtos
# )
# outra forma, nomeando funcao (SEM LAMBDA)
def filtrar_preco(produto):
    return produto['preco'] > 10

novos_produtos = filter( #funcao criada para filtrar
    filtrar_preco,
    produtos
)

print_inter(produtos)
print_inter(novos_produtos)