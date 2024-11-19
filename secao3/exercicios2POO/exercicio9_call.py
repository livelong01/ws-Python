'''
Exercício Proposto
Crie uma classe chamada ContadorDeChamadas que conte quantas vezes uma instância da classe foi chamada como uma função. A classe deve ter:

Um método __call__ que incrementa o contador e imprime o número atual de chamadas.
Um método reset() que redefine o contador para zero.
Exemplo de Como a Classe Deve Funcionar:

python

contador = ContadorDeChamadas()
contador()  # Deve imprimir "Esta é a chamada número 1"
contador()  # Deve imprimir "Esta é a chamada número 2"
contador.reset()  # Reseta o contador
contador()  # Deve imprimir "Esta é a chamada número 1" novamente
'''




class ContadorDeChamadas:
    def __init__(self, call_count = 0):
        self.call_count = call_count

    def __call__(self):
        self.call_count += 1
        print(f'Esta é a chamada número {self.call_count}')
    
    def reset(self):
        self.call_count = 0

contador = ContadorDeChamadas()
contador()
contador()
contador.reset()
contador()