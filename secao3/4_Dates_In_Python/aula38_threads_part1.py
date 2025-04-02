# Threads, executando processos em paralelo.

'''
Normalmente ele funciona de forma linear, porem com Threads em paralelo, pode fazer mais de um ao msm tempo.
'''

from time import sleep

from threading import Thread
from threading import Lock
'''

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        time.sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()
t2 = MeuThread('Thread 2', 7)
t2.start()
t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    time.sleep(1)
'''

# print('Hello')

# for i in range(10):
#     print(i)
#     time.sleep(.5)

# print('World!')

'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo! 1', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo! 2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo! 3', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)'
'''

'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo! 1', 10))
t1.start()

# while t1.is_alive():
#     print('Esperando a thread')
#     sleep(2)

# outra forma é usar o Join, porem com o join nada aparece na tela até a execucao da thread ser realizada.

t1.join()

print('Thread acabou!')'

'''


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Voce comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
        ingressos.comprar(i)

    print(ingressos.estoque)
