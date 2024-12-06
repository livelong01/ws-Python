# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

# Direcoes = enum.Enum('Direções', ['ESQUERDA', 'DIREITA']) #CRIANDO UMA CLASSE DA OUTRA FORMA.

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto() #1 Uusando o auto, vc n precisa enumerar manualmente.
    DIREITA = enum.auto() #2
    ACIMA = enum.auto() #3
    ABAIXO = enum.auto() #4

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) # trazem o MEMBRO, IGUAL!
print(Direcoes(1).name, Direcoes.ESQUERDA.value) # trazem o nome "ESQUERDA" e o valor "1"

def mover(direcao: Direcoes): #dando a funcao tipica dele.
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção invalida')
    print(f'Movendo para {direcao.name} ({direcao.value})') #assim fica bonito.


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)