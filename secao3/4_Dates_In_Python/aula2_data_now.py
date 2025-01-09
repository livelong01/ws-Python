# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
# from pytz import timezone

# data = datetime(2024, 4, 20, 20, 3, 52, tzinfo=timezone('Europe/Lisbon'))

# data0 = datetime.now(timezone('Pacific/Apia'))
# data1 = datetime.now(timezone('Pacific/Honolulu'))
# data2 = datetime.now(timezone('Europe/Lisbon'))
# data3 = datetime.now(timezone('America/Sao_Paulo'))
# print(f'Pacifico Apia {data0}\nPacifico Hawai {data1}\nEuropa Lisbon \
# {data2}\n America Sao Paulo {data3}')
# print(data)  # Muda o formato ( sem indicar o timezone )

data6 = datetime.now()
print(data6.timestamp())

''' Explicacao de timeStamp:
É o numero de segundos de 1970 ate hoje,
assim facilita o calculo das horas e dias.
ex: ate hoje sao 1734263926.377846 segundos.
E daqui a 10 dias? Ele vai calcular o total de
segundos 10 x 24 x 60 x 60 = 864000 segundos.
ele soma o valor atual com os 864000 e descobre
a data do dia que será. De forma linear e sem
abusar da memoria e processamento do computador
com uma conta simples de soma.
'''
print(datetime.fromtimestamp(1734264100.903804))
# acima vemos o seg exato que eu fiz datetime.now()
print(datetime.fromtimestamp(1))
