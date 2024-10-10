numeros = [[numero, numero**2] for numero in range(10)]
#FLAT É TIRAR O A LISTA DENTRO DA LISTA E POR ELA TUDO NO MESMO LUGAR.

flat = [y for x in numeros for y in x]

''' 
y é o q vai ser mostrado no final.
para cada x, p.e ([0,0]) em numeros
ele vai fazer outro for dentro desses dois numeros
ou seja, um for em [0,0], pegando cada um deles e jogando no 'y'
la na frente e assim vai fazendo..em tempo de execucao
ex:
[0,0,1,1,2,4...] e assim por diante, achatando a lista 
'''
# print(numeros)
print(flat)
#RESULTADO:
#[0, 0, 1, 1, 2, 4, 3, 9, 4, 16, 5, 25, 6, 36, 7, 49, 8, 64, 9, 81]