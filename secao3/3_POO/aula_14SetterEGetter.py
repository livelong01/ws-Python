# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        #private, protected public [O _ SIGNIFCA PRIVADO OU PROTECTED SO PODE SER USADO NA CLASSE.]
        self._cor = cor #quando o atributo tiver "._cor" SIGNIFICA QUE NAO DEVE SER uTULIZADO
        self._cor_tampa = None

    @property
    def cor(self):
        # print('Property')
        return self._cor 
    
    @cor.setter #confirgurar o valor, mudar, etc.
    def cor(self, valor):

        # o setter pode ser usado para restricao de certas coisas, como no caso abaixo.
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor
    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter  
    def cor_tampa(self, valor):
        self._cor_tampa = valor



# def mostrar(caneta):
#     return caneta.cor

caneta = Caneta('Azul') 
# caneta.cor = 'Rosa' 
caneta.cor = 'preto' 

#getter -> obter um valor.
# mostrar(caneta) #como n printa, so executa a funcao e por isso o property aparece sozinho.
print(caneta.cor)

caneta.cor_tampa = 'vermelho'
print(caneta.cor)
print(caneta.cor_tampa)
