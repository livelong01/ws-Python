# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# print('Este módulo se chama', __name__) #Este módulo se chama __main__

# import aula110_m

# print('Este modulo se chama',__name__)

import aula110_m
from aula110_m import soma, variavel_modulo

# print(aula110_m.variavel_modulo)
print(variavel_modulo) # agora ja uso direto a variavel
# do outro modulo.

print(soma(8,7))
# OU
print(aula110_m.soma(8,7))