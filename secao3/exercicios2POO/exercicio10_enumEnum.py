"""
Desafio
Crie um Enum chamado Cores que tenha as opções:

VERMELHO
AZUL
VERDE
Depois, escreva uma função chamada descrever_cor que recebe uma cor desse Enum e imprime algo como:

"Você escolheu a cor VERMELHO (1)".
Dicas:

Use enum.auto para os valores.
Verifique se o valor recebido é uma instância de Cores.
"""
import enum

class Cores(enum.Enum):
    VERMELHO = enum.auto()
    AZUL = enum.auto()
    VERDE = enum.auto()

def descrever_cor (cor:Cores):
    if not isinstance(cor, Cores):
        raise ValueError('Cor inválida.')
    if cor not in Cores:
        raise AttributeError('Use uma cor valida.')
    print(f'Você escolheu a cor {cor.name} ({cor.value})')

descrever_cor(Cores.AZUL)
descrever_cor(Cores.VERDE)
descrever_cor(Cores.VERMELHO)
# descrever_cor('amarela')
descrever_cor(Cores.AMARELA)