'''
Escreva uma função que, usando reduce, retorne a soma de todos os números em uma lista.

Dica: Você vai precisar definir uma função lambda ou uma função que tome dois números e retorne a soma deles.

Exemplo:

python
Copiar código
soma_lista()
Resultado esperado: 15
'''
from functools import reduce

lista = [1, 2, 3, 4, 5]

total_soma = reduce(
    lambda ac, x : ac + x,
    lista,
    0
)
print(total_soma)

'''
Crie uma função que, usando reduce, retorne o produto de todos os números em uma lista.

Dica: O processo é parecido com a soma, mas agora você vai multiplicar os números.

Exemplo:

python
Copiar código
produto_lista([1, 2, 3, 4, 5])
Resultado esperado: 120
'''

total_produto = reduce(
    lambda ac, x: ac * x,
    lista,
    1 # tem q começar em 1, pq é produto.
)
print(total_produto)

'''
Exercício 3: Dicionário de frequência de palavras
Escreva uma função que recebe uma lista de palavras e usa reduce para criar um dicionário que contém a frequência de cada palavra.

Dica: O dicionário começa vazio e vai sendo preenchido à medida que você itera pelas palavras. Utilize reduce para acumular as frequências.

Exemplo:

python
Copiar código
contar_frequencia(['gato', 'cachorro', 'gato', 'pássaro', 'cachorro', 'gato'])
Resultado esperado: {'gato': 3, 'cachorro': 2, 'pássaro': 1}
'''
 

def contar_frequencia(lista):
    def atualiza_frequencia (freq_dict, palavra):
        freq_dict[palavra] = freq_dict.get(palavra,0) + 1 
        return freq_dict
    return reduce(atualiza_frequencia, lista, {})
    # return reduce(lambda freq_dict, palavra: {**freq_dict, palavra: freq_dict.get(palavra, 0) + 1}, palavras, {})
    #usando lambda fica mais complicado, n consigo entender 100%

print(contar_frequencia(['gato', 'cachorro', 'gato', 'cachorro', 'gato', 'pássaro', 'cachorro', 'gato']))

