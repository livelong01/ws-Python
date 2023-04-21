a = 'AaaaA'
b = 'bbB'
c = 1.1

string = 'a = {} b= {} c= {:.2f}'
formato = string.format(a, b, c)
print(formato)

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
