#Exercício 1: Dado o dicionário de alunos com suas respectivas notas
from itertools import groupby
alunos = [{'nome': 'Maria', 'nota': 'A'},
           {'nome': 'João', 'nota': 'B'}, 
           {'nome': 'Ana', 'nota': 'A'}, 
           {'nome': 'Pedro', 'nota': 'C'}]


# alunos_agrupados = sorted(alunos, key = lambda a: a['nota']) #O lambda é uma FUNCAO que só vai ser usada uma unica VEZ.

def ordenar(aluno): # se for usar uma funcao mais vezes, faça desse jeito. nomeando
    return aluno['nota'] #VAI USAR A NOTA COMO OBJETIVO DE ORDENACAO.

alunos_agrupados = sorted(alunos, key = ordenar) # usou sorted pq faz copia rasa, pq se usar "amigos.sort" vc modifica a ORIGINAL!

grupos = groupby(alunos_agrupados, key = ordenar ) # VAI CRIAR GRUPOS USANDO A NOTA COMO KEY!

for chave, grupo in grupos:
    print(chave) #notas a key vai ser a nota por causa do groupby
    for aluno in grupo:
        print(aluno) #alunos
print('-----------------------------')
#Exercício 2: Dado o dicionário de pessoas com suas idades:  Agrupe as pessoas pela idade.

pessoas = [{'nome': 'Lucas', 'idade': 30},
            {'nome': 'Larissa', 'idade': 25}, 
            {'nome': 'Paulo', 'idade': 30}, 
            {'nome': 'Ana', 'idade': 25}]

def ordenar_idade(dict):
    return dict['idade']

pessoas_agrupadas = sorted(pessoas, key = ordenar_idade) #ordena

grupos_idade = groupby(pessoas_agrupadas, key = ordenar_idade) #agrupar

for chave, grupos in grupos_idade:
    print(chave)
    for idade in grupos:
        print(idade)

#Exercício 3: Dado o dicionário de produtos com suas respectivas categorias: Agrupe os produtos por categoria.

produtos = [{'produto': 'Camiseta', 'categoria': 'Vestuário'}, 
            {'produto': 'Calça', 'categoria': 'Vestuário'}, 
            {'produto': 'Sapato', 'categoria': 'Acessório'},
            {'produto': 'Boné', 'categoria': 'Acessório'}]

def ordenar3(criterio):
    return criterio['categoria']

categoria_ordenada = sorted(produtos, key = ordenar3)
grupo_ordenado = groupby(categoria_ordenada, key = ordenar3)

for chave, grupo in grupo_ordenado:
    print(chave)
    for produto in grupo:
        print(produto)

