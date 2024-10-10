'''
Exercício 1: Dada uma lista de 4 alunos ['Maria', 'João', 'Ana', 'Pedro'], 
gere todas as permutações possíveis de 2 alunos e determine quantas maneiras diferentes eles podem se sentar em uma mesa de 2 lugares.
'''
from itertools import permutations, count

# alunos =  ['Maria', 'João', 'Ana', 'Pedro']

# permutations_alunos = list(permutations(alunos, 2))
# print(*permutations_alunos, sep= '\n') # o asteristico ajuda  organizar um em cima do outro.

#------------------------
#Exercício 2: Dada uma senha de 3 caracteres alfanuméricos ['A', 'B', '1'],
#  gere todas as permutações possíveis dessa senha para testar combinações.

caracteres = ['A', 'B', '1', 'C', '3', '2', 'j']

combinacoes = list(permutations(caracteres))
senha =''
def possiveis_senhas(lista):
    senha = [''.join(senha) for senha in lista]
    return senha




x = 0
for senha in combinacoes:
    senha = ''.join(senha)

    x += 1
    if senha != 'A1B32Cj':
        print('errado')
    else:   
        print('Correto!', 'senha: ', senha, x)
        print()
        break

#--------------------------------
#Exercício 3: Um restaurante deseja reorganizar a sequência de 3 pratos principais ['Frango', 'Peixe', 'Carne']. 
# Gere todas as permutações possíveis para que eles possam testar diferentes cardápios.
ingredientes = ['Frango', 'Peixe', 'Carne']
print(*list(permutations(ingredientes)), sep = '\n')
