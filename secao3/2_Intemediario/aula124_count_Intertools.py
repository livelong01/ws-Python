# count é um iterador sem fim
from itertools import count
c1 = count(start = 8, step = 8) #multiplos de 8
r1 = range(8, 100, 8) #multiplo de 8
print(c1)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__')) # ele é i

for i in c1:
    print(i)
#     if i >= 100:
#         break

# for i in r1:
#     print(i)
#     if i >= 100000:
#         break