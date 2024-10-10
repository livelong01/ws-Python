
'''
Introducao ao desempacotamento + tuples (tuplas)
'''
'''
Ele sincroniza as entradas com as vaiaveis criadas a partir da lista
e assim "desempacota" elas facilmente.
'''
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes

nome1, *resto = ['Maria', 'Helena', 'Luiz', 'jonathan']
print(nome1, resto) #Maria ['Helena', 'Luiz']

'''
Antes precisou criar uma variavel pra cada valor existente, 
agora ele pegou o valor desejado (nome1) e para nao precisar
criar uma variavel pra cada outro valor, ele pois um "*resto"
variavel que empacotou todos os outros valores. Veja o print. 
'''

_,_, nome, *_ = ['Maria', 'Helena', 'Luiz', 'jonathan'] # pega terceiro valor
print(nome) #pega o terceiro elemento.

'''
Programadores convencionaram que quando a variavel resto
nao vai ser utilizada, eles colocam um _(underline), para
indicar o nao uso dela.
'''