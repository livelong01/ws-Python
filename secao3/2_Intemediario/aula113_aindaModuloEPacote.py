print(__name__)

from aula112_package.modulo import fala_oi

fala_oi() # agora ele funciona, pq mudei la no modulo, 
#na pasta, e mostrei o caminho da importacao de 
# fala_oi do modulo_b, para o modulo.

from sys import exit
print('Jonathan')
exit()
print('Jonathan')

'''
TODAS AS IMPORTACOES QUE VC FIZER NO SEU PROGRAMA
ELAS TEM QUE SER "RELATIVAS" AO PONTO DE VISTA 
DO SEU "MAIN". E TODOS OS OUTROS Q TIVEREM DENTRO
DE PASTAS E DENTRO DE OUTROS MODULOS, VOCE PRECISA
FAZER TODO O CAMINHO PARA QUE ELE ENTENDA DE ONDE
VEM A FUNCAO OU VARIAVEL, ETC Q VC TA IMPORTANDO.
'''