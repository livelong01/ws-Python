# Generator expression, itarables e iterators em PYTHON
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__e__next

#all iterator is a generator, but um generator is not a iterator

generator = (n for n in range(1000000)) #aponta para memoria
lista = [n for n in range(1000000)] #ja usa a memoria (MAISPESADO)

print(sys.getsizeof(lista)) #85 kbites HEAVI!
print(sys.getsizeof(generator)) # 104 kbites light!

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator:
#     print(n)