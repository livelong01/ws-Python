#Yield from

def gen1():
    print('comecou gen1')
    yield 1
    yield 2
    yield 3
    print('acabou gen1')

def gen2(gen):
    print('comecou gen2')
    yield from gen #continua aonde o gen1 parou. N REPETE. #tirei o () para ser executado dps.
    yield 4
    yield 5
    yield 6
    print('acabou gen2')


def gen3():
    print('comecou gen3')
    yield 10
    yield 20
    yield 30
    print('acabou gen3')


g1 = gen2(gen1()) #executar na hora por () na hora q quiser a execucao.
g2 = gen2(gen3())
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
