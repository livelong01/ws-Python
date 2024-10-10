#try, except, else e finally.

try:
    print('Abrir o arquivo')
    8/0
    #open ... tentando abrir um arquivo.
except ZeroDivisionError:
    print('dividiu zero.')
else: # se o codigo NAO der erro, executa o else.
    print('não deu erro.') 
finally: # sempre vai ser executado, mesmo com erro.
    print('Fechar o arquivo') #mesmo assim isso é executado, mesmo com erro.


    '''A unica coisa que nao pode:
    é um TRY sozinho.
    mas o restante pode tudo.
    
    '''

# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')