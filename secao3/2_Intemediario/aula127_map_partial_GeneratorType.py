from functools import partial
from types import GeneratorType
# map - para mapear dados
def print_inter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2) #2 cadas decimais

aumentar_dez_porcento = partial( #faz o closure automaticamente.
    aumentar_porcentagem,
    porcentagem = 1.1
)

# novos_produtos = [

#     {**p, 
#     'preco': aumentar_dez_porcento(p['preco'])} 
#     for p in produtos

# ]
def muda_preco(produto):
    return {
        **produto, #repete tudo como era
        'preco': aumentar_dez_porcento(produto['preco']) # muda só o preco.
    }

novos_produtos = map(
    muda_preco,
    produtos
)
novos_produtos_gen = (x for x in produtos)


print_inter(produtos)
print_inter(novos_produtos)

print(novos_produtos) #map object
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__')) #como as duas sao TRUE confirma que MAP é um iterator.
print(isinstance(novos_produtos_gen, GeneratorType)) #true
print(isinstance(novos_produtos, GeneratorType)) #como as duas sao TRUE confirma que MAP é um iterator.
#false.

#reexplicando: 
print(
    list(map(
        lambda x: x * 3,
        [1,2,3,4]

    ))
)