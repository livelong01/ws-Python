lista =[]
for x in range(3):
    for y in range(3):
        lista.append((x,y))

nova_lista = [
    (x, y)  #o que vai aparecer na lista
    for x in range(3) #o que vc vai mudar
    for y in range(3) #o que vc vai mudar

]
nova_lista_2 = [
    [(x, letra) for letra in 'Luiz']  #o que vai aparecer na lista
    for x in range(3) #o que vc vai mudar

]

# print(lista) #sao iguais.
# print(nova_lista)

print(nova_lista_2)