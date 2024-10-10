'''while/else'''

string = 'valor qualquer'

i= 0
while i < len(string):
    letra = string[i]

    if letra ==' ':
        break

    print(letra)
    i += 1
else: 
    print('Não encontrei um espaço na String')
print('Fora do while.')