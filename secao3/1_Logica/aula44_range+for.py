'''
FOR + RANGE
Range - > range (start, stop, step)
range e for sao independentes-
'''
numeros = range(-1,-10, -2) #qd so adc 1 valor, ele se torna o end , ou seja vai de 0 - 10 (o valor acdc)
# numeros = range(5,10) # em pyhton o ultimo valor n é incluido 0-9 nesse caso.
# numeros = range(5,1,2) # em pyhton o ultimo valor n é incluido 0-9 nesse caso.
# print(numeros[5]) # o indice e o numeo sao os mesmos.

for numero in numeros:
    print(numero)

