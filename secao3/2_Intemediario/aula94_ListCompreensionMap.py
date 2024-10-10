# Mapeamento de dados em list comprehension:

produtos = [
    {'nome' : 'p1', 'preco': 20,},
    {'nome' : 'p2', 'preco': 10,},
    {'nome' : 'p3', 'preco': 30,},
]

#mapear essa lista usando msm nome, mas com preços diferentes.

# novos_produtos = [ # vai pegar o nome de cada produto e por na nova lista.
#     produto['nome']
#     for produto in produtos
# ]
# print(*novos_produtos, sep='\n')

# novos_produtos = [ # vai pegar o nome de cada preço.
#     produto['preco']
#     for produto in produtos
# ]
# print(*novos_produtos, sep='\n')

# novos_produtos = [ 
#     {'nome': produto['nome'], 'preco': produto['preco']}
#     for produto in produtos
# ]
# ''' RECRIOU O DICIONARIO E PODE FAZER MODIFICACOES PONTUAIS.
# resultado: 
# {'nome': 'p1', 'preco': 20}
# {'nome': 'p2', 'preco': 10}
# {'nome': 'p3', 'preco': 30}
# '''
# print(*novos_produtos, sep='\n')

#Se houver muitas variaveis, voce pode escolher qual quer trabalhar
# por exemplo: so o preço e o resto continua igual

novos_produtos = [ 
    {**produto, 'preco': produto['preco'] * 1.05}#produto empacotado, preço q vai ser alterado
    if produto['preco'] > 20 else {**produto} #pode usar um if, para aumentar preco somente se preco for maior que 20!
    #O if tem q ser depois da modificacao do preço, nunca antes.
    for produto in produtos #aumentar o preço de cada produto em 5%
]
'''
{'nome': 'p1', 'preco': 20}
{'nome': 'p2', 'preco': 10}
{'nome': 'p3', 'preco': 31.5} # foi O UNICO alterado!
'''
print(*novos_produtos, sep='\n')
