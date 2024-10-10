'''
Iterando strings com while.
'''
#.......01234567 indice.
nome = "Jonathan" # iteraveis

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string =''
contador = 0
while  contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'
    contador += 1

print(nova_string)