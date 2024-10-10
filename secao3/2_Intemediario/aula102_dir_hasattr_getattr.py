#dir, hasattr e getattr em python

string = 'jonathan'

# print(string)
# print(dir(string)) ## dir mostra todos os metodos
#possiveis numa variavel... ex: str > upper()...

# if hasattr(string, 'upper'):
#     print('Existe upper')
#     print(string.upper())
    
    #se eu qiser por o nome de um metodo
    #em uma variavel, eu posso fazzer assim: (GETATTR)


metodo = 'upper'
if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)()) #JONATHAN
    print(string.upper())
else: 
    print('Nao existe o metodo', metodo)