#try, except, else e finally.



try:
    a = 18 
    b = 0
    c = a/b
    print('linha 2')

except ZeroDivisionError as e:
    print('dividiu por zero')
    print(e.__class__.__name__)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: # da pra por uma tupla e por mais de uma junto.
    print('Operador precisa ser um Inteiro/float')
    print('MSG:', error)
    print('MSG:', error.__class__.__name__)# aparece o nome do erro: "MSG: IndexError"
except Exception: #trata qualqer erro, classe superior dos erros.
    print('ERRO DESCONHECIDO')
''' except (TypeError, IndexError) as error
FAZENDO desse jeito vc descobre qual o erro, usando o "as error" E colocando
o erro na variavel "ERROR" e assim chamando ela de novo no PRINT.
'''


print( 'continuar')