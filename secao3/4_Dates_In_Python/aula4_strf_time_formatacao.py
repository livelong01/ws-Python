# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')


print(data.strftime(fmt))  # formata a data para a brasileira.
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # Hora , min e seg.
print(data.strftime('%d/%m/%Y %H:%M'))  # MIN e hora.
print(data.strftime('%Y'), data.year)  # só o ano. (str e int)
print(data.strftime('%d'), data.day)  # só o dia. (str e int)
print(data.strftime('%m'), data.month)  # só o mes. (str e int)
print(data.strftime('%H'), data.hour)  # só o hora. (str e int)
print(data.strftime('%M'), data.minute)  # só o min. (str e int)
print(data.strftime('%S'), data.second)  # só o seg. (str e int)
print()

print(type(data.strftime('%Y')))  # TIPO STR!
print(type(data.second))  # TIPO INT!

'''
13 13
12 12
07 7
59 59
23 23
'''
