'''
NORMALMENTE, o while é usado com problemas que nós NÃO
sabemos o tamanho, um texto mt grande, quantas vezes sera
perguntado e reperguntado algo, etc. 
Quando se é SABIDO o tamanho ou quatd de repeticoes que
serao feitas, é mais comum usar o "FOR".
'''

# texto = 'Python'

# i= 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)
#     i+= 1

texto = 'python'

novo_texto = ''
for letra in texto: 
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

'''
o FOR itera cada letra por causa do "in", ou seja, 
ele passa de letra em letra usando o in e faz a acao. 
o tamanho da acao é o tamanho da string "texto". 
com isso conseguimos fazer a mesma coisa que o while, 
porem usando menos codigo.
'''
