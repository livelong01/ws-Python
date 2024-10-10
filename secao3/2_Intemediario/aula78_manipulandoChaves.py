# Manipulando chaves e valores em dicionários


pessoa = {}


###
###
chave = 'nome'# usado para referenciar uma chave (chave dinamica.)

pessoa[chave] = 'Jonathan'
pessoa['sobrenome'] = 'Alonso'
print(pessoa[chave]) #com a vhave dinamica eu acesso o nome.
pessoa[chave] = 'Maria'
del pessoa['sobrenome']
print(pessoa)

# print(pessoa['nome1'])# KeyError: nome1 // ele identifica q tem erro na chave, pois ela n existe

'''
Aprendemos aqui um CRUD // Create (Criar), Read (Ler), Update (Atualizar) e Delete (Deletar)
pessoa[chave] = 'Jonathan' ## CRIAR
pessoa[chave] ## ler
pessoa[chave] = 'Maria' ## Atualizar
del pessoa['sobrenome'] ## DELETAR a chave.
'''

# print(pessoa.get('sobrenome', None)) #get n da erro, qd n encontrar uma chave.
# print(pessoa.get('sobrenome')) #get n da erro, qd n encontrar uma chave.
# print(pessoa.get('sobrenome', 'Não existe')) #Por padrao se usa "NONE"
if pessoa.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa['sobrenome'])