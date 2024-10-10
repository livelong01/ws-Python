# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# print(sys.platform) #win32 sistema operacional.
# # sys.exit()
# # print(123) #n executa.
# platform = 'A MINHA'
# print(sys.platform) # pra proteger o nome platform ... por exemp.
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform # mais de um dividir por virgulas.
# exit() # nada abaixo executa!
# platform = 'A MINHA' #sobreescreve a platform do sys. !CUIDADO!
# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s # MUDA O NOME Do modulo! apelido!

# sys = 'alguma coisa' #perde o modulo, sobreescreveu sys.
# print(s.platform) #win32
# print(sys) #alguma coisa


# alias 2 - from nome_modulo import objeto as apelido
from sys import platform as pf, exit as ex # renomear/apelida os nomes chamados no modulo. 
#entao: 
print(pf) #win32
ex() #exit no codigo!
print('ola')

# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import * #má pratica, importar TUDO!
'''
O sys usa o nome de varias variaveis e voce nao sabe o nome de todas
com isso vc pode acabar reescrevendo o nome de variaveis e perdendo o
acesso a aquela funcao que ela faz, criando uma grande BAGUNÇA!
'''
print(platform)
exit()

# from sys import exit, platform # melhor pratica, importar apenas o que vai USAR!
