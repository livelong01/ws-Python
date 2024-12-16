# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('10/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# print(data_fim > data_inicio)
# print(data_fim == data_inicio)
# print(data_fim < data_inicio)
# delta = data_fim - data_inicio
# print(delta.total_seconds())  # a diferença total em segundos
# print(delta.days, delta.seconds, delta.microseconds)  # diferença do q resta.

delta = timedelta(days=10, hours=2)  # VARIAVEL CONTENDO 10 dias
# (USADO PARA MANIPULACAO)

print(data_fim + delta)  # exemplo de uso
print(data_fim - delta)  # exemplo de uso

print(data_fim + relativedelta(seconds=60, minutes=10))
delta2 = relativedelta(data_fim, data_inicio)
# print(delta2) # mostra a diferença detalhada!
print(delta2.days, delta2.years)
