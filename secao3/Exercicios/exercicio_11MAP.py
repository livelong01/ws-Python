'''
Exercício 1: Dobrar os números em uma lista
Dada uma lista de números inteiros, use map() para retornar uma nova lista com cada número dobrado.

Exemplo de entrada:
[5, 10, 15, 20]

Exemplo de saída:
[10, 20, 30, 40]
'''
print( list(map(
  lambda x : x * 2,
  [5, 10, 15, 20]
)))
#[10, 20, 30, 40]

'''
Exercício 2: Converter uma lista de strings para maiúsculas
Dada uma lista de strings, use map() para retornar uma nova lista com todas as palavras em letras maiúsculas.

Exemplo de entrada:
["python", "map", "função"]

Exemplo de saída:
["PYTHON", "MAP", "FUNÇÃO"]
'''

print(list(map(lambda x : x.upper(),
             ["python", "map", "função"])))
#['PYTHON', 'MAP', 'FUNÇÃO']

'''
Exercício 3: Obter o comprimento de cada palavra em uma lista
Dada uma lista de palavras, use map() para retornar uma lista com o comprimento de cada palavra.

Exemplo de entrada:
["gato", "cachorro", "elefante"]

Exemplo de saída:
[4, 8, 8]
'''

print(list(map(
    lambda x : len(x),
    ["gato", "cachorro", "elefante"]
)))
#[4, 8, 8]