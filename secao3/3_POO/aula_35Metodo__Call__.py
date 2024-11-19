#Metodo especial __call__
#callable é algo que pode ser executado com parenteses
# Em classes normais, __call__ faz a instancia de uma classe "callable"

from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    #definicao do metodo call, para poder chamar ele la em baixo
    def __call__(self, nome):
        print(nome, 'está chamando o ', self.phone, '...')
        return 1233

call1 = CallMe('92121546598')
call1('Jonathan') # da erro se tentar chamar sem o metodo call na classe.
retorno = call1('Jonathan')
print(retorno) # ele executou a acao do "print" e ainda deu um retorno "1233"

