# Generator expression, itarables e iterators em PYTHON
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __iter__e__next

print(next(iterator)) # a unica coisa q o iterator sabe é o NEXT VALOR-
print(next(iterator)) 
print(next(iterator))

