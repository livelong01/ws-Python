# Generator expression, itarables e iterators em PYTHON
#generator = (n for n in range(10000000))
# generator é uma funcao que sabe PAUSAR
#GENERATOR IS A FUNCTION THAT KNNOW STOP

def generator(n=0):
    yield 1 #PAUSAR
    print('continando...') # ele vai de yeld em yeld, pausando de onde parou.
    yield 2 #pause.
    print('mais uma vez ...')
    yield 3 
    print('Vou terminar')
    return 'Acabou' #ACABOU! #aparece no erro, pq esse é o ultimo elemneto da funcao.

# gen = generator(n=0)
# print(next(gen))#1
# print(next(gen)) #cotinuando...     
#                 #2
# print(next(gen)) #mais uma vez ...
#                 #3              
# print(next(gen)) #Vou terminar          
#                 #ERROR:  StopIteration: Acabou 

gen = generator (n=0)
for n in gen:
    print(n)
'''
1
continando...
2
mais uma vez ...
3
Vou terminar
'''

def generator(n=0, maximum = 10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return n


gen = generator()
for n in gen:
    print(n)

'''
0
1
2
3
4
5
6
7
8
9
'''

#pode usar como range tmb..
gen = generator(n = 5, maximum = 8)
for n in gen:
    print(n)

'''
5
6
7
8
'''

gen = generator(maximum = 1000000)
for n in gen:
    print(n)