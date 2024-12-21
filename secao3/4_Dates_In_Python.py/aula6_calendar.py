# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar
# print(calendar.calendar(2025))  # calendario do ano todo
# print(calendar.month(2025, 1))  # mostra o mes de janeiro de 2025
# mostra o dia da semana do primeiro dia e o ultimo dia do mes
print(calendar.monthrange(2025, 2))
numero_primeiro_dia, ultimo_dia = (calendar.monthrange(2025, 2))
print(list(enumerate(calendar.day_name)))
# [(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'),
# (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]

print(calendar.day_name[calendar.weekday(2025, 10, ultimo_dia)])

# print(calendar.monthcalendar(2025, 12))

for week in calendar.monthcalendar(2025, 12):
    for day in week:
        if day == 0:
            continue  # tira os dias que n sao do proprio mes.
        print(day)
