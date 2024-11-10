# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.

#ex: 

# with open('aula_31contextManager.txt', 'w') as arquivo:
#     ...

class MyOpen: 
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo Arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding = 'utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
           print('Fechando Arquivo')
           self._arquivo.close()

instancia = MyOpen('aula_31contextManager.txt', 'w')

with instancia as arquivo: #O retorno do __enter__ vai para A VARIAVEL "alguma_coisa"
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
    print('WITH', arquivo)

''' Aula sobre a criação de um Context Manager
que é basicamente um abridor, editor e fechador de arquivo
feito por voce mesmo. Isso ajuda a personalizar um desses de acordo
com o que voce precisa, criando algumas configuracoes importantes
que seu programa precisa, na hora de imprimir o resultado.

'''