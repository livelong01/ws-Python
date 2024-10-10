a = 'AaaaA'
b = 'bbB'
c = 1.15454

string = 'a = {} b= {} c= {:.2f}'
string2 = 'a = {1} b= {1} c= {2:.3f}' #usando o indice, que sempre começa no zero.
formato = string.format(a, b, c)
formato2 = string2.format(a, b, c)
print(formato)
print(formato2)

# OU AMBAS FUNCIONAM"""

formato = 'a = {} b= {} c= {}'.format(a, b, c)

print(formato)

## pode usar o indice para numerar e repetir variaveis
## comecam no 0 - 1 -2 -3 ...
### alem disso vc pode nomear as variaveis e criar paramentros
### parametro = nome3 nesse caso

string = 'a = {nome1} a = {nome1} a = {nome1} b= {nome2} c= {nome3:.2f}'
formato = string.format(nome1= a, nome2 = b, nome3 = c)
print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))