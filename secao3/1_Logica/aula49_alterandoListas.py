"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
C.R.U.D == Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
# lista[2] = 300 #alterar valor na lista
# del lista[2] # deleta o valor 2(indice) da lista. 
'''
O valor e o tamanho da lista mudam ao usar o delete, 
nao apenas transforma o local em None, POR EXEMPLO.
Em lista, é melhor adc e retirar as coisas das pontas, 
do que do final, pois requer muito processamento, o python
reescreve toda a lista com as novas posicoes.
'''
# numero = lista[2]
# print(numero)
# print(lista)

lista.append(50)
lista.pop() # usando para remover o ULTIMO elemento, funciona com o indice tmb.
lista.append(60)##adc esses valores no FINAL da lista.
lista.append(70)
ultimo_valor = lista.pop(3) # remove o ITEm q tiver no indice 3 da lista.
# pop retorna o inteiro removido ( ele é inteiro se passar o mouse por cima.)
print(lista, 'Removido: ',ultimo_valor)

