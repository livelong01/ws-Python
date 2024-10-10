#1:Exercício 1: Dada uma lista de nomes de produtos ['Camiseta', 'Calça', 'Sapato', 'Boné', 'Óculos'], 
# gere todas as combinações possíveis de 2 produtos que podem ser comprados juntos.

# roupas = ['Camiseta', 'Calça', 'Sapato', 'Boné', 'Óculos']

from itertools import combinations

def print_comb(iter):
    return print(*list(iter), sep= '\n')

# #1
# print_comb(combinations(roupas, 2 ))

#Dada uma lista de números [1, 2, 3, 4, 5], 
# gere todas as combinações possíveis de 3 números. Depois, calcule a soma de cada uma dessas combinações.


#2
def sum_list(list):
    x = [f'\n Valor da soma: {sum(valor)}' for valor in list]
    return x

# numbers = [1, 2, 3, 4, 5]
# print_comb(combinations(numbers, 3))
# print_comb(sum_list(combinations(numbers, 3)))

#Resposta do chatgpt
numeros = [1, 2, 3, 4, 5]
comb_numeros = list(combinations(numeros, 3))
soma_combinacoes = [sum(c) for c in comb_numeros]
print(soma_combinacoes)

#Exercício 3: Suponha que você tem uma lista de três letras ['A', 'B', 'C']. 
# Gere todas as combinações possíveis de 2 letras e apresente-as em pares.

lethers = ['A', 'B', 'C']

print_comb(combinations(lethers, 2))
