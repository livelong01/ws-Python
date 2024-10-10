# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)

# print(lista)

#USANDO LIST COMPREENSION:

# lista =[1 for numero in range(10)] #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1] O q por na esquerda é oq  vai ser adc.
lista =[numero for numero in range(10)] # numero para cada numero no range de 10.
#Resulktado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista =[numero * 2
        for numero in range(10)]  #R: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(lista)