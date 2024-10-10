"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.append('Jonathan')
nome = lista.pop()
lista.append(1233)
del lista[-1] # usar o "-1" para deletar o ultimo item da lista (indice negativo)
# lista.clear() # limpa a lista inteira!
lista.insert(0, 5) #(posicao no indice, "o que vai adc")
print(lista[4], nome) #cuidado ao acessar a indice maior q a lista.