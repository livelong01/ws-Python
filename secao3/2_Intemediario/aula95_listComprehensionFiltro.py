# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint 

produtos = [
    {'nome' : 'p1', 'preco': 20,},
    {'nome' : 'p2', 'preco': 10,},
    {'nome' : 'p3', 'preco': 30,},
]

# filtro, faz as mesmas coisas que o map
#porem ele separa certas informacoes, nao
#mostra tudo.

#para n digitar isso toda vez:
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# print(produtos) # feio e desorganizado
# p(produtos) # mais bem organizado e bom  de ver.

'''
O que vem na esquerda do for é mapeamento.
o que vem na direita do for é filtro! 

'''

# lista = [n for n in range(10) 
#          if n < 5] #[0, 1, 2, 3, 4]
produtos = [
    {'nome' : 'p1', 'preco': 20,},
    {'nome' : 'p2', 'preco': 10,},
    {'nome' : 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05} ##MAP
    if produto['preco'] > 20 else {**produto}##MAP
    for produto in produtos # for iterador!
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 #filtro, ele só mostra os preços maiores q 10 **atualizados
] 

# print(novos_produtos)
p(novos_produtos)
''' RESULTADO: 
[{'nome': 'p1', 'preco': 20},
 {'nome': 'p3', 'preco': 31.5}]

ele manteve os outros produtos inalterados que fossem menor que 20 e 
multiplicou em 5% os que eram maior q 20.  !!!MAP!!!
além disso, só mostrou os produtos com preco maior que 10,
!!!!filtro!!!.

MAP == FAZ COISAS com as variaveis DE ACORDO COM UM CRITERIO.
FILTRO == FILTRA, SELECIONA, AS VARIAVEIS QUE VAO APARECER USANDO UM CRITERIO.
'''
