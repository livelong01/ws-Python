# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding= 'utf8')
        yield arquivo
    # except Exception as e:
    #     print('Ocorreu erro', e ) #nao trata o erro
    finally:
        print('fechando arquivo')
        arquivo.close()

with my_open('aula_32.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n', 123)
    arquivo.write('Linha3\n')
    print('With', arquivo)

''' Outra forma de fazer um COntext Manager
dessa forma vc consegue criar um context manager usando funcoes
a unica providencia que se deve ser tomada é decorar com o
@contextManager A FUNCAO que vai abrir e fechar o arquivo. (o context manager)
assim ele vai funcionar, alem disso, tem que tratar o erro, no caso acima
usando o except e o finally, que mesmo com erro fecha o arquivo.

'''