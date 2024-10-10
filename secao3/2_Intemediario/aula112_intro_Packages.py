
# print(__name__)
# from sys import path  # n serve pra nada...path n faz nada.

# # o correto seria:
# from aula112_package.modulo import soma # forma correta de importar um package!


# import aula112_package
# import aula112_package.modulo
# # print(*path, sep = '\n')

# #FORMA MELHOR, caminho curto!
# print(soma(3, 5))
# # ou 
# # FORMA RUIM, pois fica um caminho mt grande!
# print(aula112_package.modulo.soma(3, 5)) 

# #OU 

# from aula112_package import modulo
# # forma MEDIANA, puxa o modulo do pacote.
# print(modulo.soma(3, 5))

# # pessima pratica: 

from aula112_package.modulo import*
#IMPORTA TUDO, RISCO DE RENOMEAR FUNCOES E VARIAVEIS.
# NAO RECOMENDADO!

print(variavel) #Alguma coisa
print(soma(2,5)) #incluindo em modulo, no all ela n da mais erro.