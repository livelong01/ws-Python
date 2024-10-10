import aula111_m


print(aula111_m.variavel)

for i in range(10):
    print(i)
    import aula111_m #singleton

''' SINGLETON
O modulo é singleton, pois ele so pode ser chamado
uma vez. Se tentar chamar ele outras vezes, nada acontece!
'''

print('FIM')

''' importlib 
caso vc queira recarregar um import novamente, POUCO USADO
mas caso queira... vc pode usar o Importlib. 
como baixo:
'''

import importlib

for i in range(10):
    print(i)
    importlib.reload(aula111_m)