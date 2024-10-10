# Operadores in e not in / estar entre e nao estar entre
# Strings são """iteráveis"""
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio' # cada letra ou numero esta num espaço especifico

# nome = 'Otávio'
# print(nome[2]) # Mesma letra do indice. "á" (ind. positivo)
# print(nome[-4]) # Mesma letra do indice. "á" (ind. negativo)
# print('á' in nome) # Se tiver essa letra "á" retorna TRUE
# print('z' in nome) # Se tiver essa letra "z" retorna FALSE
# print('vio' not in nome) # Se tiver esse trcho "vio" retorna FALSE (por cauisa do not, que inverte)
# print('zero' not in nome) # true.

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} estar em {nome}')
else:
    print(f'{encontrar} não estar em {nome}')


numero = str(123456) # nao funciona com numeros, para isso tem q converter pra srt
print(numero[0])