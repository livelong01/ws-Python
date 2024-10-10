# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome' : 'Joninho',
    'sobrenome': 'Alonsoooo1',
    'idade': '90',

}

# print(len(pessoa)) #5
# print(tuple(pessoa.keys())[2]) # converte em tupla e chama o terceiro key (sobrenome1)
# print(list(pessoa.values())) #valores das keys em ordem.

# for chave in pessoa:
#     print(chave)
    #nome
    #sobrenome        #só as chaves.

# for values in pessoa.values():
#     print(values) 
    # Joninho
    # Alonsoooo1      # só os valçores

# print(list(pessoa.items())) #[('nome', 'Joninho'), ('sobrenome', 'Alonsoooo1')]
 

# for chave, valor in pessoa.items():
#     print(chave, valor)
    #nome Joninho
    #sobrenome Alonsoooo1   #chave e valor.

pessoa.setdefault('idade', None) #isso protege contra erros. Se a key n existir (agora, pode ser q venha a existir.)Ele retorna None e n executa a de baixo.
print(pessoa['idade']) #Só execuyta se a chave existir.

