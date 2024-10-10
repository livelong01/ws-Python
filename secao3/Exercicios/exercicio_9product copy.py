#Exercício 1: Dada uma lista de tamanhos de roupas ['P', 'M', 'G'] e uma lista de cores ['Azul', 'Vermelho'], 
# gere todas as combinações possíveis de tamanho e cor de roupas.

from itertools import product

# lista_tamanhos = ['P', 'M', 'G']
# lista_cores = ['Azul', 'Vermelho']

# lista_possibilidades = list(product(lista_tamanhos, lista_cores))

# print(*lista_possibilidades, sep= '\n')

#Exercício 2: Imagine que você tem dois dados: um com números de 1 a 6 e outro com as letras ['A', 'B', 'C'].
#  Gere todos os resultados possíveis que podem ser obtidos ao rolar os dois dados juntos.




listas = [
    [1,2,3,4,5,6],
    ['A', 'B', 'C'],
    ['verde', 'amarelo'],
]

print(*list(product(*listas)), sep= '\n')



#Exercício 3: Dado que você tem duas listas de frutas ['Maçã', 'Banana'] e ['Uva', 'Laranja'],
#  gere todas as combinações possíveis de uma fruta de cada lista.

