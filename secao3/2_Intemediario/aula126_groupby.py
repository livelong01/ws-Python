# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key = ordena)
for aluno in alunos_agrupados:
    print(aluno)
print('----------------------')
grupos = groupby(alunos_agrupados, key = ordena )
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# alunos = ['a','a','a', 'b', 'c','a'] #usar SORTED para realinhar, pq o groupby n ordena.
# grupos = groupby(sorted(alunos))
# #print(grupos) #<itertools.groupby object at 0x00000160C3E94BD0> o print é um iterator

# for chave ,grupo in grupos:
#     print(chave)
#     print(list(grupo))


