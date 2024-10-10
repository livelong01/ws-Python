# Empacotamento e desempacotamento de dicionários
a, b = 1, 2 # a = 1 , b = 2
a, b = b, a #inverte isso - a = 2, b = 1
# print(a, b)

# pessoa = {
#     'nome' : 'Aline',
#     'sobrenome': 'Souza'
# }

# # a, b = pessoa
# print(a, b) #nome sobrenome && dão as CHAVES

# a, b = pessoa.values()
# print(a, b) #Aline Souza && desempacota!

# a, b = pessoa.items()
# print(a, b) #('nome', 'Aline') ('sobrenome', 'Souza') tupla com nome e sobrenome

# #para desempacotar o ITEMS.
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)  ##nome Aline 
# print(b1, b2) ## sobrenome Souza

# #ISSO É A MSM COISA QUE: 

# for chave, valor in pessoa.items(): #para pegar so o valor, podia printar apenas "valor"
#     print(chave, valor) #nome Aline
#                         ##sobrenome Souza
pessoa = {
    'nome' : 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade' : 16,
    'altura': 1.60,
}

pessoa_completa = {**pessoa, 'nome': 1} # adc uma chave com valor 1.
pessoa_completa = {**pessoa, **dados_pessoa} #JUNTA OS DOIS DICS em 1.
# acima temos um desempacotamento de dicionarios.



# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): #FUNCAO mostra todas as chaves e valores de dicionarios 
    print('Não NOMEADOS: ', args) 
    for chave, valor in kwargs.items():
        print(chave, valor)

#Não NOMEADOS:  (1, 2)
# nome joana // NOMEADOS
# qlq 123

'''
Args sao NÃO nomeados, ou seja, valores que passamos sem dar nome, como abaixo: 1, 2.
enquando kwargs, sao os nomeados, como: "nome", "qlq". Logo, os prints vem separados.
'''

# mostro_argumentos_nomeados(1, 2 , nome= 'joana', qlq = 123) #EMPACOTANDO , criando dicionario
mostro_argumentos_nomeados(**pessoa_completa) #desempacotar tira as variaveis do dicionario feito
'''
Não NOMEADOS:  ()
nome Aline
sobrenome Souza
idade 16
altura 1.6
'''